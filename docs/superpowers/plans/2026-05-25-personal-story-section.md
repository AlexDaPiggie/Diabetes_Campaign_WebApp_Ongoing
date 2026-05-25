# Personal Story Section Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Add a no-heading Personal Story editorial panel after Welcome and before Hero, using the story from `Guidelines/Personal_Story.md`.

**Architecture:** Keep the page data-driven by adding `personal_story.paragraphs` to `data/content.json`, then render one focused section in `templates/index.html`. Add only small CSS rules for the panel, quote accent, and ambient background while reusing the existing `reveal` and `motion-shimmer` behavior.

**Tech Stack:** FastAPI, Jinja2 templates, Tailwind CDN classes, plain CSS, plain JavaScript motion hooks already present in `static/js/main.js`, Python `unittest`.

---

## File Structure

- Modify `static/css/styles.css`: restore the current motion interval expected by existing tests, then add Personal Story section styles.
- Modify `data/content.json`: add `personal_story.paragraphs` after `welcome`.
- Modify `templates/index.html`: render the Personal Story section immediately after the Welcome section.
- Create `tests/test_personal_story.py`: focused structural/content tests for placement, no visible heading, story hook, and motion hooks.
- Read only `Guidelines/Personal_Story.md`: source for the story content. Do not move, rewrite, or commit this untracked source file unless the user explicitly asks.

## Current Baseline Note

Before this feature, `python -m unittest discover -s tests -p "test_*.py" -q` fails because `tests/test_welcome_motion.py` expects `--motion-repeat-interval: 3.2s;`, while `static/css/styles.css` currently contains `--motion-repeat-interval: 2.0s;`. The first task restores that token so final verification can be meaningful.

---

### Task 1: Restore Motion Token Baseline

**Files:**
- Modify: `static/css/styles.css`
- Test: `tests/test_welcome_motion.py`

- [ ] **Step 1: Run the existing failing baseline test**

Run:

```powershell
python -m unittest tests.test_welcome_motion.WelcomeMotionTests.test_welcome_and_cta_shimmer_share_faster_repeat_rate -q
```

Expected: FAIL with an assertion that `--motion-repeat-interval: 3.2s;` is not found.

- [ ] **Step 2: Make the minimal CSS change**

In `static/css/styles.css`, change only this root token:

```css
:root {
  --motion-repeat-interval: 3.2s;
}
```

- [ ] **Step 3: Verify the baseline test passes**

Run:

```powershell
python -m unittest tests.test_welcome_motion.WelcomeMotionTests.test_welcome_and_cta_shimmer_share_faster_repeat_rate -q
```

Expected: PASS.

- [ ] **Step 4: Commit the baseline fix**

Run:

```powershell
git add static/css/styles.css
git commit -m "Fix motion repeat interval baseline"
```

Expected: commit succeeds with only `static/css/styles.css` staged.

---

### Task 2: Add Failing Personal Story Tests

**Files:**
- Create: `tests/test_personal_story.py`
- Test: `tests/test_personal_story.py`

- [ ] **Step 1: Create the focused test file**

Create `tests/test_personal_story.py` with this complete content:

```python
from pathlib import Path
import json
import unittest


ROOT = Path(__file__).resolve().parents[1]


class PersonalStoryTests(unittest.TestCase):
    def test_personal_story_content_is_data_driven(self):
        content = json.loads((ROOT / "data" / "content.json").read_text(encoding="utf-8"))

        self.assertIn("personal_story", content)
        paragraphs = content["personal_story"]["paragraphs"]

        self.assertIsInstance(paragraphs, list)
        self.assertGreaterEqual(len(paragraphs), 3)
        self.assertTrue(any("walked into a hospital" in paragraph for paragraph in paragraphs))
        self.assertTrue(any("doesn't take insulin" in paragraph for paragraph in paragraphs))

    def test_personal_story_is_between_welcome_and_hero(self):
        template = (ROOT / "templates" / "index.html").read_text(encoding="utf-8")

        welcome_index = template.index('class="motion-welcome')
        story_index = template.index('class="personal-story')
        hero_index = template.index('class="motion-hero')

        self.assertLess(welcome_index, story_index)
        self.assertLess(story_index, hero_index)

    def test_personal_story_has_no_visible_heading(self):
        template = (ROOT / "templates" / "index.html").read_text(encoding="utf-8")

        story_start = template.index('class="personal-story')
        story_end = template.index("<!--", story_start + 1)
        story_markup = template[story_start:story_end]

        self.assertNotIn("<h1", story_markup)
        self.assertNotIn("<h2", story_markup)
        self.assertNotIn("<h3", story_markup)
        self.assertNotIn("<h4", story_markup)

    def test_personal_story_uses_current_motion_language(self):
        template = (ROOT / "templates" / "index.html").read_text(encoding="utf-8")
        css = (ROOT / "static" / "css" / "styles.css").read_text(encoding="utf-8")

        self.assertIn("personal-story__panel motion-shimmer reveal", template)
        self.assertIn('data-reveal-delay="120"', template)
        self.assertIn("&ldquo;", template)
        self.assertIn(".personal-story {", css)
        self.assertIn(".personal-story::before", css)
        self.assertIn(".personal-story__panel {", css)
        self.assertIn(".personal-story__quote-mark {", css)
```

