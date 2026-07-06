---
name: discovery-assumption-mapping
description: Extract and rank assumptions surfaced during discovery by importance and evidence strength (step 3 of 4 in discovery-agent). Use when the user says "assumption mapping" or has raw assumptions from a workshop that need prioritizing before research.
---

# Discovery — Assumption Mapping

## Input contract

The raw assumption list and aligned priorities from the `discovery-kickoff-workshop` skill. If this input is missing, run that skill first (or extract assumptions directly from interview/workshop notes if provided ad hoc).

## Process

1. List every assumption surfaced so far — do not filter yet.
2. Score each on a 2x2 using `references/assumption-map-template.md`: importance to success (High/Medium/Low) x evidence strength (strong/weak/none).
3. Risk rank = high importance + weak/no evidence first. These are the riskiest assumptions.
4. Select the top 5 riskiest and rephrase each as a research question: "We believe [X]. We will know we are wrong if [signal]."

## Anti-patterns

- Do not assign "strong evidence" to an assumption just because a stakeholder stated it confidently — evidence means data, prior research, or documented precedent, not opinion.
- Do not limit the list to desirability assumptions; include business/viability and technical/feasibility assumptions raised in the workshop.

## Output contract

A ranked assumption map (full table) and the top 5 research questions. This output is the required input for the `discovery-competitive-scan` skill, and feeds directly into the Discovery Brief's research-questions section for UX 02.
