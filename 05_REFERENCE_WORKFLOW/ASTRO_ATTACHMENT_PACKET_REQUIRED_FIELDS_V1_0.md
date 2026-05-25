# Astro Attachment Packet Required Fields V1.0

**Status:** `ASTRO_ATTACHMENT_PACKET_TEMPLATE_ADDED_NO_SCHEMA_OUTPUT`

> This document defines the required fields, allowed statuses, and validation constraints for a future Astro attachment packet. No real packet has been created. No schema has been attached. No schema output exists. Mode 2 is not ready.

---

## Purpose

This document is the authoritative field contract for the Astro attachment packet. It defines what each field must contain, what values are allowed, what gate each field governs, and what hold code is triggered by a failure.

---

## Required fields

### `packet_id`

| Property | Value |
|----------|-------|
| Type | String |
| Required | Yes |
| Format | `RISE_ATTACH_<PAGE_FAMILY>_<DATE_YYYYMMDD>_<SEQ>` |
| Default | `PLACEHOLDER_PACKET_ID` |
| Allowed statuses | N/A — free-form unique identifier |
| Gate | Must be present before packet is submitted for review |
| Failure | Packet rejected — no ID, no packet |

---

### `target_route`

| Property | Value |
|----------|-------|
| Type | String |
| Required | Yes |
| Format | Route path starting with `/` |
| Example | `/` |
| Default | `NOT_STARTED` |
| Allowed statuses | `NOT_STARTED`, `PENDING`, `PASS`, `FAIL` |
| Gate | Must be `PASS` — confirmed from Astro route manifest |
| Failure hold code | `HOLD_ROUTE_IDENTITY_MISMATCH` |

---

### `page_family`

| Property | Value |
|----------|-------|
| Type | String |
| Required | Yes |
| Example | `HOMEPAGE` |
| Default | `NOT_STARTED` |
| Allowed statuses | `NOT_STARTED`, `PENDING`, `PASS`, `FAIL` |
| Gate | Must be `PASS` — must match `page_family` in output bundle manifest |
| Failure hold code | `HOLD_PAGE_FAMILY_MISMATCH` |

---

### `schema_bundle_id`

| Property | Value |
|----------|-------|
| Type | String |
| Required | Yes |
| Format | `RISE_RUN_<PAGE_FAMILY>_<DATE_YYYYMMDD>_<SEQ>` |
| Default | `NOT_STARTED` |
| Allowed statuses | `NOT_STARTED`, `PENDING`, `PASS`, `FAIL` |
| Gate | Must be `PASS` — confirmed from output bundle manifest and `RUN_LEDGER.json` |
| Failure hold code | `HOLD_SCHEMA_BUNDLE_MISSING` |

---

### `schema_export_id`

| Property | Value |
|----------|-------|
| Type | String |
| Required | Yes |
| Format | `RISE_EXPORT_<PAGE_FAMILY>_<DATE_YYYYMMDD>_<SEQ>` |
| Default | `NOT_STARTED` |
| Allowed statuses | `NOT_STARTED`, `PENDING`, `PASS`, `FAIL` |
| Gate | Must be `PASS` — unique across all carry operations |
| Failure hold code | `HOLD_SCHEMA_EXPORT_ID_MISSING` |

---

### `schema_owner`

| Property | Value |
|----------|-------|
| Type | String |
| Required | Yes |
| Required value | `SEO_SCHEMA_OPERATOR` |
| Allowed values | `SEO_SCHEMA_OPERATOR` only |
| May NOT be set by | Astro, runtime, CMS, or any non-operator lane |
| Gate | Must equal `SEO_SCHEMA_OPERATOR` |
| Failure | Packet rejected — schema owner violation |

---

### `source_lane`

| Property | Value |
|----------|-------|
| Type | String |
| Required | Yes |
| Required value | `SEO_SCHEMA_EXPORT` |
| Allowed values | `SEO_SCHEMA_EXPORT` only |
| Gate | Must equal `SEO_SCHEMA_EXPORT` |
| Failure | Packet rejected — source lane violation |

