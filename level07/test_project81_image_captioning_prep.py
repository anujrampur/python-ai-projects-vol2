import tempfile, unittest
from pathlib import Path
from project81_image_captioning_prep import prepare_image_request, caption_with_model

class TestImageCaptionPrep(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory(); self.addCleanup(self.tmp.cleanup)
        self.img = Path(self.tmp.name) / 'sample.PNG'; self.img.write_bytes(b'fake image bytes')
    def test_prepares_supported_file(self):
        req = prepare_image_request(str(self.img)); self.assertTrue(Path(req.path).is_absolute())
    def test_missing_file(self):
        with self.assertRaises(FileNotFoundError): prepare_image_request(str(Path(self.tmp.name)/'missing.jpg'))
    def test_unsupported_suffix(self):
        p = Path(self.tmp.name)/'notes.txt'; p.write_text('x')
        with self.assertRaises(ValueError): prepare_image_request(str(p))
    def test_empty_file(self):
        p = Path(self.tmp.name)/'empty.png'; p.touch()
        with self.assertRaises(ValueError): prepare_image_request(str(p))
    def test_adapter_and_missing_model(self):
        req = prepare_image_request(str(self.img))
        with self.assertRaises(RuntimeError): caption_with_model(req)
        self.assertEqual(caption_with_model(req, lambda p, i: 'A sample image.'), 'A sample image.')
if __name__ == '__main__': unittest.main()
