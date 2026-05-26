# Personal Story Component Size Reduction Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Reduce the size of all components in the diagram (waffle chart) and stats part (legend, callout) of the 'personal story' section by 20%.

**Architecture:** Surgical updates to `static/css/styles.css` for custom-styled components and `templates/index.html` for utility-styled components.

**Tech Stack:** HTML/CSS (Jinja2), Tailwind-like utility classes.

---

### Task 1: Create Verification Tests

**Files:**
- Create: `tests/test_personal_story_size_reduction.py`

- [ ] **Step 1: Write the failing tests**

```python
from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]

class SizeReductionTests(unittest.TestCase):
    def setUp(self):
        self.template = (ROOT / "templates" / "index.html").read_text(encoding="utf-8")
        self.css = (ROOT / "static" / "css" / "styles.css").read_text(encoding="utf-8")
        
        # Extract personal story section
        story_start = self.template.find('class="personal-story')
        story_end = self.template.find('<!-- ═══════════════ HERO ═══════════════ -->', story_start)
        self.story_html = self.template[story_start:story_end]

    def test_waffle_container_size_reduced(self):
        self.assertIn(".waffle-container {\n  position: relative;\n  width: 100%;\n  max-width: 336px;", self.css)
        self.assertIn("@media (max-width: 767px) {\n  .waffle-grid {\n    grid-template-columns: repeat(10, 1fr);\n  }\n\n  .waffle-container {\n    max-width: 256px;\n  }\n}", self.css)

    def test_waffle_grid_gap_reduced(self):
        self.assertIn("gap: clamp(4px, 0.44vw, 6.4px);", self.css)

    def test_source_link_size_reduced(self):
        self.assertIn("font-size: 16px;", self.css)
        self.assertIn("max-width: 336px;", self.css)
        self.assertIn("@media (max-width: 767px) {\n  .personal-story__source {\n    max-width: 256px;\n  font-size: 13px;\n  }\n}", self.css)

    def test_legend_stats_size_reduced(self):
        # Stat number
        self.assertIn('text-[18px]', self.story_html)
        # Stat label
        self.assertIn('text-[11px]', self.story_html)
        # Stat icon (w-5)
        self.assertIn('w-5 h-5', self.story_html)
        # Gaps
        self.assertIn('gap-x-5', self.story_html)
        self.assertIn('lg:gap-x-8', self.story_html)

    def test_callout_size_reduced(self):
        self.assertIn('text-[11px]', self.story_html)
        self.assertIn('max-w-[307px]', self.story_html)
```

- [ ] **Step 2: Run tests to verify they fail**

Run: `pytest tests/test_personal_story_size_reduction.py`
Expected: FAIL

### Task 2: Update CSS for Waffle Chart and Source Link

**Files:**
- Modify: `static/css/styles.css`

- [ ] **Step 1: Update .waffle-container, .waffle-grid, and .personal-story__source**

```css
/* Update .waffle-container */
.waffle-container {
  position: relative;
  width: 100%;
  max-width: 336px; /* Reduced from 420px */
}

/* Update .waffle-grid */
.waffle-grid {
  display: grid;
  grid-template-columns: repeat(10, 1fr);
  gap: clamp(4px, 0.44vw, 6.4px); /* Reduced from clamp(5px, 0.55vw, 8px) */
}

/* Update mobile .waffle-container */
@media (max-width: 767px) {
  /* ... */
  .waffle-container {
    max-width: 256px; /* Reduced from 320px */
  }
}

/* Update .personal-story__source */
.personal-story__source {
  /* ... */
  max-width: 336px; /* Reduced from 420px */
  font-size: 16px; /* Reduced from 20px */
  /* ... */
}

/* Update mobile .personal-story__source */
@media (max-width: 767px) {
  .personal-story__source {
    max-width: 256px; /* Reduced from 320px */
    font-size: 13px; /* Reduced from 16px */
  }
}
```

- [ ] **Step 2: Commit**

```bash
git add static/css/styles.css
git commit -m "style: reduce waffle chart and source link sizes by 20%"
```

### Task 3: Update HTML for Legend and Callout

**Files:**
- Modify: `templates/index.html`

- [ ] **Step 1: Update legend stats and callout classes**

```html
<!-- Update Legend / Stats -->
<div class="flex flex-wrap lg:flex-nowrap justify-center gap-x-5 lg:gap-x-8 gap-y-5 mt-6">
  <!-- ... -->
  <svg class="w-5 h-5 shrink-0 mt-1 ..." ...>
    <!-- ... -->
  </svg>
  
  <div class="flex flex-col">
    <div class="motion-stat font-display text-[18px] ..." ...>0</div>
    <div class="font-ui text-[11px] ...">
      {{ stat.label }}
    </div>
  </div>
</div>

{# Elderly Callout #}
<div class="personal-story__callout mt-4 text-[11px] italic text-ink/60 text-center max-w-[307px]">
  {{ personal_story.waffle.labels.elderly_callout }}
</div>
```

- [ ] **Step 2: Run tests to verify they pass**

Run: `pytest tests/test_personal_story_size_reduction.py`
Expected: PASS

- [ ] **Step 3: Commit**

```bash
git add templates/index.html
git commit -m "feat: reduce legend and callout sizes by 20% in personal story"
```

### Task 4: Final Cleanup and Verification

**Files:**
- Modify: `tests/test_personal_story.py` (to fix unrelated failure if desired, or skip)

- [ ] **Step 1: Run all tests**

Run: `pytest`

- [ ] **Step 2: Final Commit**

```bash
git add tests/test_personal_story_size_reduction.py
git commit -m "test: add verification tests for personal story size reduction"
```
