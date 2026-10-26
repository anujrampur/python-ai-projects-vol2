import unittest
from project95_human_approval_gate import ApprovalDecision, gate_action


class TestApprovalGate(unittest.TestCase):
    def test_defaults_to_not_approved(self):
        self.assertEqual(gate_action("delete old files"), ApprovalDecision(False, "awaiting_human_approval", "delete old files"))

    def test_approved_flag(self):
        decision = gate_action("send report", approved=True)
        self.assertTrue(decision.approved)
        self.assertEqual(decision.status, "approved_for_execution")

    def test_action_is_trimmed(self):
        self.assertEqual(gate_action("  publish  ").action, "publish")

    def test_empty_action_rejected(self):
        with self.assertRaises(ValueError):
            gate_action("  ")

    def test_non_string_action_rejected(self):
        for value in (None, 42, True, ["send"]):
            with self.subTest(value=value), self.assertRaises(TypeError):
                gate_action(value)

    def test_approved_requires_bool(self):
        for value in (1, "yes", None):
            with self.subTest(value=value), self.assertRaises(TypeError):
                gate_action("send report", approved=value)

    def test_decision_is_immutable(self):
        decision = gate_action("send report")
        with self.assertRaises(AttributeError):
            decision.approved = True


if __name__ == "__main__":
    unittest.main()
