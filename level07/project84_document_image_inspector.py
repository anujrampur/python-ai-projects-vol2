"""Project 84: Inspect image-file metadata and prepare a document-image workflow."""
from pathlib import Path
try:  # Support both package imports from the repository root and direct imports from level07.
    from .project81_image_captioning_prep import SUPPORTED_SUFFIXES
except ImportError:  # pragma: no cover - exercised when level07 is the working directory
    from project81_image_captioning_prep import SUPPORTED_SUFFIXES

def inspect_document_image(path: str) -> dict:
    p = Path(path).expanduser()
    if not p.exists() or not p.is_file(): raise FileNotFoundError(str(p))
    if p.suffix.lower() not in SUPPORTED_SUFFIXES: raise ValueError('Unsupported image extension')
    size = p.stat().st_size
    if size == 0: raise ValueError('Image file is empty')
    return {'path': str(p.resolve()), 'filename': p.name, 'extension': p.suffix.lower(),
            'size_bytes': size, 'likely_scanned_document': any(k in p.stem.casefold() for k in ('scan','document','page','receipt','invoice')),
            'notice': 'This is filename/size inspection only; it does not verify image contents or extract text.'}
