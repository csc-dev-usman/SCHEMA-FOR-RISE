# Runtime Appendix Schema Carry Field Reference V1.0

**Status:** `RUNTIME_APPENDIX_SCHEMA_CARRY_FIELD_REFERENCE_ADDED_NO_SCHEMA_OUTPUT`

> This document defines the Runtime Appendix schema carry fields. These are the metadata fields that must be populated before any approved schema output bundle may be carried into HTML/runtime/Astro workflows. This is a reference document only — no Runtime Appendix has been populated, no carry has occurred, and no schema output exists. Mode 2 is not ready.

---

## Purpose

The Runtime Appendix is the metadata bridge between the SEO/schema operator lane and the implementation lane (HTML/runtime/Astro). It records the identity, approval state, and carry eligibility of a governed schema output bundle — and serves as the authoritative source for whether schema may be carried and attached to a target route.

The Runtime Appendix does not author schema. It does not generate schema. It does not modify schema. It carries the identity and approval record of schema that was produced entirely within the governed operator lane.

---

## Governing principle

> Runtime/HTML/Astro workflows may only read the Runtime Appendix to determine carry eligibility. They may not write schema values into the appendix. They may not invent or normalize schema fields. They may not override or repair schema. The SEO/schema operator lane is the sole authoring lane for all schema fields.

---

## Required carry field definitions

The following 18 fields must all be present and confirmed before Gate 4 (Runtime Appendix carry fields complete) in the Astro carry gate sequence.

All fields default to `NOT_STARTED` until a governed operator run completes and a validated output bundle is approved.

---

### Field 1 — `schema_bundle_id`

| Attribute | Value |
|-----------|-------|
| Type | string |
| Required | YES |
| Format | `RISE_RUN_<PAGE_FAMILY>_<DATE_YYYYMMDD>_<SEQ>` |
| Description | The unique run ID of the approved schema output bundle. Must match the `runId` field in the output bundle manifest and the `RUN_LEDGER.json` entry. Used at Gate 6 Check 1 to verify bundle identity. |
| Current status | NOT_STARTED — no output bundle exists |
| Allowed statuses | NOT_STARTED, PENDING, PASS, FAIL |

---

### Field 2 — `schema_export_id`

| Attribute | Value |
|-----------|-------|
| Type | string |
| Required | YES |
| Format | `RISE_EXPORT_<PAGE_FAMILY>_<DATE_YYYYMMDD>_<SEQ>` |
| Description | The unique export ID for this carry operation. Generated at the time the schema output bundle is approved for carry. Must be unique across all carry operations. Used at Gate 6 Check 2. |
| Current status | NOT_STARTED — no governed run has completed |
| Allowed statuses | NOT_STARTED, PENDING, PASS, FAIL |

---

### Field 3 — `schema_owner`

| Attribute | Value |
|-----------|-------|
| Type | string enum |
| Required | YES |
| Required value | `SEO_SCHEMA_OPERATOR` |
| Description | The lane that owns and authored the schema. Must always be `SEO_SCHEMA_OPERATOR`. Runtime/HTML/Astro is never the owner. This field is set by the operator lane at bundle creation and may not be modified by any downstream lane. |
| Current status | NOT_STARTED |
| Allowed values | `SEO_SCHEMA_OPERATOR` (only) |

---

### Field 4 — `schema_source_lane`

| Attribute | Value |
|-----------|-------|
| Type | string enum |
| Required | YES |
| Required value | `SEO_SCHEMA_EXPORT` |
| Description | The lane from which the schema output was exported. Must always be `SEO_SCHEMA_EXPORT`. Identifies that the schema bundle was produced by the governed SEO/schema operator workflow, not by runtime, CMS, or Astro. |
| Current status | NOT_STARTED |
| Allowed values | `SEO_SCHEMA_EXPORT` (only) |

---

### Field 5 — `target_route`

| Attribute | Value |
|-----------|-------|
| Type | string |
| Required | YES |
| Format | Route path starting with `/` (e.g., `/`) |
| Description | The URL route for which the schema output was produced. Must exactly match the Astro route. Used at Gate 6 Check 3. For the first governed run, this will be `/` (homepage). |
| Current status | NOT_STARTED |
| Allowed statuses | NOT_STARTED, PENDING, PASS, FAIL |

---

### Field 6 — `page_family`

| Attribute | Value |
|-----------|-------|
| Type | string |
| Required | YES |
| Example value | `HOMEPAGE` |
| Description | The page family category for the target route. Must match the page family in the output bundle manifest. Used at Gate 6 Check 4. For the first governed run, this will be `HOMEPAGE`. |
| Current status | NOT_STARTED |
| Allowed statuses | NOT_STARTED, PENDING, PASS, FAIL |

---

### Field 7 — `schema_profile_expected`

