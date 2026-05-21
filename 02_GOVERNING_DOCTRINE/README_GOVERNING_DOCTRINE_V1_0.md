# Governing Doctrine — Rise FC Standalone Schema Operator Package

**Folder status:** `PR_2_DOCTRINE_BOUNDARY_ONLY`

---

## Purpose

This folder contains the governing doctrine for the Rise FC standalone schema operator package. It defines how the package relates to Rise Phase 0 factual truth, generated schema truth views, approved page evidence, schema profile decisions, and downstream implementation lanes.

This folder does not contain schema output. It does not contain truth pack files. It does not contain operator prompts or validators. Those are added in later PRs.

---

## What this folder contains (PR #2)

| File | Purpose |
|------|---------|
| `RISE_SCHEMA_SOURCE_TRUTH_BOUNDARY_V1_0.md` | Defines the source-truth hierarchy and what each layer owns. Hard boundaries and stop conditions. |
| `RISE_SCHEMA_GOVERNING_DOCTRINE_V1_0.md` | Main operating doctrine. Evidence-first rule, no-invention rule, lane ownership summary, blocked and allowed modules. |
| `RISE_SCHEMA_OPERATOR_LANE_OWNERSHIP_V1_0.md` | Defines which lane owns which actions. Cross-lane prohibitions and required handoffs. |
| `RISE_SCHEMA_NON_AUTHORIZATION_AND_HOLD_RULES_V1_0.md` | What PR #2 authorizes and does not authorize. Mandatory hold conditions. Blocked field and module categories. |

---

## What this folder does not contain

- Schema output or JSON-LD files
- Truth pack JSON files or generated Phase 0 truth views
- Homepage scoped truth derivations or evidence maps
- Schema profiles
- Operator prompts
- Validators
- Smoke tests
- Sample runs or run artifacts

Truth pack files come in PR #3.
Operator prompts and machine rules come in PR #4.
Validators, smoke tests, and the final runnable handoff come in PR #5.

---

## Recommended reading order

1. `RISE_SCHEMA_SOURCE_TRUTH_BOUNDARY_V1_0.md`
2. `RISE_SCHEMA_GOVERNING_DOCTRINE_V1_0.md`
3. `RISE_SCHEMA_OPERATOR_LANE_OWNERSHIP_V1_0.md`
4. `RISE_SCHEMA_NON_AUTHORIZATION_AND_HOLD_RULES_V1_0.md`
