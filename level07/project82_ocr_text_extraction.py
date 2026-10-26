"""Project 82: Optional OCR adapter for image files. Requires Pillow and pytesseract.
Install extras separately and install the Tesseract OCR engine on your OS.
"""
from pathlib import Path

def extract_text(image_path: str, lang: str = "eng") -> str:
    path = Path(image_path).expanduser()
    if not path.exists() or not path.is_file(): raise FileNotFoundError(f"Image not found: {path}")
    try:
        from PIL import Image
        import pytesseract
    except ImportError as exc:
        raise RuntimeError("OCR dependencies missing. Install Pillow and pytesseract, plus the Tesseract engine.") from exc
    with Image.open(path) as image:
        return pytesseract.image_to_string(image, lang=lang).strip()
