import unittest
from project59_meeting_action_items import extract_action_items
class TestActionItems(unittest.TestCase):
 def test_extracts_owner_and_due(self):
  items=extract_action_items("Anuj: Send the report by Friday. Team will review results.")
  self.assertEqual(len(items), 2)
  self.assertEqual(items[0].owner, "Anuj")
  self.assertEqual(items[0].due, "by Friday")
 def test_no_actions(self): self.assertEqual(extract_action_items("We discussed last week's progress."), [])
 def test_deduplicates(self): self.assertEqual(len(extract_action_items("Send report. Send report.")), 1)
 def test_empty_rejected(self):
  with self.assertRaises(ValueError): extract_action_items("")
if __name__ == '__main__': unittest.main()
