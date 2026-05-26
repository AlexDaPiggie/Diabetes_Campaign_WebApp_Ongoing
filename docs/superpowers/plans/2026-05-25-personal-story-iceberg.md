# "Hidden Burden" Personal Story Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Integrate USA-specific undiagnosed diabetes statistics into the Personal Story section using a 50/50 side-by-side layout with an illustrative iceberg diagram and source attribution.

**Architecture:** Refactor the existing centered `personal-story` section into a 2-column grid. The left column will house the personal narrative, and the right column will feature a custom SVG iceberg diagram with depth-themed gradients. A source citation will be added as a section footer.

**Tech Stack:** Tailwind CSS (utility classes), Vanilla CSS (custom animations/gradients), Jinja2 (templates), SVG.

---

### Task 1: Update Content Data

**Files:**
- Modify: `data/content.json`

- [ ] **Step 1: Add iceberg data and source to content.json**
Add the new statistics and source attribution strings to the `personal_story` object.

```json
  "personal_story": {
    "paragraphs": [
      "No warning signs, creeping up quietly. That was how diabetes came to my dad. Everything felt normal until the day he received a life-changing diagnosis: severe Type 2 diabetes. The damage was already done. He was told to start insulin immediately, and would likely be on it for the rest of his life."
    ],
    "iceberg": {
      "layers": [
        { "label": "Diagnosed Adults", "stat": "29.4 Million", "depth": "tip" },
        { "label": "Undiagnosed (The Missing Millions)", "stat": "8.7 Million", "depth": "middle", "age_callout": "Risk triples after 40" },
        { "label": "Prediabetes (8 in 10 don't know)", "stat": "97.6 Million", "depth": "base" }
      ],
      "source": "Source: CDC National Diabetes Statistics Report 2024 & NCHS Data Brief No. 516. Data represents US adults (18+) from 2021–2023."
    }
  }
```

- [ ] **Step 2: Commit changes**
```bash
git add data/content.json
git commit -m "data: add iceberg stats and source to personal story"
```

---

### Task 2: Define Iceberg and Grid Styles

**Files:**
- Modify: `static/css/styles.css`

- [ ] **Step 1: Add grid and iceberg specific styles**
Define the layout for the 50/50 split and the visual treatment for the "underwater" iceberg container.

```css
/* --- Personal Story Grid & Iceberg --- */
.personal-story__grid {
  display: grid;
  grid-template-columns: 1fr;
  gap: 3rem;
  align-items: center;
}

@media (min-width: 1024px) {
  .personal-story__grid {
    grid-template-columns: 1fr 1fr;
    gap: 4rem;
  }
}

.personal-story__stats {
  position: relative;
  border-radius: 1.5rem;
  overflow: hidden;
  background: linear-gradient(180deg, #eef7ff 0%, #3498db 40%, #1d5fad 100%);
  min-height: 400px;
  display: flex;
  align-items: center;
  justify-content: center;
  box-shadow: 0 18px 55px rgba(15, 61, 122, 0.15);
}

.iceberg-svg {
  width: 100%;
  height: auto;
  max-width: 320px;
}

.iceberg-label {
  font-size: 0.75rem;
  font-weight: 600;
  fill: #0f2a4a;
}

.iceberg-stat {
  font-size: 1.25rem;
  font-weight: 700;
  fill: #0f2a4a;
}

.iceberg-label--submerged {
  fill: rgba(255, 255, 255, 0.9);
}

.iceberg-stat--submerged {
  fill: #ffffff;
}

.personal-story__source {
  margin-top: 4rem;
  padding-top: 2rem;
  border-top: 1px solid rgba(197, 223, 240, 0.4);
  font-size: 0.75rem;
  color: #5e7fa0;
  text-align: center;
}
```

- [ ] **Step 2: Commit changes**
```bash
git add static/css/styles.css
git commit -m "style: add personal story grid and iceberg styles"
```

---

### Task 3: Refactor Personal Story Template

**Files:**
- Modify: `templates/index.html`

- [ ] **Step 1: Refactor section structure to grid**
Update the `personal-story` section to include the grid and the iceberg SVG.

