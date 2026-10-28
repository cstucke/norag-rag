from pathlib import Path

from fastapi import FastAPI, File, Request, UploadFile
from fastapi.responses import JSONResponse
from fastapi.staticfiles import StaticFiles

from app import rag
from app.config import load_settings, save_settings
from app.rag import ERRORS, RagError

app = FastAPI(title="RAG V1 — The Forest wiki")


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


# The UI (Step 8). Mounted last, so the /api routes above take precedence
app.mount("/", StaticFiles(directory=Path(__file__).parent / "static", html=True), name="static")