import unittest
from project61_whatsapp_style_bot import create_reply
class T(unittest.TestCase):
 def test_greeting(self): self.assertIn("Hello",create_reply("hi"))
 def test_help(self): self.assertIn("help",create_reply("help"))
 def test_empty(self):
  with self.assertRaises(ValueError): create_reply(" ")
 def test_too_long(self):
  with self.assertRaises(ValueError): create_reply("x"*4001)
if __name__=='__main__': unittest.main()
