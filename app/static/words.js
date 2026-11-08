// Words tab: word counts for diagnosing retrieval misses, over the /api/words routes.
// Uses $, api() and openChunk() from app.js, tableRow() and selectOption() from evaluation.js
const WORD_ROW_LIMIT = 200;

let vocabularyWords = [];
let questionSets = [];

const wordsCorpus = () => $("words-corpus").value;

// A failure goes to the section's error line as-is, and the caller gets null
async function wordsRequest(errorId, method, url, body) {
  const data = await api(method, url, body);
  $(errorId).textContent = data.status === "error" ? data.error.message : "";
  return data.status === "error" ? null : data;
}

function clearWords() {
  $("vocabulary-result").hidden = true;
  $("word-result").hidden = true;
  $("question-table").replaceChildren();
}

async function showWordsConfig() {
  const settings = await api("GET", "/api/settings");
  const line = `Chunk size ${settings.chunk_size}, overlap ${settings.chunk_overlap}.`;
   // Counts already on screen came from other settings, so they would contradict this line
  if (line !== $("words-config").textContent) clearWords();
  $("words-config").textContent = line;
}

// ---------------------------------------------------------------------------
// Word -> chunks
// ---------------------------------------------------------------------------

function chunkRow(chunk) {
  const row = tableRow("td", [chunk.title, chunk.doc_id, `${chunk.line_start}-${chunk.line_end}`, chunk.count]);
  row.className = "clickable";
  row.addEventListener("click", () => openChunk(chunk.chunk_id));
  return row;
}

async function showWord(word) {
  $("word-input").value = word;
  $("word-result").hidden = true;
  const url = `/api/words/chunks?corpus=${encodeURIComponent(wordsCorpus())}&word=${encodeURIComponent(word)}`;
  const data = await wordsRequest("word-error", "GET", url);
  if (!data) return;
  const shown = data.chunks.slice(0, WORD_ROW_LIMIT);
  $("word-totals").textContent = `${data.word}: ${data.count} occurrences in ${data.chunk_count} chunks`;
  $("word-showing").textContent = `showing ${shown.length} of ${data.chunk_count}`;
  $("word-table").replaceChildren(tableRow("th", ["title", "doc_id", "lines", "count"]), ...shown.map(chunkRow));
  $("word-result").hidden = false;
}

// ---------------------------------------------------------------------------
// Vocabulary
// ---------------------------------------------------------------------------

function wordRow(item) {
  const button = document.createElement("button");
  button.className = "link";
  button.textContent = item.word;
  button.addEventListener("click", () => showWord(item.word));
  return tableRow("td", [button, item.count, item.chunks]);
}

function renderVocabulary() {
  const text = $("vocabulary-filter").value.toLowerCase();
  const matches = vocabularyWords.filter((item) => item.word.includes(text));
  const shown = matches.slice(0, WORD_ROW_LIMIT);
  $("vocabulary-showing").textContent = `showing ${shown.length} of ${matches.length}`;
  $("vocabulary-table").replaceChildren(tableRow("th", ["word", "count", "chunks"]), ...shown.map(wordRow));
}

async function loadVocabulary() {
  $("vocabulary-result").hidden = true;
  const data = await wordsRequest("vocabulary-error", "GET",
                                  `/api/words/vocabulary?corpus=${encodeURIComponent(wordsCorpus())}`);
  if (!data) return;
  vocabularyWords = data.words;
  $("vocabulary-totals").textContent =
    `${data.chunk_count} chunks, ${data.token_count} tokens, ${data.word_count} distinct words`;
  renderVocabulary();
  $("vocabulary-result").hidden = false;
}

// ---------------------------------------------------------------------------
// Question
// ---------------------------------------------------------------------------

const currentQuestions = () => questionSets.find((set) => set.name === $("question-set").value).questions;

function fillQuestions() {
  $("question-pick").replaceChildren(selectOption("", "Pick a question"), ...currentQuestions().map((question) =>
    selectOption(question.id, `${question.id}: ${question.question}`)));
  $("question-info").textContent = "";
}

function pickQuestion() {
  const question = currentQuestions().find((item) => item.id === $("question-pick").value);
  if (!question) {
    $("question-info").textContent = "";
    return;
  }
  $("words-question").value = question.question;
  $("question-info").textContent =
    `Type: ${question.type}. Evidence: ${question.evidence_doc_ids.join(", ") || "none"}.`;
}

function questionRow(item) {
  if (item.count) return wordRow(item);
  const row = tableRow("td", [`${item.word} (absent)`, item.count, item.chunks]);
  row.className = "absent";
  return row;
}

async function analyseQuestion() {
  $("question-table").replaceChildren();
  const data = await wordsRequest("question-error", "POST", "/api/words/question",
                                  { corpus: wordsCorpus(), question: $("words-question").value });
  if (!data) return;
  $("question-table").replaceChildren(tableRow("th", ["word", "count", "chunks"]), ...data.words.map(questionRow));
}

// ---------------------------------------------------------------------------
// Wiring
// ---------------------------------------------------------------------------

$("show-words").addEventListener("click", showWordsConfig);
$("words-corpus").addEventListener("change", clearWords);
$("vocabulary-load").addEventListener("click", loadVocabulary);
$("vocabulary-filter").addEventListener("input", renderVocabulary);
$("word-show").addEventListener("click", () => showWord($("word-input").value));
$("question-set").addEventListener("change", fillQuestions);
$("question-pick").addEventListener("change", pickQuestion);
$("question-analyse").addEventListener("click", analyseQuestion);

api("GET", "/api/corpora").then((data) => {
  $("words-corpus").replaceChildren(...data.corpora.map((name) => selectOption(name)));
});
wordsRequest("question-error", "GET", "/api/question-sets").then((data) => {
  if (!data) return;
  questionSets = data.question_sets;
  $("question-set").replaceChildren(...questionSets.map((set) => selectOption(set.name)));
  fillQuestions();
});