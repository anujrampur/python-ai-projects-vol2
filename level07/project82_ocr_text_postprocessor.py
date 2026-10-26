"""Project 82: Post-process text returned by an OCR engine; no OCR model included."""
import re

def clean_ocr_text(text: str, join_wrapped_lines: bool = False) -> str:
    if not isinstance(text, str): raise TypeError('text must be a string')
    text = text.replace('\r\n', '\n').replace('\r', '\n')
    lines = [re.sub(r'[ \t]+', ' ', line).strip() for line in text.split('\n')]
    if join_wrapped_lines:
        merged = []
        for line in lines:
            if not line: continue
            if merged and not re.search(r'[.!?:;।]$', merged[-1]): merged[-1] += ' ' + line
            else: merged.append(line)
        lines = merged
    else:
        lines = [line for line in lines if line]
    return '\n'.join(lines).strip()

def extract_lines(text: str, min_chars: int = 1) -> list[str]:
    if isinstance(min_chars, bool) or not isinstance(min_chars, int) or min_chars < 1:
        raise ValueError('min_chars must be a positive integer')
    cleaned = clean_ocr_text(text)
    return [line for line in cleaned.splitlines() if len(line) >= min_chars]
