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

## V2

### Question sets
Both sets use the Kestrel format and live in `evaluation/questions/<corpus>.jsonl`. The Kestrel set is the provided starter set, copied verbatim. The Forest set has 12 questions, two for each of Kestrel's six cases, so it covers all six.

| Type | Kestrel | The Forest |
|---|---|---|
| `exact_identifier` | 2 | 2 |
| `split_answer` | 2 | 2 |
| `vocabulary` | 1 | 2 |
| `versions` | 2 | 2 |
| `two_hop` | 1 | 2 |
| `not_in_corpus` | 2 | 2 |
| **Total (answerable)** | **10 (8)** | **12 (10)** |

How each case appears in the Forest wiki:
- **Exact identifier:** rows of the console-command table that differ only by a number (`additem 242`, `forcerain 5`). The command name `forcerain` suggests rain, but `forcerain 5` gives cloudy weather.
- **Split answer:** answers that sit at opposite ends of a long page, with a table between them (Sanity, Save).
- **Different vocabulary:** questions that use words absent from the corpus ("queasy", "hypothermia") where the wiki says "sick" and "cold".
- **Not in the corpus:** who voices Eric LeBlanc (a strong distractor, because the credits list the voice cast without roles) and the game's Metacritic score.
- **Two versions:** the wiki keeps old and new facts side by side. The autopsy report changed from Megan to Jessica Cross in v1.0, and the booze fire upgrade was removed although the same page still explains how to apply it.
- **Two hops:** an alias leads to a subject number and then an age (Legsy → Virginia → Jarius Project), and a cave leads to a tool and then another cave (Cave 6 → rebreather → Cave 5).

The Forest questions were drafted by Claude Code (an AI assistant) at my request, from the frozen snapshot. Every evidence quote passes the harness's evidence check, which requires it to appear exactly once in its document. Evidence only credits its own page. In q07 and q10 the same fact also appears on another page, and retrieving that page counts as a miss. The sets were frozen after the no-context test and before the comparison runs.

### No-context test
Results files, all in `evaluation/results/`:
- `20261031T111015Z_kestrel_nocontext.json` for Kestrel.
- `20261103T060446Z_forest_nocontext.json` for The Forest. This run spaced the calls 13 s apart to stay under the API's per-minute limit, with the same prompt and questions. Its q07 call failed (`llm_error`).
- `20261103T055939Z_forest_nocontext.json` for The Forest's first run. 6 of its 12 calls failed, 5 of them on the rate limit. q07 below comes from this run.

"Answered without retrieval?" compares the model's answer with the expected answer: Yes, Partly or No. For unanswerable questions, the right answer is that it isn't in the documents.

| Set | Question id | Answered without retrieval? | Kept / replaced | Why |
|---|---|---|---|---|
| Kestrel | q01 | No | Kept | Said it has no information about Kestrel or KST-2044. The Kestrel set is provided and stays fixed so results compare across teams. |
| Kestrel | q02 | No | Kept | Said it has no information about KST-4012. |
| Kestrel | q03 | No | Kept | Said it has no information about Kestrel's failed-payment process. |
| Kestrel | q04 | No | Kept | Said it has no information about Kestrel's plans or single sign-on setup. |
| Kestrel | q05 | No | Kept | Gave generic advice (contact support, reset MFA), with none of the backup-code or Admin-reset steps. |
| Kestrel | q06 | No | Kept | Said it has no information about Kestrel's refund policy. |
| Kestrel | q07 | No | Kept | Said it has no information about Kestrel's pricing. |
| Kestrel | q08 | No | Kept | Said it has no information about KST-5031. |
| Kestrel | q09 | No | Kept | Answered yes, describing the "Kestrel LiNK" app of an unrelated Kestrel product. |
| Kestrel | q10 | No | Kept | Said it has no information. That matches the expected refusal, but only because the model doesn't know Kestrel. |
| The Forest | q01 | No | Kept | Answered "Flintlock Pistol" (the first run said "Camcorder"). |
| The Forest | q02 | No | Kept | Said heavy rain: the command name misleads it, as intended. |
| The Forest | q03 | Yes | Kept | Gave the effigy rule and the ways to raise sanity. I kept it because the retrieval metric doesn't depend on what the model knows, but its answer grade can't separate retrieval from training. |
| The Forest | q04 | Partly | Kept | Named the tents and the yacht (and added the crashed plane), but gave a different save path, `LocalLow\Endnight\TheForest` instead of `LocalLow\SKS\TheForest`. |
| The Forest | q05 | Partly | Kept | Named berry poisoning and the Stats tab of the Survival Guide. It missed that the game calls it sickness, doesn't show it on the HUD, and gives it a 20% chance. |
| The Forest | q06 | Partly | Kept | Fire and leaving the snow match. It missed booze and sunlight. |
| The Forest | q07 | No | Kept | Answered "Megan Cross", which is the answer from before v1.0. |
| The Forest | q08 | No | Kept | Answered yes, which is the answer from before the upgrade was removed. |
| The Forest | q09 | No | Kept | Answered "4 years old". |
| The Forest | q10 | Yes | Kept | Named Cave 6, the rebreather and Cave 5, and missed only the two explosives. Kept for the same reason as q03. |
| The Forest | q11 | No | Kept | Claimed Eric has no credited voice actor instead of saying it isn't in the documents. |
| The Forest | q12 | No | Kept | Gave 83/100 (PC) and 78/100 (PS4) from training instead of saying it isn't in the documents. |

