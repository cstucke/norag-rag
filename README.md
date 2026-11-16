# Ask your documents (norag-rag)

A web app that answers questions about a set of documents and shows the passages each answer comes from (RAG, retrieval-augmented generation). You can follow up on an answer as in a conversation. It also turns the selected documents into flashcards or a multiple-choice quiz, checks uploaded files for prompt injection before they can be used, and builds a concept graph of the documents you upload.

It comes with two document sets: 840 articles from *The Forest* game wiki, and 5 documents about Kestrel Analytics, the example company provided with the course.

## Contributors

| Name | Github |
|---|---|
| Charles Stucke | [cstucke](https://github.com/cstucke) |
| Jakub Motysia | [Jakub-Tenders](https://github.com/Jakub-Tenders) |

## Quick start

You need **Python 3.10 or newer** and an **LLM with an OpenAI-compatible API**. `.env.example` is set up for Google Gemini, which only needs a Google AI Studio API key ([create one here](https://aistudio.google.com/app/apikey)). To use another LLM, see [Configure](#2-configure).

```bash
git clone https://github.com/cstucke/norag-rag.git
cd norag-rag

python3 -m venv .venv
source .venv/bin/activate            # Windows: .venv\Scripts\activate
pip install -r requirements.txt

cp .env.example .env                 # Windows: copy .env.example .env
# open .env and set LLM_API_KEY (and LLM_URL and LLM_MODEL if you don't use Gemini)

uvicorn app.main:app
```

Then open **<http://127.0.0.1:8000>** in a browser. Stop the app with `Ctrl+C`.

Run every command from the repository root (the folder that holds this README), with the virtual environment active.

## Install and start, step by step

### 1. Install

```bash
python3 -m venv .venv
source .venv/bin/activate            # Windows: .venv\Scripts\activate
pip install -r requirements.txt
```

The first install takes a few minutes, because it downloads PyTorch and ChromaDB.

### 2. Configure

```bash
cp .env.example .env
```

Open `.env` and set the three values. The app needs all three and works with any LLM server that has an OpenAI-compatible API:

| Variable | Value |
|---|---|
| `LLM_URL` | The base URL of the server's OpenAI-compatible API. `.env.example` has Google Gemini's: `https://generativelanguage.googleapis.com/v1beta/openai/` |
| `LLM_API_KEY` | Your API key for that server. For Gemini, your key from [Google AI Studio](https://aistudio.google.com/app/apikey). If your server needs no key, put any text |
| `LLM_MODEL` | The model id, as the server names it. `.env.example` has `gemini-3.5-flash` |

For example, for a server of your own:

```bash
LLM_URL="http://localhost:11434/v1"
LLM_API_KEY="anything"
LLM_MODEL="your-model-id"
```

You can also put the values in `.env.local`: it is read first, so it wins over `.env`. Variables already set in your shell win over both files. The app reads the files when it starts, so restart it after a change.

Two things to know with another LLM: the app asks the server for JSON output (`response_format` `json_object`), and the cost shown in Details is computed with Gemini's prices.

### 3. Prepare the documents (optional)

```bash
python -m app.rag --index-all
```

This splits the 845 documents into passages and indexes them. It takes about 2 minutes and needs no API key. The first run also downloads the embedding model (`all-MiniLM-L6-v2`, about 90 MB), once.

If you skip this step, the app prepares the documents you select the first time you ask about them, so that first question is slow. Running the command again skips documents that haven't changed.

### 4. Start the app

```bash
uvicorn app.main:app
```

Open <http://127.0.0.1:8000>. To use another port, add `--port 8001`.

Don't add `--host 0.0.0.0`. The app has no login, so anyone on your network could read the documents and traces and use your API key.

## Using the app

1. **Pick documents.** In the Documents panel, type `kestrel` or `forest` in the filter and click **Select all (filtered)**, or tick documents one by one.
2. **Ask a question.** Type it and click **Ask**. The answer comes with numbered references; click one to read the passage it comes from.
3. **Follow up.** Ask the next question as you would in a conversation, for example "and for the Business plan?" after a question about single sign-on. The app first rewrites a follow-up into a question that stands on its own, and shows it as **Searched for** when it changed your wording. Earlier turns stay on screen above the newest answer. Under each answer, suggested next questions are buttons: click one to ask it. **New conversation** clears the turns, so the next question is read on its own. A follow-up costs one extra LLM call, for the rewrite; the first question of a conversation doesn't.
4. **See what happened.** Click **Details** under an answer to see each step, how long it took, the tokens used and the cost.
5. **Make a quiz.** Choose **Make a quiz**, then the type (flashcards or multiple choice), the number of items (1 to 10) and the difficulty, and click **Generate**. Every item links to its source passage. An item whose quote isn't found word for word in its source is dropped, and the page says how many were.
6. **Upload a document.** Use **Upload** for a `.md` or `.txt` file (UTF-8, up to 2 MB). The file is scanned first. If it contains text that looks like instructions to the AI, it is held: click **Review**, then **Approve** to add it unchanged or **Reject** to delete it.

### Advanced

Tick **Advanced** (top right) to show the rest:

- **Settings:** chunk size, overlap and top-k.
- **Retrievers:** dense (meaning), BM25 (keywords) and the concept graph. Dense and BM25 are on by default.
- **Retrieved passages** and the raw trace, under each answer.
- **Evaluation** and **Words** tabs: the retrieval evaluation and the word statistics from earlier versions.
- **Graph** tab: build and browse the concept graph (next section).

### Concept graph

The concept graph links the people, places and things named in a set of documents. It can be built for **the documents you upload** and for the Kestrel documents, then browsed and used as a retriever:

1. **Upload** your documents in the Ask tab (step 5 above).
2. Tick **Advanced**, open the **Graph** tab and keep **Uploaded documents** selected. The page shows how many passages there are to read.
3. Click **Build**. The app reads each passage with one LLM call. One click reads at most 40 passages, so a long document needs several clicks; **Stop** keeps what is already done. To spend few LLM calls, upload a short document: at the default settings a passage is 1,000 characters, so a 4,000-character file is about 5 calls.
4. **Browse.** The Entities table lists what was found. Click an entity to see its links, click the entity at the other end of a link to move there, and click a passage name to read the text a link comes from.
5. **Search with it.** Back in the Ask tab, select your documents, tick **Graph** under Retrievers and ask. Under the answer, **Graph path** shows the entities found in your question and the links that were followed.

Things to know:

- Choose **Kestrel** in the Graph tab to build the graph of the Kestrel documents the same way (38 passages at the default settings, one click).
- A graph belongs to the chunk settings it was built with. After a change of chunk size or overlap, build it again.
- When you upload another document or replace one, the Graph tab shows the passages left to read. Click **Build** to bring the graph up to date. Only the new passages are read. The entities of a deleted document leave the Graph tab at once.
- If the LLM refuses some passages (a rate limit, for example), the build stops and says why. Click **Build** again later: only the missing passages are read.
- Uploaded documents use six general entity types (Person, Organization, Place, Event, Object, Concept) and free relation names. Kestrel uses the fixed schema from V3.
- Graph files are in `data/graph/`, one per document set and chunk settings.

## Traces

Every question, quiz, upload, review decision and indexing run is recorded as one line in `data/traces/<UTC date>.jsonl`. The Details button reads from these files.

- **What a trace holds:** the question and the answer, the ids of the passages used, the steps and their timings, token counts, cost, the model and the outcome. For a follow-up it also holds the rewritten question and an id shared by the turns of one conversation. An upload trace holds the file name and the rule and line of each finding.
- **What it never holds:** the prompt, the text of a passage, the flagged text of an upload, or the API key.
- **Where it goes:** nowhere. `data/` stays on your machine and is not committed.
- **How long it is kept:** files older than 30 days are deleted when a new day's file is created. To delete all traces now, delete the `data/traces/` folder.

## Scanner command

To scan files or folders for prompt injection without uploading them:

```bash
python -m app.scanner corpus/uploads my_notes.md
```

It only reports what it finds. Nothing is moved or deleted.

## Troubleshooting

| What you see | What to do |
|---|---|
| The first question after start-up takes up to 20 seconds | Normal: the embedding model is loading. Later questions are faster |
| "LLM not configured. Set LLM_URL, LLM_API_KEY and LLM_MODEL in .env." | `.env` is missing or one of the three values is empty. Set them and restart the app |
| "LLM rejected the request (API key or model id)." | Check `LLM_API_KEY` and `LLM_MODEL` in `.env`, then restart. A server that doesn't support JSON output (`response_format`) gives the same message |
| "LLM rate limit reached — try again shortly." | Wait a minute and ask again |
| "LLM call failed." | Usually a temporary error on the LLM server's side, or a wrong `LLM_URL`. Ask again, then check the URL |
| `No module named 'app'` | Run the command from the repository root |
| The port is already in use | Start with `uvicorn app.main:app --port 8001` |
| Graph is greyed out under Retrievers | No graph is built for the current chunk settings. Build one in the Graph tab |

## Project layout

| Path | What it is |
|---|---|
| `app/` | The web app: API (`main.py`), the RAG pipeline (`rag.py`), follow-up questions (`conversation.py`), quiz generation (`study.py`), the injection scanner (`scanner.py`), traces (`trace.py`) and the page (`static/`) |
| `corpus/` | The documents: `forest/`, `kestrel/` and your uploads in `uploads/` |
| `evaluation/` | The retrieval evaluation, its questions and results |
| `scripts/` | The one-off script that fetched the wiki snapshot |
| `data/` | Created at run time, not committed: the index, settings, traces, concept graphs and held uploads |
| `REPORT.md` | The design decisions and evaluation results |

The sections below describe earlier versions of the project and the course's demo scripts.

## V3 — Hybrid retrieval

Three retrievers can be switched on and off: `dense` (V2), `bm25` and `graph` (concept graph). The ones that are on are fused with RRF.

### Switching retrievers

- Ask and Evaluation tabs: the **Retrievers** checkboxes. Graph is disabled until a graph exists for the current chunk settings.
- Evaluation command: `--retrievers dense,bm25,graph` (any subset, comma-separated).
- Default: `DEFAULT_RETRIEVERS` in `app/hybrid.py` (used when the UI or the command doesn't say).

### BM25

The index is a JSON file per chunk configuration in `data/bm25/`. It builds itself on the first search and is rebuilt whole when the chunks in Chroma change. To force a rebuild at the saved settings: `python -m app.bm25_index --build`.

### Concept graph commands (Kestrel)

These commands work on the Kestrel graph only. The graph of uploaded documents is built in the Graph tab (see [Concept graph](#concept-graph) above).

The graph is built with one LLM call per Kestrel chunk, at the saved chunk settings, and lives in `data/graph/kestrel_cs{N}_ov{N}.json`. It is tied to those settings: change the chunk size or overlap and the graph has to be built again.

```bash
python -m app.graph build [--sleep S]          # extract every chunk (S seconds between calls, for rate limits)
python -m app.graph build --retry-failed       # redo only the chunks that failed
python -m app.graph resolve                    # rebuild entities and edges from the stored extractions (no LLM call)
python -m app.graph stats                      # entities, edges, merges, failures, build cost
```

### Evaluation

The three minimum configurations (retrieval only, no LLM call):

```bash
python -m evaluation.run --questions evaluation/questions/forest.jsonl  --corpus forest  --retrievers dense
python -m evaluation.run --questions evaluation/questions/kestrel.jsonl --corpus kestrel --retrievers dense
python -m evaluation.run --questions evaluation/questions/forest.jsonl  --corpus forest  --retrievers dense,bm25
python -m evaluation.run --questions evaluation/questions/kestrel.jsonl --corpus kestrel --retrievers dense,bm25
python -m evaluation.run --questions evaluation/questions/kestrel.jsonl --corpus kestrel --retrievers dense,bm25,graph
```

`--candidates N` sets how long each retriever's list is before fusion (default 20, at least 10) and `--rrf-k N` the RRF constant (default 60). Each run writes `evaluation/results/<UTC stamp>_<corpus>_cs{N}_ov{N}_<retrievers>.json`.

### Extraction quality

```bash
python -m evaluation.graph_sample [--n 10] [--seed 42]
```

picks random graph edges and writes them, with the text of their chunks, to `evaluation/results/<UTC stamp>_kestrel_graph_sample.json`. Every `grade` starts as `null`: fill it in by hand with `correct`, `wrong` or `unsupported`.

## Course demo scripts

The scripts the course started from. They are separate from the app and use the same virtual environment and `.env`.

This workspace contains Python applications to compare **NoRAG** (full-context prompting) versus **RAG** (retrieval-augmented generation) using **Google Gemini** via the **OpenAI SDK**.

For the BM25 lexical-retrieval example, see [bm25/README.md](./bm25/README.md).
For the two-hop retrieval exercise, see the [concept graph challenge](./concepts/concept_graph_challenge_part1.md).

### Applications

1. `ask_norag_google.py`
- NoRAG with Google Gemini via OpenAI SDK (`gemini-3.5-flash-lite`).
- Loads `docs/CrimeAndPunishment.txt`, injects a "needle" passage, and runs two direct large-context questions:
	- a baseline question about Marmeladov (present in the original book)
	- a needle question about Denis (the injected passage)

2. `ask_rag_google.py`
- RAG with Google Gemini for generation via OpenAI SDK.
- Uses local embeddings (`all-MiniLM-L6-v2`) + local ChromaDB (`chroma_db/`) to retrieve relevant chunks before asking the model.
- Currently points to `docs/CrimeAndPunishment.txt` and retrieves `n_results=5` for the question: `What does this say about Denis?`

3. `bm25/ask_bm25_rag_google.py`
- RAG with Google Gemini for generation via OpenAI SDK and in-memory BM25 lexical retrieval.
- See [bm25/README.md](./bm25/README.md) for how it works, how to run it, and the BM25 challenge.

### Project Structure

- `docs/CrimeAndPunishment.txt`: main source text used by the scripts.
- `docs/CrimeAndPunishment-shorter.txt`: shortened version of the main source text for quicker testing and rapid experimentation in Gemini online at https://gemini.google.com/app (See note below)
- `chroma_db/`: persistent local vector database (used by RAG scripts).
- `bm25/`: BM25 retrieval example and challenges.
- `concepts/`: multi-hop retrieval challenge.
- `requirements.txt`: Python dependencies.

### Prerequisites

- Python 3.10+ (recommended)
- API key:
   - `GOOGLE_API_KEY` from [Google AI Studio](https://aistudio.google.com/app/apikey)


### Setup

1. Create and activate a virtual environment:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

2. Install dependencies:

```bash
pip install -r requirements.txt
```

3. Configure environment variables:

```bash
cp .env.example .env
```

Then edit `.env` and set your real keys.

### Run Each Application

With your virtual environment activated:

#### 1) NoRAG + Google

```bash
python ask_norag_google.py
```

#### 2) RAG + Google

```bash
python ask_rag_google.py
```

#### 3) BM25 RAG + Google

```bash
python bm25/ask_bm25_rag_google.py
```

### Notes

- Both applications use the OpenAI SDK to interact with Google Gemini via Google's OpenAI-compatible endpoint.
- The RAG app splits the text into fixed-size chunks with an overlap (`CHUNK_SIZE`, `OVERLAP_PERCENT` and `MIN_PARAGRAPH_LENGTH` at the top of the script), indexes them into `chroma_db/` and reuses them across runs.
- There is one index per document (`DOCUMENT_FILE`) and chunking configuration. When no index exists for the current document and settings, the script asks before building one (this takes a little while).
- Debug prompt printing can be enabled by passing `debug=True` in the NoRAG app.
- RAG app prints retrieved context for verification.
- Streaming output is enabled by default in both applications (controlled by `STREAM_ON` variable).

- Using the shortened version of the text (`docs/CrimeAndPunishment-shorter.txt`)
	- Go online at https://gemini.google.com/app
	- At the prompt, start writing "Here is a story: ",
	- Then paste the content of docs/CrimeAndPunishment-shorter.txt into the Gemini chat app and then, at the end of the prompt, ask "What can you tell me about Denis Amselemovitch?"
	- Observe the response from Gemini.

### Free books from Project Gutenberg
- https://www.gutenberg.org/
### Crime and Punishment by Fyodor Dostoevsky
- https://www.gutenberg.org/ebooks/2554
### Huckleberry Finn by Mark Twain
- https://www.gutenberg.org/ebooks/76
