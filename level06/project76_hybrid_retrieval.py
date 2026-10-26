"""Project 76: Hybrid keyword + supplied vector-score retrieval prototype."""
import re

def terms(text):
    return {x.casefold() for x in re.findall(r"[A-Za-z0-9]+|[\u0900-\u097f]+", text)}

def hybrid_search(query, documents, vector_scores=None, lexical_weight=0.6, top_k=5):
    if not 0 <= lexical_weight <= 1: raise ValueError('lexical_weight must be between 0 and 1')
    if isinstance(top_k, bool) or not isinstance(top_k, int) or top_k < 1: raise ValueError('top_k must be a positive integer')
    vector_scores = vector_scores or {}; q = terms(query); out=[]
    for doc in documents:
        doc_id, text = doc['id'], doc['text']; d=terms(text)
        lexical = len(q & d) / len(q) if q else 0.0
        vector = float(vector_scores.get(doc_id, 0.0))
        if not 0 <= vector <= 1: raise ValueError('vector scores must be in [0, 1]')
        out.append({'id':doc_id,'text':text,'lexical_score':lexical,'vector_score':vector,'score':lexical_weight*lexical+(1-lexical_weight)*vector})
    return sorted(out, key=lambda x:(-x['score'], x['id']))[:top_k]
