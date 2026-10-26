import unittest
from project69_research_paper_summarizer import summarize_paper

class TestProject69(unittest.TestCase):
    def test_extracts_named_sections(self):
        result=summarize_paper('Abstract\nWe studied a sample.\nMethods\nWe used a survey.\nResults\nScores improved.\nConclusion\nMore work is needed.')
        self.assertIn('We studied', result['abstract_or_overview'])
        self.assertIn('survey', result['methods'])
    def test_empty_rejected(self):
        with self.assertRaises(ValueError): summarize_paper('')

if __name__ == '__main__': unittest.main()
