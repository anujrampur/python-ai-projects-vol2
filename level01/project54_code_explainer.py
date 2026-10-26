"""Project 54: Beginner-friendly Python code explainer (offline starter).

Uses safe static parsing and simple explanations; it never executes submitted code.
"""
import ast


def explain_python(source: str) -> list[str]:
    """Return plain-language notes about a small Python snippet."""
    if not source.strip():
        raise ValueError("Please paste some Python code.")
    if len(source) > 20_000:
        raise ValueError("Code is too long (maximum 20,000 characters).")
    try:
        tree = ast.parse(source)
    except SyntaxError as exc:
        raise ValueError(f"Python syntax error on line {exc.lineno}: {exc.msg}") from exc

    notes = []
    for node in ast.walk(tree):
        if isinstance(node, ast.FunctionDef):
            notes.append(f"Defines a function named '{node.name}'.")
        elif isinstance(node, ast.ClassDef):
            notes.append(f"Defines a class named '{node.name}'.")
        elif isinstance(node, ast.For):
            notes.append("Contains a for-loop that repeats over an iterable.")
        elif isinstance(node, ast.While):
            notes.append("Contains a while-loop that repeats while its condition is true.")
        elif isinstance(node, ast.If):
            notes.append("Checks a condition with an if statement.")
        elif isinstance(node, ast.Call):
            name = node.func.id if isinstance(node.func, ast.Name) else "method or callable"
            notes.append(f"Calls '{name}'.")
        elif isinstance(node, ast.Assign):
            names = [target.id for target in node.targets if isinstance(target, ast.Name)]
            if names:
                notes.append(f"Assigns a value to: {', '.join(names)}.")
    # Preserve order while removing duplicate notes caused by nested AST traversal.
    unique = list(dict.fromkeys(notes))
    return unique or ["Valid Python syntax. This snippet contains no constructs recognized by the basic explainer."]


if __name__ == "__main__":
    print("Paste Python code, then enter a line containing only END:")
    lines = []
    while True:
        line = input()
        if line.strip() == "END": break
        lines.append(line)
    try:
        for note in explain_python("\n".join(lines)):
            print("-", note)
    except ValueError as error:
        print(error)
