"""Extract readable text and produce a plain-language checklist.

This starter supports .txt and .md only. It does not provide legal advice.
"""
from pathlib import Path


def read_document(path: str | Path, max_chars: int = 100_000) -> str:
    p=Path(path)
    if p.suffix.lower() not in {'.txt', '.md'}:
        raise ValueError('Only .txt and .md files are supported in this starter.')
    if not p.is_file():
        raise FileNotFoundError(f'Document not found: {p}')
    text=p.read_text(encoding='utf-8')
    if len(text)>max_chars:
        raise ValueError(f'Document exceeds the {max_chars}-character limit.')
    if not text.strip():
        raise ValueError('Document is empty.')
    return text


def explain_document(text: str) -> dict[str, object]:
    """Return a transparent structural overview, not an AI/legal opinion."""
    if not text.strip():
        raise ValueError('Document text cannot be empty.')
    lines=[line.strip() for line in text.splitlines() if line.strip()]
    keywords=('must','shall','required','期限','within','days','payment','terminate','termination','notice','confidential','renewal','liability','must not','may not')
    flagged=[line for line in lines if any(k in line.lower() for k in keywords)]
    return {
        'line_count': len(lines),
        'word_count': len(text.split()),
        'possible_obligation_lines': flagged,
        'disclaimer': 'Automated structural aid only; verify the full document and consult a qualified professional for legal interpretation.'
    }
