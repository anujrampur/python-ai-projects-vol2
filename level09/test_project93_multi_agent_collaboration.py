import unittest
from project93_multi_agent_collaboration import Contribution, combine_contributions


class TestCollaboration(unittest.TestCase):
    def test_combines_roles(self):
        result = combine_contributions([
            Contribution("Researcher", "Found two sources."),
            Contribution("Reviewer", "Check dates."),
        ])
        self.assertEqual(result, "## Researcher\nFound two sources.\n\n## Reviewer\nCheck dates.")

    def test_preserves_input_order(self):
        result = combine_contributions([Contribution("A", "one"), Contribution("B", "two")])
        self.assertLess(result.index("## A"), result.index("## B"))

    def test_trims_outer_whitespace(self):
        self.assertEqual(combine_contributions([Contribution(" Writer ", "  draft  ")]), "## Writer\ndraft")

    def test_empty_collection_rejected(self):
        with self.assertRaisesRegex(ValueError, "at least one"):
            combine_contributions([])

    def test_blank_role_rejected(self):
        with self.assertRaises(ValueError):
            combine_contributions([Contribution("  ", "content")])

    def test_blank_content_rejected(self):
        with self.assertRaises(ValueError):
            combine_contributions([Contribution("Writer", " ")])

    def test_wrong_collection_type_rejected(self):
        with self.assertRaises(TypeError):
            combine_contributions("not a collection")

    def test_wrong_item_type_rejected(self):
        with self.assertRaises(TypeError):
            combine_contributions(["not a contribution"])

    def test_non_string_fields_rejected(self):
        with self.assertRaises(TypeError):
            combine_contributions([Contribution(12, "content")])

    def test_multiline_role_rejected(self):
        with self.assertRaises(ValueError):
            combine_contributions([Contribution("Writer\n## Injected", "content")])


if __name__ == "__main__":
    unittest.main()
