# Astro Schema Identity Match Requirements V1.0

**Status:** `ASTRO_SCHEMA_CARRY_GATE_REFERENCE_ADDED_NO_SCHEMA_OUTPUT`

---

## Purpose

This document defines the identity match checks that must pass before any approved schema output may be carried into the Astro implementation lane.

Identity match is Gate 6 of the Astro carry gate sequence defined in `ASTRO_SCHEMA_CARRY_GATE_REFERENCE_V1_0.md`. All checks in this document must pass before Gate 6 may be marked confirmed.

---

## Identity match checks

### Check 1 — Approved schema bundle ID

| Requirement | Rule |
|-------------|------|
| `schema_bundle_id` is present in the carry packet | Required — no carry without bundle ID |
| `schema_bundle_id` matches the `runId` of the approved, validated output bundle | Must be an exact string match |
| The output bundle referenced by `schema_bundle_id` has passed `tools/validate_output_bundle.py` | Must return PASS at time of carry gate check |

**Failure action:** `HOLD_SCHEMA_BUNDLE_MISSING` or `HOLD_ROUTE_IDENTITY_MISMATCH`

---

### Check 2 — Schema export ID

| Requirement | Rule |
|-------------|------|
| `schema_export_id` is present in the carry packet | Required — no carry without export ID |
| `schema_export_id` is unique within the run ledger | Duplicate export IDs are not permitted |
| `schema_export_id` format | `RISE_EXPORT_<PAGE_FAMILY>_<DATE_YYYYMMDD>_<SEQ>` |

**Failure action:** `HOLD_SCHEMA_EXPORT_ID_MISSING`

---

### Check 3 — Route identity match

| Requirement | Rule |
|-------------|------|
| `target_route` in the carry packet | Must match the route in the approved schema output bundle |
| `target_route` in the carry packet | Must match the confirmed Astro route |
| Route format | Must begin with `/` — absolute route path |

**Failure action:** `HOLD_ROUTE_IDENTITY_MISMATCH`

---

### Check 4 — Page family match

| Requirement | Rule |
|-------------|------|
| `page_family` in the carry packet | Must match the page family in the approved schema output bundle |
| `page_family` in the carry packet | Must match the Astro page component family |
| Homepage page family | `HOMEPAGE` for route `/` |

**Failure action:** `HOLD_PAGE_FAMILY_MISMATCH`

---

### Check 5 — Schema profile match

| Requirement | Rule |
|-------------|------|
| `schema_profile_expected` | The profile declared at run start (e.g., `HOMEPAGE_SCHEMA_PROFILE`) |
| `schema_profile_actual` | The profile confirmed in the approved output bundle |
| Match condition | `schema_profile_expected` must equal `schema_profile_actual` — exact string match |

**Failure action:** `HOLD_SCHEMA_PROFILE_MISMATCH`

---

### Check 6 — Truth fingerprint match

| Requirement | Rule |
|-------------|------|
| `truth_fingerprint` in the carry packet | Must be present |
| `truth_fingerprint` value | Must match the locked homepage truth fingerprint: `80edd829806cae271242c6a8e853edabdb8b2f16ca5a8fa1a3fc69ff5b78d53d` |
| Fingerprint match is exact | SHA-256 string comparison — no partial matches |

**Failure action:** `HOLD_TRUTH_FINGERPRINT_MISMATCH`

---

### Check 7 — Evidence map pass

| Requirement | Rule |
|-------------|------|
| Evidence map exists for the target profile | Required — no carry without a passed evidence map |
| `schema_evidence_map_status` | Must be `PASS` |
| Every field marked `EMIT` in the evidence map | Must trace to `PHASE_0_CONFIRMED` or `PAGE_EVIDENCE_CONFIRMED` |

**Failure action:** `HOLD_EVIDENCE_MAP_NOT_PASSED`

---

### Check 8 — Validation gate pass

| Requirement | Rule |
|-------------|------|
| `schema_validation_gate_status` | Must be `PASS` |
| Schema.org Validator | Must have been run and returned no blocking errors |
| Google Rich Results Test | Must have been run (informational) |
| Output bundle validator | Must return PASS |

