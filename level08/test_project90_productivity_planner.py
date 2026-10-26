import unittest

from project90_productivity_planner import Task, plan_day


class TestPlanner(unittest.TestCase):
    def test_priority_first(self):
        result = plan_day([Task("later", 3, 20), Task("urgent", 1, 30)], 30)
        self.assertEqual([task.title for task in result["scheduled"]], ["urgent"])

    def test_defers_over_budget(self):
        result = plan_day([Task("a", 1, 40)], 20)
        self.assertEqual([task.title for task in result["deferred"]], ["a"])

    def test_remaining_time(self):
        result = plan_day([Task("a", 1, 10)], 20)
        self.assertEqual(result["remaining_minutes"], 10)

    def test_invalid_budget(self):
        for budget in (-1, True, 2.5, "20"):
            with self.subTest(budget=budget), self.assertRaises(ValueError):
                plan_day([], budget)

    def test_invalid_priority(self):
        for priority in (0, 4, True, 1.5, "1"):
            with self.subTest(priority=priority), self.assertRaises(ValueError):
                plan_day([Task("a", priority, 10)], 20)

    def test_invalid_title(self):
        for title in ("", "   ", None, 7):
            with self.subTest(title=title), self.assertRaises(ValueError):
                plan_day([Task(title, 1, 10)], 20)

    def test_invalid_duration(self):
        for minutes in (0, -1, True, 2.5, "10"):
            with self.subTest(minutes=minutes), self.assertRaises(ValueError):
                plan_day([Task("a", 1, minutes)], 20)

    def test_rejects_non_task_items(self):
        with self.assertRaises(ValueError):
            plan_day(["not a task"], 20)

    def test_rejects_text_as_tasks(self):
        with self.assertRaises(ValueError):
            plan_day("not a task list", 20)

    def test_alphabetical_tiebreaker_is_case_insensitive(self):
        result = plan_day([Task("zebra", 2, 5), Task("Apple", 2, 5), Task("apple", 2, 5)], 15)
        self.assertEqual([task.title for task in result["scheduled"]], ["Apple", "apple", "zebra"])

    def test_iterable_is_supported(self):
        result = plan_day(iter([Task("a", 1, 5)]), 10)
        self.assertEqual(result["used_minutes"], 5)

    def test_example_output(self):
        tasks = [Task("Prepare slides", priority=2, minutes=30), Task("Submit form", priority=1, minutes=15), Task("Read article", priority=3, minutes=20)]
        result = plan_day(tasks, available_minutes=45)
        self.assertEqual([task.title for task in result["scheduled"]], ["Submit form", "Prepare slides"])
        self.assertEqual((result["used_minutes"], result["remaining_minutes"]), (45, 0))
        self.assertEqual([task.title for task in result["deferred"]], ["Read article"])


if __name__ == "__main__":
    unittest.main()
