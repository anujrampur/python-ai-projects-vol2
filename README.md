# Python + AI: 100 Real-World AI & LLM Projects — Volume 2

## Working repository — Projects 51–100

The final release will contain all 50 projects in one consolidated ZIP, plus tests, setup instructions, dependency notes, and a complete project index. Interim milestones are not the final deliverable.

- `level01/`: Projects 51–55 — AI first steps.
- `level02/`: Projects 56–60 — Smart text tools.
- `level03/`: Projects 61–65 — Chatbot cores, language practice, and guardrails.
- `level04/`: Projects 66–70 — Documents and RAG basics (offline baselines).
- `level05/`: Projects 71–75 — Advanced RAG foundations (keyword-based prototypes).
- `level06/`: Projects 76–80 — Advanced RAG and voice foundations.
- `level07/`: Projects 81–85 — Vision AI workbenches and adapters.
- `level08/`: Projects 86–90 — Safe automation foundations.
- `book_manuscript/`: working manuscript chapters; not yet publication-ready.

## Environment

Python 3.10 or newer recommended. Levels 1 and 2 currently use only the Python standard library.

## Run all current tests

```bash
python -m unittest discover -s level01 -p 'test_*.py' -v
python -m unittest discover -s level02 -p 'test_*.py' -v
python -m unittest discover -s level03 -p 'test_*.py' -v
python -m unittest discover -s level04 -p 'test_*.py' -v
python -m unittest discover -s level05 -p 'test_*.py' -v
python -m unittest discover -s level06 -p 'test_*.py' -v
python -m unittest discover -s level07 -p 'test_*.py' -v
python -m unittest discover -s level08 -p 'test_*.py' -v
```

## Quality rule

A project is not marked publication-ready until documented behavior matches code and available tests have been run. Heuristics and templates must not be marketed as real LLM output. External API projects must document credentials, pricing, privacy, and error handling.

## Current development status
Level 7 (Projects 81–85) prototype code, README, and manuscript draft have been added. Tests discovered in `level07` currently pass (38 tests, including pre-existing prototype files). Vision-model inference is not bundled in these standard-library prototypes; adapters are explicitly required where applicable.

Level 8 (Projects 86–90) now has an initial implementation and manuscript chapter. These deterministic prototypes do not send email, alter files, browse the web, or claim autonomous AI behavior.

## Latest audit

See `README_RUNTIME_SAMPLE_OUTPUT_AUDIT_2026-10-20.md` for README coverage, syntax checks, bounded per-level test discovery, and sample-output readiness limitations.


## Sample-output audit

See `CONTROLLED_SAMPLE_OUTPUT_READINESS_AUDIT_2026-10-20.md` for the source-level output-readiness inventory and validation limitations.


## Source import/execution readiness

See `SOURCE_IMPORT_EXECUTION_READINESS_AUDIT_2026-10-20.md` and `source_import_execution_inventory.csv`. This is a static inventory, not an end-to-end test report.

## Latest regression test run (2026-10-20)

See `REGRESSION_TEST_RUN_2026-10-20.md` for per-level unittest discovery results and scope limitations.

## Controlled sample outputs (2026-10-20)

See `CONTROLLED_SAMPLE_OUTPUTS_PROJECTS_66_80_2026-10-20.md` for locally executed sample outputs for Projects 66–80. These are offline deterministic/heuristic examples, not live-model outputs.

## Controlled sample outputs (Projects 81–100, 2026-10-20)

See `CONTROLLED_SAMPLE_OUTPUTS_PROJECTS_81_100_2026-10-20.md` for bounded local examples. Optional/live integrations are explicitly distinguished from demo behavior.


## Latest controlled sample recheck
See `CONTROLLED_SAMPLE_OUTPUTS_PROJECTS_81_100_RECHECK_2026-10-20.md` for corrected-input rechecks of Projects 82, 83, 88, and 100. This is not a full publication-readiness certification.

## Optional integrations and dependencies

The core examples are intended to run offline where stated. Install optional dependencies only for the integration you plan to exercise. Run commands from the repository root.

### OCR — Project 82

The OCR adapter requires the Python packages `Pillow` and `pytesseract`, plus the separate Tesseract OCR executable installed for your operating system. Installing the Python wrapper alone does not install the OCR engine.

```bash
python -m pip install Pillow pytesseract
```

Install Tesseract separately using its official distribution for your OS, then confirm the executable is on `PATH` or configure its location as appropriate for your environment. The adapter defaults to English (`eng`); the corresponding language data must be installed in Tesseract. OCR quality depends on image quality, language data, layout, and engine configuration. The text post-processor is a separate step and does not itself perform OCR.

### HTTP API — Project 96

The validation and demo-response core can be tested without a web server. To create the optional HTTP app, install FastAPI and Uvicorn:

```bash
python -m pip install fastapi uvicorn
python -m level10.project96_fastapi_ai_service
```

The current `/generate` endpoint returns a deterministic demo response; it does not call a real language model. The sample server binds to `127.0.0.1:8000`. This educational server is not production-hardened. Before exposing it to a network, add authentication, rate limiting, logging policy, request-size controls, secret management, deployment configuration, and a privacy/security review.

### Local model endpoint — Project 97

Project 97 uses Python's standard library to call the local Ollama HTTP endpoint. Install Ollama separately, start its service, and pull a model before making a live request. For example, after installing Ollama:

```bash
ollama pull llama3.2
```

The default endpoint is `http://127.0.0.1:11434`. A model name in code does not mean the model is installed. The project tests use an injected fake transport and do not prove that a live Ollama service or model is available. Keep prompts and returned content local only if your Ollama configuration and surrounding tools actually preserve that boundary.

### General dependency guidance

- Use a virtual environment for project-specific packages.
- Do not install every optional package unless required by the example you are running.
- Keep API keys, bot tokens, and credentials out of source control.
- Check package and service documentation for platform-specific setup and supported versions.
- These notes document the current prototypes; they are not a locked, reproducible dependency specification.

## Repository and Project Index

- **GitHub repository:** https://github.com/anujrampur/python-ai-projects-vol2
- **Complete project index:** [PROJECT_INDEX.md](PROJECT_INDEX.md)
- **Source code:** Projects 51–100, organized into `level01/` through `level10/`.
- **License:** MIT (see [LICENSE](LICENSE)).

This repository contains educational prototypes. Check each project's README, dependencies, limitations, and tests before using it in a real application.
