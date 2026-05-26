# Task 2: Adjust Layout and Component Hierarchy Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Scale headings, vertical padding, and component labels to maintain visual hierarchy with the new 20px body text.

**Architecture:** Systematic replacement of Tailwind utility classes with arbitrary values calculated based on 8% heading scale and 20% padding scale. Component labels and buttons are updated to a base 16px.

**Tech Stack:** Tailwind CSS, Jinja2 (HTML templates)

---

### Task 1: Scale Headings in templates/index.html

**Files:**
- Modify: `templates/index.html`

- [ ] **Step 1: Scale Hero Title**
    - Replace `text-5xl sm:text-6xl lg:text-7xl` with `text-[51.84px] sm:text-[64.8px] lg:text-[77.76px]` in the Hero section.
- [ ] **Step 2: Scale Welcome Title**
    - Replace `text-5xl md:text-6xl` with `text-[51.84px] md:text-[64.8px]` in the Welcome section.
- [ ] **Step 3: Scale Personal Story Title**
    - Replace `text-5xl sm:text-6xl` with `text-[51.84px] sm:text-[64.8px]` in the Personal Story section.
- [ ] **Step 4: Scale Section Titles**
    - Replace `text-4xl sm:text-5xl` with `text-[38.88px] sm:text-[51.84px]` in the info sections loop.
- [ ] **Step 5: Scale Hero Stats Numbers**
    - Replace `text-4xl` with `text-[38.88px]` in the hero stats loop.

### Task 2: Scale Vertical Padding in templates/index.html

**Files:**
- Modify: `templates/index.html`

- [ ] **Step 1: Scale Welcome Section Padding**
    - Replace `pt-16` with `pt-[76.8px]` and `py-20` with `py-[96px]` in the Welcome section.
- [ ] **Step 2: Scale Personal Story Section Padding**
    - Replace `py-24 lg:py-32` with `py-[115.2px] lg:py-[153.6px]` in the Personal Story section.
- [ ] **Step 3: Scale Hero Section Padding**
    - Replace `py-20 lg:py-28` with `py-[96px] lg:py-[134.4px]` in the Hero section.
- [ ] **Step 4: Scale Info Sections Padding**
    - Replace `py-20 lg:py-28` with `py-[96px] lg:py-[134.4px]` in the info sections loop.
- [ ] **Step 5: Scale Footer Padding**
    - Replace `py-16 lg:py-20` with `py-[76.8px] lg:py-[96px]` in the Footer section.

### Task 3: Update Buttons and Labels in templates/index.html

**Files:**
- Modify: `templates/index.html`

- [ ] **Step 1: Update Hero Eyebrow**
    - Replace `text-xs` with `text-[16px]` for the hero eyebrow.
- [ ] **Step 2: Update Hero CTAs**
    - Replace `text-sm` with `text-[16px]` for both primary and secondary hero buttons.
- [ ] **Step 3: Update Hero Badge Subtitle**
    - Replace `text-xs` with `text-[16px]` for the hero badge subtitle.
- [ ] **Step 4: Update Section Eyebrows**
    - Replace `text-xs` with `text-[16px]` for section eyebrows in the loop.

### Task 4: Verification

**Files:**
- Test: `tests/test_layout_hierarchy.py`

- [ ] **Step 1: Create a test to verify class changes**
    - Check that the expected arbitrary values are present in the rendered HTML.
- [ ] **Step 2: Run tests**
    - `pytest tests/test_layout_hierarchy.py`
