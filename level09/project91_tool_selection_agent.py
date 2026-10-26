"""Project 91: Deterministic allowlisted tool selection.

This educational router scores exact keyword matches. It does not execute tools,
call an LLM, or understand intent beyond the configured vocabulary.
"""

from dataclasses import dataclass
import re


@dataclass(frozen=True)
class Tool:
    """A tool that may be selected by keyword matching."""

    name: str
    description: str
    keywords: tuple[str, ...]


TOOLS = (
    Tool(
        "calculator",
        "Evaluate simple arithmetic expressions using a safe calculator.",
        ("calculate", "calculation", "sum", "add", "plus", "multiply", "divide", "math"),
    ),
    Tool(
        "knowledge_search",
        "Search a local knowledge collection.",
        ("search", "find", "document", "documents", "knowledge", "source", "sources"),
    ),
    Tool(
        "draft_writer",
        "Draft or rewrite text without sending it.",
        ("draft", "write", "rewrite", "email", "message"),
    ),
)


def _tokenize(text: str) -> set[str]:
    """Return lowercase word tokens, treating punctuation as separators."""
    return set(re.findall(r"\w+", text.casefold(), flags=re.UNICODE))


def select_tool(request: str) -> str | None:
    """Return the best allowlisted tool name, or ``None`` for no match.

    Each configured keyword contributes at most one point. Ties are resolved by
    tool name alphabetically, so the result is deterministic. Non-string inputs
    are rejected instead of being silently coerced.
    """
    if not isinstance(request, str):
        raise TypeError("request must be a string")

    words = _tokenize(request)
    if not words:
        return None

    scores = [
        (sum(keyword in words for keyword in tool.keywords), tool.name)
        for tool in TOOLS
    ]
    best_score = max(score for score, _ in scores)
    if best_score == 0:
        return None
    return min(name for score, name in scores if score == best_score)


if __name__ == "__main__":
    examples = (
        "calculate 8 + 4",
        "search my notes",
        "draft an email",
        "launch a rocket",
    )
    for prompt in examples:
        print(f"{prompt!r} -> {select_tool(prompt)}")
