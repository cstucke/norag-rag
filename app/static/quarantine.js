// Injection scanner (V4): the held-for-review message after an upload, the waiting notice and the
// review dialog. Uses $, api and loadDocuments from app.js

// Called by uploadDocument in app.js after every upload
function showUploadReview(data) {
  $("held-message").textContent = data.status === "quarantined"
    ? `Held for review: ${data.findings.length} suspicious passage${data.findings.length === 1 ? "" : "s"}.`
    : "";
  loadQuarantine();
}

async function loadQuarantine() {
  const waiting = (await api("GET", "/api/quarantine")).documents || [];
  const count = waiting.length;
  $("review-notice").hidden = count === 0;
  $("review-count").textContent = count === 1
    ? "1 document is waiting for review" : `${count} documents are waiting for review`;
  renderReview(waiting);
  if (count === 0 && $("review-dialog").open) $("review-dialog").close();
}

function renderReview(waiting) {
  $("review-list").replaceChildren(...waiting.map((doc) => {
    const title = document.createElement("h4");
    title.textContent = doc.filename;
    const findings = document.createElement("ul");
    findings.append(...doc.findings.map((finding) => {
      const item = document.createElement("li");
      const rule = document.createElement("strong");
      rule.textContent = finding.description;
      const excerpt = document.createElement("code");
      excerpt.textContent = finding.excerpt;
      item.append(rule, ` (line ${finding.line}): `, excerpt);
      return item;
    }));
    const approve = document.createElement("button");
    approve.textContent = "Approve";
    approve.addEventListener("click", () => decide("approve", doc.filename));
    const reject = document.createElement("button");
    reject.textContent = "Reject";
    reject.addEventListener("click", () => decide("reject", doc.filename));
    const box = document.createElement("div");
    box.className = "review-item";
    box.append(title, findings, approve, " ", reject);
    return box;
  }));
}

// Approve moves the file into the document list; reject deletes it
async function decide(action, filename) {
  const data = await api("POST", `/api/quarantine/${action}`, { filename });
  $("review-error").textContent = data.status === "error" ? data.error.message : "";
  $("held-message").textContent = "";
  await loadQuarantine();
  if (action === "approve") await loadDocuments();
}

$("review-open").addEventListener("click", () => $("review-dialog").showModal());
$("review-close").addEventListener("click", () => $("review-dialog").close());
loadQuarantine();
