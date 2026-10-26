import unittest
from project57_keyword_hashtag_extractor import extract_keywords, make_hashtags
class TestKeywordExtractor(unittest.TestCase):
 def test_frequency_order(self): self.assertEqual(extract_keywords("Python code, Python data, code", 3), ["python", "code", "data"])
 def test_stopwords_ignored(self): self.assertEqual(extract_keywords("the and if"), [])
 def test_hashtags_cleaned_and_unique(self): self.assertEqual(make_hashtags(["python", "data science", "python"]), ["#python", "#datascience"])
 def test_invalid_limit(self):
  with self.assertRaises(ValueError): extract_keywords("hello", 0)
if __name__ == '__main__': unittest.main()
