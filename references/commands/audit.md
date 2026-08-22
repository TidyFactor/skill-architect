# Command: audit

Runtime entry point for "does this skill follow TidyFactor / audit this skill."

## Dispatch steps

1. Load `../memory/spec.md`.
2. Load `../workflows/audit-skill.md` — the check sequence and report format.
3. Read the target skill's actual files (SKILL.md + everything under references/, assets/, scripts/) before scoring anything — do not audit from the skill's description alone.
4. Produce the report format defined in `audit-skill.md`. Do not silently fix the skill unless the user asked for a fix, not just an audit — an audit is read-only by default.

## Do not

- Do not load `../commands/init.md` — audit is a separate command from creation; a request to audit is not a request to rebuild.
