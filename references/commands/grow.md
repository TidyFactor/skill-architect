# Command: grow

Runtime entry point for "should I add a new file / split this file / add a new market-variant to this skill."

## Dispatch steps

1. Load `../memory/growth-rule.md` only — this decision does not need the full spec, and does not need create-skill.md or audit-skill.md.
2. Check the specific change the user is proposing against the three triggers in growth-rule.md.
3. Answer directly: which trigger (if any) is met, and therefore whether to add a file, split a file, or make the change inside an existing file instead.

## Do not

- Do not treat "it might be useful later" as a trigger — growth-rule.md's triggers are all observed-now conditions, never speculative ones.
