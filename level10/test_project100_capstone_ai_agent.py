import unittest
from project100_capstone_ai_agent import CapstoneAgent, Action

class CapstoneTests(unittest.TestCase):
    def setUp(self): self.agent = CapstoneAgent({"echo": lambda x: f"echo:{x}"})
    def test_requires_approval_by_default(self):
        result = self.agent.execute([Action("echo", "hi")])
        self.assertEqual(result.status, "approval_required")
    def test_approved_execution(self):
        result = self.agent.execute([Action("echo", "hi")], approved=True)
        self.assertEqual(result.status, "completed")
        self.assertEqual(result.steps, ("echo: echo:hi",))
    def test_unknown_tool_blocked(self):
        result = self.agent.execute([Action("shell", "rm -rf")], approved=True)
        self.assertEqual(result.status, "blocked")
    def test_memory_validation(self):
        self.agent.remember("preference")
        self.assertEqual(self.agent.memory, ["preference"])
        with self.assertRaises(ValueError): self.agent.remember(" ")
    def test_tool_exception_propagates(self):
        agent = CapstoneAgent({"bad": lambda _: 1}, require_approval=False)
        self.assertEqual(agent.execute([Action("bad", "x", False)]).status, "error")

if __name__ == "__main__": unittest.main()
