#!/usr/bin/env python3
"""Replace starter placeholders across text files.

Example:
  python scripts/bootstrap.py \
    --name "Jane Doe" \
    --github "janedoe" \
    --orcid "0000-0000-0000-0000" \
    --email "jane@example.com"
"""

from __future__ import annotations
import argparse
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
TEXT_SUFFIXES = {".qmd", ".yml", ".yaml", ".md", ".css", ".bib", ".cff", ".txt"}


def main() -> None:
    p = argparse.ArgumentParser()
    p.add_argument("--name", required=True)
    p.add_argument("--github", required=True)
    p.add_argument("--orcid", required=True)
    p.add_argument("--email", required=True)
    args = p.parse_args()

    replacements = {
        "YOUR NAME": args.name,
        "YOUR_GITHUB_USERNAME": args.github,
        "YOUR_ORCID": args.orcid,
        "YOUR_EMAIL": args.email,
    }

    changed = []
    for path in ROOT.rglob("*"):
        if not path.is_file() or ".git" in path.parts:
            continue
        if path.suffix.lower() not in TEXT_SUFFIXES and path.name not in {"LICENSE"}:
            continue
        text = path.read_text(encoding="utf-8")
        new = text
        for old, value in replacements.items():
            new = new.replace(old, value)
        if new != text:
            path.write_text(new, encoding="utf-8")
            changed.append(path.relative_to(ROOT))

    print(f"Updated {len(changed)} files:")
    for path in changed:
        print(f"  {path}")


if __name__ == "__main__":
    main()
