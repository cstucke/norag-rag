import argparse
import hashlib
import json
import logging
import re
from functools import lru_cache
from pathlib import Path

import chromadb
import openai
from chromadb.utils.embedding_functions import SentenceTransformerEmbeddingFunction
from openai import OpenAI

from app.config import (CHROMA_DIR, CORPUS_DIR, DATA_DIR, GEMINI_MODEL, GOOGLE_API_KEY, INDEX_STATE_FILE, load_settings)
from app.schemas import AskConfig, AskResponse, ErrorInfo, LLMAnswer, Reference

from app.config import CHROMA_DIR, CORPUS_DIR, DATA_DIR, INDEX_STATE_FILE, load_settings

EMBEDDING_MODEL = "all-MiniLM-L6-v2"
DOC_EXTENSIONS = {".md", ".txt"}
UPLOADS_DIR = CORPUS_DIR / "uploads"
MAX_UPLOAD_BYTES = 2 * 1024 * 1024

# Failure catalogue (spec §7): error code -> (HTTP status, message the UI shows as-is)
ERRORS = {
    "empty_question": (400, "Please enter a question."),
    "no_documents_selected": (400, "Select at least one document."),
    "doc_not_found": (404, "Document not found."),
    "unsupported_file_type": (400, "Only .md and .txt files are supported."),
    "invalid_encoding": (400, "File must be UTF-8 text."),
    "empty_document": (400, "File is empty."),
    "file_too_large": (413, "File exceeds 2 MB."),
    "document_exists": (409, "A document with this name already exists."),
    "invalid_settings": (400, "Invalid settings."),
    "llm_not_configured": (503, "LLM not configured (missing API key)."),
    "llm_auth_or_model": (502, "LLM rejected the request (API key or model id)."),
    "llm_rate_limited": (503, "LLM rate limit reached — try again shortly."),
    "llm_timeout": (504, "LLM did not answer in time."),
    "llm_error": (502, "LLM call failed."),
    "invalid_llm_response": (200, "The model returned an invalid answer, so it was not shown."),
    "chunk_not_found": (404, "Passage not found (index may have changed)."),
}


class RagError(Exception):
    """A failure from the catalogue: error code, HTTP status and user-facing message."""

    def __init__(self, code, message=None):
        self.code = code
        self.http_status, default_message = ERRORS[code]
        self.message = message or default_message
        super().__init__(f"{code}: {self.message}")


# ---------------------------------------------------------------------------
# Chroma and index state
# ---------------------------------------------------------------------------

# Created on first use, so importing this module doesn't load the embedding model
@lru_cache(maxsize=1)
def chroma_client():
    return chromadb.PersistentClient(path=str(CHROMA_DIR))


@lru_cache(maxsize=1)
def embedding_function():
    return SentenceTransformerEmbeddingFunction(model_name=EMBEDDING_MODEL)


def get_collection(name):
    return chroma_client().get_or_create_collection(name=name, embedding_function=embedding_function())


def load_index_state():
    """{collection_name: {doc_id: sha256_of_file}}"""
    if not INDEX_STATE_FILE.exists():
        return {}
    with open(INDEX_STATE_FILE, "r", encoding="utf-8") as f:
        return json.load(f)


def save_index_state(state):
    DATA_DIR.mkdir(parents=True, exist_ok=True)
    with open(INDEX_STATE_FILE, "w", encoding="utf-8") as f:
        json.dump(state, f, indent=2)


# ---------------------------------------------------------------------------
# Corpus operations
# ---------------------------------------------------------------------------

def doc_id_of(path):
    """doc_id = path relative to corpus/, e.g. "forest/Katana.md"."""
    return path.relative_to(CORPUS_DIR).as_posix()


