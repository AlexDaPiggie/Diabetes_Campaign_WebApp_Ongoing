# Design Spec: Personal Story Refactor (May 2026)

## Overview
Refactor the "Personal Story" section to transition from a left-aligned, high-contrast "editorial" style to a centered, blue-gradient narrative style that matches the provided visual reference (`Guidelines/Current_Personal_Story_Section.png`).

## Goals
- Align layout with the centered aesthetic of the visual mockup.
- Replace the cream background with a light blue gradient.
- Increase the visual contrast between the heading and body text.
- Remove the vertical accent rule.

## Architecture & Components

### 1. HTML Structure (`templates/index.html`)
- **Container**: Use `<section class="personal-story ...">` instead of `.personal-story--editorial`.
- **Inner Wrapper**: A centered, maximum-width container (`max-w-4xl mx-auto text-center`).
- **Heading**:
  - Remove the flex wrapper and the `.personal-story__accent-rule`.
  - Heading text "A routine visit changed everything." will be a direct child of the centered wrapper.
  - Apply `font-display` (Playfair Display) and significantly larger sizing.
- **Body**:
  - Narrative paragraphs will be rendered from `personal_story.paragraphs` data.
  - Staggered animation (reveal) will be preserved but centered.

### 2. Styling (`static/css/styles.css`)
- **Background**: Ensure `.personal-story` uses the `linear-gradient(180deg, #fafcff 0%, #eef7ff 52%, #fafcff 100%)` and its background blobs.
- **Heading**:
  - Target the heading within `.personal-story`.
  - `font-size`: `3.5rem` to `4.5rem` (responsive).
  - `font-weight`: `700` (bold) to increase contrast ratio.
  - `margin-bottom`: Generous spacing (e.g., `4rem`).
- **Body Text**:
  - `font-size`: `1.25rem` (text-xl).
  - `line-height`: `1.8` (leading-relaxed).
  - `max-width`: Limit the width of the centered text block for optimal readability (e.g., `max-w-2xl` or `max-w-3xl`).
- **Cleanup**: Mark `.personal-story--editorial` and related rules for removal if no longer needed.

## Data Flow
- Content continues to be sourced from `data/content.json` -> `personal_story.paragraphs`.
- The heading text "A routine visit changed everything." is currently hardcoded in the template; it should remain hardcoded or be moved to `data/content.json` if consistency is preferred (the user image specifically shows this text).

## Testing Strategy
- **Visual Verification**: Confirm layout matches the screenshot.
- **Unit Tests**:
  - Update `tests/test_personal_story.py` to assert the absence of `.personal-story__accent-rule`.
  - Verify centered alignment classes (`text-center`).
  - Verify the correct section class is used (`.personal-story`).
  - Ensure the "A routine visit changed everything." text is present.

## Spec Self-Review
1. **Placeholder scan**: No "TBD" or "TODO" items.
2. **Internal consistency**: The transition from `--editorial` to the base `.personal-story` class is consistent with the desired blue gradient.
3. **Scope check**: Focused solely on the personal story section.
4. **Ambiguity check**: Sizing and spacing are explicitly defined as "generous" and "significantly larger," which will be refined during implementation to match the screenshot's proportions.
