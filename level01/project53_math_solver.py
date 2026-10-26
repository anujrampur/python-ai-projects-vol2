"""Project 53: Step-by-step arithmetic solver (safe offline starter).

Supports expressions containing numbers and +, -, *, /, parentheses and decimals.
It intentionally rejects names, function calls, powers and other Python syntax.
"""
import ast
import operator

_BINARY = {ast.Add: operator.add, ast.Sub: operator.sub, ast.Mult: operator.mul, ast.Div: operator.truediv}
_UNARY = {ast.UAdd: operator.pos, ast.USub: operator.neg}


def _evaluate(node):
    if isinstance(node, ast.Constant) and isinstance(node.value, (int, float)) and not isinstance(node.value, bool):
        return node.value
    if isinstance(node, ast.BinOp) and type(node.op) in _BINARY:
        left, right = _evaluate(node.left), _evaluate(node.right)
        if isinstance(node.op, ast.Div) and right == 0:
            raise ValueError("Division by zero is not allowed.")
        return _BINARY[type(node.op)](left, right)
    if isinstance(node, ast.UnaryOp) and type(node.op) in _UNARY:
        return _UNARY[type(node.op)](_evaluate(node.operand))
    raise ValueError("Unsupported expression. Use numbers, +, -, *, / and parentheses only.")


def solve(expression: str) -> dict:
    """Return a result and a transparent explanation of the supported expression."""
    if not expression.strip():
        raise ValueError("Expression cannot be blank.")
    if len(expression) > 200:
        raise ValueError("Expression is too long (maximum 200 characters).")
    try:
        tree = ast.parse(expression, mode="eval")
    except SyntaxError as exc:
        raise ValueError("Invalid arithmetic expression.") from exc
    value = _evaluate(tree.body)
    return {"expression": expression.strip(), "result": value,
            "steps": [f"Expression: {expression.strip()}", "Apply parentheses first, then multiplication/division, then addition/subtraction.", f"Result: {value}"]}


if __name__ == "__main__":
    try:
        answer = solve(input("Enter arithmetic expression: "))
        print("\n".join(answer["steps"]))
    except (ValueError, OverflowError) as error:
        print(f"Could not solve: {error}")
