# Volume 2 Project Index (working)

| Project | Level | Name | Status |
|---:|---|---|---|
| 51 | 1 | Joke / Shayari / Quote Generator | Initial implementation; tested |
| 52 | 1 | AI Dictionary & Word Explainer (ELI15) | Offline dictionary baseline; tested |
| 53 | 1 | Math Problem Solver | Restricted safe arithmetic parser; tested |
| 54 | 1 | Code Explainer | Static AST-based explainer; tested |
| 55 | 1 | Token & Cost Calculator | Heuristic token/cost estimate; tested |
| 56 | 2 | Paraphraser & Responsible Rewriter | Initial implementation; tests added |
| 57 | 2 | Keyword & Hashtag Extractor | Initial implementation; tests added |
| 58 | 2 | Text Classifier (spam/ham, topic) | Initial implementation; tests added |
| 59 | 2 | Meeting Minutes to Action Items | Initial implementation; tests added |
| 60 | 2 | Story & Poem Generator | Initial implementation; tests added |
| 61 | 3 | WhatsApp-style AI Bot core | Initial implementation; tests added |
| 62 | 3 | Discord AI Bot command core | Initial implementation; tests added |
| 63 | 3 | Role-Play Language Tutor | Initial implementation; tests added |
| 64 | 3 | Mental-Wellness Reflection Journal | Non-medical local reflection starter; tested |
| 65 | 3 | Chatbot with Custom Tone and Guardrails | Initial implementation; tests added |
| 66 | 4 | Excel/CSV Q&A Assistant | Offline deterministic baseline; tests added |
| 67 | 4 | Contract & Policy Document Explainer | Text/Markdown structural aid; not legal advice |
| 68 | 4 | Textbook Chapter to Notes + MCQs | Extractive heuristic baseline; tests added |
| 69 | 4 | Research Paper Summarizer | Section-based extractive baseline; tests added |
| 70 | 4 | Text Chunking & Embeddings Visualizer | Overlapping text chunker; embeddings not yet computed |
| 71 | 5 | Local Knowledge Base Search | Keyword search baseline; tests added |
| 72 | 5 | RAG Retrieval Ranking Sandbox | Keyword-overlap ranker; tests added |
| 73 | 5 | Citation-Aware Answer Draft | Extractive grounded draft; tests added |
| 74 | 5 | RAG Evaluation Dataset Builder | Dataset validation and Recall@k; tests added |
| 75 | 5 | Prompt Injection Pattern Checker | Limited phrase detector; not a security guarantee |
| 76 | 6 | Hybrid Retrieval Prototype | Lexical + caller-supplied vector scores; tests added |
| 77 | 6 | RAG Context Compressor | Query-token sentence selection; tests added |
| 78 | 6 | RAG Answer Auditor | Token-overlap source suggestions; heuristic only |
| 79 | 6 | Voice Transcript Cleaner | Cleans existing transcripts; no speech recognition |
| 80 | 6 | Voice Command Router | Allowlisted text intents; no shell execution |
| 81 | 7 | Image Captioning Workbench | Caption formatter; no vision inference |
| 82 | 7 | OCR Text Extraction | Optional Tesseract adapter; dependencies required |
| 83 | 7 | Visual Question Answering Workbench | Formats external model answers; no image inference |
| 84 | 7 | Document Image Analyzer | File metadata and SHA-256 only |
| 85 | 7 | Image Classification Workbench | Ranks external classifier scores; no model included |
| 86 | 8 | Email Draft Builder | Initial implementation; tests passed in local audit |
| 87 | 8 | Smart File Organizer | Initial implementation; tests passed in local audit |
| 88 | 8 | Workflow Automation Engine | Initial implementation; tests passed in local audit |
| 89 | 8 | Research Report Pipeline | Initial implementation; tests passed in local audit |
| 90 | 8 | Personal Productivity Planner | Initial implementation; tests passed in local audit |
| 91 | 9 | Tool Selection Agent | Educational deterministic prototype; tests passed |
| 92 | 9 | Task Planning Agent | Educational deterministic prototype; tests passed |
| 93 | 9 | Multi-Agent Collaboration | Role-labelled orchestration prototype; tests passed |
| 94 | 9 | Agent Memory Evaluation | In-memory memory/evaluation prototype; tests passed |
| 95 | 9 | Human Approval Gate | Approval-state prototype; tests passed |
| 96 | 10 | FastAPI AI Service | Demo response + validation; tests passed |
| 97 | 10 | Local AI Assistant with Ollama | Optional live Ollama adapter; fake-transport tests passed |
| 98 | 10 | AI SaaS Starter | In-memory auth/quota teaching prototype; tests passed |
| 99 | 10 | Personal AI Assistant | File/tool workflow prototype; tests passed |
| 100 | 10 | Capstone AI Agent | Deterministic approval-gated orchestration; tests passed |

Status is a development tracker, not a publication-readiness claim.

## Level 7 — Projects 81–85
- 81: Image captioning request preparation and model adapter boundary.
- 82: OCR text post-processing.
- 83: Visual question routing with injected model adapter.
- 84: Document-image metadata inspection.
- 85: Classification-score validation and ranking.
- Level 7 test discovery: 38 tests passed (includes pre-existing prototype/test files in level07). These are prototype tests, not a full integration or publication audit.
| 82 | 7 | OCR Text Postprocessor | Offline text cleanup; OCR engine not included |
| 83 | 7 | Visual Question Router | Adapter interface; no vision inference |
| 84 | 7 | Document Image Inspector | Image/document preparation; no OCR inference |
| 85 | 7 | Image Classification Workbench | Confidence-score ranking; no classifier inference |
| 86 | 8 | Email Draft Builder | Creates drafts only; does not send email |
| 87 | 8 | Smart File Organizer | Dry-run move plan; no filesystem changes |
| 88 | 8 | Workflow Automation Engine | Allowlisted text transformations only |
| 89 | 8 | Research Report Pipeline | Formats user-supplied notes; no independent web research |
| 90 | 8 | Personal Productivity Planner | Priority-based time-budget planner |
