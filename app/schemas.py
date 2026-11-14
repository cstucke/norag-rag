from __future__ import annotations
import re
from typing import Any, Literal

from pydantic import BaseModel, ConfigDict, field_validator, model_validator


class LLMAnswer(BaseModel):
    """[DECISION D11] The JSON object the LLM must return."""
    model_config = ConfigDict(extra="forbid")

    answerable: bool
    answer: str
    citations: list[int]


class Flashcard(BaseModel):
    """[DECISION D57] One study item as the LLM must return it. The checks that need the excerpts
    (excerpt range, quote) are done in study.py, as parse_llm_output does for citations."""
    model_config = ConfigDict(extra="forbid", str_strip_whitespace=True, str_min_length=1)

    question: str
    answer: str
    excerpt: int
    quote: str


class ChoiceQuestion(BaseModel):
    """[DECISION D57] answer is the position of the right option, 1 to 4."""
    model_config = ConfigDict(extra="forbid", str_strip_whitespace=True, str_min_length=1)

    question: str
    options: list[str]
    answer: int
    excerpt: int
    quote: str

class Triple(BaseModel):
    """[DECISION D40] One triple extracted by the LLM. The schema (entity and relation types) is passed
    as the validation context, so this module doesn't import graph.py."""
    subject: str
    subject_type: str
    relation: str
    object: str
    object_type: str

    @field_validator("subject", "object")
    @classmethod
    def name_not_empty(cls, value):
        value = value.strip()
        # Same test as graph.normalize: a name with no letter or digit can't become a node id
        if not re.search(r"[a-z0-9]", value.casefold()):
            raise ValueError("name must contain a letter or a digit")
        return value

    @model_validator(mode="after")
    def check_schema(self, info):
        if info.context is None:
            raise ValueError("no schema given to validate against")
        entity_types, relation_types = info.context["entity_types"], info.context["relation_types"]
        for kind in (self.subject_type, self.object_type):
            if kind not in entity_types:
                raise ValueError(f"unknown entity type: {kind}")
        if self.relation not in relation_types:
            raise ValueError(f"unknown relation: {self.relation}")
        rule = relation_types[self.relation]
        if self.subject_type not in rule["subject"]:
            raise ValueError(f"{self.relation} does not take a {self.subject_type} subject "
                             f"(allowed: {', '.join(rule['subject'])})")
        if self.object_type not in rule["object"]:
            raise ValueError(f"{self.relation} does not take a {self.object_type} object "
                             f"(allowed: {', '.join(rule['object'])})")
        return self

class Reference(BaseModel):
    ref: int
    chunk_id: str
    doc_id: str
    title: str
    source_url: str
    line_start: int
    line_end: int
    distance: float
    found_by: dict[str, int | None] | None = None


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
    graph_path: dict | None = None

class EvalRequest(BaseModel):
    """The settings stay untyped so a bad value reaches validate_settings and gets invalid_settings."""
    question_set: str = ""
    chunk_size: Any = None
    chunk_overlap: Any = None
    top_k: Any = None
    with_llm: bool = False
    retrievers: list[str] | None = None


class WordsQuestionRequest(BaseModel):
    corpus: str = ""
    question: str = ""