# Diabetes Campaign

A website to raise awareness about diabetes and accompany diabetes patients in improving their diets and lifestyle.

## Overview

Diabetes Campaign is an informational website with a dual mission:

- **Awareness** — help the general public recognise the early signs of diabetes and understand the condition
- **Support** — provide diabetes patients with practical knowledge about medications, lifestyle changes, and community connection

The site targets both undiagnosed individuals who may be experiencing symptoms and diagnosed patients looking for guidance and peer support. It presents key diabetes statistics (537M adults worldwide, 1 in 2 undiagnosed, 90% are Type 2) and walks visitors through symptoms, treatment options, and community resources.

## Tech Stack

**Current:**
- HTML5 + CSS3 — single static page, no frameworks or JavaScript
- Google Fonts: [Playfair Display](https://fonts.google.com/specimen/Playfair+Display) (headings) and [Inter](https://fonts.google.com/specimen/Inter) (body/UI)
- All CSS is inline in `<style>` tags within `index.html`

**Planned:**
- Backend to be added (technology TBD)
- Possible multi-page expansion
- Hosting on Cloudflare

## Project Structure

```
Diabetes_Campaign/
├── index.html                  # Main entry point — the entire site (HTML + inline CSS)
├── README.md                   # This file
├── CLAUDE.md                   # Behavioral guidelines for Claude/LLM agents
├── AGENTS.md                   # Same guidelines (duplicate, used by other agent frameworks)
├── PLAN.md                     # Familiarisation plan for new contributors
├── .gitignore                  # Ignores CLAUDE.md and editor temp files
│
├── Guidelines/                 # Design system reference and visual mockups
│   ├── DESIGN.md               # Design tokens (colors, typography, spacing, components)
│   ├── Touching_Quote.txt      # Inspirational quote for the project's tone
│   ├── Welcome.png             # Welcome section mockup
│   ├── Welcome_Color_Palette.png
│   ├── Welcome_Section_ratio.png
│   ├── Pages.png               # Page layout mockups
│   ├── CurrentPages.png        # Current page designs
│   ├── ColorPalette.png        # Color palette reference
│   └── Testimonials.png        # Testimonials section mockup
│
└── IndexPage/                  # Images used on the live site
    ├── Diabetes_Community.png  # Community photo (hero + community section)
    ├── Patients_in_Hospital.png# Symptoms section image
    └── Medication.png          # Medications section image
```

### Key files explained

| File | Purpose |
|---|---|
| `index.html` | The complete website. Contains all sections (Welcome, Hero, Symptoms, Medications, Community, Footer) and all CSS. Edit this to change the site. |
| `Guidelines/DESIGN.md` | Design system adapted from a Mistral AI template. The color names and font references in this file describe the *template's* orange palette — the actual site uses a blue palette. Use this file as a structural reference for component patterns, spacing, and typography hierarchy, not for exact color values. |
| `CLAUDE.md` / `AGENTS.md` | Behavioral rules for coding agents working on this project: think before coding, prefer simplicity, make surgical changes, and work toward verifiable goals. |
| `Guidelines/*.png` | Visual mockups and design references. These informed the current layout and are useful when designing new sections. |

## Site Sections

The page is a single scrolling layout with anchor navigation:

1. **Nav** — sticky top bar with logo, section links, and CTAs ("Find Support", "Learn More")
2. **Welcome** — full-width blue gradient band with a welcoming message
3. **Hero** — headline ("Understanding diabetes. Together."), key stats, and a community photo with an "Early detection saves lives" badge
4. **Symptoms** — lists warning signs (thirst, weight changes, blurred vision, fatigue, slow healing, tingling) with a hospital corridor image
5. **Medications** — covers insulin therapy, oral medications, CGM devices, diet/exercise, and medication adjustment with a medication supplies image
6. **Community** — encourages joining support groups, sharing stories, accessing peer-reviewed tips, and participating in events
7. **Footer** — four-column grid (brand, Learn, Support, About) with copyright

## Design System

### Colors

The site uses a blue-based palette defined as CSS custom properties in `:root`:

| Token | Hex | Role |
|---|---|---|
| `--primary` | `#1D5FAD` | Buttons, links, accent elements |
| `--primary-deep` | `#0F3D7A` | Button hover/pressed states |
| `--primary-light` | `#D6EEFF` | Light accent backgrounds |
| `--accent` | `#7EC8E3` | Gradient stops, secondary accent |
| `--accent-light` | `#EEF7FF` | Subtle accent backgrounds |
| `--ink` | `#0F2A4A` | Primary text |
| `--slate` | `#3A5F86` | Secondary text |
| `--steel` | `#5E7FA0` | Tertiary text |
| `--muted` | `#8FAFC8` | Disabled/placeholder text |
| `--canvas` | `#FAFCFF` | Page background |
| `--surface` | `#F0F8FF` | Alternate section background |
| `--surface-warm` | `#E8F4FF` | Hero/footer background |
| `--hairline` | `#C5DFF0` | Borders |
| `--hairline-soft` | `#DAEEFF` | Subtle dividers |

### Typography

- **Playfair Display** (serif) — hero headlines, section titles, stat numbers, brand name
- **Inter** (sans-serif) — body text, navigation, buttons, labels, captions

### Design Reference

`Guidelines/DESIGN.md` contains a comprehensive design system adapted from the Mistral AI brand. It was used as a structural template — the spacing scale, border-radius tokens, component patterns, and typographic hierarchy are relevant, but the **color values and font families in DESIGN.md do not match the actual site**. The site uses the blue palette above and Playfair Display instead of PP Editorial Old. When adding new components, follow the patterns in DESIGN.md but use the actual site's design tokens.

## Getting Started

No build tools or dependencies required:

1. Clone the repository
2. Open `index.html` in a browser
3. To make changes, edit `index.html` directly and refresh

For a better development experience, use a live-reload server (e.g., VS Code's Live Server extension).

## Deployment

The site is planned to be hosted on Cloudflare. As a static HTML site, it can be deployed to any static hosting (Cloudflare Pages, GitHub Pages, Netlify, etc.) by serving the root directory.

## Future Roadmap

- **Backend** — add server-side functionality for dynamic content, user accounts, or community features
- **Multi-page expansion** — split the single-page layout into dedicated pages for deeper content
- **Content growth** — expand each section with more detailed information, resources, and interactive tools
- **Community features** — discussion forums, user stories, support group directories

## Agent Guidelines

When working on this project as a coding agent, follow the rules in `CLAUDE.md`:

- **Think before coding** — state assumptions, surface tradeoffs, ask when uncertain
- **Simplicity first** — minimum code to solve the problem; no speculative features or premature abstractions
- **Surgical changes** — touch only what's needed; don't refactor unrelated code
- **Goal-driven execution** — define success criteria and verify before declaring done

Style conventions: no comments unless the *why* is non-obvious; match existing formatting; use the CSS custom properties defined in `:root` rather than hardcoding colors.
