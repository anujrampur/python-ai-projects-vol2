"""Project 90: Priority-based daily task planner.

The planner uses a deterministic, greedy strategy: lower numeric priorities
are considered first (1 is highest), then titles alphabetically. It schedules
a task only when its full duration fits in the remaining time budget.
"""

from dataclasses import dataclass
from typing import Iterable


@dataclass(frozen=True)
class Task:
    """A task with a non-empty title, priority 1–3, and duration in minutes."""

    title: str
    priority: int = 3
    minutes: int = 30


def _validate_task(task: Task) -> None:
    if not isinstance(task, Task):
        raise ValueError("every item must be a Task")
    if not isinstance(task.title, str) or not task.title.strip():
        raise ValueError("task title must be a non-empty string")
    if isinstance(task.priority, bool) or not isinstance(task.priority, int) or task.priority not in (1, 2, 3):
        raise ValueError("priority must be an integer: 1, 2, or 3")
    if isinstance(task.minutes, bool) or not isinstance(task.minutes, int) or task.minutes <= 0:
        raise ValueError("task minutes must be a positive integer")


def plan_day(tasks: Iterable[Task], available_minutes: int) -> dict:
    """Return scheduled/deferred tasks and the used/remaining time budget.

    Args:
        tasks: Iterable of ``Task`` instances.
        available_minutes: Non-negative integer budget in minutes.

    Returns:
        A dictionary with ``scheduled``, ``deferred``, ``used_minutes``, and
        ``remaining_minutes`` keys. Task order is deterministic.

    Raises:
        ValueError: If the budget or any task is invalid.
    """
    if isinstance(available_minutes, bool) or not isinstance(available_minutes, int) or available_minutes < 0:
        raise ValueError("available_minutes must be a non-negative integer")
    if isinstance(tasks, (str, bytes)):
        raise ValueError("tasks must be an iterable of Task objects, not text")
    try:
        task_list = list(tasks)
    except TypeError as exc:
        raise ValueError("tasks must be an iterable of Task objects") from exc

    for task in task_list:
        _validate_task(task)

    ordered = sorted(task_list, key=lambda task: (task.priority, task.title.casefold()))
    scheduled = []
    deferred = []
    used_minutes = 0

    for task in ordered:
        if used_minutes + task.minutes <= available_minutes:
            scheduled.append(task)
            used_minutes += task.minutes
        else:
            deferred.append(task)

    return {
        "scheduled": scheduled,
        "deferred": deferred,
        "used_minutes": used_minutes,
        "remaining_minutes": available_minutes - used_minutes,
    }
