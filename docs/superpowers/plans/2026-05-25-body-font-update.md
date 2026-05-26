# Body Text Font Update Implementation Plan (Final)

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Transform website typography and visual hierarchy using Open Sans (300) with precise scaling and aesthetic refinements.

**Architecture:**
- Import Open Sans (300-700) from Google Fonts.
- Update Tailwind config for neutral charcoal text colors and font family.
- Apply explicit decimal-based values for 8% heading scale and 20% vertical scale.
- Implement responsive body text (18px mobile / 20px desktop).

**Tech Stack:** HTML, CSS, Tailwind CSS, Google Fonts

---

### Task 1: Core Configuration and Global Styles

**Files:**
- Modify: `templates/base.html`
- Modify: `static/css/styles.css`

- [ ] **Step 1: Update Google Fonts and Tailwind Theme in `base.html`.**
- Replace Inter with Open Sans (300-700).
- Update Colors: `ink: #0D0F10`, `ink-dim: #33383D`, `ink-muted: #595E63`.
- Update Font Family `ui`: `["Open Sans", "Arial", "sans-serif", "serif"]`.

- [ ] **Step 2: Update `body` tag and global CSS variables.**
- Apply: `text-[18px] md:text-[20px]`, `leading-[25.2px] md:leading-[28px]`, `font-light`, `tracking-tight` (only for body).
- Update `static/css/styles.css`:
    - Increase `motion-stripe` height from 8px to **9.6px**.
    - Increase `translateY(24px)` to **28.8px** in `motionEnter` animation.
    - Reduce background glow/sweep opacities by 20% (relative to current).

### Task 2: Adjust Layout and Component Hierarchy

**Files:**
- Modify: `templates/index.html`

- [ ] **Step 1: Scale Headings (>=30px) by 8%.**
- 36px → **38.88px**
- 48px → **51.84px**
- 60px → **64.8px**
- 72px → **77.76px**
- (Apply to both mobile and desktop classes).

- [ ] **Step 2: Scale Vertical Padding by 20%.**
- `py-20` (80px) → `py-[96px]`
- `py-24` (96px) → `py-[115.2px]`
- `py-28` (112px) → `py-[134.4px]`
- `py-32` (128px) → `py-[153.6px]`
- `pt-16` (64px) → `pt-[76.8px]`

- [ ] **Step 3: Update Buttons and Labels to 16px.**
- Buttons: `text-sm` (14px) → `text-[16px]`.
- Eyebrows/Badges: `text-xs` (12px) → `text-[16px]`.

- [ ] **Step 4: Audit Nav and Footer.**
- Ensure they remain at 14px (no change).

### Task 3: Verification and Test Updates

**Files:**
- Modify: `tests/test_content_typography.py`

- [ ] **Step 1: Update typography tests to match explicit decimal values and classes.**

- [ ] **Step 2: Run all tests.**
- Run: `pytest tests/test_app_render.py tests/test_content_typography.py -v`
- Expected: PASS
