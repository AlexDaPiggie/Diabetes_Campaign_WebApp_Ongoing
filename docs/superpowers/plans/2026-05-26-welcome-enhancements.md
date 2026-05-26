# Welcome Section Enhancements Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Enhance the visual hierarchy and layout of the Welcome section by shifting content upwards and increasing the prominence of the title, divider, and subtitle.

**Architecture:** Surgical updates to Tailwind classes in `templates/index.html`.

**Tech Stack:** HTML, Tailwind CSS.

---

### Task 1: Add Verification Test

**Files:**
- Create: `tests/test_welcome_enhancements.py`

- [ ] **Step 1: Write the failing test**

```python
from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]

class WelcomeEnhancementsTests(unittest.TestCase):
    def test_welcome_enhancements_classes_applied(self):
        template = (ROOT / "templates" / "index.html").read_text(encoding="utf-8")
        
        # Layout
        self.assertIn("pt-[64px] pb-[128px]", template)
        
        # Title
        self.assertIn("font-semibold", template)
        
        # Divider
        self.assertIn("h-0.5", template)
        
        # Subtitle
        self.assertIn("text-[24px] md:text-[28px]", template)
        self.assertIn("font-semibold", template)
```

- [ ] **Step 2: Run test to verify it fails**

Run: `python -m unittest tests/test_welcome_enhancements.py`
Expected: FAIL (classes not found)

- [ ] **Step 3: Commit**

```bash
git add tests/test_welcome_enhancements.py
git commit -m "test: add verification for welcome section enhancements"
```

### Task 2: Update Welcome Section Layout

**Files:**
- Modify: `templates/index.html`

- [ ] **Step 1: Update container padding**

Update `<div class="motion-welcome-content ... py-[96px]">` to `pt-[64px] pb-[128px]`.

- [ ] **Step 2: Update title font weight**

Update `<h2 class="motion-welcome-title ... font-medium ...">` to `font-semibold`.

- [ ] **Step 3: Update divider thickness**

Update `<div class="motion-welcome-divider ... h-px ...">` to `h-0.5`.

- [ ] **Step 4: Update subtitle size and weight**

Update `<p class="motion-welcome-copy ... text-[18px] md:text-[20px] ...">` to `text-[24px] md:text-[28px] font-semibold`.

- [ ] **Step 5: Run tests and verify they pass**

Run: `python -m unittest tests/test_welcome_enhancements.py`
Expected: PASS

- [ ] **Step 6: Commit**

```bash
git add templates/index.html
git commit -m "feat: enhance welcome section layout and typography"
```
