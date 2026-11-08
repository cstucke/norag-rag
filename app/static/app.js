// RAG V1 UI: plain JavaScript over the routes in app/main.py
const $ = (id) => document.getElementById(id);

let documents = [];
const selected = new Set();

// Every route answers JSON; failures carry {"status": "error", "error": {code, message}}
async function api(method, url, body) {
  const options = { method };
  if (body instanceof FormData) {
    options.body = body;
  } else if (body !== undefined) {
    options.headers = { "Content-Type": "application/json" };
    options.body = JSON.stringify(body);
  }
  const response = await fetch(url, options);
  return response.json();
}

// ---------------------------------------------------------------------------
// Documents
// ---------------------------------------------------------------------------

function filteredDocuments() {
  const text = $("doc-filter").value.toLowerCase();
  return documents.filter((doc) =>
    doc.title.toLowerCase().includes(text) || doc.doc_id.toLowerCase().includes(text));
}

function renderDocuments() {
  const items = filteredDocuments().map((doc) => {
    const checkbox = document.createElement("input");
    checkbox.type = "checkbox";
    checkbox.checked = selected.has(doc.doc_id);
    checkbox.addEventListener("change", () => {
      if (checkbox.checked) selected.add(doc.doc_id);
      else selected.delete(doc.doc_id);
      renderCounts();
    });
    const label = document.createElement("label");
    label.title = doc.doc_id;
    label.append(checkbox, " ", doc.title);
    const remove = document.createElement("button");
    remove.textContent = "Delete";
    remove.addEventListener("click", () => deleteDocument(doc.doc_id));
    const item = document.createElement("li");
    item.append(label, remove);
    return item;
  });
  $("doc-list").replaceChildren(...items);
  renderCounts();
}

function renderCounts() {
  $("doc-count").textContent = documents.length;
  $("selected-count").textContent = selected.size;
}

async function loadDocuments() {
  documents = (await api("GET", "/api/documents")).documents;
  renderDocuments();
}

async function deleteDocument(docId) {
  if (!confirm(`Delete ${docId}?`)) return;
  const data = await api("DELETE", `/api/documents?doc_id=${encodeURIComponent(docId)}`);
  $("doc-error").textContent = data.status === "error" ? data.error.message : "";
  selected.delete(docId);
  await loadDocuments();
}

async function uploadDocument() {
  const input = $("upload");
  if (!input.files.length) return;
  const form = new FormData();
  form.append("file", input.files[0]);
  const data = await api("POST", "/api/documents", form);
  $("doc-error").textContent = data.status === "error" ? data.error.message : "";
  input.value = "";
  await loadDocuments();
}

// ---------------------------------------------------------------------------
// Settings
// ---------------------------------------------------------------------------

function showSettings(settings) {
  $("chunk-size").value = settings.chunk_size;
  $("chunk-overlap").value = settings.chunk_overlap;
  $("top-k").value = settings.top_k;
}

async function saveSettings() {
  const data = await api("PUT", "/api/settings", {
    chunk_size: Number($("chunk-size").value),
    chunk_overlap: Number($("chunk-overlap").value),
    top_k: Number($("top-k").value),
  });
  if (data.status === "error") {
    $("settings-error").textContent = data.error.message;
  } else {
    $("settings-error").textContent = "";
    showSettings(data);
  }
}

// ---------------------------------------------------------------------------
// Ask
// ---------------------------------------------------------------------------

const STATUS_LABELS = { answered: "Answered", not_found: "Not found", error: "Error" };

async function ask() {
  $("ask").disabled = true;
  $("working").hidden = false;
  // Hide the previous answer, so it can't be mistaken for the answer to this question
  $("result").hidden = true;
  try {
    showResult(await api("POST", "/api/ask", { question: $("question").value, doc_ids: [...selected],
      retrievers: checkedRetrievers("ask-retrievers") }));
  } catch {
    showResult({ status: "error", error: { message: "Request failed." } });
  } finally {
    $("ask").disabled = false;
    $("working").hidden = true;
  }
}

function passageButton(text, chunkId) {
  const button = document.createElement("button");
  button.className = "link";
  button.textContent = text;
  button.addEventListener("click", () => openChunk(chunkId));
  return button;
}

function showResult(data) {
  $("status").textContent = STATUS_LABELS[data.status] + (data.error ? `: ${data.error.message}` : "");
  $("answer").textContent = data.answer || "";
  $("config").textContent = data.config
    ? `chunk size ${data.config.chunk_size} · overlap ${data.config.chunk_overlap} · ` +
      `top-k ${data.config.top_k} · model ${data.config.model}`
    : "";
  $("references").replaceChildren(...(data.references || []).map((ref) => {
    const item = document.createElement("li");
    item.append(passageButton(`[${ref.ref}] ${ref.title}, lines ${ref.line_start}-${ref.line_end}`, ref.chunk_id));
    if (ref.source_url) {
      const link = document.createElement("a");
      link.href = ref.source_url;
      link.target = "_blank";
      link.textContent = "wiki page";
      item.append(" ", link);
    }
    renderFoundBy(ref, item);
    return item;
  }));
  $("retrieved").replaceChildren(...(data.retrieved || []).map((ref) => {
    const item = document.createElement("li");
    item.append(passageButton(`${ref.ref}. ${ref.title} (distance ${ref.distance.toFixed(3)})`, ref.chunk_id));
    return item;
  }));
  $("result").hidden = false;
  renderGraphPath(data.graph_path);
}

