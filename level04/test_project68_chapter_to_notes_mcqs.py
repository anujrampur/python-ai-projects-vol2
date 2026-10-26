import unittest
from project68_chapter_to_notes_mcqs import make_notes, make_mcqs, split_sentences

class TestProject68(unittest.TestCase):
    def test_split_sentences(self):
        self.assertEqual(len(split_sentences('One. Two!')), 2)
    def test_notes_nonempty(self):
        self.assertTrue(make_notes('This is a longer sentence for study. Another useful sentence follows.'))
    def test_mcq_count_validation(self):
        with self.assertRaises(ValueError): make_mcqs('A sentence is long enough here.', 0)

if __name__ == '__main__': unittest.main()
