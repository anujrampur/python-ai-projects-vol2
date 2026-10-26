# Level 8 — AI Automation Foundations (Projects 86–90)

## Project 86 — Email Draft Builder
Creates a draft subject and body from a recipient, purpose, key points, and a selected tone. It does not send email. Run `python -m unittest level08.test_project86_email_draft_builder -v`.

## Project 87 — Smart File Organizer
Creates a dry-run plan that groups paths by extension. It never moves or deletes files. Review paths before implementing any filesystem action. Run `python -m unittest level08.test_project87_smart_file_organizer -v`.

## Project 88 — Workflow Engine
Runs a small sequence of allowlisted string operations (strip, uppercase, lowercase). Unknown actions are rejected. This demonstrates a workflow pattern without unsafe command execution. Run `python -m unittest level08.test_project88_workflow_engine -v`.

## Project 89 — Research Report Pipeline
Formats source notes supplied by the user into a structured research brief. It does not independently search or verify sources. Run `python -m unittest level08.test_project89_research_report_pipeline -v`.

## Project 90 — Productivity Planner
Orders tasks by priority and fits them into a given time budget. Ties are ordered alphabetically for reproducibility. Run `python -m unittest level08.test_project90_productivity_planner -v`.

**Shared limitation:** These are deterministic Python prototypes, not autonomous AI agents. A future LLM or external-service adapter must add privacy, authentication, rate limits, retries, logging, and explicit user confirmation where actions have side effects.
