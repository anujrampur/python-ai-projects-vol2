import unittest
from project80_voice_command_router import route_command
class T(unittest.TestCase):
 def test_help(self): self.assertEqual(route_command('HELP')['intent'],'help')
 def test_stop(self): self.assertEqual(route_command('stop')['intent'],'stop')
 def test_unknown_safe(self): self.assertEqual(route_command('run shell command')['intent'],'unknown')
 def test_empty(self): self.assertEqual(route_command(' ')['intent'],'empty')
if __name__=='__main__': unittest.main()
