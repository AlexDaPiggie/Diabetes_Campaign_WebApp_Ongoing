from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]

class VerticalGapReductionTests(unittest.TestCase):
    def setUp(self):
        self.template = (ROOT / "templates" / "index.html").read_text(encoding="utf-8")
        self.css = (ROOT / "static" / "css" / "styles.css").read_text(encoding="utf-8")
        
        # Extract personal story section
        story_start = self.template.find('class="personal-story')
        story_end = self.template.find('<!-- ═══════════════ HERO ═══════════════ -->', story_start)
        self.story_html = self.template[story_start:story_end]

    def test_source_link_margins_reduced(self):
        self.assertIn("margin: 0.8rem auto 0.2rem;", self.css)

    def test_legend_margin_top_reduced(self):
        self.assertIn('mt-[19.2px]', self.story_html)

    def test_callout_margin_top_reduced(self):
        self.assertIn('mt-[12.8px]', self.story_html)
