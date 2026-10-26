import unittest
from project88_workflow_engine import Step, run_workflow
class TestWorkflow(unittest.TestCase):
 def test_pipeline(self): self.assertEqual(run_workflow('  Hello ',[Step('trim','strip'),Step('lower','lowercase')]),'hello')
 def test_upper(self): self.assertEqual(run_workflow('hi',[Step('up','uppercase')]),'HI')
 def test_unknown_action_rejected(self):
  with self.assertRaises(ValueError): run_workflow('x',[Step('bad','execute_shell')])
 def test_empty_pipeline(self): self.assertEqual(run_workflow('unchanged',[]),'unchanged')
 def test_step_has_only_used_fields(self): self.assertEqual(Step('up','uppercase').action, 'uppercase')
if __name__=='__main__': unittest.main()
