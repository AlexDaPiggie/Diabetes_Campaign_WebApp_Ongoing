# Personal Story Refactor Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Refactor the Personal Story section to a centered, blue-gradient narrative style matching the visual reference.

**Architecture:** Transition from the left-aligned `.personal-story--editorial` class to the base `.personal-story` class. Centering will be handled via Tailwind-like utility classes already present in the project or custom CSS.

**Tech Stack:** FastAPI, Jinja2, Vanilla CSS.

---

### Task 1: Update Tests (TDD)

**Files:**
- Modify: `tests/test_personal_story.py`

- [ ] **Step 1: Update test expectations**
Modify `tests/test_personal_story.py` to check for centered layout and absence of the vertical accent rule.

```python
import unittest
from pathlib import Path
from main import load_content

class PersonalStoryTests(unittest.TestCase):
    def test_personal_story_layout_is_centered(self):
        template_path = Path("templates/index.html")
        template = template_path.read_text(encoding="utf-8")
        
        # Should use the base personal-story class
        self.assertIn('class="personal-story', template)
        # Should not use the editorial modifier
        self.assertNotIn('personal-story--editorial', template)
        # Should be centered
        self.assertIn('text-center', template)
        # Should not have the accent rule
        self.assertNotIn('personal-story__accent-rule', template)

    def test_personal_story_css_vitals(self):
        css_path = Path("static/css/styles.css")
        css = css_path.read_text(encoding="utf-8")
        
        # Verify gradient and centering rules exist
        self.assertIn(".personal-story {", css)
        self.assertIn("linear-gradient", css)
```

- [ ] **Step 2: Run tests to verify failure**
Run: `python -m unittest tests/test_personal_story.py -v`
Expected: FAIL (as it currently uses `.personal-story--editorial` and has an accent rule).

- [ ] **Step 3: Commit**
```bash
git add tests/test_personal_story.py
git commit -m "test: update personal story expectations for centered layout"
```

### Task 2: Refactor Template Structure

**Files:**
- Modify: `templates/index.html`

- [ ] **Step 1: Modify HTML structure**
Replace the `.personal-story--editorial` section with a centered `.personal-story` implementation.

```html
<!-- PERSONAL STORY -->
<section class="personal-story relative py-24 lg:py-32 overflow-hidden" aria-label="Personal story">
  <div class="max-w-7xl mx-auto px-6 lg:px-8">
    <div class="max-w-4xl mx-auto text-center">

      <!-- Heading -->
      <h2 class="font-display text-5xl sm:text-6xl font-bold text-ink leading-tight tracking-tight mb-16 reveal" data-reveal-delay="100">
        A routine visit changed everything.
      </h2>

      <!-- Narrative Paragraphs with Staggered Fade -->
      <div class="personal-story__body space-y-12 max-w-3xl mx-auto">
        {% for paragraph in personal_story.paragraphs %}
        <p class="personal-story__paragraph reveal text-xl text-ink leading-relaxed"
           style="transition-delay: {{ 0.2 + (loop.index0 * 0.15) }}s">
          {{ paragraph }}
        </p>
        {% endfor %}
      </div>

    </div>
  </div>
</section>
```

- [ ] **Step 2: Commit**
```bash
git add templates/index.html
git commit -m "feat: refactor personal story template to centered layout"
```

### Task 3: Refine CSS and Cleanup

**Files:**
- Modify: `static/css/styles.css`

- [ ] **Step 1: Update personal-story styles**
Ensure the heading is properly targeted and sized, and clean up the unused editorial styles.

```css
/* --- Personal Story: Centered Narrative --- */
.personal-story {
  background:
    linear-gradient(180deg, #fafcff 0%, #eef7ff 52%, #fafcff 100%);
  isolation: isolate;
}

.personal-story .font-display {
  margin-bottom: 4rem;
  /* Ensure bold contrast as requested */
  font-weight: 700;
}

.personal-story__paragraph {
  text-wrap: pretty;
  transition-duration: 1200ms !important;
}

/* Remove unused editorial styles */
/* .personal-story--editorial and children to be deleted */
```

- [ ] **Step 2: Perform deletion of old styles**
Surgically remove `.personal-story--editorial`, `.personal-story__accent-rule`, and `.personal-story--editorial::before`.

- [ ] **Step 3: Run tests to verify success**
Run: `python -m unittest tests/test_personal_story.py -v`
Expected: PASS

- [ ] **Step 4: Commit**
```bash
git add static/css/styles.css
git commit -m "style: finalize centered personal story and cleanup editorial styles"
```

### Task 4: Final Verification

- [ ] **Step 1: Full test suite check**
Run: `python -m unittest discover tests -v`
Expected: ALL PASS

- [ ] **Step 2: Final Commit**
```bash
git status
# Ensure everything is clean
```
