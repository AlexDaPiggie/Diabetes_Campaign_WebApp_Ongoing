# Spec: Stats Animation Sequence

## 1. Goal
Implement a polished, sequenced animation for the "Personal Story" statistics section to enhance the storytelling impact. The animation should guide the user's eye from the source of the data to the specific percentages, concluding with a highlighted elderly demographic callout.

## 2. Animation Requirements
The animation must trigger as soon as the section scrolls into view (Intersection Observer) and follow this strict order:

### Phase 1: Source Fade-In
- **Target:** `.personal-story__source`
- **Effect:** Simple opacity fade (0 to 1).
- **Duration:** 500ms.

### Phase 2: Stats Group Fade-In
- **Target:** All `.motion-stat` and their associated labels.
- **Effect:** Group opacity fade (0 to 1).
- **Duration:** 500ms.
- **Timing:** Starts immediately after Phase 1 finishes.

### Phase 3: Synchronized Number Increment
- **Target:** All elements with `.animate-number` within this section.
- **Effect:** Numbers increment from 0 to their `data-target-number`.
- **Logic:** **Synchronized timing.** All numbers must start at 0 and reach their final value at the exact same time, regardless of how large the target number is.
- **Duration:** 1500ms.
- **Timing:** Starts immediately after Phase 2 finishes.

### Phase 4: Elderly Callout Fade-In
- **Target:** `.personal-story__callout`
- **Effect:** Opacity fade (0 to 1).
- **Duration:** 500ms.
- **Timing:** Starts immediately after Phase 3 finishes.

## 3. Technical Implementation Details
- **Trigger:** Use an `IntersectionObserver` with a threshold (e.g., 0.2) to detect when the section enters the viewport.
- **CSS:** Elements should start at `opacity: 0` (via a utility class or JS initial state).
- **JS:** Refactor the existing `animateNumber` logic to support a "synchronized duration" mode or a callback system to trigger the next phase.
- **Accessibility:** 
    - Respect `prefers-reduced-motion`.
    - Ensure text is visible if JS fails to load.

## 4. Prompt Structure (for the other model)
The final prompt will:
1.  Describe the DOM structure in text (since the model cannot see images).
2.  Define the 4-phase sequence with specific millisecond timings.
3.  Explain the math required for the "synchronized duration" increment effect.
4.  Provide the existing `main.js` and `styles.css` context for integration.
