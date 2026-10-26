import unittest
from project52_dictionary import explain_eli15, explain_word

class TestDictionary(unittest.TestCase):
    def test_known_word_case_insensitive(self):
        self.assertEqual(explain_word(" Curiosity ").hindi, "जिज्ञासा")
    def test_example_present(self):
        self.assertIn("data", explain_word("analyze").example)
    def test_eli15_output(self):
        self.assertIn("In simple words", explain_eli15(explain_word("concise")))
    def test_blank_word_rejected(self):
        with self.assertRaises(ValueError): explain_word("  ")
    def test_unknown_word_rejected(self):
        with self.assertRaises(ValueError): explain_word("unlistedword")

if __name__ == "__main__": unittest.main()
