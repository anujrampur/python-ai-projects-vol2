"""Command-line interface for Project 51."""
from __future__ import annotations

from project51_generator import generate_items


def _ask_choice(prompt: str, allowed: tuple[str, ...]) -> str:
    while True:
        value = input(prompt).strip().lower()
        if value in allowed:
            return value
        print(f"Please choose one of: {', '.join(allowed)}.")


def _ask_count() -> int:
    while True:
        raw = input("How many items (1-5): ").strip()
        try:
            count = int(raw)
        except ValueError:
            print("Enter a whole number from 1 to 5.")
            continue
        if 1 <= count <= 5:
            return count
        print("Count must be from 1 to 5.")


def main() -> None:
    print("=== Joke / Shayari / Quote Generator ===")
    language = _ask_choice("Choose language (en/hi): ", ("en", "hi"))
    content_type = _ask_choice(
        "Choose type (joke/shayari/quote): ",
        ("joke", "shayari", "quote"),
    )
    count = _ask_count()

    try:
        results = generate_items(content_type, language, count)
    except ValueError as exc:
        # Defensive handling: the CLI validates inputs before calling the generator.
        print(f"Could not generate content: {exc}")
        return

    print()
    for index, item in enumerate(results, start=1):
        print(f"{index}. {item}")


if __name__ == "__main__":
    main()
