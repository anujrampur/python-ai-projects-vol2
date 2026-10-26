# Python + AI: 100 Real-World AI & LLM Projects — Volume 2
## Working manuscript — Projects 51–55

> Editorial status: working draft, not final publication files. Page design, final pagination, front matter, index, and full-book proofreading will be completed after all 50 project chapters are stable.

# Project 51 — Joke / Shayari / Quote Generator

## Learning objectives
- Build a menu-driven Python command-line program.
- Separate application logic from user interaction.
- Validate user choices and use a local content library.
- Write repeatable unit tests.

## What it does
The program lets a user select English or Hindi, choose jokes, shayari, or quotes, and request between one and five results. This release is an offline starter using a small built-in collection; it is not presented as an LLM-backed generator.

## Run it
From the project repository root, run `python level01/project51_main.py`. Run tests with `python -m unittest discover -s level01 -p 'test_*.py' -v`.

## Design notes
The content-selection function lives in `project51_generator.py`; the CLI lives in `project51_main.py`. Keeping these separate makes the logic easier to test and later replace with an optional language-model adapter.

## Limitations
The content library is small and selection may repeat items. Review all wording before publication. A future API-based version must document the provider, credentials, pricing, privacy implications, and error handling.

# Project 52 — AI Dictionary & Word Explainer (ELI15)

## Learning objectives
- Model structured dictionary entries with a dataclass.
- Normalize input and handle unknown words clearly.
- Explain a word using a simple-language summary and an example.

## What it does
This offline starter includes a small curated English-word collection with definitions, example sentences, and Hindi meanings. Unknown words are reported instead of being guessed. Despite the project title, this first version is dictionary-backed rather than LLM-powered.

## Run it
Run `python level01/project52_dictionary.py`. Tests: `python -m unittest discover -s level01 -p 'test_*.py' -v`.

## Limitations
The included vocabulary is intentionally limited. An LLM integration can be added later behind the same function interface, with a clear distinction between dictionary facts and generated explanations.

# Project 53 — Math Problem Solver (Step-by-Step)

## Learning objectives
- Parse a restricted arithmetic expression.
- Respect operator precedence and parentheses.
- Reject unsupported syntax and division by zero.

## What it does
The starter supports numeric expressions with `+`, `-`, `*`, `/`, unary signs, and parentheses. It parses Python's abstract syntax tree and evaluates only explicitly allowed node types. It never uses `eval` and does not execute arbitrary Python code.

## Run it
Run `python level01/project53_math_solver.py`. Tests: `python -m unittest discover -s level01 -p 'test_*.py' -v`.

## Accuracy note
The current explanation states the arithmetic order and gives the result; it does not yet show every intermediate operation. The chapter and feature name must be updated if full intermediate-step tracing is not implemented before release.

# Project 54 — Code Explainer

## Learning objectives
- Parse Python source without executing it.
- Recognize selected constructs such as functions, classes, loops, conditions, calls, and assignments.
- Report syntax errors clearly.

## What it does
The starter uses Python's AST parser to produce beginner-friendly notes for selected syntax. It does not run submitted code, and it is not a full semantic or LLM-based explanation engine.

## Run it
Run `python level01/project54_code_explainer.py`, paste a snippet, and enter `END` on a line by itself. Tests: `python -m unittest discover -s level01 -p 'test_*.py' -v`.

## Safety and limitations
Because the submitted source is parsed but not executed, it avoids running arbitrary pasted code. The explanation coverage is intentionally basic; complex control flow and program meaning may not be captured.

# Project 55 — Token & Cost Calculator

## Learning objectives
- Estimate token counts from text length.
- Calculate input and output costs from user-provided rates.
- Validate non-negative counts and prices.

## What it does
The starter estimates tokens using approximately four characters per token and calculates estimated cost using rates supplied by the user per one million tokens.

## Run it
Run `python level01/project55_token_cost_calculator.py`. Tests: `python -m unittest discover -s level01 -p 'test_*.py' -v`.

## Important limitation
The four-characters-per-token method is only a rough heuristic, not a provider tokenizer. Actual token counts depend on the model and text. Prices change, so users must consult the provider's current pricing page. Never describe this estimate as an exact bill.


# Project 56 — Paraphraser & Responsible Rewriter

## Learning objectives
- Use regular expressions for conservative phrase simplification.
- Validate text input and length.
- Understand why rewriting is not plagiarism detection.

## What it does
This offline starter simplifies a small set of common English phrases. It is a transparent rules-based tool, not an AI model and not a plagiarism checker.

## Run it
Run `python level02/project56_paraphraser.py`. Tests: `python -m unittest discover -s level02 -p 'test_*.py' -v`.

## Responsible use
Review every rewrite for meaning and tone. Cite sources when ideas or facts come from others. The software cannot certify originality or guarantee that content is plagiarism-safe.

# Project 57 — Keyword & Hashtag Extractor

## Learning objectives
- Tokenize text and count word frequency.
- Filter common stopwords and produce hashtags.
- Return deterministic rankings for repeatable tests.

## What it does
The program extracts frequent English words and converts them into hashtag candidates. Ties are resolved by first appearance.

## Run it
Run `python level02/project57_keyword_hashtag_extractor.py`.

## Limitations
This is frequency-based, not semantic keyword extraction. It does not currently support robust Hindi tokenization, stemming, or phrase ranking. Review hashtags before publishing.

# Project 58 — Text Classifier (Spam/Ham and Topic)

## Learning objectives
- Build an explainable keyword baseline.
- Expose matched evidence and per-topic scores.
- Understand false positives and false negatives.

