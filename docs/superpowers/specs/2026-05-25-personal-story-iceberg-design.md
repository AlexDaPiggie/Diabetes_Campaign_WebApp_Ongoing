# Design Spec: "Hidden Burden" Personal Story Integration

**Date:** 2026-05-25
**Status:** Approved
**Topic:** Integrating USA undiagnosed diabetes statistics into the Personal Story section using an "Iceberg" metaphor.

## 1. Purpose & Success Criteria
The goal is to reinforce the "latency" of diabetes mentioned in the personal narrative with hard, trustworthy data.
*   **Success Criteria:**
    *   Side-by-side 50/50 layout (Narrative Left / Iceberg Right).
    *   Authentic USA-specific data from 2024 CDC reports.
    *   Visually reinforces the concept of "hidden" or "latent" illness.
    *   Clear source attribution for trustworthiness.

## 2. Architecture & Layout
The existing `personal-story` section will be refactored from a centered container to a grid-based layout.

### Layout (Desktop)
*   **Grid:** 2 columns, 1fr each.
*   **Left Column:** 
    *   Headline: "Before it's too late" (Left-aligned).
    *   Copy: Existing narrative about the quiet onset of diabetes.
    *   Style: Retains glassmorphic panel and subtle quote mark.
*   **Right Column:**
    *   Container: `personal-story__stats` panel with a subtle blue water-themed gradient background.
    *   Visual: Custom SVG Iceberg diagram.

### Layout (Mobile)
*   Stack vertically: Headline -> Narrative -> Iceberg.

## 3. Data & Iceberg Layers (USA 2024 Statistics)
The diagram uses data from the **CDC National Diabetes Statistics Report 2024** and **NCHS Data Brief No. 516**.

| Layer | Population Segment | Statistic | Visual Treatment |
| :--- | :--- | :--- | :--- |
| **Tip** (Above Water) | Diagnosed Adults | 29.4 Million | Bright, clear, high visibility. |
| **Middle** (Submerged) | Undiagnosed Adults | 8.7 Million | Deep blue; includes age breakdown (1.3% for 20-39, 5.6% for 40-59, 6.8% for 60+). |
| **Base** (Deepest) | Prediabetes | 97.6 Million | Darkest blue; "8 in 10 don't know it" label. |

## 4. Source Attribution
A citation will be placed at the bottom of the section:
> "Source: CDC National Diabetes Statistics Report 2024 & NCHS Data Brief No. 516. Data represents US adults (18+) from 2021–2023."

## 5. Technical Implementation Details
*   **HTML:** Use `<section class="personal-story">` with a `personal-story__grid` container.
*   **CSS:** Flexbox or Grid for the 50/50 split. Gradient backgrounds for the "water" effect.
*   **SVG:** Inline SVG for the iceberg to allow for easy animation and sharp rendering.
*   **Responsive:** Media query at `768px` to switch to single-column stacking.

## 6. Spec Self-Review
*   **Placeholder scan:** No TBDs. All stats are verified from 2024 reports.
*   **Consistency:** Headline alignment and split ratio are confirmed.
*   **Scope check:** Focused purely on the Personal Story section.
*   **Ambiguity check:** Age prevalence is explicitly mapped to the middle layer.
