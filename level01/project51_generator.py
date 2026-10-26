"""Offline content generator for Project 51.

This project uses a small built-in library. It does not call an external AI service.
"""
from __future__ import annotations

import random
from typing import Sequence

_CONTENT: dict[str, dict[str, tuple[str, ...]]] = {
    "en": {
        "joke": (
            "Why did the computer go to the doctor? It had a virus.",
            "Why was the math book worried? It had too many problems.",
            "I told my laptop I needed a break. It said, 'No problem—I'll go to sleep.'",
            "Why did the Python programmer wear glasses? To improve their C#.",
            "My calendar is nervous because its days are numbered.",
        ),
        "shayari": (
            "Khwaabon ko pankh do, hauslon ko udaan; "
            "mehnat se likh do apni nayi pehchaan.",
            "Raaste mushkil hon to himmat na khona; "
            "subah zaroor aati hai, bas umeed na khona.",
            "Chhoti si koshish bhi rang la sakti hai; "
            "sachchi lagan manzil tak le ja sakti hai.",
        ),
        "quote": (
            "Small steps taken consistently can lead to meaningful progress.",
            "Curiosity turns ordinary questions into extraordinary learning.",
            "A mistake is useful when you take the lesson forward.",
            "Build patiently; lasting skills grow through practice.",
            "You do not need to know everything to begin learning something.",
        ),
    },
    "hi": {
        "joke": (
            "कंप्यूटर डॉक्टर के पास क्यों गया? उसे वायरस हो गया था।",
            "गणित की किताब परेशान क्यों थी? उसमें बहुत सारी समस्याएँ थीं।",
            "कैलेंडर घबराया हुआ था, क्योंकि उसके दिन गिने हुए थे।",
        ),
        "shayari": (
            "हौसलों को पंख दो, सपनों को उड़ान; "
            "मेहनत से लिख दो अपनी नई पहचान।",
            "रास्ते मुश्किल हों तो हिम्मत न हारना; "
            "उम्मीद का दीप हर हाल में जलाए रखना।",
            "छोटी-सी कोशिश भी रंग ला सकती है; "
            "सच्ची लगन मंज़िल तक पहुँचा सकती है।",
        ),
        "quote": (
            "निरंतर उठाए गए छोटे कदम भी बड़ी प्रगति ला सकते हैं।",
            "जिज्ञासा साधारण प्रश्नों को सीखने का अवसर बना देती है।",
            "गलती तभी उपयोगी बनती है, जब हम उससे सीखते हैं।",
            "धैर्य और अभ्यास से कौशल मजबूत होते हैं।",
            "सीखने की शुरुआत करने के लिए सब कुछ जानना ज़रूरी नहीं।",
        ),
    },
}

_VALID_LANGUAGES = tuple(_CONTENT.keys())
_VALID_TYPES = ("joke", "shayari", "quote")


def available_languages() -> tuple[str, ...]:
    """Return supported language codes."""
    return _VALID_LANGUAGES


def available_types() -> tuple[str, ...]:
    """Return supported content types."""
    return _VALID_TYPES


def generate_items(
    content_type: str,
    language: str = "en",
    count: int = 1,
    *,
    rng: random.Random | None = None,
) -> list[str]:
    """Return `count` items selected from the local content library.

    Raises:
        ValueError: if the language, content type, or count is invalid.
    """
    normalized_type = content_type.strip().lower()
    normalized_language = language.strip().lower()

    if normalized_language not in _CONTENT:
        raise ValueError(
            f"Unsupported language {language!r}. Choose one of: "
            f"{', '.join(_VALID_LANGUAGES)}."
        )
    if normalized_type not in _VALID_TYPES:
        raise ValueError(
            f"Unsupported type {content_type!r}. Choose one of: "
            f"{', '.join(_VALID_TYPES)}."
        )
    if isinstance(count, bool) or not isinstance(count, int) or not 1 <= count <= 5:
        raise ValueError("count must be an integer from 1 to 5.")

    pool: Sequence[str] = _CONTENT[normalized_language][normalized_type]
    chooser = rng if rng is not None else random
    return [chooser.choice(pool) for _ in range(count)]