## What it does
The classifier labels a message as `spam` when it finds a configured spam term; otherwise it returns `ham/uncertain`. It also assigns a broad topic based on matching vocabulary.

## Run it
Run `python level02/project58_text_classifier.py`.

## Limitations and safety
This is not a trained classifier and has not been evaluated on a representative dataset. Do not use it as the sole basis for blocking messages, moderation, hiring, finance, or other consequential decisions.

# Project 59 — Meeting Minutes to Action Items

## Learning objectives
- Split notes into candidate sentences.
- Detect common action language.
- Capture simple owner and due-date patterns.

## What it does
The program extracts sentences containing configured action phrases and optionally detects `Name: task` ownership and a small set of due-date formats.

## Run it
Run `python level02/project59_meeting_action_items.py`; paste notes and enter `END` to finish.

## Limitations
Natural-language ownership and deadlines are difficult to infer reliably. Review all extracted tasks manually; missing a task or assigning it incorrectly is possible.

# Project 60 — Story & Poem Generator

## Learning objectives
- Use templates and user inputs to generate short creative text.
- Validate themes and required fields.
- Make random selection reproducible in tests.

## What it does
The offline program fills story templates with a hero, place, and object, or selects a short poem from a small built-in collection.

## Run it
Run `python level02/project60_story_poem_generator.py`. Choose `story` or `poem` when prompted.

## Limitations
This is template-based generation, not LLM generation. Variety is limited, and the user should review output before publication.


# Project 61 — WhatsApp-Style Bot Core

This chapter builds a provider-neutral message-response function with greeting, help, hours, and contact examples. It does not connect to WhatsApp or send messages. Real deployment requires an approved messaging provider, verified webhooks, secret management, consent, and privacy controls.

Run `python level03/project61_whatsapp_style_bot.py`.

# Project 62 — Discord AI Bot Command Core

The command handler demonstrates `!help`, `!about`, and `!ping` without connecting to Discord. A real bot needs a Discord application, permissions configured with least privilege, secure token storage, and an external library integration.

Run `python level03/project62_discord_bot_core.py`.

# Project 63 — Role-Play Language Tutor

The tutor presents cafe, interview, and travel scenarios, then gives lightweight vocabulary hints. It does not grade grammar or provide a formal proficiency score.

Run `python level03/project63_roleplay_language_tutor.py`.

# Project 64 — Reflection Journal Companion

This non-medical project models a reflection entry and offers a journaling prompt. Entries are not persisted automatically. It is not therapy, diagnosis, or crisis support; users should not treat it as medical advice.

Run `python level03/project64_reflection_journal.py`.

# Project 65 — Custom Tone and Guardrails

This project adds a tone prefix and demonstrates a small blocked-phrase check. It is not a comprehensive safety system and does not generate new factual content. Review output before using it in a real application.

Run `python level03/project65_tone_guardrails.py`.


# Level 4 — Documents and RAG Basics (Projects 66–70)

## Project 66 — Excel/CSV Q&A Assistant
**Goal.** Ask basic, explicitly supported questions about a CSV file without sending data to an external service.

**Implementation note.** The code answers row-count, column-name, and numeric-average questions. It is deterministic data processing, not natural-language reasoning by an LLM.

**Run.** Import `load_csv` and `answer_question` from `level04/project66_csv_qa_assistant.py`. Example: `answer_question([{'score':'10'}, {'score':'20'}], 'average score')` returns an average of 15.00.

**Limitations.** Questions must match the supported patterns; numeric values that cannot be parsed are skipped.

## Project 67 — Contract & Policy Document Explainer
**Goal.** Create a first-pass structural overview of a plain-text or Markdown policy.

**Implementation note.** The module counts lines and words and flags lines containing obligation-related terms. This is not legal advice and does not determine enforceability or interpret legal rights. PDF/DOCX parsing is outside this starter.

**Run.** Call `read_document(path)` and pass the result to `explain_document(text)`.

## Project 68 — Textbook Chapter to Notes + MCQs
**Goal.** Create a quick revision outline from pasted chapter text.

**Implementation note.** Notes are selected by sentence length; review prompts are simple phrase-recognition questions, not validated exam-quality MCQs. No LLM is used.

**Run.** Call `make_notes(chapter_text)` and `make_mcqs(chapter_text)`. Always compare generated notes with the original chapter.

## Project 69 — Research Paper Summarizer
**Goal.** Extract a compact overview from supplied paper text.

**Implementation note.** When recognizable headings exist, the program extracts content under Abstract, Methods, Results, and Conclusion/Discussion. Otherwise it uses sentence-position fallbacks. It does not assess research quality or verify scientific claims.

**Run.** Call `summarize_paper(paper_text)` and inspect each returned field against the source.

## Project 70 — Text Chunking & Embeddings Visualizer
**Goal.** Prepare long text for retrieval pipelines by splitting it into overlapping chunks.

**Implementation note.** This version reports character ranges and chunk lengths. It does not calculate vector embeddings; a future edition can add a separately documented embedding backend.

**Run.** Call `chunk_text(text, chunk_size=500, overlap=50)` and pass the result to `describe_chunks`. Overlap must be smaller than chunk size.

## Level 4 review checklist
- [ ] Run `python -m unittest discover -s level04 -p 'test_*.py' -v`.
- [ ] Confirm the examples against actual output.
- [ ] Keep the non-LLM limitations visible in the book.
- [ ] Add model integrations only with setup, privacy, cost, and error-handling documentation.
