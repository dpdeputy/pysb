# Python Sandbox Template

This repository hosts the **Python Sandbox** Copier template. It provides a ready-to-run project skeleton with strict tooling (ruff, mypy, pytest, pre-commit) and example modules/tests so new services start with production-grade defaults.

## Generate a project locally

```bash
copier copy gh:dpdeputy/pysb template my-new-service
```

This command clones the template, prompts for project metadata, and creates a fresh repository in `my-new-service/` with the sandbox tooling preconfigured.

## Naming conventions

- **Distribution slug:** Copier keeps the hyphenated value you enter for `project_slug` (for example `my-app`) when generating metadata such as `pyproject.toml`.
- **Python package:** The actual importable module is rendered under `src/{{ module_name }}/`, where `module_name` is automatically derived by replacing `-` with `_` (e.g., `my_app`). Import statements must therefore use the underscore form, such as `from my_app.core.config import ProjectConfig`.
