from __future__ import annotations

import argparse
import os
import subprocess
import sys
from pathlib import Path

from resolve_robotics_uri_py import resolve_robotics_uri_py


def _resolve_input_path(input_value: str) -> str:
    if input_value.startswith("package://"):
        return resolve_robotics_uri_py.resolve_robotics_uri(input_value)
    return str(Path(input_value).expanduser().resolve())


def _package_name_from_uri(input_value: str) -> str | None:
    if not input_value.startswith("package://"):
        return None
    remainder = input_value[len("package://") :]
    if not remainder:
        return None
    return remainder.split("/", 1)[0] or None


def _prefix_from_resolved_path(resolved_path: str, package_name: str) -> str | None:
    path = Path(resolved_path)
    for parent in path.parents:
        if parent.name == package_name and parent.parent.name == "share":
            return str(parent.parent.parent)
    return None


def _build_rerun_env(model_input: str, resolved_model: str) -> dict[str, str]:
    env = os.environ.copy()
    package_name = _package_name_from_uri(model_input)
    if package_name is None:
        return env

    prefix = _prefix_from_resolved_path(resolved_model, package_name)
    if prefix is None:
        return env

    existing_value = env.get("AMENT_PREFIX_PATH", "")
    prefixes = [value for value in existing_value.split(os.pathsep) if value]
    if prefix not in prefixes:
        prefixes.append(prefix)
        env["AMENT_PREFIX_PATH"] = os.pathsep.join(prefixes)

    return env


def _show_in_rerun(model_path_or_uri: str) -> int:
    try:
        resolved_model = _resolve_input_path(model_path_or_uri)
    except RuntimeError as exc:
        print(f"Error: failed to resolve URI '{model_path_or_uri}': {exc}", file=sys.stderr)
        return 1

    env = _build_rerun_env(model_path_or_uri, resolved_model)

    try:
        result = subprocess.run(["rerun", resolved_model], check=False, env=env)
    except FileNotFoundError:
        print(
            "Error: 'rerun' executable not found. Ensure rerun-sdk is installed in this environment.",
            file=sys.stderr,
        )
        return 1

    return result.returncode


def _build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(prog="gb-robot-models")
    subparsers = parser.add_subparsers(dest="command", required=True)

    show_parser = subparsers.add_parser(
        "show-in-rerun",
        help="Resolve a robot model URI/path and open it in rerun.",
    )
    show_parser.add_argument(
        "model",
        help="Model URI or path, e.g. package://gb_robot_models/robots/gene01_0/model.urdf",
    )

    return parser


def main() -> int:
    parser = _build_parser()
    args = parser.parse_args()

    if args.command == "show-in-rerun":
        return _show_in_rerun(args.model)

    parser.error("Unknown command")
    return 2


if __name__ == "__main__":
    raise SystemExit(main())
