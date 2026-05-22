# Final Standalone Operating Manual Index V1.0

**Status:** `CORE_OPERATOR_PROMPTS_ADDED_NO_SCHEMA_OUTPUT`

> This manual index defines the operator reading order. The full workflow is not yet runnable. Operators must not generate or implement schema until later PRs add truth packs, prompts, contracts, validators, and the final runnable handoff.

---

## Operator reading order

### Step 1 — Read the root README

File: `README_COMPLETE_OPERATOR_PACKAGE.md`

Understand:
- What this package is and is not
- Source truth hierarchy
- Current operating posture
- Mode 1 vs Mode 2
- Hard blocked modules
- Non-authorization statement

### Step 2 — Read CURRENT_ACTIVE_FILES

File: `00_START_HERE/CURRENT_ACTIVE_FILES.md`

Understand:
- What files exist now
- What is blocked
- What later PRs will add

### Step 2b — Read governing doctrine (PR #2 addition)

Files in this order:
1. `02_GOVERNING_DOCTRINE/README_GOVERNING_DOCTRINE_V1_0.md`
2. `02_GOVERNING_DOCTRINE/RISE_SCHEMA_SOURCE_TRUTH_BOUNDARY_V1_0.md`
3. `02_GOVERNING_DOCTRINE/RISE_SCHEMA_GOVERNING_DOCTRINE_V1_0.md`
4. `02_GOVERNING_DOCTRINE/RISE_SCHEMA_OPERATOR_LANE_OWNERSHIP_V1_0.md`
5. `02_GOVERNING_DOCTRINE/RISE_SCHEMA_NON_AUTHORIZATION_AND_HOLD_RULES_V1_0.md`

Understand:
- Source-truth hierarchy and hard boundaries
- Evidence-first and no-invention rules
- Lane ownership and cross-lane prohibitions
- Hold conditions and blocked field/module categories

### Step 2c — Read truth-pack reference (PR #3 addition)

Files in this order:
1. `03_TRUTH_PACK/README_TRUTH_PACK_V1_0.md`
2. `03_TRUTH_PACK/RISE_PHASE0_TRUTH_SOURCE_MAP_V1_0.md`
3. `03_TRUTH_PACK/RISE_PHASE0_SCHEMA_TRUTH_VIEW_HOMEPAGE_SCOPED_V1_0.json`
4. `03_TRUTH_PACK/RISE_HOMEPAGE_TRUTH_FINGERPRINT_LOCK_V1_0.md`
5. `03_TRUTH_PACK/RISE_CONTACT_SOCIAL_LOGO_OWNER_APPROVAL_WORKSHEET_V1_0.md`
6. `03_TRUTH_PACK/TRUTH_PACK_BACKLOG.md`

Understand:
- What truth classes are needed for schema operations
- Homepage scoped truth view is read-only — it is not JSON-LD, not schema output
- Fingerprint lock and freshness rules
- Which fields are held and require owner approval before schema can use them
- What truth-pack additions are needed for future pages

### Step 2d — Read reference lists (PR #4 addition)

Files in this order:
1. `07_REFERENCE_LISTS/README_REFERENCE_LISTS_V1_0.md`
2. `07_REFERENCE_LISTS/RISE_HOMEPAGE_SCHEMA_PROFILE_V1_0.md`
3. `07_REFERENCE_LISTS/RISE_FIRST_PAGE_ALLOWED_MODULES_V1_0.md`
4. `07_REFERENCE_LISTS/RISE_BLOCKED_SCHEMA_MODULES_FIRST_PAGE_V1_0.md`
5. `07_REFERENCE_LISTS/RISE_HELD_FIELD_CATEGORIES_FIRST_PAGE_V1_0.md`
6. `07_REFERENCE_LISTS/RISE_SCHEMA_PROFILE_DECISION_MATRIX_V1_0.md`

Understand:
- Active schema profile for the homepage lane (`HOMEPAGE_SCHEMA_PROFILE`, route `/`)
- Which modules are allowed for future first-page schema (Organization, WebSite, WebPage, BreadcrumbList only)
- Which modules are blocked and why — including the conditions required to unblock them
- Which fields are held and require owner approval before any schema emission
- How the decision matrix drives PROCEED or HOLD outcomes from profile selection through production

---

### Step 2e — Read master flow (PR #5 addition)

Files in this order:
1. `01_MASTER_FLOW/README_MASTER_FLOW_V1_0.md`
2. `01_MASTER_FLOW/RISE_STANDALONE_SCHEMA_MASTER_FLOW_V1_0.md`
3. `01_MASTER_FLOW/MODE_1_CURRENT_WEBSITE_SCHEMA_OPTIMIZATION_FLOW_V1_0.md`
4. `01_MASTER_FLOW/MODE_2_FUTURE_ASTRO_SCHEMA_CARRY_FLOW_V1_0.md`
5. `01_MASTER_FLOW/RISE_SCHEMA_PAGE_RUN_SEQUENCE_V1_0.md`
6. `01_MASTER_FLOW/RISE_SCHEMA_MASTER_STOP_CONDITIONS_V1_0.md`

Understand:
- The full operating sequence from intake through implementation or Astro handoff
- Mode 1 and Mode 2 flows — both documented but not yet runnable
- What upstream artifacts exist and what future artifacts are still required
- The complete master stop conditions and resolution rules for each condition

---

### Step 2f — Read operator navigation and status documents (PR #6 addition)

