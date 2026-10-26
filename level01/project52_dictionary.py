"""Project 52: AI Dictionary & Word Explainer (offline starter).

This version uses a small curated dictionary. It does not claim to be an LLM.
"""
from dataclasses import dataclass


@dataclass(frozen=True)
class Entry:
    word: str
    meaning: str
    example: str
    hindi: str

_WORDS = {
    "curiosity": Entry("curiosity", "a strong desire to learn or know something", "Her curiosity led her to ask thoughtful questions.", "जिज्ञासा"),
    "resilient": Entry("resilient", "able to recover after difficulty", "The resilient team learned from the setback.", "लचीला; कठिनाई से उबरने वाला"),
    "analyze": Entry("analyze", "to examine something carefully", "We analyze the data before drawing a conclusion.", "विश्लेषण करना"),
    "concise": Entry("concise", "short but clear and complete", "Please write a concise summary.", "संक्षिप्त और स्पष्ट"),
    "iterate": Entry("iterate", "to repeat a process to improve a result", "Developers iterate on a prototype after feedback.", "बार-बार सुधार करना"),
}


def explain_word(word: str) -> Entry:
    """Return a dictionary entry or raise ValueError for unknown words."""
    cleaned = word.strip().lower()
    if not cleaned:
        raise ValueError("Please enter a word.")
    try:
        return _WORDS[cleaned]
    except KeyError as exc:
        raise ValueError(f"'{word.strip()}' is not in this starter dictionary.") from exc


def explain_eli15(entry: Entry) -> str:
    """Explain the entry in simple language (ELI15-style)."""
    return f"In simple words, {entry.word} means: {entry.meaning}. Example: {entry.example}"


if __name__ == "__main__":
    print("Dictionary & Word Explainer (offline starter)")
    try:
        item = explain_word(input("Enter an English word: "))
        print(f"Meaning: {item.meaning}\nHindi: {item.hindi}\nExample: {item.example}")
        print(explain_eli15(item))
    except ValueError as error:
        print(error)
