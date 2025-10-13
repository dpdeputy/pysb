from __future__ import annotations

import subprocess
from pathlib import Path
from typing import TYPE_CHECKING

import pytest

if TYPE_CHECKING:
    from collections.abc import Generator


@pytest.fixture(scope="module")
def repo_root() -> Generator[Path, None, None]:
    yield Path(__file__).resolve().parents[2]


def _run_uv(args: list[str], cwd: Path) -> subprocess.CompletedProcess[str]:
    command = ["uv", "run", *args]
    return subprocess.run(
        command,
        cwd=cwd,
        text=True,
        capture_output=True,
        check=False,
    )  # noqa: S603 - controlled execution of first-party tooling


def test_ruff_configuration(repo_root: Path) -> None:
    sample = repo_root / "tests" / "fixtures" / "lint_sample.py"
    result = _run_uv(["ruff", "check", str(sample)], repo_root)
    assert result.returncode == 0, result.stderr


def test_mypy_configuration(repo_root: Path) -> None:
    sample = repo_root / "tests" / "fixtures" / "type_sample.py"
    result = _run_uv(["mypy", str(sample)], repo_root)
    assert result.returncode == 0, result.stderr


def test_pytest_configuration(repo_root: Path) -> None:
    sample = repo_root / "tests" / "fixtures"
    result = _run_uv(["pytest", str(sample)], repo_root)
    assert result.returncode == 0, result.stderr or result.stdout


def test_pre_commit_hooks(repo_root: Path) -> None:
    result = _run_uv(
        ["pre-commit", "run", "--all-files", "--show-diff-on-failure"],
        repo_root,
    )
    assert result.returncode == 0, result.stderr or result.stdout
