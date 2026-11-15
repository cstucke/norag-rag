"""Study artifacts: flashcards or multiple-choice questions written by the LLM from the chunks of the
selected documents. One LLM call per set. Every item names its excerpt and quotes it word for word,
and an item whose quote isn't in that excerpt is dropped."""
import json
import logging
import random
import time
from collections import Counter

from pydantic import ValidationError

from app import rag, trace
from app.schemas import ChoiceQuestion, Flashcard

# [DECISION D55] Chunks shorter than this hold too little to ask about; at most this many are sent
MIN_EXCERPT_CHARS = 200
MAX_EXCERPTS = 12
MIN_QUOTE_CHARS = 15
TYPES = {"flashcards": ("flashcards", Flashcard), "multiple_choice": ("multiple-choice questions", ChoiceQuestion)}
MAX_COUNT = 10
# [DECISION D56]
DIFFICULTIES = {
    "easy": "a fact one sentence states directly",
    "medium": "a condition, a number or an exception",
    "hard": "needs two statements of the same excerpt",
}

PROMPT = """You write study material from the numbered excerpts below, taken from the documents the user selected.
Write {count} {kind}. Difficulty: {difficulty} ({definition}).

Rules:
- Use ONLY the excerpts. Do not use outside knowledge.
- Each item is about one excerpt. Give its number in "excerpt".
- "quote" is a short passage copied word for word from that excerpt. It must contain the answer.
- Use different excerpts for different items when you can.
- If the excerpts hold fewer usable facts, write fewer items.
{choice_rules}
Return ONLY a JSON object:
{shape}

Excerpts:
{excerpts}"""

CHOICE_RULES = """- Give exactly 4 options. Exactly one is right. "answer" is its position, 1 to 4.
- The wrong options must be plausible, and wrong according to the excerpts.
"""
SHAPES = {
    "flashcards": '{"items": [{"question": "...", "answer": "...", "excerpt": 1, "quote": "..."}]}',
    "multiple_choice": '{"items": [{"question": "...", "options": ["...", "...", "...", "..."], '
                       '"answer": 2, "excerpt": 1, "quote": "..."}]}',
}

logger = logging.getLogger(__name__)


def check_request(body):
    """(doc_ids, type, count, difficulty) from the raw request body. A bad value is
    invalid_study_request naming the field; no documents is no_documents_selected."""
    body = body if isinstance(body, dict) else {}
    kind, count, difficulty, doc_ids = body.get("type"), body.get("count"), body.get("difficulty"), body.get("doc_ids")
    if kind not in TYPES:
        raise rag.RagError("invalid_study_request", "Invalid study request: type must be flashcards or multiple_choice.")
    # bool is a subclass of int in Python, so reject it explicitly
    if not isinstance(count, int) or isinstance(count, bool) or not 1 <= count <= MAX_COUNT:
        raise rag.RagError("invalid_study_request", f"Invalid study request: count must be a whole number from 1 to {MAX_COUNT}.")
    if difficulty not in DIFFICULTIES:
        raise rag.RagError("invalid_study_request", "Invalid study request: difficulty must be easy, medium or hard.")
    # Malformed doc_ids count as missing, as in /api/ask
    if not isinstance(doc_ids, list) or not all(isinstance(doc_id, str) for doc_id in doc_ids) or not doc_ids:
        raise rag.RagError("no_documents_selected")
    return list(dict.fromkeys(doc_ids)), kind, count, difficulty


def select_chunks(doc_ids, settings):
    """[DECISION D55] The chunks of the selected documents as stored in the collection, without the
    short ones, at most MAX_EXCERPTS of them picked at random, in document order."""
    where = {"doc_id": doc_ids[0]} if len(doc_ids) == 1 else {"doc_id": {"$in": doc_ids}}
    result = rag.get_collection(rag.collection_name(settings)).get(where=where, include=["documents", "metadatas"])
    chunks = [{"id": chunk_id, "text": text, "metadata": metadata}
              for chunk_id, text, metadata in zip(result["ids"], result["documents"], result["metadatas"])
              if len(text.strip()) >= MIN_EXCERPT_CHARS]
    position = {doc_id: i for i, doc_id in enumerate(doc_ids)}
    order = lambda chunk: (position[chunk["metadata"]["doc_id"]], chunk["metadata"]["chunk_index"])
    # The seed goes into the trace, so the same pick can be made again
    seed = random.randrange(2**32)
    with trace.span("select", available=len(chunks), seed=seed) as attrs:
        if len(chunks) > MAX_EXCERPTS:
            chunks = random.Random(seed).sample(chunks, MAX_EXCERPTS)
        chunks.sort(key=order)
        attrs["chunk_ids"] = [chunk["id"] for chunk in chunks]
        if not chunks:
            raise rag.RagError("empty_document", "The selected documents are too short to make a quiz from.")
    return chunks


