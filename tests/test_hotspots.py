import ast
import re
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SOURCE_HTML = ROOT / "index.html"
DIST_HTML = ROOT / "dist" / "index.html"


def load_people(html):
    match = re.search(r"const people = \[(.*?)\n    \];", html, re.DOTALL)
    if not match:
        raise AssertionError("people collection not found")
    return ast.literal_eval("[" + match.group(1) + "]")


class HotspotDataTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.html = SOURCE_HTML.read_text(encoding="utf-8")
        cls.people = load_people(cls.html)

    def test_source_and_dist_are_identical(self):
        self.assertEqual(self.html, DIST_HTML.read_text(encoding="utf-8"))

    def test_v7_is_the_only_visible_collage(self):
        self.assertEqual(self.html.count('class="portrait-frame"'), 1)
        self.assertIn('href="assets/collage-yacht-v7.png"', self.html)
        self.assertNotIn('href="assets/collage-yacht-v4.png"', self.html)

    def test_people_collection_has_30_unique_records(self):
        self.assertEqual(len(self.people), 30)
        self.assertEqual(len({person[0] for person in self.people}), 30)

    def test_hotspots_fit_the_v7_viewbox(self):
        width, height = 1586, 992
        for name, cx, cy, rx, ry in self.people:
            with self.subTest(name=name):
                self.assertGreaterEqual(cx - rx, 0)
                self.assertLessEqual(cx + rx, width)
                self.assertGreaterEqual(cy - ry, 0)
                self.assertLessEqual(cy + ry, height)


if __name__ == "__main__":
    unittest.main()
