# Operator Checklist — Rise FC Standalone Schema Run

**Status:** `DISABLED — NOT_RUNNABLE_YET_OUTPUT_BUNDLE_SCHEMAS_ADDED`

> This checklist is not yet active. Do not attempt to run the schema workflow after PR #9. The checklist items below are provided for reference only and will be enabled when a later PR merges the final runnable handoff.

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
- [ ] Confirm the quickstart/checklist upgrade (PR #6) has been merged ✓ Done
- [ ] Confirm you have read `00_START_HERE/RISE_OPERATOR_NAVIGATION_DECISION_TREE_V1_0.md`
- [ ] Confirm you have used `00_START_HERE/RISE_SCHEMA_OPERATOR_PREFLIGHT_CHECKLIST_V1_0.md` and all gates pass
- [ ] Confirm you have read `00_START_HERE/RISE_MODE_STATUS_AND_NEXT_STEP_GUIDE_V1_0.md`
- [ ] Confirm the master flow has been read (`01_MASTER_FLOW/RISE_STANDALONE_SCHEMA_MASTER_FLOW_V1_0.md`)
- [ ] Confirm the page run sequence has been read (`01_MASTER_FLOW/RISE_SCHEMA_PAGE_RUN_SEQUENCE_V1_0.md`)
- [ ] Confirm the master stop conditions have been read (`01_MASTER_FLOW/RISE_SCHEMA_MASTER_STOP_CONDITIONS_V1_0.md`)
- [ ] Confirm Mode 1 flow has been read (`01_MASTER_FLOW/MODE_1_CURRENT_WEBSITE_SCHEMA_OPTIMIZATION_FLOW_V1_0.md`)
- [ ] Confirm the operator prompts (PR #7) have been merged ✓ Done
- [ ] Confirm the operator prompt README has been read (`04_OPERATOR_PROMPTS/README_OPERATOR_PROMPTS_V1_0.md`)
- [ ] Confirm Prompt 00 has been read (`04_OPERATOR_PROMPTS/PROMPT_00_STANDALONE_URL_REVIEW_START_V1_0.txt`)
- [ ] Confirm Prompt 08 has been read (`04_OPERATOR_PROMPTS/PROMPT_08_PAGE_CONTENT_READINESS_GATE_V1_0.txt`)
- [ ] Confirm Prompt 01 has been read (`04_OPERATOR_PROMPTS/PROMPT_01_BUILD_NON_PRODUCTION_JSONLD_DRAFT_V1_0.txt`)
- [ ] Confirm Prompt 02 has been read (`04_OPERATOR_PROMPTS/PROMPT_02_CLAUDE_EXTERNAL_QA_ONE_ZIP_V1_0.txt`)
- [ ] Confirm Prompt 03 has been read (`04_OPERATOR_PROMPTS/PROMPT_03_CONTROLLER_DECISION_AND_REGENERATION_V1_0.txt`)
- [ ] Confirm Prompt 04 has been read (`04_OPERATOR_PROMPTS/PROMPT_04_VALIDATOR_RESULTS_REVIEW_V1_0.txt`)
- [ ] Confirm the final validation/analyzer prompts (PR #8) have been merged ✓ Done
- [ ] Confirm Prompt 13 has been read (`04_OPERATOR_PROMPTS/PROMPT_13_FIRST_REAL_PAGE_INDEPENDENT_ANALYZER_REVIEW_V1_0.txt`)
- [ ] Confirm Prompt 14 has been read (`04_OPERATOR_PROMPTS/PROMPT_14_CONTROLLER_POST_ANALYZER_DECISION_V1_0.txt`)
- [ ] Confirm Prompt 12 has been read (`04_OPERATOR_PROMPTS/PROMPT_12_FINAL_VALIDATION_AND_IMPLEMENTATION_SCHEMA_V1_0.txt`)
- [ ] Confirm Prompt 15 has been read (`04_OPERATOR_PROMPTS/PROMPT_15_MODE_1_LANE_COMPLETION_AUDIT_V1_0.txt`)
- [ ] Confirm the output bundle contract schemas (PR #9) have been merged ✓ Done
- [ ] Confirm the machine rules README has been read (`06_MACHINE_RULES/README_MACHINE_RULES_V1_0.md`)
- [ ] Confirm the output bundle manifest schema has been read (`06_MACHINE_RULES/OUTPUT_BUNDLE_MANIFEST_SCHEMA_V1_0.json`)
- [ ] Confirm the run metadata schema has been read (`06_MACHINE_RULES/RUN_METADATA_SCHEMA_V1_0.json`)
- [ ] Confirm the controller decision schema has been read (`06_MACHINE_RULES/CONTROLLER_DECISION_SCHEMA_V1_0.json`)
- [ ] Confirm the validator results schema has been read (`06_MACHINE_RULES/VALIDATOR_RESULTS_SCHEMA_V1_0.json`)
- [ ] Confirm the evidence map schema has been read (`06_MACHINE_RULES/EVIDENCE_MAP_SCHEMA_V1_0.json`)
- [ ] Confirm the lint rules have been read (`06_MACHINE_RULES/RISE_SCHEMA_LINT_RULES_V1_0.json`)
- [ ] Confirm the controlled homepage non-production JSON-LD draft contract (PR #10) has been merged

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
| PR #6 | Team quickstart and operator checklist upgrades | ✓ Done |
| PR #7 | Operator prompts 00 through 04 and 08 | ✓ Done |
| PR #8 | Final validation, analyzer, and completion prompts | ✓ Done |
| PR #9 | Output bundle contract schemas | ✓ Done |
| PR #10 | Controlled homepage non-production JSON-LD draft contract | Pending |

This checklist will be updated and activated when a later PR merges the final runnable handoff.
