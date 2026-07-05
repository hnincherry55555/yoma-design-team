---
name: ui-02-prototype-testing
description: Run UI step 02, Prototyping and Usability Testing, for a Yoma Fleet feature. Use when the user says "prototype", "usability test", "think-aloud", "test script", "task completion", or after UI 01 wireframes pass review. Requires the UI 01 Wireframe Pack.
---

# UI 02 — Prototyping & Usability Testing

Validate structure before styling it. Testing real users is the point; AI prepares and analyzes, humans run sessions.

## Input contract

Require the UI 01 Wireframe Pack (reviewed). If missing, ask for it or offer to run `ui-01-wireframing` first.

## Hard rule

NEVER fabricate test results, participant behavior, or completion rates. Analyze only data the designer provides.

## Method chain (copy this checklist)

- [ ] 1. Interactive prototype → clickable flow
- [ ] 2. Think-aloud protocol (HUMAN executes) → real-time reactions
- [ ] 3. Moderated usability testing (HUMAN executes) → observed failures and friction
- [ ] 4. Task completion measurement → pass/fail rates per task

### 1. Interactive prototype

Specify the Figma prototype wiring: which frames connect, triggers, and which unhappy paths must be clickable (error and empty states included, not just the happy path). Scope: only flows serving the chosen HMWs.

### 2. Think-aloud protocol

Generate the facilitation script from `references/test-script-template.md`: intro, consent, warm-up, think-aloud reminder phrases, neutral probes ("what do you expect to happen?"), never leading.

### 3. Moderated usability testing

Generate task scenarios (goal-based, no interface words: "You need a car this Saturday morning" not "Tap the booking button"). 5 participants per segment default. Provide an observer note sheet: task, path taken, errors, quotes, severity.

### 4. Task completion measurement

From real session data: per-task completion (success/partial/fail), time on task, error count, single-ease question score. Use `references/task-metrics-sheet.md`. Classify issues by severity (critical: blocks task; serious: major friction; minor: cosmetic).

## Output contract

Produce the **Usability Report**: task metrics table, ranked findings with evidence, and required wireframe changes (critical issues must be fixed and retested before UI 03). Separate AI-suggested interpretations from observed data. End with: "Feeds into UI 03 Visual Design: validated structure gets styled."
