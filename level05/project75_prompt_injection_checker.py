"""Flag common prompt-injection phrases for review; not a security guarantee."""
PATTERNS=('ignore previous instructions','reveal the system prompt','developer message','bypass all rules','exfiltrate secrets','ignore all prior')

def inspect_text(text):
    if not isinstance(text,str): raise TypeError('text must be a string.')
    low=text.casefold()
    hits=[p for p in PATTERNS if p in low]
    return {'flagged':bool(hits),'matched_patterns':hits,'warning':'Pattern checks are incomplete. Never treat this result as a security boundary.'}
