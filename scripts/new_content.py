#!/usr/bin/env python3
"""Create a content page from one of the repository templates."""

from __future__ import annotations
import argparse
from datetime import date
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]
MAP = {
    "publication": (ROOT / "_templates/publication.qmd", ROOT / "publications"),
    "tool": (ROOT / "_templates/tool.qmd", ROOT / "tools"),
    "note": (ROOT / "_templates/research-note.qmd", ROOT / "notes"),
    "reading": (ROOT / "_templates/reading-note.qmd", ROOT / "reading"),
}


def slugify(value: str) -> str:
    value = value.lower().strip()
    value = re.sub(r"[^a-z0-9]+", "-", value)
    return value.strip("-")


def main() -> None:
    p = argparse.ArgumentParser()
    p.add_argument("kind", choices=MAP)
    p.add_argument("title")
    p.add_argument("--slug")
    args = p.parse_args()

    template, base = MAP[args.kind]
    slug = args.slug or slugify(args.title)
    if not slug:
        raise SystemExit("Could not derive an ASCII slug; provide --slug explicitly.")

    dest = base / slug / "index.qmd"
    if dest.exists():
        raise SystemExit(f"Refusing to overwrite {dest.relative_to(ROOT)}")

    text = template.read_text(encoding="utf-8")
    text = text.replace("PAPER TITLE", args.title)
    text = text.replace("TOOL NAME", args.title)
    text = text.replace("NOTE TITLE", args.title)
    text = text.replace("YYYY-MM-DD", date.today().isoformat())

    dest.parent.mkdir(parents=True, exist_ok=True)
    dest.write_text(text, encoding="utf-8")
    print(dest.relative_to(ROOT))


if __name__ == "__main__":
    main()
