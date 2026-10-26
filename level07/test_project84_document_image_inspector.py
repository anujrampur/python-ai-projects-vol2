import tempfile, unittest
from pathlib import Path
from project84_document_image_inspector import inspect_document_image
class TestDocumentImageInspector(unittest.TestCase):
    def setUp(self):
        self.tmp=tempfile.TemporaryDirectory(); self.addCleanup(self.tmp.cleanup)
        self.p=Path(self.tmp.name)/'scan_page.png'; self.p.write_bytes(b'image')
    def test_metadata(self):
        result=inspect_document_image(str(self.p)); self.assertEqual(result['filename'],'scan_page.png'); self.assertTrue(result['likely_scanned_document'])
    def test_missing(self):
        with self.assertRaises(FileNotFoundError): inspect_document_image(str(Path(self.tmp.name)/'none.png'))
    def test_wrong_extension(self):
        p=Path(self.tmp.name)/'file.txt'; p.write_text('x')
        with self.assertRaises(ValueError): inspect_document_image(str(p))
    def test_empty(self):
        p=Path(self.tmp.name)/'empty.png'; p.touch()
        with self.assertRaises(ValueError): inspect_document_image(str(p))
if __name__ == '__main__': unittest.main()
