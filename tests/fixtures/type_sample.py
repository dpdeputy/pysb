from __future__ import annotations

from dataclasses import dataclass


@dataclass
class User:
    id: int
    name: str


def get_user_name(user: User) -> str:
    return user.name
