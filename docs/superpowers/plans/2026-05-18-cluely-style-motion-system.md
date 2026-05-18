# Cluely-Style Motion System Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Add a polished, calm Cluely-inspired motion system to the current FastAPI/Jinja diabetes awareness site without changing layout or content structure.

**Architecture:** The template receives lightweight motion classes and data attributes. CSS owns the visual motion language, while `static/js/main.js` continues to handle scroll observation, lazy loading, nav state, anchor scrolling, and stat animations.

**Tech Stack:** FastAPI, Jinja2, Tailwind CDN, vanilla CSS, vanilla JavaScript.

---

### Task 1: Add Motion Hooks To The Jinja Template

**Files:**
- Modify: `templates/index.html`

- [ ] **Step 1: Add semantic motion classes and stagger data attributes**

Add classes such as `motion-hero`, `motion-float`, `motion-shimmer`, `motion-stat`, `motion-image`, and `data-reveal-delay` attributes to existing elements only. Do not add new sections or change the copy.

- [ ] **Step 2: Verify the template still renders existing data**

Run: `python -m compileall main.py`

Expected: command exits with code `0`.

### Task 2: Define The Calm Motion System In CSS

**Files:**
- Modify: `static/css/styles.css`

- [ ] **Step 1: Extend the reveal primitive**

Update `.reveal` and `.reveal.revealed` to use opacity, translate, scale, and blur settling. Add variants for image and stat elements.

- [ ] **Step 2: Add ambient motion classes**

Add calm shimmer, glow, floating, nav, image, and gradient stripe styles. Respect `prefers-reduced-motion`.

- [ ] **Step 3: Verify the CSS remains plain static CSS**

Run: `Get-Content static/css/styles.css`

Expected: file contains no build-tool syntax and can be served directly.

### Task 3: Refine Vanilla JavaScript Motion Behavior

**Files:**
- Modify: `static/js/main.js`

- [ ] **Step 1: Read reveal delay attributes**

Update the existing `IntersectionObserver` reveal code so each element can use `data-reveal-delay` while still revealing once.

- [ ] **Step 2: Fix mixed-value stat animation**

Parse stat values by detecting numeric prefix/suffix patterns and ratios. Ensure final text is exactly the original target value.

- [ ] **Step 3: Respect reduced motion**

When reduced motion is enabled, skip animated transitions for stats and anchor scrolling.

- [ ] **Step 4: Verify JavaScript syntax**

Run: `node --check static/js/main.js`

Expected: command exits with code `0`.

### Task 4: Runtime Verification

**Files:**
- Verify: `main.py`
- Verify: `templates/index.html`
- Verify: `static/css/styles.css`
- Verify: `static/js/main.js`

- [ ] **Step 1: Start the FastAPI app**

Run: `uvicorn main:app --reload`

Expected: app serves at `http://127.0.0.1:8000`.

- [ ] **Step 2: Request the homepage**

Run: `Invoke-WebRequest http://127.0.0.1:8000/ -UseBasicParsing`

Expected: HTTP status `200` and rendered HTML contains `Understanding diabetes. Together.`

- [ ] **Step 3: Confirm root static page was not edited**

Run: `git diff -- index.html`

Expected: no diff output.
