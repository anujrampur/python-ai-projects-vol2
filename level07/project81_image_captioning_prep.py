"""Project 81: Image captioning input preparation and safe model adapter boundary.

This standard-library prototype validates image paths and prepares a request. It does
not generate captions; connect a real vision model in `caption_with_model`.
"""
from pathlib import Path
from dataclasses import dataclass

SUPPORTED_SUFFIXES = {".png", ".jpg", ".jpeg", ".webp", ".bmp"}

@dataclass(frozen=True)
class ImageRequest:
    path: str
    instruction: str = "Describe the visible contents objectively in one sentence."

def prepare_image_request(path: str, instruction: str | None = None) -> ImageRequest:
    candidate = Path(path).expanduser()
    if not candidate.exists() or not candidate.is_file():
        raise FileNotFoundError(f"Image file not found: {candidate}")
    if candidate.suffix.lower() not in SUPPORTED_SUFFIXES:
        raise ValueError(f"Unsupported image type: {candidate.suffix}")
    if candidate.stat().st_size == 0:
        raise ValueError("Image file is empty")
    text = (instruction or "Describe the visible contents objectively in one sentence.").strip()
    if not text:
        raise ValueError("instruction must not be blank")
    return ImageRequest(str(candidate.resolve()), text)

def caption_with_model(request: ImageRequest, model_adapter=None) -> str:
    """Call an injected adapter; fail clearly rather than inventing a caption."""
    if model_adapter is None:
        raise RuntimeError("No vision model is configured. Supply a model_adapter callable.")
    result = model_adapter(request.path, request.instruction)
    if not isinstance(result, str) or not result.strip():
        raise ValueError("Model adapter must return a non-empty string")
    return result.strip()