---

### `schema_profile_expected`

| Property | Value |
|----------|-------|
| Type | String |
| Required | Yes |
| Example | `HOMEPAGE_SCHEMA_PROFILE` |
| Default | `NOT_STARTED` |
| Allowed statuses | `NOT_STARTED`, `PENDING`, `PASS`, `FAIL` |
| Gate | Must be `PASS` — must match the approved profile at run intake |
| Failure hold code | `HOLD_SCHEMA_PROFILE_MISMATCH` |

---

### `schema_profile_actual`

| Property | Value |
|----------|-------|
| Type | String |
| Required | Yes |
| Example | `HOMEPAGE_SCHEMA_PROFILE` |
| Default | `NOT_STARTED` |
| Allowed statuses | `NOT_STARTED`, `PENDING`, `PASS`, `FAIL` |
| Constraint | Must exactly match `schema_profile_expected` |
| Gate | Must be `PASS` — mismatch triggers hold |
| Failure hold code | `HOLD_SCHEMA_PROFILE_MISMATCH` |

---

### `truth_fingerprint`

| Property | Value |
|----------|-------|
| Type | String |
| Required | Yes |
| Locked value | `80edd829806cae271242c6a8e853edabdb8b2f16ca5a8fa1a3fc69ff5b78d53d` |
| Default | `NOT_STARTED` |
| Allowed statuses | `NOT_STARTED`, `PENDING`, `PASS`, `FAIL` |
| Gate | Must be `PASS` — output bundle fingerprint must match locked Phase 0 fingerprint |
| Failure hold code | `HOLD_TRUTH_FINGERPRINT_MISMATCH` |

---

### `evidence_map_status`

| Property | Value |
|----------|-------|
| Type | String |
| Required | Yes |
| Default | `NOT_STARTED` |
| Allowed values | `NOT_STARTED`, `PENDING`, `PASS`, `WARN`, `FAIL`, `HOLD` |
| Gate | Must be `PASS` — all schema fields must trace to Phase 0 or confirmed page evidence |
| Failure hold code | `HOLD_EVIDENCE_MAP_NOT_PASSED` |

---

### `validation_status`

| Property | Value |
|----------|-------|
| Type | String |
| Required | Yes |
| Default | `NOT_STARTED` |
| Allowed values | `NOT_STARTED`, `PENDING`, `PASS`, `WARN`, `FAIL` |
| Gate | Must be `PASS` — 9-step final schema validation protocol must complete |
| Failure hold code | `HOLD_VALIDATION_GATE_NOT_PASSED` |

---

### `controller_decision_status`

| Property | Value |
|----------|-------|
| Type | String |
| Required | Yes |
| Default | `NOT_STARTED` |
| Allowed values | `NOT_STARTED`, `PENDING`, `APPROVED`, `NOT_APPROVED` |
| Constraint | `APPROVED` requires `unresolvedBlockers: 0` in controller review packet |
| Gate | Must be `APPROVED` with zero unresolved blockers |
| Failure hold code | `HOLD_CONTROLLER_APPROVAL_MISSING` |

---

### `human_approval_status`

| Property | Value |
|----------|-------|
| Type | String |
| Required | Yes |
| Default | `NOT_APPROVED` |
| Allowed values | `NOT_STARTED`, `PENDING`, `APPROVED`, `NOT_APPROVED` |
| Constraint | `APPROVED` requires a non-empty `humanApprovalRef` string; cannot be self-granted by Claude or automated tooling |
| Gate | Must be `APPROVED` with valid ref |
| Failure hold code | `HOLD_HUMAN_APPROVAL_MISSING` |

---

### `runtime_appendix_status`

| Property | Value |
|----------|-------|
| Type | String |
| Required | Yes |
| Default | `NOT_STARTED` |
| Allowed values | `NOT_STARTED`, `PENDING`, `PASS`, `WARN`, `FAIL`, `HOLD` |
| Gate | Must be `PASS` — all 18 Runtime Appendix carry fields confirmed |
| Failure hold code | `HOLD_ASTRO_RUNTIME_APPENDIX_MISSING` |

