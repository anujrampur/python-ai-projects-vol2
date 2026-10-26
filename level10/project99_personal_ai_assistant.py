"""Project 99: Personal AI Assistant — safe document and tool workflow skeleton."""
from dataclasses import dataclass
from pathlib import Path
from typing import Callable

@dataclass(frozen=True)
class ToolResult:
    name: str
    output: str

class PersonalAssistant:
    def __init__(self, tools: dict[str, Callable[[str], str]] | None = None):
        self.tools = dict(tools or {})
        self.notes: list[str] = []

    def add_note(self, note: str) -> None:
        note = str(note).strip()
        if not note:
            raise ValueError("Note cannot be empty.")
        self.notes.append(note)

    def read_text_file(self, path: str, allowed_root: str) -> str:
        root = Path(allowed_root).resolve()
        candidate = Path(path).resolve()
        if candidate != root and root not in candidate.parents:
            raise ValueError("File is outside the allowed directory.")
        if candidate.suffix.lower() not in {".txt", ".md"}:
            raise ValueError("Only .txt and .md files are supported.")
        return candidate.read_text(encoding="utf-8")

    def run_tool(self, name: str, argument: str) -> ToolResult:
        tool = self.tools.get(name)
        if tool is None:
            raise ValueError("Tool is not allowlisted.")
        output = tool(argument)
        if not isinstance(output, str):
            raise TypeError("Tool must return a string.")
        return ToolResult(name=name, output=output)
