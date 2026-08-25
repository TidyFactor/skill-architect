# Workflow: audit-skill

One outcome: a compliance report against `memory/spec.md`, with specific fixes — not a general code review.

## Steps

1. Read the target's `SKILL.md` in full.
2. Read every file under its `references/` (and `assets/`, `bin/`, `tools/`, `dist/` if present).
3. Score against each of spec.md's 12 rules as pass/fail, not a vague impression:
   - Does skill.md dispatch, or does it do the task itself?
   - Does every workflow file map to exactly one outcome, with a checklist?
   - Is memory factual/operational, or is it narrative/rationale?
   - Are there any folders with only one file in them (empty-structure violation)?
   - Is there philosophy/manifesto language inside skill.md, a command, or a workflow file (should be isolated to a memory/philosophy.md if it exists at all)?
   - If the skill has a growth history (multiple reference files), does each one map to one of growth-rule.md's three triggers, or does one look speculative?
   - Are deterministic operations wrapped in `tools/` over native toolchains, with no autonomous mass-edit scripts?
   - Is there any documented or observed platform-specific behavior difference (Antigravity / Claude Code / Cursor / Codex) that breaks the parity claim?
   - Does `SKILL.md` frontmatter comply with platform constraints (`name` required + matches directory, `description` ≤ 1024 chars, follows "what + when" pattern)?
   - If the skill has a `tools/` directory, does `SKILL.md` declare tooling scope (languages, mutations, network)?
   - Do all memory files have `<!-- last-verified: YYYY-MM-DD -->` comments, and are any older than 180 days?
   - If the skill has a companion MCP server, is the skill-vs-MCP boundary documented in the dispatcher body?
4. For every failed item, name the specific file and the specific fix — "split references/memory.md at line 140 because it covers two markets" beats "memory file is too long."

## Report format

```
## Compliance: X/12 rules pass

- [pass/fail] Dispatcher discipline — <file:line if fail>
- [pass/fail] One-workflow-one-outcome + checklist — <file if fail>
- [pass/fail] Memory is operational, not narrative — <file if fail>
- [pass/fail] No empty structures — <folder if fail>
- [pass/fail] Philosophy isolated — <file if fail>
- [pass/fail] Growth is trigger-justified — <file if fail>
- [pass/fail] Quality bar & native tooling — <file if fail>
- [pass/fail] Cross-platform parity — <observed gap if fail>
- [pass/fail] Platform compatibility — <frontmatter constraint violation if fail>
- [pass/fail] Tool permission declaration — <missing scope if fail, or "N/A" if no tools/>
- [pass/fail/warn] Memory freshness — <stale files if any>
- [pass/fail/N/A] Skill vs MCP boundary — <undocumented boundary if fail>

### Fixes
1. <specific, file-level fix>
2. ...
```

## Validation checklist

- [ ] Every fail has a named file and a concrete fix, not a generic note
- [ ] Report doesn't recommend adding new files unless a growth-rule.md trigger is explicitly cited
- [ ] Score is out of 12, matching spec.md's current rule count
- [ ] Memory freshness is reported as warn (not fail) for dates > 180 days
