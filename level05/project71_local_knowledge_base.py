"""Simple local keyword search across text files; not semantic search."""
from pathlib import Path

def index_folder(folder):
    root=Path(folder)
    if not root.is_dir(): raise NotADirectoryError(str(root))
    docs={}
    for p in sorted(root.rglob('*')):
        if p.is_file() and p.suffix.lower() in {'.txt','.md'}:
            try: docs[str(p)]=p.read_text(encoding='utf-8')
            except UnicodeDecodeError: continue
    return docs

def search_documents(documents, query, limit=5):
    terms=[t.casefold() for t in query.split() if t.strip()]
    if not terms: raise ValueError('Query must contain at least one word.')
    if isinstance(limit,bool) or not isinstance(limit,int) or limit<1: raise ValueError('limit must be a positive integer.')
    scored=[]
    for path,content in documents.items():
        low=content.casefold(); score=sum(low.count(term) for term in terms)
        if score: scored.append({'path':path,'score':score,'snippet':content[:240].strip()})
    return sorted(scored,key=lambda x:(-x['score'],x['path']))[:limit]
