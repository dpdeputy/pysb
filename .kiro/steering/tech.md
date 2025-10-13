# Technology Stack

## Build System & Package Management
- **Build Backend**: Hatchling (modern alternative to setuptools)
- **Configuration**: pyproject.toml (single configuration file following PEP 518/621)
- **Dependency Management**: uv for Python version and virtual environment management
- **Versioning**: Semantic versioning starting at 0.1.0, managed via git tags with hatchling

## Development Tools
- **Testing**: pytest with pytest-cov for coverage reporting
- **Linting & Formatting**: ruff (replaces flake8, black, isort)
- **Type Checking**: mypy with strict settings
- **Pre-commit Hooks**: Automated code quality checks before commits
- **Data Validation**: Pydantic for domain models and data validation

## CI/CD & Version Control
- **Platform**: GitLab for version control and CI/CD
- **Pipeline**: Multi-stage pipeline with linting, testing, type checking
- **Python Versions**: Matrix builds across multiple Python versions
- **Releases**: Automated releases triggered by git tags

## Documentation
- **System**: MkDocs with Material theme
- **Format**: Markdown-based documentation
- **Deployment**: GitLab Pages for automated documentation hosting

## Common Commands

### Environment Setup
```bash
# Install uv (if not already installed)
# See: https://docs.astral.sh/uv/getting-started/installation/

# Create and activate virtual environment
uv venv
source .venv/bin/activate  # Linux/Mac
# or .venv\Scripts\activate  # Windows

# Install dependencies
uv sync
```

### Development Workflow
```bash
# Install development dependencies
uv sync --dev

# Run tests
uv run pytest

# Run tests with coverage
uv run pytest --cov=src

# Run linting and formatting
uv run ruff check .
uv run ruff format .

# Run type checking
uv run mypy src

# Install pre-commit hooks
uv run pre-commit install

# Build package
uv build
```

### Version Management
```bash
# Create new version tag (triggers release)
git tag v0.1.0
git push origin v0.1.0

# Check current version
uv run hatch version
```

## Project Structure Requirements
- Use src-layout structure (src/package_name/)
- Separate unit and integration tests
- Include comprehensive documentation in docs/
- Follow Pydantic patterns for all domain models
