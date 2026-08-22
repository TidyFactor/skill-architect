# TidyFactor Skill Spec

Canonical structural rules. Every command and workflow in this skill enforces these. Pure rules — no rationale, no branding language (that's in `philosophy.md`, kept separate on purpose).

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

## Rules

1. **A Skill is not a prompt and not a file collection.** It assembles only what a given task needs — a command loads one workflow and the memory that workflow needs, not everything in the skill.
2. **Commands don't do tasks.** If a command file contains the actual instructions for producing output, that content belongs in a workflow; move it.
3. **One Workflow = One Outcome.** A workflow covering two distinct outcomes must be split into two.
4. **Every workflow defines validation.** A checklist, not a vague success description.
5. **No Empty Structures.** A folder that would hold exactly one file should be that one file instead (`memory.md`, not `memory/context.md`).
6. **Growth is triggered, not scheduled.** New files are added only per `growth-rule.md`'s explicit triggers — never for anticipated future need.
7. **Philosophy/branding language never enters an operational file** (skill.md, any command, any workflow, any memory file an agent reads to execute a task). If it exists at all, it lives in `memory/philosophy.md`, unreferenced by any operational file — for a human reading the repo, not for the agent executing the skill.
8. **Anti-Slop, Pre-Emit Critique & Mechanical Quality Control.** Every frontend/UI generation workflow must:
   - Declare a **Step 0 One-Line Design Read**.
   - Configure the **3-Dial System** (`designVariance`, `motionIntensity`, `visualDensity`).
   - Run **Pre-Emit Self-Critique (1-5 Scoring on 6 Axes)**: *Philosophy (P)*, *Hierarchy (H)*, *Execution (E)*, *Specificity (S)*, *Restraint (R)*, *Variety (V)*. Scores < 3 trigger an automatic revision pass. Output is stamped: `/* Pre-emit critique: P5 H4 E5 S4 R5 V5 */`.
   - Enforce mechanical pre-flight checks (eyebrow cap `ceil(sectionCount / 3)`, hero top padding cap `pt-24`, single-line CTAs, optical alignment, 16 named AI anti-patterns, and anti-interchangeable UI).
9. **SemVer Release Versioning & CHANGELOG as SSOT for Skill Evolution.**
   - Whenever a skill undergoes functional modifications, capability expansions (new commands, workflows, or toolsets), or structural refactoring, changes **MUST NEVER** occur as silent, unversioned drift.
   - Every modification requires an explicit **SemVer version bump** (`MAJOR` for breaking architecture shifts, `MINOR` for new commands/tools/capabilities, `PATCH` for bug fixes/refinements/link repairs).
   - **`CHANGELOG.md` is the Single Source of Truth (SSOT)** for skill history: Every release must have a dedicated, dated entry detailing added capabilities, modified workflows, and resolved defects.
   - Version bumps must synchronize atomically across: `package.json`, `.tidyfactor`, `brand.json`, `README.md`, `README.ar.md`, and compiled release archives (`<skill>-vX.Y.Z.skill` and `<skill>.skill`).

## Loading order (progressive disclosure)

1. name + description (always in context once the skill is installed)
2. SKILL.md body (once the skill triggers)
3. The specific command file matched to the request
4. The specific workflow + memory files that command names — nothing else
