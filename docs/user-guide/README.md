# User Guide

This guide is for end-users of the `base` package. It provides all the necessary information to get started with using the package in your own projects.

## Installation

To install the `base` package, you can use `pip`:

```bash
pip install base
```

*(Note: This assumes the package is published to PyPI. For local development, refer to the Developer Guide.)*

## Basic Usage

Here's a quick example of how to use the `User` model and `UserRepository` from the `base.examples` module.

```python
from base.examples.models import User
from base.examples.repositories import UserRepository

# Create a repository instance
repo = UserRepository()

# Create a new user
new_user = User(name="Jane Doe", email="jane.doe@example.com")

# Save the user
saved_user = repo.save(new_user)

print(f"User '{saved_user.name}' saved with ID: {saved_user.id}")

# Find the user by ID
found_user = repo.find_by_id(saved_user.id)

if found_user:
    print(f"Found user by ID: {found_user.name}")
```