async function openChunk(chunkId) {
  const data = await api("GET", `/api/chunk?id=${encodeURIComponent(chunkId)}`);
  if (data.status === "error") {
    $("chunk-title").textContent = "Error";
    $("chunk-meta").textContent = data.error.message;
    $("chunk-text").textContent = "";
  } else {
    $("chunk-title").textContent = data.title;
    $("chunk-meta").textContent = `${data.doc_id}, lines ${data.line_start}-${data.line_end}`;
    $("chunk-text").textContent = data.text;
  }
  $("chunk-dialog").showModal();
}

// ---------------------------------------------------------------------------
// Wiring
// ---------------------------------------------------------------------------

$("doc-filter").addEventListener("input", renderDocuments);
$("select-all").addEventListener("click", () => {
  for (const doc of filteredDocuments()) selected.add(doc.doc_id);
  renderDocuments();
});
$("clear-selection").addEventListener("click", () => {
  selected.clear();
  renderDocuments();
});
$("upload").addEventListener("change", uploadDocument);
$("save-settings").addEventListener("click", saveSettings);
$("ask").addEventListener("click", ask);
$("chunk-close").addEventListener("click", () => $("chunk-dialog").close());

loadDocuments();
api("GET", "/api/settings").then(showSettings);

// ---------------------------------------------------------------------------
// Tabs
// ---------------------------------------------------------------------------

const TABS = ["ask", "eval", "words"];

for (const name of TABS) {
  $(`show-${name}`).addEventListener("click", () => {
    for (const tab of TABS) $(`tab-${tab}`).hidden = tab !== name;
  });
}

// ---------------------------------------------------------------------------
// Retrievers (V3)
// ---------------------------------------------------------------------------

const RETRIEVER_LABELS = { dense: "Dense", bm25: "BM25", graph: "Graph" };

// One checkbox per retriever, checked for the defaults. A disabled box is also unchecked,
// since input:checked would still match it
function showRetrievers(fieldsetId, data) {
  for (const name of data.available) {
    const checkbox = document.createElement("input");
    checkbox.type = "checkbox";
    checkbox.value = name;
    checkbox.checked = data.default.includes(name);
    const label = document.createElement("label");
    label.append(checkbox, " ", RETRIEVER_LABELS[name]);
    if (name === "graph" && !data.graph_built) {
      checkbox.disabled = true;
      checkbox.checked = false;
      label.append(" (not built for the current settings)");
    }
    $(fieldsetId).append(label, " ");
  }
}

function checkedRetrievers(fieldsetId) {
  return [...$(fieldsetId).querySelectorAll("input:checked")].map((checkbox) => checkbox.value);
}

// "found by: dense #2 · bm25 #1", only the retrievers that found the chunk
function renderFoundBy(ref, element) {
  const ranks = Object.entries(ref.found_by || {}).filter(([, rank]) => rank !== null);
  const line = document.createElement("div");
  line.className = "small";
  line.textContent = "found by: " + ranks.map(([name, rank]) => `${name} #${rank}`).join(" · ");
  element.append(line);
}

api("GET", "/api/retrievers").then((data) => {
  showRetrievers("ask-retrievers", data);
  showRetrievers("eval-retrievers", data);
});

// The path behind an answer when the graph is on: the entities found in the question, then the
// edges followed that have a passage in the context, each with its passages. Hidden otherwise
function renderGraphPath(path) {
  const box = $("graph-path");
  box.hidden = !path;
  if (!path) return;
  const title = document.createElement("h3");
  title.textContent = "Graph path";
  const entities = document.createElement("p");
  entities.textContent = path.entities.length
    ? "Entities in the question: " + path.entities.map((entity) => `${entity.name} (${entity.type})`).join(", ")
    : "No entity from the question was found in the graph.";
  const parts = [title, entities];
  if (path.entities.length) {
    const edges = document.createElement("ul");
    edges.append(...path.edges.map((edge) => {
      const item = document.createElement("li");
      item.append(`${edge.source_name} —${edge.relation}→ ${edge.target_name} (hop ${edge.hop}) `);
      for (const chunkId of edge.chunk_ids) {
        // "support-runbook-errors.md#7" is enough to tell chunks apart; the full id is the tooltip
        const button = passageButton(chunkId.replace(/^.*\//, "").replace(/#cs\d+-ov\d+#/, "#"), chunkId);
        button.title = chunkId;
        item.append(button, " ");
      }
      return item;
    }));
    const heading = document.createElement("p");
    heading.textContent = path.edges.length
      ? "Edges followed:" : "No edge followed from these entities has a passage in the context.";
    parts.push(heading);
    if (path.edges.length) parts.push(edges);
  }
  box.replaceChildren(...parts);
}
