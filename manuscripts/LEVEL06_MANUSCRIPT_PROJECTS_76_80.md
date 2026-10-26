# Level 6 â€” Advanced RAG and Voice AI (Projects 76â€“80)

> **Editorial note:** Keep the implementation and demonstrations in the source archive as the authority. These chapters describe educational project patterns and must be checked against the corresponding source files before publication. Any model-backed or speech-backed feature requires its optional dependency/service to be installed and tested.

## Project 76 â€” RAG Retrieval Evaluation

### Learning objective
Measure whether a retrieval component returns useful passages for a small set of questions before connecting it to a language model.

### Core idea
A RAG system has at least two separate quality questions: did retrieval find relevant evidence, and did the answer generator use that evidence correctly? This project focuses on retrieval metrics. Define a small set of queries and their known relevant document IDs, run the retriever, and compare the returned IDs with the expected set.

### Suggested workflow
1. Create a tiny, hand-reviewed query-to-relevant-document dataset.
2. Run the project's retrieval method for each query.
3. Compute precision at *k*, recall at *k*, and reciprocal rank where applicable.
4. Inspect failures manually; a metric cannot tell you whether a document is genuinely relevant if the labels are poor.
5. Record a baseline before changing chunk size, overlap, or ranking strategy.

### Example
If the relevant document is `doc-3` and the top three results are `doc-3`, `doc-1`, and `doc-7`, precision@3 is 1/3 and recall@3 is 1/1 for this single relevant document. Reciprocal rank is 1 because the first result is relevant.

### Validation checklist
- Empty result sets do not crash evaluation.
- Missing relevance labels are reported or excluded deliberately.
- Metric definitions and denominator behavior are documented.
- Evaluation data contains no private or sensitive content.

## Project 77 â€” RAG Chunking Strategy Comparison

### Learning objective
Understand how document chunk size and overlap affect retrieval quality and context boundaries.

### Core idea
Chunking is a trade-off. Very small chunks may lose context; very large chunks can add irrelevant material and consume context budget. Overlap can preserve boundary information but creates duplicate text and storage overhead.

### Suggested workflow
1. Use the same small source corpus for every strategy.
2. Compare sentence-based, fixed-character, and/or token-aware chunking if implemented.
3. Track chunk count, average chunk length, retrieval hit rate, and duplicated content.
4. Inspect chunks around headings, tables, code blocks, and paragraph boundaries.
5. Choose a strategy using measured task performance rather than a universal rule.

### Example
A question about a definition split across two paragraphs may fail with non-overlapping chunks. A modest overlap can preserve the definition, but too much overlap may cause several top results to contain nearly identical text.

### Validation checklist
- No input text is silently dropped.
- Empty documents and whitespace-only input are handled.
- Chunk size and overlap constraints are validated.
- Tests cover short documents and documents shorter than one chunk.

## Project 78 â€” Hybrid Search for RAG

### Learning objective
Combine lexical matching with semantic retrieval to improve coverage across exact terms and paraphrased questions.

### Core idea
Keyword search can be strong for IDs, product names, error messages, and exact phrases. Embedding search can find semantically related passages even when wording differs. Hybrid search combines the two ranked lists, often with reciprocal-rank fusion or a normalized weighted score.

### Suggested workflow
1. Build a tiny corpus with both exact-keyword and paraphrase queries.
2. Run lexical and semantic retrieval separately.
3. Fuse rankings using a documented method.
4. Compare top-k relevance against each baseline.
5. Review disagreements and avoid assuming that a higher score automatically means better evidence.

### Example
For a query containing an exact exception name, lexical retrieval may rank the precise troubleshooting note first. For a paraphrase of that note, semantic retrieval may perform better. A fusion method can retain both candidates.

### Validation checklist
- Fusion behavior is deterministic for ties.
- Missing candidates from either ranker are handled.
- The code does not leak credentials in logs.
- If embeddings require a model, tests use a stub or fixture and document the live dependency.

## Project 79 â€” Voice Input for a RAG Assistant

### Learning objective
Connect speech input to a question-answering workflow while keeping transcription and answer generation as separate stages.

### Core idea
A voice RAG pipeline typically performs audio capture, speech-to-text, retrieval, answer generation, and optional text-to-speech. Each stage can fail independently. Displaying the recognized transcript before retrieval helps users correct recognition errors.

### Suggested workflow
1. Capture a short audio sample using a supported microphone or fixture.
2. Transcribe it using the project's selected speech engine.
3. Let the user review or edit the transcript.
4. Pass the final text to retrieval and preserve source references.
5. If spoken output is enabled, show the text answer as well.

### Privacy and safety
Do not record in the background without clear user consent. Explain whether audio is processed locally or sent to an external service. Avoid retaining recordings unless needed and explicitly disclosed.

### Validation checklist
- Missing microphone or unavailable speech service produces a useful message.
- Empty or low-confidence transcription is handled.
- Audio upload size and duration are bounded where relevant.
- Tests do not require a physical microphone.

## Project 80 â€” End-to-End Voice RAG Assistant

### Learning objective
Orchestrate retrieval, evidence-grounded answering, and optional speech input/output into a single workflow.

### Core idea
The application should preserve boundaries between transcript, retrieved evidence, generated answer, and spoken output. The answer should identify the evidence it used and say when the corpus does not contain enough information. Voice output is a presentation layer, not a substitute for visible citations.

### Suggested workflow
1. Accept typed text or an approved voice transcript.
2. Retrieve the most relevant passages.
3. Construct a prompt with explicit evidence boundaries.
4. Generate an answer only from the supplied evidence, or return an uncertainty message.
5. Display the answer and source passages; optionally read the answer aloud.
6. Log operational metadata without unnecessarily storing raw audio or sensitive prompts.

### Example interaction
**Question:** â€œWhat is the school's admission process?â€
**Retrieval:** The system finds the admission-policy document and current checklist.
**Answer:** It summarizes the steps and links the answer to those passages. If the corpus has no admission-policy evidence, it should say it cannot confirm the process.

### Validation checklist
- End-to-end flow can be tested with stubbed speech and model services.
- Empty retrieval results do not lead to fabricated citations.
- Errors at one stage do not expose API keys or local file contents.
- Documentation identifies which features run locally and which use external services.

## Level 6 review questions
1. Why should retrieval quality be measured separately from answer quality?
2. What can go wrong when chunk overlap is too large?
3. When might lexical search outperform semantic search?
4. Why should users review a speech transcript before querying a knowledge base?
5. What should the assistant do when no retrieved passage supports an answer?

## Level 6 publication checklist
- Verify each chapter against its numbered source module and README.
- Run unit tests and any optional integration tests in a documented environment.
- Replace generic examples with outputs captured from the actual implementation.
- Mark any feature not implemented in code as a planned extension, not a completed capability.
