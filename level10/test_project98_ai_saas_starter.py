import unittest
from project98_ai_saas_starter import SaaSDemo


class SaaSTests(unittest.TestCase):
    def setUp(self):
        self.app = SaaSDemo(daily_limit=2)
        self.app.register("person@example.com", "a-long-demo-password")

    def test_authentication_is_case_insensitive(self):
        self.assertTrue(self.app.authenticate("PERSON@example.com", "a-long-demo-password"))

    def test_bad_password_rejected(self):
        with self.assertRaises(ValueError):
            self.app.authenticate("person@example.com", "wrong-password")

    def test_non_string_password_rejected(self):
        with self.assertRaises(ValueError):
            self.app.authenticate("person@example.com", None)

    def test_duplicate_rejected_case_insensitively(self):
        with self.assertRaises(ValueError):
            self.app.register("PERSON@example.com", "another-long-password")

    def test_invalid_emails_rejected(self):
        for email in ("", " person@example.com", "person@", "@example.com", "a@@b.com", None):
            with self.subTest(email=email), self.assertRaises(ValueError):
                self.app.register(email, "a-long-demo-password")

    def test_short_password_rejected(self):
        with self.assertRaises(ValueError):
            self.app.register("other@example.com", "short")

    def test_quota_and_limit(self):
        self.assertEqual(self.app.consume_usage("person@example.com"), 1)
        self.assertEqual(self.app.consume_usage("person@example.com"), 0)
        with self.assertRaises(RuntimeError):
            self.app.consume_usage("person@example.com")

    def test_unknown_account(self):
        with self.assertRaises(ValueError):
            self.app.consume_usage("nobody@example.com")

    def test_invalid_quota_limits(self):
        for limit in (0, -1, True, 1.5, "2"):
            with self.subTest(limit=limit), self.assertRaises(ValueError):
                SaaSDemo(limit)


if __name__ == "__main__":
    unittest.main()
