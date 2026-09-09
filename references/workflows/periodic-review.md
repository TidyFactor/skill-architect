# Workflow: periodic-review

One outcome: a comprehensive, 6-axis skill audit report with concrete gap findings, asset bloat analysis, and an actionable implementation plan for skill evolution.

## The 6 Review Axes

Every skill undergoes rigorous evaluation across all 6 core axes:

### Axis 1: Commands & Context-Aware Prompts
- **Alignment with Manifest**: Every command in `SKILL.md` must be registered in `manifest.json` under `tools[*].invoked_by_commands` and `decision_gates`.
- **Context-Aware Prompts**: Commands must auto-sense project context, package managers, and configuration files on disk rather than guessing or prompting with static surveys.
- **Router Discipline**: Every command file in `references/commands/*.md` must route to exactly one primary workflow.

### Axis 2: Workflows & Single Outcome Checklists
- **One Workflow = One Outcome**: Workflows must produce a single, clearly bounded deliverable.
- **Mandatory Validation Checklist**: Every workflow must conclude with an explicit `## Validation checklist` with binary pass/fail verification items.
- **Architectural Traceability**: Verify if domain-critical workflows (e.g. ADR generation, changelog updates, code scraping) are present or missing.

### Axis 3: Operational Memory & Semantic Density
- **Factual Purity**: Memory files contain pure technical patterns, schemas, and configurations—zero narrative filler or marketing prose.
- **Memory Freshness (Rule 11)**: All operational memory files must feature valid `<!-- last-verified: YYYY-MM-DD -->` timestamps (≤ 180 days).
- **YAML Primacy (Rule 15)**: Brand definitions, decision snapshots, and cognitive schemas must prioritize YAML (`brand.yaml`) over JSON to maximize token efficiency.
- **Mindmaps & Naming Conventions**: Verify presence of architecture diagrams (Mermaid) and standardized naming conventions.

### Axis 4: Tooling, AST Scrapers & Protocol Integration
- **Deterministic Native Tooling**: Runtime tools in `scripts/` or packaging tools in `tools/` must execute without unhandled exceptions (`Zero Runtime Crash`).
- **MCP Protocol Integration**: Verify clean boundaries between local static workflows and stateful MCP server tools (Fail-Open doctrine).
- **Git Hook & Pre-Commit Sync**: Verify presence or guidance for pre-commit guards ensuring documentation evolves synchronously with code.

### Axis 5: Governance, Markdown Linting & Tone of Voice
- **Atomic SemVer Synchronization (Rule 2)**: Version bumps must synchronize atomically across `package.json`, `.tidyfactor`, `brand.yaml`, `brand.json`, `README.md`, `README.ar.md`, and `CHANGELOG.md`.
- **CHANGELOG as SSOT**: Follow Keep a Changelog v1.1.0 with dated release sections and Conventional Commit mappings.
- **Secret Scanning & Redaction**: Zero real credentials, tokens, or local workstation paths (`file:///C:`) allowed in any documentation.
- **Tone of Voice Policy**: Direct, imperative, technical, and free of hype or marketing adjectives.

### Axis 6: Assets & Folder Structure Hygiene
- **Duplicate Asset Elimination**: Execute SHA-256 hashing across all image assets in `assets/`. Immediate removal of identical duplicate files.
- **Orphan Asset Cleanup**: Scan all `.md` files for image references. Detect and purge unreferenced orphan images in `assets/`.
- **Format Optimization**: Enforce WebP conversion for non-vector raster images (>50KB) to achieve up to 80% compression without perceptible quality loss.

---

## Steps

1. **Execute Automated Skill Integrity Check**:
   ```bash
   python tools/validate_skill.py
   ```
2. **Scan Assets for Duplicates & Orphans**:
   - Run SHA-256 hash inspection across `assets/`.
   - Scan markdown files for image cross-references.
3. **Audit Operational Memory Freshness & YAML Primacy**:
   - Check `last-verified` timestamps.
   - Verify `brand.yaml` existence and YAML schema density.
4. **Compile 6-Axis Review Findings**:
   - Score each axis against `memory/periodic-review-matrix.md`.
   - Formulate a prioritized implementation plan (`implementation_plan.md`).
5. **Obtain User Approval & Execute Atomic Upgrade**:
   - Execute file creations and modifications.
   - Re-run automated tests and rebuild `.skill` packages.

## Validation checklist

- [ ] All 6 axes evaluated with specific file-level findings, not generic impressions
- [ ] Asset hashing executed to identify duplicate or orphaned files
- [ ] Operational memory checked for freshness (≤ 180 days) and YAML primacy
- [ ] Report provides a concrete, prioritized implementation plan for skill evolution
- [ ] Passing criteria matches the 100-point rubric in `memory/periodic-review-matrix.md`
