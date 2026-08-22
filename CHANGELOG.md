# CHANGELOG — TidyFactor Skill Architect

All notable changes to `tidyfactor-skill-architect` will be documented in this file.

The format is based on [Keep a CHANGELOG](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

---

## [1.0.0] - 2026-08-22

### Added
- **Official SSOT Skill Scaffolding**: Promoted `tidyfactor-skill-architect` into a first-class SSOT skill inside `c:\wamp64\www\TidyFactor\Skills\Skills-LAB\tidyfactor-skill-architect\`.
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
