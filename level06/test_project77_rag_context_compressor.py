import unittest
from project77_rag_context_compressor import compress_context
class T(unittest.TestCase):
 def test_relevance(self): self.assertIn('Solar uses sunlight.',compress_context('solar sunlight',['Cats sleep. Solar uses sunlight.']))
 def test_limit(self): self.assertEqual(len(compress_context('x',['x. x. x.'],2)),2)
 def test_unrelated_sentences_are_excluded(self): self.assertEqual(compress_context('solar',['Cats sleep. Dogs run.']),[])
 def test_invalid(self):
  with self.assertRaises(ValueError): compress_context('x',[],0)
if __name__=='__main__': unittest.main()
