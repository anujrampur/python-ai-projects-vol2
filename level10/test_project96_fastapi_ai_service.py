"""Offline regression tests for Project 96."""
import unittest
from project96_fastapi_ai_service import (
    MAX_PROMPT_LENGTH, GenerateResponse, generate_demo, validate_request,
)


class FastAPIServiceTests(unittest.TestCase):
    def test_valid_prompt_is_trimmed(self):
        self.assertEqual(validate_request({"prompt": "  hello  "}).prompt, "hello")

    def test_non_object_rejected(self):
        for payload in (None, "hello", [], 3):
            with self.subTest(payload=payload), self.assertRaises(ValueError):
                validate_request(payload)

    def test_missing_or_non_string_prompt_rejected(self):
        for payload in ({}, {"prompt": 5}, {"prompt": None}, {"prompt": True}):
            with self.subTest(payload=payload), self.assertRaises(ValueError):
                validate_request(payload)

    def test_empty_prompt_rejected(self):
        for prompt in ("", "  \t\n"):
            with self.subTest(prompt=repr(prompt)), self.assertRaises(ValueError):
                validate_request({"prompt": prompt})

    def test_oversized_prompt_rejected(self):
        with self.assertRaises(ValueError):
            validate_request({"prompt": "x" * (MAX_PROMPT_LENGTH + 1)})

    def test_maximum_length_prompt_is_accepted(self):
        self.assertEqual(len(validate_request({"prompt": "x" * MAX_PROMPT_LENGTH}).prompt), MAX_PROMPT_LENGTH)

    def test_demo_does_not_claim_real_model(self):
        result = generate_demo("hello")
        self.assertIsInstance(result, GenerateResponse)
        self.assertEqual(result.model, "demo-template")
        self.assertIn("5 characters", result.text)

    def test_demo_validates_direct_input(self):
        for prompt in (None, "  ", "x" * (MAX_PROMPT_LENGTH + 1)):
            with self.subTest(prompt_type=type(prompt).__name__), self.assertRaises(ValueError):
                generate_demo(prompt)


if __name__ == "__main__":
    unittest.main()
