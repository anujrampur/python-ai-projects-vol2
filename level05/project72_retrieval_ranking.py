"""Rank pre-chunked text snippets with transparent keyword overlap."""
import re

def tokenize(text): return re.findall(r"[\w'-]+",text.casefold())

def rank_chunks(chunks, query, top_k=3):
    q=set(tokenize(query))
    if not q: raise ValueError('Query must contain searchable words.')
    if isinstance(top_k,bool) or not isinstance(top_k,int) or top_k<1: raise ValueError('top_k must be a positive integer.')
    ranked=[]
    for i,chunk in enumerate(chunks):
        words=tokenize(chunk); overlap=sum(1 for w in words if w in q)
        score=overlap/max(len(words),1)
        if overlap: ranked.append({'index':i,'score':round(score,4),'text':chunk})
    return sorted(ranked,key=lambda x:(-x['score'],x['index']))[:top_k]
