# Command: review

Runtime entry point for "Periodic Skill Review" / "مراجعة وتدقيق دوري للمهارة" / "افحص ثغرات وتضخم المهارة عبر المحاور الستة".

## Context-Aware Prompts & Auto-Sensing

1. **Auto-Sense Skill Context**:
   - Detect the target skill directory (e.g. `path/to/skills/<skill-name>`).
   - Read its `SKILL.md`, `manifest.json`, `package.json`, and `references/`.
   - Inspect its `assets/` folder to prepare for duplicate and orphan scanning.

2. **Dispatch to Workflow**:
   - Load `../workflows/periodic-review.md` — the 6-Axis Periodic Review Workflow.
   - Load `../memory/periodic-review-matrix.md` — the authoritative scoring rubric and audit matrix.
   - Run the workflow.

## Does NOT

- Does not perform superficial code reviews: this command evaluates structural compliance, asset bloat, operational memory purity, and governance hygiene across all 6 axes.
- Does not modify files without explicit user approval.
