"""Project 95: Require an explicit human approval decision.

This module records an approval decision; it does not execute the action.
"""
from dataclasses import dataclass


@dataclass(frozen=True)
class ApprovalDecision:
    """Immutable decision returned by the approval gate."""

    approved: bool
    status: str
    action: str


def gate_action(action: str, approved: bool = False) -> ApprovalDecision:
    """Validate an action label and record whether it was approved.

    Raises:
        TypeError: If action is not a string or approved is not a bool.
        ValueError: If action is blank after trimming whitespace.
    """
    if not isinstance(action, str):
        raise TypeError("action must be a string")
    if not isinstance(approved, bool):
        raise TypeError("approved must be a bool")

    cleaned = action.strip()
    if not cleaned:
        raise ValueError("action must not be empty")

    status = "approved_for_execution" if approved else "awaiting_human_approval"
    return ApprovalDecision(approved=approved, status=status, action=cleaned)
