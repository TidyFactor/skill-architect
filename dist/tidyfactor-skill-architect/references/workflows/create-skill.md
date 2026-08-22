# Workflow: create-skill

One outcome: a new skill folder that is compliant with `memory/spec.md`, `memory/context-budget.md`, and validates cleanly.

---

## Steps

1. **Capture Intent & Define Triggers / Anti-Triggers**:
   - Define exact user triggers and positive activation phrases.
   - Define explicit negative triggers (anti-triggers) stating what the skill does NOT handle.
   - Clarify the single domain outcome.

2. **Decide Minimal File Count & Context Budget**:
   - Default is 4 flat files: `SKILL.md`, `references/commands.md`, `references/workflows.md`, `references/memory.md` (no subfolders).
   - Only split into directories (`commands/`, `workflows/`, `memory/`) if multiple distinct outcomes/domains already exist per `growth-rule.md`.
   - Map Tier 1 (Required), Tier 2 (Optional), and Tier 3 (Forbidden) context per command (`memory/context-budget.md`).

3. **Draft `SKILL.md` (Dispatcher Pattern)**:
   - Target size: ~350 tokens (~250 words max).
   - Frontmatter includes `name` and pushy `description` with embedded anti-triggers.
   - Dispatch table: `User Intent` → `Command` → `What it loads`.
   - No inline domain logic — pointer to `spec.md` for non-negotiable rules.

4. **Write Command File(s)**:
   - Dispatches to target workflow and loads only necessary memory.
   - Explicitly states what is omitted to prevent context pollution.

5. **Write Workflow File(s)**:
   - Step-by-step procedure for exactly one outcome.
   - Concludes with a concrete `## Validation checklist`.

6. **Write Memory File(s)**:
   - Pure facts, schemas, constraints, and operational tables.
   - Isolate any human-facing philosophy into unreferenced `memory/philosophy.md`.

7. **Add Deterministic Tooling & Metadata**:
   - Add `tools/validate_skill.py` and `tools/build-skill.js`.
   - Add `package.json`, `.tidyfactor`, `brand.json`, `CHANGELOG.md`, `README.md`, `README.ar.md`.

8. **Validate & Package**:
   - Run `python tools/validate_skill.py`.
   - Run `node tools/build-skill.js`.

---

## Validation Checklist

- [ ] `SKILL.md` token count within budget (~350 tokens) and contains explicit anti-triggers
- [ ] `SKILL.md` contains no domain knowledge or embedded rules text, only routing
- [ ] Every workflow ends in a concrete checklist
- [ ] No single-file subfolders (Rule 4: No empty structures)
- [ ] Operational memory contains zero marketing narrative or unisolated philosophy
- [ ] Automated validation (`validate_skill.py`) passes without errors
