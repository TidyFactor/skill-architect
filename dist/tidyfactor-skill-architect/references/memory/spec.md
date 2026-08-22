# TidyFactor Skill Spec

Canonical structural rules. Every command and workflow in this skill enforces these. Pure rules — no rationale, no branding language (that's in `philosophy.md`, kept separate on purpose).

This file mirrors the 8 Structural Rules defined in the master `AGENTS.md` (TidyFactor Skills-LAB Master Workspace Rules). If the two ever diverge, the master `AGENTS.md` wins — update this file, not the other way around.

## Anatomy

```
skill-name/
├── SKILL.md                    # dispatcher: intent -> command -> {workflow, memory}
└── references/
    ├── commands/ (or commands.md if only one)
    ├── workflows/ (or workflows.md if only one)
    └── memory/ (or memory.md if only one)
```

Start flat (one file per category). Split into a folder only when a category holds more than one distinct item — see `growth-rule.md`.

## Role definitions

- **skill.md** — the entry point. Declares what commands exist and what each one loads. Contains no task instructions itself.
- **Command** — a runtime dispatcher for one user intent. Selects a workflow, injects specific memory files, states what it does NOT load. A command never contains the domain knowledge or the step sequence itself — those live in workflow/memory files it points to.
- **Workflow** — the ordered steps for exactly one outcome. Every workflow ends with a validation checklist that defines what "done, correctly" means for that outcome.
- **Memory** — operational context loaded at runtime: facts, terminology, templates, domain rules, constraints. Not narrative, not justification, not "why we do this."

## The 8 Structural Rules

1. **Dispatcher Discipline.** `SKILL.md` is a router (~350 tokens), not a task-doer. It assembles only what a given task needs — a command loads one workflow and the memory that workflow needs, not everything in the skill. If a command file contains the actual instructions for producing output, that content belongs in a workflow; move it.
2. **One Workflow = One Outcome.** A workflow covering two distinct outcomes must be split into two. Every workflow defines validation — a checklist, not a vague success description.
3. **Operational Memory.** Memory is pure facts, schemas, terminology, templates, and technical rules — zero marketing commentary or narrative prose. Not narrative, not justification, not "why we do this."
4. **No Empty Structures.** A folder that would hold exactly one file should be that one file instead (`memory.md`, not `memory/context.md`).
5. **Philosophy Isolation.** Philosophy/branding language never enters an operational file (skill.md, any command, any workflow, any memory file an agent reads to execute a task). If it exists at all, it lives in `memory/philosophy.md`, unreferenced by any operational file — for a human reading the repo, not for the agent executing the skill.
6. **Trigger-Justified Growth.** New files are added only per `growth-rule.md`'s explicit triggers — never for anticipated future need.
7. **Quality Bar & Native Tooling.** Deterministic operations are encapsulated in `tools/` as wrappers over native toolchains (`tsc`, `node`, `python`, `git`, OS APIs). Do not script if a shell command is sufficient. No autonomous mass-edit scripts (e.g. no `auto_optimize.py`).
8. **Cross-Platform Parity.** 100% identical behavior across Antigravity, Claude Code, Cursor, and Codex.

## Loading order (progressive disclosure)

1. name + description (always in context once the skill is installed)
2. SKILL.md body (once the skill triggers)
3. The specific command file matched to the request
4. The specific workflow + memory files that command names — nothing else
