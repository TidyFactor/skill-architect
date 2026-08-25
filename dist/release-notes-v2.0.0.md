## 🚀 TidyFactor Skill Architect v2.0.0

### ✨ Highlights
- **12 Structural Rules Evolution**: Expanded governance rubric from 9 to 12 rules (`references/memory/spec.md`):
  - **Rule 10 (Tool Permission Declaration)**: Explicit declaration of tool languages, mutation capabilities, and network scope in `SKILL.md`.
  - **Rule 11 (Memory Freshness Verification)**: Required `<!-- last-verified: YYYY-MM-DD -->` markers with 180-day staleness audit gate.
  - **Rule 12 (Skill vs MCP Boundary)**: Clear architectural boundary separating static prompt/decision workflows from external live MCP servers.
- **New `test` Command & Workflow**: Added `references/commands/test.md` and `references/workflows/test-skill.md` to generate 3+ realistic test scenarios (`tests/scenarios.md`).
- **Enhanced Validation Engine**: Updated `tools/validate_skill.py` with numeric token estimation (~350 token budget), memory freshness checks, and frontmatter length limits.
- **Rule 9 Optimization**: Frontmatter description standard optimized to "what + when" pattern to minimize discovery-layer token footprint.
- **Cascade Update Protocol**: Codified atomic synchronization rules across all markdown references when structural rules change.

### 📦 Installation

**NPM (Recommended):**
```bash
npx @alwkala/tidyfactor-skill-architect add-skill
```

**Manual Download:**
Download `tidyfactor-skill-architect.skill` from this release.

### 🤖 Supported AI Agents
- Google Antigravity IDE
- Claude Code / Cursor / Windsurf / Codex
- Any AGENTS.md-compliant coding agent
