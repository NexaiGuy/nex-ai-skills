"""Checks for the root catalog router and the existing marketplace layout.

The skills CLI treats a valid repository-root SKILL.md as the whole package and
returns before it reads skills/, unless that file is metadata.internal or the
caller passes --full-depth. These tests lock the router to the internal form
and lock the plugin manifests to the guides already in skills/.
"""

from __future__ import annotations

import json
import re
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
ALLOWED_FRONTMATTER = {
    "name",
    "description",
    "license",
    "compatibility",
    "metadata",
    "allowed-tools",
}
NAME_RE = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")
LINK_RE = re.compile(r"\[[^\]]+\]\(([^)\s]+)\)")
RESERVED_NAME_PARTS = ("claude", "anthropic")


def split_frontmatter(text: str) -> tuple[str, str]:
    if not text.startswith("---\n"):
        raise AssertionError("SKILL.md must start with YAML frontmatter")
    end = text.find("\n---\n", 4)
    if end < 0:
        raise AssertionError("SKILL.md frontmatter is not closed")
    return text[4:end], text[end + 5 :]


def parse_scalar(raw: str):
    value = raw.strip()
    if value in {"true", "false"} and value == value.lower():
        return value == "true"
    if len(value) >= 2 and value[0] == value[-1] and value[0] in {'"', "'"}:
        quote = value[0]
        inner = value[1:-1]
        if quote == "'":
            return inner.replace("''", "'")
        return bytes(inner, "utf-8").decode("unicode_escape")
    return value


def parse_frontmatter(text: str) -> tuple[dict, str]:
    raw, body = split_frontmatter(text)
    data: dict = {}
    current = None
    for line_number, line in enumerate(raw.splitlines(), start=2):
        if not line.strip():
            continue
        if line.startswith("  ") and current is not None:
            key, _, value = line.strip().partition(":")
            if not key or not value.strip():
                raise AssertionError(f"invalid nested frontmatter on line {line_number}")
            data[current][key] = parse_scalar(value)
            continue
        if line.startswith(" "):
            raise AssertionError(f"unexpected indent on line {line_number}")
        key, separator, value = line.partition(":")
        if not separator:
            raise AssertionError(f"invalid frontmatter on line {line_number}")
        if value.strip():
            data[key] = parse_scalar(value)
            current = None
        else:
            data[key] = {}
            current = key
    return data, body


def skill_dirs(path: Path) -> list[Path]:
    return sorted(item.parent for item in path.glob("*/SKILL.md") if item.is_file())


class CatalogEntryTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.root_text = (ROOT / "SKILL.md").read_text(encoding="utf-8")
        cls.frontmatter, cls.body = parse_frontmatter(cls.root_text)
        cls.marketplace = json.loads(
            (ROOT / ".claude-plugin" / "marketplace.json").read_text(encoding="utf-8")
        )

    def test_root_frontmatter_matches_agent_skills_rules(self):
        self.assertEqual(set(self.frontmatter), {"name", "description", "license", "compatibility", "metadata"})
        self.assertLessEqual(set(self.frontmatter), ALLOWED_FRONTMATTER)
        name = self.frontmatter["name"]
        description = self.frontmatter["description"]
        compatibility = self.frontmatter["compatibility"]
        self.assertIsInstance(name, str)
        self.assertIsInstance(description, str)
        self.assertIsInstance(compatibility, str)
        self.assertEqual(name, "nex-ai-skills")
        self.assertEqual(name, ROOT.name)
        self.assertRegex(name, NAME_RE)
        self.assertNotIn("--", name)
        for part in RESERVED_NAME_PARTS:
            self.assertNotIn(part, name)
        self.assertGreaterEqual(len(description), 1)
        self.assertLessEqual(len(description), 1024)
        self.assertLessEqual(len(compatibility), 500)
        self.assertIn("route", description.lower())
        self.assertIn("skills/", description)
        self.assertIn("do not perform", description.lower())
        self.assertEqual(self.frontmatter["license"], "MIT")
        metadata = self.frontmatter["metadata"]
        self.assertEqual(metadata["author"], "Nex AI")
        self.assertIsInstance(metadata["version"], str)
        # Boolean true, not the string "true": the skills CLI skips only `=== true`.
        self.assertIs(metadata["internal"], True)

    def test_root_skill_is_a_router_not_a_copied_guide(self):
        self.assertLess(len(self.root_text.splitlines()), 220)
        self.assertNotRegex(self.root_text, r"\b(79|81|158|311)\b")
        self.assertIn("metadata.internal", self.body)
        self.assertIn("nex-systemd-starter", self.body)
        self.assertIn("nex-1099-contractor-pack", self.body)
        descriptions = []
        for skill_dir in skill_dirs(ROOT / "skills"):
            data, _ = parse_frontmatter(
                (skill_dir / "SKILL.md").read_text(encoding="utf-8")
            )
            descriptions.append(data["description"])
            self.assertNotEqual(self.frontmatter["name"], data["name"])
        self.assertNotIn(self.frontmatter["description"], descriptions)
        self.assertNotIn("# Secret Scan", self.body)

    def test_relative_links_resolve_inside_the_repository(self):
        links = LINK_RE.findall(self.root_text)
        self.assertGreaterEqual(len(links), 8)
        for link in links:
            self.assertFalse(link.startswith(("http://", "https://", "mailto:")))
            self.assertNotIn("..", Path(link).parts)
            target = ROOT / link
            self.assertTrue(target.exists(), link)

    def test_router_follows_the_marketplace_manifest(self):
        plugins = self.marketplace["plugins"]
        self.assertEqual(len(plugins), 6)
        for plugin in plugins:
            name = plugin["name"]
            description = plugin["description"]
            source = plugin["source"]
            self.assertIn(f"`{name}`", self.body)
            self.assertIn(description, self.body)
            self.assertIn(source.removeprefix("./"), self.body)
            self.assertIn(f"/plugin install {name}@nex-ai-skills", self.body)
            plugin_dir = ROOT / source
            manifest = json.loads(
                (plugin_dir / ".claude-plugin" / "plugin.json").read_text(encoding="utf-8")
            )
            self.assertEqual(manifest["name"], name)
            self.assertEqual(manifest["license"], "MIT")
            self.assertFalse(Path(source).is_absolute())
            self.assertNotIn("..", Path(source).parts)

    def test_existing_guides_and_plugin_copies_stay_paired(self):
        catalog = {path.name: path for path in skill_dirs(ROOT / "skills")}
        packaged: dict[str, Path] = {}
        for plugin in self.marketplace["plugins"]:
            for path in skill_dirs(ROOT / plugin["source"] / "skills"):
                self.assertNotIn(path.name, packaged)
                packaged[path.name] = path
        self.assertEqual(set(catalog), set(packaged))
        for name, catalog_dir in catalog.items():
            catalog_file = catalog_dir / "SKILL.md"
            packaged_file = packaged[name] / "SKILL.md"
            self.assertEqual(catalog_file.read_bytes(), packaged_file.read_bytes())
            data, body = parse_frontmatter(catalog_file.read_text(encoding="utf-8"))
            self.assertEqual(data["name"], name)
            self.assertRegex(data["name"], NAME_RE)
            for part in RESERVED_NAME_PARTS:
                self.assertNotIn(part, data["name"])
            self.assertIsInstance(data["description"], str)
            self.assertGreaterEqual(len(data["description"]), 1)
            self.assertLessEqual(len(data["description"]), 1024)
            self.assertEqual(data["license"], "MIT")
            self.assertTrue(body.strip())

    def test_internal_root_does_not_replace_bulk_discovery(self):
        """Lock the flag the skills CLI requires for bulk discovery.

        discoverSkills() returns the root skill immediately unless that file is
        skipped. parseSkillMd() skips metadata.internal only when the value is
        boolean true; the string "true" still shadows skills/.
        """
        self.assertIs(self.frontmatter["metadata"]["internal"], True)
        # Bulk discovery skips an internal root skill and keeps every guide.
        discovered = [path.name for path in skill_dirs(ROOT / "skills")]
        self.assertNotIn(self.frontmatter["name"], discovered)
        self.assertEqual(discovered, sorted(discovered))

    def test_readme_keeps_existing_install_commands(self):
        readme = (ROOT / "README.md").read_text(encoding="utf-8")
        for command in (
            "/plugin marketplace add NexaiGuy/nex-ai-skills",
            "/plugin install nex-dev-essentials@nex-ai-skills",
            "/plugin install nex-web-audits@nex-ai-skills",
            "/plugin install nex-browser-extensions@nex-ai-skills",
            "/plugin install nex-compliance@nex-ai-skills",
            "/plugin install nex-finance-property@nex-ai-skills",
            "/plugin install nex-business-operations@nex-ai-skills",
            "npx skills add NexaiGuy/nex-ai-skills",
            "npx skills add NexaiGuy/nex-ai-skills --skill secret-scan",
            "npx skills add NexaiGuy/nex-ai-skills -a cursor",
            "npx skills add NexaiGuy/nex-ai-skills -a codex",
            "npx skills add NexaiGuy/nex-ai-skills -a claude-code",
        ):
            self.assertIn(command, readme)
        self.assertIn("metadata.internal", readme)


if __name__ == "__main__":
    unittest.main()
