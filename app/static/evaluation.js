// Evaluation tab: a thin client over POST /api/eval. Uses $ and api() from app.js
const EVAL_COLUMNS = ["hit@1", "hit@3", "hit@5", "hit@10", "all@1", "all@3", "all@5", "all@10", "mrr"];

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