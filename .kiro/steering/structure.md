# Project Structure

## Directory Layout
The project follows the src-layout structure recommended by the Python Packaging Authority (PyPA):

```
python-sandbox/
├── .gitlab-ci.yml              # GitLab CI/CD pipeline configuration
├── .gitignore                  # Git ignore patterns for Python projects
├── .pre-commit-config.yaml     # Pre-commit hooks configuration
├── .kiro/                      # Kiro IDE configuration and steering
│   └── steering/               # AI assistant guidance documents
├── src/                        # Source code (src-layout)
│   └── base/                   # Main package directory
│       ├── __init__.py         # Package initialization and metadata
│       ├── core/               # Core functionality and base classes
│       │   ├── __init__.py
│       │   ├── config.py       # Configuration management with Pydantic
│       │   ├── exceptions.py   # Custom exception hierarchy
│       │   └── interfaces.py   # Abstract base classes and protocols
│       ├── utils/              # Common utilities and helpers
│       │   ├── __init__.py
│       │   ├── logging.py      # Structured logging configuration
│       │   ├── helpers.py      # General utility functions
│       │   └── validators.py   # Data validation helpers
│       └── examples/           # Example implementations and patterns
│           ├── __init__.py
│           ├── models.py       # Example Pydantic domain models
│           ├── repositories.py # Repository pattern examples
│           └── services.py     # Service layer examples
├── tests/                      # Test suite
│   ├── conftest.py            # Pytest configuration and fixtures
│   ├── unit/                  # Unit tests (test individual components)
│   │   ├── test_core/
│   │   ├── test_utils/
│   │   └── test_examples/
│   └── integration/           # Integration tests (test component interactions)
├── docs/                      # Documentation
│   ├── index.md              # Main documentation entry point
│   ├── mkdocs.yml            # MkDocs configuration
│   ├── user-guide/           # User-facing documentation
│   │   └── README.md         # Usage instructions and API reference
│   └── developer-guide/      # Development documentation
│       └── README.md         # Setup, contribution guidelines, architecture
├── pyproject.toml            # Project configuration (PEP 518/621)
├── README.md                 # Project overview and setup instructions
└── CHANGELOG.md              # Release notes and version history
```

## Key Conventions

### Package Organization
- **src-layout**: All source code lives under `src/` directory
- **Namespace**: Main package is `base` (can be renamed for specific projects)
- **Modules**: Organized by functionality (core, utils, examples)
- **Imports**: Use absolute imports from package root

### File Naming
- **Python files**: Use snake_case (e.g., `user_repository.py`)
- **Test files**: Prefix with `test_` (e.g., `test_user_repository.py`)
- **Configuration**: Use standard names (pyproject.toml, .gitignore, etc.)

### Code Organization Patterns
- **Domain Models**: Use Pydantic BaseModel for all data models
- **Repository Pattern**: Separate data access from business logic
- **Service Layer**: Business logic separate from models and repositories
- **Configuration**: Centralized in `core.config` module using Pydantic
- **Exceptions**: Custom hierarchy in `core.exceptions`

### Test Organization
- **Unit Tests**: Test individual functions/classes in isolation
- **Integration Tests**: Test component interactions
- **Fixtures**: Common test data and setup in `conftest.py`
- **Coverage**: Minimum 80% for core modules, 100% for critical logic

### Documentation Structure
- **User Guide**: How to use the package/library
- **Developer Guide**: How to contribute and develop
- **API Reference**: Auto-generated from docstrings
- **Architecture**: Design decisions and patterns explained

### Configuration Files
- **pyproject.toml**: Single source of truth for project metadata, dependencies, and tool configuration
- **No setup.py**: Modern packaging uses only pyproject.toml
- **Tool Configuration**: All tools configured in pyproject.toml [tool.*] sections