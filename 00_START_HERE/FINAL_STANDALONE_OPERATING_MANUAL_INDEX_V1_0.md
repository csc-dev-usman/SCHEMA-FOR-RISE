# Final Standalone Operating Manual Index V1.0

**Status:** `ASTRO_ATTACHMENT_PACKET_TEMPLATE_ADDED_NO_SCHEMA_OUTPUT`

> This manual index defines the operator reading order. The full workflow is not yet runnable. Operators must not generate or implement schema until later PRs add evidence maps and the final runnable handoff.

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

### Step 2g — Read operator prompts (PR #7 and PR #8 additions)

Files in run order:
1. `04_OPERATOR_PROMPTS/README_OPERATOR_PROMPTS_V1_0.md`
2. `04_OPERATOR_PROMPTS/PROMPT_00_STANDALONE_URL_REVIEW_START_V1_0.txt`
3. `04_OPERATOR_PROMPTS/PROMPT_08_PAGE_CONTENT_READINESS_GATE_V1_0.txt`
4. `04_OPERATOR_PROMPTS/PROMPT_01_BUILD_NON_PRODUCTION_JSONLD_DRAFT_V1_0.txt`
5. `04_OPERATOR_PROMPTS/PROMPT_02_CLAUDE_EXTERNAL_QA_ONE_ZIP_V1_0.txt`
6. `04_OPERATOR_PROMPTS/PROMPT_03_CONTROLLER_DECISION_AND_REGENERATION_V1_0.txt`
7. `04_OPERATOR_PROMPTS/PROMPT_04_VALIDATOR_RESULTS_REVIEW_V1_0.txt`
8. `04_OPERATOR_PROMPTS/PROMPT_13_FIRST_REAL_PAGE_INDEPENDENT_ANALYZER_REVIEW_V1_0.txt`
9. `04_OPERATOR_PROMPTS/PROMPT_14_CONTROLLER_POST_ANALYZER_DECISION_V1_0.txt`
10. `04_OPERATOR_PROMPTS/PROMPT_12_FINAL_VALIDATION_AND_IMPLEMENTATION_SCHEMA_V1_0.txt`
11. `04_OPERATOR_PROMPTS/PROMPT_15_MODE_1_LANE_COMPLETION_AUDIT_V1_0.txt`

Understand:
- Prompt files are templates only — they have not been executed
- Run order: 00 → 08 → 01 → 02 → 03 → 04 → 13 → 14 → [human approval] → 12 → 15
- Each prompt must be run in sequence — no skipping
- Prompt 13 must run in a fresh session with no prior context
- Prompt 12 requires explicit human approval before it can run
- No schema is generated by reading these files

---

### Step 2h — Read machine rules (PR #9 addition)

Files in this order:
1. `06_MACHINE_RULES/README_MACHINE_RULES_V1_0.md`
2. `06_MACHINE_RULES/OUTPUT_BUNDLE_MANIFEST_SCHEMA_V1_0.json`
3. `06_MACHINE_RULES/RUN_METADATA_SCHEMA_V1_0.json`
4. `06_MACHINE_RULES/CONTROLLER_DECISION_SCHEMA_V1_0.json`
5. `06_MACHINE_RULES/VALIDATOR_RESULTS_SCHEMA_V1_0.json`
6. `06_MACHINE_RULES/EVIDENCE_MAP_SCHEMA_V1_0.json`
7. `06_MACHINE_RULES/RISE_SCHEMA_LINT_RULES_V1_0.json`

Understand:
- These are contract schema definitions — they define the required shape of future run artifacts
- No output bundles, validators, scripts, or JSON-LD have been created
- The evidence map schema contract exists (`evidenceMapSchemaAdded=true`) but no evidence map run artifact exists yet (`evidenceMapAdded=false`)
- Lint rules define allowed modules, blocked modules, held field categories, and 10 JSON-LD safety rules (JLSR_001–JLSR_010)
- All 10 JSON-LD safety rules must be satisfied by every schema draft and implementation

---

### Step 2i — Read reference workflow (PR #10 addition)

