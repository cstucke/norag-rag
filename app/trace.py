"""Traces: one JSON line per request or indexing run, in data/traces/<UTC date>.jsonl.
A trace is a list of spans, one per step. Nothing here imports app.rag, which imports this module."""
import contextlib
import contextvars
import json
import logging
import re
import threading
import time
import uuid
from datetime import datetime, timedelta, timezone

from app.config import PRICE_PER_M_COMPLETION_USD, PRICE_PER_M_PROMPT_USD, TRACES_DIR

# [DECISION D52] Trace files older than this are deleted when a new day's file is created
TRACE_RETENTION_DAYS = 30
# [DECISION D48] The id starts with the UTC date, so find() opens one file
TRACE_ID_RE = re.compile(r"(\d{4})(\d{2})(\d{2})-[0-9a-f]{12}")
TRACE_FILE_RE = re.compile(r"(\d{4}-\d{2}-\d{2})\.jsonl")

logger = logging.getLogger(__name__)

# The trace of the request or command being served. None outside one, which makes span() record nothing
_current = contextvars.ContextVar("trace", default=None)
# Requests run on several threads; a line is written whole
_write_lock = threading.Lock()


def elapsed_ms(since):
    return round((time.perf_counter() - since) * 1000, 1)


def cost_usd(prompt_tokens, completion_tokens):
    """[DECISION D53] Cost of one LLM call, from the two prices in config.py."""
    return (prompt_tokens * PRICE_PER_M_PROMPT_USD + completion_tokens * PRICE_PER_M_COMPLETION_USD) / 1_000_000

# ---------------------------------------------------------------------------
# Recording
# ---------------------------------------------------------------------------

def start(kind, **attrs):
    """Begin the trace of one request or command (kind: ask, study, upload, review, index).
    It replaces any trace still active."""
    now = datetime.now(timezone.utc)
    current = {"trace_id": f"{now:%Y%m%d}-{uuid.uuid4().hex[:12]}", "kind": kind,
               "started_at": now.isoformat(timespec="seconds"), "ms": None, "outcome": None,
               "attrs": attrs, "llm": None, "spans": [],
               # Working state, removed by finish(): the clock, and the indexes of the spans still open
               "_clock": time.perf_counter(), "_open": []}
    _current.set(current)
    return current


@contextlib.contextmanager
def span(name, **attrs):
    """One step of the active trace. Yields the span's attributes, for the step to add to.
    With no active trace (the evaluation, for instance) it records nothing.
    [DECISION D49] Attributes hold ids, counts and names, never a prompt or the text of a chunk."""
    current = _current.get()
    if current is None:
        yield attrs
        return
    entry = {"name": name, "parent": current["_open"][-1] if current["_open"] else None,
             "start_ms": elapsed_ms(current["_clock"]), "ms": None, "error": None, "attrs": attrs}
    current["spans"].append(entry)
    current["_open"].append(len(current["spans"]) - 1)
    start_time = time.perf_counter()
    try:
        yield attrs
    except Exception as error:
        # A RagError carries its catalogue code
        entry["error"] = getattr(error, "code", None) or type(error).__name__
        raise
    finally:
        entry["ms"] = elapsed_ms(start_time)
        current["_open"].pop()


def finish(outcome, **attrs):
    """End the active trace, write it and return its id. None if no trace is active."""
    current = _current.get()
    if current is None:
        return None
    _current.set(None)
    current["ms"] = elapsed_ms(current["_clock"])
    current["outcome"] = outcome
    current["attrs"].update(attrs)
    # Only the calls that got an answer, as rag.USAGE counts them (D46)
    calls = [entry["attrs"] for entry in current["spans"] if entry["name"] == "llm" and entry["error"] is None]
    current["llm"] = {"calls": len(calls),
                      "prompt_tokens": sum(call.get("prompt_tokens", 0) for call in calls),
                      "completion_tokens": sum(call.get("completion_tokens", 0) for call in calls),
                      "cost_usd": round(sum(call.get("cost_usd", 0.0) for call in calls), 6)}
    del current["_clock"], current["_open"]
    write(current)
    return current["trace_id"]

# ---------------------------------------------------------------------------
# Storage
# ---------------------------------------------------------------------------

def write(finished):
    """[DECISION D48] Append one line to the file of the trace's UTC day. A failed write is
    logged and nothing more: tracing must never make a request fail."""
    path = TRACES_DIR / f"{finished['started_at'][:10]}.jsonl"
    try:
        with _write_lock:
            TRACES_DIR.mkdir(parents=True, exist_ok=True)
            new_day = not path.exists()
            with open(path, "a", encoding="utf-8") as f:
                # default=str: an attribute of an unexpected type is written as text
                f.write(json.dumps(finished, default=str) + "\n")
            if new_day:
                delete_old_files()
    except OSError as error:
        logger.warning("Trace %s not written: %s", finished["trace_id"], error)


def delete_old_files():
    """[DECISION D52] Only files named like a trace file are deleted."""
    cutoff = (datetime.now(timezone.utc) - timedelta(days=TRACE_RETENTION_DAYS)).date().isoformat()
    for path in TRACES_DIR.iterdir():
        match = TRACE_FILE_RE.fullmatch(path.name)
        if match and match.group(1) < cutoff:
            path.unlink()


def find(trace_id):
    """The trace with this id, or None. An id of any other form is never used to build a path."""
    match = TRACE_ID_RE.fullmatch(trace_id)
    if not match:
        return None
    path = TRACES_DIR / f"{'-'.join(match.groups())}.jsonl"
    try:
        with open(path, "r", encoding="utf-8") as f:
            for line in f:
                finished = json.loads(line)
                if finished["trace_id"] == trace_id:
                    return finished
    except (OSError, ValueError):
        pass
    return None
