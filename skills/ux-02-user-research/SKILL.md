---
name: ux-02-user-research
description: Run UX step 02, User Research, for a Yoma Fleet feature. Use when the user says "user research", "research plan", "interview users", "analytics review", "survey", or after UX 01 discovery is complete. Requires the UX 01 Discovery Brief with ranked assumptions.
---

# UX 02 — User Research

Run the four-method chain in order: analytics first (where to look), interviews (why), contextual inquiry (real environment), surveys (validate at scale).

## Input contract

Require the UX 01 Discovery Brief (research questions + ranked assumptions). If missing, ask for it or offer to run `ux-01-discovery` first. Read `${CLAUDE_PLUGIN_ROOT}/knowledge/products/<product>.md`.

## Hard rule

NEVER fabricate research data, user quotes, analytics numbers, or survey results. AI prepares instruments and analyzes real data the designer provides. If asked to invent findings, refuse and explain why.

## Method chain (copy this checklist)

- [ ] 1. Analytics review → behavioral baseline, where to look
- [ ] 2. User interviews (HUMAN executes) → qualitative why
- [ ] 3. Contextual inquiry (HUMAN executes) → real-environment behavior
- [ ] 4. Surveys → quantitative validation at scale

### 1. Analytics review

Ask the designer for available data (Amplitude exports, funnel numbers). Analyze drop-offs, frequency, segments. Output: behavioral baseline and the flows/segments interviews should probe.

### 2. User interviews

Generate a recruiting screener and interview guide from the research questions, using `references/research-plan-template.md`. 5-8 participants per segment is the default. After sessions, accept pasted notes/transcripts for cleanup and anonymization (strip names, phone numbers, KYC details before anything leaves the team).

### 3. Contextual inquiry

Draft an observation protocol: where, what tasks to observe, what to record. Flag safety and consent requirements (recording someone driving or at their workplace needs explicit consent).

### 4. Surveys

Only after qualitative signals exist. Draft survey questions from emerging themes using `references/survey-question-bank.md`. Rule: every question must map to a decision it will inform; delete questions that don't.

## Output contract

Produce the **Research Data Pack**: analytics baseline, anonymized interview/inquiry notes, survey results, and a coverage table mapping each risky assumption to the evidence gathered. Separate AI-suggested interpretations from raw data. End with: "Feeds into UX 03 Synthesis: raw material for finding patterns."