### Retrieval results
| Corpus | Config (cs / ov) | Type | n | hit@1 | hit@3 | hit@5 | hit@10 | Results file |
|---|---|---|---|---|---|---|---|---|
| Kestrel | 1000 / 200 | overall | 8 | 0.750 | 0.875 | 1.000 | 1.000 | `evaluation/results/20261031T103424Z_kestrel_cs1000_ov200.json` |
| Kestrel | 1000 / 200 | `exact_identifier` | 2 | 1.000 | 1.000 | 1.000 | 1.000 |  |
| Kestrel | 1000 / 200 | `split_answer` | 2 | 1.000 | 1.000 | 1.000 | 1.000 |  |
| Kestrel | 1000 / 200 | `vocabulary` | 1 | 1.000 | 1.000 | 1.000 | 1.000 |  |
| Kestrel | 1000 / 200 | `versions` | 2 | 0.500 | 1.000 | 1.000 | 1.000 |  |
| Kestrel | 1000 / 200 | `two_hop` | 1 | 0.000 | 0.000 | 1.000 | 1.000 |  |
| Kestrel | 1000 / 200 | `not_in_corpus` | 0 | – | – | – | – |  |
| Kestrel | 500 / 100 | overall | 8 | 0.250 | 0.750 | 0.750 | 1.000 | `evaluation/results/20261103T055924Z_kestrel_cs500_ov100.json` |
| Kestrel | 500 / 100 | `exact_identifier` | 2 | 0.000 | 0.500 | 0.500 | 1.000 |  |
| Kestrel | 500 / 100 | `split_answer` | 2 | 0.500 | 1.000 | 1.000 | 1.000 |  |
| Kestrel | 500 / 100 | `vocabulary` | 1 | 1.000 | 1.000 | 1.000 | 1.000 |  |
| Kestrel | 500 / 100 | `versions` | 2 | 0.000 | 1.000 | 1.000 | 1.000 |  |
| Kestrel | 500 / 100 | `two_hop` | 1 | 0.000 | 0.000 | 0.000 | 1.000 |  |
| Kestrel | 500 / 100 | `not_in_corpus` | 0 | – | – | – | – |  |
| The Forest | 1000 / 200 | overall | 10 | 0.200 | 0.300 | 0.600 | 0.600 | `evaluation/results/20261103T055915Z_forest_cs1000_ov200.json` |
| The Forest | 1000 / 200 | `exact_identifier` | 2 | 0.000 | 0.000 | 0.000 | 0.000 |  |
| The Forest | 1000 / 200 | `split_answer` | 2 | 0.500 | 1.000 | 1.000 | 1.000 |  |
| The Forest | 1000 / 200 | `vocabulary` | 2 | 0.000 | 0.000 | 0.500 | 0.500 |  |
| The Forest | 1000 / 200 | `versions` | 2 | 0.500 | 0.500 | 1.000 | 1.000 |  |
| The Forest | 1000 / 200 | `two_hop` | 2 | 0.000 | 0.000 | 0.500 | 0.500 |  |
| The Forest | 1000 / 200 | `not_in_corpus` | 0 | – | – | – | – |  |
| The Forest | 500 / 100 | overall | 10 | 0.200 | 0.400 | 0.400 | 0.400 | `evaluation/results/20261103T060122Z_forest_cs500_ov100.json` |
| The Forest | 500 / 100 | `exact_identifier` | 2 | 0.000 | 0.000 | 0.000 | 0.000 |  |
| The Forest | 500 / 100 | `split_answer` | 2 | 0.500 | 1.000 | 1.000 | 1.000 |  |
| The Forest | 500 / 100 | `vocabulary` | 2 | 0.500 | 0.500 | 0.500 | 0.500 |  |
| The Forest | 500 / 100 | `versions` | 2 | 0.000 | 0.500 | 0.500 | 0.500 |  |
| The Forest | 500 / 100 | `two_hop` | 2 | 0.000 | 0.000 | 0.000 | 0.000 |  |
| The Forest | 500 / 100 | `not_in_corpus` | 0 | – | – | – | – |  |

