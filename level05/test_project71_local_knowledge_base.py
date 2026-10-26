import unittest
from project71_local_knowledge_base import index_folder, search_documents

class TestProject71(unittest.TestCase):
    def test_ranks_match(self):
        docs={'a':'apple apple pear','b':'apple'}
        self.assertEqual(search_documents(docs,'apple')[0]['path'],'a')
    def test_empty_query(self):
        with self.assertRaises(ValueError): search_documents({},' ')
    def test_limit_validation(self):
        with self.assertRaises(ValueError): search_documents({},'x',0)

if __name__ == "__main__": unittest.main()
