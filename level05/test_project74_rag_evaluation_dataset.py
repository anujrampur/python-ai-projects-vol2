import unittest
from project74_rag_evaluation_dataset import validate_dataset, recall_at_k

class TestProject74(unittest.TestCase):
    def test_valid_dataset(self): self.assertEqual(validate_dataset([{'question':'Q?','expected_source_ids':['S1']}]),[])
    def test_invalid_dataset(self): self.assertTrue(validate_dataset([{'question':'','expected_source_ids':'S1'}]))
    def test_recall(self): self.assertEqual(recall_at_k(['a','b'],['b','x','a'],3),1.0)
    def test_empty_expected_set_is_undefined(self): self.assertIsNone(recall_at_k([], ['a'], 1))
    def test_invalid_k(self):
        for k in (0, -1, True, 1.5):
            with self.subTest(k=k), self.assertRaises(ValueError): recall_at_k(['a'], ['a'], k)

if __name__ == "__main__": unittest.main()
