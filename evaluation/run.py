"""Retrieval evaluation harness (RAG_V1_SPEC.md, Step 9).

    python -m evaluation.run --questions evaluation/questions.jsonl \
        [--chunk-size N --chunk-overlap N --top-k N] [--with-llm]

Without --with-llm it makes no LLM calls, so the numbers are deterministic.
"""
import argparse
import hashlib
import json
import sys
from datetime import datetime, timezone
from pathlib import Path

from app import rag
from app.config import CORPUS_DIR, GEMINI_MODEL, load_settings, validate_settings

RESULTS_DIR = Path(__file__).resolve().parent / "results"
MANIFEST_FILE = CORPUS_DIR / "forest" / "MANIFEST.json"
# [DECISION D17] A chunk is a hit if it covers at least this share of the evidence span
MIN_COVERAGE = 0.5


def load_questions(path):
    with open(path, "r", encoding="utf-8") as f:
        return [json.loads(line) for line in f if line.strip()]


def locate_evidence(questions):
    """[DECISION D17] Character span of each evidence quote, found as an exact substring of
    its file, so hits don't depend on chunking. Fails loudly on any quote that is missing
    or appears more than once."""
    problems = []
    for question in questions:
        answerable = question["type"] != "unanswerable"
        if answerable != bool(question["evidence"]):
            problems.append(f"{question['id']}: type {question['type']!r} but "
                            f"{'no' if answerable else 'some'} evidence")
        for evidence in question["evidence"]:
            quote = evidence["quote"]
            try:
                text = rag.read_document(rag.doc_path(evidence["doc_id"]))
            except rag.RagError:
                problems.append(f"{question['id']}: document not found: {evidence['doc_id']} (quote: {quote!r})")
                continue
            count = text.count(quote)
            if count != 1:
                problems.append(f"{question['id']}: quote found {count} times in {evidence['doc_id']}: {quote!r}")
                continue
            start = text.find(quote)
            evidence["span"] = (start, start + len(quote))
    if problems:
        sys.exit("Evidence check failed:\n" + "\n".join(f"  - {problem}" for problem in problems))


def forest_hashes():
    return {f"forest/{path.name}": rag.file_sha256(path)
            for path in sorted((CORPUS_DIR / "forest").glob("*.md"))}


def corpus_check(hashes):
    """Compare corpus/forest/ with MANIFEST.json; any difference makes runs incomparable."""
    with open(MANIFEST_FILE, "r", encoding="utf-8") as f:
        manifest = {entry["doc_id"]: entry["sha256"] for entry in json.load(f)["files"]}
    return {"added": sorted(hashes.keys() - manifest.keys()),
            "deleted": sorted(manifest.keys() - hashes.keys()),
            "changed": sorted(doc_id for doc_id in hashes.keys() & manifest.keys()
                              if hashes[doc_id] != manifest[doc_id])}


def evaluate(question, doc_ids, settings):
    chunks = rag.retrieve(question["question"], doc_ids, settings)
    retrieved = [{"rank": rank, "chunk_id": chunk["id"], "doc_id": chunk["metadata"]["doc_id"],
                  "char_start": chunk["metadata"]["char_start"], "char_end": chunk["metadata"]["char_end"]}
                 for rank, chunk in enumerate(chunks, 1)]
    evidence = []
    for item in question["evidence"]:
        start, end = item["span"]
        hit_ranks = [chunk["rank"] for chunk in retrieved
                     if chunk["doc_id"] == item["doc_id"]
                     and min(end, chunk["char_end"]) - max(start, chunk["char_start"]) >= MIN_COVERAGE * (end - start)]
        evidence.append({"doc_id": item["doc_id"], "char_start": start, "char_end": end, "hit_ranks": hit_ranks})
    first_hits = [item["hit_ranks"][0] for item in evidence if item["hit_ranks"]]
    return {"id": question["id"], "type": question["type"], "retrieved": retrieved, "evidence": evidence,
            "first_hit_rank": min(first_hits) if first_hits else None,
            "all_evidence_hit": bool(evidence) and all(item["hit_ranks"] for item in evidence)}


def metrics(results):
    """[DECISION D18] hit@k, all@k and MRR over answerable questions."""
    n = len(results)
    return {"n": n,
            "hit_at_k": sum(result["first_hit_rank"] is not None for result in results) / n,
            "all_at_k": sum(result["all_evidence_hit"] for result in results) / n,
            "mrr": sum(1 / result["first_hit_rank"] for result in results if result["first_hit_rank"]) / n}