def build_prompt(chunks, kind, count, difficulty):
    excerpts = "\n\n".join(
        f"[{rank}] (source: {chunk['metadata']['title']}, "
        f"lines {chunk['metadata']['line_start']}-{chunk['metadata']['line_end']})\n{chunk['text']}"
        for rank, chunk in enumerate(chunks, 1))
    return PROMPT.format(count=count, kind=TYPES[kind][0], difficulty=difficulty, definition=DIFFICULTIES[difficulty],
                         choice_rules=CHOICE_RULES if kind == "multiple_choice" else "", shape=SHAPES[kind],
                         excerpts=excerpts)


def collapse(text):
    return " ".join(text.split())


def check_item(raw_item, kind, chunks):
    """The validated item, or the reason it is dropped."""
    try:
        item = TYPES[kind][1].model_validate(raw_item)
    except ValidationError:
        return None, "missing_or_empty_field"
    if not 1 <= item.excerpt <= len(chunks):
        return None, "excerpt_out_of_range"
    if len(item.quote) < MIN_QUOTE_CHARS:
        return None, "quote_too_short"
    if collapse(item.quote) not in collapse(chunks[item.excerpt - 1]["text"]):
        return None, "quote_not_in_excerpt"
    if kind == "multiple_choice" and (len(item.options) != 4 or len(set(item.options)) != 4):
        return None, "not_four_different_options"
    if kind == "multiple_choice" and not 1 <= item.answer <= 4:
        return None, "answer_out_of_range"
    return item, None


def parse_items(raw, kind, count, chunks):
    """[DECISION D57] No retry, no repair (D15). Output that isn't a JSON object with an items list is
    invalid_llm_response; each item is then checked on its own and dropped if it fails.
    Returns (kept items, number dropped)."""
    with trace.span("validate") as attrs:
        try:
            output = json.loads(rag.strip_code_fence(raw))
            if not isinstance(output, dict) or not isinstance(output.get("items"), list):
                raise ValueError("not a JSON object with an items list")
        except ValueError as reason:
            logger.warning("invalid_llm_response (%s). Raw LLM output: %r", reason, raw)
            raise rag.RagError("invalid_llm_response") from None
        attrs["returned"] = len(output["items"])
        kept, dropped = [], Counter()
        for raw_item in output["items"]:
            item, reason = check_item(raw_item, kind, chunks)
            if item is None:
                dropped[reason] += 1
            else:
                kept.append(item)
        attrs.update(kept=len(kept), dropped=dict(dropped))
        if not kept:
            raise rag.RagError("no_study_items")
    return kept[:count], sum(dropped.values())


def to_response_item(item, chunks):
    meta = chunks[item.excerpt - 1]["metadata"]
    shown = {"question": item.question}
    if isinstance(item, ChoiceQuestion):
        shown["options"] = item.options
    shown.update(answer=item.answer, quote=item.quote,
                 reference={"chunk_id": chunks[item.excerpt - 1]["id"], "doc_id": meta["doc_id"],
                            "title": meta["title"], "line_start": meta["line_start"], "line_end": meta["line_end"]})
    return shown


def generate(body, settings):
    """The whole /api/study logic. Every failure is raised as RagError."""
    start = time.perf_counter()
    doc_ids, kind, count, difficulty = check_request(body)
    with trace.span("index", docs_checked=len(doc_ids)) as attrs:
        attrs["docs_indexed"] = rag.ensure_indexed(doc_ids, settings)
    chunks = select_chunks(doc_ids, settings)
    with trace.span("prompt", excerpts=len(chunks)) as attrs:
        prompt = build_prompt(chunks, kind, count, difficulty)
        attrs["chars"] = len(prompt)
    # [DECISION D46] This set's cost is the difference in the running totals
    usage_before = dict(rag.USAGE)
    raw = rag.call_llm(prompt)
    usage = {key: rag.USAGE[key] - usage_before[key] for key in rag.USAGE}
    items, dropped = parse_items(raw, kind, count, chunks)
    return {"status": "ok", "type": kind, "requested": count, "dropped": dropped,
            "items": [to_response_item(item, chunks) for item in items],
            "cost": {"llm_calls": usage["calls"], "prompt_tokens": usage["prompt_tokens"],
                     "completion_tokens": usage["completion_tokens"],
                     "cost_usd": round(trace.cost_usd(usage["prompt_tokens"], usage["completion_tokens"]), 6),
                     "ms": trace.elapsed_ms(start)}}
