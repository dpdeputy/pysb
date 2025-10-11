# Developer Guide

This guide is for developers who want to contribute to the `base` package. It provides instructions on how to set up your development environment, run tests, and contribute to the project.

## Development Setup

To set up the project for development, follow these steps:

1.  **Clone the repository:**
    ```bash
    git clone https://gitlab.com/example/python-sandbox.git
    cd python-sandbox
    ```

2.  **Create a virtual environment:**
    We use `uv` for managing virtual environments and dependencies.
    ```bash
    uv venv
    source .venv/bin/activate
    ```

3.  **Install dependencies:**
    Install the project in editable mode with all development dependencies.
    ```bash
    uv pip install -e .[dev]
    ```

4.  **Set up pre-commit hooks:**
    This will ensure your code is formatted and linted before you commit.
    ```bash
    pre-commit install
    ```

## Running Tests

To run the full suite of unit and integration tests, use `pytest`:

```bash
pytest
```

## Contribution Guidelines

We welcome contributions! Please follow these guidelines:

-   Create a new branch for your feature or bug fix.
-   Ensure all tests pass before submitting a pull request.
-   Follow the coding style enforced by `ruff`.
-   Write clear and concise commit messages.
