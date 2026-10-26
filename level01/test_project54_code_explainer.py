import unittest
from project54_code_explainer import explain_python

class TestCodeExplainer(unittest.TestCase):
    def test_detects_function_and_loop(self):
        notes = explain_python("def greet(name):\n    for x in name:\n        print(x)")
        self.assertTrue(any("function named 'greet'" in note for note in notes))
        self.assertTrue(any("for-loop" in note for note in notes))
    def test_detects_assignment(self):
        self.assertTrue(any("Assigns a value to: total" in note for note in explain_python("total = 5")))
    def test_invalid_syntax(self):
        with self.assertRaises(ValueError): explain_python("def broken(")
    def test_empty_source(self):
        with self.assertRaises(ValueError): explain_python(" ")
    def test_does_not_execute_code(self):
        notes = explain_python("print('hello')")
        self.assertTrue(any("Calls 'print'" in note for note in notes))

if __name__ == "__main__": unittest.main()
