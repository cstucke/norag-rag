// Conversation mode (V4): the Ask panel as a transcript. The page keeps the turns and sends them with
// each question, so a follow-up can be understood from what came before. Uses $, showResult, ask and
// passageButton from app.js, and traceButton from trace.js

// [DECISION D67] The history lives here, in the page: the app has no session and no database.
// The id only groups the traces of one conversation
const newConversationId = () => `c-${Math.random().toString(16).slice(2, 8)}`;
let conversationId = newConversationId();
// Turns that got an answer, oldest first: {question, data}. A failed turn is not part of the history
let turns = [];
// The turn shown in #result, moved to the transcript when the next question is asked
let latestTurn = null;

// The fields /api/ask reads beside the V3 ones. A turn goes into the history as the question that
// was searched, so a later follow-up can still be resolved once the first turns have left the window
function conversationFields() {
  return {
    conversation: true,
    conversation_id: conversationId,
    history: turns.map(({ question, data }) =>
      ({ question: data.standalone_question || question, answer: data.answer })),
  };
}

function searchedFor(data) {
  return data.standalone_question ? `Searched for: ${data.standalone_question}` : "";
}

// An earlier turn, as it stays on screen: question, answer, references and its own Details button
function turnElement({ question, data }) {
  const asked = document.createElement("p");
  asked.className = "turn-question";
  asked.textContent = question;
  const searched = document.createElement("p");
  searched.className = "small";
  searched.textContent = searchedFor(data);
  const answer = document.createElement("p");
  answer.textContent = data.answer;
  const references = document.createElement("ul");
  references.append(...data.references.map((ref) => {
    const item = document.createElement("li");
    item.append(passageButton(`[${ref.ref}] ${ref.title}, lines ${ref.line_start}-${ref.line_end}`, ref.chunk_id));
    return item;
  }));
  const element = document.createElement("div");
  element.className = "turn";
  element.append(asked);
  if (searched.textContent) element.append(searched);
  element.append(answer, references);
  if (data.trace_id) element.append(traceButton(data.trace_id));
  return element;
}

// Called by ask() before the request: the answer on screen joins the transcript
function archiveTurn() {
  if (latestTurn) $("transcript").append(turnElement(latestTurn));
  latestTurn = null;
}

// Called by ask() with the response: the newest turn, in the result block of app.js
function showTurn(question, data) {
  showResult(data);
  $("turn-question").textContent = question;
  $("searched-for").textContent = searchedFor(data);
  $("searched-for").hidden = !data.standalone_question;
  const followUps = data.follow_ups || [];
  $("follow-ups").hidden = !followUps.length;
  $("follow-up-list").replaceChildren(...followUps.map((text) => {
    const button = document.createElement("button");
    button.textContent = text;
    // A suggestion fills the question box and asks it
    button.addEventListener("click", () => {
      $("question").value = text;
      ask();
    });
    const item = document.createElement("li");
    item.append(button);
    return item;
  }));
  // Only a turn with an answer is kept. After an error the question stays in the box, to ask again
  if (data.status !== "error" && data.answer) {
    latestTurn = { question, data };
    turns.push(latestTurn);
    $("question").value = "";
  }
  $("new-conversation").hidden = !turns.length;
  $("question").scrollIntoView({ block: "nearest" });
}

function newConversation() {
  conversationId = newConversationId();
  turns = [];
  latestTurn = null;
  $("transcript").replaceChildren();
  $("result").hidden = true;
  $("new-conversation").hidden = true;
}

$("new-conversation").addEventListener("click", newConversation);
