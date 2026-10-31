"""No-context test (RAG_V2_SPEC.md, Step 5): every question goes to the LLM without retrieval.

    python -m evaluation.no_context --questions evaluation/questions/kestrel.jsonl --corpus kestrel

The user fills in `correct` and `note` in the results file.
"""
import argparse
import hashlib
import json
import sys
from datetime import datetime, timezone
from pathlib import Path

from app import rag
from app.config import GEMINI_MODEL
from evaluation.run import RESULTS_DIR, load_questions

# [DECISION D25] The domain tells the model what the question is about, nothing more
NO_CONTEXT_DOMAINS = {
    "forest": "The Forest, the survival horror video game by Endnight Games",
    "kestrel": "the company Kestrel Analytics",
}
PROMPT = """Answer this question about {domain} from your own knowledge.
If you don't know, say so.

Return ONLY a JSON object: {{"answer": "<string>"}}

Question: {question}"""


def run_no_context(questions_path, corpus):
    """Ask every question, unanswerable ones included. Returns the results path."""
    if corpus not in NO_CONTEXT_DOMAINS:
        raise rag.RagError("unknown_corpus", f"Corpus not found: {corpus}")
    domain = NO_CONTEXT_DOMAINS[corpus]

    entries = []
    for question in load_questions(questions_path, corpus):
        output, error = None, None
        try:
            output = rag.call_llm(PROMPT.format(domain=domain, question=question["question"]))
        except rag.RagError as failure:
            error = {"code": failure.code, "message": failure.message}
        entries.append({"id": question["id"], "type": question["type"], "question": question["question"],
                        "expected_answer": question["expected_answer"], "model_output": output, "error": error,
                        "correct": None, "note": ""})
        print(f"{question['id']}: {(error['message'] if error else output)[:80]!r}")

    RESULTS_DIR.mkdir(exist_ok=True)
    stamp = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")
    out = RESULTS_DIR / f"{stamp}_{corpus}_nocontext.json"
    report = {"config": {"model": GEMINI_MODEL, "corpus": corpus,
                         "prompt_template": PROMPT.format(domain=domain, question="<question>")},
              "questions_sha256": hashlib.sha256(questions_path.read_bytes()).hexdigest(),
              "questions": entries}
    out.write_text(json.dumps(report, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    return out


def main():
    parser = argparse.ArgumentParser(description="Ask every question to the LLM without retrieval.")
    parser.add_argument("--questions", required=True, type=Path)
    parser.add_argument("--corpus", required=True)
    args = parser.parse_args()
    try:
        print(f"Results: {run_no_context(args.questions, args.corpus)}")
    except rag.RagError as error:
        sys.exit(error.message)


if __name__ == "__main__":
    main()