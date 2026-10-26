import unittest
from project78_rag_answer_auditor import audit_answer
class T(unittest.TestCase):
 def test_match(self): self.assertEqual(audit_answer('Solar panels use sunlight.',{'S1':'Solar panels use sunlight.'})['sentences'][0]['candidate_sources'],['S1'])
 def test_flag(self): self.assertTrue(audit_answer('Whales sing quantum songs.',{'S':'Solar panels use sunlight.'})['sentences'][0]['needs_review'])
 def test_empty_sources(self):
  with self.assertRaises(ValueError): audit_answer('hello',{})
if __name__=='__main__': unittest.main()
