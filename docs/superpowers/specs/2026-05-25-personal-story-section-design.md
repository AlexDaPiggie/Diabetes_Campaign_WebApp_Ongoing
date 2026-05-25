# Personal Story Section Design (Revised: High-Contrast Editorial)

Date: 2026-05-25
Status: Approved Design

## Goal

Add a Personal Story section to the Diabetes Awareness website that feels human, authoritative, and deeply personal. This section replaces the previous "clinical" blue design with a high-contrast editorial look that prioritizes readability and emotional weight.

## Source Content
The story source is `Guidelines/Personal_Story.md`.

- Intro hook: "A routine visit changed everything."
- Core narrative: A life-changing diagnosis of severe Type 2 diabetes found during a routine visit, followed by research, hard lifestyle changes, and the successful regulation of blood sugar without insulin today.
- Tone: Sincere, first-person narrative.

## Layout & Typography

- **Section Container:** Full-width section with a solid background.
- **Content Wrapper:** A narrow centered column (`max-w-2xl`) to ensure a comfortable reading line length.
- **Intro Hook:** Large, bold statement (`text-4xl` or `text-5xl`) in `font-display`. It acts as the visual entry point.
- **Editorial Accent:** A thin, elegant vertical line (rule) to the left of the intro hook.
- **Body Text:** Standard `text-lg` or `text-xl` paragraphs with generous vertical spacing (`space-y-8`) and loose line-height (`leading-relaxed`).
- **Vertical Rhythm:** Increased top and bottom padding for the entire section (`py-24` or `py-32`) to let the content breathe.

## Visual Language

- **Background:** Warm off-white / "paper" tone (e.g., `#FCFAF7`). No gradients, tints, or "shimmer" effects.
- **Typography Colors:** 
    - Intro & Body: `text-ink` (deep charcoal/navy) for high contrast and professional clarity.
    - Avoid `text-ink-dim` or faded grays to ensure the story feels "loud" and clear.
- **Style:** Clean, minimalist, and "unboxed." No cards, borders, or heavy shadows.

## Motion

- **Staggered Reveal:** Each paragraph (and the intro hook) should fade up individually as the user scrolls.
- **Timing:** Slower, more deliberate transitions (e.g., `duration-1000` or `duration-1200`) to encourage a thoughtful reading pace.
- **No Shimmer:** Remove the `motion-shimmer` effect to maintain a focused, sincere atmosphere.
- **Reduced Motion:** Respect `prefers-reduced-motion` by disabling all transitions and delays.

## Implementation Details

- **Data:** Story text remains in `data/content.json` under `personal_story`.
- **Template:** Rendered in `templates/index.html` between the Welcome section and the Hero section.
- **CSS:** Specific classes for `.personal-story--editorial` and its children in `static/css/styles.css`.

## Verification

- **Layout Check:** Verify column width is constrained and centered.
- **Contrast Check:** Ensure deep charcoal text on a warm white background.
- **Motion Check:** Verify staggered, slow fade-up transitions on scroll.
- **Sequence Check:** Section must appear after Welcome and before Hero.
