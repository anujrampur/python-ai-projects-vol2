import unittest

from project92_task_planning_agent import Task, plan_task


class TestTaskPlanner(unittest.TestCase):
    def test_returns_five_ordered_steps(self):
        tasks = plan_task("Prepare a study plan")
        self.assertEqual(len(tasks), 5)
        self.assertEqual([task.step for task in tasks], [1, 2, 3, 4, 5])

    def test_returns_task_records(self):
        self.assertTrue(all(isinstance(task, Task) for task in plan_task("Write a book")))

    def test_goal_is_in_first_step(self):
        self.assertIn("study plan", plan_task("Prepare a study plan")[0].description)

    def test_whitespace_is_normalized(self):
        task = plan_task("  write   a\n book ")[0]
        self.assertTrue(task.description.endswith("write a book"))

    def test_empty_goal_rejected(self):
        with self.assertRaisesRegex(ValueError, "must not be empty"):
            plan_task("  \n\t ")

    def test_non_string_goal_rejected(self):
        for value in (None, 42, ["write", "a book"], True):
            with self.subTest(value=value), self.assertRaisesRegex(TypeError, "must be a string"):
                plan_task(value)

    def test_step_titles_are_nonempty(self):
        self.assertTrue(all(task.title.strip() for task in plan_task("Launch a website")))

    def test_descriptions_are_nonempty(self):
        self.assertTrue(all(task.description.strip() for task in plan_task("Launch a website")))

    def test_frozen_task_records(self):
        task = plan_task("Plan a lesson")[0]
        with self.assertRaises(AttributeError):
            task.title = "Changed"

    def test_consequential_action_requires_approval_in_guidance(self):
        tasks = plan_task("Send a report")
        self.assertIn("approval", tasks[3].description)

    def test_verification_step_mentions_unresolved_issues(self):
        tasks = plan_task("Publish a report")
        self.assertIn("unresolved issues", tasks[4].description)


if __name__ == "__main__":
    unittest.main()
