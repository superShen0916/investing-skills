#!/usr/bin/env python3
"""Build this repository's discovery metadata (not a registry submission)."""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path

try:
    import yaml
except ImportError:
    sys.exit("Install validation dependencies: python -m pip install -r requirements-dev.txt")

ROOT = Path(__file__).resolve().parents[1]


def make_index(root: Path = ROOT) -> dict:
    catalog = json.loads((root / "catalog.json").read_text())
    entries = []
    for item in catalog["skills"]:
        slug = item["id"]
        if not isinstance(slug, str) or not re.fullmatch(r"[a-z0-9]+(?:-[a-z0-9]+)*", slug):
            raise ValueError("Invalid skill id")
        path = f"skills/{slug}/SKILL.md"
        match = re.match(r"\A---\n(.*?)\n---\n", (root / path).read_text(), re.S)
        if not match:
            raise ValueError(f"Missing frontmatter: {path}")
        metadata = yaml.safe_load(match.group(1))
        if not isinstance(metadata, dict) or metadata.get("name") != slug:
            raise ValueError(f"Invalid metadata: {path}")
        description = metadata.get("description")
        if not isinstance(description, str) or not description.strip():
            raise ValueError(f"Missing description: {path}")
        entries.append({
            "name": slug,
            "title": item["title"],
            "category": item["category"],
            "inspired_by": item["inspired_by"],
            "description": description,
            "path": path,
            "sources": f"skills/{slug}/references/sources.md",
            "status": item["status"],
        })
    ids = {item["name"] for item in entries}
    packs = catalog.get("packs", [])
    if len({pack["id"] for pack in packs}) != len(packs):
        raise ValueError("Duplicate pack ids")
    for pack in packs:
        members = pack["skills"]
        if not members or len(members) != len(set(members)) or set(members) - ids:
            raise ValueError(f"Invalid members in pack: {pack['id']}")
    return {
        "schema_version": 1,
        "repository": "https://github.com/superShen0916/investing-skills",
        "version": catalog["version"],
        "language": catalog["language"],
        "validation_scope": catalog["validation_scope"],
        "skills": entries,
        "packs": packs,
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", action="store_true", help="Fail if the checked-in index is stale")
    args = parser.parse_args()
    target = ROOT / "skills-index.json"
    try:
        index = make_index()
        if args.check:
            if not target.exists() or json.loads(target.read_text()) != index:
                sys.exit("skills-index.json is stale; run python scripts/build_index.py")
            print(f"Discovery index is current: {len(index['skills'])} skills, {len(index['packs'])} packs.")
        else:
            target.write_text(json.dumps(index, ensure_ascii=False, indent=2) + "\n")
            print(f"Built skills-index.json: {len(index['skills'])} skills, {len(index['packs'])} packs.")
    except (OSError, ValueError, KeyError, TypeError, yaml.YAMLError) as exc:
        print(f"Cannot build discovery index: {exc}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

