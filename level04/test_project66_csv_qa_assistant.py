import unittest
from project66_csv_qa_assistant import answer_question, load_csv

class TestProject66(unittest.TestCase):
    def test_rows_and_columns(self):
        rows=[{'name':'A','score':'10'},{'name':'B','score':'20'}]
        self.assertIn('2 data rows', answer_question(rows,'how many rows?'))
        self.assertIn('name, score', answer_question(rows,'which columns?'))
    def test_average(self):
        self.assertIn('15.00', answer_question([{'score':'10'},{'score':'20'}],'average score'))
    def test_rejects_unsupported_question(self):
        with self.assertRaises(ValueError): answer_question([], 'tell me a secret')
    def test_load_missing_file(self):
        with self.assertRaises(FileNotFoundError): load_csv('definitely_missing_file.csv')

if __name__ == '__main__': unittest.main()
