# Python + AI Projects Volume 2 — Projects 96–100

These five educational prototypes demonstrate API validation, optional local Ollama
integration, a minimal SaaS quota/authentication core, safe personal-assistant file
and tool handling, and a human-approved capstone workflow.

## Requirements
- Python 3.10 or later (the projects use modern type annotations).
- Core projects use the Python standard library.
- Project 96's optional HTTP server requires `pip install fastapi uvicorn`.
- Project 97's live model path requires Ollama running locally and a model pulled,
  for example `ollama pull llama3.2`. Tests use a fake transport and do not require Ollama.

## Run tests
From this directory:
```bash
python -m unittest discover -v
```

## Important limitations
These are teaching examples, not production systems. Project 96 uses a deterministic
demo response rather than a real model. Project 98 uses in-memory accounts and quotas;
it is not a complete production authentication, billing, or multi-process quota system.
Project 100 does not call an LLM and requires approval by default. Review all code
before exposing services to the public internet.
