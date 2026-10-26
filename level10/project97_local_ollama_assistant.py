"""Project 97: Local AI Assistant using an optional Ollama HTTP endpoint.

No network call occurs unless chat() is explicitly invoked. The default test
path injects a fake transport, keeping tests offline and deterministic.
"""
import json
import math
from urllib.request import Request, urlopen
from urllib.error import URLError, HTTPError

class OllamaError(RuntimeError):
    pass

def build_payload(prompt: str, model: str = "llama3.2") -> dict:
    if not isinstance(prompt, str) or not prompt.strip():
        raise ValueError("Prompt must be a non-empty string.")
    if not isinstance(model, str) or not model.strip():
        raise ValueError("Model name must be a non-empty string.")
    return {"model": model.strip(), "prompt": prompt.strip(), "stream": False}

def chat(prompt: str, model: str = "llama3.2", base_url: str = "http://127.0.0.1:11434",
         transport=None, timeout: float = 30.0) -> str:
    """Generate a response through Ollama or an injected offline transport.

    The injected transport receives (url, UTF-8 JSON bytes, timeout) and must
    return a dictionary containing a string ``response`` field.
    """
    payload = build_payload(prompt, model)
    if isinstance(timeout, bool) or not isinstance(timeout, (int, float)) or not math.isfinite(timeout) or timeout <= 0:
        raise ValueError("Timeout must be a finite positive number.")
    if not isinstance(base_url, str) or not base_url.strip():
        raise ValueError("Base URL must be a non-empty string.")
    base_url = base_url.strip().rstrip("/")
    if not (base_url.startswith("http://") or base_url.startswith("https://")):
        raise ValueError("Base URL must start with http:// or https://.")
    url = base_url + "/api/generate"
    body = json.dumps(payload).encode("utf-8")
    if transport is not None:
        try:
            result = transport(url, body, timeout)
        except Exception as exc:
            raise OllamaError(f"Injected transport failed: {exc}") from exc
        return _extract_response(result)
    request = Request(url, data=body, headers={"Content-Type": "application/json"}, method="POST")
    try:
        with urlopen(request, timeout=timeout) as response:
            result = json.loads(response.read().decode("utf-8"))
    except (HTTPError, URLError, TimeoutError, json.JSONDecodeError, UnicodeDecodeError) as exc:
        raise OllamaError(f"Could not reach Ollama at {base_url}: {exc}") from exc
    return _extract_response(result)


def _extract_response(result) -> str:
    """Validate the response shape returned by Ollama or a test transport."""
    if not isinstance(result, dict) or not isinstance(result.get("response"), str):
        raise OllamaError("Unexpected response from local model.")
    return result["response"]
