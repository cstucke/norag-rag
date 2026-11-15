"""Conversation mode: a follow-up question is rewritten into one that stands on its own before
retrieval, from the turns the page sends with it. One extra LLM call per turn, none on the first.
The suggested next questions come back with the answer itself, so they cost no call."""
import json
import logging

from app import rag, trace

# [DECISION D67] The history lives in the page and comes with each request. Only the last turns
# are used, so the rewrite prompt stays bounded however long the conversation runs
MAX_HISTORY_TURNS = 6
MAX_FOLLOW_UPS = 3

# [DECISION D68]
REWRITE_PROMPT = """Below is a conversation between a user and an assistant that answers from the user's documents, then the user's new question.
Rewrite the new question as ONE question that can be understood with no conversation behind it.

Rules:
- Replace every pronoun and fill in every omitted word using the conversation ("it", "that plan", "and for the other one?").
- A short follow-up such as "and for X?" or "what about Y?" asks the SAME thing as the user's previous question, about a new subject. Keep what was asked and change only the subject, even if an earlier answer already covers it. After "How much does the red model weigh?", the follow-up "and the blue one?" becomes "How much does the blue model weigh?".
- Keep the user's wording and language where you can. Do not broaden the question. Do not answer it.
- If the new question already stands on its own, return it unchanged and set "used_history" to false.

Return ONLY a JSON object:
{{"standalone": "<the question>", "used_history": true|false}}

Conversation:
{turns}

New question: {question}"""

logger = logging.getLogger(__name__)


def clean_history(history):
    """The last MAX_HISTORY_TURNS turns, oldest first: [{question, answer}]. The body is read raw,
    so anything that isn't a list of such turns counts as no history."""
    if not isinstance(history, list):
        return []
    for turn in history:
        if not (isinstance(turn, dict) and isinstance(turn.get("question"), str)
                and isinstance(turn.get("answer"), str)):
            return []
    return [{"question": turn["question"], "answer": turn["answer"]} for turn in history[-MAX_HISTORY_TURNS:]]


def build_rewrite_prompt(question, history):
    turns = "\n".join(f"User: {turn['question']}\nAssistant: {turn['answer']}" for turn in history)
    return REWRITE_PROMPT.format(turns=turns, question=question)


def standalone(question, history):
    """[DECISION D68] The question rewritten to stand on its own, from one LLM call.
    [DECISION D69] A failed rewrite never fails the turn: on an LLM error or an unusable reply the
    question comes back as typed, and the span says why. A rewrite only improves the query,
    so this is the opposite of D15's no-repair rule for an answer."""
    with trace.span("rewrite", history_turns=len(history), changed=False, fell_back=False) as attrs:
        try:
            raw = rag.call_llm(build_rewrite_prompt(question, history))
            output = json.loads(rag.strip_code_fence(raw))
            rewritten = output.get("standalone") if isinstance(output, dict) else None
            if not isinstance(rewritten, str) or not rewritten.strip():
                raise ValueError("no standalone question in the reply")
        except rag.RagError as error:
            attrs.update(fell_back=True, reason=error.code)
            return question
        except ValueError as reason:
            logger.warning("Rewrite not usable (%s). Raw LLM output: %r", reason, raw)
            attrs.update(fell_back=True, reason="invalid_rewrite")
            return question
        rewritten = rewritten.strip()
        attrs["changed"] = rewritten != question.strip()
        return rewritten


def clean_follow_ups(follow_ups):
    """[DECISION D70] The suggested questions of an answer, at most MAX_FOLLOW_UPS. Cleaned, never
    fatal: a bad list gives fewer suggestions or none, and never rejects the answer."""
    if not isinstance(follow_ups, list):
        return []
    kept = [item.strip() for item in follow_ups if isinstance(item, str) and item.strip()]
    return kept[:MAX_FOLLOW_UPS]
