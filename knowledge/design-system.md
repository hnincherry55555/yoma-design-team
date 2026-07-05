# Yoma Fleet Design System — Shared Reference

> Single source of truth for skills. Update via PR when the Figma library changes.

## Token naming convention

Format: `{category}/{role}/{modifier}` (e.g. `color/action/primary`, `space/inset/md`).

- Colors are semantic, not literal: `color/action/primary`, never `color/blue/500` at usage level
- Spacing scale: 4px base (4, 8, 12, 16, 24, 32, 48, 64)
- Type scale: TODO paste current scale from Figma variables
- Radius: TODO
- Elevation: TODO

## Component inventory

<!-- TODO: sync with the Figma library. Keep names exactly as in Figma. -->

| Component | Status | Notes |
|-----------|--------|-------|
| Button | TODO | variants: primary/secondary/ghost/destructive, sizes sm/md/lg |
| Input | TODO | states: default/focus/error/disabled |
| Card | TODO | |
| Bottom sheet | TODO | mobile pattern of choice for secondary actions |
| Table | TODO | B2B dashboards (PLUS+) |

## Do / Don't

- DO use library components before drawing anything new; a new component requires a named gap
- DO bind every fill, text style, and spacing value to a token (no hardcoded hex/px in hi-fi)
- DON'T detach instances; propose a variant instead
- DON'T introduce a new color role without a design-system PR

## Accessibility baked in

- Text contrast 4.5:1 minimum (3:1 for large text), touch targets 44x44px minimum
- Every interactive component defines: default, hover, focus-visible, active, disabled, error states
