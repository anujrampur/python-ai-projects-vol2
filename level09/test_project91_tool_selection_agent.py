"""Regression tests for Project 91 tool selection."""

import unittest
from project91_tool_selection_agent import select_tool


class TestToolSelection(unittest.TestCase):
    def test_calculator(self):
        self.assertEqual(select_tool("calculate sum"), "calculator")

    def test_search(self):
        self.assertEqual(select_tool("search documents"), "knowledge_search")

    def test_writer(self):
        self.assertEqual(select_tool("draft email"), "draft_writer")

    def test_unknown_request(self):
        self.assertIsNone(select_tool("launch a rocket"))

    def test_tie_is_deterministic(self):
        self.assertEqual(select_tool("search draft"), "draft_writer")

    def test_punctuation_does_not_break_matching(self):
        self.assertEqual(select_tool("Please, SEARCH my notes!"), "knowledge_search")

    def test_hyphen_is_a_separator(self):
        self.assertEqual(select_tool("please re-write this"), "draft_writer")

    def test_empty_or_whitespace_request(self):
        self.assertIsNone(select_tool("   !!!   "))

    def test_keyword_is_matched_as_a_word_not_substring(self):
        self.assertIsNone(select_tool("researching"))

    def test_non_string_input_is_rejected(self):
        with self.assertRaises(TypeError):
            select_tool(None)

    def test_only_allowlisted_names_are_returned(self):
        allowed = {"calculator", "knowledge_search", "draft_writer"}
        for prompt in ("calculate", "search", "write", "unknown"):
            result = select_tool(prompt)
            self.assertTrue(result is None or result in allowed)


if __name__ == "__main__":
    unittest.main()
