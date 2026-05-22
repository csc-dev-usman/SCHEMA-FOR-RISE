# Current Active Files — Rise FC Standalone Schema Operator Package

**Status:** `MILESTONE_3_LEDGER_AND_HEALTH_TOOLS_COMPLETE_NO_SCHEMA_OUTPUT`

> PR #1 created the package shell. PRs #2–#16 added governing doctrine, truth pack, schema profiles, master flow, operator prompts, contract schemas, validators, run ledger infrastructure, and package validator. PR #17 added the smoke-test fixture contract and canned fake fixture set in `08_SMOKE_TESTS/`. PR #18 adds the smoke test runner, package health reporter, smoke test runner expectations, and the Milestone 3 completion audit. Milestone 3 is tooling-complete. No schema has been generated. No prompts have been executed. Evidence maps and the final runnable handoff are still later PRs.

---

## Active package root

| File | Purpose |
|------|---------|
| `README_COMPLETE_OPERATOR_PACKAGE.md` | Root package README. Read first. |
| `package_manifest.json` | Machine-readable package manifest. Status, modes, blocked modules. |
| `RUN_LEDGER.json` | Run ledger. Upgraded PR #14 — empty entries, `schemaVersion`, `ledgerStatus`, `productionLockStatus` added. No runs recorded. |
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

## Active reference-workflow files (PR #10, PR #12, PR #13, and PR #14)

| File | Purpose |
|------|---------|
| `05_REFERENCE_WORKFLOW/README_REFERENCE_WORKFLOW_V1_0.md` | Reference workflow folder index. Documentation contracts only — no JSON-LD, no draft. |
| `05_REFERENCE_WORKFLOW/CONTROLLED_HOMEPAGE_NON_PRODUCTION_JSONLD_DRAFT_CONTRACT_V1_0.md` | Draft contract — rules, allowed modules, blocked modules, held fields, governance rules. |
| `05_REFERENCE_WORKFLOW/HOMEPAGE_DRAFT_PRECONDITIONS_AND_HOLD_MATRIX_V1_0.md` | All preconditions required before drafting begins. Full hold matrix for all 14 held field categories. |
| `05_REFERENCE_WORKFLOW/HOMEPAGE_DRAFT_OUTPUT_FILE_LIST_V1_0.md` | Planned output file names and shapes — no files created yet. |
| `05_REFERENCE_WORKFLOW/HOMEPAGE_DRAFT_REVIEW_AND_APPROVAL_SEQUENCE_V1_0.md` | Full 10-step review and approval sequence from readiness gate through implementation handoff. |
| `05_REFERENCE_WORKFLOW/CLAUDE_QA_AND_CONTROLLER_REVIEW_WORKFLOW_V1_0.md` | Claude QA and controller review workflow — what QA is, what it is not, session rules, controller rules. Added PR #12. |
| `05_REFERENCE_WORKFLOW/CONTROLLER_DECISION_ENUM_REFERENCE_V1_0.md` | Authoritative reference for all valid controller decision values — per-finding dispositions and final recommendations. Added PR #12. |
| `05_REFERENCE_WORKFLOW/FINAL_SCHEMA_VALIDATION_PROTOCOL_V1_0.md` | Ordered 9-step validation protocol from output bundle validation through implementation handoff. Added PR #13. |
| `05_REFERENCE_WORKFLOW/SCHEMA_VALIDATOR_RUNBOOK_V1_0.md` | How to use the Schema.org Validator for future schema bundles (Step 4 of validation protocol). Added PR #13. |
| `05_REFERENCE_WORKFLOW/GOOGLE_RICH_RESULTS_REVIEW_RUNBOOK_V1_0.md` | How to use the Google Rich Results Test. Rich results eligibility not guaranteed. Step 5 is informational only. Added PR #13. |
| `05_REFERENCE_WORKFLOW/SCREAMING_FROG_STRUCTURED_DATA_EXPORT_CHECKLIST_V1_0.md` | Screaming Frog structured data extraction checklist — optional/where available. Step 6 of validation protocol. Added PR #13. |
| `05_REFERENCE_WORKFLOW/VALIDATION_EVIDENCE_HANDOFF_REQUIREMENTS_V1_0.md` | Required evidence metadata for the implementation handoff packet. No actual evidence. Added PR #13. |
| `05_REFERENCE_WORKFLOW/RUN_LEDGER_STANDALONE_SCHEMA_REVIEW_GUIDE_V1_0.md` | How to read the run ledger, field explanations, when PRODUCTION_LOCKED may and may not be claimed. Added PR #14. |

---

## Active machine-rules files (PR #9, PR #11, PR #12, PR #14, and PR #16)

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
| `06_MACHINE_RULES/RUN_LEDGER_SCHEMA_V1_0.json` | Contract schema — required shape of run ledger entries. All fields, allowed status values, safety constraints. Added PR #14. |
| `06_MACHINE_RULES/PACKAGE_VALIDATION_CHECKLIST_V1_0.md` | Manual checklist explaining all 12 package validator checks, rationale, and failure meanings. Added PR #16. |
| `06_MACHINE_RULES/PACKAGE_EXPECTED_ACTIVE_FILES_V1_0.json` | Machine-readable expected file list contract — 80 required files through PR #16, optional files, blocked files. Added PR #16. |

