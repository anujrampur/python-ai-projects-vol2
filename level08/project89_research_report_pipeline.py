"""Project 89: Build a research report from user-supplied notes and source labels.

This module formats supplied notes into Markdown. It does not discover sources,
open URLs, or independently verify the truth of any claim.
"""

from dataclasses import dataclass


@dataclass(frozen=True)
class SourceNote:
    """A note supplied by the user, with a label for tracing its origin."""

    source_id: str
    title: str
    note: str

    def __post_init__(self) -> None:
        """Reject missing or whitespace-only fields at record creation time."""
        for field_name in ("source_id", "title", "note"):
            value = getattr(self, field_name)
            if not isinstance(value, str) or not value.strip():
                raise ValueError(
                    f"{field_name.replace('_', ' ')} must be a non-empty string"
                )


def build_report(topic: str, notes: list[SourceNote]) -> str:
    """Return a structured Markdown brief from a topic and supplied notes.

    Args:
        topic: Subject of the brief. Leading/trailing whitespace is removed.
        notes: At least one validated ``SourceNote`` record.

    Raises:
        ValueError: If the topic is blank, notes are missing, or an item is
            not a ``SourceNote`` instance.
    """
    if not isinstance(topic, str) or not topic.strip():
        raise ValueError("topic is required")
    if not notes:
        raise ValueError("at least one source note is required")

    normalized_topic = topic.strip()
    lines = [
        f"# Research Brief: {normalized_topic}",
        "",
        "## Scope",
        "This draft summarizes only the notes supplied by the user.",
        "",
        "## Source Notes",
    ]

    for source in notes:
        if not isinstance(source, SourceNote):
            raise ValueError("each item must be a SourceNote instance")
        # SourceNote validates fields at construction; strip note text for output.
        lines.extend(
            [
                f"### [{source.source_id.strip()}] {source.title.strip()}",
                source.note.strip(),
                "",
            ]
        )

    lines.extend(
        [
            "## Verification Checklist",
            "- Verify each note against the original source.",
            "- Check publication date, author, and context where applicable.",
            "- Record disagreements or missing evidence rather than guessing.",
            "- Do not treat this draft as independently fact-checked.",
        ]
    )
    return "\n".join(lines)
