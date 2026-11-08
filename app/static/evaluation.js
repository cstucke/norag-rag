// Evaluation tab: a thin client over POST /api/eval. Uses $ and api() from app.js
const EVAL_COLUMNS = ["hit@1", "hit@3", "hit@5", "hit@10", "all@1", "all@3", "all@5", "all@10",
  "recall@1", "recall@3", "recall@5", "recall@10", "mrr"];
const EVAL_KS = [1, 3, 5, 10];

// The cost and graph-reach lines go under the table
const evalLines = document.createElement("div");
$("eval-table").after(evalLines);

function costText(cost) {
  const answer = cost.answer_ms === null ? "–" : `${cost.answer_ms.toFixed(0)} ms`;
  return `Cost per question: retrieval ${cost.retrieval_ms.toFixed(0)} ms, LLM calls ${cost.llm_calls.toFixed(2)}, ` +
    `tokens ${cost.prompt_tokens.toFixed(0)} prompt / ${cost.completion_tokens.toFixed(0)} completion, answer ${answer}`;
}

function reachText(values, name) {
  return `(n=${values.n})` + EVAL_KS.map((k) => {
    const value = values[`${name}@${k}`];
    return ` @${k} ${value === null ? "–" : value.toFixed(3)}`;
  }).join("");
}

// tableRow and selectOption are also used by words.js, which loads after this file
function tableRow(tag, cells) {
  const row = document.createElement("tr");
  row.append(...cells.map((content) => {
    const cell = document.createElement(tag);
    cell.append(content);
    return cell;
  }));
  return row;
}

function selectOption(value, text = value) {
  const option = document.createElement("option");
  option.value = value;
  option.textContent = text;
  return option;
}

function metricsRow(label, values) {
  return tableRow("td", [label, values.n, ...EVAL_COLUMNS.map((column) =>
    values[column] === null ? "–" : values[column].toFixed(3))]);
}

function corpusCheckText(check) {
  if (check === "no manifest") return "Corpus check: no manifest, skipped.";
  if (check.matches_manifest) return "Corpus check: matches the manifest.";
  return `Corpus check: does not match the manifest (${check.added.length} added, ${check.deleted.length} deleted, ` +
    `${check.changed.length} changed). These numbers are not comparable with runs on the original snapshot.`;
}

function showEvalResult(data) {
  $("eval-file").textContent = data.results_file;
  $("eval-corpus-check").textContent = corpusCheckText(data.corpus_check);
  $("eval-table").replaceChildren(
    tableRow("th", ["type", "n", ...EVAL_COLUMNS.map((column) => column.replace("mrr", "MRR"))]),
    metricsRow("overall", data.metrics.overall),
    ...Object.entries(data.metrics.by_type).map(([type, values]) => metricsRow(type, values)));
  const lines = [costText(data.metrics.cost)];
  if (data.metrics.graph_reach) {
    lines.push(`Graph reach ${reachText(data.metrics.graph_reach, "graph_reach")} · ` +
      `graph-only reach ${reachText(data.metrics.graph_only_reach, "graph_only_reach")}`);
  }
  evalLines.replaceChildren(...lines.map((text) => {
    const paragraph = document.createElement("p");
    paragraph.textContent = text;
    return paragraph;
  }));
  $("eval-result").hidden = false;
}

async function runEval() {
  $("eval-run").disabled = true;
  $("eval-working").hidden = false;
  // Hide the previous result, so it can't be mistaken for the result of this run
  $("eval-result").hidden = true;
  $("eval-error").textContent = "";
  try {
    const data = await api("POST", "/api/eval", {
      question_set: $("eval-set").value,
      chunk_size: Number($("eval-chunk-size").value),
      chunk_overlap: Number($("eval-chunk-overlap").value),
      top_k: Number($("eval-top-k").value),
      with_llm: $("eval-with-llm").checked,
      retrievers: checkedRetrievers("eval-retrievers"),
    });
    if (data.status === "error") $("eval-error").textContent = data.error.message;
    else showEvalResult(data);
  } catch {
    $("eval-error").textContent = "Request failed.";
  } finally {
    $("eval-run").disabled = false;
    $("eval-working").hidden = true;
  }
}

$("eval-run").addEventListener("click", runEval);

api("GET", "/api/question-sets").then((data) => {
  if (data.status === "error") $("eval-error").textContent = data.error.message;
  else $("eval-set").replaceChildren(...data.question_sets.map((set) => selectOption(set.name)));
});
api("GET", "/api/settings").then((settings) => {
  $("eval-chunk-size").value = settings.chunk_size;
  $("eval-chunk-overlap").value = settings.chunk_overlap;
  $("eval-top-k").value = settings.top_k;
});