```html
<!-- PERSONAL STORY -->
<section class="personal-story relative py-24 lg:py-32 overflow-hidden" aria-label="Personal story">
  <div class="max-w-7xl mx-auto px-6 lg:px-8">
    <div class="personal-story__grid">

      <!-- Left Column: Narrative -->
      <div class="reveal" data-reveal-delay="100">
        <h2 class="font-display text-5xl sm:text-6xl font-bold text-ink leading-tight tracking-tight mb-12">
          Before it's too late
        </h2>
        <div class="personal-story__panel p-8 sm:p-12 rounded-2xl relative overflow-hidden">
          <span class="personal-story__quote-mark absolute">“</span>
          <div class="personal-story__body space-y-8 relative z-10">
            {% for paragraph in personal_story.paragraphs %}
            <p class="personal-story__paragraph text-xl text-ink leading-relaxed">
              {{ paragraph }}
            </p>
            {% endfor %}
          </div>
        </div>
      </div>

      <!-- Right Column: Iceberg Diagram -->
      <div class="personal-story__stats reveal" data-reveal-delay="300">
        <svg class="iceberg-svg" viewBox="0 0 320 400" xmlns="http://www.w3.org/2000/svg">
          <!-- Waterline -->
          <rect y="120" width="320" height="280" fill="rgba(255,255,255,0.05)" />
          
          <!-- Iceberg Shape -->
          <path d="M160 20 L220 120 L260 280 L160 380 L60 280 L100 120 Z" fill="#ffffff" opacity="0.9" />
          <path d="M160 20 L220 120 L160 140 L100 120 Z" fill="#ffffff" />
          
          <!-- Tip Layer -->
          <text x="160" y="70" text-anchor="middle" class="iceberg-label">Diagnosed</text>
          <text x="160" y="95" text-anchor="middle" class="iceberg-stat">29.4M</text>
          
          <!-- Middle Layer (Submerged) -->
          <text x="160" y="200" text-anchor="middle" class="iceberg-label iceberg-label--submerged">Undiagnosed</text>
          <text x="160" y="225" text-anchor="middle" class="iceberg-stat iceberg-stat--submerged">8.7M</text>
          <text x="160" y="245" text-anchor="middle" font-size="10" fill="rgba(255,255,255,0.7)">Risk triples after 40</text>
          
          <!-- Base Layer -->
          <text x="160" y="320" text-anchor="middle" class="iceberg-label iceberg-label--submerged">Prediabetes</text>
          <text x="160" y="345" text-anchor="middle" class="iceberg-stat iceberg-stat--submerged">97.6M</text>
          <text x="160" y="365" text-anchor="middle" font-size="10" fill="rgba(255,255,255,0.7)">8 in 10 don't know</text>
        </svg>
      </div>

    </div>

    <!-- Source Attribution -->
    <div class="personal-story__source reveal" data-reveal-delay="400">
      {{ personal_story.iceberg.source }}
    </div>
  </div>
</section>
```

- [ ] **Step 2: Commit changes**
```bash
git add templates/index.html
git commit -m "feat: refactor personal story to grid with iceberg SVG"
```

---

### Task 4: Verification Tests

**Files:**
- Create: `tests/test_iceberg_content.py`

- [ ] **Step 1: Write test for new content and layout**
Verify that the new iceberg statistics and source are present in the rendered HTML.

```python
import pytest
from main import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_iceberg_data_presence(client):
    """Verify that the iceberg statistics and source are in the DOM."""
    response = client.get('/')
    html = response.data.decode('utf-8')
    
    # Check for stats
    assert "29.4M" in html
    assert "8.7M" in html
    assert "97.6M" in html
    
    # Check for labels
    assert "Undiagnosed" in html
    assert "Prediabetes" in html
    
    # Check for source
    assert "CDC National Diabetes Statistics Report 2024" in html
```

- [ ] **Step 2: Run tests**
Run: `pytest tests/test_iceberg_content.py`
Expected: PASS

- [ ] **Step 3: Commit tests**
```bash
git add tests/test_iceberg_content.py
git commit -m "test: verify iceberg content and layout"
```
