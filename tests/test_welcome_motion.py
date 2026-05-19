from pathlib import Path
import unittest


ROOT = Path(__file__).resolve().parents[1]


class WelcomeMotionTests(unittest.TestCase):
    def test_welcome_motion_sequence_hooks_are_defined(self):
        template = (ROOT / "templates" / "index.html").read_text(encoding="utf-8")
        css = (ROOT / "static" / "css" / "styles.css").read_text(encoding="utf-8")

        self.assertIn("motion-welcome-sweep", template)
        self.assertIn("motion-welcome-title", template)
        self.assertIn("motion-welcome-divider", template)
        self.assertIn("motion-welcome-copy", template)

        self.assertIn("motionWelcomeSweep", css)
        self.assertIn("transform-origin: left center", css)
        self.assertIn("background: linear-gradient(90deg, #3498db 0%, #65b8e8 48%, #a2d5f2 100%)", css)
        self.assertIn(".motion-welcome-title", css)
        self.assertIn(".motion-welcome-divider", css)
        self.assertIn(".motion-welcome-copy", css)

    def test_reduced_motion_does_not_leave_welcome_sweep_cover_visible(self):
        css = (ROOT / "static" / "css" / "styles.css").read_text(encoding="utf-8")

        reduced_motion_start = css.index("@media (prefers-reduced-motion: reduce)")
        reduced_motion_css = css[reduced_motion_start:]

        self.assertIn(".motion-welcome-sweep::before", reduced_motion_css)
        self.assertIn("transform: scaleX(1)", reduced_motion_css)

    def test_welcome_sweep_layer_is_never_white(self):
        css = (ROOT / "static" / "css" / "styles.css").read_text(encoding="utf-8")
        sweep_start = css.index(".motion-welcome-sweep::before")
        sweep_end = css.index(".motion-welcome::after", sweep_start)
        sweep_css = css[sweep_start:sweep_end]

        self.assertNotIn("background: #fafcff", sweep_css)
        self.assertIn("background: linear-gradient(90deg, #1d5fad 0%, #3498db 48%, #a2d5f2 100%)", sweep_css)

    def test_section_separators_use_welcome_gradient_and_fast_sweep(self):
        template = (ROOT / "templates" / "index.html").read_text(encoding="utf-8")
        css = (ROOT / "static" / "css" / "styles.css").read_text(encoding="utf-8")

        welcome_to_hero = template[
            template.index("</section>"):template.index('<section class="motion-hero')
        ]
        self.assertNotIn("motion-stripe", welcome_to_hero)

        sections_loop_start = template.index("{% for section in sections %}")
        sections_loop_end = template.index("{% endfor %}\n\n<!--", sections_loop_start)
        sections_loop = template[sections_loop_start:sections_loop_end]
        self.assertIn("motion-stripe", sections_loop)
        self.assertIn("{% if not loop.last %}", sections_loop)
        self.assertIn("background: linear-gradient(90deg, #3498db 0%, #65b8e8 48%, #a2d5f2 100%)", css)
        self.assertIn("animation: motionStripe 1.35s ease-in-out infinite", css)

    def test_section_separators_reveal_from_white_background(self):
        css = (ROOT / "static" / "css" / "styles.css").read_text(encoding="utf-8")

        stripe_start = css.index(".motion-stripe {")
        stripe_end = css.index(".motion-logo::after", stripe_start)
        stripe_css = css[stripe_start:stripe_end]
        reveal_start = css.index(".motion-stripe::before {")
        reveal_end = css.index(".motion-stripe::after {", reveal_start)
        reveal_css = css[reveal_start:reveal_end]

        self.assertIn("background: #fafcff", stripe_css)
        self.assertIn(".motion-stripe::before", css)
        self.assertIn("background: linear-gradient(90deg, #3498db 0%, #65b8e8 48%, #a2d5f2 100%)", reveal_css)
        self.assertIn("animation: motionStripeReveal 420ms cubic-bezier(0.16, 1, 0.3, 1) both", reveal_css)

        reduced_motion_start = css.index("@media (prefers-reduced-motion: reduce)")
        reduced_motion_css = css[reduced_motion_start:]
        self.assertIn(".motion-stripe::before", reduced_motion_css)
        self.assertIn("transform: scaleX(1)", reduced_motion_css)
