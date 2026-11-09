"""Extraction-quality sample: random edges of the concept graph, to grade by hand.

    python -m evaluation.graph_sample [--n 10] [--seed 42]

Writes evaluation/results/<UTC stamp>_kestrel_graph_sample.json with every grade empty. The user
fills in `grade` (correct, wrong or unsupported) and `note`; no code reads them back.
"""
import argparse
import json
import random
import sys
from datetime import datetime, timezone
from pathlib import Path

from app import graph, rag
from app.config import load_settings

RESULTS_DIR = Path(__file__).resolve().parent / "results"


def sample_edges(settings, n, seed):
    """[DECISION D47] n edges (resolved triples), picked with random.Random(seed).sample. With fewer
    than n edges, all of them are taken and a line says so. Each comes with its source chunks' text."""
    loaded = graph.load_graph(settings)
    nodes = {node["id"]: node for node in loaded["nodes"]}
    edges = loaded["edges"]
    if len(edges) < n:
        print(f"The graph has only {len(edges)} edges: taking all of them.")
        n = len(edges)
    triples = []
    for edge in random.Random(seed).sample(edges, n):
        chunks = []
        for chunk_id in edge["chunk_ids"]:
            chunk = rag.get_chunk(chunk_id)
            chunks.append({"chunk_id": chunk_id, "doc_id": chunk["doc_id"], "text": chunk["text"]})
        triples.append({"source": nodes[edge["source"]]["name"], "source_type": nodes[edge["source"]]["type"],
                        "relation": edge["relation"],
                        "target": nodes[edge["target"]]["name"], "target_type": nodes[edge["target"]]["type"],
                        "chunks": chunks, "grade": None, "note": ""})
    return loaded, triples


def main():
    parser = argparse.ArgumentParser(description="Pick random graph edges to grade against their chunks.")
    parser.add_argument("--n", type=int, default=10)
    parser.add_argument("--seed", type=int, default=42)
    args = parser.parse_args()
    settings = load_settings()
    try:
        loaded, triples = sample_edges(settings, args.n, args.seed)
    except rag.RagError as error:
        sys.exit(error.message)
    report = {"config": {"graph_file": graph.graph_path(settings).name, "seed": args.seed, "n": args.n},
              "triples": triples}
    RESULTS_DIR.mkdir(exist_ok=True)
    stamp = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")
    out = RESULTS_DIR / f"{stamp}_kestrel_graph_sample.json"
    out.write_text(json.dumps(report, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    for number, triple in enumerate(triples, 1):
        print(f"{number}. ({triple['source']}, {triple['relation']}, {triple['target']}) "
              f"[{', '.join(chunk['chunk_id'] for chunk in triple['chunks'])}]")
    print(f"Grades go in: {out}")


if __name__ == "__main__":
    main()