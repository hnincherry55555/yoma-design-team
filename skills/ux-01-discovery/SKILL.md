---
name: ux-01-discovery
description: Run UX step 01, Discovery and Stakeholder Alignment, for a Yoma Fleet feature. Use when starting a new feature or project, or when the user says "discovery", "stakeholder alignment", "kickoff", "assumption mapping", "competitive scan", or "start UX for [feature]". First step of the 11-step design workflow; requires no prior deliverable.
---

# UX 01 — Discovery & Stakeholder Alignment

Run the four-method chain in order. Each output feeds the next. Sequence is not optional.

## Input contract

This is the first step, so no prior deliverable is required. Ask for, and do not proceed without: the product (Car Share, PLUS+, Better, or Easy Lease), the feature name, and the business goal as currently understood. Then read `${CLAUDE_PLUGIN_ROOT}/knowledge/products/<product>.md` for context.

## Method chain (copy this checklist into your response and check off as you go)

- [ ] 1. Stakeholder interviews → goals, constraints, expectations
- [ ] 2. Kick-off workshop → aligned priorities, surfaced assumptions
- [ ] 3. Assumption mapping → assumptions ranked by risk
- [ ] 4. Competitive scan → market context and gaps

### 1. Stakeholder interviews (HUMAN executes, AI prepares)

Generate a stakeholder interview guide using `references/interview-guide-template.md`. Tailor questions to the product and feature. Never fabricate stakeholder answers; wait for the designer to paste notes back before summarizing.

### 2. Kick-off workshop (HUMAN executes, AI prepares)

From interview notes, draft a workshop agenda: goal alignment, scope in/out, success metrics, open questions. Output a FigJam-ready structure (sections and sticky prompts).

### 3. Assumption mapping

From interview and workshop notes, extract every assumption. Rank each on a 2x2: importance to success x evidence strength. Use `references/assumption-map-template.md`. The riskiest assumptions (high importance, low evidence) become research questions for UX 02.

### 4. Competitive scan

Identify 3-5 comparable products (regional first: Grab, local banking/fleet apps, then global). For each: relevant flows, patterns worth borrowing, gaps we can exploit. Cite Mobbin-style pattern names.

## Output contract

Produce the **Discovery Brief** containing: business goal, user problem hypothesis, scope in/out, ranked assumption map, competitive scan summary, and the research questions for the next step. Separate AI-suggested items from designer-approved items. End with: "Feeds into UX 02 User Research: these research questions define who to talk to and what to ask."
