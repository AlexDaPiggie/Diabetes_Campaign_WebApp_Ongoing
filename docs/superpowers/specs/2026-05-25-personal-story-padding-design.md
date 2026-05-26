# Design Spec: Personal Section Padding Reduction

Reduce the top and bottom padding of the "Before it's too late" personal story section to create a tighter, more balanced layout while maintaining a premium, spacious feel.

## Architecture

This is a stylistic adjustment to the `personal-story` section in the main template.

### HTML Structure Changes (`templates/index.html`)

- **Component**: `<section class="personal-story ...">`
- **Current Classes**: `py-[115.2px] lg:py-[153.6px]`
- **New Classes**: `py-[96px] lg:py-[128px]`

## Components

### Section Container
The root element of the personal story section will be updated to use the new padding values. No other attributes or children will be modified.

## Data Flow

N/A - This is a purely presentation-layer change.

## Error Handling

N/A

## Testing

1. **Static Analysis**: Verify that `templates/index.html` contains the updated class strings.
2. **Automated Tests**: Run `pytest tests/test_personal_story.py` to ensure the section is still rendered correctly and no structural changes were accidentally introduced.
3. **Visual Verification**: The user will verify the new spacing in their local environment.
