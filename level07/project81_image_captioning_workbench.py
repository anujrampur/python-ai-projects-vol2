"""Project 81: Image captioning workbench interface (model-agnostic scaffold).
This does not infer image contents; it validates and formats captions supplied by a vision model or human.
"""
from pathlib import Path

def validate_image_path(path: str, allowed_extensions=(".png", ".jpg", ".jpeg", ".webp", ".bmp")) -> Path:
    p = Path(path).expanduser()
    if not p.exists() or not p.is_file(): raise FileNotFoundError(f"Image file not found: {p}")
    if p.suffix.lower() not in allowed_extensions: raise ValueError("Unsupported image extension")
    return p

def format_caption(image_name: str, caption: str, max_chars: int = 300) -> str:
    if not image_name.strip(): raise ValueError("image_name cannot be empty")
    if not caption.strip(): raise ValueError("caption cannot be empty")
    if isinstance(max_chars, bool) or not isinstance(max_chars, int) or max_chars < 1: raise ValueError("max_chars must be a positive integer")
    clean = " ".join(caption.split())
    if len(clean) > max_chars: clean = clean[:max_chars].rstrip() + "…"
    return f"{image_name.strip()}: {clean}"
