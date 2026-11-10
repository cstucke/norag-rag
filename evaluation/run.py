"""Retrieval evaluation harness.

    python -m evaluation.run --questions evaluation/questions/kestrel.jsonl --corpus kestrel \
        [--retrievers dense,bm25,graph --candidates N --rrf-k N] [--chunk-size N --chunk-overlap N --top-k N] \
        [--with-llm]

Without --with-llm it makes no LLM calls, so the numbers are deterministic.
"""
import argparse
import hashlib
import json
import sys
import time
from datetime import datetime, timezone
from pathlib import Path

from app import bm25_index, graph, hybrid, rag
from app.config import BASE_DIR, CORPUS_DIR, GEMINI_MODEL, load_settings, validate_settings, validate_settings
from app.words import corpus_doc_ids

RESULTS_DIR = Path(__file__).resolve().parent / "results"
# [DECISION D17] A chunk is a hit if it covers at least this share of the evidence span
MIN_COVERAGE = 0.5
# [DECISION D23] Metrics at k read the first k chunks of one top-10 ranking
EVAL_KS = (1, 3, 5, 10)
COLUMNS = [f"{name}@{k}" for name in ("hit", "recall") for k in EVAL_KS] + ["mrr"]
COST_FIELDS = ("retrieval_ms", "llm_calls", "prompt_tokens", "completion_tokens", "answer_ms")
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


def covers(chunk, item):
    """[DECISION D17] Whether a chunk ({doc_id, char_start, char_end, ...}) holds at least
    MIN_COVERAGE of an evidence item's span."""
    start, end = item["span"]
    return (chunk["doc_id"] == item["doc_id"]
            and min(end, chunk["char_end"]) - max(start, chunk["char_start"]) >= MIN_COVERAGE * (end - start))


def evaluate(question, doc_ids, settings, retrievers, candidates, rrf_k):
    fused = hybrid.fused_retrieve(question["question"], doc_ids, settings, retrievers, max(EVAL_KS),
                                  candidates, rrf_k)
    chunks = fused["chunks"]
    retrieved = [{"rank": rank, "chunk_id": chunk["id"], "doc_id": chunk["metadata"]["doc_id"],
                  "char_start": chunk["metadata"]["char_start"], "char_end": chunk["metadata"]["char_end"]}
                 for rank, chunk in enumerate(chunks, 1)]
    # Spans of every retriever's candidates, for rank_in. Chroma refuses get() with an empty id list
    candidate_ids = sorted({chunk_id for ranked in fused["lists"].values() for chunk_id in ranked or []})
    spans = {}
    if candidate_ids:
        result = rag.get_collection(rag.collection_name(settings)).get(ids=candidate_ids, include=["metadatas"])
        spans = dict(zip(result["ids"], result["metadatas"]))
    evidence, retrieval_evidence = [], []
    for item in question["evidence"]:
        start, end = item["span"]
        hit_ranks = [chunk["rank"] for chunk in retrieved if covers(chunk, item)]
        evidence.append({"doc_id": item["doc_id"], "char_start": start, "char_end": end, "hit_ranks": hit_ranks})
        retrieval_evidence.append({
            "doc_id": item["doc_id"], "quote": item["quote"], "fused_rank": hit_ranks[0] if hit_ranks else None,
            "rank_in": {name: next((rank for rank, chunk_id in enumerate(ranked or [], 1)
                                    if covers(spans[chunk_id], item)), None)
                        for name, ranked in fused["lists"].items()}})
    first_hits = [item["hit_ranks"][0] for item in evidence if item["hit_ranks"]]
    graph = fused["graph"]
    return {"id": question["id"], "type": question["type"], "retrieved": retrieved, "evidence": evidence,
            "first_hit_rank": min(first_hits) if first_hits else None,
            "all_evidence_hit": bool(evidence) and all(item["hit_ranks"] for item in evidence),
            "retrieval": {"ranked": [{"rank": rank, "chunk_id": chunk["id"], "doc_id": chunk["metadata"]["doc_id"],
                                      "fused_score": chunk["fused_score"], "found_by": chunk["found_by"]}
                                     for rank, chunk in enumerate(chunks, 1)],
                          "evidence": retrieval_evidence,
                          "graph": ({"entities": graph["entities"], "edges_followed": len(graph["edges"])}
                                    if graph else None)},
            "cost": {"retrieval_ms": fused["timing_ms"]["total"], "llm_calls": 0, "prompt_tokens": 0,
                     "completion_tokens": 0, "answer_ms": None}}


