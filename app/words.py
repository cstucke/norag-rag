"""Words analytics. A diagnosis tool only: nothing here changes what
rag.retrieve returns."""
import re
from collections import Counter

from app import rag

# [DECISION D27] A word is a run of ASCII letters and digits; everything else separates words
TOKEN_RE = re.compile(r"[a-z0-9]+")


def tokenize(text):
    """[DECISION D28] Case-folded, no stopword removal, no stemming."""
    return TOKEN_RE.findall(text.lower())


def corpus_names():
    """Corpus names, from the doc_id prefixes (spec §4.2)."""
    return sorted({doc["doc_id"].split("/")[0] for doc in rag.list_documents() if "/" in doc["doc_id"]})

def corpus_doc_ids(corpus):
    """doc_ids of one corpus. A corpus is a top-level folder under corpus/ (spec §4.2)."""
    doc_ids = [doc["doc_id"] for doc in rag.list_documents() if doc["doc_id"].startswith(f"{corpus}/")]
    if not doc_ids:
        raise rag.RagError("unknown_corpus", f"Corpus not found: {corpus}")
    return doc_ids


def corpus_chunks(corpus, settings):
    """[DECISION D29] [DECISION D30] (chunk_id, metadata, Counter of tokens) for every chunk of one
    corpus, as stored in the collection: header lines included, overlap counted in both chunks."""
    doc_ids = corpus_doc_ids(corpus)
    rag.ensure_indexed(doc_ids, settings)
    where = {"doc_id": doc_ids[0]} if len(doc_ids) == 1 else {"doc_id": {"$in": doc_ids}}
    result = rag.get_collection(rag.collection_name(settings)).get(where=where, include=["documents", "metadatas"])
    return [(chunk_id, metadata, Counter(tokenize(text)))
            for chunk_id, text, metadata in zip(result["ids"], result["documents"], result["metadatas"])]


def word_totals(chunks):
    """Two Counters: occurrences of each word, and the number of chunks containing it."""
    counts, chunk_counts = Counter(), Counter()
    for _, _, tokens in chunks:
        counts.update(tokens)
        chunk_counts.update(tokens.keys())
    return counts, chunk_counts


def vocabulary(corpus, settings):
    chunks = corpus_chunks(corpus, settings)
    counts, chunk_counts = word_totals(chunks)
    words = [{"word": word, "count": count, "chunks": chunk_counts[word]}
             for word, count in sorted(counts.items(), key=lambda item: (-item[1], item[0]))]
    return {"corpus": corpus,
            "config": {"chunk_size": settings["chunk_size"], "chunk_overlap": settings["chunk_overlap"]},
            "chunk_count": len(chunks), "token_count": sum(counts.values()), "word_count": len(counts),
            "words": words}


def word_chunks(corpus, word, settings):
    tokens = tokenize(word)
    if len(tokens) != 1:
        raise rag.RagError("invalid_word")
    word = tokens[0]
    chunks = [{"chunk_id": chunk_id, "doc_id": metadata["doc_id"], "title": metadata["title"],
               "line_start": metadata["line_start"], "line_end": metadata["line_end"], "count": counts[word]}
              for chunk_id, metadata, counts in corpus_chunks(corpus, settings) if word in counts]
    chunks.sort(key=lambda chunk: (-chunk["count"], chunk["chunk_id"]))
    return {"word": word, "count": sum(chunk["count"] for chunk in chunks), "chunk_count": len(chunks),
            "chunks": chunks}


def question_words(corpus, question, settings):
    if not question.strip():
        raise rag.RagError("empty_question")
    counts, chunk_counts = word_totals(corpus_chunks(corpus, settings))
    words = [{"word": word, "count": counts[word], "chunks": chunk_counts[word]}
             for word in dict.fromkeys(tokenize(question))]
    return {"words": words, "missing": [item["word"] for item in words if item["count"] == 0]}