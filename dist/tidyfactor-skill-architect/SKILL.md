---
name: tidyfactor-skill-architect
description: Governance layer that makes every Claude Skill built, audited, or refactored follow the TidyFactor Skill methodology (skill.md as dispatcher + references/commands + references/workflows + references/memory, one-workflow-one-outcome, quantified growth rule, no empty structures). Use together with skill-creator whenever the user asks to build a new skill, turn a workflow/prompt/persona into a real skill, audit an existing skill for structural compliance, decide whether a skill should grow a new file, or explicitly asks for a "TidyFactor skill" / "مهارة بمنهجية TidyFactor". This layer does not replace skill-creator's interview/draft/test/package loop — it constrains what that loop is allowed to produce.
---

# TidyFactor Skill Architect

A command dispatcher. This file does not do the work itself — it routes to the right command, which routes to the right workflow, which injects the right memory. Read `references/memory/spec.md` once per session before dispatching; it is the canonical rule set every command below enforces.

## Commands

| User intent | Command | What it loads |
|---|---|---|
| "Build me a skill for X" / "turn this into a skill" | `references/commands/init.md` | `workflows/create-skill.md` + `memory/spec.md` + `memory/growth-rule.md` + `assets/skill-md-skeleton.md` |
| "Check if this skill follows TidyFactor" / "audit this skill" | `references/commands/audit.md` | `workflows/audit-skill.md` + `memory/spec.md` |
| "Should I add a new file to this skill?" | `references/commands/grow.md` | `memory/growth-rule.md` |

Read only the command file that matches the request. Do not read all three.

## Non-negotiable constraints on every skill this produces

These apply regardless of which command fired — hold skill-creator's own drafting step to these:

1. **skill.md is a dispatcher, not a task-doer.** It routes to workflows and memory; it does not contain the domain knowledge itself. If skill.md is doing the work instead of pointing to a file that does, that's a structural failure — fix it before packaging.
2. **One Workflow = One Outcome, with a validation checklist.** A workflow that covers two distinct outcomes must be split. A workflow without a validation checklist is incomplete.
3. **Memory is operational context, not narrative.** Facts, rules, terminology, templates — not prose explaining why the skill exists.
4. **No Empty Structures.** Don't create `references/commands/`, `references/workflows/`, or `references/memory/` as folders if the skill only needs one file of that kind — a single `commands.md` is correct until a second command exists. Don't scaffold for capabilities the skill doesn't have yet.
5. **Philosophy never ships inside skill.md or memory.** Branding language, manifestos, or rationale for the methodology itself belongs only in `memory/philosophy.md` (optional, human-facing) — never injected into the operational files an agent actually reads to execute.
6. **Growth is triggered, not scheduled.** A skill only gains a new file when `memory/growth-rule.md`'s criteria are met — never "for future-proofing."
7. **SemVer Releases & CHANGELOG as SSOT.** Any modification, capability expansion (commands, workflows, or toolsets), or structural refinement requires an explicit SemVer version bump (`MAJOR` for breaking architecture changes, `MINOR` for new commands/tools, `PATCH` for bug fixes) and a dedicated entry in `CHANGELOG.md` acting as the Single Source of Truth, synchronized across `package.json`, `.tidyfactor`, `brand.json`, `README.md`, and compiled release archives.

## Handoff to skill-creator

Once a command has assembled the runtime context (workflow + memory + skeleton), continue with skill-creator's normal loop (`/mnt/skills/examples/skill-creator/SKILL.md`) for the interview, test prompts, validation (`quick_validate`), and packaging (`package_skill.py`) — but the draft skill-creator produces at its "Write the SKILL.md" step must satisfy the constraints above before you run `quick_validate`.
