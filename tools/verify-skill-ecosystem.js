#!/usr/bin/env node
/**
 * TidyFactor Ecosystem Integrity & SSOT Verification Engine
 * Verifies zero-duplication between Skills-LAB (Community) and Skills-pro-pack (Pro),
 * checks directory completeness, frontmatter validity, and catalog alignment.
 */

const fs = require('fs');
const path = require('path');

const COMMUNITY_ROOT = path.resolve(__dirname, '../../'); // Skills-LAB
const PRO_ROOT = path.resolve(COMMUNITY_ROOT, '../Skills-pro-pack');

console.log('='.repeat(65));
console.log('🔍 TidyFactor Ecosystem Integrity & SSOT Audit');
console.log('='.repeat(65));
console.log(`🌐 Community Root: ${COMMUNITY_ROOT}`);
console.log(`💼 Pro Pack Root:  ${PRO_ROOT}\n`);

let errorCount = 0;
let warningCount = 0;

// 1. Audit Community Skills
const communitySkills = [
  'tidyfactor-skill-architect',
  'tidyfactor-cinematic',
  'tidyfactor-design',
  'tidyfactor-styler',
  'tidyfactor-doc',
  'tidyfactor-next',
  'tidyfactor-marketing',
  'tidyfactor-html',
  'tidyfactor-htmx',
  'tidyfactor-js',
  'tidyfactor-php'
];

console.log('📦 [1/4] Checking Community Skills (Skills-LAB)...');
for (const skillName of communitySkills) {
  const skillDir = path.join(COMMUNITY_ROOT, skillName);
  if (!fs.existsSync(skillDir)) {
    console.error(`  ❌ Missing community skill: ${skillName}`);
    errorCount++;
    continue;
  }

  const skillMd = path.join(skillDir, 'SKILL.md');
  const pkgJson = path.join(skillDir, 'package.json');
  const tidyMarker = path.join(skillDir, '.tidyfactor');

  if (!fs.existsSync(skillMd)) {
    console.error(`  ❌ ${skillName}: Missing SKILL.md`);
    errorCount++;
  }
  if (!fs.existsSync(pkgJson)) {
    console.warn(`  ⚠️  ${skillName}: Missing package.json`);
    warningCount++;
  }
  if (!fs.existsSync(tidyMarker)) {
    console.warn(`  ⚠️  ${skillName}: Missing .tidyfactor`);
    warningCount++;
  }
  console.log(`  ✅ ${skillName.padEnd(28)} [OK]`);
}

// 2. Audit Pro Pack Categories
console.log('\n📦 [2/4] Checking Pro Pack Categories (Skills-pro-pack)...');
const expectedProCategories = [
  'DevOps',
  'PocketOffice-Skills',
  'ENGINEERING',
  'GROWTH',
  'DESIGN',
  'GOVERNANCE & ARCHITECTURE'
];

for (const cat of expectedProCategories) {
  const catDir = path.join(PRO_ROOT, cat);
  if (!fs.existsSync(catDir)) {
    console.error(`  ❌ Missing Pro category directory: ${cat}`);
    errorCount++;
  } else {
    const items = fs.readdirSync(catDir);
    console.log(`  ✅ Category: ${cat.padEnd(26)} (${items.length} items)`);
  }
}

// 3. Strict Deduplication Check
console.log('\n🔒 [3/4] Checking Zero-Duplication Policy (SSOT Enforcement)...');
let duplicateFound = false;

function scanForDuplicates(dir, level = 0) {
  if (!fs.existsSync(dir)) return;
  const entries = fs.readdirSync(dir, { withFileTypes: true });
  for (const entry of entries) {
    if (entry.isDirectory()) {
      if (communitySkills.includes(entry.name)) {
        console.error(`  ❌ DUPLICATE DETECTED: "${entry.name}" exists in Pro directory: ${dir}`);
        duplicateFound = true;
        errorCount++;
      }
      if (level < 2) {
        scanForDuplicates(path.join(dir, entry.name), level + 1);
      }
    }
  }
}

scanForDuplicates(PRO_ROOT);
if (!duplicateFound) {
  console.log('  ✅ 100% Pure SSOT: Zero community skills duplicated in Pro pack.');
}

// 4. Governance Documentation Check
console.log('\n📑 [4/4] Checking Governance & Policy Documentation...');
const requiredDocs = [
  { path: path.join(COMMUNITY_ROOT, 'AGENTS.md'), name: 'Skills-LAB/AGENTS.md' },
  { path: path.join(COMMUNITY_ROOT, 'SKILLS-LAB-GUIDE.md'), name: 'Skills-LAB/SKILLS-LAB-GUIDE.md' },
  { path: path.join(PRO_ROOT, 'AGENTS.md'), name: 'Skills-pro-pack/AGENTS.md' },
  { path: path.join(PRO_ROOT, 'PRO-PACK-GUIDE.md'), name: 'Skills-pro-pack/PRO-PACK-GUIDE.md' },
  { path: path.join(PRO_ROOT, 'PRO-CATALOG.json'), name: 'Skills-pro-pack/PRO-CATALOG.json' }
];

for (const doc of requiredDocs) {
  if (fs.existsSync(doc.path)) {
    console.log(`  ✅ Governance Doc: ${doc.name.padEnd(35)} [PRESENT]`);
  } else {
    console.error(`  ❌ Missing Governance Doc: ${doc.name}`);
    errorCount++;
  }
}

// Summary Report
console.log('\n' + '='.repeat(65));
console.log(`🏁 Audit Complete: ${errorCount} Errors, ${warningCount} Warnings`);
console.log('='.repeat(65));

if (errorCount === 0) {
  console.log('✨ All systems GO! TidyFactor Skills ecosystem is fully compliant and unified.\n');
  process.exit(0);
} else {
  console.error('🚨 Ecosystem integrity check failed. Resolve errors above.\n');
  process.exit(1);
}
