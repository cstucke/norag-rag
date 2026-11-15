// Study artifacts (V4): the Ask a question / Make a quiz switch, the study form, flashcards and
// multiple choice. Uses $, api, selected and passageButton from app.js

// The switch shows the Ask panel or the Study panel; both use the selection in the Documents panel
function showMode() {
  const mode = document.querySelector("input[name=mode]:checked").value;
  $("ask-panel").hidden = mode !== "ask";
  $("study-panel").hidden = mode !== "study";
}
for (const radio of document.querySelectorAll("input[name=mode]")) radio.addEventListener("change", showMode);
// Some browsers keep the picked radio across a reload
showMode();

async function generateStudy() {
  $("study-generate").disabled = true;
  $("study-working").hidden = false;
  // Hide the previous set, so it can't be mistaken for this one
  $("study-result").hidden = true;
  try {
    showStudy(await api("POST", "/api/study", {
      doc_ids: [...selected],
      type: document.querySelector("input[name=study-type]:checked").value,
      count: Number($("study-count").value),
      difficulty: $("study-difficulty").value,
    }));
  } catch {
    showStudy({ status: "error", error: { message: "Request failed." } });
  } finally {
    $("study-generate").disabled = false;
    $("study-working").hidden = true;
  }
}

function plural(count, word) {
  return `${count.toLocaleString("en-US")} ${word}${count === 1 ? "" : "s"}`;
}

function showStudy(data) {
  const items = data.items || [];
  let status = data.status === "error" ? `Error: ${data.error.message}` : "";
  if (data.status === "ok") {
    if (data.dropped) status = `${items.length} of ${items.length + data.dropped} items passed the source check.`;
    else if (items.length < data.requested) status = `The documents gave ${items.length} of the ${data.requested} items asked for.`;
  }
  $("study-status").textContent = status;
  $("study-status").className = data.status === "error" ? "error" : "";
  const cost = data.cost;
  $("study-cost").textContent = cost
    ? `${plural(cost.llm_calls, "LLM call")} · ${plural(cost.prompt_tokens + cost.completion_tokens, "token")} · ` +
      `$${cost.cost_usd.toFixed(4)} · ${(cost.ms / 1000).toFixed(1)} s`
    : "";
  // The join adds the Details button here, in #study-trace-slot: traceButton(data.trace_id) from trace.js
  $("study-items").replaceChildren(...items.map((item, i) =>
    data.type === "multiple_choice" ? choiceItem(item, i) : flashcardItem(item)));
  $("study-result").hidden = false;
}

function sourceButton(item) {
  const ref = item.reference;
  return passageButton(`source: ${ref.title}, lines ${ref.line_start}-${ref.line_end}`, ref.chunk_id);
}

function quoteBlock(item) {
  const quote = document.createElement("blockquote");
  quote.textContent = item.quote;
  return quote;
}

function flashcardItem(item) {
  const question = document.createElement("p");
  question.textContent = item.question;
  const answer = document.createElement("div");
  answer.hidden = true;
  const answerText = document.createElement("p");
  answerText.textContent = item.answer;
  answer.append(answerText, quoteBlock(item));
  const show = document.createElement("button");
  show.textContent = "Show answer";
  show.addEventListener("click", () => {
    answer.hidden = !answer.hidden;
    show.textContent = answer.hidden ? "Show answer" : "Hide answer";
  });
  const row = document.createElement("div");
  row.className = "study-row";
  row.append(show, sourceButton(item));
  const element = document.createElement("li");
  element.append(question, row, answer);
  return element;
}

function choiceItem(item, index) {
  const question = document.createElement("p");
  question.textContent = item.question;
  const options = document.createElement("div");
  const labels = item.options.map((text, i) => {
    const radio = document.createElement("input");
    radio.type = "radio";
    radio.name = `study-choice-${index}`;
    radio.value = i + 1;
    const label = document.createElement("label");
    label.append(radio, " ", text);
    options.append(label);
    return label;
  });
  const verdict = document.createElement("span");
  const quote = quoteBlock(item);
  quote.hidden = true;
  const check = document.createElement("button");
  check.textContent = "Check";
  check.addEventListener("click", () => {
    const picked = options.querySelector("input:checked");
    if (!picked) {
      verdict.textContent = "Pick an answer first.";
      verdict.className = "";
      return;
    }
    const right = Number(picked.value) === item.answer;
    verdict.textContent = right ? "Right." : `Wrong. The answer is: ${item.options[item.answer - 1]}`;
    verdict.className = right ? "right" : "error";
    labels.forEach((label, i) => label.classList.toggle("right", i + 1 === item.answer));
    quote.hidden = false;
  });
  const row = document.createElement("div");
  row.className = "study-row";
  row.append(check, verdict, sourceButton(item));
  const element = document.createElement("li");
  element.append(question, options, row, quote);
  return element;
}

$("study-generate").addEventListener("click", generateStudy);
