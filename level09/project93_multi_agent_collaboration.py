"""Project 93: Combine role-labelled contributions from independent agents.

This deterministic formatter does not run or coordinate actual AI agents.
"""
from dataclasses import dataclass


@dataclass(frozen=True)
class Contribution:
    """A single contribution labelled with the role that produced it."""

    role: str
    content: str


def combine_contributions(contributions: list[Contribution]) -> str:
    """Validate and combine contributions in their original order.

    Args:
        contributions: Non-empty sequence of Contribution instances.

    Returns:
        Markdown sections, one per contribution, separated by a blank line.

    Raises:
        TypeError: If the collection or any contribution has the wrong type.
        ValueError: If the collection is empty or a role/content is blank.
    """
    if isinstance(contributions, (str, bytes)) or not isinstance(contributions, (list, tuple)):
        raise TypeError("contributions must be a list or tuple of Contribution objects")
    if not contributions:
        raise ValueError("at least one contribution is required")

    rendered = []
    for index, item in enumerate(contributions, start=1):
        if not isinstance(item, Contribution):
            raise TypeError(f"contribution {index} must be a Contribution instance")
        if not isinstance(item.role, str) or not isinstance(item.content, str):
            raise TypeError(f"contribution {index} role and content must be strings")

        role = item.role.strip()
        content = item.content.strip()
        if not role or not content:
            raise ValueError(f"contribution {index} needs a non-empty role and content")
        if "\n" in role or "\r" in role:
            raise ValueError(f"contribution {index} role must be a single line")
        rendered.append(f"## {role}\n{content}")

    return "\n\n".join(rendered)
