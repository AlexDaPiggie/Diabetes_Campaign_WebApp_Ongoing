# Plan: Welcome Section Background Image & Animation Refinement

Add a secondary background layer to the 'Welcome Section' using `Welcome_Background.png` with a specific centered, rounded-corner layout and a refined animation sequence.

## 1. Research & Analysis
- **Current State:**
  - `templates/index.html`: Contains the `<section id="welcome">` with a `motion-welcome-sweep` overlay.
  - `static/css/styles.css`: Defines the gradient sweep and initial state of welcome elements.
  - `static/js/main.js`: Handles animation triggers (currently uses `IntersectionObserver` or simple class additions).
- **Target State:**
  - Initial load: Gradient glow blue background only.
  - Step 1: "Sweepline" effect (blue gradient sweep) triggers.
  - Step 2: `Welcome_Background.png` fades in. It is centered, 70% size on desktop, rounded corners.
  - Step 3: Welcome Title and Nav Bar fade in simultaneously with the image.
  - Step 4: Rest of the animations trigger as before.

## 2. Proposed Changes

### 2.1 Templates (`templates/index.html`)
- Add a new container `<div class="welcome-image-layer"></div>` inside the `#welcome` section.
- This layer will hold the background image.
- Ensure the hierarchy is:
  1. Base Background (Blue Gradient Glow)
  2. `welcome-image-layer` (The 70% centered image)
  3. `motion-welcome-sweep` (The overlay for the sweep effect)
  4. Content (Title, Nav Bar, Subtitle)

### 2.2 Styles (`static/css/styles.css`)
- Define `.welcome-image-layer`:
  - `position: absolute; top: 50%; left: 50%; transform: translate(-50%, -50%);`
  - `width: 70vw; height: 70vh;` for desktop.
  - `border-radius: 24px;` (Subtle roundness).
  - `background: url('../images/Welcome_Background.png') center/cover no-repeat;`
  - `opacity: 0; transition: opacity 1s ease-out;`
  - Media query for mobile: `width: 90vw; height: 85vh;` to cover more screen.
- Adjust `z-index` values to ensure correct stacking.
- Ensure `motion-welcome-sweep` remains visible above the background but below the text.

### 2.3 Scripts (`static/js/main.js`)
- Refine the animation timeline:
  - Add a slight delay to the image/title/nav fade-in to ensure the sweep effect completes (or starts) first.
  - Sequence:
    1. Add `.is-active` to `#welcome` to start the sweep.
    2. After ~800ms (sweep duration), add a class (e.g., `.show-content`) to trigger the image and title/nav fade.

## 3. Implementation Steps

1. **Verification:** Confirm the exact path to `Welcome_Background.png`. (Completed)
2. **Template Update:** Edit `templates/index.html` to add the image layer.
3. **Style Update:** Edit `static/css/styles.css` with the new positioning and transition rules.
4. **Logic Update:** Edit `static/js/main.js` to manage the timing of the `.show-content` class.

## 4. Verification Plan
- **Visual Check:**
  - Does the image appear centered?
  - Are the corners rounded?
  - Does it take up ~70% of desktop space?
  - Does it expand on mobile?
- **Animation Check:**
  - Gradient Sweep -> Image/Title/Nav Fade.
- **Console Check:** Ensure no missing image errors.
