"""Create a structured, extractive summary from pasted paper text.

This offline baseline does not infer findings beyond the supplied text.
"""
import re


def summarize_paper(text: str) -> dict[str, str]:
    if not text.strip(): raise ValueError('Paper text cannot be empty.')
    sections={}
    # Recognize common section headings when the source contains them.
    pattern=re.compile(r'(?im)^\s*(abstract|introduction|methods?|methodology|results?|discussion|conclusion)\s*:?\s*$')
    matches=list(pattern.finditer(text))
    if matches:
        for idx,match in enumerate(matches):
            end=matches[idx+1].start() if idx+1<len(matches) else len(text)
            content=text[match.end():end].strip()
            key=match.group(1).lower()
            if content: sections[key]=content
    sentences=[s.strip() for s in re.split(r'(?<=[.!?])\s+', text.strip()) if s.strip()]
    def excerpt(names, fallback_index):
        for name in names:
            if name in sections:
                return ' '.join(sections[name].split())[:700]
        return sentences[fallback_index][:500] if len(sentences)>fallback_index else 'Not identified in supplied text.'
    return {
      'abstract_or_overview': excerpt(('abstract',),0),
      'methods': excerpt(('methods','method','methodology'),1),
      'results': excerpt(('results','result'),2),
      'conclusion': excerpt(('conclusion','discussion'),-1),
      'note': 'Extractive heuristic summary. Verify against the full paper; this tool does not validate scientific claims.'
    }
