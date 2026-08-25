# Command: test

Runtime entry point for "test this skill" / "generate test scenarios for this skill."

## Dispatch steps

1. Load `../memory/spec.md` — so tests validate against the actual structural rules.
2. Load `../workflows/test-skill.md` — the test scenario generation sequence.
3. Read the target skill's actual files (SKILL.md + all commands) to understand the activation surface.
4. Produce the test scenario file defined in `test-skill.md`.

## Do not

- Do not load `../commands/init.md` or `../commands/audit.md` — testing is a separate concern from creation or auditing.
- Do not execute the test scenarios automatically — generate them for human or CI review.
