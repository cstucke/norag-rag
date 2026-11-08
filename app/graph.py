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

# ---------------------------------------------------------------------------
# Chunks and entity resolution
# ---------------------------------------------------------------------------

def kestrel_chunks(settings):
    """[DECISION D44] (chunk_id, text) of every Kestrel chunk at these settings, in document order,
    as stored in the collection (the way words.corpus_chunks reads them, but keeping the texts)."""
    doc_ids = corpus_doc_ids(CORPUS)
    rag.ensure_indexed(doc_ids, settings)
    where = {"doc_id": doc_ids[0]} if len(doc_ids) == 1 else {"doc_id": {"$in": doc_ids}}
    result = rag.get_collection(rag.collection_name(settings)).get(where=where, include=["documents", "metadatas"])
    rows = sorted(zip(result["metadatas"], result["ids"], result["documents"]),
                  key=lambda row: (row[0]["doc_id"], row[0]["chunk_index"]))
    return [(chunk_id, text) for _, chunk_id, text in rows]


def normalize(name):
    """[DECISION D41] Casefolded, every run of characters other than [a-z0-9] turned into one
    space, stripped, a leading "the " removed."""
    text = re.sub(r"[^a-z0-9]+", " ", name.casefold()).strip()
    return text[len("the "):] if text.startswith("the ") else text


def resolve(extractions):
    """[DECISION D41] Nodes and edges from the stored extractions. Two mentions are the same entity
    iff they have the same type and the same normalized name. Edges with the same
    (source, relation, target) are merged: chunk_ids are unioned, count is the number of triples."""
    found = {}  # node id -> {"type", "forms": Counter, "chunk_ids": set}
    merged = {}  # (source, relation, target) -> {"chunk_ids": set, "count": int}
    for extraction in extractions:
        # A failed chunk has no triples, so it adds nothing
        for triple in extraction["triples"]:
            ids = []
            for side in ("subject", "object"):
                kind, name = triple[f"{side}_type"], triple[side]
                node_id = f"{kind}:{normalize(name)}"
                node = found.setdefault(node_id, {"type": kind, "forms": Counter(), "chunk_ids": set()})
                node["forms"][name] += 1
                node["chunk_ids"].add(extraction["chunk_id"])
                ids.append(node_id)
            edge = merged.setdefault((ids[0], triple["relation"], ids[1]), {"chunk_ids": set(), "count": 0})
            edge["chunk_ids"].add(extraction["chunk_id"])
            edge["count"] += 1
    nodes = []
    for node_id, node in sorted(found.items()):
        names = [form for form, _ in sorted(node["forms"].items(), key=lambda item: (-item[1], item[0]))]
        nodes.append({"id": node_id, "type": node["type"], "name": names[0], "names": names,
                      "chunk_ids": sorted(node["chunk_ids"])})
    edges = [{"source": source, "relation": relation, "target": target,
              "chunk_ids": sorted(edge["chunk_ids"]), "count": edge["count"]}
             for (source, relation, target), edge in sorted(merged.items())]
    return nodes, edges

# ---------------------------------------------------------------------------
# Graph file
# ---------------------------------------------------------------------------

def graph_path(settings):
    """[DECISION D42] One file per chunk configuration: the chunk_ids it points to depend on it."""
    return GRAPH_DIR / f"{CORPUS}_cs{settings['chunk_size']}_ov{settings['chunk_overlap']}.json"


def graph_built(settings):
    return graph_path(settings).exists()


def load_graph(settings):
    """The graph file for these settings. A missing or unreadable file is graph_not_built."""
    try:
        with open(graph_path(settings), "r", encoding="utf-8") as f:
            return json.load(f)
    except (OSError, ValueError):
        raise rag.RagError("graph_not_built",
                           f"No concept graph for chunk size {settings['chunk_size']} / "
                           f"overlap {settings['chunk_overlap']}. Run: python -m app.graph build") from None


def write_graph(settings, graph):
    GRAPH_DIR.mkdir(parents=True, exist_ok=True)
    with open(graph_path(settings), "w", encoding="utf-8") as f:
        json.dump(graph, f, indent=2, ensure_ascii=False)
