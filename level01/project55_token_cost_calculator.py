"""Project 55: Token & Cost Calculator.

Token counts are rough estimates (characters / 4), not tokenizer-exact counts.
Prices must be supplied by the user because provider prices change.
"""
from dataclasses import dataclass

@dataclass(frozen=True)
class Estimate:
    estimated_tokens: int
    input_cost: float
    output_cost: float
    total_cost: float


def estimate_tokens(text: str) -> int:
    """Estimate tokens using a documented 4-characters-per-token heuristic."""
    if not isinstance(text, str):
        raise ValueError("text must be a string")
    if not text:
        return 0
    return max(1, (len(text) + 3) // 4)


def estimate_cost(input_tokens: int, output_tokens: int, input_price_per_million: float,
                  output_price_per_million: float) -> Estimate:
    """Estimate cost for user-supplied prices quoted per one million tokens."""
    values = (input_tokens, output_tokens)
    if any(isinstance(v, bool) or not isinstance(v, int) or v < 0 for v in values):
        raise ValueError("Token counts must be non-negative integers.")
    prices = (input_price_per_million, output_price_per_million)
    if any(not isinstance(p, (int, float)) or isinstance(p, bool) or p < 0 for p in prices):
        raise ValueError("Prices must be non-negative numbers.")
    input_cost = input_tokens * float(input_price_per_million) / 1_000_000
    output_cost = output_tokens * float(output_price_per_million) / 1_000_000
    return Estimate(input_tokens + output_tokens, input_cost, output_cost, input_cost + output_cost)


if __name__ == "__main__":
    prompt = input("Paste prompt text: ")
    completion = input("Paste expected output text: ")
    try:
        input_tokens, output_tokens = estimate_tokens(prompt), estimate_tokens(completion)
        input_price = float(input("Input price per 1M tokens (your provider's current price): "))
        output_price = float(input("Output price per 1M tokens: "))
        result = estimate_cost(input_tokens, output_tokens, input_price, output_price)
        print(f"Estimated input tokens: {input_tokens}\nEstimated output tokens: {output_tokens}")
        print(f"Estimated total cost: {result.total_cost:.8f} (same currency as entered prices)")
        print("Note: token counts are approximate; check your provider's tokenizer and current pricing.")
    except ValueError as error:
        print(f"Invalid input: {error}")
