# Runtime Appendix Schema Carry Field Status Enums V1.0

**Status:** `RUNTIME_APPENDIX_SCHEMA_CARRY_FIELD_REFERENCE_ADDED_NO_SCHEMA_OUTPUT`

> This document defines all allowed status enum values for Runtime Appendix schema carry fields. These are the only valid values for status-type fields in the Runtime Appendix. This is a reference document only — no Runtime Appendix has been populated, no carry has occurred, and no schema output exists. Mode 2 is not ready.

---

## Purpose

Each status-type field in the Runtime Appendix (`RUNTIME_APPENDIX_SCHEMA_CARRY_FIELD_REFERENCE_V1_0.md`) accepts a limited set of allowed enum values. This document defines what each value means, when it may be used, and which fields it applies to.

No status value may be set outside this defined set. No field may accept a value not listed in its allowed statuses.

---

## Enum definitions

### `NOT_STARTED`

| Attribute | Value |
|-----------|-------|
| Meaning | The field has not been assessed or populated. Default state for all fields at package bootstrap and before any governed run begins. |
| Applies to | All 18 Runtime Appendix carry fields |
| May be set by | Package initialization; initial carry field record creation |
| May not be set by | Automated carry tooling (carry tooling may only move fields forward from NOT_STARTED, never back to it) |
| Gate implication | Any field at NOT_STARTED blocks the gate that depends on it |

---

### `NOT_APPLICABLE`

| Attribute | Value |
|-----------|-------|
| Meaning | The field does not apply to this particular carry operation or route. For example, `astro_route_manifest_status` may be NOT_APPLICABLE if the carry target is the current website only (Mode 1) and Astro carry is not being attempted. |
| Applies to | `astro_route_manifest_status` and fields that may not apply in certain carry configurations |
| May be set by | Controller, after confirming the field is genuinely not applicable |
| Gate implication | A NOT_APPLICABLE value does not block carry if the governing document explicitly allows it for that field |

---

### `PENDING`

| Attribute | Value |
|-----------|-------|
| Meaning | The field has been initiated but assessment or confirmation is in progress. Used when a governed operator run is underway or when a carry field check has started but not yet completed. |
| Applies to | All status-type fields |
| May be set by | Operator tooling during active governed run |
| Gate implication | PENDING blocks the gate that depends on this field |

---

### `PASS`

| Attribute | Value |
|-----------|-------|
| Meaning | The field has been assessed and fully confirmed. The value meets all governing requirements — identity match, fingerprint match, validation pass, evidence pass, or other field-specific confirmation. |
| Applies to | `schema_bundle_id`, `schema_export_id`, `target_route`, `page_family`, `schema_profile_expected`, `schema_profile_actual`, `schema_validation_gate_status`, `schema_evidence_map_status`, `schema_truth_fingerprint_status`, `astro_route_manifest_status`, `runtime_appendix_status` |
| May be set by | Operator after confirmed assessment; controller after review |
| Gate implication | PASS satisfies the gate check for that field |

---

### `WARN`

| Attribute | Value |
|-----------|-------|
| Meaning | The field assessment completed but returned a non-blocking warning. The carry is not blocked but the warning must be acknowledged by the controller before proceeding. |
| Applies to | `schema_validation_gate_status`, `schema_evidence_map_status`, `runtime_appendix_status` |
| May be set by | Validation tooling; controller review |
| Gate implication | WARN requires controller acknowledgment; does not automatically block carry but must be reviewed |

---

### `FAIL`

| Attribute | Value |
|-----------|-------|
| Meaning | The field assessment completed and returned a blocking failure. The carry is blocked until the underlying issue is resolved and the field is reassessed. |
| Applies to | All status-type fields |
| May be set by | Validation tooling; controller review |
| Gate implication | FAIL blocks all downstream gates. The failing field must be remediated and re-assessed before carry may proceed. |

---

### `HOLD`

| Attribute | Value |
|-----------|-------|
| Meaning | The field is on hold pending an external decision or owner action. A HOLD differs from FAIL — a FAIL means the check was run and failed; a HOLD means the check cannot be run or completed without external input. |
| Applies to | `schema_evidence_map_status`, `runtime_appendix_status`, any field awaiting owner or controller action |
| May be set by | Operator; controller |
| Gate implication | HOLD blocks carry. The hold reason must be recorded in `schema_hold_reasons`. |

---

### `APPROVED`

