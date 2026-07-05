---
name: workflow-next-step
description: Route to the next step in the Yoma Fleet 11-step design workflow. Use when the user says "next step", "what's next", "continue the workflow", "move to the next phase", or finishes a step's deliverable and wants to proceed.
---

# Workflow — Next Step

Determine where a feature is in the chain and route forward.

## Steps

1. Ask for (or locate in the conversation) the Project Tracker or the most recent deliverable.
2. Identify the last completed step by its output contract:

| If the last deliverable is… | Next skill |
|-----------------------------|-----------|
| Discovery Brief | `ux-02-user-research` |
| Research Data Pack | `ux-03-synthesis` |
| Insights Report | `ux-04-problem-definition` |
| Problem Definition Doc | `ux-05-ia-user-flows` |
| IA Pack | `ui-01-wireframing` |
| Wireframe Pack (reviewed) | `ui-02-prototype-testing` |
| Usability Report (exit criteria met) | `ui-03-visual-design` |
| Hi-Fi Pack (mockup review passed) | `ui-04-design-system` |
| System Update | `ui-05-accessibility-review` |
| A11y Report (zero critical) | `ui-06-dev-handoff-qa` |
| Handoff Pack signed off | Feature complete: log open questions for the next UX 01 cycle |

3. Before routing, verify the gate: if the previous step's output contract or review gate is not met (e.g. critical usability issues open, mockup review skipped), stop and say exactly what is missing. Skipping gates creates rework; do not allow it silently.
4. Invoke the next skill and update the Project Tracker table.
