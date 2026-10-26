"""Project 87: Dry-run file organization plan by extension.
It reports moves only; it does not change files on disk.
"""
from pathlib import Path


def plan_moves(paths: list[str | Path]) -> list[dict[str, str]]:
    plan = []

    for raw in paths:
        p = Path(raw)

        if not p.name or p.name in {".", ".."}:
            continue

        suffix = p.suffix.lower().lstrip(".")
        folder = (suffix or "no_extension").replace("\\", "_")

        plan.append({
            "source": str(p),
            "destination": (Path(folder) / p.name).as_posix(),
        })

    return plan
