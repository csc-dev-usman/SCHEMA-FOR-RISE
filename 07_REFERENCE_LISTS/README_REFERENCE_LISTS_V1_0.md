# Reference Lists — Rise FC Standalone Schema Operator Package

**Status:** `HOMEPAGE_SCHEMA_PROFILE_ADDED_NO_SCHEMA_OUTPUT`

---

## Purpose

This folder stores schema profile and reference-list policy material for the Rise FC standalone schema operator package. It defines which schema modules are allowed, which are blocked, which fields are held, and the decision logic for building schema profiles for specific pages and routes.

This folder does not contain JSON-LD. It does not generate schema. It does not authorize current website implementation. It does not authorize Astro attachment. It is policy and reference material only.

---

## PR #4 scope

PR #4 adds:
- Homepage schema profile — defines the profile ID, route, allowed modules, blocked modules, held fields, and drafting preconditions for the homepage
- Allowed future first-page module reference — per-module evidence requirements before any module may be emitted
- Blocked first-page module policy — why each module is blocked and what would be required to unblock it
- Held field category policy — default status, approval requirements, emission rule
- Schema profile decision matrix — current active profile, future profile candidates, decision inputs/outputs

This PR does not generate schema output. It does not create JSON-LD. It does not create evidence maps. It does not create operator prompts or validators.

Evidence maps, prompts, validators, output bundle schemas, and smoke tests come in later PRs.

---

## What this folder contains

| File | Purpose |
|------|---------|
| `RISE_HOMEPAGE_SCHEMA_PROFILE_V1_0.md` | Homepage schema profile — page scope, route, profile ID, allowed/blocked modules, held fields, drafting preconditions |
| `RISE_FIRST_PAGE_ALLOWED_MODULES_V1_0.md` | Allowed future first-page modules with per-module evidence requirements |
| `RISE_BLOCKED_SCHEMA_MODULES_FIRST_PAGE_V1_0.md` | Blocked first-page module policy with block reasons and exception rules |
| `RISE_HELD_FIELD_CATEGORIES_FIRST_PAGE_V1_0.md` | Held field categories — default status, approval requirements, emission rule |
| `RISE_SCHEMA_PROFILE_DECISION_MATRIX_V1_0.md` | Profile decision matrix — current active profile, future candidates, decision inputs/outputs |

---

## What this folder does not contain

- JSON-LD output files
- Schema output bundles
- Homepage JSON-LD draft
- Evidence maps
- Operator prompts
- Validators or smoke tests
- Sample runs or run artifacts
- Production schema bundles

---

## Reading order

1. `RISE_HOMEPAGE_SCHEMA_PROFILE_V1_0.md`
2. `RISE_FIRST_PAGE_ALLOWED_MODULES_V1_0.md`
3. `RISE_BLOCKED_SCHEMA_MODULES_FIRST_PAGE_V1_0.md`
4. `RISE_HELD_FIELD_CATEGORIES_FIRST_PAGE_V1_0.md`
5. `RISE_SCHEMA_PROFILE_DECISION_MATRIX_V1_0.md`

---

## Non-authorization

This folder and all files within it:
- Do not generate schema
- Do not contain JSON-LD
- Do not authorize JSON-LD output
- Do not authorize current website implementation
- Do not authorize Astro attachment
- Do not authorize production lock
- Do not mutate Rise Phase 0
- Do not approve held fields

All held fields remain held until the owner approval worksheet in `03_TRUTH_PACK/` is updated by the appropriate human owner with Phase 0 support, and a later governed PR adds the evidence map and schema profile implementation.

---

## Next expected PR

PR #5 should add the Rise standalone master flow:
`docs: add Rise standalone schema master flow`
