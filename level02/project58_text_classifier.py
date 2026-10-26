"""Project 58: Transparent rule-based text classifier (spam/ham and broad topics).

This is a teaching baseline, not a trained machine-learning model. It should not
be used as the sole basis for moderation or other consequential decisions.
"""
from __future__ import annotations
import re

_SPAM_TERMS = {"winner", "won", "prize", "claim", "urgent", "free", "offer", "cash", "click", "lottery"}
_TOPIC_TERMS = {
    "technology": {"python", "software", "computer", "code", "data", "ai", "model", "app"},
    "education": {"student", "teacher", "school", "learn", "lesson", "exam", "class", "study"},
    "health": {"health", "doctor", "exercise", "sleep", "medicine", "patient", "hospital"},
    "finance": {"money", "bank", "budget", "loan", "investment", "price", "cost", "payment"},
}


def classify_text(text: str) -> dict[str, object]:
    """Classify a short message with keyword counts and expose the evidence."""
    if not isinstance(text, str) or not text.strip():
        raise ValueError("Please enter non-empty text.")
    if len(text) > 20_000:
        raise ValueError("Text is too long (maximum 20,000 characters).")
    tokens = re.findall(r"[a-z]+", text.lower())
    token_set=set(tokens)
    spam_hits=sorted(token_set & _SPAM_TERMS)
    spam_label="spam" if spam_hits else "ham/uncertain"
    scores={topic: len(token_set & terms) for topic, terms in _TOPIC_TERMS.items()}
    best=max(scores, key=scores.get)
    topic=best if scores[best] else "general/unknown"
    return {"spam_label": spam_label, "spam_evidence": spam_hits,
            "topic": topic, "topic_scores": scores}


if __name__ == "__main__":
    print("Rule-based text classifier (educational demo)")
    try:
        result=classify_text(input("Enter a message: "))
        print("Spam result:", result["spam_label"])
        print("Matched spam terms:", ", ".join(result["spam_evidence"]) or "none")
        print("Topic:", result["topic"])
        print("Topic scores:", result["topic_scores"])
    except ValueError as exc:
        print(exc)
