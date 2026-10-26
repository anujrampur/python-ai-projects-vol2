import unittest
from project63_roleplay_language_tutor import get_prompt, review_response
class T(unittest.TestCase):
 def test_prompt(self): self.assertIn("cafe",get_prompt("CAFE").lower())
 def test_feedback(self): self.assertIn("matched_hints",review_response("cafe","Could I have tea please?"))
 def test_invalid_scenario(self):
  with self.assertRaises(ValueError): get_prompt("space")
 def test_empty_response(self):
  with self.assertRaises(ValueError): review_response("travel"," ")
if __name__=='__main__': unittest.main()
