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
        self.assertIn("waffle-chart", template)
        self.assertIn("waffle-grid", template)
        self.assertIn("waffle-icon", template)
        self.assertNotIn("personal-story--editorial", template)
        self.assertNotIn("max-w-4xl mx-auto text-center", template)
        self.assertNotIn("personal-story__accent-rule", template)
        self.assertIn("data-reveal-delay", template)

    def test_personal_story_typography(self):
        template = (ROOT / "templates" / "index.html").read_text(encoding="utf-8")
        
        # Extract personal story section to avoid false positives from other sections
        story_start = template.find('class="personal-story')
        story_end = template.find('<!-- HERO -->', story_start)
        if story_end == -1: # Fallback if marker is different
             story_end = template.find('<!-- ═══════════════ HERO ═══════════════ -->', story_start)
        
        story_html = template[story_start:story_end]
        
        # Check for original mobile size
        self.assertIn('text-[18px]', story_html)
        # Check for original desktop size
        self.assertIn('md:text-[20px]', story_html)
        # Ensure larger sizes are gone
        self.assertNotIn('text-[22px]', story_html)
        self.assertNotIn('md:text-[24px]', story_html)

    def test_personal_story_css_vitals(self):
        css = (ROOT / "static" / "css" / "styles.css").read_text(encoding="utf-8")

        self.assertIn(".personal-story {", css)
        self.assertIn(".personal-story__grid", css)
        self.assertIn(".personal-story__stats", css)
        self.assertIn(".personal-story__source", css)
        self.assertIn("linear-gradient", css)
