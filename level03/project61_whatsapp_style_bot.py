"""Project 61: WhatsApp-style bot core with a provider-neutral reply function.

This is the message-processing core only. It does not connect to WhatsApp or
send messages. A real deployment requires an approved provider, credentials,
webhook verification, privacy controls, and current provider documentation.
"""
from __future__ import annotations


def create_reply(message: str, user_id: str | None = None) -> str:
    """Return a deterministic starter reply; user_id is reserved for session routing."""
    if not isinstance(message, str) or not message.strip():
        raise ValueError("message must not be empty")
    if len(message) > 4000:
        raise ValueError("message exceeds 4,000 characters")
    text=message.strip().lower()
    if text in {"hi", "hello", "hey", "namaste", "नमस्ते"}:
        return "Hello! I am a demo bot. Ask me about its features or type help."
    if text in {"help", "/help"}:
        return "Demo commands: help, hours, contact. This starter does not send real messages."
    if "hours" in text or "समय" in text:
        return "This demo has no configured business hours yet."
    if "contact" in text or "संपर्क" in text:
        return "Please add an official contact method to the bot configuration."
    return "Thanks for your message. This demo uses simple rules; connect an approved AI provider for richer replies."


if __name__ == "__main__":
    print("WhatsApp-style Bot Core (local demo; no messages are sent)")
    while True:
        message=input("You (or quit): ")
        if message.strip().lower() in {"quit", "exit"}: break
        try: print("Bot:", create_reply(message))
        except ValueError as exc: print(exc)
