# Design Spec: Personal Story Body Text Size Update

## 1. Goal
Increase the body text size of the personal story narrative by 20% to improve readability and editorial impact, following the user's preference for direct utility class updates.

## 2. Technical Strategy
We will modify the inline Tailwind-style classes in the main template. This approach avoids creating new global CSS rules while providing the exact sizing requested.

## 3. Implementation Details

### 3.1 Template Update (`templates/index.html`)
- **Target Element**: The `<p>` tag within the `personal_story.paragraphs` loop (class `.personal-story__paragraph`).
- **Mobile Size**: Increase from `text-[18px]` to `text-[22px]`.
- **Desktop Size**: Increase from `md:text-[20px]` to `md:text-[24px]`.
- **Line Height**: Retain `leading-[1.8]` to ensure proportional spacing.

### 3.2 Stylesheet Consistency (`static/css/styles.css`)
- No changes required to `static/css/styles.css` as the user opted for Approach 1 (Direct Utility Update). The existing `.personal-story__paragraph` class in CSS handles alignment and transitions, which remain valid.

## 4. Verification Plan

### 4.1 Automated Tests
- Update `tests/test_content_typography.py` (if it exists) or `tests/test_personal_story.py` to assert the new text sizes:
    - Assert `text-[22px]` is present.
    - Assert `md:text-[24px]` is present.

### 4.2 Visual Regression
- Verify that the increased text size doesn't cause excessive overflow or clipping in the grid layout, particularly on smaller mobile viewports.
