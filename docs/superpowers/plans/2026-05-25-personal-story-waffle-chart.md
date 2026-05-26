# "Hidden in Plain Sight" Waffle Chart Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Replace the iceberg diagram with a 10x10 Waffle Chart of human silhouettes that "reveals" diabetes status via a digital scan animation.

**Architecture:** Update `content.json` with the latest CDC 2024 statistics. Refactor the `personal-story` section in `index.html` to render a grid of 100 SVG icons. Use CSS for the "scanning" bar animation and state transitions, and JS for the intersection trigger.

**Tech Stack:** Tailwind CSS, Vanilla CSS (animations), Vanilla JS (Intersection Observer), Jinja2, SVG.

---

### Task 1: Update Content Data

**Files:**
- Modify: `data/content.json`

- [ ] **Step 1: Update statistics and add waffle config**

```json
  "personal_story": {
    "paragraphs": [
      "No warning signs, creeping up quietly. That was how diabetes came to my dad. Everything felt normal until the day he received a life-changing diagnosis: severe Type 2 diabetes. The damage was already done. He was told to start insulin immediately, and would likely be on it for the rest of his life."
    ],
    "waffle": {
      "stats": {
        "diagnosed": 11,
        "undiagnosed": 5,
        "prediabetes": 38,
        "healthy": 46
      },
      "labels": {
        "diagnosed": "Diagnosed (29.4M)",
        "undiagnosed": "Hidden Millions (8.7M)",
        "prediabetes": "The Warning Zone (97.6M)",
        "healthy": "Normal (120M)"
      },
      "source": "Source: CDC National Diabetes Statistics Report 2024 & NCHS Data Brief No. 516. Data represents US adults (18+) from 2021–2023."
    }
  }
```

- [ ] **Step 2: Commit changes**
```bash
git add data/content.json
git commit -m "data: update personal story with waffle chart stats"
```

---

### Task 2: Define Waffle Chart Styles

**Files:**
- Modify: `static/css/styles.css`

- [ ] **Step 1: Add waffle grid and scan animation styles**

```css
/* --- Waffle Chart --- */
.waffle-container {
  position: relative;
  width: 100%;
  max-width: 450px;
}

.waffle-grid {
  display: grid;
  grid-template-columns: repeat(10, 1fr);
  gap: 8px;
}

@media (max-width: 767px) {
  .waffle-grid {
    grid-template-columns: repeat(5, 1fr);
  }
}

.waffle-icon {
  width: 100%;
  height: auto;
  fill: #e5e7eb; /* Neutral Grey */
  transition: fill 0.5s ease, opacity 0.5s ease;
}

/* State Classes */
.waffle-icon--diagnosed { fill: #0f2a4a; }
.waffle-icon--prediabetes { 
  fill: #3498db; 
  animation: pulse-soft 3s infinite ease-in-out;
}
.waffle-icon--undiagnosed { 
  fill: #65b8e8; 
  animation: flicker 2s infinite ease-in-out;
}

/* Scan Bar */
.waffle-scan-bar {
  position: absolute;
  top: -20px;
  left: 0;
  width: 100%;
  height: 4px;
  background: linear-gradient(90deg, transparent, #65b8e8, transparent);
  box-shadow: 0 0 15px #65b8e8;
  opacity: 0;
  pointer-events: none;
  z-index: 10;
}

.waffle-container.scanning .waffle-scan-bar {
  animation: waffle-scan 2.5s cubic-bezier(0.4, 0, 0.2, 1) forwards;
}

/* Animations */
@keyframes waffle-scan {
  0% { top: -20px; opacity: 0; }
  10% { opacity: 1; }
  90% { opacity: 1; }
  100% { top: 100%; opacity: 0; }
}

@keyframes pulse-soft {
  0%, 100% { opacity: 1; }
  50% { opacity: 0.7; }
}

@keyframes flicker {
  0%, 100% { opacity: 0.9; }
  50% { opacity: 0.4; }
  75% { opacity: 0.8; }
}
```

- [ ] **Step 2: Commit changes**
```bash
git add static/css/styles.css
git commit -m "style: add waffle chart and scan animation styles"
```

---

### Task 3: Implement Waffle Template

**Files:**
- Modify: `templates/index.html`

- [ ] **Step 1: Replace Iceberg with Waffle Grid**

