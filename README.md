# TidyFactor Skill Architect v2.0.0

> **Governance Layer & Skill Methodology Engine for AI Coding Agents**  
> Enforces the 12 Structural Rules of TidyFactor Skills across Google Antigravity, Claude Code, Cursor, Codex, and Windsurf.

---

## 🏛️ Overview

`tidyfactor-skill-architect` is the master governance layer governing how skills are built, refactored, audited, and expanded across the TidyFactor Ecosystem. It ensures skills remain lightweight token-friendly routers rather than bloated prompt dumps.

---

## ⚡ Quick Start & Commands

| Command | Intent | Description |
|---|---|---|
| `init` | "Build me a skill for X" | Scaffolds a new TidyFactor skill with dispatcher `SKILL.md` (~350 tokens) and minimal file layout. |
| `audit` | "Audit this skill" | Evaluates an existing skill against 12 compliance rules and generates concrete file-level fixes. |
| `test` | "Test this skill" | Generates 3+ realistic test scenarios (happy-path, edge-case, negative) in `tests/scenarios.md`. |
| `grow` | "Should I add a file?" | Evaluates proposed expansion against size, branch, and variant growth triggers. |

---

## 📐 The 12 Structural Rules

1. **Dispatcher Discipline**: `SKILL.md` is a router (~350 tokens), declaring commands without doing task execution.
2. **One Workflow = One Outcome**: Every workflow has a single deliverable with an explicit `Validation checklist`.
3. **Operational Memory**: Pure facts, schemas, and technical rules — zero marketing commentary or narrative prose.
4. **No Empty Structures**: Clean, flattened architecture without single-file folders.
5. **Philosophy Isolation**: Technical execution separated from brand philosophy (`memory/philosophy.md` only).
6. **Trigger-Justified Growth**: Files added only when explicit size, branch, or variant triggers are met.
7. **Quality Bar & Native Tooling**: Deterministic operations encapsulated in `tools/` using native toolchains (`node`, `python`).
8. **Cross-Platform Parity & SemVer SSOT**: 100% identical behavior across AI environments, versioned via `CHANGELOG.md`.
9. **Platform Compatibility**: `SKILL.md` YAML frontmatter must comply with platform limits (`description` ≤ 1024 chars, "what + when" pattern).
10. **Tool Permission Declaration**: Skills executing code via `tools/` must declare tooling scope (languages, mutations, network) in `SKILL.md`.
11. **Memory Freshness**: Operational memory files must include `<!-- last-verified: YYYY-MM-DD -->` comments (verified within 180 days).
12. **Skill vs MCP Boundary**: Static knowledge and decisions stay in skills; live APIs, databases, and stateful actions belong in external MCP servers.

---

## 🛠️ Tooling

```bash
# Validate skill structural compliance
npm run validate

# Package distribution archive (.skill) & auto-sync across locations
npm run build
```

---

## 📄 License

Licensed under the Apache-2.0 License. Powered by TidyFactor & Alwkala Digital Agency.
