# Astro Schema Carry Hold Reason Reference V1.0

**Status:** `ASTRO_SCHEMA_CARRY_GATE_REFERENCE_ADDED_NO_SCHEMA_OUTPUT`

---

## Purpose

This document defines all hold codes that apply to the Astro schema carry and attachment workflow. Each hold code has a definition, condition, and resolution requirement.

A hold is a stop condition — when a hold is active, no carry gate may proceed past the point at which the hold applies.

---

## Hold codes

### HOLD_ASTRO_ROUTE_MISSING

| Field | Value |
|-------|-------|
| Code | `HOLD_ASTRO_ROUTE_MISSING` |
| Category | Astro readiness |
| Definition | The target Astro route for the page family does not exist in the Astro project |
| Condition | No confirmed Astro route file exists for the target route (e.g., `/` → `src/pages/index.astro`) |
| Blocks | Gate 5 — Astro route manifest check |
| Resolution | Astro implementation lane confirms the route file exists and is the correct page family |
| Can be self-resolved by operator? | No — requires Astro implementation lane confirmation |

---

### HOLD_ASTRO_RUNTIME_APPENDIX_MISSING

| Field | Value |
|-------|-------|
| Code | `HOLD_ASTRO_RUNTIME_APPENDIX_MISSING` |
| Category | Runtime Appendix readiness |
| Definition | The Runtime Appendix carry field record for the target route is missing or incomplete |
| Condition | `RUNTIME_APPENDIX_SCHEMA_CARRY_FIELD_REFERENCE_V1_0.md` has not been loaded, or the carry field status record for the route is absent |
| Blocks | Gate 4 — Runtime Appendix carry fields complete |
| Resolution | Runtime Appendix carry fields for the target route must be defined and all required statuses set |
| Can be self-resolved by operator? | No — requires carry field record to be established |

---

### HOLD_SCHEMA_BUNDLE_MISSING

| Field | Value |
|-------|-------|
| Code | `HOLD_SCHEMA_BUNDLE_MISSING` |
| Category | Schema output readiness |
| Definition | No approved, validated schema output bundle exists for the target route |
| Condition | No governed schema run has been completed, OR the output bundle has not passed `tools/validate_output_bundle.py` |
| Blocks | Gate 1 — Schema output bundle approved |
| Resolution | A governed schema run must be completed and the output bundle must pass validation |
| Can be self-resolved by operator? | No — requires a real governed run |

---

### HOLD_SCHEMA_EXPORT_ID_MISSING

| Field | Value |
|-------|-------|
| Code | `HOLD_SCHEMA_EXPORT_ID_MISSING` |
| Category | Carry packet integrity |
| Definition | The carry packet does not contain a valid `schema_export_id` |
| Condition | `schema_export_id` is absent, blank, or does not follow the format `RISE_EXPORT_<PAGE_FAMILY>_<DATE_YYYYMMDD>_<SEQ>` |
| Blocks | Gate 6 — Identity and profile match, Check 2 |
| Resolution | Assign a valid, unique `schema_export_id` following the required format |
| Can be self-resolved by operator? | Yes — after a governed run produces the export ID |

---

### HOLD_ROUTE_IDENTITY_MISMATCH

| Field | Value |
|-------|-------|
| Code | `HOLD_ROUTE_IDENTITY_MISMATCH` |
| Category | Identity match |
| Definition | The `target_route` in the carry packet does not match the route in the approved schema output bundle or the confirmed Astro route |
| Condition | Any mismatch between carry packet `target_route`, schema bundle route, and Astro route |
| Blocks | Gate 6 — Identity and profile match, Check 3 |
| Resolution | Confirm the route is consistent across the carry packet, the schema output bundle, and the Astro project |
| Can be self-resolved by operator? | No — requires Astro implementation lane to confirm route |

---

### HOLD_PAGE_FAMILY_MISMATCH

| Field | Value |
|-------|-------|
| Code | `HOLD_PAGE_FAMILY_MISMATCH` |
| Category | Identity match |
| Definition | The `page_family` in the carry packet does not match the page family in the approved schema output bundle or the Astro page component |
| Condition | Any mismatch between `page_family` values across the carry packet, the schema bundle, and the Astro page |
| Blocks | Gate 6 — Identity and profile match, Check 4 |
| Resolution | Confirm page family is consistent across all three sources |
| Can be self-resolved by operator? | No — requires Astro implementation lane confirmation |

---

### HOLD_SCHEMA_PROFILE_MISMATCH

