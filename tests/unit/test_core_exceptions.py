"""Unit tests for the custom exceptions in the core package."""
import pytest

from base.core.exceptions import (
    BaseError,
    ConfigurationError,
    ValidationError,
)


def test_custom_exceptions():
    """Tests that the custom exceptions can be raised and caught."""
    with pytest.raises(BaseError):
        raise BaseError("This is a base error.")

    with pytest.raises(ValidationError):
        raise ValidationError("This is a validation error.")

    with pytest.raises(ConfigurationError):
        raise ConfigurationError("This is a configuration error.")


def test_custom_exception_hierarchy():
    """Tests that the custom exceptions inherit from BaseError."""
    with pytest.raises(BaseError):
        raise ValidationError("This should be caught as BaseError.")

    with pytest.raises(BaseError):
        raise ConfigurationError("This should also be caught as BaseError.")