def main():
    parser = argparse.ArgumentParser(description="Retrieval evaluation: hit@k, all@k, MRR.")
    parser.add_argument("--questions", required=True, type=Path)
    parser.add_argument("--chunk-size", type=int)
    parser.add_argument("--chunk-overlap", type=int)
    parser.add_argument("--top-k", type=int)
    parser.add_argument("--with-llm", action="store_true",
                        help="also run the full /api/ask logic for every question (costs API calls)")
    args = parser.parse_args()

    # Default: the current data/settings.json
    settings = load_settings()
    for key, value in [("chunk_size", args.chunk_size), ("chunk_overlap", args.chunk_overlap),
                       ("top_k", args.top_k)]:
        if value is not None:
            settings[key] = value
    try:
        settings = validate_settings(settings)
    except ValueError as error:
        parser.error(str(error))

    questions = load_questions(args.questions)
    if not questions:
        sys.exit(f"No questions in {args.questions}")
    locate_evidence(questions)

    hashes = forest_hashes()
    check = corpus_check(hashes)
    if any(check.values()):
        print(f"WARNING: corpus/forest/ no longer matches MANIFEST.json ({len(check['added'])} added, "
              f"{len(check['deleted'])} deleted, {len(check['changed'])} changed). "
              "These numbers are not comparable with runs on the original snapshot.")
    fingerprint = hashlib.sha256(
        "\n".join(f"{doc_id}:{sha256}" for doc_id, sha256 in sorted(hashes.items())).encode()).hexdigest()

    results = []
    for question in questions:
        # doc_ids null means the whole snapshot, corpus/forest/ (uploads are not part of it)
        doc_ids = question.get("doc_ids") or sorted(hashes)
        result = evaluate(question, doc_ids, settings)
        if args.with_llm:
            response = rag.ask(question["question"], doc_ids, settings)
            result.update(status=response.status, answer=response.answer,
                          error=response.error.code if response.error else None)
        results.append(result)

    answerable = [result for result in results if result["evidence"]]
    unanswerable = [result for result in results if not result["evidence"]]
    summary = {}
    if answerable:
        summary["all"] = metrics(answerable)
        for kind in sorted({result["type"] for result in answerable}):
            summary[kind] = metrics([result for result in answerable if result["type"] == kind])
    summary["unanswerable"] = {"n": len(unanswerable)}
    if args.with_llm and unanswerable:
        summary["unanswerable"]["not_found_share"] = (
            sum(result["status"] == "not_found" for result in unanswerable) / len(unanswerable))
        summary["unanswerable"]["llm_errors"] = sum(result["status"] == "error" for result in unanswerable)

    print(f"\nchunk_size={settings['chunk_size']} chunk_overlap={settings['chunk_overlap']} "
          f"top_k={settings['top_k']} embedding={rag.EMBEDDING_MODEL}")
    print(f"{'type':<14}{'n':>4}{'hit@k':>8}{'all@k':>8}{'MRR':>8}")
    for kind, values in summary.items():
        if kind != "unanswerable":
            print(f"{kind:<14}{values['n']:>4}{values['hit_at_k']:>8.3f}"
                  f"{values['all_at_k']:>8.3f}{values['mrr']:>8.3f}")
    line = f"unanswerable: {summary['unanswerable']['n']}"
    if "not_found_share" in summary["unanswerable"]:
        line += (f", returned not_found: {summary['unanswerable']['not_found_share']:.0%}"
                 f", LLM errors: {summary['unanswerable']['llm_errors']}")
    print(line)

    RESULTS_DIR.mkdir(exist_ok=True)
    stamp = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")
    out = RESULTS_DIR / (f"{stamp}_cs{settings['chunk_size']}_ov{settings['chunk_overlap']}"
                         f"_k{settings['top_k']}.json")
    report = {"config": {**settings, "embedding_model": rag.EMBEDDING_MODEL,
                         "llm_model": GEMINI_MODEL if args.with_llm else None},
              "questions_sha256": hashlib.sha256(args.questions.read_bytes()).hexdigest(),
              "corpus_fingerprint": fingerprint,
              "corpus_check": {"matches_manifest": not any(check.values()), **check},
              "metrics": summary,
              "questions": results}
    out.write_text(json.dumps(report, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    print(f"Results: {out}")


if __name__ == "__main__":
    main()