from pathlib import Path
import unittest


ROOT = Path(__file__).resolve().parents[1]


class PersonalStoryTests(unittest.TestCase):
    def test_personal_story_layout_uses_iceberg_grid(self):
        template = (ROOT / "templates" / "index.html").read_text(encoding="utf-8")

        self.assertIn('class="personal-story', template)
        self.assertIn("personal-story__grid", template)
        self.assertIn("personal-story__stats", template)
        self.assertIn("personal-story__source", template)
        self.assertIn("iceberg-svg", template)
        self.assertNotIn("personal-story--editorial", template)
        self.assertNotIn("max-w-4xl mx-auto text-center", template)
        self.assertNotIn("personal-story__accent-rule", template)
        self.assertIn("data-reveal-delay", template)

    def test_personal_story_css_vitals(self):
        css = (ROOT / "static" / "css" / "styles.css").read_text(encoding="utf-8")

        self.assertIn(".personal-story {", css)
        self.assertIn(".personal-story__grid", css)
        self.assertIn(".personal-story__stats", css)
        self.assertIn(".personal-story__source", css)
        self.assertIn("linear-gradient", css)
