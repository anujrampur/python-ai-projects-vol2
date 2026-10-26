# Level 2 — Smart Text Tools (Projects 56–60)

All projects are offline, standard-library teaching baselines. They are transparent heuristics/templates, not LLM-backed services.

| No. | File | Purpose | Run |
|---:|---|---|---|
| 56 | `project56_paraphraser.py` | Phrase simplification / paraphraser starter | `python level02/project56_paraphraser.py` |
| 57 | `project57_keyword_hashtag_extractor.py` | Frequency-based keyword and hashtag extraction | `python level02/project57_keyword_hashtag_extractor.py` |
| 58 | `project58_text_classifier.py` | Rule-based spam and topic classification | `python level02/project58_text_classifier.py` |
| 59 | `project59_meeting_action_items.py` | Heuristic action-item extraction from notes | `python level02/project59_meeting_action_items.py` |
| 60 | `project60_story_poem_generator.py` | Template-based story and poem generation | `python level02/project60_story_poem_generator.py` |

Run Level 2 tests from repository root:

```bash
python -m unittest discover -s level02 -p 'test_*.py' -v
```

## Important limitations
- Project 56 does not detect plagiarism and cannot guarantee that text is plagiarism-safe. Cite sources and review rewrites.
- Project 57 uses English tokenization and a small stopword list; it is not a semantic keyword model.
- Project 58 is a keyword heuristic and can make mistakes; do not use it for consequential moderation.
- Project 59 may miss or misread action items; humans should review owners and deadlines.
- Project 60 uses a small template collection, not an LLM.
