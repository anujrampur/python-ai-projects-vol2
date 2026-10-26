# Level 9 — AI Agents and Human Oversight (Projects 91–95)

## Project 91 — AI Agent with Tool Selection
A deterministic allowlist-based tool selector. It demonstrates intent routing, not LLM reasoning. Run `python -m unittest test_project91_tool_selection_agent.py -v`.

## Project 92 — Task Planning Agent
Converts a goal into a generic five-step checklist. A real agent should refine these steps and ask for clarification when needed. Run `python -m unittest test_project92_task_planning_agent.py -v`.

## Project 93 — Multi-Agent Collaboration
Combines role-labelled contributions in order. The roles are supplied by the caller; this demo does not invoke independent models. Run `python -m unittest test_project93_multi_agent_collaboration.py -v`.

## Project 94 — Agent Memory and Evaluation
Provides a small in-memory key/value store, JSON export, and exact normalized-output evaluation. Do not store secrets; this is not a secure database. Run `python -m unittest test_project94_agent_memory_evaluation.py -v`.

## Project 95 — Human-in-the-Loop Approval Gate
Represents whether a proposed action has explicit approval. Any real integration must enforce this gate at the execution boundary. Run `python -m unittest test_project95_human_approval_gate.py -v`.
