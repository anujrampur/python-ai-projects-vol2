"""Project 83: Visual QA response validator. Actual image reasoning requires a vision model.
This module validates and formats a response and its evidence note; it does not answer image questions itself.
"""
def format_visual_answer(question: str, answer: str, confidence: float | None = None, evidence_note: str = "") -> dict:
    if not question.strip(): raise ValueError("question cannot be empty")
    if not answer.strip(): raise ValueError("answer cannot be empty")
    if confidence is not None and (isinstance(confidence, bool) or not isinstance(confidence, (int, float)) or not 0 <= confidence <= 1):
        raise ValueError("confidence must be a number between 0 and 1")
    return {"question": question.strip(), "answer": answer.strip(), "confidence": confidence,
            "evidence_note": evidence_note.strip(), "requires_visual_verification": True}
