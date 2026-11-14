from __future__ import annotations

from pathlib import Path

from fastapi import FastAPI, File, Request, UploadFile
from fastapi.responses import JSONResponse
from fastapi.staticfiles import StaticFiles

from app import graph, rag, scanner, study, trace
from app.config import BASE_DIR, load_settings, save_settings, validate_settings
from app.rag import ERRORS, RagError
from app.schemas import EvalRequest, WordsQuestionRequest
from app.words import corpus_names, question_words, vocabulary, word_chunks
from evaluation.run import load_questions, run_eval
from app.hybrid import DEFAULT_RETRIEVERS, RETRIEVERS

app = FastAPI(title="RAG V1 — The Forest wiki")

# [DECISION D22] One file per question set; the file stem is also its corpus
QUESTIONS_DIR = BASE_DIR / "evaluation" / "questions"


@app.exception_handler(RagError)
async def rag_error_handler(request, error):
    # Every catalogued failure becomes the error envelope, with its HTTP status
    return JSONResponse(status_code=error.http_status,
                        content={"status": "error", "error": {"code": error.code, "message": error.message}})


async def json_body(request):
    """The request's JSON body, or None if it isn't valid JSON."""
    try:
        return await request.json()
    except ValueError:
        return None


@app.get("/api/documents")
def get_documents():
    return {"documents": rag.list_documents()}


@app.post("/api/documents")
async def post_document(file: UploadFile | None = File(None)):
    if file is None:
        raise RagError("empty_document")
    # [DECISION D50] One upload trace, with the validate, scan and store spans of add_document
    trace.start("upload", filename=file.filename)
    try:
        result = rag.add_document(file.filename, await file.read())
    except RagError as error:
        trace.finish("error", error_code=error.code)
        raise
    quarantined = result.get("status") == "quarantined"
    trace_id = trace.finish("quarantined" if quarantined else "accepted")
    return {**result, "trace_id": trace_id}


@app.get("/api/quarantine")
def get_quarantine():
    """[DECISION D59] The uploads waiting for review, with their findings."""
    waiting = scanner.list_quarantine()
    for sidecar in waiting:
        for finding in sidecar["findings"]:
            finding["description"] = scanner.RULE_DESCRIPTIONS.get(finding["rule"], finding["rule"])
    return {"documents": waiting}


async def review(request, decide, outcome):
    """Approve or reject one waiting upload, as a review trace naming the file."""
    body = await json_body(request)
    filename = body.get("filename") if isinstance(body, dict) else None
    trace.start("review", filename=filename if isinstance(filename, str) else None)
    try:
        result = decide(filename)
    except RagError as error:
        trace.finish("error", error_code=error.code)
        raise
    return {**(result or {"status": "ok"}), "trace_id": trace.finish(outcome)}


@app.post("/api/quarantine/approve")
async def post_quarantine_approve(request: Request):
    return await review(request, scanner.approve, "approved")


@app.post("/api/quarantine/reject")
async def post_quarantine_reject(request: Request):
    return await review(request, scanner.reject, "rejected")


@app.delete("/api/documents")
def delete_document(doc_id: str = ""):
    rag.delete_document(doc_id)
    return {"status": "ok"}


@app.get("/api/settings")
def get_settings():
    return load_settings()


@app.put("/api/settings")
async def put_settings(request: Request):
    try:
        return save_settings(await json_body(request))
    except ValueError as error:
        raise RagError("invalid_settings", str(error)) from None


@app.post("/api/ask")
async def post_ask(request: Request):
    body = await json_body(request)
    body = body if isinstance(body, dict) else {}
    question, doc_ids, retrievers = body.get("question"), body.get("doc_ids"), body.get("retrievers")
    # Malformed fields count as missing, so they get the catalogue's error codes
    if not isinstance(question, str):
        question = ""
    if not isinstance(doc_ids, list) or not all(isinstance(doc_id, str) for doc_id in doc_ids):
        doc_ids = []
    # A missing or malformed list of retrievers runs the default ones
    if not isinstance(retrievers, list):
        retrievers = None
    response = rag.ask(question, doc_ids, load_settings(), retrievers)
    status_code = ERRORS[response.error.code][0] if response.error else 200
    return JSONResponse(status_code=status_code, content=response.model_dump())


