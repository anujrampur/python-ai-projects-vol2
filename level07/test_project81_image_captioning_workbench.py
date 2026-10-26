import tempfile, unittest
from pathlib import Path
from project81_image_captioning_workbench import validate_image_path, format_caption
class Tests(unittest.TestCase):
 def test_caption_whitespace(self): self.assertEqual(format_caption("cat.jpg", "  A   cat "), "cat.jpg: A cat")
 def test_caption_truncates(self): self.assertTrue(format_caption("x.png", "abcdef", 3).endswith("…"))
 def test_empty_caption(self):
  with self.assertRaises(ValueError): format_caption("x.png", " ")
 def test_extension(self):
  with tempfile.TemporaryDirectory() as d:
   p=Path(d)/"a.txt"; p.write_text("x")
   with self.assertRaises(ValueError): validate_image_path(str(p))
 def test_missing_file(self):
  with self.assertRaises(FileNotFoundError): validate_image_path("not-a-real-image-82919.png")
if __name__ == '__main__': unittest.main()
