import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SOURCE_HTML = ROOT / "index.html"
DIST_HTML = ROOT / "dist" / "index.html"
WORKFLOW = ROOT / ".github" / "workflows" / "deploy-pages.yml"


class PagesDeploymentTests(unittest.TestCase):
    def test_public_html_requests_noindex(self):
        robots = '<meta name="robots" content="noindex, nofollow" />'
        self.assertIn(robots, SOURCE_HTML.read_text(encoding="utf-8"))
        self.assertIn(robots, DIST_HTML.read_text(encoding="utf-8"))

    def test_workflow_uses_pages_permissions_and_official_actions(self):
        workflow = WORKFLOW.read_text(encoding="utf-8")
        for expected in (
            "contents: read",
            "pages: write",
            "id-token: write",
            "actions/checkout@v7",
            "actions/configure-pages@v5",
            "actions/upload-pages-artifact@v5",
            "actions/deploy-pages@v5",
        ):
            with self.subTest(expected=expected):
                self.assertIn(expected, workflow)

    def test_workflow_packages_only_the_public_page_and_active_portrait(self):
        workflow = WORKFLOW.read_text(encoding="utf-8")
        self.assertIn("cp dist/index.html", workflow)
        self.assertIn("cp dist/assets/collage-yacht-v7.png", workflow)
        self.assertNotIn("path: ./dist", workflow)
        self.assertNotIn("secrets.", workflow)


if __name__ == "__main__":
    unittest.main()
