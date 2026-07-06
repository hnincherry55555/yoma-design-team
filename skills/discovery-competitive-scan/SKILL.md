---
name: discovery-competitive-scan
description: Scan comparable products for relevant flows, patterns, and gaps to inform a new feature (step 4 of 4 in discovery-agent). Use when the user says "competitive scan" or needs market context before defining the problem.
---

# Discovery — Competitive Scan

## Input contract

Product, feature name, and (if available) the ranked assumption map from `discovery-assumption-mapping` — use the riskiest assumptions to focus which flows and patterns matter most.

## Process

1. Identify 3-5 comparable products. Look regionally first (Grab, local Myanmar/Vietnam banking or fleet apps), then globally if no regional comparable exists.
2. For each comparable product, capture using `references/competitive-scan-worksheet.md`:
   - The relevant flow (e.g. booking, KYC upload, payment retry)
   - The specific pattern worth borrowing, named in Mobbin-style terms (e.g. "progressive disclosure form", "bottom sheet confirmation")
   - The gap or weakness we can exploit or should avoid repeating
3. Do not fabricate app behavior — if Mobbin or direct access isn't available, state the pattern from documented knowledge and flag it as "unverified, confirm in Mobbin before relying on it."

## Output contract

A competitive scan summary (table + 2-3 sentence synthesis of what it means for this feature). This is the final input the `discovery-agent` needs to compile the Discovery Brief.
