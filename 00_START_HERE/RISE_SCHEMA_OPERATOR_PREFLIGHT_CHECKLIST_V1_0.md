# Rise Schema Operator Preflight Checklist V1.0

**Status:** `OPERATOR_QUICKSTART_CHECKLIST_UPGRADED_NO_SCHEMA_OUTPUT`

> **Schema production is disabled.** This checklist lists all conditions that must be true before any schema run may begin. After PR #6, many of these conditions are not yet met. Do not attempt to run the schema workflow until all conditions are satisfied.

---

## Package health

- [ ] You are in the correct repository (`csc-dev-usman/SCHEMA-FOR-RISE` or its confirmed successor)
- [ ] You are on a feature branch, not `main`
- [ ] `package_manifest.json` is present and parses cleanly
- [ ] `RUN_LEDGER.json` is present and parses cleanly
- [ ] `package_manifest.json` status is the expected current status
- [ ] No unexpected files have been added to the repository

---

## Doctrine

- [ ] PR #2 (governing doctrine) has been merged ✓ Done
- [ ] You have read `02_GOVERNING_DOCTRINE/RISE_SCHEMA_SOURCE_TRUTH_BOUNDARY_V1_0.md`
- [ ] You have read `02_GOVERNING_DOCTRINE/RISE_SCHEMA_GOVERNING_DOCTRINE_V1_0.md`
- [ ] You have read `02_GOVERNING_DOCTRINE/RISE_SCHEMA_OPERATOR_LANE_OWNERSHIP_V1_0.md`
- [ ] You have read `02_GOVERNING_DOCTRINE/RISE_SCHEMA_NON_AUTHORIZATION_AND_HOLD_RULES_V1_0.md`
- [ ] You understand the evidence-first rule: no field may be emitted without Phase 0 or page evidence
- [ ] You understand the no-invention rule: no field may be estimated, inferred, or guessed

---

## Truth pack

- [ ] PR #3 (truth pack) has been merged ✓ Done
- [ ] You have read `03_TRUTH_PACK/RISE_PHASE0_TRUTH_SOURCE_MAP_V1_0.md`
- [ ] You have read `03_TRUTH_PACK/RISE_PHASE0_SCHEMA_TRUTH_VIEW_HOMEPAGE_SCOPED_V1_0.json` (read-only reference — not JSON-LD)
- [ ] You have checked the truth-pack backlog (`03_TRUTH_PACK/TRUTH_PACK_BACKLOG.md`) for the current page scope

---

## Fingerprint

- [ ] You have read `03_TRUTH_PACK/RISE_HOMEPAGE_TRUTH_FINGERPRINT_LOCK_V1_0.md`
- [ ] The truth fingerprint for the target profile is confirmed: `80edd829806cae271242c6a8e853edabdb8b2f16ca5a8fa1a3fc69ff5b78d53d`
- [ ] The fingerprint matches the locked value in `package_manifest.json`
- [ ] **HOLD if fingerprint does not match** — do not proceed until mismatch is resolved via a governed truth-pack PR

---

## Schema profile

- [ ] PR #4 (schema profile) has been merged ✓ Done
- [ ] You have read `07_REFERENCE_LISTS/RISE_HOMEPAGE_SCHEMA_PROFILE_V1_0.md`
- [ ] The active profile for route `/` is `HOMEPAGE_SCHEMA_PROFILE`
- [ ] You have read the allowed modules list (`07_REFERENCE_LISTS/RISE_FIRST_PAGE_ALLOWED_MODULES_V1_0.md`)
- [ ] You have read the blocked module policy (`07_REFERENCE_LISTS/RISE_BLOCKED_SCHEMA_MODULES_FIRST_PAGE_V1_0.md`)
- [ ] You have confirmed the decision matrix outcome (`07_REFERENCE_LISTS/RISE_SCHEMA_PROFILE_DECISION_MATRIX_V1_0.md`)

---

## Blocked modules

None of the following may appear in any schema output for the homepage lane:

- [ ] `FAQPage` — BLOCKED
- [ ] `Offer` — BLOCKED
- [ ] `Event` — BLOCKED
- [ ] `Review` — BLOCKED
- [ ] `AggregateRating` — BLOCKED
- [ ] `Place` — BLOCKED
- [ ] `GeoCoordinates` — BLOCKED
- [ ] Testimonial-derived schema — BLOCKED
- [ ] Bilingual schema — BLOCKED
- [ ] Advanced modules — BLOCKED

---

## Held fields

- [ ] You have read `07_REFERENCE_LISTS/RISE_HELD_FIELD_CATEGORIES_FIRST_PAGE_V1_0.md`
- [ ] You have checked `03_TRUTH_PACK/RISE_CONTACT_SOCIAL_LOGO_OWNER_APPROVAL_WORKSHEET_V1_0.md` for the current approval status of each field
- [ ] You confirm that no held field will be emitted without owner approval
- [ ] You confirm that held fields will be **omitted** — not estimated, not inferred, not filled with placeholders

---

## Master flow

- [ ] PR #5 (master flow) has been merged ✓ Done
- [ ] You have read `01_MASTER_FLOW/RISE_STANDALONE_SCHEMA_MASTER_FLOW_V1_0.md`
- [ ] You have read `01_MASTER_FLOW/RISE_SCHEMA_PAGE_RUN_SEQUENCE_V1_0.md`
- [ ] You have read the mode-specific flow for your target mode (Mode 1 or Mode 2)
- [ ] You understand the 14-step page run sequence

---

## Stop conditions

- [ ] You have read `01_MASTER_FLOW/RISE_SCHEMA_MASTER_STOP_CONDITIONS_V1_0.md`
- [ ] You know which stop code applies if any of the following occur: missing truth, fingerprint mismatch, missing profile, missing evidence map, blocked module request, held field violation, premature JSON-LD, premature implementation, premature Astro attachment

---

## Future gates not yet met (schema production still disabled)

The following are required before any schema output may be produced. None of these exist after PR #6:

| Gate | Required PR | Status |
|------|-------------|--------|
| Operator prompts (Prompts 00, 01, 02, 03, 04, 08) | PR #7 | NOT_YET_CREATED |
| Final validation and analyzer prompts (Prompts 12, 13, 14, 15) | PR #8 | NOT_YET_CREATED |
| Output bundle contract schemas | PR #9 | NOT_YET_CREATED |
| Homepage non-production draft contract | PR #10 | NOT_YET_CREATED |
| Homepage evidence map | Future PR | NOT_YET_CREATED |
| Validator | Future PR | NOT_YET_CREATED |
| Final runnable handoff | Future PR | NOT_YET_CREATED |

**If any gate above is not met: STOP. Do not produce schema output.**

---

## Non-authorization

This preflight checklist does not authorize schema output. It does not authorize JSON-LD generation. It does not authorize current website implementation or Astro attachment. All gates above must be met and all items checked before any schema work may begin.
