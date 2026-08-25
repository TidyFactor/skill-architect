# Context Budget & Token Economy

<!-- last-verified: 2026-08-25 -->

Pure operational rules for managing agent context budgets and token economy across TidyFactor skills.

---

## 1. Component Size & Token Limits

| Component | Target Size | Maximum Cap | Purpose |
|---|---|---|---|
| **`SKILL.md`** (Dispatcher) | ~350 tokens (~250 words) | 500 tokens (~350 words) | Ultra-fast routing without task execution |
| **`references/commands/*.md`** | 30–80 lines | 150 lines | Dispatcher glue and parameter resolution |
| **`references/workflows/*.md`** | 50–120 lines | 150 lines | Step-by-step procedure + validation checklist |
| **`references/memory/*.md`** | 60–200 lines | 300 lines | Deterministic schemas, rules, and tables |

---

## 2. Context Tiers per Execution

Every command execution enforces three distinct context boundaries:

### Tier 1: Required Context (Strictly Injected)
- The single matching `references/commands/<command>.md`.
- The single target `references/workflows/<workflow>.md`.
- The primary domain memory file required for that specific outcome (e.g., `references/memory/spec.md`).

### Tier 2: Optional Context (Branch-Triggered Only)
- Injected **only** when an explicit workflow step branches on an environmental variable (e.g., loading stack-specific memory like Next.js vs PHP).
- Never pre-loaded speculatively.

### Tier 3: Forbidden Context (Never Injected)
- Unrelated command files from the same skill.
- Inactive workflow files.
- `references/memory/philosophy.md` (human-facing brand rationale).
- Bulk codebase dumps or un-indexed external directory trees.

---

## 3. Progressive Disclosure & Anti-Over-Injection

1. **Single Routing Layer**: Maintain exactly one level of progressive disclosure (`SKILL.md` → Command → Workflow + Memory). Avoid multi-layer nested sub-dispatchers.
2. **Negative Triggers (Anti-Triggers)**: Every skill frontmatter `description` must declare explicit negative triggers (what the skill does NOT do) to prevent accidental context waste.
3. **Lazy Memory Loading**: Commands must explicitly specify which memory files to load and which to omit.
