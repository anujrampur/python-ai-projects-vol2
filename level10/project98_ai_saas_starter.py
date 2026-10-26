"""Project 98: AI SaaS Starter — in-memory demo auth and usage quotas.

Educational example only: this is not production authentication or a secure,
persistent SaaS backend. Usage counts do not reset automatically each day.
"""
from dataclasses import dataclass
import hashlib
import secrets


@dataclass
class User:
    user_id: str
    email: str
    password_salt: str
    password_hash: str
    usage_count: int = 0


class SaaSDemo:
    def __init__(self, daily_limit: int = 10):
        if isinstance(daily_limit, bool) or not isinstance(daily_limit, int) or daily_limit < 1:
            raise ValueError("daily_limit must be a positive integer.")
        self.daily_limit = daily_limit
        self._users = {}

    @staticmethod
    def _hash_password(password: str, salt: str) -> str:
        return hashlib.pbkdf2_hmac(
            "sha256", password.encode("utf-8"), salt.encode("utf-8"), 200_000
        ).hex()

    @staticmethod
    def _email_key(email: str) -> str:
        if not isinstance(email, str) or not email or email.strip() != email or "@" not in email:
            raise ValueError("Enter a valid email address.")
        local, separator, domain = email.partition("@")
        if not separator or not local or not domain or "@" in domain:
            raise ValueError("Enter a valid email address.")
        return email.casefold()

    def register(self, email: str, password: str) -> str:
        key = self._email_key(email)
        if not isinstance(password, str) or len(password) < 10:
            raise ValueError("Password must be at least 10 characters.")
        if key in self._users:
            raise ValueError("Account already exists.")
        salt = secrets.token_hex(16)
        user_id = secrets.token_urlsafe(12)
        self._users[key] = User(user_id, email, salt, self._hash_password(password, salt))
        return user_id

    def authenticate(self, email: str, password: str) -> str:
        key = self._email_key(email)
        if not isinstance(password, str):
            raise ValueError("Invalid credentials.")
        user = self._users.get(key)
        if user is None or not secrets.compare_digest(
            self._hash_password(password, user.password_salt), user.password_hash
        ):
            raise ValueError("Invalid credentials.")
        return user.user_id

    def consume_usage(self, email: str) -> int:
        key = self._email_key(email)
        user = self._users.get(key)
        if user is None:
            raise ValueError("Unknown account.")
        if user.usage_count >= self.daily_limit:
            raise RuntimeError("Daily usage limit reached.")
        user.usage_count += 1
        return self.daily_limit - user.usage_count
