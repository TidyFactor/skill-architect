# Growth Rule (generic — applies to any skill this layer creates or audits)

<!-- last-verified: 2026-08-25 -->

A skill starts flat: `SKILL.md` + one commands file + one workflows file + one memory file. Add a new file, or split an existing one into a folder, only when ONE of these is true right now — not in anticipation:

1. **Size trigger.** A file exceeds ~150-300 lines (300 for memory/reference docs, 150 for command/workflow files — commands and workflows should stay scannable). Split along the axis actually causing the growth (a new market, a new engagement type, a new platform variant) — not arbitrarily in half.

2. **Branch trigger.** A workflow needs to branch on a variable none of the current memory files cover (e.g., a new client segment, a new target stack, a new compliance regime). Add one new memory or workflow file for that specific branch. Don't rewrite existing files to bolt the branch on inline.

3. **Variant trigger.** The skill's output needs a second distinct form (a short-form vs. full-form template, a different target platform). Add one new asset/template file, and add one line to skill.md's dispatch table (or the relevant command) saying which request maps to which variant.

## Explicitly not triggers

- "We might need this later" — not a trigger.
- "It would be more organized as a folder" — not a trigger by itself; organization follows from an actual second file existing (rule 5 in spec.md), not the reverse.
- Matching another skill's file count "for consistency" — not a trigger; each skill's structure follows its own triggers.

## When auditing

If an existing skill has multiple files in a category, each one should trace back to one of the three triggers above. A file that doesn't map to any trigger is a spec violation — flag it in the audit report as a candidate for merging back in.
