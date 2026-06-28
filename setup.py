from __future__ import annotations

import os
from pathlib import Path

from setuptools import setup

_SHARE_DIR = Path("share")


def _build_data_files() -> list[tuple[str, list[str]]]:
    """Recursively collect share/ into wheel data-files without manual enumeration."""
    install_share = Path("share")
    data_files: dict[str, list[str]] = {}
    if _SHARE_DIR.is_dir():
        for path in sorted(_SHARE_DIR.rglob("*")):
            if not path.is_file():
                continue
            rel_dir = path.parent.relative_to(_SHARE_DIR)
            target = str(install_share / rel_dir)
            data_files.setdefault(target, []).append(str(path))
    return sorted(data_files.items())


setup(data_files=_build_data_files())

