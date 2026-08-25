## 🚀 TidyFactor Skill Architect v2.0.1

### ✨ What's Changed
- **Automated Validation Checks [9-11]**: Expanded `tools/validate_skill.py` to programmatically enforce:
  - **Check [9]**: Tooling Scope declaration (Rule 10) in `SKILL.md` when executable scripts exist in `tools/`.
  - **Check [10]**: Test scenario existence and count ($\ge 3$) in `tests/scenarios.md`.
  - **Check [11]**: Skill vs MCP boundary documentation (Rule 12).
- **CDL Growth Trigger (Trigger 4)**: Codified exact quantitative criteria in `references/memory/growth-rule.md` for when a skill qualifies to adopt the Contextual Decision Layer ($\ge 3$ interdependent architectural choices, cross-turn cache requirement, and Axis 7 decision alignment).

### 📦 Installation

**NPM:**
```bash
npx @alwkala/tidyfactor-skill-architect add-skill
```

**Download:**
Download `tidyfactor-skill-architect-v2.0.1.skill` from this release.
