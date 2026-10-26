"""Project 85: Validate image-classifier predictions and summarize top-k labels."""
from math import isfinite

def top_predictions(scores: dict[str, float], top_k: int = 3) -> list[dict[str, float | str]]:
    if not isinstance(scores, dict) or not scores: raise ValueError('scores must be a non-empty mapping')
    if isinstance(top_k, bool) or not isinstance(top_k, int) or top_k < 1: raise ValueError('top_k must be a positive integer')
    clean = {}
    for label, score in scores.items():
        if not isinstance(label, str) or not label.strip(): raise ValueError('labels must be non-empty strings')
        if isinstance(score, bool) or not isinstance(score, (int,float)) or not isfinite(score) or not 0 <= score <= 1:
            raise ValueError(f'invalid confidence for {label!r}')
        clean[label.strip()] = float(score)
    return [{'label': label, 'confidence': score} for label, score in sorted(clean.items(), key=lambda x: (-x[1], x[0]))[:top_k]]