| Attribute | Value |
|-----------|-------|
| Meaning | The relevant approval (controller or human) has been explicitly granted for this carry operation. |
| Applies to | `controller_decision_status`, `human_approval_status` |
| May be set by | Controller (for `controller_decision_status`); human owner only (for `human_approval_status`) |
| May not be set by | Claude; automated tooling; self-approval of any kind |
| Gate implication | APPROVED satisfies the approval gate check |

---

### `NOT_APPROVED`

| Attribute | Value |
|-----------|-------|
| Meaning | The relevant approval has been explicitly withheld or has not been granted. |
| Applies to | `controller_decision_status`, `human_approval_status` |
| May be set by | Controller; human owner |
| Gate implication | NOT_APPROVED blocks all downstream gates. Carry may not proceed. |

---

### `ATTACH_ELIGIBLE`

| Attribute | Value |
|-----------|-------|
| Meaning | All 8 carry gates have been confirmed, all 12 identity match checks have passed, and no hold codes are active. The schema output bundle is eligible to be attached to the Astro route at Gate 8. |
| Applies to | `schema_attach_eligible` |
| May be set by | Controller, after confirming all gates pass and hold reasons are empty |
| Gate implication | ATTACH_ELIGIBLE is required before Gate 8 may proceed |

---

### `NOT_ATTACH_ELIGIBLE`

| Attribute | Value |
|-----------|-------|
| Meaning | One or more carry gates have not passed, one or more identity match checks have failed, or one or more hold codes are active. The schema output bundle may not be attached. |
| Applies to | `schema_attach_eligible` |
| Default value | This is the default value at package bootstrap |
| Gate implication | NOT_ATTACH_ELIGIBLE blocks Gate 8 |

---

### `ATTACHED`

| Attribute | Value |
|-----------|-------|
| Meaning | The schema output bundle has been successfully attached to the Astro route. Gate 8 is complete. Post-attachment verification steps should begin. |
| Applies to | `schema_attach_status` |
| May be set by | Astro implementation lane, after Gate 8 completes with human approval confirmed |
| Gate implication | ATTACHED marks completion of the carry sequence |

---

### `NOT_ATTACHED`

| Attribute | Value |
|-----------|-------|
| Meaning | Schema has not yet been attached to the Astro route. Default state at package bootstrap and throughout carry preparation. |
| Applies to | `schema_attach_status` |
| Default value | This is the default value at package bootstrap |
| Gate implication | NOT_ATTACHED is expected until Gate 8 completes |

---

## Field-to-enum applicability matrix

| Field | Allowed enum values |
|-------|---------------------|
| `schema_bundle_id` | NOT_STARTED, PENDING, PASS, FAIL |
| `schema_export_id` | NOT_STARTED, PENDING, PASS, FAIL |
| `schema_owner` | `SEO_SCHEMA_OPERATOR` (string constant, not an enum) |
| `schema_source_lane` | `SEO_SCHEMA_EXPORT` (string constant, not an enum) |
| `target_route` | NOT_STARTED, PENDING, PASS, FAIL |
| `page_family` | NOT_STARTED, PENDING, PASS, FAIL |
| `schema_profile_expected` | NOT_STARTED, PENDING, PASS, FAIL |
| `schema_profile_actual` | NOT_STARTED, PENDING, PASS, FAIL |
| `schema_validation_gate_status` | NOT_STARTED, PENDING, PASS, WARN, FAIL |
| `schema_evidence_map_status` | NOT_STARTED, PENDING, PASS, WARN, FAIL, HOLD |
| `schema_truth_fingerprint_status` | NOT_STARTED, PENDING, PASS, FAIL |
| `schema_attach_eligible` | NOT_STARTED, NOT_ATTACH_ELIGIBLE, ATTACH_ELIGIBLE |
| `schema_attach_status` | NOT_STARTED, NOT_ATTACHED, ATTACHED |
| `schema_hold_reasons` | Array of hold code strings (see `ASTRO_SCHEMA_CARRY_HOLD_REASON_REFERENCE_V1_0.md`) |
| `controller_decision_status` | NOT_STARTED, PENDING, APPROVED, NOT_APPROVED |
| `human_approval_status` | NOT_STARTED, PENDING, APPROVED, NOT_APPROVED |
| `astro_route_manifest_status` | NOT_STARTED, PENDING, PASS, FAIL, NOT_APPLICABLE |
| `runtime_appendix_status` | NOT_STARTED, PENDING, PASS, WARN, FAIL, HOLD |

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

No Runtime Appendix record has been populated with any of these enum values. All fields remain NOT_STARTED by default.
