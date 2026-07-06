# Yoma Fleet Design Team Plugin

AI-native design workflow for the Yoma Fleet design team (3 designers, 4 products). Encodes our 11-step NN/g-based process as chained skills: the output of each step is the required input of the next. Sequence is not optional.

## The workflow

| Phase | Step | Skill | Method chain |
|-------|------|-------|--------------|
| UX | 01 | `ux-01-discovery` | Stakeholder interviews → kickoff workshop → assumption mapping → competitive scan |
| UX | 02 | `ux-02-user-research` | Analytics review → user interviews → contextual inquiry → surveys |
| UX | 03 | `ux-03-synthesis` | Affinity mapping → thematic analysis → empathy mapping → journey mapping |
| UX | 04 | `ux-04-problem-definition` | POV statements → HMW questions → prioritization matrix → design principles |
| UX | 05 | `ux-05-ia-user-flows` | Card sorting → sitemap → tree testing → user flow diagramming |
| UI | 01 | `ui-01-wireframing` | Content priority → paper sketching → digital lo-fi → component blocking |
| UI | 02 | `ui-02-prototype-testing` | Interactive prototype → think-aloud → moderated testing → task metrics |
| UI | 03 | `ui-03-visual-design` | Spacing/grid → color/type scale → component styling → visual system application |
| UI | 04 | `ui-04-design-system` | Atoms → molecules → organisms → token definition → component docs |
| UI | 05 | `ui-05-accessibility-review` | Contrast → touch targets → keyboard → screen reader → WCAG 2.1 AA audit |
| UI | 06 | `ui-06-dev-handoff-qa` | Spec annotation → interaction states → edge cases → async walkthrough → design QA |

Workflow helpers: `workflow-start-project` (kick off a feature with product context), `workflow-next-step` (route to the next step in the chain), `workflow-status` (where is each feature in the pipeline).

## Ground rules baked into every skill

- Each skill requires the previous step's deliverable before it runs.
- Human-only methods (interviews, moderated tests, screen reader runs, Loom walkthroughs) are prepared by AI, executed by a designer. Skills never fabricate research data or user quotes.
- Every output separates AI-suggested from designer-approved.
- WCAG 2.1 AA is a baseline, not a bonus.

## Product knowledge

`knowledge/products/` holds one file per product (Car Share, PLUS+, Better, Easy Lease): users, goals, constraints, tone. Skills read these at runtime. **Fill in the TODO sections before first use** and review each file every release.

## Install (team members)

Option A, from GitHub (recommended once this repo is pushed):

```
/plugin marketplace add hnincherry55555/yoma-design-team
/plugin install yoma-fleet-design-team@yoma-fleet-design
```

Option B, Cowork: install the packaged `yoma-fleet-design-team.plugin` file via Settings > Capabilities.

## Connectors

- **Figma**: configured in `.mcp.json` (official Figma MCP, OAuth on first use).
- **ClickUp**: connect via your Claude connector settings; skills reference ClickUp for task creation and status.

No credentials live in this repo. Auth is OAuth or environment-based only.

## Maintenance

- Owner: Pyae Phyo Kyaw (UX/UI Designer, IT Department)
- Changes go through GitHub PR review.
- Versioning (semver): patch = wording, minor = new templates/references, major = process changes.
