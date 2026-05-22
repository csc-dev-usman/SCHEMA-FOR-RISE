# Current Active Files — Rise FC Standalone Schema Operator Package

**Status:** `CLAUDE_QA_CONTROLLER_CONTRACTS_ADDED_NO_SCHEMA_OUTPUT`

> PR #1 created the package shell. PR #2 added the governing doctrine and source-truth boundary. PR #3 added the read-only homepage scoped truth-pack reference. PR #4 added the homepage schema profile, blocked module policy, and reference lists. PR #5 added the standalone schema master flow. PR #6 added the operator navigation decision tree, preflight checklist, and mode status guide. PR #7 added core operator prompt templates (Prompts 00–04, 08). PR #8 added the final validation, analyzer, and completion prompt templates (Prompts 12–15). PR #9 added output bundle contract schemas to `06_MACHINE_RULES/`. PR #10 added the controlled homepage non-production JSON-LD draft contract to `05_REFERENCE_WORKFLOW/`. PR #11 added the output bundle validator to `tools/`. PR #12 adds the Claude QA finding schema, controller review packet schema, QA/controller workflow, and controller decision enum reference. No schema has been generated. No prompts have been executed. Evidence maps and the final runnable handoff are still later PRs.

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
| `04_OPERATOR_PROMPTS/PROMPT_12_FINAL_VALIDATION_AND_IMPLEMENTATION_SCHEMA_V1_0.txt` | Prompt 12 — Final validation and implementation schema — post human approval only. |
| `04_OPERATOR_PROMPTS/PROMPT_13_FIRST_REAL_PAGE_INDEPENDENT_ANALYZER_REVIEW_V1_0.txt` | Prompt 13 — Independent analyzer review — fresh session, no prior context. |
| `04_OPERATOR_PROMPTS/PROMPT_14_CONTROLLER_POST_ANALYZER_DECISION_V1_0.txt` | Prompt 14 — Controller post-analyzer decision (adds PATCH_REQUIRED). |
| `04_OPERATOR_PROMPTS/PROMPT_15_MODE_1_LANE_COMPLETION_AUDIT_V1_0.txt` | Prompt 15 — Mode 1 lane completion audit and RUN_LEDGER entry. |

---

## Active reference-workflow files (PR #10 and PR #12)

| File | Purpose |
|------|---------|
| `05_REFERENCE_WORKFLOW/README_REFERENCE_WORKFLOW_V1_0.md` | Reference workflow folder index. Documentation contracts only — no JSON-LD, no draft. |
| `05_REFERENCE_WORKFLOW/CONTROLLED_HOMEPAGE_NON_PRODUCTION_JSONLD_DRAFT_CONTRACT_V1_0.md` | Draft contract — rules, allowed modules, blocked modules, held fields, governance rules. |
| `05_REFERENCE_WORKFLOW/HOMEPAGE_DRAFT_PRECONDITIONS_AND_HOLD_MATRIX_V1_0.md` | All preconditions required before drafting begins. Full hold matrix for all 14 held field categories. |
| `05_REFERENCE_WORKFLOW/HOMEPAGE_DRAFT_OUTPUT_FILE_LIST_V1_0.md` | Planned output file names and shapes — no files created yet. |
| `05_REFERENCE_WORKFLOW/HOMEPAGE_DRAFT_REVIEW_AND_APPROVAL_SEQUENCE_V1_0.md` | Full 10-step review and approval sequence from readiness gate through implementation handoff. |
| `05_REFERENCE_WORKFLOW/CLAUDE_QA_AND_CONTROLLER_REVIEW_WORKFLOW_V1_0.md` | Claude QA and controller review workflow — what QA is, what it is not, session rules, controller rules. Added PR #12. |
| `05_REFERENCE_WORKFLOW/CONTROLLER_DECISION_ENUM_REFERENCE_V1_0.md` | Authoritative reference for all valid controller decision values — per-finding dispositions and final recommendations. Added PR #12. |

---

## Active machine-rules files (PR #9, PR #11, and PR #12)

| File | Purpose |
|------|---------|
| `06_MACHINE_RULES/README_MACHINE_RULES_V1_0.md` | Machine rules folder index. Contract schema definitions and validator tooling. |
| `06_MACHINE_RULES/OUTPUT_BUNDLE_MANIFEST_SCHEMA_V1_0.json` | Contract schema — required shape of a run output bundle manifest. |
| `06_MACHINE_RULES/RUN_METADATA_SCHEMA_V1_0.json` | Contract schema — required shape of a run metadata record. |
| `06_MACHINE_RULES/CONTROLLER_DECISION_SCHEMA_V1_0.json` | Contract schema — allowed controller decisions and required fields for Prompt 03 and Prompt 14. |
| `06_MACHINE_RULES/VALIDATOR_RESULTS_SCHEMA_V1_0.json` | Contract schema — required shape of external validator result sets from Prompt 04. |
| `06_MACHINE_RULES/EVIDENCE_MAP_SCHEMA_V1_0.json` | Contract schema — required shape of a future evidence map run artifact. Schema added; no evidence map run artifact exists yet. |
| `06_MACHINE_RULES/RISE_SCHEMA_LINT_RULES_V1_0.json` | Lint rules — allowed modules, blocked modules, held field categories, and 10 JSON-LD safety rules. |
| `06_MACHINE_RULES/OUTPUT_BUNDLE_VALIDATOR_RULES_V1_0.md` | Validation rules for the output bundle validator — RULE_VAL_001 through RULE_VAL_007. Added PR #11. |
| `06_MACHINE_RULES/OUTPUT_BUNDLE_VALIDATOR_EXPECTED_FILES_V1_0.json` | Machine-readable expected file list contract for validator — required, conditional, and blocked files. Added PR #11. |
| `06_MACHINE_RULES/CLAUDE_QA_FINDING_SCHEMA_V1_0.json` | Contract schema — required shape of a Claude QA finding record. Severity, category, claim, evidence, recommendation, controller disposition. Added PR #12. |
| `06_MACHINE_RULES/CONTROLLER_REVIEW_PACKET_SCHEMA_V1_0.json` | Contract schema — required shape of a controller review packet. Per-finding dispositions, final recommendation, patch/human-review flags. Added PR #12. |

---

## Active tools files (PR #11)

| File | Purpose |
|------|---------|
| `tools/validate_output_bundle.py` | Python standard-library output bundle validator. Checks required files, JSON validity, truth fingerprint, blocked modules, held fields, production lock, and safety booleans. Does not create or modify output bundles. |
| `tools/README_OUTPUT_BUNDLE_VALIDATOR_V1_0.md` | Operator README for the output bundle validator. Usage, exit codes, check descriptions, non-authorization statement. |

---

## Active placeholder directories

| Directory | Status | Purpose |
|-----------|--------|---------|
| `08_SMOKE_TESTS/` | Future PR | Smoke test files |

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
- **PR #8:** ~~Final validation, analyzer, and completion prompts~~ ✓ Done
- **PR #9:** ~~Output bundle contract schemas~~ ✓ Done
- **PR #10:** ~~Controlled homepage non-production JSON-LD draft contract~~ ✓ Done
- **PR #11:** ~~Output bundle validator~~ ✓ Done
- **PR #12:** ~~Claude QA finding schema and controller review contracts~~ ✓ Done
- **PR #13:** Final schema validation protocol and validator runbook

Generated schema, evidence maps, real run artifacts, and smoke tests are still not allowed. They require a future governed run after all preconditions are confirmed.
