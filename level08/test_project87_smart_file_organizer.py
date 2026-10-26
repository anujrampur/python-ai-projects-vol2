import unittest
from project87_smart_file_organizer import plan_moves
class TestFilePlan(unittest.TestCase):
 def test_extension_folder(self): self.assertTrue(plan_moves(['docs/report.PDF'])[0]['destination'].endswith('pdf/report.PDF'))
 def test_no_extension(self): self.assertTrue(plan_moves(['README'])[0]['destination'].endswith('no_extension/README'))
 def test_does_not_move_files(self): self.assertEqual(plan_moves(['a.txt'])[0]['source'],'a.txt')
 def test_multiple(self): self.assertEqual(len(plan_moves(['a.txt','b.png'])),2)
if __name__=='__main__': unittest.main()
