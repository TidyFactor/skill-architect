# Workflow: create-skill

One outcome: a new skill folder that is both (a) valid per skill-creator's `quick_validate`, and (b) compliant with `memory/spec.md`. Every step below produces something checked by the Validation section at the end.

## Steps

1. **Capture intent** (skill-creator's own step) — what should the skill do, when should it trigger, what's the output format. Do this before anything else; a structurally perfect skill for the wrong task is still wrong.

2. **Decide the minimal file count.** Default is 4 files: `SKILL.md`, one commands file, one workflows file, one memory file — flat, no subfolders. Only create `references/commands/`, `references/workflows/`, `references/memory/` as folders (each holding multiple files) if the interview in step 1 already surfaced more than one distinct command, more than one distinct workflow-outcome, or more than one distinct memory domain. Otherwise stay flat. This decision is made once, here — not revisited mid-draft.

3. **Write skill.md from `assets/skill-md-skeleton.md`.** It must contain: frontmatter (name, description — pushy per skill-creator's guidance), a dispatch table (intent → command → what it loads), and a short "non-negotiable constraints" section if the skill has more than one command. It must NOT contain the domain knowledge itself — that goes in the command/workflow/memory files it points to.

4. **Write the command file(s).** Each command: states what it dispatches to, states what it does NOT do, states what it must NOT load (to prevent over-injection). A command that contains actual task instructions instead of pointers is miswritten — move that content to a workflow.

5. **Write the workflow file(s).** One file per outcome. Each ends with a Validation checklist — concrete, checkable items, not "make sure it's good."

6. **Write the memory file(s).** Facts, rules, terminology, pricing/technical/domain anchors — whatever the skill needs to know that isn't a sequence of actions. If the interview revealed branding or rationale language ("why this methodology exists"), put it in a separate `memory/philosophy.md` and do not reference it from skill.md or any command — it's for a human reading the folder, not for the agent executing it.

7. **Run skill-creator's own validate/test loop** (`quick_validate`, then test prompts per skill-creator's process) on top of this draft.

## Validation

- [ ] `quick_validate` from skill-creator passes
- [ ] skill.md contains no domain knowledge, only dispatch + constraints
- [ ] Every workflow file ends in a checklist
- [ ] No folder (`commands/`, `workflows/`, `memory/`) exists with only one file in it
- [ ] No philosophy/manifesto language appears outside `memory/philosophy.md`, and `memory/philosophy.md` (if present) is not referenced by skill.md or any command
