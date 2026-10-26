"""Project 60: Template-based story and poem generator (offline, no LLM)."""
from __future__ import annotations
import random

_STORY_TEMPLATES = {
    "adventure": [
        "One morning, {hero} discovered a {object} near {place}. Instead of giving up, {hero} asked questions, followed the clues, and found that courage grows when we help others. By sunset, the mystery was solved and the whole village celebrated.",
        "When {hero} reached {place}, a strange {object} began to glow. Each clue demanded patience, teamwork, and one brave choice. At last, {hero} learned that the real treasure was the people who stood together.",
    ],
    "kindness": [
        "At {place}, {hero} noticed a lonely traveler holding a {object}. A small act of kindness turned into a friendship, and soon others joined in. The day reminded everyone that generosity can begin with one simple question: 'How can I help?'",
    ],
}
_POEMS = {
    "hope": [
        "When quiet skies are turning grey,\nA little hope can light the way.\nTake one small step, then try once more;\nNew chances wait beyond the door.",
        "A seed may sleep beneath the snow,\nYet roots are learning how to grow.\nBe patient through the longest night;\nThe dawn will bring a softer light.",
    ],
    "learning": [
        "Ask a question, test an idea,\nMake the difficult a little clearer.\nEvery error helps you see\nWhat your next step ought to be.",
    ],
}


def generate_story(theme: str = "adventure", hero: str = "A curious learner",
                   place: str = "an old library", object_name: str = "silver key",
                   *, rng: random.Random | None = None) -> str:
    """Fill a short story template with user-provided safe plain-text details."""
    if theme not in _STORY_TEMPLATES:
        raise ValueError(f"Unknown story theme. Choose: {', '.join(_STORY_TEMPLATES)}")
    values=(hero, place, object_name)
    if any(not isinstance(v,str) or not v.strip() or len(v)>80 for v in values):
        raise ValueError("Hero, place, and object must be non-empty strings of at most 80 characters.")
    chooser=rng if rng is not None else random
    template=chooser.choice(_STORY_TEMPLATES[theme])
    return template.format(hero=hero.strip(), place=place.strip(), object=object_name.strip())


def generate_poem(theme: str = "hope", *, rng: random.Random | None = None) -> str:
    """Return an original short poem from the built-in template collection."""
    if theme not in _POEMS:
        raise ValueError(f"Unknown poem theme. Choose: {', '.join(_POEMS)}")
    chooser=rng if rng is not None else random
    return chooser.choice(_POEMS[theme])


if __name__ == "__main__":
    print("Story & Poem Generator (offline template demo)")
    mode=input("Choose story or poem: ").strip().lower()
    try:
        if mode=="story":
            theme=input("Theme (adventure/kindness): ").strip().lower()
            hero=input("Hero: ").strip() or "A curious learner"
            place=input("Place: ").strip() or "an old library"
            obj=input("Object: ").strip() or "silver key"
            print("\n"+generate_story(theme,hero,place,obj))
        elif mode=="poem":
            print("\n"+generate_poem(input("Theme (hope/learning): ").strip().lower()))
        else: print("Choose 'story' or 'poem'.")
    except ValueError as exc: print(exc)
