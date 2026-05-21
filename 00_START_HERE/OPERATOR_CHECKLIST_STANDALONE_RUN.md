# Operator Checklist — Rise FC Standalone Schema Run

**Status:** `DISABLED — NOT_RUNNABLE_YET_DOCTRINE_ADDED`

> This checklist is not yet active. Do not attempt to run the schema workflow after PR #2. The checklist items below are provided for reference only and will be enabled when PR #5 merges the final runnable handoff.

---

## Before you start

- [ ] Confirm you have read `README_COMPLETE_OPERATOR_PACKAGE.md`
- [ ] Confirm you have read `00_START_HERE/FINAL_STANDALONE_OPERATING_MANUAL_INDEX_V1_0.md`
- [ ] Confirm you have read `00_START_HERE/TEAM_QUICKSTART_STANDALONE_URL_REVIEW.md`
- [ ] Confirm PR #5 (runnable handoff) has been merged
- [ ] Confirm the governing doctrine (PR #2) has been merged ✓ Done
- [ ] Confirm the source-truth boundary has been read (`02_GOVERNING_DOCTRINE/RISE_SCHEMA_SOURCE_TRUTH_BOUNDARY_V1_0.md`)
- [ ] Confirm the governing doctrine has been read (`02_GOVERNING_DOCTRINE/RISE_SCHEMA_GOVERNING_DOCTRINE_V1_0.md`)
- [ ] Confirm the lane ownership rules have been read (`02_GOVERNING_DOCTRINE/RISE_SCHEMA_OPERATOR_LANE_OWNERSHIP_V1_0.md`)
- [ ] Confirm the hold rules have been read (`02_GOVERNING_DOCTRINE/RISE_SCHEMA_NON_AUTHORIZATION_AND_HOLD_RULES_V1_0.md`)
- [ ] Confirm the Phase 0 truth source map (PR #3) has been merged
- [ ] Confirm the operator prompts (PR #4) have been merged

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
| PR #3 | Phase 0 truth source map and homepage scoped truth view | Pending |
| PR #4 | Operator prompts and machine rules | Pending |
| PR #5 | Validators, smoke tests, and final runnable handoff | Pending |

This checklist will be updated and activated when PR #5 is merged.
