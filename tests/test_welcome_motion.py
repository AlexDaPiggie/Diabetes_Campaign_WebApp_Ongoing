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
