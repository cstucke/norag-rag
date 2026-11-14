// Details view: what happened behind one answer, read back from its trace (GET /api/traces/{id}).
// Uses $, api() and passageButton() from app.js, and tableRow() from evaluation.js

// [DECISION D54] A trace in plain words: its outcome, the name of each step, one sentence per step
const TRACE_OUTCOMES = {
  answered: "Answered", abstained: "No answer in the documents", invalid: "Answer rejected", error: "Error",
  ok: "Done", accepted: "Accepted", quarantined: "Held for review", approved: "Approved", rejected: "Rejected",
};
const TRACE_STEPS = {
  "index": "Prepare documents", "index.bm25": "Rebuild the keyword index",
  "retrieve.dense": "Meaning search", "retrieve.bm25": "Keyword search", "retrieve.graph": "Concept graph search",
  "fuse": "Combine", "prompt": "Build the prompt", "llm": "Ask the model", "validate": "Check the result",
  "select": "Pick passages", "scan": "Scan for suspicious text", "store": "Save the file",
  "extract": "Extract concepts",
};

const traceNumber = (value) => value.toLocaleString("en-US");
const traceCount = (value, word) => `${traceNumber(value)} ${word}${value === 1 ? "" : "s"}`;
// "1.2 s" from one second up, "340 ms" below
const traceDuration = (ms) => ms >= 1000 ? `${(ms / 1000).toFixed(1)} s` : `${Math.round(ms)} ms`;

// Links to the passage viewer, labelled as in the graph path: "support-runbook-errors.md#3"
function tracePassages(chunkIds) {
  return chunkIds.flatMap((chunkId) => {
    const button = passageButton(chunkId.replace(/^.*\//, "").replace(/#cs\d+-ov\d+#/, "#"), chunkId);
    button.title = chunkId;
    return [" ", button];
  });
}

// What one step did, as text and passage links. The attributes of each step are listed in spec §5.4
function traceSentence(span) {
  const attrs = span.attrs;
  if (span.error) return [`Failed: ${span.error}`];
  switch (span.name) {
    case "index":
      return [`Checked ${traceCount(attrs.docs_checked, "document")}, ` +
        (attrs.docs_indexed ? `prepared ${traceNumber(attrs.docs_indexed)}.` : "none needed preparing.")];
    case "index.bm25":
      return [`Rebuilt over ${traceCount(attrs.n_chunks, "passage")}.`];
    case "retrieve.dense":
    case "retrieve.bm25":
      return [`Found ${traceCount(attrs.chunk_ids.length, "passage")}.`];
    case "retrieve.graph":
      return [attrs.entities.length
        ? `Found ${traceCount(attrs.chunk_ids.length, "passage")} from ${attrs.entities.join(", ")}, ` +
          `following ${traceCount(attrs.edges_followed, "link")}.`
        : "No concept from the question is in the graph."];
    case "fuse":
      return attrs.chunks.length
        ? [`Kept the best ${attrs.chunks.length}:`, ...tracePassages(attrs.chunks.map((chunk) => chunk.chunk_id))]
        : ["Nothing was found."];
    case "prompt":
      return [`${traceCount(attrs.excerpts, "passage")}, ${traceNumber(attrs.chars)} characters.`];
    case "llm":
      return [`${attrs.model} read ${traceCount(attrs.prompt_tokens, "token")} ` +
        `and wrote ${traceNumber(attrs.completion_tokens)}.`];
    case "validate":
      // Three steps share this name: a question's answer, a study set, an uploaded file
      if ("answerable" in attrs) {
        if (!attrs.answerable) return ["Accepted. The model found no answer in the passages."];
        const cited = attrs.citations.length > 1
          ? `passages ${attrs.citations.slice(0, -1).join(", ")} and ${attrs.citations.at(-1)}`
          : `passage ${attrs.citations[0]}`;
        return [`Accepted. It cites ${cited}.`];
      }
      if ("returned" in attrs) {
        const reasons = Object.entries(attrs.dropped).map(([reason, number]) => `${reason} (${number})`);
        return [`Kept ${attrs.kept} of ${traceCount(attrs.returned, "item")}.` +
          (reasons.length ? ` Dropped: ${reasons.join(", ")}.` : "")];
      }
      return [`The file is valid, ${traceCount(attrs.bytes, "byte")}.`];
    case "select":
      return [`Picked ${attrs.chunk_ids.length} of ${traceCount(attrs.available, "passage")}:`,
        ...tracePassages(attrs.chunk_ids)];
    case "scan":
      return [attrs.findings.length
        ? `Found ${traceCount(attrs.findings.length, "suspicious passage")}: ` +
          attrs.findings.map((finding) => `${finding.rule} (line ${finding.line})`).join(", ") + "."
        : "Nothing suspicious found."];
    case "store":
      return [attrs.destination === "quarantine" ? "Held for review, outside the documents."
        : "Saved with the uploaded documents."];
    case "extract":
      return [...tracePassages([attrs.chunk_id]),
        ` ${attrs.status}: ${traceCount(attrs.triples, "link")} kept, ${attrs.rejected} rejected.`];
    default:
      return [];
  }
}

function showTrace(trace) {
  const tokens = trace.llm.prompt_tokens + trace.llm.completion_tokens;
  $("trace-summary").textContent = [TRACE_OUTCOMES[trace.outcome] || trace.outcome, traceDuration(trace.ms),
    traceCount(trace.llm.calls, "LLM call"), traceCount(tokens, "token"),
    `$${trace.llm.cost_usd.toFixed(4)}`].join(" · ");
  // A step that ran inside another one is indented under it
  const depth = (span) => span.parent === null ? 0 : 1 + depth(trace.spans[span.parent]);
  $("trace-steps").replaceChildren(tableRow("th", ["Step", "Time", "What happened"]), ...trace.spans.map((span) => {
    const label = document.createElement("span");
    label.textContent = TRACE_STEPS[span.name] || span.name;
    label.style.paddingLeft = `${depth(span)}rem`;
    const sentence = document.createElement("span");
    sentence.append(...traceSentence(span));
    return tableRow("td", [label, `${traceNumber(Math.round(span.ms))} ms`, sentence]);
  }));
  $("trace-json").textContent = JSON.stringify(trace, null, 2);
}

async function openTrace(traceId) {
  let data;
  try {
    data = await api("GET", `/api/traces/${encodeURIComponent(traceId)}`);
  } catch {
    data = { status: "error", error: { message: "Request failed." } };
  }
  if (data.status === "error") {
    $("trace-summary").textContent = data.error.message;
    $("trace-steps").replaceChildren();
    $("trace-json").textContent = "";
  } else {
    showTrace(data);
  }
  $("trace-dialog").showModal();
}

// Also used by study.js, for the trace of a study set
function traceButton(traceId) {
  const button = document.createElement("button");
  button.textContent = "Details";
  button.addEventListener("click", () => openTrace(traceId));
  return button;
}

$("trace-close").addEventListener("click", () => $("trace-dialog").close());
