"""Custom exception types for the base package."""


class BaseError(Exception):
    """Base exception for the base package."""


class ValidationError(BaseError):
    """Raised when data validation fails."""


class ConfigurationError(BaseError):
    """Raised when configuration is invalid."""