Files in this order:
1. `05_REFERENCE_WORKFLOW/README_REFERENCE_WORKFLOW_V1_0.md`
2. `05_REFERENCE_WORKFLOW/CONTROLLED_HOMEPAGE_NON_PRODUCTION_JSONLD_DRAFT_CONTRACT_V1_0.md`
3. `05_REFERENCE_WORKFLOW/HOMEPAGE_DRAFT_PRECONDITIONS_AND_HOLD_MATRIX_V1_0.md`
4. `05_REFERENCE_WORKFLOW/HOMEPAGE_DRAFT_OUTPUT_FILE_LIST_V1_0.md`
5. `05_REFERENCE_WORKFLOW/HOMEPAGE_DRAFT_REVIEW_AND_APPROVAL_SEQUENCE_V1_0.md`

Understand:
- These are documentation contracts only — no JSON-LD, no draft exists
- The draft contract defines allowed modules (Organization, WebSite, WebPage, BreadcrumbList), blocked modules, held fields, and all 10 governance rules
- The preconditions matrix lists every gate that must pass before any draft run begins — including truth fingerprint match, evidence map, schema profile, and readiness gate
- The output file list defines planned file names and shapes — no files have been created
- The 10-step review and approval sequence is the complete governed path from readiness gate through implementation handoff
- Human approval is required at Step 9 before any implementation handoff can occur

---

### Step 2j — Read output bundle validator (PR #11 addition)

Files in this order:
1. `tools/README_OUTPUT_BUNDLE_VALIDATOR_V1_0.md`
2. `06_MACHINE_RULES/OUTPUT_BUNDLE_VALIDATOR_RULES_V1_0.md`
3. `06_MACHINE_RULES/OUTPUT_BUNDLE_VALIDATOR_EXPECTED_FILES_V1_0.json`

Understand:
- The validator is Python standard library only — no third-party packages required
- Run with: `python tools/validate_output_bundle.py <bundle_dir>`
- The validator checks: required files present, JSON validity, truth fingerprint (homepage), blocked modules, held fields without approval, production lock without human approval, safety booleans
- Exit codes: 0=PASS, 1=FAIL, 2=WARN
- The validator does NOT create or modify output bundles
- The validator does NOT generate schema or JSON-LD
- A PASS result is necessary but not sufficient — human review is still required before any implementation action
- The expected-files contract lists all required, conditional, and blocked files for a future output bundle

---

### Step 2k — Read Claude QA and controller review contracts (PR #12 addition)

Files in this order:
1. `05_REFERENCE_WORKFLOW/CLAUDE_QA_AND_CONTROLLER_REVIEW_WORKFLOW_V1_0.md`
2. `05_REFERENCE_WORKFLOW/CONTROLLER_DECISION_ENUM_REFERENCE_V1_0.md`
3. `06_MACHINE_RULES/CLAUDE_QA_FINDING_SCHEMA_V1_0.json`
4. `06_MACHINE_RULES/CONTROLLER_REVIEW_PACKET_SCHEMA_V1_0.json`

Understand:
- Claude QA is a reviewer only — it is not a source of truth for Rise FC
- Claude QA must run in a fresh session with no prior context from the schema generation run
- Claude QA findings use severity levels: BLOCKER, HIGH, MEDIUM, LOW, INFO
- Finding categories: SOURCE_TRUTH, HELD_FIELD, BLOCKED_MODULE, JSONLD_VALIDITY, EVIDENCE_MAP, VALIDATOR_RESULT, ASTRO_CARRY, CURRENT_SITE_IMPLEMENTATION, DOCUMENTATION, OTHER
- Controller dispositions per finding: ACCEPT, MODIFY, REJECT, DEFER, HUMAN_REVIEW_REQUIRED, PATCH_REQUIRED
- Controller final recommendations: PROCEED_TO_HUMAN_APPROVAL, PATCH_REQUIRED, REJECT_RUN, HUMAN_REVIEW_REQUIRED, DEFER_TO_LATER_PR
- The controller cannot mutate Phase 0 and cannot self-approve production
- Human approval at Step 9 is required before any implementation action — controller review does not replace it
- No QA has been run. No findings exist. These are contract definitions only.

---

### Step 2l — Read final schema validation protocol (PR #13 addition)

