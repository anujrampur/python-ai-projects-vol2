import unittest
from project83_visual_question_answering import format_visual_answer
class Tests(unittest.TestCase):
 def test_formats_answer(self): self.assertTrue(format_visual_answer("What?", "A dog")['requires_visual_verification'])
 def test_strips_text(self): self.assertEqual(format_visual_answer(" Q ", " A ")['question'], 'Q')
 def test_empty_question(self):
  with self.assertRaises(ValueError): format_visual_answer(" ", "answer")
 def test_bad_confidence(self):
  with self.assertRaises(ValueError): format_visual_answer("Q", "A", 1.5)
if __name__ == '__main__': unittest.main()
