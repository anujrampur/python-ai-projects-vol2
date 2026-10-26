"""Split text into overlapping chunks and show their sizes.

No embeddings are calculated in this standard-library starter. The project
prepares chunks for a future embedding model integration.
"""
from dataclasses import dataclass

@dataclass(frozen=True)
class Chunk:
    index: int
    text: str
    start: int
    end: int


def chunk_text(text: str, chunk_size: int = 500, overlap: int = 50) -> list[Chunk]:
    if not text: raise ValueError('Text cannot be empty.')
    if isinstance(chunk_size,bool) or not isinstance(chunk_size,int) or chunk_size < 1:
        raise ValueError('chunk_size must be a positive integer.')
    if isinstance(overlap,bool) or not isinstance(overlap,int) or overlap < 0:
        raise ValueError('overlap must be a non-negative integer.')
    if overlap >= chunk_size: raise ValueError('overlap must be smaller than chunk_size.')
    chunks=[]; start=0; index=1
    while start < len(text):
        end=min(start+chunk_size,len(text))
        chunks.append(Chunk(index,text[start:end],start,end))
        if end==len(text): break
        start=end-overlap; index+=1
    return chunks


def describe_chunks(chunks: list[Chunk]) -> str:
    if not chunks: return 'No chunks.'
    lines=[f'Chunks: {len(chunks)}']
    lines.extend(f'{c.index}: chars={len(c.text)}, range=[{c.start}:{c.end}]' for c in chunks)
    return '\n'.join(lines)
