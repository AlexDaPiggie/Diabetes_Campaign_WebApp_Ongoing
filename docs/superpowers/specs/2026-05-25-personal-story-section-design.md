# Personal Story Section Design

Date: 2026-05-25

## Goal

Add a Personal Story section to the Diabetes Awareness website directly after the Welcome section and before the Hero section. The section should feel simple, touching, and consistent with the current site design language.

## Source Content

The story source is `Guidelines/Personal_Story.md`.

The final website copy may be lightly edited or shortened for flow and layout, but it must preserve the original meaning and first-person voice:

- A father went to the hospital for a routine visit and received a severe Type 2 diabetes diagnosis.
- He had not recognized dramatic warning signs.
- The disease had been progressing quietly.
- He researched, changed his diet, movement, and daily lifestyle.
- Today, he does not take insulin because his lifestyle regulates his blood sugar.

The section must not add an explicit lesson, guarantee, CTA, or statement that readers can achieve the same outcome. The desired effect should come from the story itself.

## Layout

Use the selected option 2 design: an editorial story panel.

- Place it immediately after the Welcome section.
- Do not show a visible heading.
- Center the panel within the page using the same max-width rhythm as the current layout.
- Use a soft blue-tinted panel, subtle border, restrained shadow, and rounded corners that fit the current visual system.
- Include a subtle oversized quote mark as the editorial accent.
- Present the story as a short narrative block, split into readable paragraphs.
- Keep the section visually quiet enough that it transitions naturally from Welcome into Hero.

## Visual Language

The section must match the current site:

- Reuse the existing blue palette and Tailwind theme tokens where possible.
- Use existing typography conventions: display font for editorial accent only, readable body typography for the story text.
- Use `text-ink` and `text-ink-dim` style colors for copy.
- Match the current spacing scale, rounded panel style, borders, and soft shadow language.
- Avoid introducing a new color palette, new icon system, or unrelated decorative graphics.

## Motion

The section should participate in the current motion language:

- Use the existing reveal-on-scroll pattern for the story panel.
- Apply subtle motion consistent with current `reveal`, shimmer, and ambient sweep effects.
- Keep effects restrained so the section remains sincere and readable.
- Respect existing reduced-motion behavior.

## Data And Template Shape

Follow the existing data-driven pattern:

- Add a `personal_story` object to `data/content.json`.
- Render the section in `templates/index.html` between the Welcome section and Hero section.
- Add only the CSS needed for the new section in `static/css/styles.css`.
- Do not refactor unrelated page structure.

## Verification

Add or update focused tests to verify:

- The Personal Story section is rendered after Welcome and before Hero.
- The section has no visible heading.
- The story content includes a stable text hook from the source story.
- The section uses the expected motion/reveal hooks.
- Existing tests continue to pass.

Run verification with:

```powershell
python -m unittest discover -s tests -p "test_*.py" -q
```

`pytest` is not currently available in the local Python environment, so `unittest` discovery is the reliable baseline.
