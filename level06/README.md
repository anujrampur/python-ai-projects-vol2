# Level 6 — Advanced RAG & Voice AI (Projects 76–80)

All projects are offline Python prototypes and use the standard library only.

- **76 Hybrid Retrieval:** combines keyword overlap and externally supplied vector scores; it does not generate embeddings.
- **77 Context Compressor:** ranks source sentences using query-token overlap; it is not semantic compression.
- **78 Answer Auditor:** flags sentences with no lexical overlap with supplied sources; it cannot prove factual entailment.
- **79 Transcript Cleaner:** cleans existing transcript text; it does not record audio or run speech recognition.
- **80 Voice Command Router:** recognizes an explicit allowlist and never executes arbitrary shell commands.

Run tests from this directory with `python -m unittest discover -v`.
