# Current Active Files — Rise FC Standalone Schema Operator Package

**Status:** `CORE_OPERATOR_PROMPTS_ADDED_NO_SCHEMA_OUTPUT`

> PR #1 created the package shell. PR #2 added the governing doctrine and source-truth boundary. PR #3 added the read-only homepage scoped truth-pack reference. PR #4 added the homepage schema profile, blocked module policy, and reference lists. PR #5 added the standalone schema master flow. PR #6 added the operator navigation decision tree, preflight checklist, and mode status guide. PR #7 adds core operator prompt templates (Prompts 00, 01, 02, 03, 04, and 08) as templates only. No schema has been generated. No prompts have been executed. Evidence maps, final validation prompts, output bundle schemas, the draft contract, validators, and the final runnable handoff are still later PRs.

---

## Active package root

| File | Purpose |
|------|---------|
| `README_COMPLETE_OPERATOR_PACKAGE.md` | Root package README. Read first. |
| `package_manifest.json` | Machine-readable package manifest. Status, modes, blocked modules. |
| `RUN_LEDGER.json` | Run ledger. Currently empty — no runs have occurred. |
| `DOCTRINE_VERSION_LEDGER.md` | Doctrine and version history. PR log. |

---

## Active start files

| File | Purpose |
|------|---------|
| `00_START_HERE/CURRENT_ACTIVE_FILES.md` | This file. Active file index. |
| `00_START_HERE/FINAL_STANDALONE_OPERATING_MANUAL_INDEX_V1_0.md` | Operator reading order and manual index. |
| `00_START_HERE/TEAM_QUICKSTART_STANDALONE_URL_REVIEW.md` | Plain-language quickstart for team members. |
| `00_START_HERE/OPERATOR_CHECKLIST_STANDALONE_RUN.md` | Pre-run checklist. Currently disabled — not runnable yet. |
| `00_START_HERE/FINAL_MODE_1_RUNNABLE_HANDOFF_V1_0.md` | Mode 1 handoff placeholder. Not runnable yet. |
| `00_START_HERE/RISE_OPERATOR_NAVIGATION_DECISION_TREE_V1_0.md` | Navigation aid — which document to read for each task |
| `00_START_HERE/RISE_SCHEMA_OPERATOR_PREFLIGHT_CHECKLIST_V1_0.md` | Preflight checklist — all gates required before schema production |
| `00_START_HERE/RISE_MODE_STATUS_AND_NEXT_STEP_GUIDE_V1_0.md` | Current Mode 1 and Mode 2 status and next steps |

---

## Active governing doctrine files (PR #2)

| File | Purpose |
|------|---------|
| `02_GOVERNING_DOCTRINE/README_GOVERNING_DOCTRINE_V1_0.md` | Doctrine folder index and reading order |
| `02_GOVERNING_DOCTRINE/RISE_SCHEMA_SOURCE_TRUTH_BOUNDARY_V1_0.md` | Source-truth hierarchy and stop conditions |
| `02_GOVERNING_DOCTRINE/RISE_SCHEMA_GOVERNING_DOCTRINE_V1_0.md` | Main operating doctrine |
| `02_GOVERNING_DOCTRINE/RISE_SCHEMA_OPERATOR_LANE_OWNERSHIP_V1_0.md` | Lane ownership and cross-lane prohibitions |
| `02_GOVERNING_DOCTRINE/RISE_SCHEMA_NON_AUTHORIZATION_AND_HOLD_RULES_V1_0.md` | Hold rules and blocked fields/modules |

---

## Active truth-pack files (PR #3)

| File | Purpose |
|------|---------|
| `03_TRUTH_PACK/README_TRUTH_PACK_V1_0.md` | Truth-pack folder index and reading order |
| `03_TRUTH_PACK/RISE_PHASE0_TRUTH_SOURCE_MAP_V1_0.md` | Source map defining truth classes needed by schema operators |
| `03_TRUTH_PACK/RISE_PHASE0_SCHEMA_TRUTH_VIEW_HOMEPAGE_SCOPED_V1_0.json` | Read-only homepage scoped truth-view reference. **Not JSON-LD. Not schema output.** |
| `03_TRUTH_PACK/RISE_HOMEPAGE_TRUTH_FINGERPRINT_LOCK_V1_0.md` | Fingerprint lock for homepage truth-view currency verification |
| `03_TRUTH_PACK/RISE_CONTACT_SOCIAL_LOGO_OWNER_APPROVAL_WORKSHEET_V1_0.md` | Owner approval worksheet — all held fields default to NOT_REVIEWED |
| `03_TRUTH_PACK/TRUTH_PACK_BACKLOG.md` | Future truth-pack additions for other pages and routes |

---

## Active reference-list files (PR #4)

| File | Purpose |
|------|---------|
| `07_REFERENCE_LISTS/README_REFERENCE_LISTS_V1_0.md` | Reference-lists folder index and reading order |
| `07_REFERENCE_LISTS/RISE_HOMEPAGE_SCHEMA_PROFILE_V1_0.md` | Active homepage schema profile — `HOMEPAGE_SCHEMA_PROFILE` for route `/` |
| `07_REFERENCE_LISTS/RISE_FIRST_PAGE_ALLOWED_MODULES_V1_0.md` | Allowed future modules for first-page lane with per-module evidence requirements |
| `07_REFERENCE_LISTS/RISE_BLOCKED_SCHEMA_MODULES_FIRST_PAGE_V1_0.md` | Blocked module policy with block reasons and unblocking requirements |
| `07_REFERENCE_LISTS/RISE_HELD_FIELD_CATEGORIES_FIRST_PAGE_V1_0.md` | All 15 held field categories — all default to NOT_REVIEWED_HELD |
| `07_REFERENCE_LISTS/RISE_SCHEMA_PROFILE_DECISION_MATRIX_V1_0.md` | Decision matrix for profile selection, PROCEED_* and HOLD_* outcomes |

