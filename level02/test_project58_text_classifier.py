import unittest
from project58_text_classifier import classify_text
class TestTextClassifier(unittest.TestCase):
 def test_spam_evidence(self):
  r=classify_text("Urgent! Claim your free prize")
  self.assertEqual(r["spam_label"], "spam")
  self.assertIn("prize", r["spam_evidence"])
 def test_ham_uncertain(self): self.assertEqual(classify_text("Could we meet tomorrow?")["spam_label"], "ham/uncertain")
 def test_topic(self): self.assertEqual(classify_text("The teacher helps every student learn")["topic"], "education")
 def test_empty_rejected(self):
  with self.assertRaises(ValueError): classify_text(" ")
if __name__ == '__main__': unittest.main()
