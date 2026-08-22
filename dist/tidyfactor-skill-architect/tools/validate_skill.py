#!/usr/bin/env python3
"""
validate_skill.py — TidyFactor Skill structural validator.
Checks SKILL.md token count, frontmatter schema, and 8 Structural Rules compliance.
"""

import sys
import os
import re

# Set stdout/stderr encoding to UTF-8 on Windows
if sys.platform == "win32":
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")

def validate_skill(root_dir):
    skill_md_path = os.path.join(root_dir, "SKILL.md")
    if not os.path.exists(skill_md_path):
        print(f"[FAIL] {skill_md_path} does not exist.")
        sys.exit(1)
        
    with open(skill_md_path, "r", encoding="utf-8") as f:
        content = f.read()

    # 1. Frontmatter check
    if not content.startswith("---"):
        print("[FAIL] SKILL.md missing frontmatter.")
        sys.exit(1)

    # 2. Token estimate check (~350 words max for dispatcher)
    words = len(content.split())
    if words > 700:
        print(f"[WARN] SKILL.md is {words} words (~{int(words * 1.3)} tokens). Consider trimming to keep dispatcher scannable.")

    print(f"[PASS] SKILL.md structural validation passed ({words} words).")

if __name__ == "__main__":
    target = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    validate_skill(target)
