# Personal Section Padding Reduction Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Reduce top/bottom padding of the personal section in `index.html` from `py-[115.2px] lg:py-[153.6px]` to `py-[96px] lg:py-[128px]`.

**Architecture:** Pure stylistic HTML update in the section container class list.

**Tech Stack:** HTML, Tailwind CSS (JIT classes).

---

### Task 1: Update Section Padding

**Files:**
- Modify: `templates/index.html`

- [ ] **Step 1: Identify and replace padding classes**

Locate the `<section>` tag with class `personal-story` and replace its padding utilities.

**Old Code:**
```html
<section class="personal-story relative py-[115.2px] lg:py-[153.6px] overflow-hidden" aria-label="Personal story">
```

**New Code:**
```html
<section class="personal-story relative py-[96px] lg:py-[128px] overflow-hidden" aria-label="Personal story">
```

- [ ] **Step 2: Commit changes**

```bash
git add templates/index.html
git commit -m "style: reduce personal section padding for tighter layout"
```
