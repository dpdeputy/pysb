class BaseError(Exception):
    """Base exception for the Demo Agent package."""


class ValidationError(BaseError):
    """Raised when data validation fails."""


class ConfigurationError(BaseError):
    """Raised when configuration is invalid."""
