---
name: ui-03-visual-design
description: Run UI step 03, Visual Design (Hi-Fi), for a Yoma Fleet feature. Use when the user says "hi-fi", "visual design", "style the screens", "apply the design system", "make it high fidelity", or after UI 02 usability testing passes. Requires the UI 02 Usability Report with critical issues resolved.
---

# UI 03 — Visual Design (Hi-Fi)

Style the validated structure. Tokens only; zero hardcoded values.

## Input contract

Require the UI 02 Usability Report showing critical issues resolved (exit criteria met). If missing, ask for it or offer to run `ui-02-prototype-testing` first. Read `${CLAUDE_PLUGIN_ROOT}/knowledge/design-system.md` and `${CLAUDE_PLUGIN_ROOT}/knowledge/copy-voice.md`.

## Method chain (copy this checklist)

- [ ] 1. Spacing & grid system → layout rules
- [ ] 2. Color & typography scale → visual hierarchy system
- [ ] 3. Component styling → styled UI elements
- [ ] 4. Visual system application → fully styled screens

### 1. Spacing & grid system

Define per-breakpoint grid (columns, margins, gutters) and confirm the 4px spacing scale application. Every spacing decision maps to a token.

### 2. Color & typography scale

Apply semantic color roles and the type scale from the design system. New roles require a design-system PR, not a local value. Pre-check contrast intent here (4.5:1) so UI 05 finds no surprises.

### 3. Component styling

Use library components; propose variants instead of detaching. Every interactive component shows all states: default, hover, focus-visible, active, disabled, error.

### 4. Visual system application

Apply across all screens and states from the Wireframe Pack, following `references/figma-frame-naming.md`. Write final UX copy per copy-voice rules (primary + 1 alternative per key string). Realistic content: long Myanmar strings, long names, edge amounts.

## Output contract

Produce the **Hi-Fi Pack**: styled screens (all states), token usage notes, UX copy table, and a deviation log (anywhere the design leaves the system, with justification). Separate AI-suggested from designer-approved. Gate: mockup review with BA/design team. End with: "Feeds into UI 04 Design System: codifies new patterns for scale."
