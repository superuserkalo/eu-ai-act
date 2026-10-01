import hashlib
import json
import re
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SKILL = ROOT / "skills" / "eu-ai-act"


class SkillTests(unittest.TestCase):
    def test_single_skill_and_manifest(self):
        self.assertEqual(
            sorted(path.parent.name for path in (ROOT / "skills").glob("*/SKILL.md")),
            ["eu-ai-act"],
        )
        manifest = json.loads((ROOT / "plugin.json").read_text())
        self.assertEqual(manifest["name"], "eu-ai-act")
        self.assertEqual(manifest["repository"], "https://github.com/superuserkalo/eu-ai-act")
        self.assertFalse(list(ROOT.glob("*/plugin.json")))

    def test_license_ships_with_skill(self):
        root = (ROOT / "LICENSE").read_text()
        self.assertTrue(root.startswith("MIT License"))
        self.assertEqual(root, (SKILL / "LICENSE").read_text())

    def test_frontmatter(self):
        text = (SKILL / "SKILL.md").read_text()
        self.assertTrue(text.startswith("---\n"))
        frontmatter = text.split("---\n", 2)[1]
        self.assertRegex(frontmatter, r"(?m)^name: eu-ai-act$")
        description = re.search(r"(?m)^description: (.+)$", frontmatter).group(1)
        self.assertLessEqual(len(description), 1024)
        self.assertIn("references/articles/", text)
        self.assertIn("not legal advice", text)
        for link in re.findall(r"\((references/[^)]+\.md)\)", text):
            self.assertTrue((SKILL / link).is_file(), link)

    def test_provenance(self):
        provenance = json.loads((SKILL / "SOURCE.json").read_text())
        self.assertEqual(provenance["documents"]["act"]["celex"], "32024R1689")
        self.assertEqual(provenance["documents"]["omnibus"]["celex"], "32026R1744")
        for item in provenance["texts"] + provenance["supplements"]:
            data = (SKILL / item["reference"]).read_bytes()
            self.assertEqual(item["bytes"], len(data), item["reference"])
            self.assertEqual(item["sha256"], hashlib.sha256(data).hexdigest())
        self.assertTrue((SKILL / "NOTICE.md").is_file())

    def test_layout(self):
        referenced = {item["reference"] for item in json.loads((SKILL / "SOURCE.json").read_text())["texts"]}
        self.assertEqual(len([r for r in referenced if r.startswith("references/articles/")]), 119)
        self.assertEqual(len([r for r in referenced if r.startswith("references/recitals/")]), 180)
        points = set()
        for ref in referenced:
            text = (SKILL / ref).read_text()
            points.update(int(n) for n in re.findall(r"Article 1, point \((\d+)\)", text))
        self.assertEqual(points, set(range(1, 44)))
        amended = (SKILL / "references/articles/050.md").read_text()
        self.assertLess(
            amended.index("## Amended by Regulation (EU) 2026/1744"),
            amended.index("## Text as published in 2024"),
        )


if __name__ == "__main__":
    unittest.main()
