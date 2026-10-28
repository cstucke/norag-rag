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
    showResult(await api("POST", "/api/ask", { question: $("question").value, doc_ids: [...selected] }));
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
    return item;
  }));
  $("retrieved").replaceChildren(...(data.retrieved || []).map((ref) => {
    const item = document.createElement("li");
    item.append(passageButton(`${ref.ref}. ${ref.title} (distance ${ref.distance.toFixed(3)})`, ref.chunk_id));
    return item;
  }));
  $("result").hidden = false;
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