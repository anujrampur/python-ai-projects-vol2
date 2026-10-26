"""Project 77: Extractive query-relevant sentence selector."""
import re

def compress_context(query, passages, max_sentences=5):
    if isinstance(max_sentences,bool) or not isinstance(max_sentences,int) or max_sentences<1: raise ValueError('max_sentences must be positive')
    tok=lambda s:{x.casefold() for x in re.findall(r'[A-Za-z0-9]+|[\u0900-\u097f]+',s)}
    q=tok(query); candidates=[]
    for pi,p in enumerate(passages):
        for si,s in enumerate(re.split(r'(?<=[.!?।])\s+',p.strip())):
            if s.strip():
                overlap = len(q & tok(s))
                if overlap:
                    candidates.append((overlap/max(len(q),1),pi,si,s.strip()))
    chosen=sorted(sorted(candidates,key=lambda x:(-x[0],x[1],x[2]))[:max_sentences],key=lambda x:(x[1],x[2]))
    return [x[3] for x in chosen]
