import unittest
from project56_paraphraser import paraphrase
class TestParaphraser(unittest.TestCase):
 def test_simplifies_known_phrase(self): self.assertEqual(paraphrase("We make use of tools."), "We use tools.")
 def test_case_insensitive(self): self.assertEqual(paraphrase("IN ORDER TO learn"), "to learn")
 def test_blank_rejected(self):
  with self.assertRaises(ValueError): paraphrase("  ")
 def test_non_string_rejected(self):
  with self.assertRaises(ValueError): paraphrase(None)
if __name__ == '__main__': unittest.main()