Files in this order:
1. `05_REFERENCE_WORKFLOW/FINAL_SCHEMA_VALIDATION_PROTOCOL_V1_0.md`
2. `05_REFERENCE_WORKFLOW/SCHEMA_VALIDATOR_RUNBOOK_V1_0.md`
3. `05_REFERENCE_WORKFLOW/GOOGLE_RICH_RESULTS_REVIEW_RUNBOOK_V1_0.md`
4. `05_REFERENCE_WORKFLOW/SCREAMING_FROG_STRUCTURED_DATA_EXPORT_CHECKLIST_V1_0.md`
5. `05_REFERENCE_WORKFLOW/VALIDATION_EVIDENCE_HANDOFF_REQUIREMENTS_V1_0.md`

Understand:
- The validation protocol defines 9 ordered steps that every future schema output bundle must pass
- Step 1 is the Python output bundle validator (`tools/validate_output_bundle.py`) — must return PASS
- Step 2 is JSON parse validation of all bundle files
- Step 3 is schema lint rules (all 10 JLSR rules must pass)
- Step 4 is Schema.org Validator — no critical errors allowed
- Step 5 is Google Rich Results Test — informational only; rich results eligibility is not guaranteed; "not eligible" does not block
- Step 6 is Screaming Frog structured data extraction — optional/where available; `N/A` does not block
- Step 7 is controller review — `finalRecommendation` must be `PROCEED_TO_HUMAN_APPROVAL` with `unresolvedBlockers: 0`
- Step 8 is human approval — required before any implementation handoff
- Step 9 is implementation handoff — produced by Prompt 12 after human approval
- Passing the full validation protocol does NOT authorize production deployment — human approval at Step 8 is always required
- No validators have been run. No schema has been generated. These are documentation contracts only.

---

### Step 2m — Read run ledger schema and review guide (PR #14 addition)

Files in this order:
1. `06_MACHINE_RULES/RUN_LEDGER_SCHEMA_V1_0.json`
2. `05_REFERENCE_WORKFLOW/RUN_LEDGER_STANDALONE_SCHEMA_REVIEW_GUIDE_V1_0.md`

Understand:
- The run ledger schema defines the required shape of all future run ledger entries — all fields, allowed status values, and safety constraints
- Every future run entry must conform to this schema before being appended to `RUN_LEDGER.json`
- `runId` must be unique; format: `RISE_RUN_<PAGE_FAMILY>_<DATE_YYYYMMDD>_<SEQ>`
- `productionLockStatus` defaults to `NO_PRODUCTION_LOCKS` and may only be set to `PRODUCTION_LOCKED` with an explicit human approval record
- `PRODUCTION_LOCKED` may never be self-claimed by Claude, a validator, or any automated process
- The review guide explains how to read ledger entries and what each field means
- `RUN_LEDGER.json` has been upgraded with `schemaVersion`, `ledgerStatus`, `productionLockStatus` — entries remain empty
- No governed runs have been performed. No run entries exist. The ledger is bootstrap-empty.

---

### Step 2n — Read run ledger tools (PR #15 addition)

Files in this order:
1. `tools/README_RUN_LEDGER_TOOLS_V1_0.md`
2. `tools/append_run_ledger_entry.py` (review the safety checks and usage)
3. `tools/report_run_ledger_status.py` (review the read-only reporter)

Understand:
- The append helper runs 20 safety checks on a candidate entry JSON before writing to `RUN_LEDGER.json`
- Supports `--dry-run` — no files are modified in dry-run mode
- Safety checks enforce no duplicate runIds, no PRODUCTION_LOCKED without humanApprovalRef, no PRODUCTION_LOCKED on failed readiness or missing evidence or failed validation
- The reporter is read-only — it prints ledger metadata, entry counts, status breakdowns, and integrity warnings without modifying any files
- Neither tool generates schema, creates JSON-LD, or authorizes production deployment
- Do not use the append helper to add fake or test entries — real entries only after the final runnable handoff is in place
- Run `python tools/report_run_ledger_status.py RUN_LEDGER.json` at any time to check ledger state — no side effects

---

### Step 2o — Read package validator (PR #16 addition)

