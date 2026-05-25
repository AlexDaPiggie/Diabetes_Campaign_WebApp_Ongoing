from pathlib import Path
import unittest


ROOT = Path(__file__).resolve().parents[1]


class PersonalStoryTests(unittest.TestCase):
    def test_personal_story_layout_is_centered(self):
        template = (ROOT / "templates" / "index.html").read_text(encoding="utf-8")

        self.assertIn('class="personal-story', template)
        self.assertNotIn("personal-story--editorial", template)
        self.assertIn("text-center", template)
        self.assertNotIn("personal-story__accent-rule", template)
        self.assertIn("data-reveal-delay", template)

    def test_personal_story_css_vitals(self):
        css = (ROOT / "static" / "css" / "styles.css").read_text(encoding="utf-8")

        self.assertIn(".personal-story {", css)
        self.assertIn("linear-gradient", css)
