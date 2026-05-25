# Astro Attachment Packet Hold Matrix V1.0

**Status:** `ASTRO_ATTACHMENT_PACKET_TEMPLATE_ADDED_NO_SCHEMA_OUTPUT`

> This document defines the hold matrix for the Astro attachment packet review sequence. All hold conditions are active by default. No packet review has occurred. No schema has been attached. No schema output exists. Mode 2 is not ready.

---

## Purpose

The hold matrix defines every condition that can block the Astro attachment packet review sequence from proceeding. Each hold entry specifies the blocking step, the triggering condition, whether the hold can be self-resolved, and what is required to clear it.

All holds must be cleared — `hold_reasons` must be empty (`[]`) — before `final_attachment_decision` may be set to `APPROVED`.

---

## Hold matrix

### HOLD_ASTRO_ROUTE_MISSING

| Property | Value |
|----------|-------|
| Blocked step | Step 1 — cannot confirm target route |
| Triggered when | No confirmed Astro route manifest exists for the target route; or the target route does not appear in any Astro route manifest |
| Self-resolvable | No — requires real Astro route evidence from the Astro implementation |
| Packet field blocked | `target_route`, `astro_route_manifest_status` |
| Resolution required | A confirmed Astro route manifest must be provided; the target route must be verified in the Astro project |

---

### HOLD_ASTRO_RUNTIME_APPENDIX_MISSING

| Property | Value |
|----------|-------|
| Blocked step | Step 4 — Runtime Appendix not confirmed |
| Triggered when | The Runtime Appendix carry field record for the target route does not exist, is incomplete, or `runtime_appendix_status` is not `PASS` |
| Self-resolvable | No — requires a complete governed Mode 1 run and all 18 carry fields confirmed |
| Packet field blocked | `runtime_appendix_status` |
| Resolution required | Complete a governed Mode 1 run and populate all 18 Runtime Appendix carry fields; confirm `runtime_appendix_status` is `PASS` |

---

### HOLD_SCHEMA_BUNDLE_MISSING

| Property | Value |
|----------|-------|
| Blocked step | Step 1 — cannot confirm output bundle |
| Triggered when | No validated schema output bundle exists for the target route; or `schema_bundle_id` is `NOT_STARTED` or `FAIL` |
| Self-resolvable | No — requires a completed governed Mode 1 run |
| Packet field blocked | `schema_bundle_id` |
| Resolution required | Complete a governed Mode 1 run and produce a validated schema output bundle with controller approval and human sign-off |

---

### HOLD_SCHEMA_EXPORT_ID_MISSING

| Property | Value |
|----------|-------|
| Blocked step | Step 1 — cannot confirm export ID |
| Triggered when | `schema_export_id` is `NOT_STARTED`, `FAIL`, or a duplicate of an existing carry operation |
| Self-resolvable | No — export ID is generated at bundle approval time by the operator lane |
| Packet field blocked | `schema_export_id` |
| Resolution required | A unique export ID must be generated and confirmed at bundle approval time |

---

### HOLD_ROUTE_IDENTITY_MISMATCH

| Property | Value |
|----------|-------|
| Blocked step | Step 6 — identity check fails |
| Triggered when | The `target_route` in the packet does not exactly match the route in the output bundle manifest or the Astro route manifest |
| Self-resolvable | No — requires re-confirmation of route identity across all three sources |
| Packet field blocked | `target_route`, `attach_eligibility_status` |
| Resolution required | Confirm route identity matches across the output bundle manifest, the Runtime Appendix, and the Astro route manifest |

---

### HOLD_PAGE_FAMILY_MISMATCH

| Property | Value |
|----------|-------|
| Blocked step | Step 6 — identity check fails |
| Triggered when | `page_family` in the packet does not match `page_family` in the output bundle manifest |
| Self-resolvable | No |
| Packet field blocked | `page_family`, `attach_eligibility_status` |
| Resolution required | Confirm `page_family` matches the output bundle manifest exactly |

---

### HOLD_SCHEMA_PROFILE_MISMATCH

| Property | Value |
|----------|-------|
| Blocked step | Step 6 — identity check fails |
| Triggered when | `schema_profile_actual` does not exactly match `schema_profile_expected` |
| Self-resolvable | No |
| Packet field blocked | `schema_profile_expected`, `schema_profile_actual`, `attach_eligibility_status` |
| Resolution required | Confirm the profile used in the output bundle matches the profile approved at run intake |

---

### HOLD_TRUTH_FINGERPRINT_MISMATCH

| Property | Value |
|----------|-------|
| Blocked step | Step 6 — identity check fails |
| Triggered when | The truth fingerprint in the output bundle does not match the locked Phase 0 homepage fingerprint: `80edd829806cae271242c6a8e853edabdb8b2f16ca5a8fa1a3fc69ff5b78d53d` |
| Self-resolvable | No — the locked fingerprint is fixed until a new Phase 0 baseline is established |
| Packet field blocked | `truth_fingerprint`, `attach_eligibility_status` |
| Resolution required | The output bundle must be produced from the correct Phase 0 baseline with the matching fingerprint |

---

### HOLD_EVIDENCE_MAP_NOT_PASSED

| Property | Value |
|----------|-------|
| Blocked step | Step 3 — evidence map not confirmed |
| Triggered when | `evidence_map_status` is not `PASS`; or any schema field in the output bundle cannot be traced to Phase 0 or confirmed page evidence |
| Self-resolvable | No — requires a complete evidence map review |
| Packet field blocked | `evidence_map_status`, `attach_eligibility_status` |
| Resolution required | Complete an evidence map review; confirm all fields trace to Phase 0 or confirmed page evidence; resolve any untraced fields |

---

### HOLD_VALIDATION_GATE_NOT_PASSED

