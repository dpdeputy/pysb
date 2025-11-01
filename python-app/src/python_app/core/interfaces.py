"""Abstract base classes and interfaces for the {{ project_name }} package."""

from abc import ABC, abstractmethod
from typing import Generic, TypeVar

T = TypeVar("T")


class Repository(ABC, Generic[T]):
    """An abstract base class for a repository."""

    @abstractmethod
    def save(self, entity: T) -> T:
        """Saves an entity."""
        raise NotImplementedError

    @abstractmethod
    def find_by_id(self, entity_id: int) -> T | None:
        """Finds an entity by its ID."""
        raise NotImplementedError
