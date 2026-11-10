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


# ---------------------------------------------------------------------------
# Build
# ---------------------------------------------------------------------------

def extract_all(chunks, sleep):
    """One extraction entry per (chunk_id, text), printing one progress line each. `sleep` seconds
    are waited between calls, for rate limits."""
    extractions = []
    for number, (chunk_id, text) in enumerate(chunks, 1):
        if number > 1 and sleep:
            time.sleep(sleep)
        entry = extract_chunk(chunk_id, text)
        extractions.append(entry)
        detail = f" ({entry['error']['code']})" if entry["error"] else ""
        print(f"[{number}/{len(chunks)}] {chunk_id}: {entry['status']}{detail}, "
              f"{len(entry['triples'])} triples, {len(entry['rejected'])} rejected")
    return extractions


def need_api_key():
    # Not a per-chunk failure: without a key every call would fail and overwrite a good graph file
    if not rag.GOOGLE_API_KEY:
        raise rag.RagError("llm_not_configured")


def cost_since(before, start):
    """[DECISION D42] Build cost from the USAGE difference and the wall time. Only calls that
    got an answer are counted (D46)."""
    return {"llm_calls": rag.USAGE["calls"] - before["calls"],
            "prompt_tokens": rag.USAGE["prompt_tokens"] - before["prompt_tokens"],
            "completion_tokens": rag.USAGE["completion_tokens"] - before["completion_tokens"],
            "seconds": time.perf_counter() - start}


def count_problems(extractions):
    return {"failed_chunks": sum(entry["status"] == "failed" for entry in extractions),
            "rejected_triples": sum(len(entry["rejected"]) for entry in extractions)}


def build(settings, sleep):
    """Extracts every Kestrel chunk, resolves, writes the graph file."""
    need_api_key()
    chunks = kestrel_chunks(settings)
    print(f"{len(chunks)} Kestrel chunks, so {len(chunks)} LLM calls.")
    started_at = datetime.now(timezone.utc).isoformat(timespec="seconds")
    before, start = dict(rag.USAGE), time.perf_counter()
    extractions = extract_all(chunks, sleep)
    cost = cost_since(before, start)
    nodes, edges = resolve(extractions)
    graph = {"config": {"corpus": CORPUS, "chunk_size": settings["chunk_size"],
                        "chunk_overlap": settings["chunk_overlap"], "model": GEMINI_MODEL,
                        "entity_types": ENTITY_TYPES, "relation_types": RELATION_TYPES,
                        "prompt_template": PROMPT},
             "build": {"started_at": started_at, "chunks": len(chunks), **cost, **count_problems(extractions)},
             "extractions": extractions, "nodes": nodes, "edges": edges}
    graph["build"]["seconds"] = round(graph["build"]["seconds"], 1)
    write_graph(settings, graph)
    print(f"Wrote {graph_path(settings)}")


def retry_failed(settings, sleep):
    """Re-extracts only the failed chunks of the existing file, re-resolves, adds their cost to build."""
    graph = load_graph(settings)
    texts = dict(kestrel_chunks(settings))
    todo = [number for number, entry in enumerate(graph["extractions"])
            if entry["status"] == "failed" and entry["chunk_id"] in texts]
    if not todo:
        print("No failed chunk to retry.")
        return
    need_api_key()
    print(f"{len(todo)} failed chunks, so {len(todo)} LLM calls.")
    before, start = dict(rag.USAGE), time.perf_counter()
    redone = extract_all([(graph["extractions"][number]["chunk_id"], texts[graph["extractions"][number]["chunk_id"]])
                          for number in todo], sleep)
    cost = cost_since(before, start)
    for number, entry in zip(todo, redone):
        graph["extractions"][number] = entry
    build = graph["build"]
    for field in ("llm_calls", "prompt_tokens", "completion_tokens"):
        build[field] += cost[field]
    build["seconds"] = round(build["seconds"] + cost["seconds"], 1)
    build.update(count_problems(graph["extractions"]))
    graph["nodes"], graph["edges"] = resolve(graph["extractions"])
    write_graph(settings, graph)
    print(f"Wrote {graph_path(settings)}")


