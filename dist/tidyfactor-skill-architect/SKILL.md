---
name: tidyfactor-skill-architect
description: "Master governance layer for AI Coding Agent Skills. Use when building a new skill, auditing for structural compliance, generating test scenarios, evaluating file growth, or when the user asks for a 'TidyFactor skill' or 'مهارة بمنهجية TidyFactor'. Anti-triggers: Do NOT use for general prompt writing or non-skill content tasks."
---

# TidyFactor Skill Architect

A command dispatcher. This file does not do the work itself — it routes to the right command, which routes to the right workflow, which injects the right memory. Read `references/memory/spec.md` once per session before dispatching; it is the canonical rule set (12 structural rules) every command below enforces.

## Commands

| User intent | Command | What it loads |
|---|---|---|
| "Build me a skill for X" / "turn this into a skill" | `references/commands/init.md` | `workflows/create-skill.md` + `memory/spec.md` + `memory/growth-rule.md` + `assets/skill-md-skeleton.md` |
| "Check if this skill follows TidyFactor" / "audit this skill" | `references/commands/audit.md` | `workflows/audit-skill.md` + `memory/spec.md` |
| "Test this skill" / "generate test scenarios" | `references/commands/test.md` | `workflows/test-skill.md` + `memory/spec.md` |
| "Should I add a new file to this skill?" | `references/commands/grow.md` | `memory/growth-rule.md` |

Read only the command file that matches the request. Do not read all four.

## Non-negotiable constraints

The 12 structural rules every skill this layer produces must satisfy live in `references/memory/spec.md` — read them before drafting or auditing anything; do not restate them here. Embedding the rule text in this dispatcher would itself violate Rule 1 (Dispatcher Discipline).

## Handoff to skill-creator

Once a command has assembled the runtime context (workflow + memory + skeleton), continue with skill-creator's normal loop (`/mnt/skills/examples/skill-creator/SKILL.md`) for the interview, test prompts, validation (`quick_validate`), and packaging (`package_skill.py`) — but the draft skill-creator produces at its "Write the SKILL.md" step must satisfy `spec.md`'s 12 rules before you run `quick_validate`.

## Tooling Scope (Rule 10)

- **Languages**: Python, Node.js
- **Mutations**: File creation/modification (skill scaffolding, archive building)
- **Network**: None required