| Field | Value |
|-------|-------|
| Code | `HOLD_SCHEMA_PROFILE_MISMATCH` |
| Category | Identity match |
| Definition | `schema_profile_expected` does not match `schema_profile_actual` in the carry packet |
| Condition | The schema profile declared at run start differs from the profile confirmed in the approved output bundle |
| Blocks | Gate 6 — Identity and profile match, Check 5 |
| Resolution | Investigate the profile discrepancy. The run must be redone if the wrong profile was used. |
| Can be self-resolved by operator? | No — requires controller review of the discrepancy |

---

### HOLD_TRUTH_FINGERPRINT_MISMATCH

| Field | Value |
|-------|-------|
| Code | `HOLD_TRUTH_FINGERPRINT_MISMATCH` |
| Category | Identity match |
| Definition | The `truth_fingerprint` in the carry packet does not match the locked homepage truth fingerprint |
| Condition | Any value other than `80edd829806cae271242c6a8e853edabdb8b2f16ca5a8fa1a3fc69ff5b78d53d` |
| Blocks | Gate 6 — Identity and profile match, Check 6 |
| Resolution | The Phase 0 truth view must be re-confirmed. If the truth view has been updated, a new fingerprint lock PR is required before the carry may proceed. |
| Can be self-resolved by operator? | No — requires truth pack owner review |

---

### HOLD_EVIDENCE_MAP_NOT_PASSED

| Field | Value |
|-------|-------|
| Code | `HOLD_EVIDENCE_MAP_NOT_PASSED` |
| Category | Evidence readiness |
| Definition | The evidence map for the target schema profile has not been created, or has not passed all field-level checks |
| Condition | No evidence map exists, OR `schema_evidence_map_status` is not `PASS` |
| Blocks | Gate 6 — Identity and profile match, Check 7 |
| Resolution | Create and pass the homepage evidence map per `06_MACHINE_RULES/EVIDENCE_MAP_SCHEMA_V1_0.json` |
| Can be self-resolved by operator? | No — requires a future governed evidence map PR |

---

### HOLD_VALIDATION_GATE_NOT_PASSED

| Field | Value |
|-------|-------|
| Code | `HOLD_VALIDATION_GATE_NOT_PASSED` |
| Category | Validation readiness |
| Definition | The final schema validation protocol has not been completed, or one or more validation steps failed |
| Condition | `schema_validation_gate_status` is not `PASS`, OR Schema.org Validator returned blocking errors, OR output bundle validator returned FAIL |
| Blocks | Gate 6 — Identity and profile match, Check 8 |
| Resolution | Complete all steps of `FINAL_SCHEMA_VALIDATION_PROTOCOL_V1_0.md` and resolve all blocking errors |
| Can be self-resolved by operator? | Operator may fix schema issues, but validation must be re-run after any fix |

---

### HOLD_CONTROLLER_APPROVAL_MISSING

| Field | Value |
|-------|-------|
| Code | `HOLD_CONTROLLER_APPROVAL_MISSING` |
| Category | Review readiness |
| Definition | The controller has not issued `finalRecommendation: PROCEED_TO_HUMAN_APPROVAL`, or `unresolvedBlockers` is not 0 |
| Condition | `controller_decision_status` is not `APPROVED`, OR unresolved blockers remain |
| Blocks | Gate 2 — Controller approval; Gate 6 — Identity and profile match, Check 9 |
| Resolution | Complete the controller review workflow. Resolve all blockers. |
| Can be self-resolved by operator? | No — controller must issue the final recommendation |

---

### HOLD_HUMAN_APPROVAL_MISSING

| Field | Value |
|-------|-------|
| Code | `HOLD_HUMAN_APPROVAL_MISSING` |
| Category | Approval readiness |
| Definition | Human approval has not been granted for the schema output bundle or for the Astro attachment step |
| Condition | `human_approval_status` is not `APPROVED`, OR `humanApprovalRef` is absent from the run ledger |
| Blocks | Gate 3 — Human approval; Gate 6 — Identity and profile match, Check 10 |
| Resolution | Human owner reviews and explicitly approves. No Claude session may self-approve. |
| Can be self-resolved by operator? | No — human must approve explicitly |

---

### HOLD_HELD_FIELD_UNAPPROVED

