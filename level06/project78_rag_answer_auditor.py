"""Project 78: Heuristic source-overlap auditor; not factual verification."""
import re

def audit_answer(answer, sources):
    if not sources: raise ValueError('provide at least one source')
    terms=lambda s:{x.casefold() for x in re.findall(r'[A-Za-z0-9]+|[\u0900-\u097f]+',s) if len(x)>1}
    source_terms={k:terms(v) for k,v in sources.items()}
    sentences=[s.strip() for s in re.split(r'(?<=[.!?।])\s+',answer.strip()) if s.strip()]
    items=[]
    for sentence in sentences:
        matches=[k for k,v in source_terms.items() if terms(sentence)&v]
        items.append({'sentence':sentence,'candidate_sources':matches,'needs_review':not bool(matches)})
    return {'sentences':items,'needs_review_count':sum(x['needs_review'] for x in items),'notice':'Token overlap is a heuristic, not proof of factual support.'}
