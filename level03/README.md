# Level 3 — Chatbots with Memory (Projects 61–65)

These are local teaching cores. The WhatsApp and Discord projects do not connect to their platforms in this release; real deployment requires provider setup and current official documentation.

| No. | File | Scope | Run |
|---:|---|---|---|
| 61 | `project61_whatsapp_style_bot.py` | Provider-neutral message reply core | `python level03/project61_whatsapp_style_bot.py` |
| 62 | `project62_discord_bot_core.py` | Discord-style command handler | `python level03/project62_discord_bot_core.py` |
| 63 | `project63_roleplay_language_tutor.py` | Role-play prompts and lightweight feedback | `python level03/project63_roleplay_language_tutor.py` |
| 64 | `project64_reflection_journal.py` | Non-medical reflection entry model | `python level03/project64_reflection_journal.py` |
| 65 | `project65_tone_guardrails.py` | Tone formatting and simple blocked-marker demo | `python level03/project65_tone_guardrails.py` |

Run tests: `python -m unittest discover -s level03 -p 'test_*.py' -v`.

## Limitations and privacy
- Projects 61–62 do not send real messages or connect to external platforms. Never place API tokens in source control.
- Project 63 gives vocabulary hints only; it is not a reliable grammar or proficiency assessment.
- Project 64 does not provide medical or mental-health care and does not save entries automatically. Avoid storing sensitive journal data without a privacy and security design.
- Project 65 uses a tiny list of blocked phrases; it is not comprehensive safety moderation. Human review remains necessary.
