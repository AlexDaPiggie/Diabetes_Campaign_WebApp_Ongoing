# Personal Story Vertical Gap Reduction Design

**Goal:** Reduce the vertical gaps between components in the 'stat' part of the 'personal story' section by 20%.

**Target Area:** The right-hand side of the `personal-story` section.

## Vertical Gap Adjustments

| Gap Location | Current Spacing | New Spacing (20% Reduction) |
| :--- | :--- | :--- |
| **Waffle to Source** | `margin-top: 1rem` (16px) | **`margin-top: 0.8rem` (12.8px)** |
| **Source to Legend** | 28px (4px bottom + 24px top) | **22.4px (3.2px bottom + 19.2px top)** |
| **Legend to Callout** | `mt-4` (16px) | **`mt-[12.8px]` (12.8px)** |

## Specific Code Changes

1.  **Source Link** (`.personal-story__source`):
    *   `margin: 1rem auto 0.25rem` -> **`margin: 0.8rem auto 0.2rem`**.
2.  **Legend Container**:
    *   `mt-6` -> **`mt-[19.2px]`**.
3.  **Elderly Callout**:
    *   `mt-4` -> **`mt-[12.8px]`**.

## Implementation Strategy

1.  **CSS Updates**: Modify `static/css/styles.css` for `.personal-story__source`.
2.  **HTML Template Updates**: Modify `templates/index.html` for legend and callout utility classes.
3.  **Verification**: Verify the vertical rhythm is tighter and visually consistent with the previous component size reductions.

## Testing Plan

- **Visual Inspection**: Confirm the vertical gaps are noticeably smaller.
- **Unit Tests**: Create a new test file or update the existing one to verify the presence of these specific spacing values.
