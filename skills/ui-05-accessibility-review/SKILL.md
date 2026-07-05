---
name: ui-05-accessibility-review
description: Run UI step 05, Accessibility Review, for a Yoma Fleet design. Use when the user says "accessibility review", "a11y check", "WCAG audit", "contrast check", "touch targets", or when hi-fi screens or a design system update is ready for compliance checking. Requires the UI 04 System Update or UI 03 Hi-Fi Pack.
---

# UI 05 — Accessibility Review

WCAG 2.1 AA is the baseline, not a bonus. Five checks in order; the audit compiles them.

## Input contract

Require the UI 04 System Update (component library + token JSON) or, for screen-level review, the UI 03 Hi-Fi Pack. If missing, ask which feature/product and where the deliverable is. This review must be run by someone other than the screen's designer where possible; offer to delegate to the `a11y-auditor` agent.

## Method chain (copy this checklist)

- [ ] 1. Color contrast check → pass/fail per color pair (4.5:1 min)
- [ ] 2. Touch target review → flag targets under 44x44px
- [ ] 3. Keyboard navigation test → focus flow issues
- [ ] 4. Screen reader test (HUMAN executes) → missing labels, broken hierarchy
- [ ] 5. WCAG 2.1 AA audit → full compliance report

### 1. Color contrast check

Run `scripts/contrast_check.py <fg-hex> <bg-hex>` per pair, or pass a token JSON to check all color pairs used in text/background roles. Thresholds: 4.5:1 normal text, 3:1 large text (18pt+/14pt bold) and UI components.

### 2. Touch target review

From specs or Figma values: every interactive element 44x44px minimum (including spacing between adjacent targets). List violations with the frame name.

### 3. Keyboard navigation test

Walk each flow: logical focus order, visible focus-visible state on every interactive element, no keyboard traps, skip patterns for long lists. Document expected tab order per screen for the handoff spec.

### 4. Screen reader test

Prepare the test sheet: per screen, the expected reading order, labels for every control, heading hierarchy, and announcements for dynamic changes (loading, errors). The designer executes with VoiceOver/TalkBack and pastes results back. Do not invent results.

### 5. WCAG 2.1 AA audit

Compile all findings against `references/wcag-aa-checklist.md`. Each issue: criterion number, severity, screen, fix recommendation.

## Output contract

Produce the **A11y Compliance Report**: pass/fail per check, issue table, and a fix list ordered by severity. Critical issues block handoff. Separate AI-suggested findings from designer-verified ones. End with: "Feeds into UI 06 Developer Handoff: clean, accessible specs to engineering."
