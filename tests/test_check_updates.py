import datetime as dt
import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))
import check_updates  # noqa: E402

TRACKING = {
    "bundled": {"32024R1689": "", "32026R1744": ""},
    "reviewed": {"32025R0454": ""},
    "review_after_days": 90,
    "watch": [{"name": "Page", "url": "https://example.eu", "why": "Why", "last_reviewed": "2026-10-01"}],
}


def row(celex, rel="resource_legal_amends_resource_legal", target="32024R1689"):
    return {"celex": celex, "rel": rel, "target": target, "date": "2027-01-01", "title": f"Act {celex}"}


class CheckUpdatesTests(unittest.TestCase):
    def test_reports_only_unknown_relevant_acts(self):
        rows = [
            row("32026R1744"),  # bundled
            row("32025R0454", "resource_legal_based_on_resource_legal"),  # reviewed
            row("52026IP0066", "resource_legal_based_on_resource_legal"),  # parliament resolution
            row("32027R0001"),  # new amendment
            row("32024R1689R(05)", "resource_legal_corrects_resource_legal"),  # English correction
        ]
        found = check_updates.new_acts(rows, TRACKING)
        self.assertEqual(set(found), {"32027R0001", "32024R1689R(05)"})
        self.assertIn("corrects 32024R1689", found["32024R1689R(05)"]["links"])

    def test_watch_list_due_and_broken(self):
        ok = lambda url: 200  # noqa: E731
        self.assertEqual(check_updates.stale_watch(TRACKING, dt.date(2026, 11, 1), ok), [])
        self.assertEqual(len(check_updates.stale_watch(TRACKING, dt.date(2027, 2, 1), ok)), 1)
        broken = check_updates.stale_watch(TRACKING, dt.date(2026, 11, 1), lambda url: 404)
        self.assertIn("404", broken[0][1])

    def test_tracking_file_is_valid(self):
        import json
        data = json.loads((Path(__file__).resolve().parents[1] / "skills" / "eu-ai-act" / "tracking.json").read_text())
        for item in data["watch"]:
            dt.date.fromisoformat(item["last_reviewed"])
            self.assertTrue(item["url"].startswith("https://"))


if __name__ == "__main__":
    unittest.main()
