from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
TEMPLATES = ROOT / "templates"
CONFIG = ROOT / "config" / "current_template.txt"

def selected_name():
    if len(sys.argv) > 1:
        return sys.argv[1].strip()
    return CONFIG.read_text(encoding="utf-8").strip()

def main():
    name = selected_name()
    if not name or "/" in name or "\\" in name:
        raise SystemExit("Invalid template name")
    path = TEMPLATES / f"{name}.md"
    if not path.exists():
        available = sorted(p.stem for p in TEMPLATES.glob("*.md"))
        raise SystemExit(f"Template '{name}' not found. Available: {', '.join(available)}")
    print(path)
    print(path.read_text(encoding="utf-8"))

if __name__ == "__main__":
    main()
