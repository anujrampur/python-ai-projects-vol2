import json
import unittest
from project97_local_ollama_assistant import build_payload, chat, OllamaError

class OllamaAssistantTests(unittest.TestCase):
    def test_payload(self):
        self.assertEqual(build_payload(" hi ", " llama3.2 "), {"model": "llama3.2", "prompt": "hi", "stream": False})

    def test_empty_prompt_rejected(self):
        for value in (" ", None, 4):
            with self.subTest(value=value), self.assertRaises(ValueError):
                build_payload(value)

    def test_empty_model_rejected(self):
        for value in (" ", None, 4):
            with self.subTest(value=value), self.assertRaises(ValueError):
                build_payload("question", value)

    def test_fake_transport(self):
        seen = {}
        def fake(url, body, timeout):
            seen.update(url=url, body=json.loads(body), timeout=timeout)
            return {"response": "local answer"}
        self.assertEqual(chat("question", transport=fake), "local answer")
        self.assertEqual(seen["url"], "http://127.0.0.1:11434/api/generate")
        self.assertEqual(seen["body"]["prompt"], "question")

    def test_bad_response_rejected(self):
        for result in ({"unexpected": "value"}, {"response": None}, [], None):
            with self.subTest(result=result), self.assertRaises(OllamaError):
                chat("question", transport=lambda *_: result)

    def test_bad_timeout_rejected(self):
        for value in (0, -1, True, float("inf"), float("nan"), "2"):
            with self.subTest(value=value), self.assertRaises(ValueError):
                chat("q", transport=lambda *_: {}, timeout=value)

    def test_bad_base_url_rejected(self):
        for value in ("", "  ", None, "localhost:11434", "file:///tmp"):
            with self.subTest(value=value), self.assertRaises(ValueError):
                chat("q", base_url=value, transport=lambda *_: {"response": "ok"})

    def test_trailing_slash_normalized(self):
        seen = {}
        def fake(url, body, timeout):
            seen["url"] = url
            return {"response": "ok"}
        chat("q", base_url="http://localhost:11434/", transport=fake)
        self.assertEqual(seen["url"], "http://localhost:11434/api/generate")

    def test_transport_error_wrapped(self):
        def fake(*_): raise OSError("offline")
        with self.assertRaises(OllamaError): chat("q", transport=fake)

if __name__ == "__main__":
    unittest.main()
