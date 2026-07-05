---
name: ux-03-synthesis
description: Run UX step 03, Synthesis and Insights, for a Yoma Fleet feature. Use when the user says "synthesize research", "affinity mapping", "find themes", "empathy map", "journey map", or has raw research data from UX 02 to make sense of. Requires the UX 02 Research Data Pack.
---

# UX 03 — Synthesis & Insights

Turn raw research into evidence-backed insights. For large datasets (5+ transcripts), delegate the heavy clustering to the `synthesis-analyst` agent and review its output.

## Input contract

Require the UX 02 Research Data Pack (or equivalent raw research: transcripts, notes, survey exports). If missing, ask for it or offer to run `ux-02-user-research` first. Never synthesize from imagined data.

## Method chain (copy this checklist)

- [ ] 1. Affinity mapping → raw clusters from research
- [ ] 2. Thematic analysis → named themes with evidence
- [ ] 3. Empathy mapping → user mental model
- [ ] 4. Journey mapping → current-state experience with pain points

### 1. Affinity mapping

Break data into atomic observations (one fact/quote per note). Cluster by meaning, not by question asked. Label clusters only after grouping. Output FigJam-ready: cluster name + notes under each.

### 2. Thematic analysis

Promote clusters to themes only with evidence from 3+ participants. Each theme: name, one-sentence claim, supporting quotes (anonymized), count of participants, confidence (strong/moderate/weak).

### 3. Empathy mapping

Per segment: says / thinks / does / feels, built strictly from evidence. Mark any cell lacking evidence as "no data" rather than inventing.

### 4. Journey mapping

Current-state journey using `references/journey-map-format.md`: stages, actions, thoughts, emotion curve, pain points, opportunity areas. Pain points must trace back to specific evidence.

## Output contract

Produce the **Insights Report**: themes table, empathy maps per segment, journey map, and top pain points ranked by frequency x severity. Separate AI-suggested insights from designer-approved ones. End with: "Feeds into UX 04 Problem Definition: turns insights into design challenges."
