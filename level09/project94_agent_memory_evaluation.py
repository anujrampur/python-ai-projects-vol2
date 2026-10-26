"""Project 94: Minimal in-process memory store and outcome evaluator.

Memory is volatile and intended for small, non-sensitive notes. It is not a
secure database and does not persist automatically between program runs.
"""
from dataclasses import dataclass
import json
from pathlib import Path


@dataclass(frozen=True)
class MemoryRecord:
    """A simple key/value record used to describe a memory entry."""

    key: str
    value: str


class MemoryStore:
    """Store short string notes in memory for the current process."""

    def __init__(self) -> None:
        self._records: dict[str, str] = {}

    @staticmethod
    def _clean_text(value: str, field: str) -> str:
        if not isinstance(value, str):
            raise TypeError(f"{field} must be a string")
        cleaned = value.strip()
        if not cleaned:
            raise ValueError(f"{field} must be non-empty")
        return cleaned

    def remember(self, key: str, value: str) -> None:
        """Save a non-empty string key and value after trimming whitespace."""
        clean_key = self._clean_text(key, "key")
        clean_value = self._clean_text(value, "value")
        self._records[clean_key] = clean_value

    def recall(self, key: str) -> str | None:
        """Return the saved value, or None if the key has not been stored."""
        clean_key = self._clean_text(key, "key")
        return self._records.get(clean_key)

    def export_json(self, path: str | Path) -> None:
        """Export current records as UTF-8 JSON to the given file path."""
        destination = Path(path)
        destination.write_text(
            json.dumps(self._records, ensure_ascii=False, indent=2) + "\n",
            encoding="utf-8",
        )


def evaluate_outcome(expected: str, actual: str) -> dict[str, object]:
    """Compare strings after case-folding and collapsing whitespace.

    Original values are returned unchanged so callers can inspect a mismatch.
    This exact-text check is not a general measure of AI response quality.
    """
    if not isinstance(expected, str) or not isinstance(actual, str):
        raise TypeError("expected and actual must be strings")
    expected_norm = " ".join(expected.casefold().split())
    actual_norm = " ".join(actual.casefold().split())
    return {
        "passed": expected_norm == actual_norm,
        "expected": expected,
        "actual": actual,
    }
