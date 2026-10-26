"""Project 64: Private local reflection journal (non-medical, reflection only).

Entries are returned to the caller but are not saved automatically. This avoids
surprising persistence; add secure storage only after designing consent and privacy.
"""
from __future__ import annotations
from dataclasses import dataclass
from datetime import datetime, timezone

@dataclass(frozen=True)
class JournalEntry:
    created_at: str
    mood: str
    reflection: str
    prompt: str

_PROMPTS=("What felt important today?", "What is one thing you would like to let go of?", "What is one small thing you can do for yourself tomorrow?")

def create_entry(mood: str, reflection: str, *, now: datetime | None = None) -> JournalEntry:
    if not isinstance(mood,str) or not mood.strip() or len(mood)>40:
        raise ValueError("mood must be a non-empty label of at most 40 characters")
    if not isinstance(reflection,str) or not reflection.strip():
        raise ValueError("reflection must not be empty")
    if len(reflection)>10_000: raise ValueError("reflection exceeds 10,000 characters")
    timestamp=now or datetime.now(timezone.utc)
    if timestamp.tzinfo is None: raise ValueError("now must include timezone information")
    prompt=_PROMPTS[len(reflection.strip()) % len(_PROMPTS)]
    return JournalEntry(timestamp.isoformat(),mood.strip(),reflection.strip(),prompt)

if __name__ == "__main__":
    print("Reflection Journal — non-medical journaling only. Nothing is saved automatically.")
    try:
        entry=create_entry(input("Mood label: "),input("Reflection: "))
        print(f"Entry created (not saved) at {entry.created_at}\nPrompt: {entry.prompt}")
    except ValueError as exc: print(exc)
