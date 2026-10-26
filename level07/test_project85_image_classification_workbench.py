import unittest
from project85_image_classification_workbench import top_predictions
class TestImageClassifierWorkbench(unittest.TestCase):
    def test_top_k_sorted(self): self.assertEqual(top_predictions({'cat':.8,'dog':.9,'bird':.2},2)[0]['label'],'dog')
    def test_stable_tie(self): self.assertEqual(top_predictions({'z':.5,'a':.5})[0]['label'],'a')
    def test_empty_scores(self):
        with self.assertRaises(ValueError): top_predictions({})
    def test_bad_confidence(self):
        with self.assertRaises(ValueError): top_predictions({'cat':1.2})
    def test_bad_top_k(self):
        with self.assertRaises(ValueError): top_predictions({'cat':.5},0)
if __name__ == '__main__': unittest.main()
