"""Injection scanner: rules applied line by line to an uploaded document, and the quarantine where
a flagged upload waits for the user's review. No LLM call: the suspicious text is never sent to the
model it targets. CLI: python -m app.scanner <path> [<path> ...]"""
import argparse
import hashlib
import json
import re
import sys
from datetime import datetime, timezone
from pathlib import Path

from app import rag
from app.config import QUARANTINE_DIR

EXCERPT_CHARS = 200

# [DECISION D58] (name, pattern, what it catches in plain words). Case-insensitive, one line at a time
RULES = [
    ("override_instructions",
     re.compile(r"\b(ignore|disregard|forget|override)\b[^.\n]{0,40}?"
                r"\b(previous|prior|above|earlier|preceding|all|any|your|these|those|the)\b[^.\n]{0,20}?"
                r"\b(instructions?|rules?|prompts?|directions?|guidelines?)\b", re.IGNORECASE),
     "Tells the model to ignore its instructions"),
    ("new_role",
     re.compile(r"\byou are now\b|\bfrom now on,? you\b|\bpretend (to be|you are)\b", re.IGNORECASE),
     "Gives the model a new role"),
    ("system_marker",
     re.compile(r"^\s*(system\s*:|<\|im_start\|>|<\|system\|>|\[INST\]|<<SYS>>)", re.IGNORECASE),
     "Imitates a system or chat-template marker"),
    ("prompt_leak",
     re.compile(r"\b(reveal|print|show|display|output|repeat|leak|tell me|give me)\b[^.\n]{0,30}?"
                r"(system prompt|\byour (instructions|prompt|rules)\b|\b(the )?(api|secret) key\b)", re.IGNORECASE),
     "Asks the model to reveal its prompt or a key"),
    ("answer_hijack",
     re.compile(r"\b(respond|reply|answer) only with\b|\bonly (respond|reply|answer) with\b|\bdo not (mention|reveal|tell|say)\b"
                r"|\balways (answer|respond|reply|say)\b", re.IGNORECASE),
     "Dictates what the answer must say"),
    ("addressed_to_model",
     re.compile(r"\b(note|message|instructions?)\s+(to|for)\s+(the\s+|any\s+)?"
                r"(ai|assistant|ai assistant|language model|llm|chatbot)\b", re.IGNORECASE),
     "Addresses the AI model directly"),
    ("hidden_text",
     re.compile(r"[​-‏‪-‮⁠-⁤⁦-⁩﻿]|<!--.*?-->", re.IGNORECASE),
     "Contains invisible characters or a hidden HTML comment"),
    ("exfiltration",
     re.compile(r"\b(send|post|upload|forward|transmit|submit|email)\b[^\n]{0,80}?\bto\b[^\n]{0,20}?https?://"
                r"|!\[[^\]\n]*\]\([^)\s]*\?[^)\s]*\)", re.IGNORECASE),
     "Tries to send data to an outside address"),
]
RULE_DESCRIPTIONS = {name: description for name, _, description in RULES}


def scan(text):
    """[{rule, line, excerpt}] for every rule a line matches. excerpt is that line, cut."""
    # A byte-order mark at the very start of the file is how some editors save UTF-8, not hidden text
    text = text.removeprefix("﻿")
    findings = []
    for number, line in enumerate(text.splitlines(), 1):
        for name, pattern, _ in RULES:
            if pattern.search(line):
                findings.append({"rule": name, "line": number, "excerpt": line.strip()[:EXCERPT_CHARS]})
    return findings

# ---------------------------------------------------------------------------
# Quarantine: data/quarantine/<name> and its sidecar <name>.json
# ---------------------------------------------------------------------------

def quarantine_path(name):
    return QUARANTINE_DIR / name


def sidecar_path(name):
    return QUARANTINE_DIR / f"{name}.json"


def quarantine(name, raw_bytes, findings):
    """[DECISION D59] Store the whole upload unchanged, with what was found in it."""
    QUARANTINE_DIR.mkdir(parents=True, exist_ok=True)
    quarantine_path(name).write_bytes(raw_bytes)
    sidecar = {"filename": name, "uploaded_at": datetime.now(timezone.utc).isoformat(timespec="seconds"),
               "sha256": hashlib.sha256(raw_bytes).hexdigest(), "findings": findings}
    with open(sidecar_path(name), "w", encoding="utf-8") as f:
        json.dump(sidecar, f, indent=2)


def list_quarantine():
    """The sidecars of the files waiting for review, oldest first."""
    if not QUARANTINE_DIR.exists():
        return []
    waiting = []
    for path in QUARANTINE_DIR.glob("*.json"):
        with open(path, "r", encoding="utf-8") as f:
            sidecar = json.load(f)
        if quarantine_path(sidecar["filename"]).is_file():
            waiting.append(sidecar)
    return sorted(waiting, key=lambda sidecar: (sidecar["uploaded_at"], sidecar["filename"]))


def waiting_name(filename):
    """The filename if it is in the list, else quarantine_not_found. Comparing with the list is also
    the path guard: a name like "../x" is never used to build a path."""
    if not isinstance(filename, str) or filename not in {s["filename"] for s in list_quarantine()}:
        raise rag.RagError("quarantine_not_found")
    return filename


def approve(filename):
    """Move the file to corpus/uploads/ unchanged and return its document_info."""
    name = waiting_name(filename)
    destination = rag.UPLOADS_DIR / name
    if destination.exists():
        raise rag.RagError("document_exists")
    rag.UPLOADS_DIR.mkdir(parents=True, exist_ok=True)
    quarantine_path(name).replace(destination)
    sidecar_path(name).unlink()
    return rag.document_info(destination)


def reject(filename):
    name = waiting_name(filename)
    quarantine_path(name).unlink()
    sidecar_path(name).unlink()

# ---------------------------------------------------------------------------
# CLI: python -m app.scanner corpus/forest corpus/kestrel
# ---------------------------------------------------------------------------

def main():
    """[DECISION D60] Reports only; nothing is moved."""
    parser = argparse.ArgumentParser(description="Scan files or folders for prompt injection. Moves nothing.")
    parser.add_argument("paths", nargs="+", type=Path)
    args = parser.parse_args()
    files = []
    for path in args.paths:
        if path.is_dir():
            files += sorted(p for p in path.rglob("*") if p.is_file() and p.suffix.lower() in rag.DOC_EXTENSIONS)
        elif path.is_file():
            files.append(path)
        else:
            sys.exit(f"Not found: {path}")
    flagged, by_rule = 0, {name: 0 for name, _, _ in RULES}
    for path in files:
        try:
            findings = scan(path.read_text(encoding="utf-8"))
        except UnicodeDecodeError:
            print(f"{path}: not UTF-8, skipped")
            continue
        if not findings:
            continue
        flagged += 1
        print(f"{path}: {len(findings)} finding(s)")
        for finding in findings:
            by_rule[finding["rule"]] += 1
            print(f"  line {finding['line']}  {finding['rule']}  {finding['excerpt']!r}")
    print(f"\n{len(files)} files scanned, {flagged} flagged")
    for name, count in by_rule.items():
        print(f"  {name}: {count}")


if __name__ == "__main__":
    main()
