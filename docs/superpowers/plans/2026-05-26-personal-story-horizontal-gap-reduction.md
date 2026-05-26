# Personal Story Horizontal Gap Reduction Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Further reduce the horizontal gap between individual stat items in the 'personal story' section by 20%.

**Architecture:** Surgical updates to `templates/index.html`.

**Tech Stack:** HTML (Jinja2), Tailwind-like utility classes.

---

### Task 1: Create Verification Tests

**Files:**
- Create: `tests/test_personal_story_horizontal_gap_reduction.py`

- [ ] **Step 1: Write the failing tests**

```python
from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]

class HorizontalGapReductionTests(unittest.TestCase):
    def setUp(self):
        self.template = (ROOT / "templates" / "index.html").read_text(encoding="utf-8")
        
        # Extract personal story section
        story_start = self.template.find('class="personal-story')
        story_end = self.template.find('<!-- ═══════════════ HERO ═══════════════ -->', story_start)
        self.story_html = self.template[story_start:story_end]

    def test_legend_horizontal_gaps_reduced(self):
        # Base/Mobile gap reduced from gap-x-5 (20px) to gap-x-4 (16px)
        self.assertIn('gap-x-4', self.story_html)
        # Desktop gap reduced from lg:gap-x-8 (32px) to lg:gap-x-[25.6px]
        self.assertIn('lg:gap-x-[25.6px]', self.story_html)
```

- [ ] **Step 2: Run tests to verify they fail**

Run: `pytest tests/test_personal_story_horizontal_gap_reduction.py`
Expected: FAIL

### Task 2: Update HTML for Legend Gaps

**Files:**
- Modify: `templates/index.html`

- [ ] **Step 1: Update legend container classes**

```html
<!-- Update Legend / Stats gaps -->
<div class="flex flex-wrap lg:flex-nowrap justify-center gap-x-4 lg:gap-x-[25.6px] gap-y-5 mt-[19.2px]">
  <!-- ... -->
</div>
```

### Task 3: Final Verification

- [ ] **Step 1: Run verification tests**

Run: `pytest tests/test_personal_story_horizontal_gap_reduction.py`
Expected: PASS
