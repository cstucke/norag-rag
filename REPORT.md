# REPORT

## Team Details
| Member | Worked on |
|---|---|
| Charles Otto STUCKE | Entire project |

## Decision Log

### 1. Corpus
- **Options considered:** Hobbies, course materials, and other 'niche' references.
- **Picked:** The Forest online wiki, one of my favorite video games of all time.
- **Why:** From personal experience, I know that LLMs are unreliable when trying to find accurate information on The Forest. The LLMs that we'll make calls to are unlikely to have been trained with this data in mind, so it's good to test the RAG capabilities against the wiki itself.

### 2. Stack (frontend, backend, embedding model, vector database, LLM)
- **Options considered:** Frontend: React/Next with Zod or plain HTML + JS, Backend: FastAPI, Flask, or Node.js, Vector DB: ChromaDB (never personally used one before, so went with your recommendation), LLM: Gemini
- **Picked:** Plain HTML + JS, FastAPI, MiniLM, ChromaDB, Gemini 3.5 Flash
- **Why:** Among the aforementioned technologies, I have the most experience with the selected ones. Furthermore, the LLM / embedding model choices are limited due to the resources at my disposal.

### 3. Question set
- **Options considered:** A variety of questions, the exact structure and reporting syntax wasn't given.
- **Picked:** This set of 8 questions.
- **Why:** I choose a series of questions that give insight to the places where our implementation decision really mattered (rather than where two different choices could have a convergent implementation / result).

### 4. What "the right passage was retrieved" means
- **Options considered:** Correct document retrieval, exact chunk id, or overlap with the evidence text.
- **Picked:** All evidence text is direct quotes, with the location saved as a character span in the file. The retrieved chunk is validated if it originates from the same file and matches with the majority of the span (at least 50%).
- **Why:** We can avoid the failures that come with exact chunk ids while allowing for greater accuracy than simple document retrieval validity.

### 5. When nothing relevant is retrieved
- **Options considered:** Distance from correct answer or letting the LLM decide
- **Picked:** No threshold for retrieval. If no chunks are returned, the app will simply show "nothing retrieved".
- **Why:** We want to avoid giving a wrong answer silently: that would defeat the elementary purpose of this RAG implementation.

### 6. Response schema and citation check
- **Options considered:** Free text, JSON citing chunk ids, JSON citing excerpt numbers
- **Picked:** {answerable, answer, citations: [int]}
- **Why:** Excerpt numbers are shorter than the generated chunk ids, so we can limit the possibility that the model mis-copies. Invalid responses aren't retried.

### 7. What a reference points to
- **Options considered:** File, chunk, line number
- **Picked:** chunk, correlated with the document, line, and source URL.
- **Why:** By utilizing the chunk, we can see what the LLM was provided and use that to rectify against the answer. We also use the context around the chunk to further verify the output.

### 8. What is recomputed when a parameter changes
- **Options considered:** rebuild the entire index scheme on every change or keep a collection per chunk setting and indexing there
- **Picked:** Index a document completely upon its initial inclusion, then create a new collection upon changes to chunk size.
- **Why:** If every change required the whole indexing schema to be re-embedded, it would be very costly to iterate.

## Known Failures


### <Failure>
- **Question:** "How much health does a starving cannibal have on normal difficulty?"
- **Observed:** status not_found. The top 5 retrieved were chunks of the correct page, but the chunk with the correct information was not retrieved.

- **Question:** "In which update was the katana added?", "Who is Matthew Cross?", "Has Sons of the Forest been released?"
- **Observed:** 3 of 5 probe calls returned llm_error. Retrieval worked for all three, but the response returned an HTTP 503, with a message that "This model is currently experiencing high demand". This failure doesn't demonstrate anything about the integrity / validity of the project, but it does show that dependencies beyond the project scope can have a massive impact on the project's outcomes.

- **Question:** "Has Sons of the Forest been released?"
- **Observed:** The first two retrieved articles are the wiki landing page. The correct page (which actually references Sons of the Forest) only appears at rank 3.