from __future__ import annotations
import argparse
import json
import logging
import re
import sys
import time
from collections import Counter
from datetime import datetime, timezone

from pydantic import ValidationError

from app import rag
from app.config import DATA_DIR, GEMINI_MODEL, load_settings
from app.schemas import Triple
from app.words import corpus_doc_ids

GRAPH_DIR = DATA_DIR / "graph"
CORPUS = "kestrel"

logger = logging.getLogger(__name__)

# ---------------------------------------------------------------------------
# Schema
# ---------------------------------------------------------------------------

# [DECISION D38] A fixed schema, approved before any extraction. Fixed so that a chain like
# error -> service -> team -> channel is made of the same few edge kinds in every chunk
ENTITY_TYPES = {
    "ErrorCode": "An error code of the form KST- plus four digits",
    "Service": "A Kestrel production service from the service catalog",
    "Team": "An engineering team that owns services and runs an on-call rotation",
    "Person": "A named person, such as a team's engineering lead",
    "Channel": "A chat channel, written with a leading #",
    "Plan": "A subscription plan: Free, Starter, Team, Business or Enterprise",
    "Role": "A workspace role: Owner, Admin, Editor or Viewer",
    "Feature": "A product capability or procedure (single sign-on, scheduled reports, refunds, payment retries)",
}

RELATION_TYPES = {
    "raised_by": {"subject": ["ErrorCode"], "object": ["Service"],
                  "meaning": "The service that raises the error"},
    "escalates_to": {"subject": ["ErrorCode"], "object": ["Team", "Service"],
                     "meaning": "Where support escalates the error"},
    "resolved_by": {"subject": ["ErrorCode"], "object": ["Feature"],
                    "meaning": "The feature or procedure that fixes the error"},
    "owned_by": {"subject": ["Service"], "object": ["Team"],
                 "meaning": "The team that owns the service"},
    "provides": {"subject": ["Service"], "object": ["Feature"],
                 "meaning": "A feature the service implements"},
    "replaces": {"subject": ["Service"], "object": ["Service"],
                 "meaning": "The newer service (subject) took over from the older one (object)"},
    "led_by": {"subject": ["Team"], "object": ["Person"],
               "meaning": "The team's engineering lead"},
    "has_channel": {"subject": ["Team"], "object": ["Channel"],
                    "meaning": "The team's on-call chat channel"},
    "covered_by": {"subject": ["Team"], "object": ["Team"],
                   "meaning": "The team that covers it outside its own hours"},
    "available_on": {"subject": ["Feature"], "object": ["Plan"],
                     "meaning": "A plan that includes the feature"},
    "performed_by": {"subject": ["Feature"], "object": ["Role"],
                     "meaning": "The role that can do or request it"},
}

SCHEMA = {"entity_types": ENTITY_TYPES, "relation_types": RELATION_TYPES}

# ---------------------------------------------------------------------------
# Extraction
# ---------------------------------------------------------------------------

# [DECISION D39] One LLM call per chunk. The two lists are generated from the constants above
PROMPT = """You extract a knowledge graph from one excerpt of the Kestrel Analytics knowledge base.

Entity types:
<ENTITY_TYPES>

Relation types (subject type → object type):
<RELATION_TYPES>

Rules:
- Use only the types and relations listed above.
- Extract only facts the excerpt states. Do not infer or add outside knowledge.
- Write entity names exactly as they appear in the excerpt.
- If there is nothing to extract, return {"triples": []}.

Return ONLY a JSON object:
{"triples": [{"subject": "...", "subject_type": "...", "relation": "...", "object": "...", "object_type": "..."}]}

Excerpt:
<EXCERPT>"""


def build_prompt(text):
    entity_lines = "\n".join(f"- {name}: {definition}" for name, definition in ENTITY_TYPES.items())
    relation_lines = "\n".join(
        f"- {name} ({', '.join(rule['subject'])} → {', '.join(rule['object'])}): {rule['meaning']}"
        for name, rule in RELATION_TYPES.items())
    # The excerpt is put in last, so nothing in it can be mistaken for a marker
    return (PROMPT.replace("<ENTITY_TYPES>", entity_lines).replace("<RELATION_TYPES>", relation_lines)
            .replace("<EXCERPT>", text))


def error_text(error):
    """A Pydantic error on one line."""
    return "; ".join(f"{'.'.join(str(part) for part in item['loc']) or 'triple'}: {item['msg']}"
                     for item in error.errors())


def extract_chunk(chunk_id, text):
    """[DECISION D40] The extraction entry of one chunk. An LLM error or an output that isn't a JSON
    object with a `triples` list marks the chunk failed. Each triple is validated on its own: an
    invalid one goes to `rejected` and the others are kept. No retry (D15)."""
    failed = {"chunk_id": chunk_id, "status": "failed", "error": None, "triples": [], "rejected": []}
    try:
        raw = rag.call_llm(build_prompt(text))
    except rag.RagError as error:
        return {**failed, "error": {"code": error.code, "message": error.message}}
    try:
        items = json.loads(rag.strip_code_fence(raw))["triples"]
        if not isinstance(items, list):
            raise ValueError("triples is not a list")
    except (ValueError, KeyError, TypeError):
        logger.warning("Invalid extraction output for %s. Raw LLM output: %r", chunk_id, raw)
        return {**failed, "error": {"code": "invalid_llm_response",
                                    "message": "The output is not a JSON object with a triples list."}}
    triples, rejected = [], []
    for item in items:
        try:
            triples.append(Triple.model_validate(item, context=SCHEMA).model_dump())
        except ValidationError as error:
            rejected.append({"triple": item, "error": error_text(error)})
    return {"chunk_id": chunk_id, "status": "ok", "error": None, "triples": triples, "rejected": rejected}
