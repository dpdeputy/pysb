"""Configuration models for the project."""
from typing import List

from pydantic import BaseModel, Field


class ProjectConfig(BaseModel):
    """Defines the project's configuration schema."""

    name: str = Field(..., description="Project name")
    version: str = Field(..., description="Project version")
    description: str = Field(..., description="Project description")
    authors: List[str] = Field(
        default_factory=list, description="Project authors"
    )
    dependencies: List[str] = Field(
        default_factory=list, description="Runtime dependencies"
    )
    dev_dependencies: List[str] = Field(
        default_factory=list, description="Development dependencies"
    )