| Attribute | Value |
|-----------|-------|
| Type | string |
| Required | YES |
| Example value | `HOMEPAGE_SCHEMA_PROFILE` |
| Description | The schema profile that was expected at run intake. Must match the profile that was approved before drafting began. Used at Gate 6 Check 5 (expected vs. actual). |
| Current status | NOT_STARTED |
| Allowed statuses | NOT_STARTED, PENDING, PASS, FAIL |

---

### Field 8 — `schema_profile_actual`

| Attribute | Value |
|-----------|-------|
| Type | string |
| Required | YES |
| Example value | `HOMEPAGE_SCHEMA_PROFILE` |
| Description | The schema profile that was actually used to produce the output bundle. Must exactly match `schema_profile_expected`. A mismatch triggers `HOLD_SCHEMA_PROFILE_MISMATCH`. Used at Gate 6 Check 5. |
| Current status | NOT_STARTED |
| Allowed statuses | NOT_STARTED, PENDING, PASS, FAIL |

---

### Field 9 — `schema_validation_gate_status`

| Attribute | Value |
|-----------|-------|
| Type | string enum |
| Required | YES |
| Description | The result of the 9-step final schema validation protocol (`FINAL_SCHEMA_VALIDATION_PROTOCOL_V1_0.md`). Must be `PASS` before Gate 8. A `FAIL` or `WARN` blocks carry. Used at Gate 6 Check 8. |
| Current status | NOT_STARTED |
| Allowed statuses | NOT_STARTED, PENDING, PASS, WARN, FAIL |

---

### Field 10 — `schema_evidence_map_status`

| Attribute | Value |
|-----------|-------|
| Type | string enum |
| Required | YES |
| Description | The status of the evidence map for the target route. Must be `PASS` — confirming that all schema fields trace to Phase 0 or confirmed page evidence. A `FAIL` or `HOLD` blocks carry. Used at Gate 6 Check 7. |
| Current status | NOT_STARTED |
| Allowed statuses | NOT_STARTED, PENDING, PASS, WARN, FAIL, HOLD |

---

### Field 11 — `schema_truth_fingerprint_status`

| Attribute | Value |
|-----------|-------|
| Type | string enum |
| Required | YES |
| Description | Whether the truth fingerprint of the output bundle matches the locked Phase 0 homepage fingerprint (`80edd829806cae271242c6a8e853edabdb8b2f16ca5a8fa1a3fc69ff5b78d53d`). Must be `PASS`. A mismatch triggers `HOLD_TRUTH_FINGERPRINT_MISMATCH`. Used at Gate 6 Check 6. |
| Current status | NOT_STARTED |
| Allowed statuses | NOT_STARTED, PENDING, PASS, FAIL |

---

### Field 12 — `schema_attach_eligible`

| Attribute | Value |
|-----------|-------|
| Type | string enum |
| Required | YES |
| Description | Whether the schema output bundle is eligible for Astro attachment — all 8 carry gates have been confirmed, all identity match checks have passed, no hold codes are active. Must be `ATTACH_ELIGIBLE` before Gate 8. |
| Current status | NOT_ATTACH_ELIGIBLE — no gates have passed |
| Allowed statuses | NOT_STARTED, NOT_ATTACH_ELIGIBLE, ATTACH_ELIGIBLE |

---

### Field 13 — `schema_attach_status`

| Attribute | Value |
|-----------|-------|
| Type | string enum |
| Required | YES |
| Description | Whether schema has been attached to the Astro route. Starts as `NOT_ATTACHED`. Set to `ATTACHED` only after Gate 8 completes and human approval is confirmed. |
| Current status | NOT_ATTACHED |
| Allowed statuses | NOT_STARTED, NOT_ATTACHED, ATTACHED |

---

### Field 14 — `schema_hold_reasons`

| Attribute | Value |
|-----------|-------|
| Type | array of strings |
| Required | YES |
| Description | List of active hold codes that are blocking schema carry. All 15 hold codes from `ASTRO_SCHEMA_CARRY_HOLD_REASON_REFERENCE_V1_0.md` are active by default. Must be empty (`[]`) before Gate 8. |
| Current status | All 15 hold codes active |
| Allowed values | Hold code strings from `ASTRO_SCHEMA_CARRY_HOLD_REASON_REFERENCE_V1_0.md` |

---

### Field 15 — `controller_decision_status`

| Attribute | Value |
|-----------|-------|
| Type | string enum |
| Required | YES |
| Description | The final recommendation from the controller review. Must be `APPROVED` with `unresolvedBlockers: 0` before Gates 2 and Gate 6 Check 9. A value of `PATCH_REQUIRED`, `REJECT_RUN`, or `HUMAN_REVIEW_REQUIRED` blocks carry. |
| Current status | NOT_STARTED |
| Allowed statuses | NOT_STARTED, PENDING, APPROVED, NOT_APPROVED |

---

### Field 16 — `human_approval_status`

