---
name: discovery-stakeholder-interviews
description: Prepare a stakeholder interview guide covering goals, constraints, and expectations for a new feature (step 1 of 4 in discovery-agent). Use when the user says "stakeholder interview guide" or is kicking off a feature and needs to align with PM/BA first.
---

# Discovery — Stakeholder Interviews

HUMAN executes, AI prepares. This skill produces the guide; it never fabricates the answers.

## Input contract

Product (Car Share, PLUS+, Better, or Easy Lease), feature name, and business goal as currently understood. If any are missing, ask before proceeding.

## Process

1. Generate a stakeholder interview guide using `references/interview-guide-template.md`, tailored to the product and feature.
2. Identify who should be interviewed (PM, BA, Scrum Master, and any domain owner relevant to the feature).
3. Hand the guide to the designer and stop. Wait for the designer to paste back real notes from the actual conversations.
4. Once notes are provided, summarize them into: goals, constraints, expectations, and open concerns per stakeholder. Never invent quotes or answers that were not provided.

## Output contract

A completed interview guide (if notes are not yet available) or a structured summary of goals / constraints / expectations (once notes are provided). This output is the required input for the `discovery-kickoff-workshop` skill.
