import unittest
from project82_ocr_text_postprocessor import clean_ocr_text, extract_lines
class TestOCRPostprocessor(unittest.TestCase):
    def test_normalizes_spaces_and_newlines(self): self.assertEqual(clean_ocr_text(' A   B \r\n\n C '), 'A B\nC')
    def test_join_wrapped_lines(self): self.assertEqual(clean_ocr_text('A wrapped\nline continues.\nNext.', True), 'A wrapped line continues.\nNext.')
    def test_extract_min_length(self): self.assertEqual(extract_lines('a\nhello', 2), ['hello'])
    def test_bad_min_length(self):
        with self.assertRaises(ValueError): extract_lines('x', 0)
    def test_type_error(self):
        with self.assertRaises(TypeError): clean_ocr_text(None)
if __name__ == '__main__': unittest.main()
