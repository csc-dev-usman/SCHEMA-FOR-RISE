# Operator Checklist — Rise FC Standalone Schema Run

**Status:** `DISABLED — NOT_RUNNABLE_YET_MASTER_FLOW_ADDED`

> This checklist is not yet active. Do not attempt to run the schema workflow after PR #5. The checklist items below are provided for reference only and will be enabled when a later PR merges the final runnable handoff.

---

## Before you start

- [ ] Confirm you have read `README_COMPLETE_OPERATOR_PACKAGE.md`
- [ ] Confirm you have read `00_START_HERE/FINAL_STANDALONE_OPERATING_MANUAL_INDEX_V1_0.md`
- [ ] Confirm you have read `00_START_HERE/TEAM_QUICKSTART_STANDALONE_URL_REVIEW.md`
- [ ] Confirm PR #6 (runnable handoff) has been merged
- [ ] Confirm the governing doctrine (PR #2) has been merged ✓ Done
- [ ] Confirm the source-truth boundary has been read (`02_GOVERNING_DOCTRINE/RISE_SCHEMA_SOURCE_TRUTH_BOUNDARY_V1_0.md`)
- [ ] Confirm the governing doctrine has been read (`02_GOVERNING_DOCTRINE/RISE_SCHEMA_GOVERNING_DOCTRINE_V1_0.md`)
- [ ] Confirm the lane ownership rules have been read (`02_GOVERNING_DOCTRINE/RISE_SCHEMA_OPERATOR_LANE_OWNERSHIP_V1_0.md`)
- [ ] Confirm the hold rules have been read (`02_GOVERNING_DOCTRINE/RISE_SCHEMA_NON_AUTHORIZATION_AND_HOLD_RULES_V1_0.md`)
- [ ] Confirm the Phase 0 truth source map (PR #3) has been merged ✓ Done
- [ ] Confirm the Phase 0 truth source map has been read (`03_TRUTH_PACK/RISE_PHASE0_TRUTH_SOURCE_MAP_V1_0.md`)
- [ ] Confirm the homepage scoped truth view has been read (`03_TRUTH_PACK/RISE_PHASE0_SCHEMA_TRUTH_VIEW_HOMEPAGE_SCOPED_V1_0.json`)
- [ ] Confirm the homepage truth fingerprint lock has been read (`03_TRUTH_PACK/RISE_HOMEPAGE_TRUTH_FINGERPRINT_LOCK_V1_0.md`)
- [ ] Confirm the owner approval worksheet has been read (`03_TRUTH_PACK/RISE_CONTACT_SOCIAL_LOGO_OWNER_APPROVAL_WORKSHEET_V1_0.md`)
- [ ] Confirm no held fields are being emitted in any schema draft
- [ ] Confirm the truth-pack backlog has been checked for current page scope (`03_TRUTH_PACK/TRUTH_PACK_BACKLOG.md`)
- [ ] Confirm the homepage schema profile (PR #4) has been merged ✓ Done
- [ ] Confirm the homepage schema profile has been read (`07_REFERENCE_LISTS/RISE_HOMEPAGE_SCHEMA_PROFILE_V1_0.md`)
- [ ] Confirm the blocked module policy has been read (`07_REFERENCE_LISTS/RISE_BLOCKED_SCHEMA_MODULES_FIRST_PAGE_V1_0.md`)
- [ ] Confirm the held field categories have been read (`07_REFERENCE_LISTS/RISE_HELD_FIELD_CATEGORIES_FIRST_PAGE_V1_0.md`)
- [ ] Confirm the allowed modules list has been read (`07_REFERENCE_LISTS/RISE_FIRST_PAGE_ALLOWED_MODULES_V1_0.md`)
- [ ] Confirm the schema profile decision matrix has been read (`07_REFERENCE_LISTS/RISE_SCHEMA_PROFILE_DECISION_MATRIX_V1_0.md`)
- [ ] Confirm the active schema profile is `HOMEPAGE_SCHEMA_PROFILE` for route `/`
- [ ] Confirm no held fields are being emitted (all 15 held field categories default to NOT_REVIEWED_HELD)
- [ ] Confirm the standalone master flow (PR #5) has been merged ✓ Done
- [ ] Confirm the master flow has been read (`01_MASTER_FLOW/RISE_STANDALONE_SCHEMA_MASTER_FLOW_V1_0.md`)
- [ ] Confirm the page run sequence has been read (`01_MASTER_FLOW/RISE_SCHEMA_PAGE_RUN_SEQUENCE_V1_0.md`)
- [ ] Confirm the master stop conditions have been read (`01_MASTER_FLOW/RISE_SCHEMA_MASTER_STOP_CONDITIONS_V1_0.md`)
- [ ] Confirm Mode 1 flow has been read (`01_MASTER_FLOW/MODE_1_CURRENT_WEBSITE_SCHEMA_OPTIMIZATION_FLOW_V1_0.md`)
- [ ] Confirm the operator prompts (PR #7) have been merged

**If any of the above are not true: STOP. Do not proceed.**

---

## Confirm repo health

- [ ] You are in the correct repo (`csc-dev-usman/SCHEMA-FOR-RISE` or its successor)
- [ ] You are on the correct working branch (not `main`)
- [ ] `package_manifest.json` is present and parses cleanly
- [ ] `RUN_LEDGER.json` is present and parses cleanly
- [ ] No unexpected files have been added to the repo

---

## Confirm source truth

- [ ] You have a confirmed Phase 0 source reference for the target page
- [ ] You have a confirmed schema truth view or scoped derivation
- [ ] You have a confirmed evidence map for the target page
- [ ] You have a confirmed schema profile (e.g., `HOMEPAGE_SCHEMA_PROFILE`)
- [ ] No content fields have been invented — all fields trace to Phase 0 or confirmed page evidence

---

## Confirm page candidate

- [ ] Target page is confirmed (e.g., homepage `/`)
- [ ] Target route is confirmed
- [ ] Target schema profile is confirmed and approved
- [ ] Allowed modules are confirmed (first-page lane: Organization, WebSite, WebPage, BreadcrumbList only)

---

## Confirm blocked modules

None of the following are included in the current schema profile:

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

## Do not run yet

**This checklist is disabled after PR #1.**

Operators must not:
- Generate any JSON-LD
- Create any schema output
- Create any production schema bundles
- Run the schema operator workflow
- Commit real run artifacts

---

## What later PRs will add

| PR | What it adds | Status |
|----|-------------|--------|
| PR #2 | Governing doctrine and source-truth boundary | ✓ Done |
| PR #3 | Phase 0 truth source map and homepage scoped truth view | ✓ Done |
| PR #4 | Homepage schema profile and blocked module policy | ✓ Done |
| PR #5 | Standalone schema master flow | ✓ Done |
| PR #6 | Team quickstart and operator checklist upgrades | Pending |
| PR #7 | Operator prompts 00 through 04 and 08 | Pending |
| PR #8 | Final validation, analyzer, and completion prompts | Pending |
| PR #9 | Output bundle contract schemas | Pending |
| PR #10 | Controlled homepage non-production JSON-LD draft contract | Pending |

This checklist will be updated and activated when a later PR merges the final runnable handoff.
