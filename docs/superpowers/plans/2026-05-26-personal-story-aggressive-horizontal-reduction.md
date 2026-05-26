# Personal Story Aggressive Horizontal Reduction Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Aggressively reduce horizontal spacing between stat items and tighten label widths in the 'personal story' section.

**Architecture:** Surgical updates to `templates/index.html`.

**Tech Stack:** HTML (Jinja2), Tailwind-like utility classes.

---

### Task 1: Create Verification Tests

**Files:**
- Create: `tests/test_personal_story_aggressive_horizontal_reduction.py`

- [ ] **Step 1: Write the failing tests**

```python
from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]

class AggressiveHorizontalReductionTests(unittest.TestCase):
    def setUp(self):
        self.template = (ROOT / "templates" / "index.html").read_text(encoding="utf-8")
        
        # Extract personal story section
        story_start = self.template.find('class="personal-story')
        story_end = self.template.find('<!-- ═══════════════ HERO ═══════════════ -->', story_start)
        self.story_html = self.template[story_start:story_end]

    def test_legend_aggressive_gaps_reduced(self):
        # Base/Mobile gap reduced from gap-x-4 (16px) to gap-x-2 (8px)
        self.assertIn('gap-x-2', self.story_html)
        # Desktop gap reduced from lg:gap-x-[25.6px] to lg:gap-x-4 (16px)
        self.assertIn('lg:gap-x-4', self.story_html)

    def test_label_max_width_reduced(self):
        # Max-width reduced from max-w-[100px] to max-w-[80px]
        self.assertIn('max-w-[80px]', self.story_html)
```

- [ ] **Step 2: Run tests to verify they fail**

Run: `pytest tests/test_personal_story_aggressive_horizontal_reduction.py`
Expected: FAIL

### Task 2: Update HTML for Legend Gaps and Label Width

**Files:**
- Modify: `templates/index.html`

- [ ] **Step 1: Update legend container and label classes**

```html
<!-- Update Legend / Stats gaps -->
<div class="flex flex-wrap lg:flex-nowrap justify-center gap-x-2 lg:gap-x-4 gap-y-5 mt-[19.2px]">
  <!-- ... -->
  <div class="font-ui text-[11px] font-light text-ink-muted leading-[20px] -mt-1.0 max-w-[80px]">
    {{ stat.label }}
  </div>
  <!-- ... -->
</div>
```

### Task 3: Final Verification

- [ ] **Step 1: Run verification tests**

Run: `pytest tests/test_personal_story_aggressive_horizontal_reduction.py`
Expected: PASS
