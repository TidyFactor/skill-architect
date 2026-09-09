# Contributing to TidyFactor Skill Architect

Thank you for contributing to the governance layer of TidyFactor AI Agent Skills!

## Core Governance Rules

All modifications to this repository must satisfy the non-negotiable rules codified in `references/memory/spec.md`:

1. **Dispatcher Discipline (Rule 1)**: Keep `SKILL.md` strictly as a lightweight router (~350 tokens).
2. **One Workflow = One Outcome (Rule 2)**: Every workflow must produce a single, distinct deliverable with an explicit `## Validation checklist`.
3. **Operational Memory (Rule 3)**: Pure technical patterns and schemas—zero marketing commentary.
4. **No Empty Structures (Rule 4)**: No single-file directories.
5. **Quality Bar & Tooling (Rule 7)**: Deterministic checks encapsulated in `tools/` or `scripts/`.
6. **Cross-Platform Parity (Rule 8)**: Parity across Antigravity, Claude Code, Cursor, and Codex.
7. **SemVer Synchronization (Rule 2)**: Atomic updates across `package.json`, `.tidyfactor`, `brand.yaml`, `brand.json`, `README.md`, `README.ar.md`, and `CHANGELOG.md`.

## Local Validation Workflow

Before submitting a Pull Request:

1. Validate skill integrity:
   ```bash
   python tools/validate_skill.py
   ```
2. Build distribution archives:
   ```bash
   node tools/build-skill.js
   ```
3. Ensure zero uncommitted drift or machine-specific absolute file paths (`file:///C:`).
