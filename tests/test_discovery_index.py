"""Publication invariants: descriptions stay current and packs resolve."""

import importlib.util
import json
import shutil
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location("index_builder", ROOT / "scripts/build_index.py")
BUILDER = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(BUILDER)


class DiscoveryIndexTests(unittest.TestCase):
    def setUp(self):
        self.temporary = tempfile.TemporaryDirectory(prefix="investing-index-")
        self.addCleanup(self.temporary.cleanup)
        self.root = Path(self.temporary.name)
        shutil.copytree(ROOT / "skills", self.root / "skills")
        shutil.copytree(ROOT / "scripts", self.root / "scripts", ignore=shutil.ignore_patterns("__pycache__"))
        for name in ("catalog.json", "skills-index.json"):
            shutil.copy2(ROOT / name, self.root / name)

    def test_checked_in_metadata_matches_skill_files(self):
        self.assertEqual(BUILDER.make_index(self.root), json.loads((self.root / "skills-index.json").read_text()))

    def test_check_rejects_changed_description(self):
        path = next((self.root / "skills").glob("*/SKILL.md"))
        lines = path.read_text().splitlines()
        index = next(i for i, line in enumerate(lines) if line.startswith("description:"))
        lines[index] = 'description: "A changed research task requiring a fresh index."'
        path.write_text("\n".join(lines) + "\n")
        result = subprocess.run(
            [sys.executable, str(self.root / "scripts/build_index.py"), "--check"],
            capture_output=True, text=True, check=False,
        )
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("stale", result.stdout + result.stderr)

    def test_rejects_pack_pointing_to_missing_skill(self):
        path = self.root / "catalog.json"
        data = json.loads(path.read_text())
        data["packs"][0]["skills"].append("missing-framework")
        path.write_text(json.dumps(data))
        with self.assertRaisesRegex(ValueError, "pack"):
            BUILDER.make_index(self.root)


if __name__ == "__main__":
    unittest.main()

