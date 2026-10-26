# Level 10 — Deployment, Personal Assistants and Capstone (Projects 96–100)

## Project 96 — FastAPI AI Service
**Goal:** Build a small API boundary with input validation and a health endpoint.
The generation core deliberately returns a clearly labeled demo response, so API
behavior can be tested without credentials or model downloads.

**Run:** `python project96_fastapi_ai_service.py` after installing `fastapi` and `uvicorn`.
**Test:** `python -m unittest test_project96_fastapi_ai_service.py`

## Project 97 — Local AI Assistant with Ollama
**Goal:** Send a prompt to a local Ollama `/api/generate` endpoint.
The transport injection allows deterministic tests; live calls happen only when
`chat()` is invoked without a fake transport.

**Run:** Start Ollama, pull a model, then call `chat("Explain recursion")` from Python.
**Test:** `python -m unittest test_project97_local_ollama_assistant.py`

## Project 98 — AI SaaS Starter
**Goal:** Explore password hashing, registration, authentication and usage quotas.
The account store is in memory and resets when the process ends. Do not treat this
as production authentication or billing.

**Test:** `python -m unittest test_project98_ai_saas_starter.py`

## Project 99 — Personal AI Assistant
**Goal:** Combine notes, text-file reading constrained to an allowed directory, and
explicitly allowlisted tools. The path check prevents reading files outside the root.

**Test:** `python -m unittest test_project99_personal_ai_assistant.py`

## Project 100 — Capstone AI Agent
**Goal:** Orchestrate allowlisted actions with approval gates and simple memory.
The capstone is deterministic; it demonstrates control flow, not autonomous reasoning.

**Test:** `python -m unittest test_project100_capstone_ai_agent.py`

## Level 10 review checklist
- [ ] Run the unit tests on the target Python version.
- [ ] Install optional dependencies and test the HTTP/local-model integrations separately.
- [ ] Add persistent storage, real authentication/session management, rate limiting,
      audit logging and deployment configuration before production use.
- [ ] Confirm book examples match the exact source-code behavior.
