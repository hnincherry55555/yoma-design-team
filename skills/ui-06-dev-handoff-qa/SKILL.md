---
name: ui-06-dev-handoff-qa
description: Run UI step 06, Developer Handoff and QA, for a Yoma Fleet feature. Use when the user says "handoff", "dev handoff", "spec", "handoff notes", "design QA", "compare build to design", or when a design has passed accessibility review and is ready for engineering. Requires the UI 05 A11y Compliance Report with no critical issues open.
---

# UI 06 — Developer Handoff & QA

The last gate. Engineering gets complete, accessible, unambiguous specs; the loop closes with design QA on the build.

## Input contract

Require the UI 05 A11y Compliance Report with zero open critical issues. If critical issues remain, stop and route back to `ui-05-accessibility-review`. Read `${CLAUDE_PLUGIN_ROOT}/knowledge/design-system.md` for token/component names used in specs.

## Method chain (copy this checklist)

- [ ] 1. Spec annotation → measurements, states, tokens documented
- [ ] 2. Interaction state documentation → hover, active, error, empty states
- [ ] 3. Edge case documentation → what happens when things go wrong
- [ ] 4. Async walkthrough / Loom (HUMAN executes) → dev team briefed
- [ ] 5. Design QA review → built vs designed comparison, sign-off

### 1. Spec annotation

Per screen, using `references/handoff-spec-template.md`: layout (spacing tokens, breakpoints), component + variant names matching the library, token names for every value, and expected focus/tab order from UI 05. DevMode-friendly: names in the spec must match Figma exactly.

### 2. Interaction state documentation

Every interactive element: all states with trigger, visual change (token deltas), and animation intent (duration, easing, what moves). Include loading and skeleton behavior.

### 3. Edge case documentation

Work through `references/edge-case-checklist.md` per screen: empty, error, offline, slow network, long content, permission denied, concurrent change. Every case gets defined behavior; "not applicable" must be stated, never silent.

### 4. Async walkthrough

Draft the Loom script: flow purpose, decisions that need explanation, known trade-offs, where edge cases live in the file. Designer records; link goes in the ClickUp task.

### 5. Design QA review

When the build is ready: compare built vs designed per screen and state. Output a diff table (screen, expected, actual, severity, screenshot refs). Sign-off requires all serious+ diffs resolved. Post the QA result to the ClickUp task.

## Output contract

Produce the **Handoff Pack**: annotated specs, interaction/state docs, edge case docs, walkthrough script, and (post-build) the QA diff table with sign-off status. Separate AI-suggested from designer-approved. End with: "Shipped. Back to research: log open questions and metrics to watch for the next UX 01 cycle."