`not_in_corpus` questions have no evidence, so they are left out of the retrieval metrics (n = 0, shown as –). A hit means that one retrieved chunk covers at least half of one evidence quote. all@k and MRR are in each results file. The two other Kestrel 1000 / 200 files (`20261031T124441Z`, `20261102T103738Z`) came from the API and UI checks and are identical to the Step 3 run.

### What changed between configurations, and what moved
I compared V1's default, 1000 / 200, with 500 / 100. Both values are halved, so the overlap stays at 20% and only the chunk size changes. Every k comes from the same top-10 ranking, and evidence is located by character span, so both configurations are scored on the same evidence.

Smaller chunks were worse on both corpora, so 1000 / 200 is the best configuration for both.

| Corpus | Config | hit@1 | hit@5 | all@5 | MRR |
|---|---|---|---|---|---|
| Kestrel | 1000 / 200 | 0.750 | 1.000 | 0.875 | 0.844 |
| Kestrel | 500 / 100 | 0.250 | 0.750 | 0.625 | 0.533 |
| The Forest | 1000 / 200 | 0.200 | 0.600 | 0.300 | 0.325 |
| The Forest | 500 / 100 | 0.200 | 0.400 | 0.200 | 0.300 |

What moved:
- **Kestrel q01 (exact identifier):** rank 1 → 6. At 500 / 100 the KST-2044 chunk ranks behind the runbook's introduction, the KST-2051 and KST-3020 sections, and two product-guide chunks. The runbook is a list of near-identical code sections, and smaller chunks give the embedding less to tell them apart.
- **Kestrel q03 (split answer):** all four parts were in the top 10 at 1000 / 200. At 500 / 100 the last part ("60 days … suspended") drops out, and the 2025 policy's failed-payment section and the KST-6002 runbook entry take its place.
- **Kestrel q08 (two hops):** hop 1 falls from rank 4 to 10. Hop 2 is missing at both sizes.
- **Forest q06 (vocabulary):** rank 4 → 1, the only clear gain. At 1000 / 200 the matching chunk mixes the causes of cold with the ways to keep warm, and it ranks behind Hydration and Suggestions. The smaller chunk holds the warmth list and the booze line and ranks first.
- **Forest q08 (versions):** rank 4 → out of the top 10. At 500 / 100 the top 10 fills with smaller fire-upgrade chunks from Upgrades, Burning, Booze and Cloth. That includes the stale "Fire Upgrade Mechanics" chunk at rank 5, but not the chunk with the removal sentence.
- **Forest q03 and q10:** q03 no longer has all three parts in the top 10, and q10 loses its only hit (rank 4).
- **Forest q01, q02, q05 and q09** miss at both sizes. A different chunk size doesn't help with an exact number, a word that isn't in the corpus, or a chain of two pages.