| Field | Value |
|-------|-------|
| Code | `HOLD_HELD_FIELD_UNAPPROVED` |
| Category | Field compliance |
| Definition | One or more held fields are present in the carry packet schema without a recorded owner approval |
| Condition | Any held field category (phone, email, sameAs, logoUrl, descriptionFromTagline, coordinates, addressPlaceIdentity, reviews, ratings, prices, eventDates, offerDetails, testimonialDerivedClaims, bilingualAlternateData) is emitted without a matching entry in `RISE_CONTACT_SOCIAL_LOGO_OWNER_APPROVAL_WORKSHEET_V1_0.md` |
| Blocks | Gate 6 — Identity and profile match, Check 11 |
| Resolution | Remove the held field from the schema output, OR obtain owner approval and confirm Phase 0 or page evidence source before re-running |
| Can be self-resolved by operator? | No — owner must approve held fields |

---

### HOLD_BLOCKED_MODULE_PRESENT

| Field | Value |
|-------|-------|
| Code | `HOLD_BLOCKED_MODULE_PRESENT` |
| Category | Module compliance |
| Definition | One or more blocked schema modules are present in the carry packet schema |
| Condition | Any of FAQPage, Offer, Event, Review, AggregateRating, Place, GeoCoordinates, testimonial-derived schema, bilingual schema, or advanced modules is present |
| Blocks | Gate 6 — Identity and profile match, Check 12 |
| Resolution | Remove the blocked module from the schema output. No waiver process exists for blocked modules without a future governing doctrine PR. |
| Can be self-resolved by operator? | Only by removing the blocked module — unblocking requires a future doctrine PR |

---

### HOLD_ASTRO_ATTACHMENT_NOT_AUTHORIZED

| Field | Value |
|-------|-------|
| Code | `HOLD_ASTRO_ATTACHMENT_NOT_AUTHORIZED` |
| Category | Authorization |
| Definition | Astro attachment has not been authorized by a governing doctrine PR and human approval |
| Condition | `astroAttachmentAuthorized: false` in `package_manifest.json`, OR no human approval for the Astro attachment step exists |
| Blocks | Gate 8 — Astro implementation lane attaches schema |
| Resolution | All prior carry gates (1–7) must pass. A governing PR must set `astroAttachmentAuthorized: true`. Human approval for the attachment step must be granted. |
| Can be self-resolved by operator? | No — requires governing PR and human approval |

---

## Hold code summary table

| Code | Category | Blocks gate | Can operator self-resolve? |
|------|----------|-------------|---------------------------|
| `HOLD_ASTRO_ROUTE_MISSING` | Astro readiness | Gate 5 | No |
| `HOLD_ASTRO_RUNTIME_APPENDIX_MISSING` | Runtime Appendix readiness | Gate 4 | No |
| `HOLD_SCHEMA_BUNDLE_MISSING` | Schema output readiness | Gate 1 | No |
| `HOLD_SCHEMA_EXPORT_ID_MISSING` | Carry packet integrity | Gate 6, Check 2 | Yes (after governed run) |
| `HOLD_ROUTE_IDENTITY_MISMATCH` | Identity match | Gate 6, Check 3 | No |
| `HOLD_PAGE_FAMILY_MISMATCH` | Identity match | Gate 6, Check 4 | No |
| `HOLD_SCHEMA_PROFILE_MISMATCH` | Identity match | Gate 6, Check 5 | No |
| `HOLD_TRUTH_FINGERPRINT_MISMATCH` | Identity match | Gate 6, Check 6 | No |
| `HOLD_EVIDENCE_MAP_NOT_PASSED` | Evidence readiness | Gate 6, Check 7 | No |
| `HOLD_VALIDATION_GATE_NOT_PASSED` | Validation readiness | Gate 6, Check 8 | Partial |
| `HOLD_CONTROLLER_APPROVAL_MISSING` | Review readiness | Gates 2, 6 Check 9 | No |
| `HOLD_HUMAN_APPROVAL_MISSING` | Approval readiness | Gates 3, 6 Check 10 | No |
| `HOLD_HELD_FIELD_UNAPPROVED` | Field compliance | Gate 6, Check 11 | No |
| `HOLD_BLOCKED_MODULE_PRESENT` | Module compliance | Gate 6, Check 12 | Partial (remove only) |
| `HOLD_ASTRO_ATTACHMENT_NOT_AUTHORIZED` | Authorization | Gate 8 | No |

---

## What this document does not do

- It does not create Astro implementation
- It does not attach schema to Astro
- It does not create JSON-LD
- It does not create schema output
- It does not mark Mode 2 as ready
- It does not resolve any hold codes — all holds are active by default
- It does not mutate Rise Phase 0
- It does not authorize production lock