def resolve_again(settings):
    """Rebuilds nodes and edges from the stored extractions, with no LLM call, to try a change of the
    resolution rule for free."""
    graph = load_graph(settings)
    graph["nodes"], graph["edges"] = resolve(graph["extractions"])
    write_graph(settings, graph)
    print(f"Wrote {graph_path(settings)}: {len(graph['nodes'])} entities, {len(graph['edges'])} edges")

# ---------------------------------------------------------------------------
# Stats
# ---------------------------------------------------------------------------

def print_stats(settings):
    graph = load_graph(settings)
    nodes, edges, build = graph["nodes"], graph["edges"], graph["build"]
    print(f"Graph file: {graph_path(settings)}")
    per_type = Counter(node["type"] for node in nodes)
    print(f"Entities: {len(nodes)}")
    for kind in ENTITY_TYPES:
        print(f"  {kind}: {per_type[kind]}")
    per_relation = Counter(edge["relation"] for edge in edges)
    print(f"Edges: {len(edges)}")
    for relation in RELATION_TYPES:
        print(f"  {relation}: {per_relation[relation]}")
    merges = [node for node in nodes if len(node["names"]) > 1]
    print(f"Merges (entities with more than one surface form): {len(merges)}")
    for node in merges:
        print(f"  {node['id']}: " + " | ".join(node["names"]))
    # The same normalized name under different types: the type rule kept them apart
    by_name = {}
    for node in nodes:
        by_name.setdefault(node["id"].split(":", 1)[1], []).append(node["id"])
    missed = {name: ids for name, ids in by_name.items() if len(ids) > 1}
    print(f"Possible missed merges (same normalized name, different types): {len(missed)}")
    for name, ids in sorted(missed.items()):
        print(f"  {name!r}: " + ", ".join(ids))
    failed = [entry for entry in graph["extractions"] if entry["status"] == "failed"]
    print(f"Failed chunks: {len(failed)}")
    for entry in failed:
        print(f"  {entry['chunk_id']}: {entry['error']['code']}")
    rejected = [(entry["chunk_id"], item) for entry in graph["extractions"] for item in entry["rejected"]]
    print(f"Rejected triples: {len(rejected)}")
    for chunk_id, item in rejected:
        print(f"  {chunk_id}: {json.dumps(item['triple'], ensure_ascii=False)} -> {item['error']}")
    print(f"Build: {build['chunks']} chunks, {build['llm_calls']} LLM calls, {build['prompt_tokens']} prompt / "
          f"{build['completion_tokens']} completion tokens, {build['seconds']} s (started {build['started_at']})")

# ---------------------------------------------------------------------------
# Retriever
# ---------------------------------------------------------------------------

HOP_WEIGHTS = {1: 1.0, 2: 0.5}


def link_entities(question, nodes):
    """[DECISION D43] Entity linking by string matching, no LLM. A node matches if one of its surface
    forms (normalized, at least 2 characters) appears in the normalized question as whole words. A
    matched form contained in a longer matched form doesn't count. Returns the seed nodes, by id."""
    text = f" {normalize(question)} "
    matched = []  # (normalized form, node)
    for node in nodes:
        for form in node["names"]:
            norm = normalize(form)
            if len(norm) >= 2 and f" {norm} " in text:
                matched.append((norm, node))
    seeds = {node["id"]: node for norm, node in matched
             if not any(len(other) > len(norm) and f" {norm} " in f" {other} " for other, _ in matched)}
    return [seeds[node_id] for node_id in sorted(seeds)]


def doc_id_of_chunk(chunk_id):
    """chunk ids are {doc_id}#cs{size}-ov{overlap}#{index}"""
    return re.fullmatch(r"(.+)#cs\d+-ov\d+#\d+", chunk_id).group(1)