| Property | Value |
|----------|-------|
| Blocked step | Step 2 — validation not complete |
| Triggered when | `validation_status` is not `PASS`; or any step of the 9-step final schema validation protocol has not been completed or has an unresolved failure |
| Self-resolvable | No — requires completing the full validation protocol |
| Packet field blocked | `validation_status`, `attach_eligibility_status` |
| Resolution required | Complete all 9 steps of `FINAL_SCHEMA_VALIDATION_PROTOCOL_V1_0.md`; document results in the validation evidence handoff packet |

---

### HOLD_CONTROLLER_APPROVAL_MISSING

| Property | Value |
|----------|-------|
| Blocked step | Step 5 — controller not approved |
| Triggered when | `controller_decision_status` is not `APPROVED`; or `unresolvedBlockers` in the controller review packet is not `0` |
| Self-resolvable | No — controller must review and issue approval |
| Packet field blocked | `controller_decision_status`, `attach_eligibility_status` |
| Resolution required | Controller must complete review and issue final approval with `unresolvedBlockers: 0` |

---

### HOLD_HUMAN_APPROVAL_MISSING

| Property | Value |
|----------|-------|
| Blocked step | Step 7 — human approval not granted |
| Triggered when | `human_approval_status` is not `APPROVED`; or `humanApprovalRef` is absent or empty |
| Self-resolvable | No — human owner must grant explicit approval; cannot be self-granted by Claude or automated tooling |
| Packet field blocked | `human_approval_status`, `final_attachment_decision` |
| Resolution required | Human owner must review the complete attachment packet and explicitly grant approval with a valid reference |

---

### HOLD_HELD_FIELD_UNAPPROVED

| Property | Value |
|----------|-------|
| Blocked step | Step 3 — evidence map check; Step 6 — identity checks |
| Triggered when | Any held field category from `RISE_HELD_FIELD_CATEGORIES_FIRST_PAGE_V1_0.md` is present in the output bundle without explicit owner approval |
| Self-resolvable | No — requires owner approval for each held field category |
| Packet field blocked | `evidence_map_status`, `attach_eligibility_status` |
| Resolution required | Obtain explicit owner approval for each held field; confirm approvals are documented with approval refs |

---

### HOLD_BLOCKED_MODULE_PRESENT

| Property | Value |
|----------|-------|
| Blocked step | Step 3 — evidence map check |
| Triggered when | Any blocked module from `RISE_BLOCKED_SCHEMA_MODULES_FIRST_PAGE_V1_0.md` is present in the output bundle |
| Self-resolvable | No — blocked modules may not be included without a governing doctrine PR explicitly authorizing each one |
| Packet field blocked | `evidence_map_status`, `attach_eligibility_status` |
| Resolution required | Remove the blocked module from the output bundle; a governing doctrine PR is required to unblock any module |

---

### HOLD_ASTRO_ATTACHMENT_NOT_AUTHORIZED

| Property | Value |
|----------|-------|
| Blocked step | Step 8 — final packet approval; Step 9 — attachment |
| Triggered when | `final_attachment_decision` is `NOT_APPROVED`; or any prior step has not completed; or `attach_eligibility_status` is `NOT_ATTACH_ELIGIBLE` |
| Self-resolvable | No — all prior steps must complete and human owner must grant final approval |
| Packet field blocked | `final_attachment_decision` |
| Resolution required | Complete all 8 prior steps; confirm all packet fields are at required passing states; obtain human owner final approval |

---

## Hold matrix summary table

| Hold code | Blocking step | Self-resolvable | Packet field blocked |
|-----------|--------------|----------------|---------------------|
| `HOLD_ASTRO_ROUTE_MISSING` | Step 1 | No | `target_route`, `astro_route_manifest_status` |
| `HOLD_ASTRO_RUNTIME_APPENDIX_MISSING` | Step 4 | No | `runtime_appendix_status` |
| `HOLD_SCHEMA_BUNDLE_MISSING` | Step 1 | No | `schema_bundle_id` |
| `HOLD_SCHEMA_EXPORT_ID_MISSING` | Step 1 | No | `schema_export_id` |
| `HOLD_ROUTE_IDENTITY_MISMATCH` | Step 6 | No | `target_route` |
| `HOLD_PAGE_FAMILY_MISMATCH` | Step 6 | No | `page_family` |
| `HOLD_SCHEMA_PROFILE_MISMATCH` | Step 6 | No | `schema_profile_expected`, `schema_profile_actual` |
| `HOLD_TRUTH_FINGERPRINT_MISMATCH` | Step 6 | No | `truth_fingerprint` |
| `HOLD_EVIDENCE_MAP_NOT_PASSED` | Step 3 | No | `evidence_map_status` |
| `HOLD_VALIDATION_GATE_NOT_PASSED` | Step 2 | No | `validation_status` |
| `HOLD_CONTROLLER_APPROVAL_MISSING` | Step 5 | No | `controller_decision_status` |
| `HOLD_HUMAN_APPROVAL_MISSING` | Step 7 | No | `human_approval_status` |
| `HOLD_HELD_FIELD_UNAPPROVED` | Steps 3, 6 | No | `evidence_map_status` |
| `HOLD_BLOCKED_MODULE_PRESENT` | Step 3 | No | `evidence_map_status` |
| `HOLD_ASTRO_ATTACHMENT_NOT_AUTHORIZED` | Steps 8, 9 | No | `final_attachment_decision` |

**All 15 hold codes are active by default.** No hold is self-resolvable. Each requires real governed evidence or explicit human approval.

---

## Non-authorization statement

This document does not authorize:
- Astro schema attachment
- JSON-LD generation
- Schema output creation
- Current website implementation
- Production deployment
- Mode 2 readiness

All hold codes are active. No packet review has occurred. Mode 2 is not ready.