---

## Active smoke-test tool files (PR #18)

| File | Purpose |
|------|---------|
| `tools/run_standalone_smoke_test.py` | Smoke test runner — 12 checks against `08_SMOKE_TESTS/fixtures/standalone_v1_0/`. Verifies fixture integrity and package validator pass. Added PR #18. |
| `tools/report_package_health.py` | Package health reporter — 8 health check sections, read-only. Summarizes manifest, ledger, mode status, safety flags, tool presence. Added PR #18. |
| `tools/README_SMOKE_TEST_AND_HEALTH_TOOLS_V1_0.md` | Operator README for the smoke test runner and health reporter. Usage, exit codes, check tables, non-authorization statement. Added PR #18. |
| `08_SMOKE_TESTS/SMOKE_TEST_RUNNER_EXPECTATIONS_V1_0.md` | Expected PASS/FAIL behavior of the smoke test runner for all 12 checks. Added PR #18. |
| `05_REFERENCE_WORKFLOW/MILESTONE_3_LEDGER_AND_HEALTH_TOOLS_COMPLETION_AUDIT_V1_0.md` | Milestone 3 completion audit — records all Milestone 3 components, tool inventory, validation results, current package posture. Added PR #18. |

---

## Active tools files (PR #11, PR #15, PR #16, and PR #18)

| File | Purpose |
|------|---------|
| `tools/validate_output_bundle.py` | Python standard-library output bundle validator. Checks required files, JSON validity, truth fingerprint, blocked modules, held fields, production lock, and safety booleans. Does not create or modify output bundles. |
| `tools/README_OUTPUT_BUNDLE_VALIDATOR_V1_0.md` | Operator README for the output bundle validator. Usage, exit codes, check descriptions, non-authorization statement. |
| `tools/append_run_ledger_entry.py` | Run ledger append helper. Runs 20 safety checks on a candidate entry JSON file before appending to `RUN_LEDGER.json`. Supports `--dry-run`. Does not generate schema or JSON-LD. Added PR #15. |
| `tools/report_run_ledger_status.py` | Read-only ledger status reporter. Prints ledger metadata, entry counts, status breakdowns, and integrity checks. Does not modify any files. Added PR #15. |
| `tools/README_RUN_LEDGER_TOOLS_V1_0.md` | Operator README for the run ledger tools. Usage, safety checks, exit codes, non-authorization statement. Added PR #15. |
| `tools/validate_package.py` | Package validator. 12 checks — required files, JSON validity, no JSON-LD, no sample_runs, no production readiness claimed, mode1Runnable false, no schema output claimed, ledger lock status, no fake reports, truth view JSON valid. Added PR #16. |
| `tools/README_PACKAGE_VALIDATOR_V1_0.md` | Operator README for the package validator. Usage, checks, exit codes, non-authorization statement. Added PR #16. |

---

## Active smoke-test files (PR #17)

| File | Purpose |
|------|---------|
| `08_SMOKE_TESTS/README_SMOKE_TESTS.md` | Smoke tests folder index. Smoke tests are package/tooling checks only — not schema production checks. |
| `08_SMOKE_TESTS/STANDALONE_SMOKE_TEST_FIXTURE_CONTRACT_V1_0.md` | Contract defining fixture safety rules, required fields, and what fake fixtures may and may not contain. |
| `08_SMOKE_TESTS/fixtures/standalone_v1_0/README_FAKE_FIXTURE.md` | Explanation of what the canned fixture is and is not. |
| `08_SMOKE_TESTS/fixtures/standalone_v1_0/fixture_manifest.json` | Fixture index — lists all fixture files, confirms fake status, records fixture version. |
| `08_SMOKE_TESTS/fixtures/standalone_v1_0/fake_run_metadata.json` | Synthetic run metadata record. Uses `example.invalid`. **Not a real run artifact.** |
| `08_SMOKE_TESTS/fixtures/standalone_v1_0/fake_output_bundle_manifest.json` | Synthetic output bundle manifest. Uses `example.invalid`. **Not a real output bundle.** |
| `08_SMOKE_TESTS/fixtures/standalone_v1_0/fake_controller_decision.json` | Synthetic controller decision record. Uses `example.invalid`. **Not a real controller review.** |
| `08_SMOKE_TESTS/fixtures/standalone_v1_0/fake_validator_results.json` | Synthetic validator results record. Uses `example.invalid`. **Not real validation output.** |

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
- **PR #13:** ~~Final schema validation protocol and validator runbook~~ ✓ Done
- **PR #14:** ~~Governed run ledger schema and RUN_LEDGER upgrade~~ ✓ Done
- **PR #15:** ~~Run ledger append helper and reporter~~ ✓ Done
- **PR #16:** ~~Package validator and active-file coherence checks~~ ✓ Done
- **PR #17:** ~~Smoke-test fixture contract and canned fixture~~ ✓ Done
- **PR #18:** ~~Smoke-test runner and package health reporter~~ ✓ Done
- **PR #19:** Homepage evidence map and first real page handoff template

Generated schema, evidence maps, and real run artifacts are still not allowed. They require a future governed run after all preconditions are confirmed.
