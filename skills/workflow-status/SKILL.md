---
name: workflow-status
description: Report where each Yoma Fleet design feature stands in the 11-step workflow. Use when the user says "status", "where are we", "design pipeline status", "what's in progress", or asks about the state of design work across features or products.
---

# Workflow — Status

Summarize pipeline position across active features.

## Steps

1. Gather Project Tracker blocks: from the current conversation, from files the user points to, or from ClickUp (if connected, search design tasks by product).
2. For each feature, report one line: product, feature, current step (n/11), gate status, blocker if any, days since last movement (flag 5+ days as stalled).
3. Output a compact table sorted by: blocked first, then stalled, then by step descending (closest to shipping first).

```
| Product | Feature | Step | Status | Blocker |
|---------|---------|------|--------|---------|
```

4. End with: items needing the senior designer's attention (open gates, stalled features, unfilled product-knowledge TODOs encountered this week).
5. If asked for a leadership-ready version, rewrite conclusion-first in plain language without design jargon.
