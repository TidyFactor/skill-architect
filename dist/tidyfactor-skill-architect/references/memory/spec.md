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

## The 14 Structural Rules

1. **Dispatcher Discipline.** `SKILL.md` is a router (~350 tokens), not a task-doer. It assembles only what a given task needs — a command loads one workflow and the memory that workflow needs, not everything in the skill. If a command file contains the actual instructions for producing output, that content belongs in a workflow; move it.
2. **One Workflow = One Outcome.** A workflow covering two distinct outcomes must be split into two. Every workflow defines validation — a checklist, not a vague success description.
3. **Operational Memory.** Memory is pure facts, schemas, terminology, templates, and technical rules — zero marketing commentary or narrative prose. Not narrative, not justification, not "why we do this."
4. **No Empty Structures.** A folder that would hold exactly one file should be that one file instead (`memory.md`, not `memory/context.md`).
5. **Philosophy Isolation.** Philosophy/branding language never enters an operational file (skill.md, any command, any workflow, any memory file an agent reads to execute a task). If it exists at all, it lives in `memory/philosophy.md`, unreferenced by any operational file — for a human reading the repo, not for the agent executing the skill.
6. **Trigger-Justified Growth.** New files are added only per `growth-rule.md`'s explicit triggers — never for anticipated future need.
7. **Quality Bar & Deterministic Native Tooling.** Deterministic operations (audits, calculations, ratio verifications, AST linting) are encapsulated in executable scripts inside `scripts/` (for project runtime execution) or `tools/` (for skill packaging). Skills must enforce deterministic script-based audits in their `## Validation checklist` rather than relying solely on subjective model self-critiques. Do not script if native toolchains (`tsc`, `node`, `python`, `git`, OS APIs) suffice. No autonomous mass-edit scripts.
8. **Cross-Platform Parity.** 100% identical behavior across Antigravity, Claude Code, Cursor, and Codex.
9. **Platform Compatibility (SKILL.md Frontmatter Constraints).** The YAML frontmatter in `SKILL.md` must comply with all target platform limits and pass strict YAML parsing (`yaml.safe_load()`). `name` is required and must match the skill directory name. `description` is required, must be enclosed in double quotes `description: "..."` whenever it contains colons (`:`), single/double quotes, or special characters, and must not exceed **1024 characters** (Claude Skills hard limit). The `description` should follow the "what + when" pattern: one sentence for what the skill does, one for when to trigger it. Move trigger keyword lists and technical details into the dispatcher body below the frontmatter — every token in `description` is loaded at session start regardless of skill activation. These limits are enforced by `tools/validate_skill.py` and the pre-publish gate. Publishing MUST be blocked if any frontmatter constraint is violated.
10. **Runtime Tooling Manifest Contract (`manifest.json`).** Skills providing runtime-executable scripts in `scripts/` must declare an authoritative `manifest.json` conforming to `skill-manifest.tools.schema.json`. Every tool must specify `"skill_root_anchor": "self"`, entrypoint runtime, typed CLI argument patterns, structured JSON output channels with optional schema references, and be documented in the `SKILL.md` tooling scope. Tools must support dual invocability: direct CLI invocation and centralized MCP execution via `tidyfactor-brain`'s `run_skill_tool`. Skills with no runtime `scripts/` skip this rule.
11. **Memory Freshness.** Every operational memory file must include a `<!-- last-verified: YYYY-MM-DD -->` HTML comment at the top, below the heading. During `audit`, verify that no memory file's last-verified date exceeds 180 days. Stale memory is flagged as a compliance warning (not a hard fail) but must be addressed before the next MINOR or MAJOR release.
12. **Skill vs MCP Boundary.** A capability belongs inside the skill (as a memory/workflow file) when it is: static knowledge, a decision framework, or a template. A capability belongs in an external MCP server when it: calls live APIs, queries databases, or performs stateful actions. If both layers are needed, the skill provides the decision logic and the MCP server provides the execution tools — never duplicate the same logic in both. Document the boundary in `SKILL.md` dispatcher body when a skill has a companion MCP server.
13. **Two-Tier Multi-Language Documentation.** Every skill enforces a distinct separation between Canonical Global Technical Documentation (`README.md` SSOT) and First-Class Market Localizations (`README.ar.md`, `README.fa.md`, `README.es.md`, `README.pt.md`, `README.zh.md`, `README.de.md`, `README.fr.md`). All localized documentation must feature: (a) the universal 8-language switcher bar, (b) the standardized 8-badge suite (including live GitHub Stars), (c) an above-the-fold Manifesto Callout defining the anti-slop value proposition, and (d) an interactive Before & After visual comparison for UI tracks. All localizations must be declared in `package.json["files"]`, staged in `build-skill.js`, and verified by `validate_skill.py`.
14. **Contextual Decision Layer (CDL) & Context Delta Resolution.** Every interactive skill workflow (e.g., `brief`, `init`, `collect`, `configure`) MUST operate under the Contextual Decision Layer contract:
    - **Declarative Decision Gates (`manifest.json`)**: All required decisions, their discovery sources, local persistence paths, and recommended defaults MUST be formally declared under `decision_gates[]` conforming to manifest schema v1.1.0.
    - **Mechanical Context Delta Resolution Formula**: Before prompting the user, the agent must deterministically compute:
      $$\text{Unknowns} = \text{Required Decisions} - (\text{Discovered Facts} \cup \text{Brain KIs})$$
      The agent is STRICTLY FORBIDDEN from asking the user about any fact already present on disk (`brand.json`, `.tidyfactor/*`, project configs) or cached in memory.
    - **Interactive Disclosure & User Agency First**: All genuine $\text{Unknowns}$ resulting from the Delta equation are presented interactively to the user with structured choices (A/B/C/D) and clear recommendations. Zero arbitrary truncation—the user is given full visibility and conversational agency over their project decisions, organized logically by priority.
    - **Zero Robotic Preamble**: Strictly forbid bot persona greetings, self-introductions, lecturing, or textbook dumps.
    - **Local Staleness Tracking**: For file sources marked with `track_staleness: true`, the engine compares file hash/mtime at read time against snapshot values. A changed hash re-opens the decision locally without network or MCP overhead.
    - **Anti-Dual-Write & Fail-Open SSOT Doctrine**: The local workspace file (`.tidyfactor/*-brief.md` or `*.snapshot.json`) is the SOLE Single Source of Truth. Brain/Cloud synchronization is strictly an Outbound Push (`--sync-brain`) executed after local success. Brain MCP lookup must FAIL OPEN silently (0ms latency penalty) if unavailable.


