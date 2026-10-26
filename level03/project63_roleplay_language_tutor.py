"""Project 63: Role-play English practice with supportive feedback heuristics."""
from __future__ import annotations

SCENARIOS={
    "cafe": {"prompt": "You are ordering a drink at a cafe. Ask for a tea politely.", "keywords": ("please", "tea", "could", "may")},
    "interview": {"prompt": "You are in a job interview. Introduce yourself in two sentences.", "keywords": ("i am", "my", "experience", "work", "name")},
    "travel": {"prompt": "You are at a train station. Ask where platform two is.", "keywords": ("platform", "where", "please", "station")},
}

def get_prompt(scenario: str) -> str:
    key=scenario.strip().lower()
    if key not in SCENARIOS:
        raise ValueError(f"Choose a scenario: {', '.join(SCENARIOS)}")
    return SCENARIOS[key]["prompt"]

def review_response(scenario: str, response: str) -> dict[str, object]:
    """Give lightweight vocabulary hints, not a formal language proficiency score."""
    key=scenario.strip().lower()
    if key not in SCENARIOS: raise ValueError(f"Choose a scenario: {', '.join(SCENARIOS)}")
    if not isinstance(response,str) or not response.strip(): raise ValueError("Please enter a practice response.")
    text=response.lower()
    matched=[term for term in SCENARIOS[key]["keywords"] if term in text]
    tips=[]
    if len(response.split()) < 4: tips.append("Try adding one more detail to make your answer clearer.")
    if "please" not in text and key in {"cafe","travel"}: tips.append("Consider adding 'please' for a more polite request.")
    if not tips: tips.append("Good effort. Read your answer aloud and check that it sounds natural.")
    return {"scenario": key, "matched_hints": matched, "tips": tips,
            "disclaimer": "Practice hints only; this is not an automated grammar or proficiency assessment."}

if __name__ == "__main__":
    scenario=input("Scenario (cafe/interview/travel): ")
    try:
        print(get_prompt(scenario)); response=input("Your response: ")
        print(review_response(scenario,response))
    except ValueError as exc: print(exc)
