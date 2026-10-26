import unittest
from project79_voice_transcript_cleaner import clean_transcript
class T(unittest.TestCase):
 def test_spaces(self): self.assertEqual(clean_transcript('  hello   world '),'hello world')
 def test_punctuation(self): self.assertEqual(clean_transcript('Hi ,there!yes'),'Hi, there! yes')
 def test_type(self):
  with self.assertRaises(TypeError): clean_transcript(None)
if __name__=='__main__': unittest.main()
