"""Unit tests for Project 51."""
import random
import unittest

from project51_generator import available_languages, available_types, generate_items


class TestGenerator(unittest.TestCase):
    def test_supported_languages_and_types(self):
        self.assertEqual(available_languages(), ("en", "hi"))
        self.assertEqual(available_types(), ("joke", "shayari", "quote"))

    def test_returns_requested_number_of_items(self):
        for kind in available_types():
            for language in available_languages():
                with self.subTest(kind=kind, language=language):
                    result = generate_items(kind, language, 3, rng=random.Random(1))
                    self.assertEqual(len(result), 3)
                    self.assertTrue(all(isinstance(item, str) and item for item in result))

    def test_normalizes_case_and_whitespace(self):
        result = generate_items(" QUOTE ", " EN ", 1, rng=random.Random(2))
        self.assertEqual(len(result), 1)

    def test_rejects_unknown_language(self):
        with self.assertRaises(ValueError):
            generate_items("quote", "fr")

    def test_rejects_unknown_type(self):
        with self.assertRaises(ValueError):
            generate_items("poem", "en")

    def test_rejects_invalid_count(self):
        for count in (0, 6, -1, 1.5, True, "2"):
            with self.subTest(count=count):
                with self.assertRaises(ValueError):
                    generate_items("quote", "en", count)  # type: ignore[arg-type]


if __name__ == "__main__":
    unittest.main()