@app.post("/api/study")
async def post_study(request: Request):
    """[DECISION D50] One study trace. Errors keep their HTTP status and carry the trace id, so
    Details still opens, as /api/ask does."""
    body = await json_body(request)
    attrs = body if isinstance(body, dict) else {}
    doc_ids = attrs.get("doc_ids")
    trace.start("study", type=attrs.get("type"), count=attrs.get("count"), difficulty=attrs.get("difficulty"),
                doc_count=len(doc_ids) if isinstance(doc_ids, list) else 0)
    try:
        result = study.generate(body, load_settings())
    except RagError as error:
        outcome = "invalid" if error.code in ("invalid_llm_response", "no_study_items") else "error"
        trace_id = trace.finish(outcome, error_code=error.code)
        return JSONResponse(status_code=error.http_status,
                            content={"status": "error", "error": {"code": error.code, "message": error.message},
                                     "trace_id": trace_id})
    return {**result, "trace_id": trace.finish("ok", items=len(result["items"]), dropped=result["dropped"])}


@app.get("/api/chunk")
def get_chunk(id: str = ""):
    return rag.get_chunk(id)


@app.get("/api/corpora")
def get_corpora():
    return {"corpora": corpus_names()}


@app.get("/api/question-sets")
def get_question_sets():
    question_sets = []
    for path in sorted(QUESTIONS_DIR.glob("*.jsonl")):
        questions = [{"id": question["id"], "question": question["question"], "type": question["type"],
                      "evidence_doc_ids": list(dict.fromkeys(item["doc_id"] for item in question["evidence"]))}
                     for question in load_questions(path, path.stem)]
        question_sets.append({"name": path.stem, "questions": questions})
    return {"question_sets": question_sets}

@app.get("/api/retrievers")
def get_retrievers():
        return {"available": list(RETRIEVERS), "default": list(DEFAULT_RETRIEVERS),
            "graph_built": graph.graph_built(load_settings())}

@app.post("/api/eval")
def post_eval(body: EvalRequest):
    """[DECISION D31] Synchronous, no job queue. A plain def, so FastAPI runs it in a worker
    thread and a long run doesn't stop the server answering other requests."""
    path = QUESTIONS_DIR / f"{body.question_set}.jsonl"
    # Comparing with the real files also rejects a name that points outside the folder
    if path not in QUESTIONS_DIR.glob("*.jsonl"):
        raise RagError("unknown_question_set", f"Question set not found: {body.question_set}")
    try:
        # Used for this run only, never saved
        settings = validate_settings(body.model_dump(exclude={"question_set", "with_llm"}))
    except ValueError as error:
        raise RagError("invalid_settings", str(error)) from None
    results, results_path = run_eval(path, body.question_set, settings, body.with_llm,
                                     DEFAULT_RETRIEVERS if body.retrievers is None else body.retrievers)
    return {"results_file": results_path.relative_to(BASE_DIR).as_posix(), "metrics": results["metrics"],
            "corpus_check": results["corpus_check"]}


@app.get("/api/words/vocabulary")
def get_vocabulary(corpus: str = ""):
    return vocabulary(corpus, load_settings())


@app.get("/api/words/chunks")
def get_word_chunks(corpus: str = "", word: str = ""):
    return word_chunks(corpus, word, load_settings())


@app.post("/api/words/question")
def post_words_question(body: WordsQuestionRequest):
    return question_words(body.corpus, body.question, load_settings())

# The UI (Step 8). Mounted last, so the /api routes above take precedence
app.mount("/", StaticFiles(directory=Path(__file__).parent / "static", html=True), name="static")