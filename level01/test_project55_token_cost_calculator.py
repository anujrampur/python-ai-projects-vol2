import unittest
from project55_token_cost_calculator import estimate_cost, estimate_tokens

class TestTokenCostCalculator(unittest.TestCase):
    def test_empty_text(self): self.assertEqual(estimate_tokens(""), 0)
    def test_rounds_up_estimate(self): self.assertEqual(estimate_tokens("hello"), 2)
    def test_cost_estimate(self):
        result = estimate_cost(1_000_000, 500_000, 2.0, 4.0)
        self.assertAlmostEqual(result.total_cost, 4.0)
    def test_rejects_negative_tokens(self):
        with self.assertRaises(ValueError): estimate_cost(-1, 0, 1, 1)
    def test_rejects_negative_price(self):
        with self.assertRaises(ValueError): estimate_cost(1, 1, -1, 1)
    def test_rejects_non_string(self):
        with self.assertRaises(ValueError): estimate_tokens(None)

if __name__ == "__main__": unittest.main()
