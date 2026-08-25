---
name: <skill-name>
description: <what it does AND when to trigger it — "what + when" pattern, one paragraph, max 1024 chars, no philosophy language>
---

# <Skill Title>

A command dispatcher. [One line: what this skill's job is, in plain terms.]

## Commands

| User intent | Command | What it loads |
|---|---|---|
| <intent 1> | `references/commands.md` (or `references/commands/<name>.md` if more than one) | <workflow file> + <memory file(s)> |

<!-- Add one row per distinct command. Do not add a row for a command that doesn't exist yet. -->

## Non-negotiable constraints

<!-- Only include this section if the skill has more than one command, or if there's a
     domain-specific rule every command must respect regardless of which one fires.
     Otherwise delete this section — an empty constraints list is an empty structure. -->

1. <constraint>

## Tooling Scope (Rule 10)

<!-- Required only if this skill has a tools/ directory. Delete this section otherwise. -->

- **Languages**: <node | python | shell>
- **Mutations**: <read-only | file-mutations | network>
- **Network**: <none | required for X>

## Validation

<!-- Only if there's a skill-wide check that applies across all commands, distinct from
     each workflow's own checklist. Otherwise omit — validation lives in the workflow files. -->
