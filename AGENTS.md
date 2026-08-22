# AGENTS.md — TidyFactor Skill Architect Rules

This skill is the Single Source of Truth for TidyFactor Skill Governance.

## Key Rules
1. Maintain SSOT at `c:\wamp64\www\TidyFactor\Skills\Skills-LAB\tidyfactor-skill-architect\`.
2. Any changes must trigger a version bump in `package.json`, `.tidyfactor`, `brand.json`, `README.md`, `README.ar.md`, and an entry in `CHANGELOG.md`.
3. Auto-sync release build outputs using `npm run build`.
