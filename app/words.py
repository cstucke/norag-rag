"""Words analytics (RAG_V2_SPEC.md, Step 6)."""
from app import rag


def corpus_doc_ids(corpus):
    """doc_ids of one corpus. A corpus is a top-level folder under corpus/ (spec §4.2)."""
    doc_ids = [doc["doc_id"] for doc in rag.list_documents() if doc["doc_id"].startswith(f"{corpus}/")]
    if not doc_ids:
        raise rag.RagError("unknown_corpus", f"Corpus not found: {corpus}")
    return doc_ids