# Test Scenarios for tidyfactor-skill-architect

## Test 1: Initialize a new skill (Happy Path)
- **Type**: happy-path
- **Prompt**: "Build me a new skill for SEO optimization following TidyFactor methodology"
- **Expected Command**: `references/commands/init.md`
- **Expected Behavior**: Loads `create-skill.md` workflow, `spec.md`, `growth-rule.md`, and `skill-md-skeleton.md` to scaffold a flat 4-file structure.
- **Pass Criteria**: Output is a compliant `SKILL.md` dispatcher (~350 tokens) + 3 initial flat reference files.

## Test 2: Audit an existing skill (Happy Path)
- **Type**: happy-path
- **Prompt**: "Audit tidyfactor-marketing skill against TidyFactor rules"
- **Expected Command**: `references/commands/audit.md`
- **Expected Behavior**: Loads `audit-skill.md` workflow and scores the skill against all 12 structural rules.
- **Pass Criteria**: Compliance report scored out of 12 (X/12) with file-level specific fixes for any fails.

## Test 3: Generate test scenarios (Happy Path)
- **Type**: happy-path
- **Prompt**: "Generate test scenarios for tidyfactor-design skill"
- **Expected Command**: `references/commands/test.md`
- **Expected Behavior**: Loads `test-skill.md` workflow and generates `tests/scenarios.md` with happy-path, edge-case, and negative test cases.
- **Pass Criteria**: A structured `tests/scenarios.md` file containing 3+ test cases with pass criteria.

## Test 4: Evaluate skill file expansion (Edge Case)
- **Type**: edge-case
- **Prompt**: "Should I split my single memory.md into memory/a.md and memory/b.md because it feels too long?"
- **Expected Command**: `references/commands/grow.md`
- **Expected Behavior**: Evaluates request against size (>300 lines), branch, or variant triggers.
- **Pass Criteria**: Rejects split if file is under 300 lines or split is arbitrary; requires an explicit growth trigger.

## Test 5: Generic non-structural prompt request (Negative Test)
- **Type**: negative
- **Prompt**: "Write me a prompt to improve my email marketing conversion rate"
- **Expected Command**: none (Anti-trigger)
- **Expected Behavior**: Declines activation as a skill architect; directs to domain-specific skill (`tidyfactor-marketing`).
- **Pass Criteria**: `tidyfactor-skill-architect` does not activate for general copywriting or non-structural tasks.
