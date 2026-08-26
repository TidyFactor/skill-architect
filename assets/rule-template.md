# Rule Template: <prefix>-<rule-name>

<!-- Template for authoring deterministic, agent-consumable operational rules within TidyFactor skills -->

**Rule ID**: `<prefix>-<rule-slug>` (e.g. `async-cheap-condition-before-await`, `sec-rsc-service-role`)  
**Impact Tier**: `<CRITICAL | HIGH | MEDIUM-HIGH | MEDIUM | LOW-MEDIUM | LOW>`  
**Domain / Subsystem**: `<Subsystem or Category>`  
**Target Runtimes**: `<React 19 | Next.js 16 | TypeScript | Postgres | Node.js | Python>`

---

## 1. Problem & Rationale
<!-- 1-2 concise sentences explaining why the anti-pattern is detrimental (performance, security, correctness) -->
Brief statement of the defect or inefficiency. Explain the exact mechanism (e.g., causes full sequential network latency, triggers full component re-render, leaks credentials across bundle boundary).

---

## 2. Anti-Pattern (❌ Incorrect)
<!-- Minimal, realistic code snippet demonstrating the violation -->

```typescript
// ❌ Incorrect: [Explain what is wrong in 1 line]
const flag = await getFeatureFlag('expensive_key');
if (flag && isLocalConditionTrue) {
  executeAction();
}
```

---

## 3. Optimal Pattern (✅ Correct)
<!-- Drop-in compliant replacement demonstrating the fix -->

```typescript
// ✅ Correct: [Explain the fix in 1 line]
if (isLocalConditionTrue) {
  const flag = await getFeatureFlag('expensive_key');
  if (flag) executeAction();
}
```

---

## 4. Edge Cases & Boundary Constraints
<!-- Specific exceptions or nuances where this rule must NOT be applied or requires special care -->
- **Exception 1**: Do NOT apply if `isLocalConditionTrue` depends on the output of `getFeatureFlag()`.
- **Exception 2**: If side-effects must execute in an unalterable sequence, maintain original execution order.
- **Safety Boundary**: Automated application must be verified against the skill's Safe Optimizations / Safety Boundary matrix.