Files in this order:
1. `tools/README_PACKAGE_VALIDATOR_V1_0.md`
2. `06_MACHINE_RULES/PACKAGE_VALIDATION_CHECKLIST_V1_0.md`
3. `06_MACHINE_RULES/PACKAGE_EXPECTED_ACTIVE_FILES_V1_0.json`

Understand:
- The package validator runs 12 checks against the package directory root
- Checks include: required files present, key JSON schemas valid, no JSON-LD files, no sample_runs directory, no production readiness claimed, mode1Runnable false, no schema output flags claimed, ledger lock status correct, no fake reports, truth view JSON valid
- Exit codes: 0=PASS (all checks), 1=FAIL (one or more checks failed), 2=input error
- Run with: `python tools/validate_package.py .` from the package root
- The expected active files contract (`PACKAGE_EXPECTED_ACTIVE_FILES_V1_0.json`) lists all 80 required files through PR #16 plus optional and blocked files
- A PASS result confirms structural integrity only — it does not authorize schema production or deployment
- The validator does not modify any files

---

### Step 2p — Read smoke-test fixture contract (PR #17 addition)

Files in this order:
1. `08_SMOKE_TESTS/README_SMOKE_TESTS.md`
2. `08_SMOKE_TESTS/STANDALONE_SMOKE_TEST_FIXTURE_CONTRACT_V1_0.md`
3. `08_SMOKE_TESTS/fixtures/standalone_v1_0/README_FAKE_FIXTURE.md`
4. `08_SMOKE_TESTS/fixtures/standalone_v1_0/fixture_manifest.json`

Understand:
- Smoke tests are package/tooling integrity checks only — they do not run the schema operator workflow
- The fixture contract defines safety rules: `example.invalid` only, no real Rise data, no JSON-LD, no production lock
- The canned fixture (`standalone_v1_0`) is synthetic — all data is fake, all URLs use `example.invalid`
- The smoke-test runner is not yet available — it will be added in PR #18
- Reading these files does not authorize schema production or any governed run

---

### Step 2q — Read smoke-test runner and health reporter (PR #18 addition)

Files in this order:
1. `tools/README_SMOKE_TEST_AND_HEALTH_TOOLS_V1_0.md`
2. `08_SMOKE_TESTS/SMOKE_TEST_RUNNER_EXPECTATIONS_V1_0.md`
3. `05_REFERENCE_WORKFLOW/MILESTONE_3_LEDGER_AND_HEALTH_TOOLS_COMPLETION_AUDIT_V1_0.md`

Understand:
- The smoke test runner (`tools/run_standalone_smoke_test.py`) runs 12 checks against the fake fixture — it does not test real Rise FC schema
- Run with: `python tools/run_standalone_smoke_test.py .` — exit 0 = PASS
- The package health reporter (`tools/report_package_health.py`) prints a full package health summary without modifying files
- Run with: `python tools/report_package_health.py .` — exit 0 = CLEAN
- Milestone 3 is tooling-complete — the audit confirms this and states Mode 1 remains not runnable
- PASS and CLEAN results do not authorize schema production or production deployment

---

### Step 2r — Read first real page handoff template and supervision rules (PR #19 addition)

Files in this order:
1. `05_REFERENCE_WORKFLOW/FIRST_REAL_PAGE_RUN_HANDOFF_TEMPLATE_V1_0.md`
2. `05_REFERENCE_WORKFLOW/FIRST_REAL_PAGE_RUN_INTAKE_FIELDS_V1_0.md`
3. `05_REFERENCE_WORKFLOW/HOMEPAGE_FIRST_REAL_RUN_SUPERVISION_RULES_V1_0.md`
4. `05_REFERENCE_WORKFLOW/FIRST_REAL_PAGE_RUN_HOLD_REASON_REFERENCE_V1_0.md`

Understand:
- The handoff template is a blank future-use template — it is not a completed run artifact; no real run ID or URL is filled in
- All fields default to placeholder, NOT_STARTED, HOLD, or NOT_AUTHORIZED
- The intake fields document defines what must be confirmed before any governed run begins — all 9 required field groups must pass intake validation
- The homepage supervision rules define: route `/`, `HOMEPAGE_SCHEMA_PROFILE`, fingerprint `80edd829806cae271242c6a8e853edabdb8b2f16ca5a8fa1a3fc69ff5b78d53d`, allowed modules, blocked modules, held fields, and 10 supervision rules
- The hold reason reference defines 14 hold codes (HOLD_PHASE0_SOURCE_MISSING through HOLD_ASTRO_CARRY_NOT_READY) — each with condition and resolution requirement
- Reading these files does not start a run, generate schema, or authorize any implementation

