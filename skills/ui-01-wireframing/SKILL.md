---
name: ui-01-wireframing
description: Run UI step 01, Wireframing (Lo-Fi), for a Yoma Fleet feature. Use when the user says "wireframe", "lo-fi", "sketch layouts", "content priority", or "block out screens", or after UX 05 user flows are complete. Requires the UX 05 IA Pack (validated flows).
---

# UI 01 — Wireframing (Lo-Fi)

Structure before style. No color, no type styling, no visual polish at this step.

## Input contract

Require the UX 05 IA Pack (user flows + sitemap). If missing, ask for it or offer to run `ux-05-ia-user-flows` first. Read the product file and `${CLAUDE_PLUGIN_ROOT}/knowledge/ux-principles.md`.

## Method chain (copy this checklist)

- [ ] 1. Content priority mapping → what goes where based on user needs
- [ ] 2. Paper sketching (HUMAN executes) → fast layout explorations
- [ ] 3. Digital lo-fi wireframes → structured screen layouts
- [ ] 4. Component blocking → reusable element inventory

### 1. Content priority mapping

Per screen in the flow: rank every content element and action by user need at that moment. One primary action per screen. Output a priority table per screen before any layout exists.

### 2. Paper sketching

Prompt the designer with Crazy 8s-style exploration briefs per key screen (the constraint or question each sketch round should answer). Review posted photos/descriptions and give structured feedback referencing Fitts and Hick by name.

### 3. Digital lo-fi wireframes

Describe layouts per screen for the chosen sketch direction, following `references/wireframe-annotation-rules.md`: regions, hierarchy, primary action placement (thumb zone on mobile), states (loading, empty, error, offline where the flow requires). Grayscale boxes and real content structure; use realistic content length (Myanmar strings run longer), never lorem ipsum for critical labels.

### 4. Component blocking

Inventory every repeated element across the wireframes. Map each to an existing design-system component from `${CLAUDE_PLUGIN_ROOT}/knowledge/design-system.md`; anything unmapped is a named gap that becomes a UI 04 candidate. No unnamed custom elements allowed forward.

## Output contract

Produce the **Wireframe Pack**: per-screen priority tables, annotated lo-fi layouts (Figma frame names per conventions), component inventory with design-system mapping and gaps. Separate AI-suggested from designer-approved. End with: "Feeds into UI 02 Prototyping & Testing: adds interaction to test with users." Gate: wireframe review with BA before proceeding.
