from __future__ import annotations

import os
from collections.abc import Generator
from pathlib import Path
from typing import TYPE_CHECKING

import pytest

if TYPE_CHECKING:
    pass


@pytest.fixture()
def project_root() -> Generator[Path, None, None]:
    yield Path(__file__).resolve().parent.parent


@pytest.fixture()
def change_test_dir(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> Generator[Path, None, None]:
    original_cwd = Path.cwd()
    try:
        monkeypatch.chdir(tmp_path)
        yield tmp_path
    finally:
        os.chdir(original_cwd)
