# Terminology

Used consistently across every skill this layer produces, so a person moving between tidyfactor-html, tidyfactor-php, tidyfactor-design, etc. finds the same vocabulary each time.

- **Skill** — a runtime capability package (SKILL.md + references + optional assets/scripts), not a single prompt.
- **Command** — one dispatcher file, mapped to one user intent, that selects a workflow and injects memory. Never contains task instructions itself.
- **Workflow** — one ordered sequence of steps producing one outcome, ending in a validation checklist.
- **Memory** — operational context loaded at runtime: facts, rules, terminology, templates, constraints. Distinguished from workflow by being static reference, not a sequence of actions.
- **Runtime Context Assembly** — the act of a command loading exactly the workflow + memory files a given task needs, nothing more.
- **Growth trigger** — one of the three conditions in `growth-rule.md` that justifies adding or splitting a file. The only legitimate reason a skill gains files over time.
- **Empty structure** — a folder created for organization before it holds more than one file. Always avoided (spec.md rule 5).
