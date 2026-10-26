import json
import tempfile
import unittest
from pathlib import Path
from project94_agent_memory_evaluation import MemoryStore, evaluate_outcome


class TestMemoryAndEvaluation(unittest.TestCase):
    def test_remember_recall(self):
        store = MemoryStore()
        store.remember("topic", "RAG")
        self.assertEqual(store.recall("topic"), "RAG")

    def test_key_and_value_are_trimmed(self):
        store = MemoryStore()
        store.remember(" topic ", " RAG ")
        self.assertEqual(store.recall("topic"), "RAG")

    def test_empty_values_rejected(self):
        with self.assertRaises(ValueError):
            MemoryStore().remember("", "value")
        with self.assertRaises(ValueError):
            MemoryStore().remember("key", "  ")

    def test_non_string_memory_inputs_rejected(self):
        with self.assertRaises(TypeError):
            MemoryStore().remember(42, "value")
        with self.assertRaises(TypeError):
            MemoryStore().remember("key", None)

    def test_recall_missing_key_returns_none(self):
        self.assertIsNone(MemoryStore().recall("missing"))

    def test_export_json(self):
        store = MemoryStore()
        store.remember("language", "Hindi")
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / "memory.json"
            store.export_json(path)
            self.assertEqual(json.loads(path.read_text(encoding="utf-8"))["language"], "Hindi")

    def test_export_json_preserves_unicode(self):
        store = MemoryStore()
        store.remember("greeting", "नमस्ते")
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / "memory.json"
            store.export_json(path)
            self.assertIn("नमस्ते", path.read_text(encoding="utf-8"))

    def test_evaluation_normalizes_whitespace_case(self):
        self.assertTrue(evaluate_outcome("Hello  World", " hello world ")["passed"])

    def test_evaluation_detects_mismatch(self):
        self.assertFalse(evaluate_outcome("yes", "no")["passed"])

    def test_evaluation_preserves_original_values(self):
        result = evaluate_outcome(" Hello ", "hello")
        self.assertEqual(result["expected"], " Hello ")
        self.assertEqual(result["actual"], "hello")

    def test_evaluation_rejects_non_string_inputs(self):
        with self.assertRaises(TypeError):
            evaluate_outcome(None, "hello")

if __name__ == "__main__":
    unittest.main()
