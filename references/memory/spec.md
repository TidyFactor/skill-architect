# TidyFactor Skill Spec

<!-- last-verified: 2026-08-25 -->

Canonical structural rules. Every command and workflow in this skill enforces these. Pure rules — no rationale, no branding language (that's in `philosophy.md`, kept separate on purpose).

This file mirrors the 12 Structural Rules defined in the master `AGENTS.md` (TidyFactor Skills-LAB Master Workspace Rules). If the two ever diverge, the master `AGENTS.md` wins — update this file, not the other way around.

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

## The 12 Structural Rules

1. **Dispatcher Discipline.** `SKILL.md` is a router (~350 tokens), not a task-doer. It assembles only what a given task needs — a command loads one workflow and the memory that workflow needs, not everything in the skill. If a command file contains the actual instructions for producing output, that content belongs in a workflow; move it.
2. **One Workflow = One Outcome.** A workflow covering two distinct outcomes must be split into two. Every workflow defines validation — a checklist, not a vague success description.
3. **Operational Memory.** Memory is pure facts, schemas, terminology, templates, and technical rules — zero marketing commentary or narrative prose. Not narrative, not justification, not "why we do this."
4. **No Empty Structures.** A folder that would hold exactly one file should be that one file instead (`memory.md`, not `memory/context.md`).
5. **Philosophy Isolation.** Philosophy/branding language never enters an operational file (skill.md, any command, any workflow, any memory file an agent reads to execute a task). If it exists at all, it lives in `memory/philosophy.md`, unreferenced by any operational file — for a human reading the repo, not for the agent executing the skill.
6. **Trigger-Justified Growth.** New files are added only per `growth-rule.md`'s explicit triggers — never for anticipated future need.
7. **Quality Bar & Native Tooling.** Deterministic operations are encapsulated in `tools/` as wrappers over native toolchains (`tsc`, `node`, `python`, `git`, OS APIs). Do not script if a shell command is sufficient. No autonomous mass-edit scripts (e.g. no `auto_optimize.py`).
8. **Cross-Platform Parity.** 100% identical behavior across Antigravity, Claude Code, Cursor, and Codex.
9. **Platform Compatibility (SKILL.md Frontmatter Constraints).** The YAML frontmatter in `SKILL.md` must comply with all target platform limits. `name` is required and must match the skill directory name. `description` is required and must not exceed **1024 characters** (Claude Skills hard limit). The `description` should follow the "what + when" pattern: one sentence for what the skill does, one for when to trigger it. Move trigger keyword lists and technical details into the dispatcher body below the frontmatter — every token in `description` is loaded at session start regardless of skill activation. These limits are enforced by `tools/validate_frontmatter.py` and the NPM publisher pre-publish gate. Publishing MUST be blocked if any frontmatter constraint is violated.
10. **Tool Permission Declaration.** Skills that execute code via `tools/` must declare their tooling scope in `SKILL.md` dispatcher body. List: (a) languages invoked (node, python, shell), (b) whether tools are read-only or mutate files, (c) whether network access is required. This narrows the security surface and enables future `allowed-tools` frontmatter integration. Skills with no `tools/` directory skip this rule.
11. **Memory Freshness.** Every operational memory file must include a `<!-- last-verified: YYYY-MM-DD -->` HTML comment at the top, below the heading. During `audit`, verify that no memory file's last-verified date exceeds 180 days. Stale memory is flagged as a compliance warning (not a hard fail) but must be addressed before the next MINOR or MAJOR release.
12. **Skill vs MCP Boundary.** A capability belongs inside the skill (as a memory/workflow file) when it is: static knowledge, a decision framework, or a template. A capability belongs in an external MCP server when it: calls live APIs, queries databases, or performs stateful actions. If both layers are needed, the skill provides the decision logic and the MCP server provides the execution tools — never duplicate the same logic in both. Document the boundary in `SKILL.md` dispatcher body when a skill has a companion MCP server.

## The Contextual Decision Layer (CDL) Pattern

For complex skills where execution depends on high-impact architectural choices (e.g. `tidyfactor-styler`, `tidyfactor-next`):
1. **Thin Arbitration Protocol (`memory/decision-points.md`)**: Define triggers, boolean skip conditions, and pointers to existing SSOT memory catalogs. Never hardcode duplicate options.
2. **Pre-flight Brief & Cache (`brief` command / `.tidyfactor/<skill>-brief.md`)**: Interview once per project, cache baseline decisions, and run downstream commands silently without repetitive questions.
3. **Single-Round Batching & Priority**: Batch unresolved questions into 1 round (max 3 questions). Overflow is resolved to safe conservative defaults.
4. **Direct Invocation vs. Redesign Invariants**: Direct command calls never skip; redesign workflows silently preserve existing baselines unless overhaul is explicitly requested.
5. **Decision Alignment Axis**: Add Axis 7 (`D` - Decision Alignment) to the Pre-Emit Self-Critique to verify that generated output respects the confirmed brief.

## Loading order (progressive disclosure)

1. name + description (always in context once the skill is installed)
2. SKILL.md body (once the skill triggers)
3. The specific command file matched to the request
4. The specific workflow + memory files that command names — nothing else

## Cascade Update Protocol

When any structural rule in this file is added, modified, or removed:
1. Update the rule count in all referencing files: `SKILL.md` (both SSOT and `.agents/` wrapper), `references/workflows/audit-skill.md`, `README.md`, and `README.ar.md`.
2. Re-run `node tools/build-skill.js` to rebuild `dist/` and sync across all 5 target locations.
3. Verify zero stale references: search for the old count across all `.md` files.
