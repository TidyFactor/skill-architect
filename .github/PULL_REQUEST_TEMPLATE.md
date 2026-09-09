## 🏛️ Summary & Context

[Describe the problem, proposed architectural change, or capability expansion.]

---

## 📋 TidyFactor Methodology Checklist

- [ ] **Dispatcher Discipline (Rule 1)**: `SKILL.md` routes without in-line task execution.
- [ ] **One Workflow = One Outcome (Rule 2)**: Every workflow has a single outcome and ends with `## Validation checklist`.
- [ ] **Operational Memory (Rule 3)**: Pure technical patterns, schemas, and facts—zero marketing narrative.
- [ ] **No Empty Structures (Rule 4)**: Clean flattened folder hierarchy.
- [ ] **Philosophy Isolation (Rule 5)**: No philosophy language in operational files.
- [ ] **Trigger-Justified Growth (Rule 6)**: Changes map strictly to size, branch, or variant triggers.
- [ ] **Quality Bar & Tooling (Rule 7)**: Deterministic checks encapsulated in `tools/` or `scripts/`.
- [ ] **Cross-Platform Parity (Rule 8)**: Parity across Antigravity, Claude Code, Cursor, and Codex.
- [ ] **Memory Freshness (Rule 11)**: `<!-- last-verified: YYYY-MM-DD -->` comments present and ≤ 180 days.
- [ ] **Atomic SemVer Sync (Rule 2)**: Version bumped and synced across metadata files and `CHANGELOG.md`.

---

## 🧪 Verification & Results

- [ ] Ran `python tools/validate_skill.py` (100% pass).
- [ ] Built `.skill` bundle with `node tools/build-skill.js`.
- [ ] Zero machine-specific absolute file paths (`file:///C:`).