def hit_at(result, k):
    return any(rank <= k for item in result["evidence"] for rank in item["hit_ranks"])


def all_at(result, k):
    return all(any(rank <= k for rank in item["hit_ranks"]) for item in result["evidence"])


def recall_at(result, k):
    """[DECISION D45] Share of the question's evidence items covered by its first k chunks."""
    return sum(any(rank <= k for rank in item["hit_ranks"]) for item in result["evidence"]) / len(result["evidence"])


def metrics(results):
    """[DECISION D18] [DECISION D23] [DECISION D45] hit@k, all@k, recall@k and MRR over the answerable
    questions in results. With no answerable question, n is 0 and every metric is None."""
    answerable = [result for result in results if result["evidence"]]
    n = len(answerable)
    values = {"n": n, "unanswerable": len(results) - n}
    for k in EVAL_KS:
        values[f"hit@{k}"] = sum(hit_at(result, k) for result in answerable) / n if n else None
    for k in EVAL_KS:
        values[f"all@{k}"] = sum(all_at(result, k) for result in answerable) / n if n else None
    for k in EVAL_KS:
        values[f"recall@{k}"] = sum(recall_at(result, k) for result in answerable) / n if n else None
    values["mrr"] = (sum(1 / result["first_hit_rank"] for result in answerable if result["first_hit_rank"]) / n
                     if n else None)
    return values


def reach(results, name, graph_only):
    """[DECISION D45] Among the evidence items the graph retriever found (with graph_only, the ones no
    other retriever found), the share whose first fused rank is at most k. With no such item, None."""
    items = [item for result in results for item in result["retrieval"]["evidence"]
             if item["rank_in"]["graph"] is not None
             and not (graph_only and any(rank is not None for other, rank in item["rank_in"].items()
                                         if other != "graph"))]
    n = len(items)
    values = {"n": n}
    for k in EVAL_KS:
        values[f"{name}@{k}"] = (sum(item["fused_rank"] is not None and item["fused_rank"] <= k for item in items) / n
                                 if n else None)
    return values

def llm_entry(response):
    """One answer and the chunks behind it, so it can be graded from the results file alone.
    [DECISION D26] The user fills in grade and grade_note; the harness never reads them back."""
    # AskResponse carries no chunk text, so each chunk is fetched by its id
    context = [{"rank": ref.ref, "chunk_id": ref.chunk_id, "doc_id": ref.doc_id, "line_start": ref.line_start,
                "line_end": ref.line_end, "text": rag.get_chunk(ref.chunk_id)["text"]}
               for ref in response.retrieved]
    return {"status": response.status, "answer": response.answer,
            "error": response.error.model_dump() if response.error else None,
            "references": [{"ref": ref.ref, "chunk_id": ref.chunk_id} for ref in response.references],
            "context": context, "grade": None, "grade_note": ""}

