"""Project 59: Extract action items from meeting notes with transparent heuristics."""
from __future__ import annotations
import re
from dataclasses import dataclass

_ACTION_VERBS = r"(?:will|must|need to|needs to|should|follow up|send|prepare|create|review|complete|contact|schedule|share|update|confirm|assign|check)"
_ACTION_RE = re.compile(rf"\b{_ACTION_VERBS}\b", re.IGNORECASE)
_OWNER_RE = re.compile(r"^\s*([A-Z][A-Za-z .'-]{0,35})\s*:\s*(.+)$")
_DUE_RE = re.compile(r"\b(by\s+(?:Monday|Tuesday|Wednesday|Thursday|Friday|Saturday|Sunday|tomorrow|today|EOD|\d{4}-\d{2}-\d{2}))\b", re.IGNORECASE)

@dataclass(frozen=True)
class ActionItem:
    task: str
    owner: str | None = None
    due: str | None = None


def extract_action_items(notes: str) -> list[ActionItem]:
    """Extract likely action sentences; review results because this is heuristic."""
    if not isinstance(notes, str) or not notes.strip():
        raise ValueError("Please provide meeting notes.")
    if len(notes) > 50_000:
        raise ValueError("Notes are too long (maximum 50,000 characters).")
    items=[]
    for raw in re.split(r"[\n.!?]+", notes):
        sentence=raw.strip(" -\t")
        if not sentence or not _ACTION_RE.search(sentence):
            continue
        owner=None; task=sentence
        match=_OWNER_RE.match(sentence)
        if match:
            owner=match.group(1).strip()
            task=match.group(2).strip()
        due_match=_DUE_RE.search(task)
        due=due_match.group(1) if due_match else None
        if not any(item.task.casefold()==task.casefold() for item in items):
            items.append(ActionItem(task=task, owner=owner, due=due))
    return items


if __name__ == "__main__":
    print("Paste meeting notes; enter END on a line by itself:")
    lines=[]
    while True:
        line=input()
        if line.strip().upper()=="END": break
        lines.append(line)
    try:
        items=extract_action_items("\n".join(lines))
        if not items: print("No likely action items found. Review the notes manually.")
        for i,item in enumerate(items,1):
            print(f"{i}. {item.task} | Owner: {item.owner or 'Unassigned'} | Due: {item.due or 'Not specified'}")
    except ValueError as exc: print(exc)
