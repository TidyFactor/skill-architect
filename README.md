# 🏛️ TidyFactor Skill Architect `v2.7.1`

<div align="center">

[ English ](README.md) • [ العربية ](README.ar.md) • [ Español ](README.es.md) • [ Français ](README.fr.md) • [ Deutsch ](README.de.md) • [ Português ](README.pt.md) • [ 简体中文 ](README.zh.md) • [ فارسی ](README.fa.md)

<br/>

[![Version](https://img.shields.io/badge/version-2.7.1-blue.svg)](CHANGELOG.md)
[![License](https://img.shields.io/badge/license-Apache--2.0-green.svg)](LICENSE)
[![CI](https://github.com/TidyFactor/skill-architect/actions/workflows/ci.yml/badge.svg)](https://github.com/TidyFactor/skill-architect/actions/workflows/ci.yml)
[![Integrity Score](https://img.shields.io/badge/integrity-100%25%20Pass-brightgreen.svg)](#-tooling--integrity-validation-suite)
[![Ecosystem](https://img.shields.io/badge/ecosystem-TidyFactor-orange.svg)](https://tidyfactor.com)
[![Partner](https://img.shields.io/badge/partner-Alwkala-indigo.svg)](https://alwkala.com)

</div>

> **The Canonical Governance Engine & Architecture Specification for AI Coding Agent Skills.**  
> Enforces the **15 Structural Rules** and the **Universal 6-Axis Periodic Review Protocol** of TidyFactor Skills across **Google Antigravity, Claude Code, Cursor, OpenAI Codex, and Windsurf**.

---

## ⚡ Quick Start (Above the Fold)

Install and register `tidyfactor-skill-architect` into your active coding environment in seconds:

```bash
# Option A: Install via official TidyFactor Ecosystem CLI (Recommended)
npx @tidyfactor/cli add skill-architect

# Option B: Install via Open Agent Skills multi-agent standard (skills.sh)
npx skills add tidyfactor/skill-architect

# Option C: Direct standalone runner (zero global dependencies)
npx @tidyfactor/skill-architect@latest
```

---

## 📖 Table of Contents

- [Overview & Philosophy](#-overview--philosophy)
  - [The Problem It Solves](#the-problem-it-solves)
  - [The TidyFactor Solution](#the-tidyfactor-solution)
  - [Progressive Disclosure Architecture](#progressive-disclosure-architecture)
- [Commands & Operational Workflows](#-commands--operational-workflows)
  - [Summary of Commands](#summary-of-commands)
  - [1. `init` — Scaffold a New Skill](#1-init--scaffold-a-new-skill)
  - [2. `audit` — Audit & Score an Existing Skill](#2-audit--audit--score-an-existing-skill)
  - [3. `review` — Universal 6-Axis Periodic Review Protocol](#3-review--universal-6-axis-periodic-skill-review-protocol)
  - [4. `test` — Generate Test Scenarios](#4-test--generate-test-scenarios)
  - [5. `grow` — Evaluate Architecture Growth](#5-grow--evaluate-architecture-growth)
- [Universal 6-Axis Periodic Skill Review Protocol](#-universal-6-axis-periodic-skill-review-protocol)
  - [The 6 Core Evaluation Axes](#the-6-core-evaluation-axes)
  - [100-Point Audit Rubric & Grading Thresholds](#100-point-audit-rubric--grading-thresholds)
- [The 15 Structural Rules of TidyFactor Skills](#-the-15-structural-rules)
- [The Contextual Decision Layer (CDL v2.0)](#-the-contextual-decision-layer-cdl-v20)
  - [4-Phase Arbitration Pattern](#4-phase-arbitration-pattern)
  - [Execution Modes: Mode A (Modal Wizard) vs Mode B (Debate Mode)](#execution-modes-mode-a-vs-mode-b)
- [Tooling & Integrity Validation Suite](#-tooling--integrity-validation-suite)
  - [13-Point Automated Validation Matrix](#13-point-automated-validation-matrix)
- [Cross-Agent Distribution & Synchronization](#-cross-agent-distribution--synchronization)
- [Installation & Detailed Guide](#-installation--detailed-guide)
  - [CLI & Package Options](#cli--package-options)
  - [Manual Agent Registration](#manual-agent-registration)
- [License & Credits](#-license--credits)

---

## 🌟 Overview & Philosophy

**`tidyfactor-skill-architect`** is the foundational governance layer that establishes standard operating procedures for creating, auditing, expanding, packaging, and maintaining AI Coding Agent Skills across diverse developer ecosystems.

### The Problem It Solves

Traditional AI coding skills frequently degrade due to four systemic anti-patterns:
1. **Context Window Pollution**: Giant monolithic prompt files dump thousands of tokens into the context window upon session boot, degrading reasoning depth.
2. **Execution Hallucinations**: Ambiguous instructional text causes models to "guess" parameters instead of traversing deterministic, schema-validated execution graphs.
3. **Multi-Agent Behavioral Drift**: Divergent behaviors between Antigravity, Claude Code, Cursor, Codex, and Windsurf due to vendor-specific lock-in.
4. **Syntax & Frontmatter Failures**: Unquoted strings or invalid YAML frontmatter silently break IDE autocomplete and slash (`/`) command discovery.

### The TidyFactor Solution

A TidyFactor skill is engineered not as an instructional prompt, but as a **high-speed deterministic router** that applies **Progressive Disclosure**: loading only the minimal necessary context at the exact moment it is required.

### Progressive Disclosure Architecture

```
┌─────────────────────────────────────────────────────────────────────────┐
│                      Session Discovery Layer                            │
│           SKILL.md Frontmatter (name + description ≤ 1024 chars)        │
└────────────────────────────────────┬────────────────────────────────────┘
                                     │ (Trigger Matched)
                                     ▼
┌─────────────────────────────────────────────────────────────────────────┐
│                      Dispatcher Layer (Router)                          │
│            SKILL.md (~350 tokens, Anti-triggers, Tool Scope)            │
└────────────────────────────────────┬────────────────────────────────────┘
                                     │ (Intent Identified)
                                     ▼
┌─────────────────────────────────────────────────────────────────────────┐
│                     Command Layer (Router Link)                         │
│                  references/commands/<command>.md                       │
└──────────────────┬───────────────────────────────────┬──────────────────┘
                   │ (Loads Workflow)                  │ (Injects Memory)
                   ▼                                   ▼
┌─────────────────────────────────────┐ ┌─────────────────────────────────┐
│           Workflow Layer            │ │          Memory Layer           │
│       Ordered Execution Steps       │ │   Pure Technical Constraints    │
│       + Validation Checklist        │ │   Schemas, Rules, Data Tables   │
└─────────────────────────────────────┘ └─────────────────────────────────┘
```

---

## ⚡ Commands & Operational Workflows

### Summary of Commands

| Command | Category | Trigger Prompt Examples | What It Loads | Output Deliverable |
|---|---|---|---|---|
| **`init`** | Scaffolding | `"Build me a skill for X"`, `"Scaffold new skill"` | `create-skill.md` + `spec.md` + `growth-rule.md` | Fully compliant skill scaffold with valid YAML frontmatter |
| **`audit`** | Governance | `"Audit this skill"`, `"Check TidyFactor rules"` | `audit-skill.md` + `spec.md` | 15-Rule compliance scorecard & exact code remediations |
| **`review`** | Periodic Lifecycle | `"Review this skill"`, `"/review"` | `periodic-review.md` + `periodic-review-matrix.md` | 100-Point 6-Axis Audit Scorecard with Pass/Warn/Fail rubric |
| **`test`** | Quality Assurance | `"Test this skill"`, `"Generate scenarios"` | `test-skill.md` + `spec.md` | Populates `tests/scenarios.md` with $\ge 3$ deterministic test cases |
| **`grow`** | Architecture | `"Should I add a file?"`, `"Evaluate skill growth"` | `growth-rule.md` | Deterministic decision (`SPLIT`, `EXPAND`, or `REJECT`) |

---

### 1. `init` — Scaffold a New Skill
- **User Intent**: Create a new production-ready AI skill from scratch following TidyFactor invariants.
- **Workflow Loaded**: `references/workflows/create-skill.md` + `references/memory/spec.md` + `references/memory/growth-rule.md` + `assets/skill-md-skeleton.md`.
- **Delivered Output**: Complete directory scaffold, compliant `SKILL.md` dispatcher (~350 tokens), first workflow with a `## Validation checklist`, and metadata files (`package.json`, `.tidyfactor`, `brand.yaml`).

### 2. `audit` — Audit & Score an Existing Skill
- **User Intent**: Verify an existing skill's structural integrity against the 15 Structural Rules.
- **Workflow Loaded**: `references/workflows/audit-skill.md` + `references/memory/spec.md`.
- **Delivered Output**: Quantitative compliance scorecard (`Score: X/15`), enumerated rule violations, and mechanical file-level diffs.

### 3. `review` — Universal 6-Axis Periodic Skill Review Protocol
- **User Intent**: Conduct scheduled quarterly or pre-release maintenance reviews across all 6 engineering dimensions.
- **Workflow Loaded**: `references/workflows/periodic-review.md` + `references/memory/periodic-review-matrix.md`.
- **Delivered Output**: Standardized 100-point 6-Axis scorecard, orphan asset purge, stale date refresh, and deduplication report.

### 4. `test` — Generate Test Scenarios
- **User Intent**: Generate black-box evaluation prompts to validate skill triggering, execution paths, and negative-case rejection.
- **Workflow Loaded**: `references/workflows/test-skill.md` + `references/memory/spec.md`.
- **Delivered Output**: Minimum 3 test cases added to `tests/scenarios.md` covering Happy Path, Complex/Edge Case, and Anti-Trigger Rejection.

### 5. `grow` — Evaluate Architecture Growth
- **User Intent**: Decide whether new capabilities warrant adding files, splitting workflows, or creating a separate skill.
- **Workflow Loaded**: `references/memory/growth-rule.md`.
- **Delivered Output**: Mathematical evaluation based on line counts ($\ge 400$ lines), branch variants, and contextual triggers (`SPLIT`, `EXPAND`, or `REJECT`).

---

## 🏛️ Universal 6-Axis Periodic Skill Review Protocol

Introduced in **v2.7.0**, the **6-Axis Periodic Skill Review Protocol** provides a repeatable, objective maintenance engine to prevent architectural rot, stale knowledge, and asset bloat over time.

### The 6 Core Evaluation Axes

```
   ┌────────────────────────────────────────────────────────┐
   │       Universal 6-Axis Periodic Review Engine          │
   └───────┬────────────┬────────────┬────────────┬─────────┘
           │            │            │            │
    ┌──────▼─────┐┌─────▼──────┐┌────▼───────┐┌───▼────────┐
    │   Axis 1   ││   Axis 2   ││   Axis 3   ││   Axis 4   │
    │  Commands  ││  Workflows ││   Memory   ││   Tooling  │
    └────────────┘└────────────┘└────────────┘└────────────┘
                        │                     │
                 ┌──────▼──────┐       ┌──────▼──────┐
                 │   Axis 5    │       │   Axis 6    │
                 │ Governance  │       │ Asset Clean │
                 └─────────────┘       └─────────────┘
```

1. **Axis 1: Commands & Context-Aware Prompts (20 pts)**
   - Manifest synchronization between `SKILL.md` table and `references/commands/`.
   - Single-router dispatch discipline; zero multi-command sprawl.
2. **Axis 2: Workflows & Single Outcome Checklists (20 pts)**
   - Exactly one tangible outcome per workflow file.
   - Mandatory, non-empty `## Validation checklist` concluding every workflow.
3. **Axis 3: Operational Memory Purity & YAML Primacy (15 pts)**
   - Zero marketing copy, fluff, or ideological text inside memory files.
   - Rule 15 YAML Primacy (`brand.yaml`, briefs) for 35–50% token reduction.
   - Active freshness timestamps (`<!-- last-verified: YYYY-MM-DD -->` $\le 180$ days).
4. **Axis 4: Tooling, AST Scrapers & Protocol Integration (15 pts)**
   - Zero Runtime Crash guarantee via deterministic Node/Python scripts in `tools/`.
   - Safe MCP boundary declarations with fail-open fallback logic.
5. **Axis 5: Governance, Markdown Linting & Tone of Voice (15 pts)**
   - Atomic SemVer synchronization across all metadata files.
   - Single Source of Truth adherence and secret scanning passes.
   - Direct, technical tone free of conversational bot preambles.
6. **Axis 6: Assets & Folder Structure Hygiene (15 pts)**
   - SHA-256 duplicate image and media elimination.
   - Zero orphaned or unreferenced assets in `assets/`.
   - WebP format optimization for web previews.

### 100-Point Audit Rubric & Grading Thresholds

| Grade | Score Range | Status | Action Required |
|---|---|---|---|
| **Grade A** | **90 – 100** | ✅ **Production Ready** | Certified for immediate release and cross-agent synchronization. |
| **Grade B** | **75 – 89** | ⚠️ **Warning** | Minor hygiene or freshness remediation needed before major releases. |
| **Grade C** | **< 75** | ❌ **Failed Quality Bar** | Blocking release. Must apply mechanical remediation formulas immediately. |

---

## 📐 The 15 Structural Rules

Every skill in the TidyFactor ecosystem strictly complies with the **15 Structural Rules**:

| # | Rule Name | Core Mandate | Failure Mode Prevented |
|---|---|---|---|
| **1** | **Dispatcher Discipline** | `SKILL.md` is strictly a router (~350 tokens). Zero inline instructions. | Token bloat & memory exhaustion at session boot. |
| **2** | **One Workflow = One Outcome** | 1 workflow produces exactly 1 tangible deliverable with a `## Validation checklist`. | Ambiguous multi-tasking and incomplete executions. |
| **3** | **Operational Memory** | Pure technical facts, schemas, and tables. Zero marketing narrative. | AI hallucinating promotional text into production code. |
| **4** | **No Empty Structures** | Clean, flat file hierarchies. No single-file folders (`memory.md` vs `memory/`). | Deep directory nesting and navigation overhead. |
| **5** | **Philosophy Isolation** | Brand philosophy and rationale live solely in `memory/philosophy.md` (unreferenced). | Agents outputting promotional fluff instead of code. |
| **6** | **Trigger-Justified Growth** | Files are added strictly upon verifiable triggers (Size, Branch, Variant, CDL). | Premature folder explosion and architecture sprawl. |
| **7** | **Quality Bar & Native Tooling** | Deterministic operations encapsulated in `tools/` wrapping native tools (`node`, `python`). | Unreliable LLM regex replacements & flaky bash scripts. |
| **8** | **Cross-Platform Parity & SemVer SSOT** | 100% behavioral parity across all agent platforms; atomic metadata sync. | Agent version drift and silent breaking changes. |
| **9** | **Platform Compatibility & YAML Invariants** | Valid YAML parsing (`yaml.safe_load()`), `description` ≤ 1024 chars, mandatory double quotes `"..."`. | Silent failure in IDE slash (`/`) command autocomplete. |
| **10** | **Tool Permission Declaration** | Explicit declaration of tool languages, mutation abilities, and network scope in `SKILL.md`. | Security blind spots and unprompted file overwrites. |
| **11** | **Memory Freshness** | Required `<!-- last-verified: YYYY-MM-DD -->` marker with $\le 180$ days freshness gate. | Stale API references, deprecated flags, and broken specs. |
| **12** | **Skill vs MCP Boundary** | Static decision logic lives in skills; dynamic APIs & databases delegate to MCP. | Skill bloat and duplicated live-data implementations. |
| **13** | **Two-Tier Multi-Language Documentation** | Distinct separation between Canonical Global Docs (`README.md`) and 7 First-Class Market Localizations with 8-language switcher. | Linguistic slop, translation debt, and secondary market fragmentation. |
| **14** | **Contextual Decision Layer (CDL v2.0)** | Evaluates $\text{Unknowns} = \text{Required} - (\text{Discovered} \cup \text{KIs})$, scans workspace first, invokes native interactive modal wizards (`ask_question`), and supports Debate Mode. | Redundant user grilling, robotic greetings, and dual-write state drift. |
| **15** | **Token Efficiency & YAML Primacy** | Prioritizes YAML (`brand.yaml`, briefs, memory) for 35–50% context savings; reserves JSON for machine wire contracts with dual-engine fallback. | Context window exhaustion, JSON syntax noise, and trailing comma errors. |

---

## 🧠 The Contextual Decision Layer (CDL v2.0)

For complex skills where execution depends on interdependent architectural choices, the Skill Architect codifies the **CDL Pattern**:

### 4-Phase Arbitration Pattern

1. **Active Context Synthesis**: Scans workspace files (e.g. `package.json`, `composer.json`, existing configs) and persistent Knowledge Items (KIs) to identify already settled decisions.
2. **Pre-flight Brief & Local Cache (`brief` command)**: Gathers missing parameters and persists them to `.tidyfactor/<skill>-brief.md` as the local Single Source of Truth.
3. **Single-Round Interactive Arbitration**:
   - **Mode A (Smart Modal Wizard)**: Never outputs questionnaires as plain chat text. Invokes the IDE's native interactive modal tool (`ask_question`) in 1 structured round (max 3 questions).
   - **Mode B (Debate Mode)**: Evaluates complex trade-offs with architectural recommendations before final code emission.
4. **Decision Alignment Axis (`D`)**: Evaluates generated code against Axis 7 (`D` - Decision Alignment) during pre-emit self-critique (`/* Pre-emit critique: P5 H5 E5 S5 R5 V5 D5 */`).

---

## 🛠️ Tooling & Integrity Validation Suite

The skill includes a deterministic verification engine that ensures strict compliance before release:

```bash
# Run the 13-point automated integrity validator
python tools/validate_skill.py
```

### 13-Point Automated Validation Matrix

| # | Checkpoint | Target Verification | Verification Tool / Logic |
|---|---|---|---|
| **1** | **SemVer Synchronization** | `package.json`, `.tidyfactor`, `brand.yaml`, and `CHANGELOG.md` share identical versions. | Regex & JSON/YAML parser |
| **2** | **License Consistency** | Canonical `LICENSE` file exists and declares Apache-2.0. | File existence & header scan |
| **3** | **Referenced File Integrity** | Every file path referenced in `SKILL.md` physically exists on disk. | Filesystem link auditor |
| **4** | **Validation Checklists** | Every workflow file ends with a non-empty `## Validation checklist`. | Heading & token scanner |
| **5** | **Absolute Path Leak Prevention** | Zero machine-specific local paths (e.g., `C:\`, `/Users/`) leaked. | Path leak regex detector |
| **6** | **Token Budget Gate** | Dispatcher `SKILL.md` remains within ~350 token budget (max 500 tokens). | Word count & token estimator |
| **7** | **Memory Freshness Gate** | All memory files contain `<!-- last-verified: YYYY-MM-DD -->` $\le 180$ days. | Date delta math check |
| **8** | **Strict YAML Syntax** | Executes `yaml.safe_load()` to ensure syntax validity; description $\le 1024$ chars. | Python PyYAML safe loader |
| **9** | **Tooling Scope Declaration** | Verifies Rule 10 permission block exists when `tools/` directory is present. | Frontmatter scope auditor |
| **10** | **Test Scenario Suite** | Asserts `tests/scenarios.md` contains $\ge 3$ distinct evaluation test cases. | Markdown scenario parser |
| **11** | **MCP Boundary Audit** | Asserts fail-open fallback boundaries are documented for external APIs. | MCP architecture checker |
| **12** | **CDL Gate Compliance** | Verifies `manifest.json` decision gates conform to CDL v1.1.0/v2.0 schema. | JSON Schema validator |
| **13** | **YAML Primacy (Rule 15)** | Enforces cognitive layers (`brand.yaml`) use YAML and wire contracts use JSON. | Dual-format validator |

---

## 🔄 Cross-Agent Distribution & Synchronization

When compiling with `node tools/build-skill.js`, the builder automatically packages the distribution bundle and synchronizes across all registered target environments:

```
Skills-LAB/tidyfactor-skill-architect/ (Single Source of Truth - SSOT)
  ├── 📦 dist/tidyfactor-skill-architect.skill (Latest Claude Archive)
  ├── 📦 dist/tidyfactor-skill-architect-v2.7.1.skill (Versioned Archive)
  ├── 🔁 .agents/skills/tidyfactor-skill-architect/ (Local Workspace Agent)
  ├── 🔁 ~/.gemini/config/skills/tidyfactor-skill-architect/ (Global Antigravity / Gemini)
  └── 🔁 /mnt/skills/user/tidyfactor-skill-architect/ (Claude / Unix Runtime)
```

---

## 🚀 Installation & Detailed Guide

### CLI & Package Options

Choose your preferred installation method:

#### Option A: Via TidyFactor Ecosystem CLI (Recommended)
Install directly into your active workspace using the official CLI:
```bash
npx @tidyfactor/cli add skill-architect
```
*Or if you have the CLI installed globally (`npm i -g @tidyfactor/cli`):*
```bash
tidyfactor add skill-architect
```

#### Option B: Via Open Agent Skills Ecosystem (skills.sh / Vercel Labs)
Install using the universal multi-agent standard across Cursor, Antigravity, Claude Code, Windsurf, Trae, and Codex:
```bash
npx skills add tidyfactor/skill-architect
```

#### Option C: Standalone Zero-Dependency Runner (NPM Direct)
Run the dedicated skill installer directly with automatic cache invalidation:
```bash
npx @tidyfactor/skill-architect@latest
```

### Manual Agent Registration

You can also manually clone or copy the skill directory into your agent's customization root:

```bash
# Google Antigravity & Gemini IDE (Global Customization Root)
cp -r tidyfactor-skill-architect ~/.gemini/config/skills/

# Local Project Agent Wrapper (Workspace Root)
cp -r tidyfactor-skill-architect .agents/skills/
```

---

## 📄 License & Credits

- **License**: [Apache-2.0](LICENSE)
- **Engineered by**: [TidyFactor Ecosystem](https://tidyfactor.com) & [Alwkala Digital Agency](https://alwkala.com)
- **Official Inquiries**: `hello@tidyfactor.com` | `+201016656899`
- **Location**: Cairo, Egypt
