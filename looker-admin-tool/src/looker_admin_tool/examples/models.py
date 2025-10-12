"""Example domain models for the base package."""
from datetime import UTC, datetime
from typing import Optional

from pydantic import BaseModel, EmailStr, Field, field_validator


class User(BaseModel):
    """Represents a user in the system."""

    id: Optional[int] = Field(default=None, description="Unique user identifier")
    name: str = Field(..., min_length=1, max_length=100, description="User full name")
    email: EmailStr = Field(..., description="User email address")
    created_at: datetime = Field(default_factory=lambda: datetime.now(UTC))
    is_active: bool = Field(default=True)

    @field_validator("name")
    def validate_name(cls, v: str) -> str:
        """Validate that the name is not empty or just whitespace."""
        if not v.strip():
            raise ValueError("Name cannot be empty or whitespace")
        return v.strip()
