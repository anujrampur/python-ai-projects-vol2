# Projects 91–95 — AI Agents and Human Oversight

These are educational, deterministic prototypes using only the Python standard library. They do not call an LLM or autonomously perform external actions.

- **91 Tool Selection:** choose among a fixed allowlist using keyword matching.
- **92 Task Planning:** create a generic five-step checklist for a goal.
- **93 Multi-Agent Collaboration:** combine role-labelled text contributions; no agents are actually invoked.
- **94 Memory & Evaluation:** store small local key/value records and compare expected vs actual output.
- **95 Human Approval Gate:** represent approval state; downstream code must enforce it before any real action.

Run all tests:
```bash
python -m unittest discover -v
```

Use synthetic/demo data only. The memory store is in-memory unless explicitly exported and has no encryption or access controls. Do not put secrets or sensitive personal information in it.