### Answer grading
#### Grading rules
- Using purely the results file as context, I compare `answer` with the question's `expected_answer`, and I check it against the texts of the chunks it cites (`references`, with their text in `context`).
- **correct:** the answer has every key fact of the expected answer, and everything it says is backed by the cited chunks. furthermore, a 'correct' answer does not include incorrect information.
- **partial:** everything the answer says is right and backed, but part of the expected answer is missing, for example one half of a split answer or one hop of a two-hop question.
- **wrong:** the answer gets a key fact wrong, answers a different question, or says the answer is not in the documents when it is.
- **unsupported:** the answer says something the cited chunks don't say, even if it happens to be true.
- **Unanswerable questions:** the answer is correct only if the app says the answer is not in the documents. Any other answer is wrong.
- **Two versions:** giving the old value as the answer is wrong. Mentioning the old value next to the current one is fine. Giving both without saying which one is current is partial.
- **When two grades fit,** I use the worse one, in this order: wrong, unsupported, partial, correct.
- Wording, length and extra correct details don't change the grade.
- An LLM error (`status: error`) leaves nothing to grade. I note it in `grade_note` and count it separately from the four grades.
- The grade goes in `grade` and a one-line reason goes in `grade_note`.
#### Graded run
Configuration 1000 / 200 with top-k 5, Kestrel set, `evaluation/results/20261031T104558Z_kestrel_cs1000_ov200_llm_k5.json`. 1000 / 200 is the best configuration on both corpora, and this run already has Kestrel's answers next to their chunks.

| Grade | Count |
|---|---|
| correct | 6 |
| partial | 3 |
| wrong | 0 |
| unsupported | 0 |

One more question, q03, ended in an LLM error, so it had no answer to grade. The three partial answers:
- **q04** left out the last two setup steps: testing with one Admin, then enforcing single sign-on.
- **q06** gave both refund policies without saying which one applies now.
- **q08** stopped at hop 1. It says to escalate to the team that owns postroom, but it doesn't name Messaging or its channel.

No answer said anything its cited chunks don't. Both unanswerable questions were correctly answered as not found.

### Diagnosed misses
#### Kestrel
- **Question:** q08 (`two_hop`), "Error KST-5031 happened on the last two scheduled reports. Which team should support contact, and where?"
- **Miss:** at 1000 / 200 the hop-1 runbook chunk is retrieved at ranks 4 and 9, but the hop-2 service-catalog chunk is not in the top 10 (all@10 = 0). The top 10 is nine runbook chunks and one product-guide chunk, and the answer stops at hop 1.
- **Words tab:** the question's distinctive words all point at the runbook. `kst` appears only in the runbook and the product guide, and `5031` appears in 2 chunks, both in the runbook. The word that links the two hops, `postroom`, isn't in the question. `messaging` and `oncall`, which appear only in the service catalog, aren't in the question either. The only question word the target chunk shares is the generic `team` (12 chunks).
- **Cause:** one query embedding can't follow a chain. The link (postroom) only becomes known after reading hop 1, so the catalog row is never close to the question.
- **What would fix it:** a second retrieval that uses what hop 1 found. That is query rewriting, which is out of scope here.

#### The Forest
- **Question:** q01 (`exact_identifier`), "What item does the console command additem 242 give me?"
- **Miss:** no evidence is in the top 10 at either configuration. At 1000 / 200 the top 10 has patch notes (V1.0) at ranks 1 and 3 and five other Console Commands chunks, but not the chunk with the `additem 242` row.
- **Words tab:** `242` appears 4 times in only 2 chunks: the right Console Commands chunk (the `additem`, `spawnitem` and `removeitem 242` cells) and Keycard Two ("Item ID 242"). `additem` appears 443 times in 57 chunks, because the item table is the same text over and over with a different number on each row.
- **Cause:** the embedding gives a number almost no weight, so the 57 `additem` chunks look alike and the right one has no advantage. A word lookup narrows `242` to 2 chunks.
- **What would fix it:** exact-match (keyword) or hybrid search, which is out of scope here.

### Decision log (V2)
### Evaluation setup (question sets, k values, configurations)
- **Options considered:**
  - Question sets: one file per corpus, or a single file with a corpus field. The Kestrel format, or V1's own format.
  - k: only the app's top-k, or several k values taken from one ranking.
  - Configurations: change the chunk size only, the overlap only, or both.
