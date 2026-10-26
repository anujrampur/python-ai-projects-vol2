import unittest
from project67_document_explainer import explain_document, read_document

class TestProject67(unittest.TestCase):
    def test_flags_possible_obligations(self):
        result=explain_document('Payment must be completed within 30 days.')
        self.assertTrue(result['possible_obligation_lines'])
    def test_empty_text_rejected(self):
        with self.assertRaises(ValueError): explain_document('  ')
    def test_unsupported_extension_rejected(self):
        with self.assertRaises(ValueError): read_document('contract.pdf')

if __name__ == '__main__': unittest.main()
