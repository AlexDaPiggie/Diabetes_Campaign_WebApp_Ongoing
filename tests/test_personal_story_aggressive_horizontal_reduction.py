from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]

class AggressiveHorizontalReductionTests(unittest.TestCase):
    def setUp(self):
        self.template = (ROOT / "templates" / "index.html").read_text(encoding="utf-8")
        
        # Extract personal story section
        story_start = self.template.find('class="personal-story')
        story_end = self.template.find('<!-- ═══════════════ HERO ═══════════════ -->', story_start)
        self.story_html = self.template[story_start:story_end]

    def test_legend_aggressive_gaps_reduced(self):
        # Base/Mobile gap reduced from gap-x-4 (16px) to gap-x-2 (8px)
        self.assertIn('gap-x-2', self.story_html)
        # Desktop gap reduced from lg:gap-x-[25.6px] to lg:gap-x-4 (16px)
        self.assertIn('lg:gap-x-4', self.story_html)

    def test_label_max_width_reduced(self):
        # Max-width reduced from max-w-[100px] to max-w-[80px]
        self.assertIn('max-w-[80px]', self.story_html)