```html
      <!-- Right Column: Waffle Chart -->
      <div class="personal-story__stats flex flex-col items-center justify-center reveal" data-reveal-delay="300">
        <div class="waffle-container" id="waffle-chart">
          <div class="waffle-scan-bar"></div>
          <div class="waffle-grid">
            {# 11 Diagnosed #}
            {% for i in range(11) %}
              <svg class="waffle-icon" data-status="diagnosed" viewBox="0 0 24 24"><path d="M12 12c2.21 0 4-1.79 4-4s-1.79-4-4-4-4 1.79-4 4 1.79 4 4 4zm0 2c-2.67 0-8 1.34-8 4v2h16v-2c0-2.66-5.33-4-8-4z"/></svg>
            {% endfor %}
            {# 5 Undiagnosed #}
            {% for i in range(5) %}
              <svg class="waffle-icon" data-status="undiagnosed" viewBox="0 0 24 24"><path d="M12 12c2.21 0 4-1.79 4-4s-1.79-4-4-4-4 1.79-4 4 1.79 4 4 4zm0 2c-2.67 0-8 1.34-8 4v2h16v-2c0-2.66-5.33-4-8-4z"/></svg>
            {% endfor %}
            {# 38 Prediabetes #}
            {% for i in range(38) %}
              <svg class="waffle-icon" data-status="prediabetes" viewBox="0 0 24 24"><path d="M12 12c2.21 0 4-1.79 4-4s-1.79-4-4-4-4 1.79-4 4 1.79 4 4 4zm0 2c-2.67 0-8 1.34-8 4v2h16v-2c0-2.66-5.33-4-8-4z"/></svg>
            {% endfor %}
            {# 46 Healthy #}
            {% for i in range(46) %}
              <svg class="waffle-icon" data-status="healthy" viewBox="0 0 24 24"><path d="M12 12c2.21 0 4-1.79 4-4s-1.79-4-4-4-4 1.79-4 4 1.79 4 4 4zm0 2c-2.67 0-8 1.34-8 4v2h16v-2c0-2.66-5.33-4-8-4z"/></svg>
            {% endfor %}
          </div>
        </div>

        <!-- Legend -->
        <div class="mt-12 grid grid-cols-2 gap-4 text-xs font-bold tracking-wider uppercase text-ink/70">
          <div class="flex items-center gap-2">
            <span class="w-3 h-3 rounded-full bg-[#0f2a4a]"></span>
            {{ personal_story.waffle.labels.diagnosed }}
          </div>
          <div class="flex items-center gap-2">
            <span class="w-3 h-3 rounded-full bg-[#65b8e8] animate-pulse"></span>
            {{ personal_story.waffle.labels.undiagnosed }}
          </div>
          <div class="flex items-center gap-2">
            <span class="w-3 h-3 rounded-full bg-[#3498db]"></span>
            {{ personal_story.waffle.labels.prediabetes }}
          </div>
          <div class="flex items-center gap-2">
            <span class="w-3 h-3 rounded-full bg-gray-300"></span>
            {{ personal_story.waffle.labels.healthy }}
          </div>
        </div>
      </div>
```

- [ ] **Step 2: Commit changes**
```bash
git add templates/index.html
git commit -m "feat: replace iceberg with waffle chart grid"
```

---

### Task 4: Trigger Scan Animation

**Files:**
- Modify: `static/js/main.js`

- [ ] **Step 1: Add intersection observer for waffle scan**

```javascript
// Waffle Chart Scan Trigger
const initWaffleScan = () => {
  const waffle = document.getElementById('waffle-chart');
  if (!waffle) return;

  const observer = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
      if (entry.isIntersecting) {
        waffle.classList.add('scanning');
        
        // Staggered reveal of icons based on status
        const icons = waffle.querySelectorAll('.waffle-icon');
        icons.forEach((icon, index) => {
          const status = icon.getAttribute('data-status');
          // Delay reveal until scan bar reaches approx position
          const delay = (index / icons.length) * 2000; 
          setTimeout(() => {
            icon.classList.add(`waffle-icon--${status}`);
          }, delay + 300);
        });

        observer.unobserve(waffle);
      }
    });
  }, { threshold: 0.5 });

  observer.observe(waffle);
};

document.addEventListener('DOMContentLoaded', initWaffleScan);
```

- [ ] **Step 2: Commit changes**
```bash
git add static/js/main.js
git commit -m "feat: add JS trigger for waffle scan animation"
```

---

### Task 5: Verification

- [ ] **Step 1: Update test_iceberg_content.py to test_waffle_content.py**
- [ ] **Step 2: Run tests**
- [ ] **Step 3: Commit**