- **Picked:**
  - One file per corpus, `evaluation/questions/<corpus>.jsonl`, in the Kestrel format. The file name is also the corpus.
  - Each question is retrieved once (top 10). hit@k and all@k come from that one ranking at k = 1, 3, 5 and 10, along with MRR, overall and per type.
  - Two configurations: 1000 / 200 (V1's default) and 500 / 100.
- **Why:**
  - The Kestrel format is the one every team receives, so its file is used verbatim. Naming a file after its corpus means a question set can't run against the wrong corpus.
  - One ranking keeps the k values consistent with each other, and k = 10 shows whether the evidence is anywhere near the top. all@k matters for split and two-hop questions, where one hit isn't enough.
  - Halving both settings keeps the overlap at 20%, so only the chunk size changes. Evidence spans don't depend on chunking (decision 4), so both configurations are scored on the same evidence. Re-embedding the 840 Forest pages for the second configuration took about 2 minutes.

### Words analytics choices (tokenizer, case/stopwords/stemming, what is counted, scope)
- **Options considered:**
  - Tokenizer: split on whitespace, use a regex, or use the embedding model's own tokenizer.
  - Case folding, stopword removal and stemming, each on or off.
  - Counting the source files or the stored chunks.
  - Scope: one corpus, or the documents selected in the Ask tab.
- **Picked:**
  - A word is a run of letters and digits (`[a-z0-9]+` on lower-cased text), so `KST-2044` gives `kst` and `2044`.
  - No stopword removal and no stemming.
  - Counts come from the chunk texts as stored for the current chunk settings, header lines included. Text in an overlap is counted in both chunks.
  - One corpus at a time.
- **Why:**
  - The rule is simple enough to apply by hand, and an identifier still splits into parts that can be looked up: `242` appears in only 2 Forest chunks.
  - Keeping stopwords gives every word of a question a row. Keeping `refund` and `refunds` apart shows the exact forms the corpus uses, which is what a vocabulary miss is about.
  - Counting stored chunks shows exactly what was embedded, including fragments cut at chunk boundaries such as `refundabl`.
  - One corpus matches how question sets are scoped. Counting the whole Forest corpus takes about 1.6 s, so nothing is cached.

## V3

### Results
All runs at 1000 / 200, retrieval only, 20 candidates, RRF k = 60. Kestrel now has 10 answerable questions (I added two `two_hop`, q11 and q12), so it doesn't compare directly with V2. Files in `evaluation/results/`: `20261108T101135Z_kestrel_cs1000_ov200_dense.json`, `20261108T101200Z_kestrel_cs1000_ov200_dense+bm25.json`, `20261108T101229Z_forest_cs1000_ov200_dense.json`, `20261108T101254Z_forest_cs1000_ov200_dense+bm25.json`, `20261110T084513Z_kestrel_cs1000_ov200_dense+bm25+graph.json`.

| Corpus | Retrievers | Type | n | hit@1 | hit@3 | hit@5 | hit@10 | recall@1 | recall@3 | recall@5 | recall@10 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| Kestrel | dense | overall | 10 | 0.600 | 0.700 | 1.000 | 1.000 | 0.550 | 0.700 | 0.850 | 0.950 |
| Kestrel | dense | `exact_identifier` | 2 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 |
| Kestrel | dense | `split_answer` | 2 | 1.000 | 1.000 | 1.000 | 1.000 | 0.750 | 1.000 | 1.000 | 1.000 |
| Kestrel | dense | `vocabulary` | 1 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 |
| Kestrel | dense | `versions` | 2 | 0.500 | 1.000 | 1.000 | 1.000 | 0.500 | 1.000 | 1.000 | 1.000 |
| Kestrel | dense | `two_hop` | 3 | 0.000 | 0.000 | 1.000 | 1.000 | 0.000 | 0.000 | 0.500 | 0.833 |
| Kestrel | dense + bm25 | overall | 10 | 0.400 | 0.900 | 0.900 | 1.000 | 0.300 | 0.700 | 0.750 | 0.950 |
| Kestrel | dense + bm25 | `exact_identifier` | 2 | 1.000 | 1.000 | 1.000 | 1.000 | 0.750 | 0.750 | 1.000 | 1.000 |
| Kestrel | dense + bm25 | `split_answer` | 2 | 0.500 | 1.000 | 1.000 | 1.000 | 0.250 | 1.000 | 1.000 | 1.000 |
| Kestrel | dense + bm25 | `vocabulary` | 1 | 0.000 | 0.000 | 0.000 | 1.000 | 0.000 | 0.000 | 0.000 | 1.000 |
| Kestrel | dense + bm25 | `versions` | 2 | 0.500 | 1.000 | 1.000 | 1.000 | 0.500 | 1.000 | 1.000 | 1.000 |
| Kestrel | dense + bm25 | `two_hop` | 3 | 0.000 | 1.000 | 1.000 | 1.000 | 0.000 | 0.500 | 0.500 | 0.833 |
| Kestrel | dense + bm25 + graph | overall | 10 | 0.700 | 0.900 | 0.900 | 1.000 | 0.450 | 0.750 | 0.750 | 0.950 |
| Kestrel | dense + bm25 + graph | `exact_identifier` | 2 | 1.000 | 1.000 | 1.000 | 1.000 | 0.750 | 0.750 | 0.750 | 1.000 |
| Kestrel | dense + bm25 + graph | `split_answer` | 2 | 0.500 | 1.000 | 1.000 | 1.000 | 0.250 | 1.000 | 1.000 | 1.000 |
| Kestrel | dense + bm25 + graph | `vocabulary` | 1 | 0.000 | 0.000 | 0.000 | 1.000 | 0.000 | 0.000 | 0.000 | 1.000 |
| Kestrel | dense + bm25 + graph | `versions` | 2 | 0.500 | 1.000 | 1.000 | 1.000 | 0.500 | 1.000 | 1.000 | 1.000 |
| Kestrel | dense + bm25 + graph | `two_hop` | 3 | 1.000 | 1.000 | 1.000 | 1.000 | 0.500 | 0.667 | 0.667 | 0.833 |
| The Forest | dense | overall | 10 | 0.200 | 0.300 | 0.600 | 0.600 | 0.133 | 0.183 | 0.467 | 0.500 |
| The Forest | dense | `exact_identifier` | 2 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 |
| The Forest | dense | `split_answer` | 2 | 0.500 | 1.000 | 1.000 | 1.000 | 0.167 | 0.417 | 0.583 | 0.750 |
| The Forest | dense | `vocabulary` | 2 | 0.000 | 0.000 | 0.500 | 0.500 | 0.000 | 0.000 | 0.500 | 0.500 |
| The Forest | dense | `versions` | 2 | 0.500 | 0.500 | 1.000 | 1.000 | 0.500 | 0.500 | 1.000 | 1.000 |
| The Forest | dense | `two_hop` | 2 | 0.000 | 0.000 | 0.500 | 0.500 | 0.000 | 0.000 | 0.250 | 0.250 |
| The Forest | dense + bm25 | overall | 10 | 0.400 | 0.500 | 0.600 | 0.900 | 0.233 | 0.367 | 0.417 | 0.717 |
| The Forest | dense + bm25 | `exact_identifier` | 2 | 0.000 | 0.000 | 0.000 | 1.000 | 0.000 | 0.000 | 0.000 | 1.000 |
| The Forest | dense + bm25 | `split_answer` | 2 | 1.000 | 1.000 | 1.000 | 1.000 | 0.417 | 0.583 | 0.583 | 0.583 |
| The Forest | dense + bm25 | `vocabulary` | 2 | 0.000 | 0.000 | 0.000 | 0.500 | 0.000 | 0.000 | 0.000 | 0.500 |
| The Forest | dense + bm25 | `versions` | 2 | 0.500 | 1.000 | 1.000 | 1.000 | 0.500 | 1.000 | 1.000 | 1.000 |
| The Forest | dense + bm25 | `two_hop` | 2 | 0.500 | 0.500 | 1.000 | 1.000 | 0.250 | 0.250 | 0.500 | 0.500 |

`not_in_corpus` has no evidence (n = 0), so it's left out.

| Corpus | Retrievers | LLM calls / q | Tokens / q | Latency / q |
|---|---|---|---|---|
| Kestrel | dense | 0 | 0 | 637 ms |
| Kestrel | dense + bm25 | 0 | 0 | 619 ms |
| Kestrel | dense + bm25 + graph | 0 | 0 | 702 ms |
| The Forest | dense | 0 | 0 | 969 ms |
| The Forest | dense + bm25 | 0 | 0 | 801 ms |

Retrieval only, so no LLM calls or tokens. The latency differences are noise (the dense query dominates). The graph has no LLM call at query time, its cost is the one-off build (below).

What I take from it:
- BM25 fixes what dense can't. On The Forest the two identifier questions go from never found to ranks 6 and 9 (hit@10 0.0 → 1.0, overall 0.6 → 0.9). On Kestrel the two-hop hit@3 goes 0.0 → 1.0.
- It costs precision at the top: Kestrel hit@1 0.6 → 0.4 and hit@5 1.0 → 0.9, because of one vocabulary question (see below).
- The graph fixes the top of the ranking on chains: two-hop hit@1 0.0 → 1.0, overall hit@1 0.4 → 0.7, MRR 0.644 → 0.812. Deeper it changes nothing: hit@5 stays 0.9 and recall@10 stays 0.950. It even loses a bit on identifiers (recall@5 1.0 → 0.75).

### Default configuration, and why
`DEFAULT_RETRIEVERS = ("dense", "bm25")`. Dense + bm25 + graph is the best on Kestrel (MRR 0.812, hit@1 0.7), but the graph only exists for Kestrel: with it in the default, an evaluation on The Forest stops with `invalid_retrievers`. So the default is dense + bm25, which works on both corpora, and I switch the graph on for Kestrel. The graph also costs 37 LLM calls to build and has to be rebuilt when the chunk settings change.

### BM25: index, tokenization, updates
- **Index:** one JSON file per chunk configuration in `data/bm25/`, built from the chunks stored in Chroma, so BM25 and dense see the same chunks and ids.
- **Tokenization:** the Words tab's tokenizer (lowercase letters and digits, no stopwords, no stemming). `KST-5031` becomes `kst` and `5031`.
- **Scoring:** BM25, k1 = 1.5, b = 0.75, Lucene IDF, statistics over the whole collection, nothing tuned.
- **Updates:** on each search I hash the sorted chunk ids. If the file is missing or the hash differs, the whole index is rebuilt (one line printed). No incremental update, a full rebuild is fast at this size.
- **Fails on:** vocabulary questions (no shared word with the chunk), and common words matching unrelated chunks, since stopwords are kept.

### Concept graph
**Schema (fixed).** 8 entity types (ErrorCode, Service, Team, Person, Channel, Plan, Role, Feature) and 11 relations (raised_by, escalates_to, resolved_by, owned_by, provides, replaces, led_by, has_channel, covered_by, available_on, performed_by), each with allowed subject and object types. Fixed so the chains use the same edge kinds in every chunk. Role instead of a Policy type so q12's second hop has an edge in the right chunk. Values (IPs, durations) aren't entities.

**Extraction and validation.** One LLM call per chunk (38). Each triple is checked with Pydantic against the schema, including the allowed subject and object types. A bad triple goes to `rejected`, a chunk with an LLM error or non-JSON output is `failed`, no retry. `build --retry-failed` redoes failed chunks.

**Entity resolution.** Same type and same normalized name (lowercase, non-alphanumeric runs become one space, leading "the " removed). No alias table, so every merge is explainable and re-running is free.
- Right merge: `Feature:single sign on` merges `single sign-on` and `Single sign-on` (same for the SAML form).
- Missed merge: `audit log` exists as `Feature:audit log` and `Service:audit log`. It's the same thing under two types, and the type rule keeps them apart.

**Retrieval (no LLM at query time).** Entity linking by whole-word string match on the entities' surface forms (a form inside a longer matched form is ignored). Then 2 hops over the edges in both directions. Each followed edge adds 1.0 (hop 1) or 0.5 (hop 2) to its chunks, sorted by score. No seed, empty list. Not picked: LLM or embedding entity linking (a call per question), more hops (noise).

| Entities | Relations | Merges | LLM calls | Tokens | Build time |
|---|---|---|---|---|---|
| 63 | 65 edges | 2 | 37 | 25,189 prompt / 4,083 completion | 1,344 s |

Failed chunks: 1 (`support-runbook-errors.md#8`, rate limit, never recovered). It isn't needed for the two-hop questions: KST-5031, KST-2040 and KST-6010 all have edges from other chunks. Rejected triples: 0, so Pydantic never rejected anything on the real run. The first build had 16 failed chunks on the rate limit and 6 after the first retry, so most of the 1,344 s was waiting and retrying. The call count only includes calls that got an answer.

Extraction quality (10 triples, file: `evaluation/results/___`): correct / wrong / unsupported = ___ / ___ / ___. ___ (one sentence on a wrong or unsupported triple and what it cost, or "none in the 10 sampled").

**Where it fails.**
- 2 hops is a hard stop. In q08 the graph finds hop 1 (graph rank 4) but not the `| Messaging | ... |` row of the catalog (no graph rank): that row is 3 edges from KST-5031. It only reached the top 10 because dense and BM25 both had it at rank 11.
- Names that are also words. q08 asks "which team should support contact", so `Plan:Team` became a seed along with `scheduled reports`, and the graph followed 12 edges, mostly noise. q12 says "the admin console", so `Role:Admin` became a seed.
- q12's second hop (the 2026 refund policy) isn't reached by the graph. I think the runbook and the policy don't give the refund the same name, so the chain doesn't connect, but I didn't check.
- A seed needs an exact name, so a nickname or typo gives an empty list.

Optional features added: none.

### The graph's chunks after fusion
They reached the top k. 6 evidence items had a graph rank, and all of them were in the top 3 after fusion (67% at rank 1). But graph-only reach has n = 0: every evidence item the graph found was also in the dense or BM25 top 20. So on these questions the graph doesn't find new chunks, it reorders chunks that were already there, and a chunk all three retrievers agree on goes to rank 1 under plain RRF. That's what moves the two-hop hit@1 from 0.0 to 1.0. q11 is the clean example: the graph finds both hops (ranks 2 and 1) and they end up at fused ranks 1 and 2. I didn't change k or the candidates.

### A question where adding a retriever made things worse
Kestrel q05, "I lost my phone and I can't log in anymore. What can I do?". Dense alone has the right chunk at rank 1; with dense + bm25 it's at rank 9. BM25 doesn't find it at all (the chunk says "authenticator device" and "backup codes", the question says "phone" and "log in"). It returns other chunks, and RRF puts chunks that both lists half-agree on (about 1/62 + 1/62) above one that only dense ranks first (1/61). I think the BM25 matches come from common words, since I keep stopwords, but I didn't check. The graph doesn't fix it: with graph on, q05 is at rank 8. The same effect pushed q12's second hop out of the top 10 (dense rank 5) and Forest q06 from rank 4 to 8.

### Decision log (V3)
- **D32 BM25 index.** Options: in memory, a file, a database. Picked: a JSON file per chunk configuration in `data/bm25/`, built from Chroma's chunks. Why: it survives restarts and matches the dense chunks and ids.
- **D33 BM25 updates.** Options: incremental or full rebuild. Picked: full rebuild when the chunk-id hash changes. Why: simple, fast, never stale.
- **D34 Tokenization.** Options: Words tab tokenizer, a new one, stemming and stopwords. Picked: the Words tab's. Why: same words in both places, identifiers split into findable parts. Cost: the common-word matches in q05.
- **D35 Scoring.** Picked: k1 = 1.5, b = 0.75, Lucene IDF. Why: usual defaults, nothing tuned on the questions.
- **D36 Fusion.** Options: mixing scores, weighted RRF, plain RRF. Picked: plain RRF, k = 60, 20 candidates. Why: ranks compare across retrievers, scores don't.
- **D37 Switches.** Picked: `dense`, `bm25`, `graph`, any subset, one `DEFAULT_RETRIEVERS` in `app/hybrid.py`.
- **D38 Schema.** Options: open or fixed. Picked: fixed, 8 types, 11 relations. Why: the chains need the same edge kinds in every chunk.
- **D39 Extraction.** Picked: one call per chunk. Why: provenance is the chunk, cost is the number of chunks.
- **D40 Validation.** Picked: Pydantic per triple, invalid ones dropped and kept in `rejected`, bad chunks `failed`, no retry. Why: a bad triple never becomes an edge, but I still see it.
- **D41 Resolution.** Options: exact names, normalized names, alias table, embeddings. Picked: same type and normalized name. Why: explainable and free to re-run.
- **D42 Storage.** Picked: one JSON file per chunk configuration, with chunk ids on every node and edge and the build cost.
- **D43 Graph retrieval.** Options: LLM or embedding linking, string match, more hops. Picked: string match, 2 hops, 1.0 / 0.5 per edge. Why: no query-time LLM call, readable path.
- **D44 Settings.** Picked: built for the saved settings only. Why: its chunk ids only exist for them.
- **D45 Metrics.** recall@k = share of a question's evidence items in the first k chunks; graph reach is computed on the items the graph found.
- **D46 Usage counter.** A counter in `call_llm`, cost = difference of two copies, only answered calls.
- **D47 Sample.** 10 edges from `random.Random(42)`, graded by hand.