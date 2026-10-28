from typing import Literal

from pydantic import BaseModel, ConfigDict


class LLMAnswer(BaseModel):
    """[DECISION D11] The JSON object the LLM must return."""
    model_config = ConfigDict(extra="forbid")

    answerable: bool
    answer: str
    citations: list[int]


class Reference(BaseModel):
    ref: int
    chunk_id: str
    doc_id: str
    title: str
    source_url: str
    line_start: int
    line_end: int
    distance: float


class ErrorInfo(BaseModel):
    code: str
    message: str


class AskConfig(BaseModel):
    chunk_size: int
    chunk_overlap: int
    top_k: int
    model: str


class AskResponse(BaseModel):
    status: Literal["answered", "not_found", "error"]
    answer: str | None = None
    references: list[Reference] = []
    retrieved: list[Reference] = []
    error: ErrorInfo | None = None
    config: AskConfig