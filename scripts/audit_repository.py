#!/usr/bin/env python3
"""Audit skill structure, template switching, and common privacy leaks."""

from __future__ import annotations

import re
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
TEXT_SUFFIXES = {".md", ".py", ".txt", ".json", ".yaml", ".yml", ".toml"}
SEMANTIC_NAME = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")
EMAIL = re.compile(r"\b[A-Z0-9._%+-]+@[A-Z0-9.-]+\.[A-Z]{2,}\b", re.I)
PHONE = re.compile(r"(?<!\d)1[3-9]\d{9}(?!\d)")
ABSOLUTE_USER_PATH = re.compile(r"(?:/Users/[^/\s]+|/home/[^/\s]+|[A-Z]:\\Users\\[^\\\s]+)")
SECRET = re.compile(
    r"(?:api[_-]?key|access[_-]?token|client[_-]?secret|password)"
    r"\s*[:=]\s*['\"]?[^\s'\"<>]+",
    re.I,
)
PROPRIETARY_AGENT_NAMES = re.compile(r"\b(?:ChatGPT|Codex|Claude|Cursor)\b", re.I)


def is_public_file(path: Path) -> bool:
    relative = path.relative_to(ROOT)
    if any(part in {".git", "__pycache__"} for part in relative.parts):
        return False
    if relative.as_posix() == "scripts/audit_repository.py":
        return False
    if relative.as_posix() == ".privacy-denylist":
        return False
    if "private" in relative.parts:
        return path.name == "README.md" or path.name.endswith(".example.md")
    return path.suffix.lower() in TEXT_SUFFIXES


def read_denylist() -> list[str]:
    path = ROOT / ".privacy-denylist"
    if not path.exists():
        return []
    return [
        line.strip()
        for line in path.read_text(encoding="utf-8").splitlines()
        if line.strip() and not line.lstrip().startswith("#")
    ]


def check_frontmatter(skill: Path, errors: list[str]) -> None:
    text = (skill / "SKILL.md").read_text(encoding="utf-8")
    match = re.match(r"^---\n(.*?)\n---\n", text, re.S)
    if not match:
        errors.append(f"{skill.name}/SKILL.md: missing YAML frontmatter")
        return
    keys: list[str] = []
    values: dict[str, str] = {}
    for line in match.group(1).splitlines():
        if ":" not in line:
            continue
        key, value = line.split(":", 1)
        keys.append(key.strip())
        values[key.strip()] = value.strip()
    if set(keys) != {"name", "description"}:
        errors.append(f"{skill.name}/SKILL.md: frontmatter must contain only name and description")
    if values.get("name") != skill.name:
        errors.append(f"{skill.name}/SKILL.md: name must match directory")
    if not values.get("description"):
        errors.append(f"{skill.name}/SKILL.md: description is empty")
    if re.search(r"^##\s+(?:Format|Example)\b", text, re.M | re.I):
        errors.append(f"{skill.name}/SKILL.md: embedded template body detected")
    if PROPRIETARY_AGENT_NAMES.search(text):
        errors.append(f"{skill.name}/SKILL.md: platform-specific agent/tool name detected")


def check_templates(skill: Path, errors: list[str]) -> None:
    templates = skill / "templates"
    config = skill / "config" / "current_template.txt"
    if not templates.is_dir():
        errors.append(f"{skill.name}: missing templates/")
        return
    if not config.is_file():
        errors.append(f"{skill.name}: missing config/current_template.txt")
        return
    defaults = config.read_text(encoding="utf-8").splitlines()
    if len(defaults) != 1 or not defaults[0].strip():
        errors.append(f"{skill.name}: current_template.txt must contain one non-empty line")
        return
    default = defaults[0].strip()
    if not SEMANTIC_NAME.fullmatch(default):
        errors.append(f"{skill.name}: default template name is not semantic")
    files = sorted(templates.glob("*.md"))
    if not files:
        errors.append(f"{skill.name}: no active templates")
    stems = {path.stem for path in files}
    if default not in stems:
        errors.append(f"{skill.name}: default template '{default}' does not exist")
    for path in files:
        if not SEMANTIC_NAME.fullmatch(path.stem):
            errors.append(f"{skill.name}/{path.name}: template filename is not semantic")
        text = path.read_text(encoding="utf-8")
        if not re.search(r"^##\s+Format\s*$", text, re.M):
            errors.append(f"{skill.name}/{path.name}: missing '## Format'")
        if not re.search(r"^##\s+Example\s*$", text, re.M):
            errors.append(f"{skill.name}/{path.name}: missing '## Example'")


def smoke_test(skill: Path, errors: list[str]) -> None:
    selector = skill / "scripts" / "select_template.py"
    if not selector.is_file():
        errors.append(f"{skill.name}: missing scripts/select_template.py")
        return
    for args in (["--check"], ["--path-only"]):
        result = subprocess.run(
            [sys.executable, str(selector), *args],
            cwd=skill,
            capture_output=True,
            text=True,
            check=False,
        )
        if result.returncode:
            errors.append(f"{skill.name}: selector smoke test failed")
            return
    templates = sorted((skill / "templates").glob("*.md"))
    default = (skill / "config" / "current_template.txt").read_text(encoding="utf-8").strip()
    alternate = next((path.stem for path in templates if path.stem != default), default)
    result = subprocess.run(
        [sys.executable, str(selector), "--template", alternate, "--path-only"],
        cwd=skill,
        capture_output=True,
        text=True,
        check=False,
    )
    if result.returncode:
        errors.append(f"{skill.name}: explicit template switch failed")


def scan_privacy(errors: list[str]) -> None:
    denylist = read_denylist()
    patterns = [
        ("email address", EMAIL),
        ("phone number", PHONE),
        ("absolute user path", ABSOLUTE_USER_PATH),
        ("possible secret", SECRET),
    ]
    for path in sorted(ROOT.rglob("*")):
        if not path.is_file() or not is_public_file(path):
            continue
        try:
            text = path.read_text(encoding="utf-8")
        except UnicodeDecodeError:
            continue
        relative = path.relative_to(ROOT)
        for label, pattern in patterns:
            if pattern.search(text):
                errors.append(f"{relative}: {label} pattern detected")
        lowered = text.casefold()
        for item in denylist:
            if item.casefold() in lowered:
                errors.append(f"{relative}: local denylist match detected")


def main() -> None:
    errors: list[str] = []
    skills = sorted(path.parent for path in ROOT.glob("*/SKILL.md"))
    if not skills:
        errors.append("No skills found")
    for skill in skills:
        for required in ("README.md", "SKILL.md"):
            if not (skill / required).is_file():
                errors.append(f"{skill.name}: missing {required}")
        check_frontmatter(skill, errors)
        check_templates(skill, errors)
        smoke_test(skill, errors)
    scan_privacy(errors)

    if errors:
        print("Audit failed:")
        for error in errors:
            print(f"- {error}")
        raise SystemExit(1)
    print(f"Audit passed: {len(skills)} skill(s), privacy scan clean, template switching verified.")


if __name__ == "__main__":
    main()
