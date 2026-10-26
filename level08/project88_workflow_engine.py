"""Project 88: Small allowlisted workflow engine; steps are declarative only."""
from dataclasses import dataclass

@dataclass(frozen=True)
class Step:
    name: str
    action: str

_ALLOWED = {'uppercase', 'lowercase', 'strip'}
def run_workflow(value: str, steps: list[Step]) -> str:
    result=value
    for step in steps:
        if step.action not in _ALLOWED:
            raise ValueError(f"unsupported action: {step.action}")
        if step.action == 'uppercase': result=result.upper()
        elif step.action == 'lowercase': result=result.lower()
        elif step.action == 'strip': result=result.strip()
    return result
