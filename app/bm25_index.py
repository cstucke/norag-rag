"""BM25 over the chunks stored in Chroma. One index file per chunk configuration,
rebuilt whole when the collection's chunks change."""
import argparse
import hashlib
import json
import math
import time
from collections import Counter

from app import rag
from app.config import DATA_DIR, load_settings
from app.words import tokenize

BM25_DIR = DATA_DIR / "bm25"
# [DECISION D35] The usual defaults
K1 = 1.5
B = 0.75

# [DECISION D33] The last loaded index, so a question doesn't re-read the file
_index = None


def index_path(settings):
    return BM25_DIR / f"cs{settings['chunk_size']}_ov{settings['chunk_overlap']}.json"


def chunk_ids_sha256(chunk_ids):
    return hashlib.sha256("\n".join(sorted(chunk_ids)).encode()).hexdigest()


def build_index(settings):
    """[DECISION D32] Index every chunk stored in the collection for these settings, header
    lines included, so BM25 sees the same chunks, ids and text as the dense retriever.
    Writes the file and returns the index."""
    result = rag.get_collection(rag.collection_name(settings)).get(include=["documents", "metadatas"])
    chunks, df = [], Counter()
    for chunk_id, text, metadata in zip(result["ids"], result["documents"], result["metadatas"]):
        # [DECISION D34] The Words tab's tokenizer; document length = number of tokens
        tokens = tokenize(text)
        tf = Counter(tokens)
        df.update(tf.keys())
        chunks.append({"chunk_id": chunk_id, "doc_id": metadata["doc_id"], "length": len(tokens), "tf": tf})
    index = {"config": {"chunk_size": settings["chunk_size"], "chunk_overlap": settings["chunk_overlap"],
                        "k1": K1, "b": B},
             "chunk_ids_sha256": chunk_ids_sha256(result["ids"]), "n_chunks": len(chunks),
             "avgdl": sum(chunk["length"] for chunk in chunks) / len(chunks),
             "df": df, "chunks": chunks}
    BM25_DIR.mkdir(parents=True, exist_ok=True)
    with open(index_path(settings), "w", encoding="utf-8") as f:
        json.dump(index, f)
    return index


def current_index(settings):
    """[DECISION D33] The index for these settings. Rebuilt whole if the file is missing,
    unreadable, or was built from other chunks than the collection holds now."""
    global _index
    sha256 = chunk_ids_sha256(rag.get_collection(rag.collection_name(settings)).get(include=[])["ids"])
    if _index is not None and _index["chunk_ids_sha256"] == sha256:
        return _index
    try:
        with open(index_path(settings), "r", encoding="utf-8") as f:
            _index = json.load(f)
    except (OSError, ValueError):
        _index = None
    if _index is None or _index["chunk_ids_sha256"] != sha256:
        start = time.perf_counter()
        _index = build_index(settings)
        print(f"BM25 index rebuilt: {_index['n_chunks']} chunks, {time.perf_counter() - start:.1f} s")
    return _index


def search(question, doc_ids, settings, n):
    """Up to n chunk_ids of the selected docs with a score > 0, best first, ties by chunk_id.
    [DECISION D35] N, df and avgdl come from the whole collection, as for the dense index;
    only the results are restricted to doc_ids."""
    index = current_index(settings)
    n_chunks, avgdl, df = index["n_chunks"], index["avgdl"], index["df"]
    # [DECISION D34] Each query term counts once, however often the question repeats it
    idf = {term: math.log(1 + (n_chunks - df[term] + 0.5) / (df[term] + 0.5))
           for term in dict.fromkeys(tokenize(question)) if term in df}
    selected = set(doc_ids)
    scored = []
    for chunk in index["chunks"]:
        if chunk["doc_id"] not in selected:
            continue
        norm = K1 * (1 - B + B * chunk["length"] / avgdl)
        score = 0.0
        for term, weight in idf.items():
            tf = chunk["tf"].get(term, 0)
            score += weight * tf * (K1 + 1) / (tf + norm)
        if score > 0:
            scored.append((score, chunk["chunk_id"]))
    scored.sort(key=lambda item: (-item[0], item[1]))
    return [chunk_id for _, chunk_id in scored[:n]]

# ---------------------------------------------------------------------------
# CLI: python -m app.bm25_index --build
# ---------------------------------------------------------------------------

def main():
    parser = argparse.ArgumentParser(description="Rebuild the BM25 index for the saved settings.")
    parser.add_argument("--build", action="store_true", required=True, help="rebuild the index file now")
    parser.parse_args()
    settings = load_settings()
    start = time.perf_counter()
    index = build_index(settings)
    seconds = time.perf_counter() - start
    path = index_path(settings)
    print(f"{path}: {index['n_chunks']} chunks, {len(index['df'])} words, "
          f"{path.stat().st_size / 1e6:.1f} MB, {seconds:.1f} s")


if __name__ == "__main__":
    main()