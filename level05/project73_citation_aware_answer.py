"""Draft a grounded extractive response with source IDs attached."""

def draft_answer(question, sources, max_sources=3):
    if not question.strip(): raise ValueError('Question cannot be empty.')
    if isinstance(max_sources,bool) or not isinstance(max_sources,int) or max_sources<1: raise ValueError('max_sources must be positive.')
    selected=[]
    terms={w.casefold().strip('.,?!:;') for w in question.split() if len(w)>2}
    for source in sources:
        sid=str(source.get('id','')).strip(); text=str(source.get('text','')).strip()
        if not sid or not text: continue
        score=sum(1 for w in text.casefold().split() if w.strip('.,?!:;') in terms)
        if score: selected.append((score,sid,text))
    selected.sort(key=lambda x:(-x[0],x[1]))
    if not selected: return {'answer':'No matching source text was found. Do not infer an answer.','citations':[]}
    selected=selected[:max_sources]
    return {'answer':' '.join(f'[{sid}] {text}' for _,sid,text in selected),'citations':[sid for _,sid,_ in selected], 'note':'Extractive draft; verify every citation against the original source.'}
