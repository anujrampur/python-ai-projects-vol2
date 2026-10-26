"""Project 86: Template-based email draft builder; no email is sent."""
from dataclasses import dataclass

@dataclass(frozen=True)
class EmailDraft:
    subject: str
    body: str

def build_draft(recipient: str, purpose: str, key_points: list[str], tone: str = "professional") -> EmailDraft:
    recipient, purpose, tone = recipient.strip(), purpose.strip(), tone.strip().lower()
    if not recipient or not purpose:
        raise ValueError("recipient and purpose are required")
    if tone not in {"professional", "friendly", "concise"}:
        raise ValueError("tone must be professional, friendly, or concise")
    points = [p.strip() for p in key_points if isinstance(p, str) and p.strip()]
    if not points:
        raise ValueError("provide at least one key point")
    bullets = "\n".join(f"- {p}" for p in points)
    if tone == "friendly":
        opening, closing = f"Hi {recipient},", "Thanks so much,\n[Your name]"
    elif tone == "concise":
        opening, closing = f"Hello {recipient},", "Regards,\n[Your name]"
    else:
        opening, closing = f"Dear {recipient},", "Kind regards,\n[Your name]"
    body = f"{opening}\n\nI am writing regarding {purpose}.\n\nKey points:\n{bullets}\n\n{closing}"
    return EmailDraft(subject=f"Regarding {purpose}", body=body)