---

### `astro_route_manifest_status`

| Property | Value |
|----------|-------|
| Type | String |
| Required | Yes |
| Default | `NOT_STARTED` |
| Allowed values | `NOT_STARTED`, `PENDING`, `PASS`, `FAIL`, `NOT_APPLICABLE` |
| Constraint | Cannot be self-resolved — requires real Astro route evidence |
| Gate | Must be `PASS` |
| Failure hold code | `HOLD_ASTRO_ROUTE_MISSING` |

---

### `attach_eligibility_status`

| Property | Value |
|----------|-------|
| Type | String |
| Required | Yes |
| Default | `NOT_ATTACH_ELIGIBLE` |
| Allowed values | `NOT_STARTED`, `NOT_ATTACH_ELIGIBLE`, `ATTACH_ELIGIBLE` |
| Gate | Must be `ATTACH_ELIGIBLE` — all 8 carry gates must pass, no hold codes active |
| Failure | `final_attachment_decision` may not be `APPROVED` |

---

### `hold_reasons`

| Property | Value |
|----------|-------|
| Type | Array of strings |
| Required | Yes |
| Default | `HOLD` (all 15 hold codes active by default) |
| Constraint | Must be empty (`[]`) before `final_attachment_decision` may be `APPROVED` |
| Gate | Must be empty at Gate 8 |
| Reference | `ASTRO_SCHEMA_CARRY_HOLD_REASON_REFERENCE_V1_0.md` |

---

### `final_attachment_decision`

| Property | Value |
|----------|-------|
| Type | String |
| Required | Yes |
| Default | `NOT_APPROVED` |
| Allowed values | `NOT_APPROVED`, `APPROVED` |
| Constraint | May only be `APPROVED` when: all fields pass, `attach_eligibility_status` is `ATTACH_ELIGIBLE`, `hold_reasons` is empty, and human owner grants explicit approval |
| May NOT be set by | Claude or automated tooling — human approval required |

---

## Field-to-gate dependency summary

| Field | Required state | Blocking gate |
|-------|---------------|---------------|
| `packet_id` | Present | Gate 8 (packet review) |
| `target_route` | `PASS` | Gate 1 (route confirmation) |
| `page_family` | `PASS` | Gate 1 |
| `schema_bundle_id` | `PASS` | Gate 2 (output bundle) |
| `schema_export_id` | `PASS` | Gate 2 |
| `schema_owner` | `SEO_SCHEMA_OPERATOR` | Gate 2 |
| `source_lane` | `SEO_SCHEMA_EXPORT` | Gate 2 |
| `schema_profile_expected` | `PASS` | Gate 6 (identity checks) |
| `schema_profile_actual` | `PASS` (= expected) | Gate 6 |
| `truth_fingerprint` | `PASS` | Gate 6 |
| `evidence_map_status` | `PASS` | Gate 3 (evidence) |
| `validation_status` | `PASS` | Gate 5 (validation) |
| `controller_decision_status` | `APPROVED` (0 blockers) | Gate 6 |
| `human_approval_status` | `APPROVED` (with ref) | Gate 7 (human approval) |
| `runtime_appendix_status` | `PASS` | Gate 4 (Runtime Appendix) |
| `astro_route_manifest_status` | `PASS` | Gate 1 |
| `attach_eligibility_status` | `ATTACH_ELIGIBLE` | Gate 8 |
| `hold_reasons` | `[]` (empty) | Gate 8 |
| `final_attachment_decision` | `APPROVED` | Gate 8 |

---

## Non-authorization statement

This document does not authorize:
- Astro schema attachment
- JSON-LD generation
- Schema output creation
- Current website implementation
- Production deployment
- Mode 2 readiness

All fields are at default/NOT_STARTED. No real packet has been created. No carry has occurred.