**Failure action:** `HOLD_VALIDATION_GATE_NOT_PASSED`

---

### Check 9 — Controller approval

| Requirement | Rule |
|-------------|------|
| `controller_decision_status` | Must be `APPROVED` |
| `finalRecommendation` in controller review packet | Must be `PROCEED_TO_HUMAN_APPROVAL` |
| `unresolvedBlockers` | Must be `0` |

**Failure action:** `HOLD_CONTROLLER_APPROVAL_MISSING`

---

### Check 10 — Human approval

| Requirement | Rule |
|-------------|------|
| `human_approval_status` | Must be `APPROVED` |
| `humanApprovalRef` | Must be present in the run ledger entry |
| Human approver | Must be a named person — not Claude, not a validator, not an automated process |

**Failure action:** `HOLD_HUMAN_APPROVAL_MISSING`

---

### Check 11 — No held fields emitted without approval

| Requirement | Rule |
|-------------|------|
| All held field categories | Must be `NOT_REVIEWED_HELD` or owner-approved before emission |
| Held fields emitted | Only allowed if owner approval is recorded in `RISE_CONTACT_SOCIAL_LOGO_OWNER_APPROVAL_WORKSHEET_V1_0.md` with a confirmed Phase 0 or page evidence source |
| Self-approval by operator | Not permitted |

**Failure action:** `HOLD_HELD_FIELD_UNAPPROVED`

---

### Check 12 — No blocked modules emitted

| Requirement | Rule |
|-------------|------|
| Blocked modules | All 10 blocked modules must be absent from the carry packet schema |
| Blocked module list | FAQPage, Offer, Event, Review, AggregateRating, Place, GeoCoordinates, testimonial-derived schema, bilingual schema, advanced modules |
| Presence of any blocked module | Blocks the entire carry — `HOLD_BLOCKED_MODULE_PRESENT` |

**Failure action:** `HOLD_BLOCKED_MODULE_PRESENT`

---

## Identity match summary table

| Check | Field | Required value | Failure hold code |
|-------|-------|----------------|-------------------|
| 1 | `schema_bundle_id` | Matches approved output bundle runId | `HOLD_SCHEMA_BUNDLE_MISSING` |
| 2 | `schema_export_id` | Present, unique, correct format | `HOLD_SCHEMA_EXPORT_ID_MISSING` |
| 3 | `target_route` | Matches bundle route and Astro route | `HOLD_ROUTE_IDENTITY_MISMATCH` |
| 4 | `page_family` | Matches bundle and Astro page family | `HOLD_PAGE_FAMILY_MISMATCH` |
| 5 | `schema_profile_expected` vs `schema_profile_actual` | Exact match | `HOLD_SCHEMA_PROFILE_MISMATCH` |
| 6 | `truth_fingerprint` | `80edd829...d53d` | `HOLD_TRUTH_FINGERPRINT_MISMATCH` |
| 7 | `schema_evidence_map_status` | `PASS` | `HOLD_EVIDENCE_MAP_NOT_PASSED` |
| 8 | `schema_validation_gate_status` | `PASS` | `HOLD_VALIDATION_GATE_NOT_PASSED` |
| 9 | `controller_decision_status` | `APPROVED` | `HOLD_CONTROLLER_APPROVAL_MISSING` |
| 10 | `human_approval_status` | `APPROVED` | `HOLD_HUMAN_APPROVAL_MISSING` |
| 11 | Held fields | None emitted without owner approval | `HOLD_HELD_FIELD_UNAPPROVED` |
| 12 | Blocked modules | None present | `HOLD_BLOCKED_MODULE_PRESENT` |

---

## What this document does not do

- It does not create Astro implementation
- It does not attach schema to Astro
- It does not create JSON-LD
- It does not create schema output
- It does not mark Mode 2 as ready
- It does not confirm any of the listed identity checks — all checks are NOT REACHED
- It does not mutate Rise Phase 0
- It does not authorize production lock
