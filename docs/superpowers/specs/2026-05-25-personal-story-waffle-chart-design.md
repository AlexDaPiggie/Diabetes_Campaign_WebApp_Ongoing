# Design Spec: "Hidden in Plain Sight" Waffle Chart

**Date:** 2026-05-25
**Status:** Approved
**Topic:** Replacing the "Iceberg" diagram with a 10x10 Waffle Chart representing US diabetes and prediabetes statistics.

## 1. Purpose & Success Criteria
The goal is to shift from a metaphorical "iceberg" to a relatable "people-focused" grid that visualizes the massive scale of the "latent" diabetes epidemic in the USA.
*   **Success Criteria:**
    *   10x10 grid of human silhouette icons (100 people).
    *   "Digital Scan" animation that reveals health status.
    *   Clearly distinguishes between Diagnosed, Undiagnosed (Hidden), and Prediabetes.
    *   Maintains the 50/50 side-by-side layout (Narrative Left / Waffle Right).

## 2. Data & Icon Breakdown
Based on **CDC 2024 National Diabetes Statistics Report** (Adults 18+).

| Category | Population | Percentage (Icons) | Visual Treatment |
| :--- | :--- | :--- | :--- |
| **Normal / Healthy** | ~120 Million | 46 icons | Neutral Grey |
| **Prediabetes** | 97.6 Million | 38 icons | Azure Blue (Soft Pulse) |
| **Diagnosed Diabetes** | 29.4 Million | 11 icons | Solid Navy Blue |
| **Undiagnosed Diabetes** | 8.7 Million | 5 icons | Flickering/Ghostly Blue |

## 3. Visual & Animation Design
### The Waffle Grid
*   **Icon:** Minimalist human silhouette SVG.
*   **Layout:** 10x10 grid on desktop; 5x20 grid on mobile (< 768px).
*   **Style:** Modern, clean, data-driven aesthetic.

### "Digital Scan" Animation
1.  **Initial State:** All 100 icons are Neutral Grey.
2.  **Trigger:** Animation starts when the section enters the viewport (Intersection Observer).
3.  **The Scan:** A horizontal light-blue gradient bar ("the scanner") moves vertically from top to bottom.
4.  **The Reveal:** As the bar passes an icon, it transitions to its final color/state.
5.  **Persistence:** Icons remain colored after the scan completes.

## 4. Labels & Legends
*   **Legend Items:** Located below the grid.
    *   **Solid Navy:** "Diagnosed (29.4M)"
    *   **Azure Blue:** "The Warning Zone (Prediabetes: 97.6M)"
    *   **Flickering Blue:** "Hidden Millions (Undiagnosed: 8.7M)"
    *   **Grey:** "Normal (120M)"
*   **Hover Interactivity:** Tooltips on icons provide extra context (e.g., "1 in 3 adults have prediabetes. 8 in 10 don't know it.").

## 5. Technical Implementation
*   **HTML:** Inline SVG for the grid or a Flex/Grid container of individual SVGs for easier animation control.
*   **CSS:** CSS Keyframes for the scan-bar movement and icon transitions.
*   **JS:** Intersection Observer to trigger the scanning animation.

## 6. Spec Self-Review
*   **Placeholder scan:** All stats are fixed based on 2024 CDC data.
*   **Internal consistency:** Grid total equals 100 icons exactly. Mobile layout accounted for.
*   **Scope check:** Replaces the iceberg component within the existing grid.
*   **Ambiguity check:** "Flickering/Ghostly" is defined as a transparency/opacity animation.
