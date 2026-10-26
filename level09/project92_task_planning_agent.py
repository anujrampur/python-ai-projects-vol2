"""Project 92: Turn a goal into a small, explicit task checklist.

This deterministic starter creates a generic plan. It does not execute tasks,
call an LLM, or decide whether a plan is optimal for a particular goal.
"""

from dataclasses import dataclass


@dataclass(frozen=True)
class Task:
    """One numbered planning step."""

    step: int
    title: str
    description: str


def plan_task(goal: str) -> list[Task]:
    """Return a five-step checklist for a non-empty text goal.

    Leading, trailing, and repeated whitespace are normalized. Non-string
    inputs are rejected explicitly rather than failing with an incidental
    attribute error.
    """
    if not isinstance(goal, str):
        raise TypeError("goal must be a string")

    cleaned = " ".join(goal.split())
    if not cleaned:
        raise ValueError("goal must not be empty")

    return [
        Task(1, "Clarify the goal", f"Write a measurable outcome for: {cleaned}"),
        Task(2, "Gather inputs", "List required files, facts, tools, and constraints."),
        Task(3, "Break down the work", "Create small steps with clear completion criteria."),
        Task(
            4,
            "Execute safely",
            "Perform one step at a time; ask for approval before consequential actions.",
        ),
        Task(
            5,
            "Verify the result",
            "Check the result against the original goal and record unresolved issues.",
        ),
    ]
