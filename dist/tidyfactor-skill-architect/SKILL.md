---
name: tidyfactor-skill-architect
description: Governance layer that makes every Claude Skill built, audited, or refactored follow the TidyFactor Skill methodology (skill.md as dispatcher + references/commands + references/workflows + references/memory, one-workflow-one-outcome, quantified growth rule, no empty structures). Use together with skill-creator whenever the user asks to build a new skill, turn a workflow/prompt/persona into a real skill, audit an existing skill for structural compliance, decide whether a skill should grow a new file, or explicitly asks for a "TidyFactor skill" / "مهارة بمنهجية TidyFactor". This layer does not replace skill-creator's interview/draft/test/package loop — it constrains what that loop is allowed to produce. Do NOT use for general prompt writing, one-off instruction tweaks, or non-skill content tasks — this governs skill *structure*, not skill *content*.
---

# TidyFactor Skill Architect

A command dispatcher. This file does not do the work itself — it routes to the right command, which routes to the right workflow, which injects the right memory. Read `references/memory/spec.md` once per session before dispatching; it is the canonical rule set (8 structural rules) every command below enforces.

## Commands

| User intent | Command | What it loads |
|---|---|---|
| "Build me a skill for X" / "turn this into a skill" | `references/commands/init.md` | `workflows/create-skill.md` + `memory/spec.md` + `memory/growth-rule.md` + `assets/skill-md-skeleton.md` |
| "Check if this skill follows TidyFactor" / "audit this skill" | `references/commands/audit.md` | `workflows/audit-skill.md` + `memory/spec.md` |
| "Should I add a new file to this skill?" | `references/commands/grow.md` | `memory/growth-rule.md` |

Read only the command file that matches the request. Do not read all three.

## Non-negotiable constraints

The 8 structural rules every skill this layer produces must satisfy live in `references/memory/spec.md` — read them before drafting or auditing anything; do not restate them here. Embedding the rule text in this dispatcher would itself violate Rule 1 (Dispatcher Discipline).

## Handoff to skill-creator

Once a command has assembled the runtime context (workflow + memory + skeleton), continue with skill-creator's normal loop (`/mnt/skills/examples/skill-creator/SKILL.md`) for the interview, test prompts, validation (`quick_validate`), and packaging (`package_skill.py`) — but the draft skill-creator produces at its "Write the SKILL.md" step must satisfy `spec.md`'s 8 rules before you run `quick_validate`.
