# Personal Story Component Size Reduction Design

**Goal:** Reduce the size of all components in the diagram (waffle chart) and stats part (legend, callout) of the 'personal story' section by 20%.

**Target Area:** The right-hand side of the `personal-story` section.

## 1. Waffle Chart (Diagram)

| Property | Current | New (Reduced by 20%) |
| :--- | :--- | :--- |
| Container Max-width | 420px | **336px** |
| Container Max-width (Mobile) | 320px | **256px** |
| Grid Gap | clamp(5px, 0.55vw, 8px) | **clamp(4px, 0.44vw, 6.4px)** |

## 2. Source Link

| Property | Current | New (Reduced by 20%) |
| :--- | :--- | :--- |
| Font Size | 20px | **16px** (text-base) |
| Font Size (Mobile) | 16px | **13px** |
| Max-width | 420px | **336px** |

## 3. Legend & Stats

| Property | Current | New (Reduced by 20%) |
| :--- | :--- | :--- |
| Stat Number Font Size | 23px | **18px** |
| Stat Label Font Size | 14px | **11px** |
| Stat Icon Size | 24px (w-6) | **20px (w-5)** |
| Gap (Small) | gap-x-6 | **gap-x-5** |
| Gap (Large) | gap-x-10 | **gap-x-8** |

## 4. Callout

| Property | Current | New (Reduced by 20%) |
| :--- | :--- | :--- |
| Font Size | text-sm (14px) | **text-[11px]** |
| Max-width | max-w-sm (384px) | **max-w-[307px]** |

## Implementation Strategy

1.  **CSS Updates**: Modify `static/css/styles.css` for properties controlled by custom CSS classes (`.waffle-container`, `.waffle-grid`, `.personal-story__source`).
2.  **HTML Template Updates**: Modify `templates/index.html` for properties controlled by Tailwind-like utility classes in the legend and callout sections.
3.  **Verification**: Ensure the layout remains balanced and the 20% reduction is applied consistently.

## Testing Plan

- **Visual Inspection**: Verify the components appear smaller and proportionally correct.
- **Responsive Check**: Ensure the reduction works correctly on both mobile and desktop views.
- **Unit Tests**: Update or add tests in `tests/test_personal_story.py` to verify the presence of new size-related classes or style properties if applicable.
