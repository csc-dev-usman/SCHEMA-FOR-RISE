# Rise Homepage Truth Fingerprint Lock V1.0

**Status:** `TRUTH_PACK_HOMEPAGE_SCOPED_REFERENCE_ADDED_NO_SCHEMA_OUTPUT`

---

## Purpose

This document records the locked fingerprint for the homepage scoped Phase 0 schema truth view. The fingerprint allows operators and validators to verify that the truth-view reference in use is current and has not been superseded by a Phase 0 update that would require a new truth-pack derivation.

---

## Locked fingerprint

```
80edd829806cae271242c6a8e853edabdb8b2f16ca5a8fa1a3fc69ff5b78d53d
```

---

## Algorithm

SHA-256

---

## Scope

This fingerprint is scoped to:
- **Page:** homepage
- **Route:** `/`
- **Schema profile:** `HOMEPAGE_SCHEMA_PROFILE`
- **Truth-view artifact:** `RISE_PHASE0_SCHEMA_TRUTH_VIEW_HOMEPAGE_SCOPED_V1_0.json`
- **Source:** Locked from governed Rise schema lane reference

---

## What the fingerprint authorizes

The presence of a matching fingerprint confirms that:
- The homepage scoped truth-view reference is current as of this PR
- Schema operators may proceed to the next gate (evidence map, then schema profile) once later PRs provide those components
- The truth-view has not been superseded by a Phase 0 update requiring re-derivation

---

## What the fingerprint does not authorize

The fingerprint alone does not authorize:
- JSON-LD draft generation
- Production schema output
- Current website implementation
- Astro attachment
- Proceeding without a confirmed evidence map
- Proceeding without an approved schema profile
- Any held field to be emitted in schema

---

## Mismatch rules

| Condition | Required action |
|-----------|----------------|
| Fingerprint in operator context does not match locked value | HOLD — do not proceed. Request a truth-pack update PR. |
| Fingerprint field is missing from truth-view artifact | HOLD — truth-view is invalid without a fingerprint. |
| Phase 0 has been updated since this fingerprint was locked | HOLD — re-derive the homepage scoped truth view and update the fingerprint in a new PR. |
| Truth-view file has been modified outside a governed PR | HARD STOP — treat as source truth integrity violation. |

---

## Freshness rules

- This fingerprint is valid as of PR #3.
- If a Phase 0 update changes any fact that affects the homepage schema truth classes, a new scoped truth view must be derived and a new fingerprint locked in a governing truth-pack update PR.
- Operators must not proceed with schema drafting if the fingerprint cannot be verified.
- Missing or stale truth source requires HOLD.

---

## Next dependency

Later PRs must add the following before schema drafting can begin:

| Dependency | Status | Expected PR |
|-----------|--------|-------------|
| Homepage evidence map | NOT_YET_CREATED | Later PR |
| HOMEPAGE_SCHEMA_PROFILE | NOT_YET_CREATED | PR #4 |
| Operator prompts | NOT_YET_CREATED | PR #4 |
| Validators | NOT_YET_CREATED | PR #5 |
| Final runnable handoff | NOT_YET_CREATED | PR #5 |
