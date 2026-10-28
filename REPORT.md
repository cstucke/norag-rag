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
- **Options considered:** 
- **Picked:**
- **Why:**

### 4. What "the right passage was retrieved" means
- **Options considered:**
- **Picked:**
- **Why:**

### 5. When nothing relevant is retrieved
- **Options considered:**
- **Picked:**
- **Why:**

### 6. Response schema and citation check
- **Options considered:**
- **Picked:**
- **Why:**

### 7. What a reference points to
- **Options considered:**
- **Picked:**
- **Why:**

### 8. What is recomputed when a parameter changes
- **Options considered:**
- **Picked:**
- **Why:**

## Known Failures


### <Failure>
- **Question:**
- **Observed:**