#!/usr/bin/env python3
"""Check skill packaging and local references; never evaluates profitability."""

from __future__ import annotations

import json
import re
import sys
from datetime import date
from pathlib import Path
from urllib.parse import unquote, urlsplit

try:
    import yaml
except ImportError:
    sys.exit("Install validation dependencies: python -m pip install -r requirements-dev.txt")

ROOT = Path(__file__).resolve().parents[1]
SLUG = re.compile(r"[a-z0-9]+(?:-[a-z0-9]+)*\Z")
LINK = re.compile(r"!?\[[^\]\n]*\]\(([^)\n]+)\)")
errors: list[str] = []


def error(path: Path, message: str) -> None:
    errors.append(f"{path.relative_to(ROOT)}: {message}")


def check_links(path: Path, content: str) -> None:
    # This project uses inline Markdown links; strip code before checking prose.
    prose = re.sub(r"```[^\n]*\n.*?```", "", content, flags=re.S)
    prose = re.sub(r"`[^`\n]*`", "", prose)
    for match in LINK.finditer(prose):
        target = match.group(1).strip().strip("<>")
        if target.startswith("#"):
            continue
        parsed = urlsplit(target)
        if parsed.scheme:
            if parsed.scheme not in {"https", "http", "mailto"}:
                error(path, f"unexpected link scheme: {target}")
            continue
        destination = (path.parent / unquote(parsed.path)).resolve()
        if not destination.is_relative_to(ROOT):
            error(path, f"local link escapes repository: {target}")
        elif not destination.exists():
            error(path, f"missing local link: {target}")


def main() -> int:
    try:
        catalog = json.loads((ROOT / "catalog.json").read_text())
        entries = catalog["skills"]
        if not isinstance(entries, list) or not entries:
            raise ValueError("skills must be a non-empty list")
        ids = [entry["id"] for entry in entries]
        if len(ids) != len(set(ids)):
            raise ValueError("duplicate skill ids")
        if any(not isinstance(item, str) or not SLUG.fullmatch(item) for item in ids):
            raise ValueError("invalid skill id")
    except (OSError, ValueError, KeyError, TypeError) as exc:
        print(f"catalog.json: {exc}", file=sys.stderr)
        return 1

    skill_paths = sorted((ROOT / "skills").glob("*/SKILL.md"))
    actual = {path.parent.name for path in skill_paths}
    if actual != set(ids):
        error(ROOT / "catalog.json", f"catalog/directory mismatch: {sorted(actual ^ set(ids))}")

    for path in skill_paths:
        content = path.read_text()
        match = re.match(r"\A---\n(.*?)\n---\n", content, re.S)
        if not match:
            error(path, "missing YAML frontmatter")
            continue
        try:
            meta = yaml.safe_load(match.group(1))
        except yaml.YAMLError as exc:
            error(path, f"invalid YAML: {exc}")
            continue
        if not isinstance(meta, dict):
            error(path, "frontmatter must be a mapping")
            continue
        name, description = meta.get("name"), meta.get("description")
        if name != path.parent.name or not isinstance(name, str) or len(name) > 64:
            error(path, "name must match its directory and be at most 64 characters")
        if not isinstance(description, str) or not 1 <= len(description.strip()) <= 1024:
            error(path, "description must be 1–1024 characters")
        if not content[match.end():].strip():
            error(path, "empty instructions")
        if re.search(r"\[TODO[:：]|\[INSERT|<your-", content, re.I):
            error(path, "unfinished scaffold placeholder")
        source = path.parent / "references" / "sources.md"
        if not source.exists():
            error(path, "missing references/sources.md")
            continue
        source_content = source.read_text()
        if not re.search(r"https://\S+", source_content):
            error(source, "no source URLs")
        dates = re.findall(r"\b\d{4}-\d{2}-\d{2}\b", source_content)
        if not dates:
            error(source, "no dated source record")
        for value in dates:
            try:
                date.fromisoformat(value)
            except ValueError:
                error(source, f"invalid date: {value}")

    for path in sorted(ROOT.rglob("*.md")):
        if any(part in {".git", ".venv", ".agents", ".claude", "private"} for part in path.relative_to(ROOT).parts):
            continue
        check_links(path, path.read_text())

    if errors:
        print("Validation failed:\n" + "\n".join(f"- {item}" for item in errors), file=sys.stderr)
        return 1
    print(f"Validated {len(skill_paths)} skills: manifests, catalog, source records and local links.")
    print("Scope: packaging only. No external link, client-runtime or investment-performance validation.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

