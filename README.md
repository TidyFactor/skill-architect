# 🏛️ TidyFactor Skill Architect `v2.1.1`

> **The Canonical Governance Engine & Architecture Specification for AI Coding Agent Skills.**  
> Enforces the **12 Structural Rules** of TidyFactor Skills across **Google Antigravity, Claude Code, Cursor, OpenAI Codex, and Windsurf**.

[![Version](https://img.shields.io/badge/version-2.1.0-blue.svg)](CHANGELOG.md)
[![License](https://img.shields.io/badge/license-Apache--2.0-green.svg)](LICENSE)
[![Ecosystem](https://img.shields.io/badge/ecosystem-TidyFactor-orange.svg)](https://tidyfactor.com)
[![Partner](https://img.shields.io/badge/partner-Alwkala-indigo.svg)](https://alwkala.com)

---

## 📖 Table of Contents

- [Overview & Philosophy](#-overview--philosophy)
- [The Architecture: Progressive Disclosure](#-the-architecture-progressive-disclosure)
- [The 12 Structural Rules of TidyFactor Skills](#-the-12-structural-rules)
- [Commands & Operational Workflows](#-commands--operational-workflows)
- [The Contextual Decision Layer (CDL)](#-the-contextual-decision-layer-cdl)
- [Tooling & Integrity Validation Suite](#-tooling--integrity-validation-suite)
- [Cross-Agent Distribution & Synchronization](#-cross-agent-distribution--synchronization)
- [Installation & Usage](#-installation--usage)
- [License & Credits](#-license--credits)

---

## 🌟 Overview & Philosophy

**`tidyfactor-skill-architect`** is the foundational governance layer that establishes standard operating procedures for creating, auditing, expanding, and packaging AI Coding Agent Skills.

### The Problem It Solves
Traditional AI skills often suffer from:
1. **Context Window Pollution**: Massive, monolithic markdown files that dump thousands of tokens on startup.
2. **Execution Hallucinations**: Prompt ambiguity where the agent attempts to "guess" rather than follow deterministic paths.
3. **Multi-Agent Drift**: Divergent behaviors across different AI coding environments (Antigravity vs. Claude Code vs. Cursor).
4. **Syntax & Frontmatter Failures**: Unquoted strings or malformed YAML breaking IDE autocomplete and discovery indexing.

### The TidyFactor Solution
A skill must behave as a **high-speed deterministic router**, loading only the minimal necessary context at the exact moment it is required.

```
┌─────────────────────────────────────────────────────────────┐
│                 Session Discovery Layer                     │
│        SKILL.md Frontmatter (name + description)            │
└──────────────────────────────┬──────────────────────────────┘
                               │ (Trigger Matched)
                               ▼
┌─────────────────────────────────────────────────────────────┐
│                 Dispatcher Layer (Router)                   │
│          SKILL.md (~350 tokens, Anti-triggers, Scope)       │
└──────────────────────────────┬──────────────────────────────┘
                               │ (Intent Identified)
                               ▼
┌─────────────────────────────────────────────────────────────┐
│                 Command Layer (Router Link)                 │
│              references/commands/<command>.md               │
└──────────────┬───────────────────────────────┬──────────────┘
               │ (Loads Workflow)              │ (Injects Memory)
               ▼                               ▼
┌──────────────────────────────┐ ┌────────────────────────────┐
│        Workflow Layer        │ │        Memory Layer        │
│   Ordered Execution Steps    │ │ Pure Technical Constraints │
│    + Validation Checklist    │ │  Schemas, Patterns, Tables │
└──────────────────────────────┘ └────────────────────────────┘
```

---

## 📐 The 12 Structural Rules

Every skill created, audited, or packaged within the TidyFactor ecosystem strictly adheres to the **12 Structural Rules**:

| # | Rule | Core Mandate | Failure Mode Prevented |
|---|---|---|---|
| **1** | **Dispatcher Discipline** | `SKILL.md` is strictly a router (~350 tokens). Zero in-line instructions. | Token bloat & memory exhaustion at session boot. |
| **2** | **One Workflow = One Outcome** | 1 workflow produces exactly 1 tangible deliverable with a `## Validation checklist`. | Ambiguous multi-tasking and incomplete executions. |
| **3** | **Operational Memory** | Pure technical facts, schemas, and schemas. Zero marketing narrative. | AI hallucinating promotional text into production code. |
| **4** | **No Empty Structures** | Clean, flat file hierarchies. No single-file folders (`memory.md` vs `memory/`). | Deep directory nesting and navigation overhead. |
| **5** | **Philosophy Isolation** | Brand philosophy and rationale live solely in `memory/philosophy.md` (unreferenced). | Agents outputting promotional fluff instead of code. |
| **6** | **Trigger-Justified Growth** | Files are added strictly upon verifiable triggers (Size, Branch, Variant, CDL). | Premature folder explosion and architecture sprawl. |
| **7** | **Quality Bar & Native Tooling** | Deterministic operations encapsulated in `tools/` wrapping native tools (`node`, `python`). | Unreliable LLM regex replacements & flaky bash scripts. |
| **8** | **Cross-Platform Parity & SemVer SSOT** | 100% behavioral parity across all agent platforms; atomic metadata sync. | Agent version drift and silent breaking changes. |
| **9** | **Platform Compatibility & YAML Invariants** | Valid YAML parsing (`yaml.safe_load()`), `description` ≤ 1024 chars, mandatory double quotes `"..."`. | Silent failure in IDE slash (`/`) command autocomplete. |
| **10** | **Tool Permission Declaration** | Explicit declaration of tool languages, mutation abilities, and network scope in `SKILL.md`. | Security blind spots and unprompted file overwrites. |
| **11** | **Memory Freshness** | Required `<!-- last-verified: YYYY-MM-DD -->` marker with $\le 180$ days freshness gate. | Stale API references, deprecated flags, and broken specs. |
| **12** | **Skill vs MCP Boundary** | Static decision logic lives in skills; dynamic APIs & databases delegate to MCP. | Skill bloat and duplicated live-data implementations. |

---

## ⚡ Commands & Operational Workflows

`tidyfactor-skill-architect` exposes 4 core operational commands:

### 1. `init` — Scaffold a New Skill
- **Trigger**: `"Build me a skill for X"` / `"Turn this workflow into a TidyFactor skill"`
- **Loads**: `references/workflows/create-skill.md` + `references/memory/spec.md` + `references/memory/growth-rule.md` + `assets/skill-md-skeleton.md`
- **Output**: Fully scaffolded, compliant skill directory with valid YAML frontmatter, dispatcher `SKILL.md`, and initial workflow.

### 2. `audit` — Audit & Score an Existing Skill
- **Trigger**: `"Audit this skill"` / `"Check if this skill follows TidyFactor rules"`
- **Loads**: `references/workflows/audit-skill.md` + `references/memory/spec.md`
- **Output**: 12-rule compliance scorecard (`Score: X/12`), list of violations, and exact automated file-level remediations.

### 3. `test` — Generate Test Scenarios
- **Trigger**: `"Test this skill"` / `"Generate test scenarios"`
- **Loads**: `references/workflows/test-skill.md` + `references/memory/spec.md`
- **Output**: Populates `tests/scenarios.md` with $\ge 3$ distinct evaluation prompts (happy-path, edge-case, anti-trigger rejection).

### 4. `grow` — Evaluate Architecture Growth
- **Trigger**: `"Should I add a new file/folder to this skill?"`
- **Loads**: `references/memory/growth-rule.md`
- **Output**: Deterministic decision (`SPLIT`, `EXPAND`, or `REJECT`) based on quantitative line count and lifecycle triggers.

---

## 🧠 The Contextual Decision Layer (CDL)

For complex skills where execution depends on interdependent architectural choices (e.g. `tidyfactor-styler`, `tidyfactor-next`), the Skill Architect codifies the **CDL Pattern**:

1. **Thin Arbitration Protocol (`memory/decision-points.md`)**: Defines triggers, boolean skip conditions, and pointers to existing SSOT catalogs.
2. **Pre-flight Brief & Cache (`brief` command / `.tidyfactor/<skill>-brief.md`)**: Gathers decisions once per project, saving them to disk so downstream commands execute silently without asking repetitive questions.
3. **Single-Round Batching & Safe Defaults**: Unresolved ambiguities are batched into 1 single round (max 3 questions). Any overflow defaults to safe conventions.
4. **Decision Alignment Axis**: Evaluates generated code against Axis 7 (`D` - Decision Alignment) during pre-emit self-critique.

---

## 🛠️ Tooling & Integrity Validation Suite

The skill includes a dedicated deterministic verification engine:

```bash
# Run the 11-point automated integrity validator
python tools/validate_skill.py
```

### Automated Validation Matrix
- `[1]` **SemVer Synchronization**: Verifies `package.json`, `.tidyfactor`, `brand.json`, and `CHANGELOG.md` share identical versions.
- `[2]` **License Consistency**: Ensures standard Apache-2.0 license file exists.
- `[3]` **Referenced File Integrity**: Checks that all paths referenced in `SKILL.md` exist on disk.
- `[4]` **Validation Checklists**: Confirms every workflow file contains a `## Validation checklist`.
- `[5]` **Leak Prevention**: Audits for leaked local machine absolute paths.
- `[6]` **Token Budget Gate**: Asserts dispatcher `SKILL.md` is within ~350 token budget (max 500).
- `[7]` **Memory Freshness Gate**: Enforces `<!-- last-verified: YYYY-MM-DD -->` marker within $\le 180$ days.
- `[8]` **Strict YAML Frontmatter Validation**: Executes `yaml.safe_load()` to ensure frontmatter is syntactically valid and `description` is properly quoted and $\le 1024$ chars.
- `[9]` **Tooling Scope Declaration**: Verifies Rule 10 declaration when `tools/` exist.
- `[10]` **Test Scenario Suite**: Asserts `tests/scenarios.md` contains $\ge 3$ test cases.
- `[11]` **MCP Boundary**: Checks that skills interacting with MCP document boundary logic.

---

## 🔄 Cross-Agent Distribution & Synchronization

When packaging or releasing with `node tools/build-skill.js`, the builder automatically compiles the distribution archive and synchronizes across all 5 target environments:

```
Skills-LAB/tidyfactor-skill-architect/ (SSOT)
  ├── 📦 dist/tidyfactor-skill-architect.skill
  ├── 📦 dist/tidyfactor-skill-architect-vX.Y.Z.skill
  ├── 🔁 .agents/skills/tidyfactor-skill-architect/ (Local Agent Wrapper)
  ├── 🔁 ~/.gemini/config/skills/tidyfactor-skill-architect/ (Global Gemini/Antigravity)
  └── 🔁 /mnt/skills/user/tidyfactor-skill-architect/ (Claude / Unix Environment)
```

---

## 📦 Installation & Usage

### 1. Via NPM / NPX
```bash
# Add directly to your active agent workspace
npx @tidyfactor/cli-skill-architect

# Or install globally
npm install -g @tidyfactor/skill-architect
```

### 2. Manual Agent Registration
Clone or copy into your agent's skill root:
```bash
# Google Antigravity & Gemini IDE
cp -r tidyfactor-skill-architect ~/.gemini/config/skills/

# Local Project Agent Wrapper
cp -r tidyfactor-skill-architect .agents/skills/
```

---

## 📄 License & Credits

- **License**: [Apache-2.0](LICENSE)
- **Engineered by**: [TidyFactor Ecosystem](https://tidyfactor.com) & [Alwkala Digital Agency](https://alwkala.com)
- **Contact**: `hello@tidyfactor.com` | `+201016656899`
