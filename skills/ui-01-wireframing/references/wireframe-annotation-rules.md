# Wireframe Annotation Rules

## Frame naming
`[UI01] <product> / <flow> / <screen> / <state>` e.g. `[UI01] car-share / booking / vehicle-detail / default`

## Required states per screen
default, loading, empty, error; plus offline for mobile booking/payment flows.

## Annotation format (sticky per frame)
- Purpose: the one job of this screen
- Primary action: what and why it wins
- Content source: where each dynamic element comes from (API field, user input)
- Open questions: flagged with `?` for BA review

## Layout rules
- Mobile: primary action inside thumb zone; destructive actions separated (Fitts)
- Max choice sets ~5-7 visible (Hick, Miller); overflow goes behind progressive disclosure
- Grouping communicated by spacing first (Gestalt), boxes second