def doc_path(doc_id):
    """Path of an existing document. Anything else, including a path that resolves
    outside corpus/, is doc_not_found."""
    try:
        path = (CORPUS_DIR / doc_id).resolve()
        found = (path.is_relative_to(CORPUS_DIR)
                 and path.suffix.lower() in DOC_EXTENSIONS
                 and path.is_file())
    except (OSError, ValueError):
        found = False
    if not found:
        raise RagError("doc_not_found", f"Document not found: {doc_id}")
    return path


def read_document(path):
    """Text of a document. Chunk offsets and evaluation spans are both computed on this string."""
    return path.read_text(encoding="utf-8")


def document_info(path):
    """{doc_id, title, source_url, bytes}. Title and Source come from the header lines
    (before the first blank line), as written by the snapshot script."""
    title, source_url = path.name, None
    with open(path, "r", encoding="utf-8") as f:
        for i, line in enumerate(f):
            line = line.strip()
            if not line:
                break
            if i == 0 and line.startswith("# "):
                title = line[2:].strip() or path.name
            elif line.startswith("Source: "):
                source_url = line[len("Source: "):].strip()
    return {"doc_id": doc_id_of(path), "title": title, "source_url": source_url,
            "bytes": path.stat().st_size}


def list_documents():
    # The extension filter also leaves out MANIFEST.json and .gitkeep
    paths = sorted(p for p in CORPUS_DIR.rglob("*")
                   if p.is_file() and p.suffix.lower() in DOC_EXTENSIONS)
    return [document_info(p) for p in paths]


def safe_filename(filename):
    # Same rule as the snapshot script: spaces and anything outside [A-Za-z0-9._()-] become "_"
    return re.sub(r"[^A-Za-z0-9._()-]", "_", filename.replace(" ", "_"))


def add_document(filename, raw_bytes):
    name = safe_filename(filename or "")
    if Path(name).suffix.lower() not in DOC_EXTENSIONS:
        raise RagError("unsupported_file_type")
    if len(raw_bytes) > MAX_UPLOAD_BYTES:
        raise RagError("file_too_large")
    try:
        text = raw_bytes.decode("utf-8")  # strict
    except UnicodeDecodeError:
        raise RagError("invalid_encoding") from None
    if not text.strip():
        raise RagError("empty_document")
    path = UPLOADS_DIR / name
    if path.exists():
        raise RagError("document_exists")
    UPLOADS_DIR.mkdir(parents=True, exist_ok=True)
    path.write_bytes(raw_bytes)
    return document_info(path)


def delete_document(doc_id):
    path = doc_path(doc_id)
    doc_id = doc_id_of(path)
    # Remove its chunks from every collection, then the file
    state = load_index_state()
    for collection_name, indexed in state.items():
        get_collection(collection_name).delete(where={"doc_id": doc_id})
        indexed.pop(doc_id, None)
    save_index_state(state)
    path.unlink()

# ---------------------------------------------------------------------------
# Chunking and indexing
# ---------------------------------------------------------------------------

def chunk_text(text, size, overlap):
    """[DECISION D9] Fixed-size character windows over the whole text, header lines
    included, advancing by size - overlap. The last chunk may be shorter."""
    chunks = []
    for start in range(0, len(text), size - overlap):
        end = min(start + size, len(text))
        chunks.append((start, end, text[start:end]))
        if end == len(text):
            break
    return chunks


def line_number(text, offset):
    """1-based line of the character at offset."""
    return text.count("\n", 0, offset) + 1


def collection_name(settings):
    return f"rag_cs{settings['chunk_size']}_ov{settings['chunk_overlap']}"


