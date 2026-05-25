from pathlib import Path
import unittest


ROOT = Path(__file__).resolve().parents[1]


class PersonalStoryTests(unittest.TestCase):
    def test_personal_story_uses_editorial_language(self):
        template = (ROOT / "templates" / "index.html").read_text(encoding="utf-8")
        css = (ROOT / "static" / "css" / "styles.css").read_text(encoding="utf-8")

        self.assertIn('class="personal-story--editorial', template)
        self.assertIn("personal-story__accent-rule", template)
        self.assertIn("personal-story__intro", template)
        self.assertIn("data-reveal-delay", template)

        self.assertIn(".personal-story--editorial {", css)
        self.assertIn("background-color: #FCFAF7", css)
        self.assertIn("color: #0f2a4a", css)
