from pathlib import Path
import unittest


ROOT = Path(__file__).resolve().parents[1]


class ContentTypographyTests(unittest.TestCase):
    def test_base_body_typography_classes(self):
        template = (ROOT / "templates" / "base.html").read_text(encoding="utf-8")
        # Verify Open Sans 300 typography on body
        self.assertIn('font-light text-[18px] md:text-[20px] leading-[25.2px] md:leading-[28px] tracking-tight', template)
        # Verify Open Sans import
        self.assertIn('family=Open+Sans:wght@300;400;500;600;700', template)

    def test_content_page_copy_matches_body_size(self):
        template = (ROOT / "templates" / "index.html").read_text(encoding="utf-8")

        # Hero subtitle
        self.assertIn('<p class="motion-load text-[18px] md:text-[20px] text-ink-dim leading-relaxed max-w-lg mb-8 animate-fade-up"', template)
        # Section body
        self.assertIn('<p class="text-[18px] md:text-[20px] text-ink-dim leading-relaxed mb-6 reveal"', template)
        # List items
        self.assertIn('<li class="flex items-start gap-3 text-[18px] md:text-[20px] text-ink-dim leading-relaxed">', template)
        # Section link
        self.assertIn('class="inline-flex items-center gap-1.5 text-[18px] md:text-[20px] font-medium text-accent-bright', template)

    def test_heading_scaling(self):
        template = (ROOT / "templates" / "index.html").read_text(encoding="utf-8")
        # Hero headline (72px -> 77.76px)
        self.assertIn('text-[51.84px] sm:text-[64.8px] lg:text-[77.76px]', template)
        # Section title (36px -> 38.88px)
        self.assertIn('text-[38.88px] sm:text-[51.84px]', template)

    def test_ui_component_scaling(self):
        template = (ROOT / "templates" / "index.html").read_text(encoding="utf-8")
        # Eyebrows (12px -> 16px)
        self.assertIn('text-[16px] font-semibold tracking-widest uppercase', template)
        # Buttons (14px -> 16px)
        self.assertIn('text-[16px] font-medium', template)
