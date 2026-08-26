# Growth Rule (generic — applies to any skill this layer creates or audits)

<!-- last-verified: 2026-08-27 -->

A skill starts flat: `SKILL.md` + one commands file + one workflows file + one memory file. Add a new file, or split an existing one into a folder, only when ONE of these is true right now — not in anticipation:

1. **Size trigger.** A file exceeds ~150-300 lines (300 for memory/reference docs, 150 for command/workflow files — commands and workflows should stay scannable). Split along the axis actually causing the growth (a new market, a new engagement type, a new platform variant) — not arbitrarily in half.

2. **Branch trigger.** A workflow needs to branch on a variable none of the current memory files cover (e.g., a new client segment, a new target stack, a new compliance regime). Add one new memory or workflow file for that specific branch. Don't rewrite existing files to bolt the branch on inline.

3. **Variant trigger.** The skill's output needs a second distinct form (a short-form vs. full-form template, a different target platform). Add one new asset/template file, and add one line to skill.md's dispatch table (or the relevant command) saying which request maps to which variant.

4. **Decision Complexity trigger (CDL Layer).** Adopt the Contextual Decision Layer (`brief` command + `decision-points.md` + `.tidyfactor/<skill>-brief.md` cache) ONLY when a skill meets all three criteria:
   - (a) The skill has $\ge 3$ interdependent architectural choices (e.g., framework, database engine, UI styling tier) where wrong assumptions cause total deliverable failure.
   - (b) Downstream commands must inherit cached baseline decisions across repeated user turns without re-interviewing.
   - (c) The skill implements pre-emit self-critique (Axis 7: Decision Alignment).
   *Do NOT adopt CDL speculatively for linear, single-purpose, or standalone utility skills.*

5. **Rule Catalog Complexity Trigger (Prioritized Impact Taxonomy).** When a skill maintains $\ge 15$ operational guidelines, lints, or performance/security best practices:
   - Group rules strictly by prioritized impact tiers (`CRITICAL`, `HIGH`, `MEDIUM`, `LOW`) rather than flat alphabetical lists.
   - Standardize rule anatomy following `assets/rule-template.md` (Rule ID, Impact Rating, Problem Rationale, Incorrect Code, Correct Code, Edge Cases).
   - Encapsulate rules within a dedicated memory catalog (e.g. `memory/<domain>-rules.md`) and load it selectively into relevant commands/workflows.

## Explicitly not triggers

- "We might need this later" — not a trigger.
- "It would be more organized as a folder" — not a trigger by itself; organization follows from an actual second file existing (rule 5 in spec.md), not the reverse.
- Matching another skill's file count "for consistency" — not a trigger; each skill's structure follows its own triggers.

## When auditing

If an existing skill has multiple files in a category, each one should trace back to one of the triggers above. A file that doesn't map to any trigger is a spec violation — flag it in the audit report as a candidate for merging back in.
