# Cluely-Style Motion System Design

## Scope

Apply a polished, calm Cluely-inspired motion system to the existing FastAPI/Jinja diabetes awareness site.

The implementation targets only:

- `templates/index.html`
- `static/css/styles.css`
- `static/js/main.js`

The root `index.html` remains unchanged. Existing page sections, copy, navigation targets, and content structure remain unchanged.

## Goals

- Add a more refined motion system without changing the site layout.
- Keep the interaction appropriate for a health awareness site: calm, readable, and supportive.
- Use CSS and small vanilla JavaScript enhancements only.
- Preserve accessibility through `prefers-reduced-motion`.
- Fix stat animations so mixed values such as `537M`, `1 in 2`, and `90%` animate correctly.

## Motion Behaviors

### Page Load

The first viewport should feel gently staged:

- Welcome heading and subtitle fade upward.
- Hero eyebrow, headline, body, CTAs, stats, image, and badge enter with staggered timing.
- The hero image and badge receive subtle glow and floating motion.

### Scroll Reveals

Existing `.reveal` elements become the base motion primitive:

- Reveals use opacity, vertical translation, slight scale, and blur settling.
- Items reveal once when entering the viewport.
- Repeated content uses staggered timing through data attributes.
- Image containers settle more slowly than text so sections feel layered.

### Ambient Effects

Use restrained Cluely-like accents:

- Soft shimmer on primary CTA and gradient stripe surfaces.
- Gentle pulse/glow on logo and key visual badge.
- Subtle image hover scale remains, but with smoother timing.
- Navigation receives a smoother scrolled state.

### Reduced Motion

When `prefers-reduced-motion: reduce` is active:

- Reveal elements should be visible immediately.
- Floating, shimmer, pulse, and number animations should not run.
- Smooth scrolling should fall back to instant target jumps where practical.

## JavaScript Responsibilities

`static/js/main.js` remains vanilla JS and handles:

- Scroll reveal observation.
- Lazy image loading.
- Navigation scroll state.
- Anchor scrolling with fixed-nav offset.
- Stat animation for mixed text formats.

No build step, package manager, animation library, or frontend framework is added.

## Verification

Run the FastAPI app with:

```powershell
uvicorn main:app --reload
```

Verify:

- `/` renders successfully.
- Existing content and anchors still work.
- Sections reveal on scroll.
- Lazy images load.
- Stats end as `537M`, `1 in 2`, and `90%`.
- Root `index.html` is unchanged.
