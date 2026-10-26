"""Project 96: a small, testable FastAPI AI-service example.

The core stays framework-independent so validation can be tested offline. The
optional HTTP layer uses a clearly labelled demo response, not a real model.
"""
from dataclasses import dataclass
from typing import Any

MAX_PROMPT_LENGTH = 4000


@dataclass(frozen=True)
class GenerateRequest:
    """Validated prompt accepted by the service."""

    prompt: str


@dataclass(frozen=True)
class GenerateResponse:
    """Response shape returned by the demo adapter."""

    text: str
    model: str = "demo-template"


def validate_request(payload: Any) -> GenerateRequest:
    """Validate a JSON-object-like payload and normalize its prompt."""
    if not isinstance(payload, dict):
        raise ValueError("Request body must be a JSON object.")

    prompt = payload.get("prompt")
    if not isinstance(prompt, str):
        raise ValueError("'prompt' must be a string.")

    prompt = prompt.strip()
    if not prompt:
        raise ValueError("'prompt' cannot be empty.")
    if len(prompt) > MAX_PROMPT_LENGTH:
        raise ValueError(f"'prompt' must be at most {MAX_PROMPT_LENGTH} characters.")

    return GenerateRequest(prompt=prompt)


def generate_demo(prompt: str) -> GenerateResponse:
    """Return a deterministic placeholder; this function does not call an LLM."""
    request = validate_request({"prompt": prompt})
    return GenerateResponse(
        text=(
            "Demo response: I received a prompt containing "
            f"{len(request.prompt)} characters."
        )
    )


def create_app():
    """Create the optional FastAPI app, or explain how to install dependencies."""
    try:
        from fastapi import FastAPI, HTTPException
    except ImportError as exc:
        raise RuntimeError(
            "Install optional dependencies: pip install fastapi uvicorn"
        ) from exc

    app = FastAPI(title="Educational AI Service", version="1.0.0")

    @app.get("/health")
    def health():
        return {"status": "ok"}

    @app.post("/generate")
    def generate(payload: dict):
        try:
            request = validate_request(payload)
            response = generate_demo(request.prompt)
        except ValueError as exc:
            raise HTTPException(status_code=422, detail=str(exc)) from exc
        return {"text": response.text, "model": response.model}

    return app


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(create_app(), host="127.0.0.1", port=8000)
