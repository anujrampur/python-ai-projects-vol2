import unittest
from datetime import datetime, timezone
from project64_reflection_journal import create_entry
class T(unittest.TestCase):
 def test_entry(self):
  e=create_entry("calm","I took a walk",now=datetime(2026,1,1,tzinfo=timezone.utc))
  self.assertEqual(e.mood,"calm"); self.assertIn("T",e.created_at)
 def test_empty_reflection(self):
  with self.assertRaises(ValueError): create_entry("okay"," ")
 def test_naive_datetime_rejected(self):
  with self.assertRaises(ValueError): create_entry("okay","fine",now=datetime(2026,1,1))
 def test_empty_mood(self):
  with self.assertRaises(ValueError): create_entry(" ","fine")
if __name__=='__main__': unittest.main()
