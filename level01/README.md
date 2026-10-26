# Level 1 — AI Ka Pehla Kadam (Projects 51–55)

These first five Volume 2 projects are deliberately designed to run offline with Python 3.10+ and the standard library. Where a project uses a local example library or heuristic rather than a real language model, that limitation is stated explicitly.

## Projects

| No. | File | Purpose | Run |
|---:|---|---|---|
| 51 | `project51_main.py` | Joke / Shayari / Quote Generator | `python project51_main.py` |
| 52 | `project52_dictionary.py` | Dictionary & Word Explainer | `python project52_dictionary.py` |
| 53 | `project53_math_solver.py` | Safe arithmetic solver | `python project53_math_solver.py` |
| 54 | `project54_code_explainer.py` | Static Python code explainer | `python project54_code_explainer.py` |
| 55 | `project55_token_cost_calculator.py` | Token and cost estimate | `python project55_token_cost_calculator.py` |

## Run all Level 1 tests

```bash
python -m unittest discover -s level01 -p 'test_*.py' -v
```

## Accuracy notes

- Project 51 uses a small built-in content collection, not an LLM.
- Project 52 contains a small offline dictionary; unknown words are reported rather than invented.
- Project 53 supports only arithmetic operators `+`, `-`, `*`, `/` and parentheses. It parses an AST and never calls `eval`.
- Project 54 parses Python syntax and describes selected constructs; it does not run pasted code and is not a full semantic AI explanation.
- Project 55 estimates tokens using roughly four characters per token. Exact tokenization depends on the model; prices must be entered from the provider's current pricing page.
