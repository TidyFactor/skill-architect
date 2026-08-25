# CHANGELOG — TidyFactor Skill Architect

All notable changes to `tidyfactor-skill-architect` will be documented in this file.

The format is based on [Keep a CHANGELOG](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

---

## [2.0.0] - 2026-08-25

### Added
- **12 Structural Rules Evolution**: Expanded canonical spec from 9 to 12 rules (`references/memory/spec.md`):
  - **Rule 10 (Tool Permission Declaration)**: Explicit declaration of tool languages, mutation capabilities, and network scope in `SKILL.md`.
  - **Rule 11 (Memory Freshness Verification)**: Required `<!-- last-verified: YYYY-MM-DD -->` markers with 180-day staleness audit gate.
  - **Rule 12 (Skill vs MCP Boundary)**: Clear architectural boundary separating static prompt/decision workflows from external live MCP servers.
- **New `test` Command & Workflow**: Added `references/commands/test.md` and `references/workflows/test-skill.md` to generate 3+ realistic test scenarios (`tests/scenarios.md`).
- **Enhanced Validation Engine**: Updated `tools/validate_skill.py` with numeric token estimation (~350 token budget), memory freshness checks, and frontmatter length limits.
- **Cascade Update Protocol**: Codified atomic synchronization rules across all markdown references when structural rules change.

### Changed
- **Rule 9 Optimization**: Refined frontmatter description standard to "what + when" pattern to minimize discovery-layer token footprint.
- **Audit Workflow**: Upgraded `audit-skill.md` scoring to 12-rule rubric (X/12).
- **Template Update**: Updated `assets/skill-md-skeleton.md` with Tooling Scope section.

---

## [1.1.1] - 2026-08-25

### Fixed
- **CLI Executable & NPX Packaging**: Added standard `"add-skill": "bin/add-skill.js"` mapping in `package.json` to ensure unified `npx @alwkala/tidyfactor-skill-architect add-skill` execution.
- **Workflow Compliance**: Standardized header in `references/workflows/audit-skill.md` to `## Validation checklist`.

---

## [1.1.0] - 2026-08-22

### Added
- **Context Budgeting & Token Economy Layer**: Added `references/memory/context-budget.md` defining strict component token boundaries (~350 tokens dispatcher, ~150 lines workflows/commands, ~300 lines memory) and 3-tier context injection rules (Required, Optional, Forbidden).
- **Anti-Triggers / Negative Triggers**: Added explicit negative triggers in `SKILL.md` frontmatter `description` to prevent non-structural prompt engineering task misdirection.
- **5-Way Multi-Environment Synchronization**: Added support in `tools/build-skill.js` and `AGENTS.md` for Claude/Unix agent environment (`/mnt/skills/user/<skill-name>/`).
- **Draft Mode vs. Release Mode Lifecycle**: Codified two-tier governance in `AGENTS.md` for frictionless local development vs strict release hygiene.
- **Expanded 8-Rule Audit Workflow**: Updated `audit-skill.md` to evaluate compliance on full 8/8 rules, context budget health, and ecosystem scope overlap / collision checks.

### Changed
- **Dispatcher Trim**: Refactored `SKILL.md` into a lean ~350 token pure router, relocating inline rule constraints to `references/memory/spec.md`.
- **Behavioral Parity Standard**: Updated Rule 8 from "100% identical behavior" to "Behavioral Parity across Antigravity, Claude Code, Cursor, and Codex".

---

## [1.0.0] - 2026-08-22

### Added
- **Official SSOT Skill Scaffolding**: Promoted `tidyfactor-skill-architect` into a first-class SSOT skill inside `tidyfactor-skill-architect/`.
- **Command Router**:
  - `init`: Scaffolds a new skill following the 8 structural rules & dispatcher pattern.
  - `audit`: Audits any existing skill against structural compliance checklist.
  - `grow`: Evaluates file splitting & expansion against three explicit growth triggers.
- **Workflows & Operational Memory**:
  - `create-skill.md` & `audit-skill.md` workflows.
  - `spec.md`, `growth-rule.md`, `philosophy.md`, `terminology.md` memory files.
  - `skill-md-skeleton.md` asset template.
- **Native Tooling & Distribution**:
  - CLI binary runner `bin/add-skill.js`.
  - Packaging script `tools/build-skill.js` supporting cross-platform zipping and automatic multi-location sync.
  - Structural validator `tools/validate_skill.py`.
- **Atomic Multi-Location Synchronization**:
  - SSOT Workspace: `Skills-LAB/tidyfactor-skill-architect/`
  - Agent Wrapper: `.agents/skills/tidyfactor-skill-architect/`
  - Global Config: `~/.gemini/config/skills/tidyfactor-skill-architect/`
  - Packaged Archives: `tidyfactor-skill-architect-v1.0.0.skill` and `tidyfactor-skill-architect.skill` in root and `dist/`.
