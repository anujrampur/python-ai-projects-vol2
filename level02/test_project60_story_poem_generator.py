import random
import unittest
from project60_story_poem_generator import generate_poem, generate_story
class TestStoryPoemGenerator(unittest.TestCase):
 def test_story_fills_fields(self):
  s=generate_story("kindness", "Mira", "the park", "a red kite", rng=random.Random(1))
  self.assertIn("Mira", s); self.assertIn("the park", s); self.assertIn("a red kite", s)
 def test_poem_has_lines(self): self.assertIn("\\n", repr(generate_poem("hope", rng=random.Random(1))))
 def test_unknown_theme_rejected(self):
  with self.assertRaises(ValueError): generate_poem("mystery")
 def test_empty_story_field_rejected(self):
  with self.assertRaises(ValueError): generate_story(hero="", rng=random.Random(1))
if __name__ == '__main__': unittest.main()
