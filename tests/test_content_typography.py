from pathlib import Path
import unittest


ROOT = Path(__file__).resolve().parents[1]


class ContentTypographyTests(unittest.TestCase):
    def test_content_page_copy_matches_hero_paragraph_size(self):
        template = (ROOT / "templates" / "index.html").read_text(encoding="utf-8")

        self.assertIn('<p class="motion-load text-lg text-ink-dim leading-relaxed max-w-lg mb-8 animate-fade-up"', template)
        self.assertIn('<p class="text-lg text-ink-dim leading-relaxed mb-6 reveal"', template)
        self.assertIn('<li class="flex items-start gap-3 text-lg text-ink-dim leading-relaxed">', template)
        self.assertIn('<a href="{{ section.link.href }}" class="inline-flex items-center gap-1.5 text-lg font-medium text-accent-bright hover:gap-2.5 transition-all duration-200 reveal"', template)

