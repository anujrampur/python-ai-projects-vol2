import unittest
from project72_retrieval_ranking import rank_chunks, tokenize

class TestProject72(unittest.TestCase):
    def test_relevant_chunk_ranks_first(self):
        got=rank_chunks(['cats and dogs','retrieval augmented generation uses retrieval'], 'retrieval generation')
        self.assertEqual(got[0]['index'],1)
    def test_tokenize_casefold(self): self.assertEqual(tokenize('RAG rag'),['rag','rag'])
    def test_empty_query(self):
        with self.assertRaises(ValueError): rank_chunks(['hello'],'!!!')

if __name__ == "__main__": unittest.main()
