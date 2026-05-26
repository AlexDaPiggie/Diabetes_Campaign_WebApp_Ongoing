# Design Spec: Welcome Section Enhancements

**Date:** 2026-05-26
**Topic:** Welcome Section Visual Polish
**Status:** Approved

## Goals
- Improve the visual hierarchy of the "Welcome" section.
- Move the primary title and divider higher on the screen for better composition.
- Increase the weight and size of key text elements for better legibility and impact.

## Changes

### 1. Positioning and Layout
- **Target:** `.motion-welcome-content` container in `templates/index.html`.
- **Action:** Adjust vertical padding to shift content upwards.
- **Implementation:** Replace `py-[96px]` with `pt-[64px] pb-[128px]`.

### 2. Title Enhancements
- **Target:** `.motion-welcome-title` (h2).
- **Action:** Increase font weight.
- **Implementation:** Replace `font-medium` with `font-semibold`.

### 3. Divider Enhancements
- **Target:** `.motion-welcome-divider`.
- **Action:** Increase line thickness.
- **Implementation:** Replace `h-px` with `h-0.5`.

### 4. Subtitle Enhancements
- **Target:** `.motion-welcome-copy` (p).
- **Action:** Increase font size and weight.
- **Implementation:** Replace `text-[18px] md:text-[20px]` with `text-[24px] md:text-[28px]` and add `font-semibold`.

## Success Criteria
- The "Diabetes Awareness" title and divider appear higher on the screen.
- The title is visibly bolder.
- The divider line is thicker (2px).
- The subtitle is significantly larger and bolder, making it a strong secondary element.

## Verification Plan
- Manually inspect the "Welcome" section in the browser.
- Verify Tailwind classes are correctly applied in `templates/index.html`.
