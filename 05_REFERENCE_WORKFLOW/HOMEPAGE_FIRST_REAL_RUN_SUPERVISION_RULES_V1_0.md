# Homepage First Real Run Supervision Rules V1.0

**Status:** `FIRST_REAL_PAGE_HANDOFF_TEMPLATE_ADDED_NO_SCHEMA_OUTPUT`

> This document defines the supervision rules for the first real homepage schema run. These rules apply exclusively to the homepage lane (route `/`) with `HOMEPAGE_SCHEMA_PROFILE`. No real run has been started. No schema has been generated. These are governance rules only.

---

## Non-authorization statement

This document does not start a schema run, generate JSON-LD, create an evidence map, authorize current website implementation, authorize Astro attachment, or claim production lock. These rules will apply when a future governed run begins after the final runnable handoff is in place.

---

## Homepage lane identity

| Property | Value |
|----------|-------|
| Page | Homepage |
| Route | `/` |
| Active schema profile | `HOMEPAGE_SCHEMA_PROFILE` |
| Homepage scoped truth fingerprint | `80edd829806cae271242c6a8e853edabdb8b2f16ca5a8fa1a3fc69ff5b78d53d` |
| Mode | `MODE_1_CURRENT_WEBSITE` (primary) |

---

## Supervision rule 1 — Phase 0 anchor required

Every field in the homepage schema output must trace directly to Rise Phase 0 or confirmed page evidence. No field may be invented, assumed, or inferred without a confirmed source.

If a field cannot be traced to Phase 0 or confirmed page evidence, it must not appear in any schema output.

---

## Supervision rule 2 — Fingerprint lock enforcement

Before any homepage schema run begins, the operator must confirm that the active scoped truth view (`03_TRUTH_PACK/RISE_PHASE0_SCHEMA_TRUTH_VIEW_HOMEPAGE_SCOPED_V1_0.json`) matches the fingerprint lock:

```
80edd829806cae271242c6a8e853edabdb8b2f16ca5a8fa1a3fc69ff5b78d53d
```

If the fingerprint does not match: STOP. The truth view may be stale. Do not proceed until the truth view is re-confirmed and the fingerprint is updated.

---

## Supervision rule 3 — Allowed modules only

For the homepage lane, only the following schema modules are permitted:

| Module | Supervision notes |
|--------|-------------------|
| `Organization` | Fields must trace to Phase 0. Held fields must remain held until owner approval exists. |
| `WebSite` | Includes `SearchAction` only if confirmed from page evidence. |
| `WebPage` | Scoped to homepage route `/` only. |
| `BreadcrumbList` | Homepage BreadcrumbList is typically a single root node. Confirm from page structure. |

No other module may appear in any homepage schema draft or output bundle.

---

## Supervision rule 4 — Blocked modules

The following modules are blocked for the homepage lane. None may appear in any schema draft, output bundle, or implementation:

| Module | Block reason |
|--------|-------------|
| `FAQPage` | Blocked — no governed FAQ content confirmed |
| `Offer` | Blocked — no governed offer/pricing content confirmed |
| `Event` | Blocked — no governed event content confirmed |
| `Review` | Blocked — no governed review content confirmed |
| `AggregateRating` | Blocked — no governed ratings confirmed |
| `Place` | Blocked — address/place identity is a held field category |
| `GeoCoordinates` | Blocked — coordinates are a held field category |
| `testimonial_derived_schema` | Blocked — testimonial claims may not become schema fields |
| `bilingual_schema` | Blocked — bilingual alternate data is a held field category |
| `advanced_modules` | Blocked — not yet authorized by governing doctrine |

---

## Supervision rule 5 — Held fields

All 14 held field categories default to `HOLD` for the homepage lane. A held field category may not be emitted in any schema output unless **all three** of the following are true:

1. The field has been reviewed and approved by the Rise owner.
2. A confirmed Phase 0 or page evidence record supports the field value.
3. The approval is recorded in `03_TRUTH_PACK/RISE_CONTACT_SOCIAL_LOGO_OWNER_APPROVAL_WORKSHEET_V1_0.md`.

