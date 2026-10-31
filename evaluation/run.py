"""Retrieval evaluation harness (RAG_V1_SPEC.md Step 9, RAG_V2_SPEC.md Steps 3-4).

    python -m evaluation.run --questions evaluation/questions/kestrel.jsonl --corpus kestrel \
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
from app.words import corpus_doc_ids

RESULTS_DIR = Path(__file__).resolve().parent / "results"
# [DECISION D17] A chunk is a hit if it covers at least this share of the evidence span
MIN_COVERAGE = 0.5
# [DECISION D23] Metrics at k read the first k chunks of one top-10 ranking
EVAL_KS = (1, 3, 5, 10)
COLUMNS = [f"{name}@{k}" for name in ("hit", "all") for k in EVAL_KS] + ["mrr"]
REQUIRED_FIELDS = ("id", "question", "type", "answerable", "evidence", "expected_answer")


def load_questions(path, corpus):
    """[DECISION D22] Kestrel format. Evidence names a bare file in `source`, so the
    doc_id is <corpus>/<source>. The file itself is never rewritten."""
    path = Path(path)
    questions = []
    with open(path, "r", encoding="utf-8") as f:
        for number, line in enumerate(f, 1):
            if not line.strip():
                continue
            try:
                question = json.loads(line)
                for field in REQUIRED_FIELDS:
                    question[field]
                for evidence in question["evidence"]:
                    evidence["quote"]
                    evidence["doc_id"] = f"{corpus}/{evidence['source']}"
            except (ValueError, KeyError, TypeError):
                raise rag.RagError("invalid_question_set",
                                   f"Invalid question set {path.stem}, line {number}.") from None
            questions.append(question)
    return questions


def locate_evidence(questions):
    """[DECISION D17] Character span of each evidence quote, found as an exact substring of
    its file, so hits don't depend on chunking. Fails loudly on any quote that is missing
    or appears more than once."""
    problems = []
    for question in questions:
        answerable = question["answerable"]
        if answerable != bool(question["evidence"]):
            problems.append(f"{question['id']}: answerable is {answerable} but "
                            f"{'no' if answerable else 'some'} evidence")
        for evidence in question["evidence"]:
            quote = evidence["quote"]
            try:
                text = rag.read_document(rag.doc_path(evidence["doc_id"]))
            except rag.RagError:
                problems.append(f"{question['id']}: {quote!r} (document not found: {evidence['doc_id']})")
                continue
            count = text.count(quote)
            if count != 1:
                found = "not found" if count == 0 else f"found {count} times"
                problems.append(f"{question['id']}: {quote!r} ({found})")
                continue
            start = text.find(quote)
            evidence["span"] = (start, start + len(quote))
    if problems:
        raise rag.RagError("evidence_check_failed", "Evidence check failed: " + "; ".join(problems))


def corpus_hashes(doc_ids):
    return {doc_id: rag.file_sha256(rag.doc_path(doc_id)) for doc_id in doc_ids}


def corpus_check(corpus, hashes):
    """Compare corpus/<corpus>/ with its MANIFEST.json, if it has one; any difference
    makes runs incomparable. Returns None when there is no manifest."""
    manifest_file = CORPUS_DIR / corpus / "MANIFEST.json"
    if not manifest_file.exists():
        return None
    with open(manifest_file, "r", encoding="utf-8") as f:
        manifest = {entry["doc_id"]: entry["sha256"] for entry in json.load(f)["files"]}
    return {"added": sorted(hashes.keys() - manifest.keys()),
            "deleted": sorted(manifest.keys() - hashes.keys()),
            "changed": sorted(doc_id for doc_id in hashes.keys() & manifest.keys()
                              if hashes[doc_id] != manifest[doc_id])}


def evaluate(question, doc_ids, settings):
    chunks = rag.retrieve(question["question"], doc_ids, {**settings, "top_k": max(EVAL_KS)})
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


def hit_at(result, k):
    return any(rank <= k for item in result["evidence"] for rank in item["hit_ranks"])


def all_at(result, k):
    return all(any(rank <= k for rank in item["hit_ranks"]) for item in result["evidence"])


def metrics(results):
    """[DECISION D18] [DECISION D23] hit@k, all@k and MRR over the answerable questions in
    results. With no answerable question, n is 0 and every metric is None."""
    answerable = [result for result in results if result["evidence"]]
    n = len(answerable)
    values = {"n": n, "unanswerable": len(results) - n}
    for k in EVAL_KS:
        values[f"hit@{k}"] = sum(hit_at(result, k) for result in answerable) / n if n else None
    for k in EVAL_KS:
        values[f"all@{k}"] = sum(all_at(result, k) for result in answerable) / n if n else None
    values["mrr"] = (sum(1 / result["first_hit_rank"] for result in answerable if result["first_hit_rank"]) / n
                     if n else None)
    return values


def run_eval(questions_path, corpus, settings, with_llm):
    """One evaluation run, shared by the CLI and POST /api/eval. Returns (results, results_path)."""
    questions_path = Path(questions_path)
    doc_ids = corpus_doc_ids(corpus)
    questions = load_questions(questions_path, corpus)
    if not questions:
        raise rag.RagError("empty_question_set")
    locate_evidence(questions)

    hashes = corpus_hashes(doc_ids)
    check = corpus_check(corpus, hashes)
    if check is None:
        print(f"corpus/{corpus}/ has no MANIFEST.json: corpus check skipped.")
    elif any(check.values()):
        print(f"WARNING: corpus/{corpus}/ no longer matches MANIFEST.json ({len(check['added'])} added, "
              f"{len(check['deleted'])} deleted, {len(check['changed'])} changed). "
              "These numbers are not comparable with runs on the original snapshot.")
    fingerprint = hashlib.sha256(
        "\n".join(f"{doc_id}:{sha256}" for doc_id, sha256 in sorted(hashes.items())).encode()).hexdigest()

    results = []
    for question in questions:
        result = evaluate(question, doc_ids, settings)
        if with_llm:
            response = rag.ask(question["question"], doc_ids, settings)
            result.update(status=response.status, answer=response.answer,
                          error=response.error.code if response.error else None)
        results.append(result)

    unanswerable = [result for result in results if not result["evidence"]]
    summary = {"overall": metrics(results),
               "by_type": {kind: metrics([result for result in results if result["type"] == kind])
                           for kind in sorted({result["type"] for result in results})},
               "unanswerable": {"n": len(unanswerable)}}
    if with_llm and unanswerable:
        summary["unanswerable"]["not_found_share"] = (
            sum(result["status"] == "not_found" for result in unanswerable) / len(unanswerable))
        summary["unanswerable"]["llm_errors"] = sum(result["status"] == "error" for result in unanswerable)

    config = {**settings, "corpus": corpus, "questions_file": questions_path.name, "eval_ks": list(EVAL_KS),
              "embedding_model": rag.EMBEDDING_MODEL, "llm_model": GEMINI_MODEL if with_llm else None}
    name = f"{corpus}_cs{settings['chunk_size']}_ov{settings['chunk_overlap']}"
    if with_llm:
        config["top_k_answers"] = settings["top_k"]
        name += f"_llm_k{settings['top_k']}"

    RESULTS_DIR.mkdir(exist_ok=True)
    stamp = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")
    out = RESULTS_DIR / f"{stamp}_{name}.json"
    report = {"config": config,
              "questions_sha256": hashlib.sha256(questions_path.read_bytes()).hexdigest(),
              "corpus_fingerprint": fingerprint,
              "corpus_check": "no manifest" if check is None else {"matches_manifest": not any(check.values()), **check},
              "metrics": summary,
              "questions": results}
    out.write_text(json.dumps(report, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    return report, out


def cell(value):
    return "–" if value is None else f"{value:.3f}"


def print_row(label, values):
    print(f"{label:<18}{values['n']:>4}" + "".join(f"{cell(values[column]):>8}" for column in COLUMNS))


def main():
    parser = argparse.ArgumentParser(description="Retrieval evaluation: hit@k, all@k, MRR.")
    parser.add_argument("--questions", required=True, type=Path)
    parser.add_argument("--corpus", default="forest")
    parser.add_argument("--chunk-size", type=int)
    parser.add_argument("--chunk-overlap", type=int)
    parser.add_argument("--top-k", type=int, help="top_k used for answers (--with-llm); metrics always use EVAL_KS")
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

    try:
        report, out = run_eval(args.questions, args.corpus, settings, args.with_llm)
    except rag.RagError as error:
        sys.exit(error.message)

    summary = report["metrics"]
    print(f"\ncorpus={args.corpus} chunk_size={settings['chunk_size']} chunk_overlap={settings['chunk_overlap']} "
          f"embedding={rag.EMBEDDING_MODEL}")
    print(f"{'type':<18}{'n':>4}" + "".join(f"{column.replace('mrr', 'MRR'):>8}" for column in COLUMNS))
    print_row("overall", summary["overall"])
    for kind, values in summary["by_type"].items():
        print_row(kind, values)
    line = f"unanswerable: {summary['unanswerable']['n']}"
    if "not_found_share" in summary["unanswerable"]:
        line += (f", returned not_found: {summary['unanswerable']['not_found_share']:.0%}"
                 f", LLM errors: {summary['unanswerable']['llm_errors']}")
    print(line)
    print(f"Results: {out}")


if __name__ == "__main__":
    main()