import unittest
from project53_math_solver import solve

class TestMathSolver(unittest.TestCase):
    def test_order_of_operations(self): self.assertEqual(solve("2 + 3 * 4")["result"], 14)
    def test_parentheses(self): self.assertEqual(solve("(2 + 3) * 4")["result"], 20)
    def test_negative_number(self): self.assertEqual(solve("-3 + 5")["result"], 2)
    def test_division_by_zero(self):
        with self.assertRaises(ValueError): solve("3 / 0")
    def test_rejects_code_execution_syntax(self):
        with self.assertRaises(ValueError): solve("__import__('os').system('echo bad')")
    def test_blank_expression(self):
        with self.assertRaises(ValueError): solve(" ")

if __name__ == "__main__": unittest.main()
