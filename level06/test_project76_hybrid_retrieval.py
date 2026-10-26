import unittest
from project76_hybrid_retrieval import hybrid_search
class T(unittest.TestCase):
 def test_keyword(self): self.assertEqual(hybrid_search('python',[{'id':'a','text':'python guide'}])[0]['lexical_score'],1)
 def test_vector(self): self.assertEqual(hybrid_search('x',[{'id':'a','text':'no match'},{'id':'b','text':'x'}],{'a':1},.2)[0]['id'],'a')
 def test_bad_weight(self):
  with self.assertRaises(ValueError): hybrid_search('x',[],lexical_weight=2)
 def test_bad_k(self):
  with self.assertRaises(ValueError): hybrid_search('x',[],top_k=0)
if __name__=='__main__': unittest.main()