- [ ] **Step 2: Run the new tests to verify they fail**

Run:

```powershell
python -m unittest tests.test_personal_story -q
```

Expected: FAIL because `personal_story`, `personal-story`, and related CSS hooks do not exist yet.

- [ ] **Step 3: Commit the failing tests**

Run:

```powershell
git add tests/test_personal_story.py
git commit -m "Add personal story section tests"
```

Expected: commit succeeds with only `tests/test_personal_story.py` staged.

---

### Task 3: Add Story Content Data

**Files:**
- Modify: `data/content.json`
- Test: `tests/test_personal_story.py`

- [ ] **Step 1: Add the `personal_story` object after `welcome`**

In `data/content.json`, insert this object immediately after the existing `welcome` object and before `hero`:

```json
  "personal_story": {
    "paragraphs": [
      "A few years ago, my dad walked into a hospital for a routine visit and walked out with a life-changing diagnosis: severe Type 2 diabetes. The doctors told him the damage was already serious. He needed to start insulin immediately, and most likely, he'd be on it for the rest of his life.",
      "Here's the thing: he had no idea. No dramatic warning signs. No moment where he thought, \"something is really wrong.\" It crept up quietly, the way diabetes so often does, and by the time it showed up, it had already been building for years.",
      "My dad is not someone who gives up easily. Instead of just accepting what he was told, he started researching. He read everything he could find about people who had been in his exact situation. He made hard changes to what he ate, to how he moved, and to how he lived every single day.",
      "Today, he doesn't take insulin. His lifestyle regulates his blood sugar."
    ]
  },
```

The surrounding structure should become:

```json
  "welcome": {
    "title": "Welcome",
    "subtitle": "Millions of people around the world live with diabetes. We're here to help you recognise the signs, understand your treatment options, and connect with a community that truly gets it."
  },
  "personal_story": {
    "paragraphs": [
      "A few years ago, my dad walked into a hospital for a routine visit and walked out with a life-changing diagnosis: severe Type 2 diabetes. The doctors told him the damage was already serious. He needed to start insulin immediately, and most likely, he'd be on it for the rest of his life.",
      "Here's the thing: he had no idea. No dramatic warning signs. No moment where he thought, \"something is really wrong.\" It crept up quietly, the way diabetes so often does, and by the time it showed up, it had already been building for years.",
      "My dad is not someone who gives up easily. Instead of just accepting what he was told, he started researching. He read everything he could find about people who had been in his exact situation. He made hard changes to what he ate, to how he moved, and to how he lived every single day.",
      "Today, he doesn't take insulin. His lifestyle regulates his blood sugar."
    ]
  },
  "hero": {
```

- [ ] **Step 2: Verify the JSON parses and the data test passes**

Run:

```powershell
python -m unittest tests.test_personal_story.PersonalStoryTests.test_personal_story_content_is_data_driven -q
```

Expected: PASS.

- [ ] **Step 3: Commit the content**

Run:

```powershell
git add data/content.json
git commit -m "Add personal story content"
```

Expected: commit succeeds with only `data/content.json` staged.

---

### Task 4: Render The Editorial Story Panel

**Files:**
- Modify: `templates/index.html`
- Test: `tests/test_personal_story.py`

- [ ] **Step 1: Insert the section after Welcome and before Hero**

In `templates/index.html`, insert this block immediately after the closing `</section>` for the Welcome section and before the existing Hero comment:

```html
<!-- PERSONAL STORY -->
<section class="personal-story relative py-16 lg:py-20 overflow-hidden" aria-label="Personal story">
  <div class="max-w-7xl mx-auto px-6 lg:px-8">
    <div class="personal-story__panel motion-shimmer reveal relative max-w-4xl mx-auto rounded-2xl border border-border/60 bg-surface/75 shadow-card px-6 py-10 sm:px-10 lg:px-14 lg:py-12" data-reveal-delay="120">
      <div class="personal-story__quote-mark font-display absolute select-none" aria-hidden="true">&ldquo;</div>
      <div class="personal-story__copy relative space-y-5">
        {% for paragraph in personal_story.paragraphs %}
        <p class="text-lg text-ink-dim leading-relaxed">
          {{ paragraph }}
        </p>
        {% endfor %}
      </div>
    </div>
  </div>
</section>

```

After insertion, the `<!-- PERSONAL STORY -->` comment must appear after the Welcome section closing `</section>` and before the existing Hero section comment.

- [ ] **Step 2: Verify placement and no visible heading tests pass**

Run:

