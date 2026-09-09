<!-- last-verified: 2026-09-09 -->
# Memory: periodic-review-matrix

Authoritative scoring rubric, compliance thresholds, and remediation formulas for the 6-Axis Periodic Skill Review Protocol.

## 1. 100-Point Scoring Rubric

| Axis | Max Points | Key Criteria | Failure Penalty |
|---|---|---|---|
| **1. Commands & Context-Aware Prompts** | 15 pts | Manifest alignment, context auto-sensing, single workflow routing | -5 per unregistered or missing command |
| **2. Workflows & Single Outcome** | 20 pts | One deliverable per workflow, explicit `## Validation checklist` | -10 per missing checklist or dual outcome |
| **3. Operational Memory Purity** | 15 pts | Factual density, YAML primacy, `last-verified` (≤ 180 days) | -5 per stale date or narrative bloat |
| **4. Tooling & Protocol Integration** | 15 pts | Zero Runtime Crash, AST linting, MCP boundary, Git sync hook | -10 for script crashes or leaked tool scope |
| **5. Governance & Tone of Voice** | 20 pts | Atomic SemVer sync, Keep a Changelog SSOT, secret scrubbing, direct tone | -15 for unsynced versions or leaked secrets |
| **6. Assets & Hygiene** | 15 pts | Zero duplicates (SHA-256), zero orphaned images, WebP format optimization | -5 per duplicate asset or unreferenced file |

## 2. Evaluation Grades

- **🎖️ Grade A — Production Ready (90–100 pts)**: Zero critical defects, 100% test pass, optimal asset hygiene. Ready for immediate release.
- **⚠️ Grade B — Needs Hardening (75–89 pts)**: Minor documentation drift, unoptimized PNG assets, or memory dates nearing 180 days. Requires patch updates.
- **❌ Grade C — Non-Compliant (< 75 pts)**: Missing checklists, broken relative links, version divergence, or duplicate assets. Block release until remediated.

## 3. Immediate Remediation Matrix

| Defect Detected | Root Cause | Mandatory Corrective Action |
|---|---|---|
| **Duplicate Asset** | Identical file saved under multiple names | Run SHA-256 hash check. Delete duplicate and redirect references to canonical asset. |
| **Orphaned Asset** | Obsolete image left in `assets/` | Scan `.md` files. If zero occurrences found, delete asset file from repository. |
| **Stale Memory Date** | `<!-- last-verified -->` > 180 days | Re-verify memory rules against active codebase, update content, and refresh date stamp. |
| **Missing Changelog** | Unreleased changes or undocumented version | Create or update `CHANGELOG.md` under Keep a Changelog v1.1.0 and SemVer 2.0.0. |
| **Static Text Survey** | Asking user via chat bullet points | Refactor to Native Modal Wizard (`ask_question`) under Context Delta Resolution formula. |
| **JSON Cognitive Bloat** | Storing brand or design tokens in JSON | Migrate to `brand.yaml` or YAML snapshot schemas (Rule 15 YAML Primacy). |
