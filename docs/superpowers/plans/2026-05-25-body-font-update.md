# Personal Story Body Text Size Update Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Increase the body text size of the personal story section by 20% (from 18px/20px to 22px/24px) for better readability.

**Architecture:** Direct update of Tailwind-style utility classes in the Jinja2 template.

**Tech Stack:** HTML/Jinja2, Tailwind CSS (Utility Classes).

---

### Task 1: Update Verification Test

**Files:**
- Modify: `tests/test_personal_story.py`

- [ ] **Step 1: Update the test to expect new font sizes**

```python
def test_personal_story_typography(client):
    response = client.get('/')
    html = response.data.decode()
    # Check for new mobile size
    assert 'text-[22px]' in html
    # Check for new desktop size
    assert 'md:text-[24px]' in html
    # Ensure old sizes are gone
    assert 'text-[18px]' not in html
    assert 'md:text-[20px]' not in html
```

- [ ] **Step 2: Run test to verify it fails**

Run: `pytest tests/test_personal_story.py`
Expected: FAIL (AssertionError for 'text-[22px]' not in html)

- [ ] **Step 3: Commit test change**

```bash
git add tests/test_personal_story.py
git commit -m "test: update personal story typography expectations"
```

### Task 2: Implement Typography Update

**Files:**
- Modify: `templates/index.html`

- [ ] **Step 1: Update utility classes in the template**

Locate the `.personal-story__paragraph` element and update its classes.

```html
<!-- old -->
<p class="personal-story__paragraph text-[18px] md:text-[20px] text-ink leading-[1.8] text-center reveal" ...>

<!-- new -->
<p class="personal-story__paragraph text-[22px] md:text-[24px] text-ink leading-[1.8] text-center reveal" ...>
```

- [ ] **Step 2: Run test to verify it passes**

Run: `pytest tests/test_personal_story.py`
Expected: PASS

- [ ] **Step 3: Commit implementation**

```bash
git add templates/index.html
git commit -m "feat: increase personal story body text size by 20%"
```