Files:
1. `00_START_HERE/RISE_OPERATOR_NAVIGATION_DECISION_TREE_V1_0.md` — which document to read for each task
2. `00_START_HERE/RISE_SCHEMA_OPERATOR_PREFLIGHT_CHECKLIST_V1_0.md` — all preflight gates required before schema work
3. `00_START_HERE/RISE_MODE_STATUS_AND_NEXT_STEP_GUIDE_V1_0.md` — current Mode 1 and Mode 2 status

Understand:
- How to navigate to the right document for any task
- What all preflight conditions look like — and which are not yet met
- The current status of Mode 1 and Mode 2 and what is still needed

---

### Step 2g — Read operator prompts (PR #7 addition)

Files in this order:
1. `04_OPERATOR_PROMPTS/README_OPERATOR_PROMPTS_V1_0.md`
2. `04_OPERATOR_PROMPTS/PROMPT_00_STANDALONE_URL_REVIEW_START_V1_0.txt`
3. `04_OPERATOR_PROMPTS/PROMPT_08_PAGE_CONTENT_READINESS_GATE_V1_0.txt`
4. `04_OPERATOR_PROMPTS/PROMPT_01_BUILD_NON_PRODUCTION_JSONLD_DRAFT_V1_0.txt`
5. `04_OPERATOR_PROMPTS/PROMPT_02_CLAUDE_EXTERNAL_QA_ONE_ZIP_V1_0.txt`
6. `04_OPERATOR_PROMPTS/PROMPT_03_CONTROLLER_DECISION_AND_REGENERATION_V1_0.txt`
7. `04_OPERATOR_PROMPTS/PROMPT_04_VALIDATOR_RESULTS_REVIEW_V1_0.txt`

Understand:
- Prompt files are templates only — they have not been executed
- Run order: Prompt 00 → Prompt 08 → Prompt 01 → Prompt 02 → Prompt 03 → Prompt 04
- Each prompt must be run in sequence — no skipping
- No schema is generated by reading these files
- Final validation and analyzer prompts (Prompts 12–15) are pending in PR #8

---

### Step 3 — Read TEAM_QUICKSTART

File: `00_START_HERE/TEAM_QUICKSTART_STANDALONE_URL_REVIEW.md`

Understand:
- Plain-language operating context
- Why this package exists
- What operators can and cannot do right now

### Step 4 — Read OPERATOR_CHECKLIST

File: `00_START_HERE/OPERATOR_CHECKLIST_STANDALONE_RUN.md`

Understand:
- Pre-run checks
- Current disabled status
- What must be in place before running

### Step 5 — Wait for later PRs before running actual schema workflow

The schema workflow is **not runnable after PR #7**.

Operators must wait for:
- PR #2: Governing doctrine ✓ Done
- PR #3: Phase 0 truth source map and homepage scoped truth view ✓ Done
- PR #4: Homepage schema profile and blocked module policy ✓ Done
- PR #5: Standalone schema master flow ✓ Done
- PR #6: Team quickstart and operator checklist upgrades ✓ Done
- PR #7: Operator prompts 00 through 04 and 08 ✓ Done
- PR #8: Final validation, analyzer, and completion prompts
- PR #9: Output bundle contract schemas
- PR #10: Controlled homepage non-production JSON-LD draft contract

Do not generate schema. Do not create JSON-LD. Do not implement on the website.

---

## Mode 1 — Current website goal

Produce validated schema for pages on the current risefcsoccer.com website.

- First-page target: homepage, route `/`, with `HOMEPAGE_SCHEMA_PROFILE`
- Allowed first-page modules (future only): Organization, WebSite, WebPage, BreadcrumbList
- Schema is derived from approved Phase 0 content and confirmed page evidence
- Output must be validated before any implementation handoff

**Not runnable yet. Waiting for PR #8 final validation and analyzer prompts, PR #9 output bundle schemas, PR #10 draft contract, and final runnable handoff.**

---

## Mode 2 — Future Astro goal

Carry validated schema into the Astro implementation after carry gates are defined.

- Blocked until Astro carry gates exist
- No Astro files are modified by this package at bootstrap
- A future PR will define the carry gates and attachment protocol

**Not yet scoped. Waiting for Astro route and runtime evidence.**

---

## Stop conditions

Operators must stop immediately and not proceed if any of the following are true:

| Condition | Action |
|-----------|--------|
| Missing Phase 0 source reference | STOP — do not proceed without Phase 0 anchor |
| Missing schema truth view or scoped derivation | STOP — derive schema only from approved truth view |
| Missing evidence map | STOP — do not create schema profiles without evidence |
| Missing schema profile | STOP — do not generate output without an approved profile |
| Attempted `Review` schema | STOP — blocked module |
| Attempted `AggregateRating` schema | STOP — blocked module |
| Attempted `FAQPage` schema | STOP — blocked module |
| Attempted `Offer` schema | STOP — blocked module |
| Attempted `Event` schema | STOP — blocked module |
| Attempted `Place` schema | STOP — blocked module |
| Attempted `GeoCoordinates` schema | STOP — blocked module |
| Attempted bilingual schema | STOP — blocked module |
| Attempted testimonial-derived schema | STOP — blocked module |
| Attempted production lock without human approval | STOP — production lock requires explicit human authorization |
| Attempted real artifact commit before governed run | STOP — no real run artifacts until runnable handoff exists |
| Attempted Astro attachment before carry gates exist | STOP — Mode 2 not yet authorized |
| Attempted Phase 0 mutation | STOP — Phase 0 is read-only from this package |
| Attempted source truth mutation | STOP — this package is downstream of source truth |
