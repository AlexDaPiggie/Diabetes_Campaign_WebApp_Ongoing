from pathlib import Path
import unittest


ROOT = Path(__file__).resolve().parents[1]


class ScrollProgressTests(unittest.TestCase):
    def test_fixed_scroll_progress_bar_is_rendered_once(self):
        base = (ROOT / "templates" / "base.html").read_text(encoding="utf-8")

        self.assertEqual(base.count('class="scroll-progress"'), 1)
        self.assertEqual(base.count('class="scroll-progress__bar"'), 1)
        self.assertIn('aria-hidden="true"', base)

    def test_scroll_progress_bar_is_fixed_to_bottom(self):
        css = (ROOT / "static" / "css" / "styles.css").read_text(encoding="utf-8")

        self.assertIn(".scroll-progress {", css)
        self.assertIn(".scroll-progress__bar {", css)
        progress_start = css.index(".scroll-progress {")
        progress_end = css.index(".scroll-progress__bar {", progress_start)
        progress_css = css[progress_start:progress_end]
        bar_start = progress_end
        bar_end = css.index("/* Reveal animations", bar_start)
        bar_css = css[bar_start:bar_end]

        self.assertIn("position: fixed", progress_css)
        self.assertIn("bottom: 0", progress_css)
        self.assertIn("inset-inline: 0", progress_css)
        self.assertIn("z-index: 60", progress_css)
        self.assertIn("transform-origin: left center", bar_css)
        self.assertIn("transform: scaleX(0)", bar_css)

    def test_native_horizontal_scrollbar_is_not_shown_under_progress_bar(self):
        css = (ROOT / "static" / "css" / "styles.css").read_text(encoding="utf-8")

        self.assertIn("overflow-x: hidden", css)
        self.assertIn("::-webkit-scrollbar:horizontal", css)
        self.assertIn("display: none", css)

    def test_scroll_progress_is_updated_from_page_scroll_position(self):
        js = (ROOT / "static" / "js" / "main.js").read_text(encoding="utf-8")

        self.assertIn("scroll-progress__bar", js)
        self.assertIn("document.documentElement.scrollHeight - window.innerHeight", js)
        self.assertIn("window.scrollY / maxScroll", js)
        self.assertIn("bar.style.transform = `scaleX(${progress})`", js)
        self.assertIn("window.addEventListener('resize'", js)
