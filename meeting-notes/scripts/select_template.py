#!/usr/bin/env python3
"""Select and validate a semantic Markdown template."""

from __future__ import annotations

import argparse
import re
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
TEMPLATES = ROOT / "templates"
CONFIG = ROOT / "config" / "current_template.txt"
SEMANTIC_NAME = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")


def available() -> dict[str, Path]:
    return {path.stem: path for path in sorted(TEMPLATES.glob("*.md"))}


def default_name() -> str:
    lines = CONFIG.read_text(encoding="utf-8").splitlines()
    if len(lines) != 1 or not lines[0].strip():
        raise SystemExit("current_template.txt must contain exactly one template name")
    return lines[0].strip()


def validate() -> None:
    templates = available()
    default = default_name()
    if default not in templates:
        raise SystemExit(f"Default template '{default}' does not exist")
    for name, path in templates.items():
        if not SEMANTIC_NAME.fullmatch(name):
            raise SystemExit(f"Invalid semantic template name: {name}")
        text = path.read_text(encoding="utf-8")
        if "## Format" not in text or "## Example" not in text:
            raise SystemExit(f"Template '{name}' must contain Format and Example sections")


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--template", help="Use one template without changing the default")
    parser.add_argument("--list", action="store_true", help="List active template names")
    parser.add_argument("--path-only", action="store_true", help="Print only the selected path")
    parser.add_argument("--check", action="store_true", help="Validate templates and exit")
    args = parser.parse_args()

    validate()
    templates = available()
    if args.check:
        print(f"OK: {len(templates)} template(s)")
        return
    if args.list:
        print("\n".join(templates))
        return
    name = (args.template or default_name()).strip()
    if not SEMANTIC_NAME.fullmatch(name) or name not in templates:
        raise SystemExit(f"Unknown template '{name}'. Available: {', '.join(templates)}")
    path = templates[name]
    print(path)
    if not args.path_only:
        print(path.read_text(encoding="utf-8"))


if __name__ == "__main__":
    main()