---

### Step 2s — Read independent analyzer and controller post-analyzer flow (PR #20 addition)

Files in this order:
1. `05_REFERENCE_WORKFLOW/INDEPENDENT_ANALYZER_AND_CONTROLLER_FLOW_V1_0.md`
2. `05_REFERENCE_WORKFLOW/FIRST_REAL_PAGE_INDEPENDENT_ANALYZER_REVIEW_TEMPLATE_V1_0.md`
3. `05_REFERENCE_WORKFLOW/CONTROLLER_POST_ANALYZER_DECISION_TEMPLATE_V1_0.md`
4. `05_REFERENCE_WORKFLOW/ANALYZER_CONTROLLER_DISPOSITION_MATRIX_V1_0.md`

Understand:
- The analyzer runs in a fresh session with no prior context and produces findings only — it does not approve or reject the run
- The analyzer checks 10 items: evidence mapping, truth-view currency, schema profile conformance, held field compliance, JSON-LD validity, lint rule compliance, validation result, implementation eligibility, Phase 0 boundary, and production lock status
- The controller reviews each finding and assigns a per-finding disposition (ACCEPT, MODIFY, REJECT, DEFER, HUMAN_REVIEW_REQUIRED, PATCH_REQUIRED, or HOLD)
- The controller issues a final recommendation; `PROCEED_TO_HUMAN_APPROVAL` with `unresolvedBlockers: 0` is required before Step 8
- Neither the analyzer nor the controller may mutate Phase 0, self-approve production, or bypass the human approval gate
- The analyzer review template and controller decision template are blank future-use documents only — no real findings or decisions exist
- Reading these files does not run the analyzer or create any findings

---

### Step 2t — Read current website implementation handoff checklist (PR #21 addition)

Files in this order:
1. `05_REFERENCE_WORKFLOW/CURRENT_WEBSITE_IMPLEMENTATION_HANDOFF_CHECKLIST_V1_0.md`
2. `05_REFERENCE_WORKFLOW/CURRENT_WEBSITE_IMPLEMENTATION_NON_AUTHORIZATION_RULES_V1_0.md`
3. `05_REFERENCE_WORKFLOW/CURRENT_WEBSITE_PRE_IMPLEMENTATION_APPROVAL_GATE_V1_0.md`
4. `05_REFERENCE_WORKFLOW/CURRENT_WEBSITE_POST_IMPLEMENTATION_VERIFICATION_CHECKLIST_V1_0.md`

Understand:
- The implementation handoff checklist defines 8 sections (schema output bundle, validation pass, controller approval, human approval, implementation details, rollback plan, post-implementation verification, run ledger update) — all items are NOT_STARTED
- The non-authorization rules define 10 explicit rules: no implementation without a validated output bundle, no implementation without controller approval, no implementation without human approval, no held fields without owner approval, no blocked modules, no Phase 0 mutation, no self-merge, no production lock without human approval reference, mode1Runnable must be true before any run, evidence map required before drafting
- The pre-implementation approval gate defines 7 gates that must ALL be confirmed before any implementation: package readiness, truth pack currency, evidence map, schema profile and modules, validated output bundle, controller review, human approval — all currently NOT REACHED
- The post-implementation verification checklist defines 8 sections for verifying a live implementation — all items are NOT_STARTED
- None of these documents authorize implementation — they are future-use governance contracts only
- Mode 1 remains not runnable after PR #21

---

### Step 2u — Read governed sample-run artifact policy (PR #22 addition)

Files in this order:
1. `05_REFERENCE_WORKFLOW/GOVERNED_SAMPLE_RUN_ARTIFACT_POLICY_V1_0.md`
2. `05_REFERENCE_WORKFLOW/REAL_RUN_ARTIFACT_COMMIT_RULES_V1_0.md`
3. `05_REFERENCE_WORKFLOW/REDACTED_SAMPLE_ARTIFACT_REQUIREMENTS_V1_0.md`
4. `05_REFERENCE_WORKFLOW/MILESTONE_4_FIRST_REAL_PAGE_RUN_SUPPORT_COMPLETION_AUDIT_V1_0.md`

