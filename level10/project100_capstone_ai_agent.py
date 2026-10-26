"""Project 100: Capstone AI Agent — deterministic orchestration demonstration.

This capstone combines planning, allowlisted tools, memory and approval. It is
not an autonomous LLM; model integration can be added behind the planner later.
"""
from dataclasses import dataclass
from typing import Callable

@dataclass(frozen=True)
class Action:
    tool: str
    argument: str
    requires_approval: bool = True

@dataclass(frozen=True)
class RunReport:
    status: str
    steps: tuple[str, ...]

class CapstoneAgent:
    def __init__(self, tools: dict[str, Callable[[str], str]], require_approval: bool = True):
        self.tools = dict(tools)
        self.require_approval = require_approval
        self.memory: list[str] = []

    def remember(self, text: str) -> None:
        if not isinstance(text, str) or not text.strip():
            raise ValueError("Memory text cannot be empty.")
        self.memory.append(text.strip())

    def execute(self, actions: list[Action], approved: bool = False) -> RunReport:
        if not isinstance(actions, list):
            raise TypeError("actions must be a list.")
        steps = []
        for action in actions:
            if action.tool not in self.tools:
                return RunReport("blocked", tuple(steps + [f"Unknown tool: {action.tool}"]))
            if self.require_approval and action.requires_approval and not approved:
                return RunReport("approval_required", tuple(steps + [f"Approval required: {action.tool}"]))
            result = self.tools[action.tool](action.argument)
            if not isinstance(result, str):
                return RunReport("error", tuple(steps + [f"Tool {action.tool} returned a non-string result."]))
            steps.append(f"{action.tool}: {result}")
        return RunReport("completed", tuple(steps))
