# Command: init

Runtime entry point for "build me a skill for X." This command does not draft anything itself — it assembles context, then hands off.

## Dispatch steps

1. Load `../memory/spec.md` — the structural rules the draft must satisfy.
2. Load `../memory/growth-rule.md` — so the initial file count decision (4 files vs. more) is made correctly from the start, not retrofitted later.
3. Load `../workflows/create-skill.md` — the actual creation sequence.
4. Load `../../assets/skill-md-skeleton.md` — the skeleton the new skill.md is written from, so every TidyFactor-governed skill's skill.md has the same shape (dispatcher table + constraints section), consistent with Convention over Configuration.
5. Proceed into skill-creator's Capture Intent → Interview → Write the SKILL.md loop, applying the loaded context at the "Write the SKILL.md" step.

## Do not

- Do not skip straight to skill-creator without loading spec.md first — the resulting draft will be a generic skill-creator skill, not a TidyFactor one.
- Do not create `references/commands/`, `references/workflows/`, `references/memory/` as folders for the new skill unless step 2 of `create-skill.md` determines the skill needs more than one file in that category (see No Empty Structures in spec.md).
