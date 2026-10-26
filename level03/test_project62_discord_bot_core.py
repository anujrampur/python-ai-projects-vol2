import unittest
from project62_discord_bot_core import handle_command
class T(unittest.TestCase):
 def test_ping(self): self.assertEqual(handle_command("!ping"),"Pong!")
 def test_normal_message_ignored(self): self.assertIsNone(handle_command("hello"))
 def test_unknown_command(self): self.assertIn("Unknown",handle_command("!xyz"))
 def test_non_string(self):
  with self.assertRaises(ValueError): handle_command(None)
if __name__=='__main__': unittest.main()