| Field category | Default status |
|----------------|----------------|
| `phone` | `HOLD` |
| `email` | `HOLD` |
| `sameAs_social_urls` | `HOLD` |
| `absolute_logo_url` | `HOLD` |
| `schema_description_from_tagline_or_mission` | `HOLD` |
| `coordinates` | `HOLD` |
| `address_place_identity` | `HOLD` |
| `reviews` | `HOLD` |
| `ratings` | `HOLD` |
| `prices` | `HOLD` |
| `event_dates` | `HOLD` |
| `offer_details` | `HOLD` |
| `testimonial_derived_claims` | `HOLD` |
| `bilingual_alternate_data` | `HOLD` |

---

## Supervision rule 6 — Evidence map required before drafting

No homepage JSON-LD draft may be produced without a confirmed evidence map for the homepage route `/`. The evidence map must:

- Exist as a file conforming to `06_MACHINE_RULES/EVIDENCE_MAP_SCHEMA_V1_0.json`
- Reference confirmed Phase 0 evidence for every field it supports
- Be reviewed and confirmed before the run begins

See `FIRST_REAL_PAGE_RUN_INTAKE_FIELDS_V1_0.md` for evidence map intake validation requirements.

---

## Supervision rule 7 — Human approval required at every gate

The homepage schema run is a supervised workflow. Human approval is required before:

- Implementation handoff (Step 8 of the validation protocol)
- Production lock claim
- Any schema attachment to the current website

The controller may not self-approve production. Claude may not self-approve production. The run ledger append helper enforces this: `PRODUCTION_LOCKED` without `humanApprovalRef` will fail the 20 safety checks.

---

## Supervision rule 8 — No Phase 0 mutation

This package is a downstream read model from Rise Phase 0. The homepage first real run must not:

- Modify any file in `03_TRUTH_PACK/`
- Modify any Phase 0 source document
- Override or normalize Phase 0 field values
- Invent field values to fill gaps in Phase 0

If Phase 0 does not confirm a field, that field does not go into schema.

---

## Supervision rule 9 — Run ledger entry required

After a successful governed homepage run, a run ledger entry must be appended to `RUN_LEDGER.json` using `tools/append_run_ledger_entry.py`. The entry must conform to `06_MACHINE_RULES/RUN_LEDGER_SCHEMA_V1_0.json`.

Do not skip the run ledger update. An unrecorded run has no governance history.

---

## Supervision rule 10 — No self-merge

All PRs associated with the homepage first real run must be merged by a human. No self-merge.

---

## Summary — homepage first run stop conditions

| Condition | Action |
|-----------|--------|
| Phase 0 source not confirmed | STOP — hold code `HOLD_PHASE0_SOURCE_MISSING` |
| Truth view not confirmed | STOP — hold code `HOLD_TRUTH_VIEW_MISSING` |
| Truth view fingerprint stale | STOP — hold code `HOLD_TRUTH_VIEW_STALE` or `HOLD_FINGERPRINT_MISMATCH` |
| Schema profile not confirmed | STOP — hold code `HOLD_PROFILE_MISSING` |
| Evidence map missing | STOP — hold code `HOLD_EVIDENCE_MAP_MISSING` |
| Readiness gate not passed | STOP — hold code `HOLD_READINESS_NOT_PASSED` |
| Blocked module requested | STOP — hold code `HOLD_BLOCKED_MODULE_REQUESTED` |
| Held field unapproved | STOP — hold code `HOLD_HELD_FIELD_UNAPPROVED` |
| Validation missing | STOP — hold code `HOLD_VALIDATION_MISSING` |
| Controller decision missing | STOP — hold code `HOLD_CONTROLLER_DECISION_MISSING` |
| Human approval missing | STOP — hold code `HOLD_HUMAN_APPROVAL_MISSING` |
| Implementation not authorized | STOP — hold code `HOLD_IMPLEMENTATION_NOT_AUTHORIZED` |

See `FIRST_REAL_PAGE_RUN_HOLD_REASON_REFERENCE_V1_0.md` for full hold code definitions and resolution requirements.
