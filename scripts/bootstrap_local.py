#!/usr/bin/env python3
"""Create local private configuration files without overwriting user data."""

from __future__ import annotations

import argparse
import shutil
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


def skill_directories(selected: str | None) -> list[Path]:
    skills = sorted(path.parent for path in ROOT.glob("*/SKILL.md"))
    if selected is None:
        return skills
    match = [path for path in skills if path.name == selected]
    if not match:
        available = ", ".join(path.name for path in skills)
        raise SystemExit(f"Unknown skill '{selected}'. Available: {available}")
    return match


def destination_for(example: Path) -> Path:
    suffix = ".example.md"
    if not example.name.endswith(suffix):
        raise ValueError(f"Unsupported example filename: {example.name}")
    return example.with_name(example.name[: -len(suffix)] + ".md")


def bootstrap(skill: Path) -> tuple[list[Path], list[Path]]:
    private = skill / "private"
    private.mkdir(exist_ok=True)
    (private / "assets").mkdir(exist_ok=True)
    created: list[Path] = []
    skipped: list[Path] = []
    for example in sorted(private.glob("*.example.md")):
        target = destination_for(example)
        if target.exists():
            skipped.append(target)
            continue
        shutil.copyfile(example, target)
        created.append(target)
    return created, skipped


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--skill", help="Initialize one skill instead of all skills")
    args = parser.parse_args()

    total_created = 0
    for skill in skill_directories(args.skill):
        created, skipped = bootstrap(skill)
        total_created += len(created)
        print(f"{skill.name}: created {len(created)}, kept {len(skipped)} existing")
    print(f"Done. Created {total_created} local private file(s).")


if __name__ == "__main__":
    main()
