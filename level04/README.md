# Level 4 — Documents and RAG Basics (Projects 66–70)

These projects are intentionally transparent offline baselines. They do not claim to be LLM-powered. Each module can later be extended with a model adapter.

| Project | Module | Purpose |
|---:|---|---|
| 66 | `project66_csv_qa_assistant.py` | Basic CSV row/column/average questions |
| 67 | `project67_document_explainer.py` | Text/Markdown document structure and possible obligation lines; not legal advice |
| 68 | `project68_chapter_to_notes_mcqs.py` | Heuristic extractive notes and simple review prompts |
| 69 | `project69_research_paper_summarizer.py` | Extractive section-based paper overview |
| 70 | `project70_chunking_embeddings_visualizer.py` | Character chunking with overlap; no embeddings computed yet |

## Run tests
From the repository root:

```bash
python -m unittest discover -s level04 -p 'test_*.py' -v
```

Python 3.10+; standard library only.