def file_sha256(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def ensure_indexed(doc_ids, settings):
    """[DECISION D16] (Re)index each doc that is missing from, or stale in, the collection
    for the current chunk size and overlap. Returns how many docs were indexed."""
    size, overlap = settings["chunk_size"], settings["chunk_overlap"]
    name = collection_name(settings)
    collection = get_collection(name)
    state = load_index_state()
    indexed = state.setdefault(name, {})
    count = 0
    for doc_id in doc_ids:
        path = doc_path(doc_id)
        sha256 = file_sha256(path)
        if indexed.get(doc_id) == sha256:
            continue
        collection.delete(where={"doc_id": doc_id})
        text = read_document(path)
        info = document_info(path)
        chunks = chunk_text(text, size, overlap)
        ids = [f"{doc_id}#cs{size}-ov{overlap}#{i}" for i in range(len(chunks))]
        documents = [chunk for _, _, chunk in chunks]
        metadatas = [{"doc_id": doc_id, "title": info["title"], "source_url": info["source_url"] or "",
                      "chunk_index": i, "char_start": start, "char_end": end,
                      "line_start": line_number(text, start), "line_end": line_number(text, end - 1)}
                     for i, (start, end, _) in enumerate(chunks)]
        # Chroma caps how many records one add() takes; small chunk sizes exceed it on the largest pages
        batch = chroma_client().get_max_batch_size()
        for i in range(0, len(ids), batch):
            collection.add(ids=ids[i:i + batch], documents=documents[i:i + batch],
                           metadatas=metadatas[i:i + batch])
        indexed[doc_id] = sha256
        count += 1
    save_index_state(state)
    return count

# ---------------------------------------------------------------------------
# Retrieval and answering
# ---------------------------------------------------------------------------

GEMINI_BASE_URL = "https://generativelanguage.googleapis.com/v1beta/openai/"

PROMPT = """You answer questions using ONLY the numbered excerpts below, taken from The Forest wiki.
If the excerpts do not contain the answer, set "answerable" to false and explain briefly in "answer".
Do not use outside knowledge.

Return ONLY a JSON object with exactly these keys:
{{"answerable": true|false, "answer": "<string>", "citations": [<excerpt numbers you used>]}}

Excerpts:
{excerpts}

Question: {question}"""

logger = logging.getLogger(__name__)


def retrieve(question, doc_ids, settings):
    """Top-k chunks of the selected docs, best first: [{id, text, metadata, distance}].
    The evaluation harness calls this same function."""
    ensure_indexed(doc_ids, settings)
    where = {"doc_id": doc_ids[0]} if len(doc_ids) == 1 else {"doc_id": {"$in": doc_ids}}
    result = get_collection(collection_name(settings)).query(
        query_texts=[question], n_results=settings["top_k"], where=where)
    return [{"id": chunk_id, "text": text, "metadata": metadata, "distance": distance}
            for chunk_id, text, metadata, distance in zip(
                result["ids"][0], result["documents"][0], result["metadatas"][0], result["distances"][0])]


def build_prompt(question, chunks):
    excerpts = "\n\n".join(
        f"[{rank}] (source: {chunk['metadata']['title']}, "
        f"lines {chunk['metadata']['line_start']}-{chunk['metadata']['line_end']})\n{chunk['text']}"
        for rank, chunk in enumerate(chunks, 1))
    return PROMPT.format(excerpts=excerpts, question=question)


def call_llm(prompt):
    """Gemini's raw reply text. API failures become the matching catalogue error."""
    if not GOOGLE_API_KEY:
        raise RagError("llm_not_configured")
    # max_retries=0: otherwise the SDK retries on its own (D15: no retry),
    # and the 60 s timeout would no longer be the limit
    client = OpenAI(api_key=GOOGLE_API_KEY, base_url=GEMINI_BASE_URL, timeout=60, max_retries=0)
    try:
        response = client.chat.completions.create(
            model=GEMINI_MODEL, messages=[{"role": "user", "content": prompt}],
            temperature=0, response_format={"type": "json_object"})
    except openai.APITimeoutError:
        raise RagError("llm_timeout") from None
    except openai.RateLimitError:
        raise RagError("llm_rate_limited") from None
    # Gemini answers a bad API key with 400 and an unknown model id with 404
    except (openai.BadRequestError, openai.AuthenticationError,
            openai.PermissionDeniedError, openai.NotFoundError):
        raise RagError("llm_auth_or_model") from None
    except openai.OpenAIError:
        raise RagError("llm_error") from None
    return response.choices[0].message.content or ""


def strip_code_fence(text):
    match = re.fullmatch(r"```(?:json)?\s*(.*?)\s*```", text.strip(), re.DOTALL)
    return match.group(1) if match else text


def parse_llm_output(raw, k):
    """[DECISION D12] The validated LLMAnswer, with duplicate citations removed.
    [DECISION D15] Any violation is invalid_llm_response: raw text logged, no retry, no repair."""
    try:
        llm_answer = LLMAnswer.model_validate_json(strip_code_fence(raw))
        llm_answer.citations = list(dict.fromkeys(llm_answer.citations))
        if any(not 1 <= citation <= k for citation in llm_answer.citations):
            raise ValueError(f"citation outside 1..{k}: {llm_answer.citations}")
        if llm_answer.answerable and (not llm_answer.answer.strip() or not llm_answer.citations):
            raise ValueError("answerable=true without an answer or without citations")
    except ValueError as reason:
        logger.warning("invalid_llm_response (%s). Raw LLM output: %r", reason, raw)
        raise RagError("invalid_llm_response") from None
    return llm_answer


def to_reference(rank, chunk):
    meta = chunk["metadata"]
    return Reference(ref=rank, chunk_id=chunk["id"], doc_id=meta["doc_id"], title=meta["title"],
                     source_url=meta["source_url"], line_start=meta["line_start"],
                     line_end=meta["line_end"], distance=chunk["distance"])


def ask(question, doc_ids, settings):
    """The whole /api/ask logic, also used by the evaluation harness (--with-llm).
    Request errors are raised as RagError. Everything after retrieval is reported
    in the returned AskResponse."""
    if not question.strip():
        raise RagError("empty_question")
    if not doc_ids:
        raise RagError("no_documents_selected")
    config = AskConfig(chunk_size=settings["chunk_size"], chunk_overlap=settings["chunk_overlap"],
                       top_k=settings["top_k"], model=GEMINI_MODEL)
    chunks = retrieve(question, doc_ids, settings)
    retrieved = [to_reference(rank, chunk) for rank, chunk in enumerate(chunks, 1)]
    if not chunks:
        # [DECISION D14] Nothing retrieved: the LLM is not called
        return AskResponse(status="not_found", answer="Nothing was retrieved from the selected documents.",
                           config=config)
    try:
        llm_answer = parse_llm_output(call_llm(build_prompt(question, chunks)), len(chunks))
    except RagError as error:
        return AskResponse(status="error", error=ErrorInfo(code=error.code, message=error.message),
                           retrieved=retrieved, config=config)
    references = [retrieved[citation - 1] for citation in llm_answer.citations]
    if not llm_answer.answerable:
        # [DECISION D14] The excerpts don't contain the answer
        return AskResponse(status="not_found",
                           answer=f"The selected documents don't contain an answer. {llm_answer.answer}".strip(),
                           references=references, retrieved=retrieved, config=config)
    return AskResponse(status="answered", answer=llm_answer.answer, references=references,
                       retrieved=retrieved, config=config)

# ---------------------------------------------------------------------------
# CLI: python -m app.rag --index-all
# ---------------------------------------------------------------------------

def main():
    parser = argparse.ArgumentParser(description="Pre-build the index for the current settings.")
    parser.add_argument("--index-all", action="store_true", required=True,
                        help="index all documents under the current settings")
    parser.parse_args()
    settings = load_settings()
    doc_ids = [doc["doc_id"] for doc in list_documents()]
    indexed = 0
    for i in range(0, len(doc_ids), 50):
        indexed += ensure_indexed(doc_ids[i:i + 50], settings)
        print(f"{min(i + 50, len(doc_ids))}/{len(doc_ids)} documents checked, {indexed} indexed")
    name = collection_name(settings)
    print(f"{name}: {get_collection(name).count()} chunks")


if __name__ == "__main__":
    main()