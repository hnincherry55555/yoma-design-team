---
name: discovery-kickoff-workshop
description: Draft a kick-off workshop agenda that turns stakeholder interview notes into aligned priorities and surfaced assumptions (step 2 of 4 in discovery-agent). Use when interviews are done and the team needs to align on scope, or the user says "kickoff workshop agenda".
---

# Discovery — Kick-off Workshop

HUMAN executes, AI prepares. This skill produces the agenda and structure; the designer or facilitator runs the actual workshop.

## Input contract

Stakeholder interview notes summary from the `discovery-stakeholder-interviews` skill (goals, constraints, expectations, open concerns). If this input is missing, run that skill first.

## Process

1. Draft a workshop agenda using `references/workshop-agenda-template.md`, covering: goal alignment, scope in/out, success metrics, and open questions — each seeded from the interview notes.
2. Output the agenda as a FigJam-ready structure: sections and sticky-note prompts the facilitator can paste directly into a board.
3. After the workshop runs, wait for the designer to paste back real outcomes (decisions made, priorities agreed, assumptions raised). Never invent workshop outcomes.
4. Summarize outcomes into: aligned priorities (ranked) and a raw list of surfaced assumptions (not yet scored).

## Output contract

Aligned priorities and a raw assumption list. This output is the required input for the `discovery-assumption-mapping` skill.
