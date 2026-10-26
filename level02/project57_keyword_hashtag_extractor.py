"""Project 57: Keyword and hashtag extractor using simple frequency scoring."""
from __future__ import annotations
import re
from collections import Counter

_STOPWORDS = set("a an the and or but if then is are was were be been being to of in on for with by from as at it this that these those we you they he she i our your their not can will would should into about".split())
_TOKEN_RE = re.compile(r"[A-Za-z][A-Za-z0-9'-]{1,}")


def extract_keywords(text: str, limit: int = 8) -> list[str]:
    """Return frequent non-stopword tokens, ordered by frequency then first appearance."""
    if not isinstance(text, str):
        raise ValueError("text must be a string")
    if isinstance(limit, bool) or not isinstance(limit, int) or not 1 <= limit <= 50:
        raise ValueError("limit must be an integer from 1 to 50")
    tokens = [m.group(0).lower() for m in _TOKEN_RE.finditer(text)]
    counts = Counter(t for t in tokens if t not in _STOPWORDS)
    first = {t: tokens.index(t) for t in counts}
    return sorted(counts, key=lambda t: (-counts[t], first[t]))[:limit]


def make_hashtags(keywords: list[str], limit: int = 8) -> list[str]:
    """Convert keywords into social hashtags, removing punctuation and duplicates."""
    if isinstance(limit, bool) or not isinstance(limit, int) or not 1 <= limit <= 50:
        raise ValueError("limit must be an integer from 1 to 50")
    result=[]
    for word in keywords:
        cleaned = re.sub(r"[^A-Za-z0-9_]", "", str(word))
        if cleaned and ("#" + cleaned) not in result:
            result.append("#" + cleaned)
        if len(result) >= limit:
            break
    return result


if __name__ == "__main__":
    text=input("Paste text: ")
    try:
        words=extract_keywords(text)
        print("Keywords:", ", ".join(words) if words else "No keywords found")
        print("Hashtags:", " ".join(make_hashtags(words)))
    except ValueError as exc:
        print(exc)
