---
name: workflow-start-project
description: Kick off a new design project or feature through the Yoma Fleet 11-step workflow. Use when the user says "start a new feature", "start project", "new design project", "begin design for [feature]", or names a product and feature they want to design. Loads product context and routes to UX 01 Discovery.
---

# Workflow — Start Project

Initialize a feature in the 11-step design workflow.

## Steps

1. Ask (if not given): which product (Car Share, PLUS+, Better, Easy Lease), the feature name, and the business goal as currently stated by PM/BA.
2. Read `${CLAUDE_PLUGIN_ROOT}/knowledge/products/<product>.md`. If the file still has unfilled TODOs relevant to this feature, list them and ask the designer to confirm or fill the gaps now; wrong product context poisons every later step.
3. Create the **Project Tracker** block the team will carry through all steps:

```
# <Product> — <Feature> — Design Tracker
Started: <date> | Designer: <name> | ClickUp: <link>

| Step | Status | Deliverable link | Gate passed |
|------|--------|------------------|-------------|
| UX 01 Discovery | in progress | | |
| UX 02 User Research | pending | | |
| UX 03 Synthesis | pending | | |
| UX 04 Problem Definition | pending | | |
| UX 05 IA & User Flows | pending | | |
| UI 01 Wireframing | pending | | wireframe review |
| UI 02 Prototype & Testing | pending | | exit criteria |
| UI 03 Visual Design | pending | | mockup review |
| UI 04 Design System | pending | | |
| UI 05 A11y Review | pending | | zero critical |
| UI 06 Handoff & QA | pending | | sign-off |
```

4. If ClickUp is connected, offer to create the feature task with this tracker as the description.
5. Route to `ux-01-discovery` and begin its method chain.
