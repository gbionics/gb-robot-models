#!/usr/bin/env python3
from __future__ import annotations

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


VERSION_RE = re.compile(r"^[0-9]+\.[0-9]+\.[0-9]+(?:[a-zA-Z0-9._-]*)?$")


def _replace_once(path: Path, pattern: str, replacement: str) -> None:
    text = path.read_text(encoding="utf-8")
    new_text, count = re.subn(pattern, replacement, text, count=1, flags=re.MULTILINE)
    if count != 1:
        raise RuntimeError(f"Failed to update expected pattern in {path}")
    path.write_text(new_text, encoding="utf-8")


def main() -> int:
    if len(sys.argv) != 2:
        print("Usage: pixi run set-version -- <version>", file=sys.stderr)
        return 2

    version = sys.argv[1].strip()
    if not VERSION_RE.match(version):
        print(f"Invalid version '{version}'", file=sys.stderr)
        return 2

    _replace_once(
        ROOT / "pixi.toml",
        r'^(version\s*=\s*")[^"]+("\s*)$',
        rf'\g<1>{version}\2',
    )
    _replace_once(
        ROOT / "pyproject.toml",
        r'^(version\s*=\s*")[^"]+("\s*)$',
        rf'\g<1>{version}\2',
    )
    _replace_once(
        ROOT / "package.xml",
        r'^(\s*<version>)[^<]+(</version>\s*)$',
        rf'\g<1>{version}\2',
    )
    _replace_once(
        ROOT / "CMakeLists.txt",
        r'^(project\(gb-robot-models\s+VERSION\s+)[^\s)]+(\s+LANGUAGES\s+NONE\)\s*)$',
        rf'\g<1>{version}\2',
    )
    _replace_once(
        ROOT / "src/gb_robot_models/version.py",
        r'^(__version__\s*=\s*")[^"]+("\s*)$',
        rf'\g<1>{version}\2',
    )

    print(f"Updated version to {version}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
