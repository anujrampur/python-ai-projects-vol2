"""Project 83: Route visual questions to an injected VQA model adapter."""
from dataclasses import dataclass

@dataclass(frozen=True)
class VisualQuestion:
    image_path: str
    question: str

def prepare_question(image_path: str, question: str) -> VisualQuestion:
    path, prompt = image_path.strip(), question.strip()
    if not path: raise ValueError('image_path must not be blank')
    if not prompt: raise ValueError('question must not be blank')
    if len(prompt) > 1000: raise ValueError('question must be at most 1000 characters')
    return VisualQuestion(path, prompt)

def answer_visual_question(request: VisualQuestion, model_adapter=None) -> str:
    if model_adapter is None: raise RuntimeError('No VQA model configured; supply a model_adapter callable.')
    answer = model_adapter(request.image_path, request.question)
    if not isinstance(answer, str) or not answer.strip(): raise ValueError('Model adapter returned an empty or invalid answer')
    return answer.strip()
