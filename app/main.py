from pathlib import Path

from fastapi import FastAPI, File, Request, UploadFile
from fastapi.responses import JSONResponse
from fastapi.staticfiles import StaticFiles

from app import rag
from app.config import BASE_DIR, load_settings, save_settings, validate_settings
from app.rag import ERRORS, RagError
from app.schemas import EvalRequest, WordsQuestionRequest
from app.words import corpus_names, question_words, vocabulary, word_chunks
from evaluation.run import load_questions, run_eval

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
    return rag.add_document(file.filename, await file.read())


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
    question, doc_ids = body.get("question"), body.get("doc_ids")
    # Malformed fields count as missing, so they get the catalogue's error codes
    if not isinstance(question, str):
        question = ""
    if not isinstance(doc_ids, list) or not all(isinstance(doc_id, str) for doc_id in doc_ids):
        doc_ids = []
    response = rag.ask(question, doc_ids, load_settings())
    status_code = ERRORS[response.error.code][0] if response.error else 200
    return JSONResponse(status_code=status_code, content=response.model_dump())


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
    results, results_path = run_eval(path, body.question_set, settings, body.with_llm)
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