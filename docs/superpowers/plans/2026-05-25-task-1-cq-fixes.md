# Task 1 Code Quality Fixes Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Implement requested animation and styling fixes from the Task 1 code quality review, including syncing translateY values and reducing glow opacities.

**Architecture:** Surgical updates to Tailwind configuration in `base.html`, CSS classes in `styles.css`, and utility class cleanup in `index.html`.

**Tech Stack:** HTML, Tailwind CSS, Vanilla CSS.

---

### Task 1: Update base.html Animations

**Files:**
- Modify: `templates/base.html`

- [ ] **Step 1: Update fadeUp keyframe and pulseGlow opacities**

Replace the `fadeUp` and `pulseGlow` keyframes in `templates/base.html`:
- `fadeUp`: `translateY(24px)` -> `translateY(28.8px)`
- `pulseGlow`: `rgba(59, 130, 246, 0.04)` -> `rgba(59, 130, 246, 0.032)`
- `pulseGlow`: `rgba(59, 130, 246, 0.12)` -> `rgba(59, 130, 246, 0.096)`

- [ ] **Step 2: Commit changes**

```bash
git add templates/base.html
git commit -m "fix: sync fadeUp translateY and reduce pulseGlow opacities in base.html"
```

### Task 2: Update Reveal Animations in styles.css

**Files:**
- Modify: `static/css/styles.css`

- [ ] **Step 1: Increase translateY for reveal classes**

Update `.reveal` and `.reveal-image` classes:
- `.reveal`: `translateY(26px)` -> `translateY(31.2px)`
- `.reveal-image`: `translateY(30px)` -> `translateY(36px)`

- [ ] **Step 2: Commit changes**

```bash
git add static/css/styles.css
git commit -m "fix: increase reveal animation translateY by 20% in styles.css"
```

### Task 3: Cleanup Utility Classes in index.html

**Files:**
- Modify: `templates/index.html`

- [ ] **Step 1: Remove h-1.5 from motion-stripe elements**

Find all occurrences of `motion-stripe` and remove the `h-1.5` class.

- [ ] **Step 2: Commit changes**

```bash
git add templates/index.html
git commit -m "fix: remove redundant height utility from motion-stripe elements"
```

### Task 4: Verification

- [ ] **Step 1: Run existing tests to ensure no regressions**

Run: `pytest tests/test_welcome_motion.py tests/test_app_render.py`

- [ ] **Step 2: Verify visual changes (Manual/CSS Check)**
Check that `styles.css` and `base.html` reflect the new values.
