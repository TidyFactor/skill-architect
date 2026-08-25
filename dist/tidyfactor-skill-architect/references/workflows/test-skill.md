# Workflow: test-skill

One outcome: a `tests/scenarios.md` file containing 3+ realistic test scenarios that validate the target skill end-to-end.

---

## Steps

1. **Read the target skill's activation surface**:
   - Read `SKILL.md` frontmatter (`name`, `description`, anti-triggers).
   - Read every command file under `references/commands/`.
   - Note the dispatch table: which intents map to which commands.

2. **Generate happy-path tests (1 per command)**:
   - For each command in the dispatch table, write one realistic user prompt that should trigger it.
   - Define expected behavior: which command fires, which workflow/memory files load, what output shape looks like.

3. **Generate edge-case tests (1 per command)**:
   - For each command, write one prompt near the anti-trigger boundary — something that sounds related but tests the skill's discrimination ability.
   - Define whether the skill should activate or decline.

4. **Generate negative tests (at least 1)**:
   - Write a prompt that should explicitly NOT trigger the skill — something that matches a keyword but violates the anti-triggers.
   - Expected behavior: skill does not activate.

5. **Format as structured scenarios**:
   - Output to `tests/scenarios.md` in the target skill directory.
   - Use the format defined below.

---

## Scenario Format

```markdown
# Test Scenarios for <skill-name>

## Test 1: <short description>
- **Type**: happy-path | edge-case | negative
- **Prompt**: "<exact user prompt>"
- **Expected Command**: `references/commands/<name>.md` (or "none" for negative tests)
- **Expected Behavior**: <what should happen>
- **Pass Criteria**: <how to verify success>

## Test 2: ...
```

---

## Validation Checklist

- [ ] At least 3 test scenarios generated (1 happy-path, 1 edge-case, 1 negative minimum)
- [ ] Every command in the dispatch table has at least 1 happy-path test
- [ ] At least 1 negative test exercises an anti-trigger
- [ ] Each scenario has a concrete pass criteria, not a vague description
- [ ] Scenarios are written as user prompts, not as internal system descriptions
