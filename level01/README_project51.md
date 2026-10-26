# Project 51 — Joke / Shayari / Quote Generator

**Volume 2: Python + AI — 100 Real-World AI & LLM Projects**

A beginner-friendly command-line app that generates jokes, shayari, and motivational quotes in English or Hindi. This first version works offline and needs no API key.

## Features
- Choose jokes, shayari, or quotes.
- Choose English or Hindi.
- Generate one item or a small batch.
- Uses a local content library, so results are repeatable and the app works without internet.
- Includes unit tests.

> **Important:** This is a rule-based/template-library starter, not an LLM-powered generator. A later upgrade can connect an optional AI API while keeping the same interface.

## Requirements
- Python 3.10 or newer
- No third-party packages required

## Run
From this directory:

```bash
python project51_main.py
```

For automated tests:

```bash
python -m unittest test_project51_generator -v
```

## Project structure
```text
level01/
├── project51_main.py
├── project51_generator.py
├── test_project51_generator.py
└── README_project51.md
```

## Sample interaction
```text
=== Joke / Shayari / Quote Generator ===
Choose language (en/hi): en
Choose type (joke/shayari/quote): quote
How many items (1-5): 1

1. Small steps taken consistently can lead to meaningful progress.
```

## Limitations and next steps
- The built-in library is intentionally small.
- Random selection may repeat an item across separate runs.
- Before publishing, review all Hindi/English wording and add attribution for any quoted material. The included lines are original short examples.
- Possible upgrades: Streamlit UI, user-submitted categories, save-to-file, and an optional LLM backend.