---

## Active master-flow files (PR #5)

| File | Purpose |
|------|---------|
| `01_MASTER_FLOW/README_MASTER_FLOW_V1_0.md` | Master-flow folder index and reading order |
| `01_MASTER_FLOW/RISE_STANDALONE_SCHEMA_MASTER_FLOW_V1_0.md` | Root master flow — source-truth hierarchy, modes, homepage lane, sequence, stop conditions |
| `01_MASTER_FLOW/MODE_1_CURRENT_WEBSITE_SCHEMA_OPTIMIZATION_FLOW_V1_0.md` | Mode 1 current-site optimization flow — documented, not runnable yet |
| `01_MASTER_FLOW/MODE_2_FUTURE_ASTRO_SCHEMA_CARRY_FLOW_V1_0.md` | Mode 2 future Astro carry flow — documented, not ready |
| `01_MASTER_FLOW/RISE_SCHEMA_PAGE_RUN_SEQUENCE_V1_0.md` | Per-page run sequence from intake through implementation or Astro handoff |
| `01_MASTER_FLOW/RISE_SCHEMA_MASTER_STOP_CONDITIONS_V1_0.md` | All master stop conditions with resolution rules |

---

## Active operator prompt files (PR #7)

| File | Purpose |
|------|---------|
| `04_OPERATOR_PROMPTS/README_OPERATOR_PROMPTS_V1_0.md` | Operator prompts folder index. Templates only — not executed. |
| `04_OPERATOR_PROMPTS/PROMPT_00_STANDALONE_URL_REVIEW_START_V1_0.txt` | Prompt 00 — Intake and run context. Collect target, truth state, profile, blocked modules, held fields, evidence map status. |
| `04_OPERATOR_PROMPTS/PROMPT_01_BUILD_NON_PRODUCTION_JSONLD_DRAFT_V1_0.txt` | Prompt 01 — Build non-production JSON-LD draft from confirmed evidence. |
| `04_OPERATOR_PROMPTS/PROMPT_02_CLAUDE_EXTERNAL_QA_ONE_ZIP_V1_0.txt` | Prompt 02 — Claude external QA one-zip review. |
| `04_OPERATOR_PROMPTS/PROMPT_03_CONTROLLER_DECISION_AND_REGENERATION_V1_0.txt` | Prompt 03 — Controller decision (ACCEPT / MODIFY / REJECT / DEFER / HUMAN_REVIEW_REQUIRED). |
| `04_OPERATOR_PROMPTS/PROMPT_04_VALIDATOR_RESULTS_REVIEW_V1_0.txt` | Prompt 04 — Validator results review (Google Rich Results Test, Schema.org validator, Screaming Frog). |
| `04_OPERATOR_PROMPTS/PROMPT_08_PAGE_CONTENT_READINESS_GATE_V1_0.txt` | Prompt 08 — Page content readiness gate. Runs before Prompt 01. |

---

## Active placeholder directories

| Directory | Status | Purpose |
|-----------|--------|---------|
| `05_REFERENCE_WORKFLOW/` | Pending PR #10 | Reference workflow documents |
| `06_MACHINE_RULES/` | Pending PR #9 | Output bundle contract schemas |
| `08_SMOKE_TESTS/` | Future PR | Smoke test files |
| `tools/` | Placeholder only | Future tooling scripts |

---

## Active ledger

| File | Status |
|------|--------|
| `RUN_LEDGER.json` | `BOOTSTRAP_EMPTY_NO_RUNS` — no runs recorded |

---

## Blocked files and artifacts — not allowed yet

The following file types and artifacts are **not permitted** in this repository at bootstrap status:

| Blocked artifact | Reason |
|-----------------|--------|
| JSON-LD output files | Not authorized until governed output workflow exists |
| Schema output bundles | Not authorized until validators and truth-pack are in place |
| `sample_runs/` directory | Not authorized — real run artifacts only after governed runs |
| Real run artifacts | Not authorized until runnable handoff exists |
| Validator screenshots | Not authorized yet |
| Screaming Frog exports | Not authorized yet |
| Claude QA zips | Not authorized yet |
| Generated schema files | Not authorized — no schema has been generated |
| Astro implementation files | Not authorized until Astro carry gates are defined |
| Website source files | Not part of this package |
| Runtime source files | Not part of this package |
| Medical or CSC-specific doctrine | Not applicable to Rise FC |
| Fake package validation tools | Not permitted |
| Fake passing reports | Not permitted |

---

## What later PRs will add

- **PR #2:** ~~Governing doctrine and source-truth boundary~~ ✓ Done
- **PR #3:** ~~Phase 0 truth source map and homepage scoped truth view~~ ✓ Done
- **PR #4:** ~~Homepage schema profile and blocked module policy~~ ✓ Done
- **PR #5:** ~~Standalone schema master flow~~ ✓ Done
- **PR #6:** ~~Team quickstart and operator checklist upgrades~~ ✓ Done
- **PR #7:** ~~Operator prompts 00 through 04 and 08~~ ✓ Done
- **PR #8:** Final validation, analyzer, and completion prompts
- **PR #9:** Output bundle contract schemas
- **PR #10:** Controlled homepage non-production JSON-LD draft contract

Generated schema, output bundle schemas, evidence maps, real run artifacts, and smoke tests are still not allowed. They require PR #8 and later.
