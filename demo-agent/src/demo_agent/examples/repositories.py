from typing import Dict, Optional

from demo_agent.core.interfaces import Repository
from demo_agent.utils.logging import logger

from .models import User


class UserRepository(Repository[User]):
    """A repository for managing User objects in memory."""

    def __init__(self) -> None:
        """Initializes the in-memory user store."""
        self._users: Dict[int, User] = {}
        self._next_id: int = 1

    def save(self, user: User) -> User:
        """Saves a user to the in-memory store.

        If the user has no ID, a new one is assigned.
        If the user already has an ID, it is updated.
        """
        if user.id is None:
            user.id = self._next_id
            self._next_id += 1
        self._users[user.id] = user
        logger.info(f"Saving user: {user.name}")
        return user

    def find_by_id(self, user_id: int) -> Optional[User]:
        """Finds a user by their ID."""
        logger.info(f"Finding user by id: {user_id}")
        return self._users.get(user_id)

    def find_by_email(self, email: str) -> Optional[User]:
        """Finds a user by their email address."""
        logger.info(f"Finding user by email: {email}")
        for user in self._users.values():
            if user.email == email:
                return user
        return None
