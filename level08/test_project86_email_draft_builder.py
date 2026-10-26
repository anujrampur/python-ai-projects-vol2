import unittest
from project86_email_draft_builder import build_draft
class TestEmailDraft(unittest.TestCase):
 def test_builds_subject_and_points(self):
  d=build_draft('Team','the meeting',['Share agenda'])
  self.assertIn('meeting',d.subject); self.assertIn('Share agenda',d.body)
 def test_tone(self): self.assertTrue(build_draft('A','update',['Done'],'friendly').body.startswith('Hi A,'))
 def test_missing_required(self):
  with self.assertRaises(ValueError): build_draft('','update',['x'])
 def test_invalid_tone(self):
  with self.assertRaises(ValueError): build_draft('A','update',['x'],'angry')
 def test_empty_points(self):
  with self.assertRaises(ValueError): build_draft('A','update',[])
if __name__=='__main__': unittest.main()
