from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]

class SizeReductionTests(unittest.TestCase):
    def setUp(self):
        self.template = (ROOT / "templates" / "index.html").read_text(encoding="utf-8")
        self.css = (ROOT / "static" / "css" / "styles.css").read_text(encoding="utf-8")
        
        # Extract personal story section
        story_start = self.template.find('class="personal-story')
        story_end = self.template.find('<!-- ═══════════════ HERO ═══════════════ -->', story_start)
        self.story_html = self.template[story_start:story_end]

    def test_waffle_container_size_reduced(self):
        self.assertIn(".waffle-container {\n  position: relative;\n  width: 100%;\n  max-width: 336px;", self.css)
        self.assertIn("@media (max-width: 767px) {\n  .waffle-grid {\n    grid-template-columns: repeat(10, 1fr);\n  }\n\n  .waffle-container {\n    max-width: 256px;\n  }\n}", self.css)

    def test_waffle_grid_gap_reduced(self):
        self.assertIn("gap: clamp(4px, 0.44vw, 6.4px);", self.css)

    def test_source_link_size_reduced(self):
        self.assertIn("font-size: 16px;", self.css)
        self.assertIn("max-width: 336px;", self.css)
        self.assertIn("@media (max-width: 767px) {\n  .personal-story__source {\n    max-width: 256px;\n  font-size: 13px;\n  }\n}", self.css)

    def test_legend_stats_size_reduced(self):
        # Stat number
        self.assertIn('text-[18px]', self.story_html)
        # Stat label
        self.assertIn('text-[11px]', self.story_html)
        # Stat icon (w-5)
        self.assertIn('w-5 h-5', self.story_html)
        # Gaps
        self.assertIn('gap-x-5', self.story_html)
        self.assertIn('lg:gap-x-8', self.story_html)

    def test_callout_size_reduced(self):
        self.assertIn('text-[11px]', self.story_html)
        self.assertIn('max-w-[307px]', self.story_html)
