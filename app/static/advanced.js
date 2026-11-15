// [DECISION D62] The Advanced switch. Off, the page shows what a first-time user needs. On, it also
// shows every element with the class "advanced": the tabs, settings, retrievers and retrieval details.
// The choice is kept in this browser. Uses $ from app.js, and loads last
$("advanced-toggle").checked = localStorage.advanced === "1";
document.body.classList.toggle("advanced", $("advanced-toggle").checked);

$("advanced-toggle").addEventListener("change", () => {
  const on = $("advanced-toggle").checked;
  localStorage.advanced = on ? "1" : "0";
  document.body.classList.toggle("advanced", on);
  // The tab bar is hidden now, so the Evaluation and Words tabs could no longer be left
  if (!on && $("tab-ask").hidden) $("show-ask").click();
});
