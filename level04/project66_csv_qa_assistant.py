"""Answer simple questions about a CSV file using deterministic summaries.

This is a local data assistant, not an LLM. It reads CSV safely and supports
row count, column names, and numeric-column averages.
"""
from __future__ import annotations
import csv
from pathlib import Path


def load_csv(path: str | Path) -> list[dict[str, str]]:
    """Load a UTF-8 CSV as dictionaries; reject missing or empty files."""
    file_path = Path(path)
    if not file_path.is_file():
        raise FileNotFoundError(f"CSV file not found: {file_path}")
    with file_path.open('r', encoding='utf-8-sig', newline='') as handle:
        reader = csv.DictReader(handle)
        if not reader.fieldnames:
            raise ValueError('CSV must contain a header row.')
        rows = list(reader)
    return rows


def answer_question(rows: list[dict[str, str]], question: str) -> str:
    """Answer a small set of explicit questions about loaded CSV rows."""
    q = question.strip().lower()
    if not q:
        raise ValueError('Question cannot be empty.')
    columns = list(rows[0].keys()) if rows else []
    if any(term in q for term in ('how many rows', 'row count', 'number of rows')):
        return f'The CSV contains {len(rows)} data rows.'
    if any(term in q for term in ('which columns', 'column names', 'what columns')):
        return 'Columns: ' + (', '.join(columns) if columns else '(no columns)')
    if 'average' in q or 'mean' in q:
        requested = next((c for c in columns if c.lower() in q), None)
        if requested is None:
            raise ValueError('Mention a column name when asking for an average.')
        values=[]
        for row in rows:
            raw=(row.get(requested) or '').strip()
            if raw:
                try: values.append(float(raw))
                except ValueError: continue
        if not values:
            raise ValueError(f'Column {requested!r} has no numeric values.')
        return f'Average of {requested}: {sum(values)/len(values):.2f} (n={len(values)}).'
    raise ValueError('Supported questions: row count, column names, or average of a numeric column.')
