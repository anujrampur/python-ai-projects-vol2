"""Project 56: Offline paraphraser starter using conservative phrase substitutions.

This is not an AI model and cannot guarantee originality or plagiarism safety.
Review rewritten text and cite sources where appropriate.
"""
from __future__ import annotations
import re

_REPLACEMENTS = {
    r"\bin order to\b": "to",
    r"\bdue to the fact that\b": "because",
    r"\bat this point in time\b": "now",
    r"\bmake use of\b": "use",
    r"\ba large number of\b": "many",
    r"\bhas the ability to\b": "can",
    r"\bin addition\b": "also",
    r"\bhowever\b": "however",
}


def paraphrase(text: str) -> str:
    """Apply a small set of meaning-preserving phrase simplifications.

    The function deliberately avoids rewriting every word: automatic substitutions
    can change meaning, tone, or factual precision. Input is returned trimmed.
    """
    if not isinstance(text, str):
        raise ValueError("text must be a string")
    if not text.strip():
        raise ValueError("Please enter text to rewrite.")
    if len(text) > 20_000:
        raise ValueError("Text is too long (maximum 20,000 characters).")
    result = text.strip()
    for pattern, replacement in _REPLACEMENTS.items():
        result = re.sub(pattern, replacement, result, flags=re.IGNORECASE)
    return result


if __name__ == "__main__":
    print("Offline Paraphraser (heuristic demo; not plagiarism detection)")
    try:
        print("\nRewritten text:\n" + paraphrase(input("Enter text: ")))
    except ValueError as exc:
        print(exc)
