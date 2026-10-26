import tempfile, unittest
from pathlib import Path
from project84_document_image_analyzer import analyze_image_file
class Tests(unittest.TestCase):
 def test_metadata(self):
  with tempfile.TemporaryDirectory() as d:
   p=Path(d)/'a.png'; p.write_bytes(b'fake-image')
   result=analyze_image_file(str(p)); self.assertEqual(result['size_bytes'],10); self.assertEqual(len(result['sha256']),64)
 def test_missing(self):
  with self.assertRaises(FileNotFoundError): analyze_image_file('missing-9381.png')
 def test_bad_extension(self):
  with tempfile.TemporaryDirectory() as d:
   p=Path(d)/'a.txt'; p.write_text('x')
   with self.assertRaises(ValueError): analyze_image_file(str(p))
if __name__ == '__main__': unittest.main()
