# norag-rag project

This workspace contains Python applications to compare **NoRAG** (full-context prompting) versus **RAG** (retrieval-augmented generation) using **Google Gemini** via the **OpenAI SDK**.

For the BM25 lexical-retrieval example, see [bm25/README.md](./bm25/README.md).
For the two-hop retrieval exercise, see the [concept graph challenge](./concepts/concept_graph_challenge_part1.md).

## Applications

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

## Project Structure

- `docs/CrimeAndPunishment.txt`: main source text used by the scripts.
- `docs/CrimeAndPunishment-shorter.txt`: shortened version of the main source text for quicker testing and rapid experimentation in Gemini online at https://gemini.google.com/app (See note below)
- `chroma_db/`: persistent local vector database (used by RAG scripts).
- `bm25/`: BM25 retrieval example and challenges.
- `concepts/`: multi-hop retrieval challenge.
- `requirements.txt`: Python dependencies.

## Prerequisites

- Python 3.10+ (recommended)
- API key:
   - `GOOGLE_API_KEY` from [Google AI Studio](https://aistudio.google.com/app/apikey)


## Setup

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

## Run Each Application

With your virtual environment activated:

### 1) NoRAG + Google

```bash
python ask_norag_google.py
```

### 2) RAG + Google

```bash
python ask_rag_google.py
```

### 3) BM25 RAG + Google

```bash
python bm25/ask_bm25_rag_google.py
```

## Notes

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

# Free books from Project Gutenberg
- https://www.gutenberg.org/
# Crime and Punishment by Fyodor Dostoevsky
- https://www.gutenberg.org/ebooks/2554
# Huckleberry Finn by Mark Twain
- https://www.gutenberg.org/ebooks/76



## V3 — Hybrid retrieval

Three retrievers can be switched on and off: `dense` (V2), `bm25` and `graph` (concept graph, Kestrel only). The ones that are on are fused with RRF.

### Switching retrievers

- Ask and Evaluation tabs: the **Retrievers** checkboxes. Graph is disabled until a graph exists for the current chunk settings.
- Evaluation command: `--retrievers dense,bm25,graph` (any subset, comma-separated).
- Default: `DEFAULT_RETRIEVERS` in `app/hybrid.py` (used when the UI or the command doesn't say).

### BM25

The index is a JSON file per chunk configuration in `data/bm25/`. It builds itself on the first search and is rebuilt whole when the chunks in Chroma change. To force a rebuild at the saved settings: `python -m app.bm25_index --build`.

### Concept graph (Kestrel only)

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