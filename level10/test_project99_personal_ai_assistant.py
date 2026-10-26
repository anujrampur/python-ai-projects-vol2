import tempfile, unittest
from pathlib import Path
from project99_personal_ai_assistant import PersonalAssistant

class PersonalAssistantTests(unittest.TestCase):
    def test_notes(self):
        a = PersonalAssistant(); a.add_note(" hello ")
        self.assertEqual(a.notes, ["hello"])
        with self.assertRaises(ValueError): a.add_note(" ")
    def test_allowlisted_tool(self):
        a = PersonalAssistant({"upper": str.upper})
        self.assertEqual(a.run_tool("upper", "hello").output, "HELLO")
        with self.assertRaises(ValueError): a.run_tool("delete_everything", "x")
    def test_read_allowed_text_file(self):
        with tempfile.TemporaryDirectory() as d:
            p = Path(d) / "note.txt"; p.write_text("hello", encoding="utf-8")
            self.assertEqual(PersonalAssistant().read_text_file(str(p), d), "hello")
    def test_path_escape_rejected(self):
        with tempfile.TemporaryDirectory() as d, tempfile.TemporaryDirectory() as other:
            p = Path(other) / "note.txt"; p.write_text("secret", encoding="utf-8")
            with self.assertRaises(ValueError):
                PersonalAssistant().read_text_file(str(p), d)
    def test_file_extension_rejected(self):
        with tempfile.TemporaryDirectory() as d:
            p = Path(d) / "note.py"; p.write_text("x", encoding="utf-8")
            with self.assertRaises(ValueError): PersonalAssistant().read_text_file(str(p), d)

if __name__ == "__main__": unittest.main()
