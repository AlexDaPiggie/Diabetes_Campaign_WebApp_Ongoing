# Personal Story Vertical Alignment Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Align the personal story narrative column to the top of the waffle chart column on desktop displays.

**Architecture:** Use `align-items: flex-start` on the grid container for desktop sizes and adjust the padding of the left column to match the chart's internal padding.

**Tech Stack:** Tailwind CSS, Vanilla CSS (styles.css), HTML/Jinja2 (index.html).

---

### Task 1: Update Grid Alignment in CSS

**Files:**
- Modify: `static/css/styles.css`

- [ ] **Step 1: Change align-items to start for desktop grid**

```css
/* static/css/styles.css:167-172 */
@media (min-width: 1024px) {
  .personal-story__grid {
    grid-template-columns: 1fr 1fr;
    gap: 5rem;
    align-items: start; /* Changed from center to start */
  }
}
```

- [ ] **Step 2: Commit CSS change**

```bash
git add static/css/styles.css
git commit -m "style: align personal story grid to top on desktop"
```

---

### Task 2: Adjust Top Padding for Narrative Column

**Files:**
- Modify: `templates/index.html`

- [ ] **Step 1: Add lg:pt-8 to the narrative column**

This matches the `padding-block: 2rem` (32px / pt-8) on the `.personal-story__stats` column.

```html
<!-- templates/index.html:61 -->
      <!-- Left Column: Narrative -->
      <div class="flex flex-col items-center text-center lg:pt-8">
```

- [ ] **Step 2: Commit HTML change**

```bash
git add templates/index.html
git commit -m "style: add top padding to personal story text to match chart baseline"
```

---

### Task 3: Verification

- [ ] **Step 1: Verify layout visually (manual)**
Confirm the "Before it's too late" headline starts at the same vertical position as the top row of icons in the waffle chart.

- [ ] **Step 2: Run existing tests**

Run: `pytest tests/test_app_render.py tests/test_personal_story.py`
Expected: PASS
