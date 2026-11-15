// Graph tab: build the concept graph of a set of documents and browse it, over /api/graph.
// Uses $, api() and showRetrievers' checkboxes from app.js, tableRow() from evaluation.js
// and tracePassages() from trace.js

// [DECISION D65] LLM calls one click on Build may spend. Kestrel (38 passages) fits in one click
const GRAPH_CLICK_LIMIT = 40;
const GRAPH_ROW_LIMIT = 200;

let graphNodes = [];
let graphEdges = [];
let graphStopped = false;

const graphUrl = (path) => `${path}?corpus=${encodeURIComponent($("graph-corpus").value)}`;
const graphLinks = (nodeId) => graphEdges.filter((edge) => edge.source === nodeId || edge.target === nodeId);

// ---------------------------------------------------------------------------
// Status and build
// ---------------------------------------------------------------------------

function showGraph(data) {
  graphNodes = data.nodes;
  graphEdges = data.edges;
  const left = data.chunks - data.chunks_done;
  $("graph-status").textContent = data.chunks === 0
    ? "No document here yet. Upload one in the Ask tab, then come back."
    : `${data.chunks_done} of ${data.chunks} passages read (chunk size ${data.chunk_size}, overlap ` +
      `${data.chunk_overlap}) · ${graphNodes.length} entities · ${graphEdges.length} links` +
      (left ? ` · ${left} left to read, one LLM call each, at most ${GRAPH_CLICK_LIMIT} per click` : "");
  $("graph-build").disabled = left === 0;
  $("graph-entity").hidden = true;
  renderEntities();
}

async function loadGraph() {
  const data = await api("GET", graphUrl("/api/graph"));
  $("graph-error").textContent = data.status === "error" ? data.error.message : "";
  if (data.status !== "error") showGraph(data);
}

// The Graph boxes were drawn disabled if no graph existed when the page loaded
function enableGraphRetriever() {
  for (const id of ["ask-retrievers", "eval-retrievers"]) {
    const checkbox = $(id).querySelector('input[value="graph"]');
    if (checkbox && checkbox.disabled) {
      checkbox.disabled = false;
      // The " (not built for the current settings)" note
      checkbox.parentNode.lastChild.remove();
    }
  }
}

// One request extracts a few passages. Repeated until nothing is left, the click's limit is reached,
// Stop is pressed or a request extracts nothing (a rate limit, for example)
async function buildGraph() {
  graphStopped = false;
  $("graph-corpus").disabled = true;
  $("graph-build").disabled = true;
  $("graph-stop").hidden = false;
  $("graph-error").textContent = "";
  let calls = 0;
  let left = true;
  while (left && !graphStopped && calls < GRAPH_CLICK_LIMIT) {
    let data;
    try {
      data = await api("POST", graphUrl("/api/graph/build"));
    } catch {
      data = { status: "error", error: { message: "Request failed." } };
    }
    if (data.status === "error") {
      $("graph-error").textContent = data.error.message;
      break;
    }
    showGraph(data);
    enableGraphRetriever();
    calls += data.step.tried;
    left = data.chunks_done < data.chunks;
    if (left && data.step.extracted === 0) {
      $("graph-error").textContent = `Stopped: ${data.step.error.message} Click Build to try again.`;
      break;
    }
  }
  $("graph-corpus").disabled = false;
  $("graph-stop").hidden = true;
}

// ---------------------------------------------------------------------------
// Browse
// ---------------------------------------------------------------------------

// The entities with the most links first
function renderEntities() {
  const text = $("graph-filter").value.toLowerCase();
  const found = graphNodes
    .filter((node) => node.names.some((name) => name.toLowerCase().includes(text)))
    .map((node) => ({ node, links: graphLinks(node.id).length }))
    .sort((a, b) => b.links - a.links || a.node.name.localeCompare(b.node.name));
  $("graph-showing").textContent = found.length > GRAPH_ROW_LIMIT
    ? `Showing the first ${GRAPH_ROW_LIMIT} of ${found.length} entities.` : "";
  const rows = found.slice(0, GRAPH_ROW_LIMIT).map(({ node, links }) => {
    const row = tableRow("td", [node.name, node.type, links]);
    row.className = "clickable";
    row.addEventListener("click", () => showEntity(node.id));
    return row;
  });
  $("graph-entities").replaceChildren(...(rows.length ? [tableRow("th", ["Entity", "Type", "Links"]), ...rows] : []));
}

// One entity: its other spellings, the passages that name it, then each link with the entity at its
// other end (click it to move there) and the passages the link comes from
function showEntity(nodeId) {
  const node = graphNodes.find((candidate) => candidate.id === nodeId);
  $("graph-entity-name").textContent = `${node.name} (${node.type})`;
  const info = [];
  if (node.names.length > 1) info.push(`Also written: ${node.names.slice(1).join(", ")}. `);
  info.push("Named in:", ...tracePassages(node.chunk_ids));
  $("graph-entity-info").replaceChildren(...info);
  $("graph-entity-links").replaceChildren(...graphLinks(nodeId).map((edge) => {
    const outgoing = edge.source === nodeId;
    const other = graphNodes.find((candidate) => candidate.id === (outgoing ? edge.target : edge.source));
    const button = document.createElement("button");
    button.className = "link";
    button.textContent = `${other.name} (${other.type})`;
    button.addEventListener("click", () => showEntity(other.id));
    const item = document.createElement("li");
    item.append(...(outgoing ? [`${node.name} —${edge.relation}→ `, button] : [button, ` —${edge.relation}→ ${node.name}`]),
                ...tracePassages(edge.chunk_ids));
    return item;
  }));
  $("graph-entity").hidden = false;
}

// ---------------------------------------------------------------------------
// Wiring
// ---------------------------------------------------------------------------

$("show-graph").addEventListener("click", loadGraph);
$("graph-corpus").addEventListener("change", loadGraph);
$("graph-build").addEventListener("click", buildGraph);
$("graph-stop").addEventListener("click", () => { graphStopped = true; });
$("graph-filter").addEventListener("input", renderEntities);
