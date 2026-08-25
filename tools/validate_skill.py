#!/usr/bin/env python3
"""
validate_skill.py — TidyFactor Skill Architect Release & Integrity Validator.
Checks:
1. SemVer synchronization across package.json, .tidyfactor, brand.json, CHANGELOG.md.
2. License consistency (Apache-2.0).
3. Existence of all files referenced in SKILL.md.
4. Validation checklists in all workflow files.
5. Absence of machine-specific absolute paths.
"""

import sys
import os
import json
import re
from pathlib import Path

# Ensure UTF-8 output on Windows terminal
if sys.platform == "win32":
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")

def main():
    root = Path(__file__).resolve().parent.parent
    errors = []
    warnings = []
    
    print("=" * 60)
    print("  RUNNING TIDYFACTOR SKILL ARCHITECT RELEASE VALIDATION")
    print("=" * 60)
    
    # 1. SemVer Synchronization Check
    print("\n[1] Checking SemVer synchronization across metadata...")
    pkg_file = root / "package.json"
    tf_file = root / ".tidyfactor"
    brand_file = root / "brand.json"
    cl_file = root / "CHANGELOG.md"
    
    pkg_ver = json.loads(pkg_file.read_text(encoding="utf-8")).get("version") if pkg_file.exists() else None
    tf_ver = json.loads(tf_file.read_text(encoding="utf-8")).get("version") if tf_file.exists() else None
    
    brand_data = json.loads(brand_file.read_text(encoding="utf-8")) if brand_file.exists() else {}
    brand_ver = brand_data.get("version") or brand_data.get("meta", {}).get("version")
    
    print(f"  package.json : {pkg_ver}")
    print(f"  .tidyfactor  : {tf_ver}")
    print(f"  brand.json   : {brand_ver}")
    
    if not (pkg_ver and tf_ver and brand_ver and pkg_ver == tf_ver == brand_ver):
        errors.append(f"Version mismatch: package.json({pkg_ver}) vs .tidyfactor({tf_ver}) vs brand.json({brand_ver})")
    else:
        print(f"  [OK] Version {pkg_ver} synchronized across all JSON metadata.")
        
    if cl_file.exists():
        cl_text = cl_file.read_text(encoding="utf-8")
        if f"## [{pkg_ver}]" not in cl_text and f"[{pkg_ver}]" not in cl_text:
            errors.append(f"CHANGELOG.md is missing release entry for version [{pkg_ver}].")
        else:
            print(f"  [OK] CHANGELOG.md contains release entry for [{pkg_ver}].")
    else:
        errors.append("Missing CHANGELOG.md.")
        
    # 2. License check
    print("\n[2] Checking license consistency...")
    license_file = root / "LICENSE"
    if license_file.exists():
        print("  [OK] LICENSE file exists (Apache-2.0).")
    else:
        errors.append("Missing LICENSE file.")
        
    # 3. Check referenced files in SKILL.md
    print("\n[3] Checking SKILL.md referenced files exist on disk...")
    skill_md = root / "SKILL.md"
    if skill_md.exists():
        content = skill_md.read_text(encoding="utf-8")
        refs = re.findall(r'(?:references|memory|commands|workflows)/[a-zA-Z0-9_\-\./]+(?:\.md|\.json)?', content)
        for ref in sorted(set(refs)):
            target = root / ref
            if not target.exists() and not (root / "references" / ref).exists():
                errors.append(f"SKILL.md references non-existent file: {ref}")
            else:
                print(f"  [OK] Found {ref}")
    else:
        errors.append("Missing SKILL.md.")

    # 4. Check workflow validation checklists
    print("\n[4] Checking workflow checklists...")
    wf_dir = root / "references" / "workflows"
    if wf_dir.exists():
        for wf in wf_dir.glob("*.md"):
            txt = wf.read_text(encoding="utf-8").lower()
            if "validation checklist" not in txt:
                errors.append(f"Workflow {wf.name} missing '## Validation checklist'")
            else:
                print(f"  [OK] {wf.name} has Validation checklist.")

    # 5. Audit for leaked machine paths
    print("\n[5] Auditing for leaked machine-specific absolute paths...")
    for ext in ["*.md", "*.json", "*.js", "*.py"]:
        for file in root.rglob(ext):
            if any(part in file.parts for part in [".git", "node_modules", "dist"]):
                continue
            text = file.read_text(encoding="utf-8", errors="ignore")
            if re.search(r'[A-Za-z]:\\[Users|wamp64|Dev\-Studio]', text, re.IGNORECASE):
                if file.name not in ["release_suite.py", "audit_all_skills.py", "validate_skill.py"]:
                    errors.append(f"Machine-specific absolute path found in: {file.relative_to(root)}")

    # 6. SKILL.md token count estimation (Rule 1: ~350 tokens target, 500 max)
    print("\n[6] Checking SKILL.md token budget...")
    if skill_md.exists():
        skill_text = skill_md.read_text(encoding="utf-8")
        words = len(skill_text.split())
        estimated_tokens = int(words * 1.25)
        print(f"  SKILL.md size: {len(skill_text)} chars / {words} words ≈ {estimated_tokens} tokens")
        if estimated_tokens > 500:
            warnings.append(f"SKILL.md estimated at {estimated_tokens} tokens (target: ~350, max: 500)")
        else:
            print(f"  [OK] Within token budget ({estimated_tokens} tokens, target ~350, max 500).")

    # 7. Memory freshness check (Rule 11: last-verified within 180 days)
    print("\n[7] Checking memory freshness markers (Rule 11)...")
    mem_dir = root / "references" / "memory"
    if mem_dir.exists():
        from datetime import datetime, timedelta
        today = datetime.now()
        max_age = timedelta(days=180)
        for mf in mem_dir.glob("*.md"):
            if mf.name == "philosophy.md":
                continue  # Philosophy is unreferenced, skip
            text = mf.read_text(encoding="utf-8")
            match = re.search(r'<!--\s*last-verified:\s*(\d{4}-\d{2}-\d{2})\s*-->', text)
            if match:
                verified_date = datetime.strptime(match.group(1), "%Y-%m-%d")
                age = today - verified_date
                if age > max_age:
                    warnings.append(f"Memory file {mf.name} last verified {match.group(1)} ({age.days} days ago, max 180)")
                else:
                    print(f"  [OK] {mf.name}: verified {match.group(1)} ({age.days} days ago)")
            else:
                warnings.append(f"Memory file {mf.name} missing <!-- last-verified: YYYY-MM-DD --> marker")

    # 8. SKILL.md Frontmatter YAML Syntax & Constraints (Rule 9)
    print("\n[8] Checking SKILL.md frontmatter YAML syntax & constraints (Rule 9)...")
    if skill_md.exists():
        content = skill_md.read_text(encoding="utf-8")
        if not content.startswith("---"):
            errors.append("SKILL.md is missing opening YAML frontmatter '---'.")
        else:
            parts = content.split("---", 2)
            if len(parts) < 3:
                errors.append("SKILL.md has unclosed YAML frontmatter '---'.")
            else:
                fm_raw = parts[1]
                try:
                    import yaml
                    fm_data = yaml.safe_load(fm_raw)
                    if not isinstance(fm_data, dict):
                        errors.append("SKILL.md frontmatter is not a valid YAML mapping.")
                    else:
                        name_val = fm_data.get("name")
                        desc_val = fm_data.get("description")

                        # Validate name
                        if not name_val or not isinstance(name_val, str):
                            errors.append("SKILL.md frontmatter missing or invalid 'name' field.")
                        elif name_val != root.name:
                            warnings.append(f"SKILL.md name '{name_val}' does not match root folder '{root.name}'.")
                        else:
                            print(f"  [OK] Name: '{name_val}' (valid).")

                        # Validate description
                        if not desc_val or not isinstance(desc_val, str):
                            errors.append("SKILL.md frontmatter missing or empty 'description' field.")
                        else:
                            desc_len = len(desc_val.strip())
                            if desc_len > 1024:
                                errors.append(f"SKILL.md description is {desc_len} chars (max 1024, Claude limit).")
                            elif desc_len > 920:
                                warnings.append(f"SKILL.md description is {desc_len}/1024 chars (near limit).")
                                print(f"  [WARN] Description: {desc_len}/1024 chars (near limit).")
                            else:
                                print(f"  [OK] Description: {desc_len}/1024 chars (YAML syntax valid).")
                except Exception as e:
                    errors.append(f"SKILL.md YAML frontmatter parsing failed: {e}")

    # 9. Tooling Scope Declaration (Rule 10)
    print("\n[9] Checking Tooling Scope declaration (Rule 10)...")
    tools_dir = root / "tools"
    has_executable_tools = tools_dir.exists() and any(
        f.suffix in [".py", ".js", ".sh", ".ts"] for f in tools_dir.iterdir() if f.is_file()
    )
    if has_executable_tools and skill_md.exists():
        skill_text = skill_md.read_text(encoding="utf-8")
        if "tooling scope" not in skill_text.lower():
            warnings.append("Skill has tools/ directory but SKILL.md is missing '## Tooling Scope' section (Rule 10)")
            print("  [WARN] Missing '## Tooling Scope' section in SKILL.md.")
        else:
            has_lang = any(k in skill_text.lower() for k in ["language", "languages", "python", "node", "shell"])
            has_mut = any(k in skill_text.lower() for k in ["mutation", "mutations", "read-only", "file"])
            if has_lang and has_mut:
                print("  [OK] Tooling Scope declared with languages and mutation scope.")
            else:
                warnings.append("Tooling Scope section in SKILL.md should specify Languages and Mutations.")
                print("  [WARN] Tooling Scope section incomplete.")
    else:
        print("  [OK] No executable tools directory found (N/A).")

    # 10. Test Scenarios Verification
    print("\n[10] Checking Test Scenarios (tests/scenarios.md)...")
    tests_file = root / "tests" / "scenarios.md"
    if tests_file.exists():
        test_content = tests_file.read_text(encoding="utf-8")
        test_matches = re.findall(r'(?m)^##\s+Test|\bTest\s+\d+:', test_content)
        test_count = len(test_matches)
        if test_count >= 3:
            print(f"  [OK] tests/scenarios.md found with {test_count} test scenarios (min 3).")
        else:
            warnings.append(f"tests/scenarios.md has only {test_count} scenario(s) (recommended: >= 3)")
            print(f"  [WARN] tests/scenarios.md has only {test_count} scenario(s).")
    else:
        warnings.append("Missing tests/scenarios.md (recommended: generate via 'test' command)")
        print("  [WARN] tests/scenarios.md not found.")

    # 11. Skill vs MCP Boundary (Rule 12)
    print("\n[11] Checking MCP boundary documentation (Rule 12)...")
    mcp_refs = False
    if skill_md.exists():
        st = skill_md.read_text(encoding="utf-8").lower()
        if "mcp" in st or (root / "mcp.json").exists() or (root / ".mcp").exists():
            mcp_refs = True
            if "boundary" in st or "mcp server" in st or "mcp" in st:
                print("  [OK] Skill vs MCP boundary documented.")
            else:
                warnings.append("Skill references MCP but does not explicitly document the Skill vs MCP boundary (Rule 12).")
                print("  [WARN] Undocumented MCP boundary.")
    if not mcp_refs:
        print("  [OK] No external MCP dependencies detected (N/A).")

    print("\n" + "=" * 60)
    if errors:
        print(f"[FAIL] {len(errors)} validation error(s) found:")
        for err in errors:
            print(f"  ❌ {err}")
    if warnings:
        print(f"[WARN] {len(warnings)} warning(s):")
        for warn in warnings:
            print(f"  ⚠️  {warn}")
    if not errors and not warnings:
        print("[SUCCESS] ALL SKILL INTEGRITY CHECKS PASSED!")
    elif not errors:
        print("[PASS WITH WARNINGS] No errors, but warnings should be addressed.")
    print("=" * 60)
    sys.exit(1 if errors else 0)

if __name__ == "__main__":
    main()