```powershell
python -m unittest tests.test_personal_story.PersonalStoryTests.test_personal_story_is_between_welcome_and_hero tests.test_personal_story.PersonalStoryTests.test_personal_story_has_no_visible_heading -q
```

Expected: PASS.

- [ ] **Step 3: Commit the template rendering**

Run:

```powershell
git add templates/index.html
git commit -m "Render personal story section"
```

Expected: commit succeeds with only `templates/index.html` staged.

---

### Task 5: Add Personal Story Styling

**Files:**
- Modify: `static/css/styles.css`
- Test: `tests/test_personal_story.py`

- [ ] **Step 1: Add CSS after `.motion-hero::before`**

In `static/css/styles.css`, add this block after the existing `.motion-hero::before` rule:

```css
.personal-story {
  background:
    linear-gradient(180deg, #fafcff 0%, #eef7ff 52%, #fafcff 100%);
  isolation: isolate;
}

.personal-story::before {
  content: '';
  position: absolute;
  inset: 0;
  pointer-events: none;
  background:
    radial-gradient(ellipse at 20% 15%, rgba(29, 95, 173, 0.10), transparent 42%),
    linear-gradient(90deg, rgba(126, 200, 227, 0.10), transparent 65%);
  z-index: 0;
}

.personal-story__panel {
  isolation: isolate;
  background:
    linear-gradient(135deg, rgba(240, 248, 255, 0.94), rgba(232, 244, 255, 0.82));
  box-shadow: 0 18px 55px rgba(15, 61, 122, 0.10);
}

.personal-story__quote-mark {
  top: 0.1rem;
  left: 1.2rem;
  color: rgba(29, 95, 173, 0.15);
  font-size: 7rem;
  line-height: 1;
  z-index: 0;
}

.personal-story__copy {
  z-index: 1;
}
```

- [ ] **Step 2: Add reduced-motion coverage for the section background**

In the existing reduced-motion media query, add `.personal-story::before` to the selector that disables animation effects. The final selector should include this new item:

```css
  .motion-load,
  .motion-float,
  .motion-float-delayed,
  .motion-welcome-sweep::before,
  .motion-welcome-title,
  .motion-welcome-divider,
  .motion-welcome-copy,
  .motion-logo::after,
  .motion-shimmer::before,
  .motion-stripe::before,
  .motion-stripe::after,
  .motion-welcome::after,
  .personal-story::before {
    animation: none !important;
  }
```

- [ ] **Step 3: Verify motion hook test passes**

Run:

```powershell
python -m unittest tests.test_personal_story.PersonalStoryTests.test_personal_story_uses_current_motion_language -q
```

Expected: PASS.

- [ ] **Step 4: Commit the styling**

Run:

```powershell
git add static/css/styles.css
git commit -m "Style personal story panel"
```

Expected: commit succeeds with only `static/css/styles.css` staged.

---

### Task 6: Full Verification

**Files:**
- Verify: `data/content.json`
- Verify: `templates/index.html`
- Verify: `static/css/styles.css`
- Verify: `tests/test_personal_story.py`

- [ ] **Step 1: Run the focused Personal Story test file**

Run:

```powershell
python -m unittest tests.test_personal_story -q
```

Expected: all 4 Personal Story tests pass.

- [ ] **Step 2: Run the full local test suite**

Run:

```powershell
python -m unittest discover -s tests -p "test_*.py" -q
```

Expected: all tests pass.

- [ ] **Step 3: Start the local dev server**

Run:

```powershell
python -m uvicorn main:app --host 127.0.0.1 --port 8000
```

Expected: server starts and prints a line containing `Uvicorn running on http://127.0.0.1:8000`.

- [ ] **Step 4: Manually inspect the page in a browser**

Open:

```text
http://127.0.0.1:8000
```

Expected:

- The Personal Story section appears directly below Welcome.
- No visible heading appears in the Personal Story section.
- The panel reads as a quiet editorial story card.
- The oversized quote mark is subtle and does not cover the story text.
- The panel reveals on scroll.
- The Hero section still follows naturally after the Personal Story section.

- [ ] **Step 5: Stop the dev server**

Stop the running `uvicorn` process with `Ctrl+C` in the terminal that started it.

- [ ] **Step 6: Check the final diff**

Run:

```powershell
git status --porcelain=v1
git diff --stat HEAD
```

Expected: no uncommitted tracked changes remain from the implementation tasks. `Guidelines/Personal_Story.md` may still appear as untracked because it was provided as the source story file and is not part of this implementation unless the user asks to add it.

---

## Plan Self-Review

- Spec coverage: placement, no heading, source-story narrative, editorial panel, current visual language, motion hooks, data-driven rendering, and tests are covered by Tasks 2 through 6.
- Baseline coverage: the existing motion-token test failure is covered by Task 1 so full verification can pass.
- Scope check: this is one section in the existing single-page site. No decomposition is needed.
- Placeholder scan: this plan contains no deferred implementation sections.
