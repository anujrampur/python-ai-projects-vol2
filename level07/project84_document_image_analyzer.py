"""Project 84: Basic image-file metadata analyzer using the standard library.
It reports file metadata only, not semantic image contents.
"""
from pathlib import Path
import hashlib
_ALLOWED={'.png','.jpg','.jpeg','.webp','.bmp','.tif','.tiff'}
def analyze_image_file(path: str) -> dict:
    p=Path(path).expanduser()
    if not p.exists() or not p.is_file(): raise FileNotFoundError(str(p))
    if p.suffix.lower() not in _ALLOWED: raise ValueError("Unsupported image extension")
    digest=hashlib.sha256()
    with p.open('rb') as f:
        for chunk in iter(lambda:f.read(65536), b''): digest.update(chunk)
    return {"name":p.name,"extension":p.suffix.lower(),"size_bytes":p.stat().st_size,"sha256":digest.hexdigest()}
