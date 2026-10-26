import unittest
from project73_citation_aware_answer import draft_answer

class TestProject73(unittest.TestCase):
    def test_includes_matching_citation(self):
        out=draft_answer('What is retrieval?', [{'id':'S1','text':'Retrieval finds relevant documents.'}])
        self.assertEqual(out['citations'],['S1'])
    def test_no_match_is_explicit(self):
        out=draft_answer('quantum physics', [{'id':'S1','text':'A recipe for soup.'}])
        self.assertEqual(out['citations'],[])
    def test_question_required(self):
        with self.assertRaises(ValueError): draft_answer(' ',[])

if __name__ == "__main__": unittest.main()
