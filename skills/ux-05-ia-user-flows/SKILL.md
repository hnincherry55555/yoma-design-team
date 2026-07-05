---
name: ux-05-ia-user-flows
description: Run UX step 05, Information Architecture and User Flows, for a Yoma Fleet feature. Use when the user says "user flow", "sitemap", "card sorting", "tree testing", "IA", "navigation structure", or "map the flow", or after UX 04 problem definition is complete. Requires the UX 04 Problem Definition Doc.
---

# UX 05 — Information Architecture & User Flows

Structure the solution space before any screen is drawn.

## Input contract

Require the UX 04 Problem Definition Doc (chosen HMWs + design principles). If missing, ask for it or offer to run `ux-04-problem-definition` first. Read the product file for existing navigation context.

## Method chain (copy this checklist)

- [ ] 1. Card sorting (HUMAN executes with users) → how users mentally group content
- [ ] 2. Sitemap creation → navigation structure
- [ ] 3. Tree testing (HUMAN executes with users) → validated sitemap
- [ ] 4. User flow diagramming → screen-by-screen task paths

### 1. Card sorting

Generate the card set (content/features affected by scope) and a session protocol (open sort for new areas, closed sort for fitting into existing nav). 15-30 cards, 5+ participants. Analyze real results only.

### 2. Sitemap creation

From sort results plus existing product IA: proposed structure with labels in user language (from research vocabulary, not internal jargon). Flag every label that differs from users' words. Apply Miller's Law: max ~7 items per nav level.

### 3. Tree testing

Generate task scenarios ("Where would you go to…?") covering the changed areas. Success threshold: 70%+ direct success per task; below that, revise and note what changed.

### 4. User flow diagramming

For each chosen HMW: screen-by-screen flow using `references/figjam-flow-conventions.md`. Cover the happy path plus defined unhappy paths (error, empty, no-network, permission-denied). Every decision diamond gets all branches resolved; no dangling arrows.

## Output contract

Produce the **IA Pack**: validated sitemap, task-success results, and user flow diagrams (FigJam-ready descriptions or Mermaid). Separate AI-suggested from designer-approved. End with: "Feeds into UI 01 Wireframing: the skeleton to build lo-fi screens on."
