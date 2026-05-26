# Personal Story Vertical Gap Reduction Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Reduce the vertical gaps between components in the 'stat' part of the 'personal story' section by 20%.

**Architecture:** Surgical updates to `static/css/styles.css` and `templates/index.html`.

**Tech Stack:** HTML/CSS (Jinja2), Tailwind-like utility classes.

---

### Task 1: Create Verification Tests

**Files:**
- Create: `tests/test_personal_story_vertical_gap_reduction.py`

- [ ] **Step 1: Write the failing tests**

```python
from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]

class VerticalGapReductionTests(unittest.TestCase):
    def setUp(self):
        self.template = (ROOT / "templates" / "index.html").read_text(encoding="utf-8")
        self.css = (ROOT / "static" / "css" / "styles.css").read_text(encoding="utf-8")
        
        # Extract personal story section
        story_start = self.template.find('class="personal-story')
        story_end = self.template.find('<!-- ═══════════════ HERO ═══════════════ -->', story_start)
        self.story_html = self.template[story_start:story_end]

    def test_source_link_margins_reduced(self):
        self.assertIn("margin: 0.8rem auto 0.2rem;", self.css)

    def test_legend_margin_top_reduced(self):
        self.assertIn('mt-[19.2px]', self.story_html)

    def test_callout_margin_top_reduced(self):
        self.assertIn('mt-[12.8px]', self.story_html)
```

- [ ] **Step 2: Run tests to verify they fail**

Run: `pytest tests/test_personal_story_vertical_gap_reduction.py`
Expected: FAIL

### Task 2: Update CSS for Source Link

**Files:**
- Modify: `static/css/styles.css`

- [ ] **Step 1: Update .personal-story__source margins**

```css
.personal-story__source {
  /* ... */
  margin: 0.8rem auto 0.2rem; /* Reduced from 1rem auto 0.25rem */
  /* ... */
}
```

### Task 3: Update HTML for Legend and Callout

**Files:**
- Modify: `templates/index.html`

- [ ] **Step 1: Update legend and callout margin classes**

```html
<!-- Update Legend / Stats -->
<div class="flex flex-wrap lg:flex-nowrap justify-center gap-x-5 lg:gap-x-8 gap-y-5 mt-[19.2px]">
  <!-- ... -->
</div>

{# Elderly Callout #}
<div class="personal-story__callout mt-[12.8px] text-[11px] ...">
```

### Task 4: Final Verification

- [ ] **Step 1: Run verification tests**

Run: `pytest tests/test_personal_story_vertical_gap_reduction.py`
Expected: PASS