def run_eval(questions_path, corpus, settings, with_llm, retrievers=hybrid.DEFAULT_RETRIEVERS,
             candidates=hybrid.RRF_CANDIDATES, rrf_k=hybrid.RRF_K):
    """One evaluation run, shared by the CLI and POST /api/eval. Returns (results, results_path)."""
    if "graph" in retrievers and corpus != "kestrel":
        raise rag.RagError("invalid_retrievers", "The graph retriever only exists for the kestrel corpus.")
    if candidates < max(EVAL_KS):
        raise rag.RagError("invalid_settings", f"candidates must be at least {max(EVAL_KS)}.")
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
        result = evaluate(question, doc_ids, settings, retrievers, candidates, rrf_k)
        if with_llm:
            before, start = dict(rag.USAGE), time.perf_counter()
            response = rag.ask(question["question"], doc_ids, settings, retrievers)
            result["cost"].update(llm_calls=rag.USAGE["calls"] - before["calls"],
                                  prompt_tokens=rag.USAGE["prompt_tokens"] - before["prompt_tokens"],
                                  completion_tokens=rag.USAGE["completion_tokens"] - before["completion_tokens"],
                                  answer_ms=(time.perf_counter() - start) * 1000)
            result["llm"] = llm_entry(response)
        results.append(result)

    unanswerable = [result for result in results if not result["evidence"]]
    summary = {"overall": metrics(results),
               "by_type": {kind: metrics([result for result in results if result["type"] == kind])
                           for kind in sorted({result["type"] for result in results})},
               "unanswerable": {"n": len(unanswerable)}}
    if with_llm and unanswerable:
        summary["unanswerable"]["not_found_share"] = (
            sum(result["llm"]["status"] == "not_found" for result in unanswerable) / len(unanswerable))
        summary["unanswerable"]["llm_errors"] = sum(result["llm"]["status"] == "error" for result in unanswerable)
    if "graph" in retrievers:
        summary["graph_reach"] = reach(results, "graph_reach", False)
        summary["graph_only_reach"] = reach(results, "graph_only_reach", True)
    # Means per question; answer_ms has no mean without --with-llm
    summary["cost"] = {field: None if any(result["cost"][field] is None for result in results)
                       else sum(result["cost"][field] for result in results) / len(results)
                       for field in COST_FIELDS}

    config = {**settings, "corpus": corpus, "questions_file": questions_path.name, "eval_ks": list(EVAL_KS),
              "embedding_model": rag.EMBEDDING_MODEL, "llm_model": GEMINI_MODEL if with_llm else None,
              "retrievers": list(retrievers), "candidates": candidates, "rrf_k": rrf_k}
    if "bm25" in retrievers:
        config["bm25_chunk_ids_sha256"] = bm25_index.current_index(settings)["chunk_ids_sha256"]
        if "graph" in retrievers:
            config["graph_file"] = graph.graph_path(settings).relative_to(BASE_DIR).as_posix()
            config["graph_build"] = graph.load_graph(settings)["build"]
    name = f"{corpus}_cs{settings['chunk_size']}_ov{settings['chunk_overlap']}_{'+'.join(retrievers)}"
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
    print(f"{label:<18}{values['n']:>4}" + "".join(f"{cell(values[column]):>10}" for column in COLUMNS))


def reach_text(values, name):
    return f"(n={values['n']})" + "".join(f" @{k} {cell(values[f'{name}@{k}'])}" for k in EVAL_KS)


def main():
    parser = argparse.ArgumentParser(description="Retrieval evaluation: hit@k, recall@k, all@k, MRR.")
    parser.add_argument("--questions", required=True, type=Path)
    parser.add_argument("--corpus", default="forest")
    parser.add_argument("--retrievers", default=",".join(hybrid.DEFAULT_RETRIEVERS),
                        help="comma-separated, any of dense, bm25, graph")
    parser.add_argument("--candidates", type=int, default=hybrid.RRF_CANDIDATES,
                        help="length of each retriever's list before fusion (at least 10)")
    parser.add_argument("--rrf-k", type=int, default=hybrid.RRF_K)
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
    # Empty names are dropped, so --retrievers "" gets "Switch on at least one retriever."
    retrievers = [name for name in args.retrievers.split(",") if name]

    try:
        report, out = run_eval(args.questions, args.corpus, settings, args.with_llm, retrievers,
                               args.candidates, args.rrf_k)
    except rag.RagError as error:
        sys.exit(error.message)

    summary = report["metrics"]
    print(f"\ncorpus={args.corpus} chunk_size={settings['chunk_size']} chunk_overlap={settings['chunk_overlap']} "
          f"embedding={rag.EMBEDDING_MODEL}")
    print(f"{'type':<18}{'n':>4}" + "".join(f"{column.replace('mrr', 'MRR'):>10}" for column in COLUMNS))
    print_row("overall", summary["overall"])
    for kind, values in summary["by_type"].items():
        print_row(kind, values)
    line = f"unanswerable: {summary['unanswerable']['n']}"
    if "not_found_share" in summary["unanswerable"]:
        line += (f", returned not_found: {summary['unanswerable']['not_found_share']:.0%}"
                 f", LLM errors: {summary['unanswerable']['llm_errors']}")
    print(line)
    cost = summary["cost"]
    answer = "–" if cost["answer_ms"] is None else f"{cost['answer_ms']:.0f} ms"
    print(f"cost per question: retrieval {cost['retrieval_ms']:.0f} ms, LLM calls {cost['llm_calls']:.2f}, "
          f"tokens {cost['prompt_tokens']:.0f} prompt / {cost['completion_tokens']:.0f} completion, "
          f"answer {answer}")
    if "graph_reach" in summary:
        print(f"graph reach {reach_text(summary['graph_reach'], 'graph_reach')} · "
              f"graph-only reach {reach_text(summary['graph_only_reach'], 'graph_only_reach')}")
    print(f"Results: {out}")


if __name__ == "__main__":
    main()
