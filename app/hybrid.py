"""Hybrid retrieval: plain RRF over the retrievers switched on."""
import time

from app import bm25_index, rag

RETRIEVERS = ("dense", "bm25", "graph")
# [DECISION D37] V2 behaviour. Changed once the default configuration is picked
DEFAULT_RETRIEVERS = ("dense",)
# [DECISION D36] Plain RRF constants
RRF_K = 60
RRF_CANDIDATES = 20


def fused_retrieve(question, doc_ids, settings, retrievers, top_k, candidates=RRF_CANDIDATES, rrf_k=RRF_K):
    """[DECISION D36] Each retriever that is on ranks its top `candidates` chunks, and a chunk scores
    sum(1 / (rrf_k + rank)) over the lists that contain it. Returns the top_k chunks in the
    rag.retrieve shape plus fused_score and found_by, with each retriever's list and timing."""
    if not retrievers:
        raise rag.RagError("invalid_retrievers")
    for name in retrievers:
        if name not in RETRIEVERS:
            raise rag.RagError("invalid_retrievers", f"Unknown retriever: {name}. Use dense, bm25 or graph.")
    if "graph" in retrievers:
        raise rag.RagError("invalid_retrievers", "The graph retriever isn't built yet.")
    if candidates < top_k:
        raise rag.RagError("invalid_settings", "candidates must be at least top_k.")

    start = time.perf_counter()
    # Indexed here and not only in rag.retrieve, so BM25 sees the selected documents when dense is off
    rag.ensure_indexed(doc_ids, settings)
    lists = {name: None for name in RETRIEVERS}
    timing_ms = {name: None for name in RETRIEVERS}
    known = {}  # chunk_id -> chunk in the rag.retrieve shape
    for name in RETRIEVERS:
        if name not in retrievers:
            continue
        retriever_start = time.perf_counter()
        if name == "dense":
            dense = rag.retrieve(question, doc_ids, {**settings, "top_k": candidates})
            known.update((chunk["id"], chunk) for chunk in dense)
            lists["dense"] = [chunk["id"] for chunk in dense]
        elif name == "bm25":
            lists["bm25"] = bm25_index.search(question, doc_ids, settings, candidates)
        timing_ms[name] = (time.perf_counter() - retriever_start) * 1000

    scores = {}
    for ranked in lists.values():
        for rank, chunk_id in enumerate(ranked or [], 1):
            scores[chunk_id] = scores.get(chunk_id, 0.0) + 1 / (rrf_k + rank)
    fused = sorted(scores, key=lambda chunk_id: (-scores[chunk_id], chunk_id))[:top_k]

    missing = [chunk_id for chunk_id in fused if chunk_id not in known]
    if missing:
        # A query restricted to these ids gives them the distance the dense query would have given
        result = rag.get_collection(rag.collection_name(settings)).query(
            query_texts=[question], ids=missing, n_results=len(missing))
        known.update((chunk_id, {"id": chunk_id, "text": text, "metadata": metadata, "distance": distance})
                     for chunk_id, text, metadata, distance in zip(
                         result["ids"][0], result["documents"][0], result["metadatas"][0], result["distances"][0]))
    chunks = [{**known[chunk_id], "fused_score": scores[chunk_id],
               "found_by": {name: ranked.index(chunk_id) + 1 if ranked and chunk_id in ranked else None
                            for name, ranked in lists.items()}}
              for chunk_id in fused]
    timing_ms["total"] = (time.perf_counter() - start) * 1000
    return {"chunks": chunks, "lists": lists, "graph": None, "timing_ms": timing_ms}