| Attribute | Value |
|-----------|-------|
| Type | string enum |
| Required | YES |
| Description | Whether explicit human approval for schema carry has been granted. Must be `APPROVED` with a valid `humanApprovalRef` before Gates 3 and Gate 6 Check 10. Human approval is required and cannot be self-granted by Claude, a validator, or any automated process. |
| Current status | NOT_STARTED |
| Allowed statuses | NOT_STARTED, PENDING, APPROVED, NOT_APPROVED |

---

### Field 17 — `astro_route_manifest_status`

| Attribute | Value |
|-----------|-------|
| Type | string enum |
| Required | YES |
| Description | Whether a confirmed Astro route manifest is available for the target route. Must be `PASS` before Gate 5. The route manifest confirms that an actual Astro route exists at the target path. Cannot be self-resolved by schema or operator tooling — requires real Astro route evidence. |
| Current status | NOT_STARTED — no Astro route manifest exists |
| Allowed statuses | NOT_STARTED, PENDING, PASS, FAIL, NOT_APPLICABLE |

---

### Field 18 — `runtime_appendix_status`

| Attribute | Value |
|-----------|-------|
| Type | string enum |
| Required | YES |
| Description | The overall status of the Runtime Appendix for this carry operation. `NOT_STARTED` until all 18 fields are populated and confirmed. `PASS` when all fields meet their required values and no hold codes are active. Used at Gate 4 to confirm the appendix is complete. |
| Current status | NOT_STARTED — appendix is a reference only; no governed run has completed |
| Allowed statuses | NOT_STARTED, PENDING, PASS, WARN, FAIL, HOLD |

---

## Field summary table

| Field | Required value / format | Current status | Blocks gate |
|-------|------------------------|----------------|-------------|
| `schema_bundle_id` | `RISE_RUN_*` format | NOT_STARTED | Gate 1, Gate 6 Check 1 |
| `schema_export_id` | `RISE_EXPORT_*` format | NOT_STARTED | Gate 6 Check 2 |
| `schema_owner` | `SEO_SCHEMA_OPERATOR` | NOT_STARTED | Gate 6 |
| `schema_source_lane` | `SEO_SCHEMA_EXPORT` | NOT_STARTED | Gate 6 |
| `target_route` | `/` (homepage) | NOT_STARTED | Gate 6 Check 3 |
| `page_family` | `HOMEPAGE` | NOT_STARTED | Gate 6 Check 4 |
| `schema_profile_expected` | `HOMEPAGE_SCHEMA_PROFILE` | NOT_STARTED | Gate 6 Check 5 |
| `schema_profile_actual` | `HOMEPAGE_SCHEMA_PROFILE` | NOT_STARTED | Gate 6 Check 5 |
| `schema_validation_gate_status` | `PASS` | NOT_STARTED | Gate 6 Check 8 |
| `schema_evidence_map_status` | `PASS` | NOT_STARTED | Gate 6 Check 7 |
| `schema_truth_fingerprint_status` | `PASS` | NOT_STARTED | Gate 6 Check 6 |
| `schema_attach_eligible` | `ATTACH_ELIGIBLE` | NOT_ATTACH_ELIGIBLE | Gate 8 |
| `schema_attach_status` | `NOT_ATTACHED` → `ATTACHED` | NOT_ATTACHED | Gate 8 |
| `schema_hold_reasons` | `[]` (empty) | 15 codes active | Gate 8 |
| `controller_decision_status` | `APPROVED` | NOT_STARTED | Gates 2, 6 Check 9 |
| `human_approval_status` | `APPROVED` | NOT_STARTED | Gates 3, 6 Check 10 |
| `astro_route_manifest_status` | `PASS` | NOT_STARTED | Gate 5 |
| `runtime_appendix_status` | `PASS` | NOT_STARTED | Gate 4 |

---

## Carry field population sequence

These fields are not populated in arbitrary order. The governed sequence is:

1. A governed operator run completes and a validated output bundle is produced → `schema_bundle_id` and `schema_export_id` become available
2. Evidence map is confirmed → `schema_evidence_map_status: PASS`
3. Final validation protocol passes → `schema_validation_gate_status: PASS`
4. Truth fingerprint verified → `schema_truth_fingerprint_status: PASS`
5. Controller review completes → `controller_decision_status: APPROVED`
6. Human approval granted → `human_approval_status: APPROVED`
7. Astro route manifest confirmed → `astro_route_manifest_status: PASS`
8. All hold codes clear → `schema_hold_reasons: []`
9. `schema_attach_eligible: ATTACH_ELIGIBLE` — all Gate 6 checks pass
10. `runtime_appendix_status: PASS` — Gate 4 confirmed
11. Gate 8: Astro attachment occurs → `schema_attach_status: ATTACHED`

---

## Non-authorization statement

This document does not authorize:
- Schema output
- JSON-LD generation
- Evidence map creation
- Astro attachment
- Runtime code creation
- Current website implementation
- Production lock

No Runtime Appendix record has been populated. No carry has occurred. No schema output exists. Mode 2 is not ready.
