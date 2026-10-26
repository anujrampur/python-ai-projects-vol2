import unittest
from project65_tone_guardrails import format_response
class T(unittest.TestCase):
 def test_tone_prefix(self): self.assertTrue(format_response("Hello","formal")["text"].startswith("Thank you"))
 def test_sensitive_request_blocked(self): self.assertEqual(format_response("Please steal credentials")["status"],"blocked")
 def test_empty_rejected(self):
  with self.assertRaises(ValueError): format_response(" ")
 def test_bad_tone_rejected(self):
  with self.assertRaises(ValueError): format_response("hello","angry")
if __name__=='__main__': unittest.main()