Understand:
- Real run artifacts (JSON-LD, output bundles, validator screenshots, QA zips, implementation evidence) are prohibited by default until an authorized artifact lane is established
- Seven explicit prohibition rules (RAC-001–RAC-007) govern what may not be committed
- Synthetic artifacts using `example.invalid` are permitted only in designated fake-data directories (e.g., `08_SMOKE_TESTS/fixtures/`)
- Redacted sample artifacts are not yet authorized — the redaction requirements document defines the future standard for when a redacted lane is established
- Milestone 4 is now complete: all four support-layer PRs (#19–#22) are merged; the package has first real page handoff templates, analyzer/controller flow, implementation handoff checklist, and artifact policy
- Mode 1 remains not runnable — the final Mode 1 runnable handoff PR (#26) is still required
- Reading these files does not create any artifacts or authorize any commits

---

### Step 2v — Read Astro schema carry gate reference (PR #23 addition)

Files in this order:
1. `05_REFERENCE_WORKFLOW/ASTRO_SCHEMA_CARRY_GATE_REFERENCE_V1_0.md`
2. `05_REFERENCE_WORKFLOW/ASTRO_SCHEMA_CARRY_NON_AUTHORIZATION_RULES_V1_0.md`
3. `05_REFERENCE_WORKFLOW/ASTRO_SCHEMA_IDENTITY_MATCH_REQUIREMENTS_V1_0.md`
4. `05_REFERENCE_WORKFLOW/ASTRO_SCHEMA_CARRY_HOLD_REASON_REFERENCE_V1_0.md`

Understand:
- The Astro carry gate sequence defines 8 gates that must all pass before any schema output may be carried into Astro — no gates are currently passed
- Astro does not author, repair, normalize, or override schema — it carries approved output only
- Seven non-authorization rules (ACNA-001–007) govern what may not be done: no Astro code changes, no schema attachment, no production deployment, no Mode 2 readiness
- Twelve identity match checks must pass at Gate 6 — bundle ID, export ID, route, page family, profile, truth fingerprint, evidence map, validation, controller approval, human approval, held fields, blocked modules
- Fifteen hold codes define all conditions that block Astro carry — all active by default
- Mode 2 remains not ready — `mode2AstroReady: false`
- Reading these files does not attach schema, change any Astro code, or authorize carry

---

### Step 2w — Read Runtime Appendix schema carry field reference (PR #24 addition)

Files in this order:
1. `05_REFERENCE_WORKFLOW/RUNTIME_APPENDIX_SCHEMA_CARRY_FIELD_REFERENCE_V1_0.md`
2. `05_REFERENCE_WORKFLOW/RUNTIME_APPENDIX_SCHEMA_CARRY_FIELD_STATUS_ENUMS_V1_0.md`
3. `05_REFERENCE_WORKFLOW/RUNTIME_APPENDIX_SCHEMA_CARRY_NON_AUTHORIZATION_RULES_V1_0.md`
4. `06_MACHINE_RULES/RUNTIME_APPENDIX_SCHEMA_CARRY_FIELDS_SCHEMA_V1_0.json`

Understand:
- The Runtime Appendix is the metadata bridge between the SEO/schema operator lane and the HTML/runtime/Astro carry implementation — it does not author schema
- 18 carry fields must all be populated and confirmed before Gate 4 (Runtime Appendix complete) in the Astro carry gate sequence
- Required constants: `schema_owner: SEO_SCHEMA_OPERATOR`, `schema_source_lane: SEO_SCHEMA_EXPORT`
- 13 status enum values govern what values each status field may accept
- Seven non-authorization rules (RANA-001–RANA-007) confirm no runtime code, no Astro code, no schema generated, no attachment, no production deployment
- The JSON contract schema defines the required shape of a future Runtime Appendix carry field record — contract definition only, no record created
- All 18 carry fields are at NOT_STARTED; no governed run has completed
- Reading these files does not create a Runtime Appendix record, generate schema, or authorize carry

---

### Step 2x — Read Astro attachment packet template (PR #25 addition)

Files in this order:
1. `05_REFERENCE_WORKFLOW/ASTRO_ATTACHMENT_PACKET_TEMPLATE_V1_0.md`
2. `05_REFERENCE_WORKFLOW/ASTRO_ATTACHMENT_PACKET_REQUIRED_FIELDS_V1_0.md`
3. `05_REFERENCE_WORKFLOW/ASTRO_ATTACHMENT_PACKET_REVIEW_SEQUENCE_V1_0.md`
4. `05_REFERENCE_WORKFLOW/ASTRO_ATTACHMENT_PACKET_HOLD_MATRIX_V1_0.md`

Understand:
- The attachment packet is the governing instrument that authorizes schema transfer from the SEO operator lane to an Astro route — it must be filled and approved before any schema may be attached to Astro
- 19 packet fields all default to NOT_STARTED or NOT_APPROVED — no real packet has been created or filled
- The required fields reference defines type, format, allowed values, gate dependency, and failure hold code for each field
- The 9-step review sequence is strictly sequential — no step may be skipped; final attachment decision requires all prior steps to complete
- All 15 hold codes are active by default; none are self-resolvable; each requires real governed evidence or explicit human approval
- Reading these files does not create an attachment packet, attach schema, change any Astro code, or authorize Mode 2

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

The schema workflow is **not runnable after PR #10**.

Operators must wait for:
- PR #2: Governing doctrine ✓ Done
- PR #3: Phase 0 truth source map and homepage scoped truth view ✓ Done
- PR #4: Homepage schema profile and blocked module policy ✓ Done
- PR #5: Standalone schema master flow ✓ Done
- PR #6: Team quickstart and operator checklist upgrades ✓ Done
- PR #7: Operator prompts 00 through 04 and 08 ✓ Done
- PR #8: Final validation, analyzer, and completion prompts ✓ Done
- PR #9: Output bundle contract schemas ✓ Done
- PR #10: Controlled homepage non-production JSON-LD draft contract ✓ Done
- PR #11: Output bundle validator ✓ Done
- PR #12: Claude QA finding schema and controller review contracts ✓ Done
- PR #13: Final schema validation protocol and validator runbook ✓ Done
- PR #14: Governed run ledger schema and RUN_LEDGER upgrade ✓ Done
- PR #15: Run ledger append helper and reporter ✓ Done
- PR #16: Package validator and active-file coherence checks ✓ Done
- PR #17: Smoke-test fixture contract and canned fixture ✓ Done
- PR #18: Smoke-test runner and package health reporter ✓ Done
- PR #19: First real page handoff template ✓ Done
- PR #20: Independent analyzer and controller post-analyzer flow ✓ Done
- PR #21: Current website implementation handoff checklist ✓ Done
- PR #22: Governed sample-run artifact policy ✓ Done
- PR #23: Astro schema carry gate reference ✓ Done
- PR #24: Runtime Appendix schema carry field reference ✓ Done
- PR #25: Astro attachment packet template ✓ Done

Do not generate schema. Do not create JSON-LD. Do not implement on the website.

---

## Mode 1 — Current website goal

Produce validated schema for pages on the current risefcsoccer.com website.

- First-page target: homepage, route `/`, with `HOMEPAGE_SCHEMA_PROFILE`
- Allowed first-page modules (future only): Organization, WebSite, WebPage, BreadcrumbList
- Schema is derived from approved Phase 0 content and confirmed page evidence
- Output must be validated before any implementation handoff

**Not runnable yet. Waiting for evidence maps, validators, and the final runnable handoff.**

---

## Mode 2 — Future Astro goal

Carry validated schema into the Astro implementation after all carry gates pass.

- Blocked until all Astro carry gates pass — carry gate sequence defined in PR #23 (`ASTRO_SCHEMA_CARRY_GATE_REFERENCE_V1_0.md`); no gates have been passed
- No Astro files are modified by this package
- Carry gate sequence defined in PR #23. Runtime Appendix carry field reference added in PR #24. Attachment packet template added in PR #25.

**Not yet scoped. Waiting for Astro route, runtime evidence, and all carry gates to pass.**

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
