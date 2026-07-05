---
name: ux-04-problem-definition
description: Run UX step 04, Problem Definition, for a Yoma Fleet feature. Use when the user says "define the problem", "POV statement", "HMW", "how might we", "prioritize opportunities", or "design principles", or after UX 03 synthesis is complete. Requires the UX 03 Insights Report.
---

# UX 04 — Problem Definition

Convert insights into a prioritized, actionable problem space.

## Input contract

Require the UX 03 Insights Report (themes + ranked pain points). If missing, ask for it or offer to run `ux-03-synthesis` first. Read the product file in `${CLAUDE_PLUGIN_ROOT}/knowledge/products/` and `${CLAUDE_PLUGIN_ROOT}/knowledge/ux-principles.md`.

## Method chain (copy this checklist)

- [ ] 1. POV statements → "user needs X because Y"
- [ ] 2. HMW questions → reframed design opportunities
- [ ] 3. Prioritization matrix → ranked by impact/effort
- [ ] 4. Design principles → guardrails for solution decisions

### 1. POV statements

For each top pain point: "[Specific user] needs [need, not solution] because [evidence-backed insight]." Reject any POV that embeds a solution ("needs a button" is not a need). See `references/pov-hmw-examples.md`.

### 2. HMW questions

3-5 HMWs per POV, spanning breadth: amplify good, remove bad, question assumption, flip the problem. Not so broad they're useless, not so narrow they dictate a solution.

### 3. Prioritization matrix

Score each HMW: user impact (from evidence) x business impact (from Discovery Brief goals) x effort (flag "needs dev input" where unknown). Output 2x2 placement and a ranked list. Effort estimates are AI-suggested until BA/dev confirms; label them as such.

### 4. Design principles

3-5 project-specific principles derived from themes (e.g. "Progress is never lost" for a KYC-heavy flow). Each principle: name, one sentence, the evidence that motivated it, and one example of what it rules out.

## Output contract

Produce the **Problem Definition Doc**: POVs, HMW list, prioritization matrix, chosen HMW(s) for this cycle, design principles. Separate AI-suggested from designer-approved (designer picks the final HMWs with PM/BA alignment). End with: "Feeds into UX 05 IA & User Flows: structures the solution space."
