class BaseError(Exception):
    """Base exception for the {{ project_name }} package."""


class ValidationError(BaseError):
    """Raised when data validation fails."""


class ConfigurationError(BaseError):
    """Raised when configuration is invalid."""
