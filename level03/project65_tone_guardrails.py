"""Project 65: Apply simple tone preferences and safety guardrails to draft text.

This is a demonstration filter, not a comprehensive safety system or a substitute
for review. It does not generate factual content.
"""
from __future__ import annotations

_TONE_PREFIX={"friendly":"Thanks for sharing. ","formal":"Thank you for your message. ","concise":"In brief: ","encouraging":"You can take this one step at a time. "}
_BLOCKED_MARKERS=("ignore all rules", "reveal your password", "steal credentials")

def format_response(text: str, tone: str = "friendly", max_chars: int = 1000) -> dict[str,str]:
    if not isinstance(text,str) or not text.strip(): raise ValueError("text must not be empty")
    if tone not in _TONE_PREFIX: raise ValueError(f"tone must be one of: {', '.join(_TONE_PREFIX)}")
    if isinstance(max_chars,bool) or not isinstance(max_chars,int) or not 20 <= max_chars <= 5000:
        raise ValueError("max_chars must be an integer from 20 to 5000")
    clean=" ".join(text.split())
    if any(marker in clean.lower() for marker in _BLOCKED_MARKERS):
        return {"status":"blocked", "text":"I can't help with requests to expose passwords or steal credentials."}
    prefix=_TONE_PREFIX[tone]
    result=(prefix+clean)[:max_chars]
    return {"status":"ok", "text":result}

if __name__ == "__main__":
    try:
        text=input("Draft text: "); tone=input("Tone (friendly/formal/concise/encouraging): ").strip().lower()
        result=format_response(text,tone); print(result["status"].upper()+":",result["text"])
    except ValueError as exc: print(exc)
