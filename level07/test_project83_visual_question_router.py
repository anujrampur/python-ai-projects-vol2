import unittest
from project83_visual_question_router import prepare_question, answer_visual_question
class TestVQA(unittest.TestCase):
    def test_prepare(self): self.assertEqual(prepare_question(' a.png ', ' What is shown? ').question, 'What is shown?')
    def test_blank_image(self):
        with self.assertRaises(ValueError): prepare_question(' ', 'question')
    def test_blank_question(self):
        with self.assertRaises(ValueError): prepare_question('a.png', ' ')
    def test_question_length(self):
        with self.assertRaises(ValueError): prepare_question('a.png', 'x'*1001)
    def test_adapter(self):
        req=prepare_question('a.png','What?')
        self.assertEqual(answer_visual_question(req, lambda p,q:' A cup. '), 'A cup.')
        with self.assertRaises(RuntimeError): answer_visual_question(req)
if __name__ == '__main__': unittest.main()