## The Contextual Decision Layer (CDL) Pattern

For skills where execution depends on architectural or strategic choices (e.g. `tidyfactor-design`, `tidyfactor-marketing`, `tidyfactor-doc`, `tidyfactor-styler`, `tidyfactor-next`):
1. **Declarative Decision Manifest (`manifest.json["decision_gates"]`)**: Formally declare each gate's `command`, `decisions[]`, `discovery[]` sources, `persist_to` targets, and `default` values.
2. **Context Delta Resolution Engine**: Automatically evaluate $\text{Unknowns} = \text{Required} - (\text{Discovered} \cup \text{KIs})$ at runtime.
3. **Structured Interactive Dialogue**: Present unresolved decisions with clear, contextual multiple-choice options (A/B/C/D) and highlighted recommendations.
4. **Local Snapshot & Persistence**: Cache confirmed parameters in `.tidyfactor/<skill>-brief.md` and/or `*.snapshot.json` to lock downstream commands silently to the confirmed baseline.
5. **Anti-Dual-Write & Outbound Push**: Treat local files as the sole SSOT. Replicate to Brain KIs only upon explicit user request (`--sync-brain`).
6. **Decision Alignment Axis**: When applicable, include Axis 7 (`D` - Decision Alignment) in Pre-Emit Self-Critiques to verify that generated artifacts strictly adhere to the confirmed brief.

## The Prioritized Rule Catalog Pattern

For skills containing complex guideline libraries, lints, or performance/security standards ($\ge 15$ rules, e.g. `tidyfactor-next`, `tidyfactor-styler`, `cpanel-server-admin`):
1. **Prioritized Impact Ranking**: Categorize rules strictly by quantifiable impact (`CRITICAL` $\to$ `HIGH` $\to$ `MEDIUM` $\to$ `LOW`) with standard domain prefixes (e.g., `async-`, `bundle-`, `server-`, `sec-`).
2. **Standardized Rule Anatomy (`assets/rule-template.md`)**: Every rule must contain: (a) Rule ID, (b) Impact Tier, (c) Problem Rationale, (d) Incorrect Code Snippet (❌), (e) Correct Drop-in Code Snippet (✅), (f) Edge Cases & Constraints.
3. **Separation from General Prose**: Keep the rule catalog strictly in operational memory (`memory/<domain>-rules.md`), loaded only by commands that generate or audit corresponding code/configurations.

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
