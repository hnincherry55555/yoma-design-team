---
name: ui-04-design-system
description: Run UI step 04, Design System and Component Library, for Yoma Fleet. Use when the user says "design system", "component library", "atomic design", "design tokens", "document component", or after UI 03 hi-fi produces new patterns. Requires the UI 03 Hi-Fi Pack (or a specific component/token change request).
---

# UI 04 — Design System & Component Library

Codify patterns atomically: atoms → molecules → organisms → tokens → docs.

## Input contract

Require the UI 03 Hi-Fi Pack, specifically the component inventory gaps and deviation log. For standalone system work, require a named component or token change request instead. Read `${CLAUDE_PLUGIN_ROOT}/knowledge/design-system.md`.

## Method chain (copy this checklist)

- [ ] 1. Atomic inventory (atoms) → base elements: color, type, icons
- [ ] 2. Molecules → combined elements: inputs, buttons
- [ ] 3. Organisms → full components: nav, cards, forms
- [ ] 4. Token definition → JSON-ready design tokens
- [ ] 5. Component documentation → usage guidelines per component

### 1-3. Atomic build-up

For each new pattern from the gap list, place it at the correct atomic level. Before creating anything, check for an existing component or variant that covers 80% of the need; extend rather than duplicate. Each component defines: variants, all interaction states, min touch target 44x44, content min/max behavior (long MM strings), and RTL-safety notes if applicable.

### 4. Token definition

Emit tokens as JSON following the `{category}/{role}/{modifier}` convention. Run `scripts/validate_tokens.py <file.json>` to check naming and completeness before handoff. Semantic roles only; no literal color names at usage level.

### 5. Component documentation

Use `references/component-doc-template.md` per component: anatomy, variants, states, do/don't, accessibility notes, and code-mapping name for Code Connect.

## Output contract

Produce the **System Update**: new/changed components with docs, validated token JSON, and a migration note for the other 3 products (which existing screens are affected). Update `knowledge/design-system.md` inventory via PR. Separate AI-suggested from designer-approved. End with: "Feeds into UI 05 Accessibility Review: check the system meets WCAG."
