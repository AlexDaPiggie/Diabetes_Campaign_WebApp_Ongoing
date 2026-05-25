# Personal Story High-Contrast Editorial Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Implement a "High-Contrast Editorial" Personal Story section that replaces the current placeholder/blue-tinted design with a professional, human-centric narrative block.

**Architecture:** A full-width section with a warm "paper" background, a narrow centered text column for readability, and a large bold intro hook. It uses a staggered fade-up motion pattern for paragraphs.

**Tech Stack:** Python (FastAPI/Jinja2), TailwindCSS (for utility classes), Vanilla CSS (for custom motion), Unittest.

---

### Task 1: Update Tests for Editorial Layout

**Files:**
- Modify: `tests/test_personal_story.py`

- [ ] **Step 1: Update test assertions for the new editorial structure**

```python
# tests/test_personal_story.py (update existing or add new)
def test_personal_story_uses_editorial_language(self):
    template = (ROOT / "templates" / "index.html").read_text(encoding="utf-8")
    css = (ROOT / "static" / "css" / "styles.css").read_text(encoding="utf-8")

    self.assertIn('class="personal-story--editorial', template)
    self.assertIn('personal-story__accent-rule', template)
    self.assertIn('personal-story__intro', template)
    self.assertIn('data-reveal-delay', template)
    
    # Check for the warm background and charcoal text in CSS
    self.assertIn(".personal-story--editorial {", css)
    self.assertIn("background-color: #FCFAF7", css)
    self.assertIn("color: #0f2a4a", css) # text-ink equivalent
```

- [ ] **Step 2: Run tests to verify they fail**

Run: `python -m unittest tests.test_personal_story -q`
Expected: FAIL (Assertions about editorial classes will fail)

- [ ] **Step 3: Commit**

```bash
git add tests/test_personal_story.py
git commit -m "test: update personal story tests for editorial design"
```

### Task 2: Update Content Data

**Files:**
- Modify: `data/content.json`

- [ ] **Step 1: Ensure the story paragraphs are correct**

```json
{
  "personal_story": {
    "paragraphs": [
      "A few years ago, my dad walked into a hospital for a routine visit and walked out with a life-changing diagnosis: severe Type 2 diabetes. The doctors told him the damage was already serious. He needed to start insulin immediately, and most likely, he'd be on it for the rest of his life.",
      "Here's the thing: he had no idea. No dramatic warning signs. No moment where he thought, \"something is really wrong.\" It crept up quietly, the way diabetes so often does, and by the time it showed up, it had already been building for years.",
      "My dad is not someone who gives up easily. Instead of just accepting what he was told, he started researching. He read everything he could find about people who had been in his exact situation. He made hard changes to what he ate, to how he moved, and to how he lived every single day.",
      "Today, he doesn't take insulin. His lifestyle regulates his blood sugar."
    ]
  }
}
```

- [ ] **Step 2: Commit**

```bash
git add data/content.json
git commit -m "data: finalize personal story content"
```

### Task 3: Implement Template Markup

**Files:**
- Modify: `templates/index.html`

- [ ] **Step 1: Replace the current personal story section with the editorial markup**

```html
<!-- PERSONAL STORY (EDITORIAL) -->
<section class="personal-story--editorial relative py-24 lg:py-32 overflow-hidden" aria-label="Personal story">
  <div class="max-w-7xl mx-auto px-6 lg:px-8">
    <div class="personal-story__container max-w-2xl mx-auto">
      
      <!-- Intro Hook with Vertical Accent Rule -->
      <div class="flex gap-6 mb-12 reveal" data-reveal-delay="100">
        <div class="personal-story__accent-rule w-px bg-ink/20 shrink-0"></div>
        <h2 class="personal-story__intro font-display text-4xl sm:text-5xl font-medium text-ink leading-tight tracking-tight">
          A routine visit changed everything.
        </h2>
      </div>

      <!-- Narrative Paragraphs with Staggered Fade -->
      <div class="personal-story__body space-y-10">
        {% for paragraph in personal_story.paragraphs %}
        <p class="personal-story__paragraph reveal text-xl text-ink leading-relaxed" 
           style="transition-delay: {{ 0.2 + (loop.index0 * 0.15) }}s">
          {{ paragraph }}
        </p>
        {% endfor %}
      </div>

    </div>
  </div>
</section>
```

- [ ] **Step 2: Commit**

```bash
git add templates/index.html
git commit -m "feat: implement high-contrast editorial markup for personal story"
```

### Task 4: Implement Editorial Styles

**Files:**
- Modify: `static/css/styles.css`

- [ ] **Step 1: Replace/Add editorial styles**

```css
/* --- Personal Story: High-Contrast Editorial --- */
.personal-story--editorial {
  background-color: #FCFAF7; /* Warm Paper Tone */
  color: #0f2a4a; /* text-ink */
}

.personal-story__accent-rule {
  height: auto;
  min-height: 80px;
}

.personal-story__paragraph {
  text-wrap: pretty;
  transition-duration: 1200ms !important; /* Slower, deliberate pace */
}

/* Override reveal for editorial to be a pure fade-up without blur if preferred, 
   but we'll keep the system's reveal for consistency unless it feels too "techy" */

/* Ensure the background doesn't have the blue tint from the previous design */
.personal-story--editorial::before {
  display: none; /* Remove previous ambient gradients */
}
```

- [ ] **Step 2: Verify tests pass**

Run: `python -m unittest tests.test_personal_story -q`
Expected: PASS

- [ ] **Step 3: Commit**

```bash
git add static/css/styles.css
git commit -m "style: apply high-contrast editorial styles and motion"
```

---

### Task 5: Final Site-Wide Verification

- [ ] **Step 1: Run all tests**

Run: `python -m unittest discover -s tests -p "test_*.py" -q`
Expected: PASS

- [ ] **Step 2: Visual Smoke Check**
Confirm the section is between Welcome and Hero, has high contrast, and the staggered reveal works as intended.

- [ ] **Step 3: Commit**

```bash
git commit --allow-empty -m "chore: final verification of personal story editorial section"
```
