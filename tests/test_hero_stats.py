from pathlib import Path
import json
import subprocess
import textwrap
import unittest


ROOT = Path(__file__).resolve().parents[1]


def run_stat_animation(prefers_reduced_motion: bool) -> list[str]:
    script = textwrap.dedent(
        """
        const fs = require('fs');
        const vm = require('vm');
        const path = require('path');

        const mainJs = fs.readFileSync(path.join(process.cwd(), 'static', 'js', 'main.js'), 'utf8');
        const elements = ['537M', '1 in 2', '90%'].map((target) => ({
          dataset: { targetNumber: target, targetText: target },
          textContent: '0',
          classList: { add() {}, remove() {} },
        }));
        const rafQueue = [];
        const observers = [];

        global.window = {
          matchMedia: () => ({ matches: __REDUCED_MOTION__ }),
          addEventListener() {},
          scrollY: 0,
          innerHeight: 100,
          scrollTo() {},
        };
        global.document = {
          documentElement: { scrollHeight: 1000 },
          querySelector() { return null; },
          querySelectorAll(selector) {
            if (selector === '.animate-number') return elements;
            return [];
          },
        };
        global.IntersectionObserver = class {
          constructor(callback) {
            this.callback = callback;
            this.targets = [];
            observers.push(this);
          }

          observe(target) {
            this.targets.push(target);
          }

          unobserve() {}
        };
        global.requestAnimationFrame = (callback) => {
          rafQueue.push(callback);
          return rafQueue.length;
        };

        vm.runInThisContext(mainJs, { filename: 'main.js' });

        for (const observer of observers) {
          for (const target of observer.targets) {
            observer.callback([{ isIntersecting: true, target }]);
          }
        }

        let time = 0;
        while (rafQueue.length) {
          const callback = rafQueue.shift();
          time += 100;
          callback(time);
        }

        console.log(JSON.stringify(elements.map((element) => element.textContent)));
        """
    ).replace("__REDUCED_MOTION__", str(prefers_reduced_motion).lower())

    completed = subprocess.run(
        ["node", "-e", script],
        cwd=ROOT,
        capture_output=True,
        text=True,
        check=False,
    )

    if completed.returncode != 0:
        raise AssertionError(completed.stderr.strip() or completed.stdout.strip())

    return json.loads(completed.stdout)


class HeroStatsAnimationTests(unittest.TestCase):
    def test_stat_animation_preserves_full_target_text_for_mixed_values(self):
        rendered_values = run_stat_animation(prefers_reduced_motion=False)

        self.assertEqual(rendered_values, ["537M", "1 in 2", "90%"])

    def test_reduced_motion_uses_final_stat_text_without_stripping_units(self):
        rendered_values = run_stat_animation(prefers_reduced_motion=True)

        self.assertEqual(rendered_values, ["537M", "1 in 2", "90%"])