def graph_search(question, doc_ids, settings, n):
    """[DECISION D43] Returns (chunk_ids, info): up to n chunks of the selected docs, best first, and the
    path behind them. Seeds are the entities found in the question. Breadth-first over edges, in both
    directions, up to 2 hops: an edge touching a seed is hop 1, an edge touching a hop-1 neighbour (and
    no seed) is hop 2. Each followed edge adds 1.0 (hop 1) or 0.5 (hop 2) to every chunk it comes from.
    No seed: no chunk."""
    graph = load_graph(settings)
    names = {node["id"]: node["name"] for node in graph["nodes"]}
    seeds = link_entities(question, graph["nodes"])
    seed_ids = {node["id"] for node in seeds}

    followed = []  # (hop, edge)
    for edge in graph["edges"]:
        if {edge["source"], edge["target"]} & seed_ids:
            followed.append((1, edge))
    neighbours = {end for _, edge in followed for end in (edge["source"], edge["target"])} - seed_ids
    for edge in graph["edges"]:
        ends = {edge["source"], edge["target"]}
        if not ends & seed_ids and ends & neighbours:
            followed.append((2, edge))

    scores = {}
    for hop, edge in followed:
        for chunk_id in edge["chunk_ids"]:
            scores[chunk_id] = scores.get(chunk_id, 0.0) + HOP_WEIGHTS[hop]
    selected = set(doc_ids)
    ranked = sorted((chunk_id for chunk_id in scores if doc_id_of_chunk(chunk_id) in selected),
                    key=lambda chunk_id: (-scores[chunk_id], chunk_id))
    if ranked:
        # A graph built before the corpus changed can point at chunks that no longer exist
        present = set(rag.get_collection(rag.collection_name(settings)).get(ids=ranked, include=[])["ids"])
        ranked = [chunk_id for chunk_id in ranked if chunk_id in present]
    info = {"entities": [{"id": node["id"], "name": node["name"], "type": node["type"]} for node in seeds],
            "edges": [{"source": edge["source"], "relation": edge["relation"], "target": edge["target"],
                       "source_name": names[edge["source"]], "target_name": names[edge["target"]],
                       "hop": hop, "chunk_ids": edge["chunk_ids"]} for hop, edge in followed]}
    return ranked[:n], info


def context_path(info, chunks):
    """What the UI shows: the seeds, and the followed edges that have a chunk in the context sent to
    the LLM, each with only those chunk ids. None when the graph is off."""
    if info is None:
        return None
    in_context = {chunk["id"] for chunk in chunks}
    edges = []
    for edge in info["edges"]:
        shown = [chunk_id for chunk_id in edge["chunk_ids"] if chunk_id in in_context]
        if shown:
            edges.append({**edge, "chunk_ids": shown})
    return {"entities": info["entities"], "edges": edges}

# ---------------------------------------------------------------------------
# CLI: python -m app.graph build | resolve | stats
# ---------------------------------------------------------------------------

def main():
    parser = argparse.ArgumentParser(description="Concept graph of the Kestrel corpus, at the saved settings.")
    commands = parser.add_subparsers(dest="command", required=True)
    build_parser = commands.add_parser("build", help="extract every chunk (one LLM call each) and write the graph")
    build_parser.add_argument("--sleep", type=float, default=0, help="seconds to wait between calls")
    build_parser.add_argument("--retry-failed", action="store_true",
                              help="only re-extract the failed chunks of the existing file")
    commands.add_parser("resolve", help="rebuild nodes and edges from the stored extractions (no LLM call)")
    commands.add_parser("stats", help="print the graph's numbers, merges and build cost")
    args = parser.parse_args()
    settings = load_settings()
    try:
        if args.command == "build":
            (retry_failed if args.retry_failed else build)(settings, args.sleep)
        elif args.command == "resolve":
            resolve_again(settings)
        else:
            print_stats(settings)
    except rag.RagError as error:
        sys.exit(error.message)


if __name__ == "__main__":
    main()
