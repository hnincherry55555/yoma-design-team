# Figma Frame & File Naming (Hi-Fi)

## File structure
Page per flow: `UI03 - <flow>`. Cover frame with status chip: WIP / In review / Approved.

## Frame naming
`<product> / <flow> / <screen> / <breakpoint> / <state>`
e.g. `car-share / booking / vehicle-detail / mobile-360 / error-payment`

## Breakpoints
mobile-360 (default), mobile-390, tablet-768, desktop-1280, desktop-1440 (PLUS+ dashboards).

## Layer hygiene
- Auto-layout everywhere; no absolute-positioned patches
- Layers named semantically (`header`, `price-summary`), never `Frame 427`
- All fills/text/spacing bound to variables; deviation log for exceptions

## Copy
Final strings only in Approved frames; placeholders marked `[TBD]` block approval.
