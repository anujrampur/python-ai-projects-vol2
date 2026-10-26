"""Project 79: Clean text transcripts; does not perform speech recognition."""
import re

def clean_transcript(text, remove_fillers=False):
    if not isinstance(text,str): raise TypeError('text must be a string')
    text=text.replace('\r\n','\n').replace('\r','\n')
    lines=[]
    for line in text.split('\n'):
        line=re.sub(r'[ \t]+',' ',line).strip()
        if remove_fillers:
            line=re.sub(r'\b(um+|uh+|erm+|you know)\b','',line,flags=re.I)
            line=re.sub(r'\s+([,.!?;:])',r'\1',line); line=re.sub(r' {2,}',' ',line).strip()
        line=re.sub(r'\s+([,.!?;:])',r'\1',line); line=re.sub(r'([,.!?])(?=\S)',r'\1 ',line)
        lines.append(line)
    return '\n'.join(lines).strip()
