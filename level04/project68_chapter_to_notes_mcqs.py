"""Turn a supplied chapter text into extractive notes and simple MCQs.

No generative model is used: summaries are sentence-selection heuristics.
"""
import re


def split_sentences(text: str) -> list[str]:
    return [s.strip() for s in re.split(r'(?<=[.!?।])\s+', text.strip()) if s.strip()]


def make_notes(text: str, max_sentences: int = 5) -> list[str]:
    if not text.strip(): raise ValueError('Chapter text cannot be empty.')
    if isinstance(max_sentences, bool) or not isinstance(max_sentences, int) or max_sentences < 1:
        raise ValueError('max_sentences must be a positive integer.')
    sentences=split_sentences(text)
    # Transparent baseline: select longer sentences first, preserve source order in output.
    chosen=set(sorted(range(len(sentences)), key=lambda i: len(sentences[i]), reverse=True)[:max_sentences])
    return [f'- {s}' for i,s in enumerate(sentences) if i in chosen]


def make_mcqs(text: str, count: int = 3) -> list[dict[str, str]]:
    if isinstance(count, bool) or not isinstance(count, int) or not 1 <= count <= 10:
        raise ValueError('count must be an integer from 1 to 10.')
    sentences=split_sentences(text)
    candidates=[s for s in sentences if len(s.split()) >= 5]
    questions=[]
    for i,sentence in enumerate(candidates[:count], start=1):
        words=sentence.split()
        answer=' '.join(words[:min(4,len(words))]).strip(' ,:;')
        questions.append({'question': f'Which phrase begins statement {i}?', 'answer': answer, 'source_sentence': sentence})
    return questions
