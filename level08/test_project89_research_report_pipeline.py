"""Regression tests for Project 89: Research Report Pipeline."""

import unittest

from project89_research_report_pipeline import SourceNote, build_report


class TestSourceNote(unittest.TestCase):
    def test_rejects_blank_fields(self):
        for values in (
            ("", "Title", "Note"),
            ("S1", "   ", "Note"),
            ("S1", "Title", "\n"),
        ):
            with self.subTest(values=values):
                with self.assertRaises(ValueError):
                    SourceNote(*values)

    def test_rejects_non_string_field(self):
        with self.assertRaises(ValueError):
            SourceNote("S1", "Title", None)  # type: ignore[arg-type]


class TestBuildReport(unittest.TestCase):
    def setUp(self):
        self.notes = [SourceNote("S1", "Study", "Result note")]

    def test_report_contains_source(self):
        report = build_report("AI", self.notes)
        self.assertIn("### [S1] Study", report)
        self.assertIn("Result note", report)

    def test_scope_disclaimer(self):
        report = build_report("AI", self.notes)
        self.assertIn("only the notes supplied by the user", report)
        self.assertIn("independently fact-checked", report)

    def test_trims_topic_and_source_text(self):
        report = build_report(
            "  AI research  ", [SourceNote(" S1 ", " Study ", " Note ")]
        )
        self.assertIn("# Research Brief: AI research", report)
        self.assertIn("### [S1] Study", report)
        self.assertIn("\nNote\n", report)

    def test_includes_multiple_sources_in_order(self):
        notes = [
            SourceNote("S1", "First", "First note"),
            SourceNote("S2", "Second", "Second note"),
        ]
        report = build_report("AI", notes)
        self.assertLess(report.index("[S1] First"), report.index("[S2] Second"))

    def test_verification_checklist_is_present(self):
        report = build_report("AI", self.notes)
        self.assertIn("## Verification Checklist", report)
        self.assertIn("Verify each note against the original source", report)
        self.assertIn("Record disagreements or missing evidence", report)

    def test_rejects_blank_topic(self):
        for topic in ("", " ", "\n\t"):
            with self.subTest(topic=topic):
                with self.assertRaisesRegex(ValueError, "topic is required"):
                    build_report(topic, self.notes)

    def test_rejects_non_string_topic(self):
        with self.assertRaisesRegex(ValueError, "topic is required"):
            build_report(None, self.notes)  # type: ignore[arg-type]

    def test_rejects_empty_notes(self):
        with self.assertRaisesRegex(ValueError, "at least one source note"):
            build_report("AI", [])

    def test_rejects_wrong_item_type(self):
        with self.assertRaisesRegex(ValueError, "SourceNote instance"):
            build_report("AI", ["not a source note"])  # type: ignore[list-item]


if __name__ == "__main__":
    unittest.main()
