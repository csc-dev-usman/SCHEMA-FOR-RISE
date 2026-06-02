# Team Quickstart — Rise FC Standalone Schema Operator Package

**Status:** `MILESTONE_5_ASTRO_CARRY_BRIDGE_COMPLETE_MODE_1_SUPERVISED_RUNNABLE_NO_SCHEMA_OUTPUT`

---

## Plain-language overview

This package is the governed workspace for Rise FC schema work. It provides a controlled environment where the team can produce, validate, and hand off schema markup for the Rise FC website — without guessing, inventing content, or bypassing review.

It is modeled after the CSC standalone schema operator pattern. The medical doctrine from CSC does **not** apply here. Rise FC has its own doctrine, which will be added in PR #2.

---

## Why this package exists

The Rise FC website (risefcsoccer.com) needs validated, accurate schema markup for search optimization. Rather than generating schema ad hoc, this package establishes a governed workflow:

1. Factual truth comes from Rise Phase 0.
2. Schema is derived from that truth — not invented.
3. Each output is validated before it touches the website.
4. Human approval is required at every gate.

---

## What you can do right now (after PR #26)

- Use `00_START_HERE/RISE_OPERATOR_NAVIGATION_DECISION_TREE_V1_0.md` to find the right document for your task.
- Use `00_START_HERE/RISE_SCHEMA_OPERATOR_PREFLIGHT_CHECKLIST_V1_0.md` to check all gates before any schema work.
- Use `00_START_HERE/RISE_MODE_STATUS_AND_NEXT_STEP_GUIDE_V1_0.md` to understand the current status of Mode 1 and Mode 2.
- Read the package README and start files.
- Read the governing doctrine in `02_GOVERNING_DOCTRINE/`.
- Read the homepage scoped truth-pack reference in `03_TRUTH_PACK/`.
- Read the homepage schema profile and reference lists in `07_REFERENCE_LISTS/`.
- Read the master flow documents in `01_MASTER_FLOW/` to understand the full operating sequence.
- Read the full operator prompt set in `04_OPERATOR_PROMPTS/` to understand what each governed step will do.
- Read the output bundle contract schemas in `06_MACHINE_RULES/` to understand the required shape of run artifacts.
- Read the lint rules in `06_MACHINE_RULES/RISE_SCHEMA_LINT_RULES_V1_0.json` — all 10 JSON-LD safety rules apply to every schema draft.
- Read the reference workflow documents in `05_REFERENCE_WORKFLOW/` to understand the draft contract, all preconditions, planned output files, and the 10-step review sequence.
- Read `tools/README_OUTPUT_BUNDLE_VALIDATOR_V1_0.md` to understand the output bundle validator and how it enforces governed rules.
- Run `python tools/validate_output_bundle.py --help` to see the validator usage.
- Read `05_REFERENCE_WORKFLOW/CLAUDE_QA_AND_CONTROLLER_REVIEW_WORKFLOW_V1_0.md` to understand the governed Claude QA and controller review process.
- Read `05_REFERENCE_WORKFLOW/CONTROLLER_DECISION_ENUM_REFERENCE_V1_0.md` to understand all valid controller decision values.
- Read `05_REFERENCE_WORKFLOW/FINAL_SCHEMA_VALIDATION_PROTOCOL_V1_0.md` to understand the required 9-step validation sequence for all future schema output bundles.
- Read the associated validation runbooks in `05_REFERENCE_WORKFLOW/` — Schema.org Validator, Google Rich Results Test, Screaming Frog checklist, and validation evidence handoff requirements.
- Read `06_MACHINE_RULES/RUN_LEDGER_SCHEMA_V1_0.json` to understand the required shape of future run ledger entries.
- Read `05_REFERENCE_WORKFLOW/RUN_LEDGER_STANDALONE_SCHEMA_REVIEW_GUIDE_V1_0.md` to understand how to read the ledger and when `PRODUCTION_LOCKED` may and may not be claimed.
- Read `tools/README_RUN_LEDGER_TOOLS_V1_0.md` to understand the run ledger append helper and read-only reporter added in PR #15.
- Run `python tools/report_run_ledger_status.py RUN_LEDGER.json` to check the current ledger state (read-only, no side effects).
- Read `tools/README_PACKAGE_VALIDATOR_V1_0.md` to understand the package validator added in PR #16.
- Read `06_MACHINE_RULES/PACKAGE_VALIDATION_CHECKLIST_V1_0.md` to understand all 12 package checks.
- Run `python tools/validate_package.py .` at any time to verify package structural integrity (read-only, no side effects).
- Read `08_SMOKE_TESTS/README_SMOKE_TESTS.md` to understand what smoke tests are and are not.
- Read `08_SMOKE_TESTS/STANDALONE_SMOKE_TEST_FIXTURE_CONTRACT_V1_0.md` to understand fixture safety rules.
- Review `08_SMOKE_TESTS/fixtures/standalone_v1_0/` to understand the canned fake fixture — all data uses `example.invalid`, no real Rise data.
- Read `tools/README_SMOKE_TEST_AND_HEALTH_TOOLS_V1_0.md` to understand the smoke test runner and package health reporter.
- Run `python tools/run_standalone_smoke_test.py .` to exercise the fake fixture (12 checks, read-only, no side effects).
- Run `python tools/report_package_health.py .` for a full package health summary (read-only, no side effects).
- Read `05_REFERENCE_WORKFLOW/MILESTONE_3_LEDGER_AND_HEALTH_TOOLS_COMPLETION_AUDIT_V1_0.md` to understand Milestone 3 completion status and current package posture.
- Read `05_REFERENCE_WORKFLOW/FIRST_REAL_PAGE_RUN_HANDOFF_TEMPLATE_V1_0.md` to understand the blank future-use handoff template for first real page runs.
- Read `05_REFERENCE_WORKFLOW/FIRST_REAL_PAGE_RUN_INTAKE_FIELDS_V1_0.md` to understand required intake fields and validation expectations.
- Read `05_REFERENCE_WORKFLOW/HOMEPAGE_FIRST_REAL_RUN_SUPERVISION_RULES_V1_0.md` to understand the homepage lane supervision rules — route `/`, `HOMEPAGE_SCHEMA_PROFILE`, fingerprint, allowed modules, blocked modules, held fields.
- Read `05_REFERENCE_WORKFLOW/FIRST_REAL_PAGE_RUN_HOLD_REASON_REFERENCE_V1_0.md` to understand all hold codes and resolution requirements for first real page runs.
- Read `05_REFERENCE_WORKFLOW/INDEPENDENT_ANALYZER_AND_CONTROLLER_FLOW_V1_0.md` to understand the two-stage analyzer/controller post-analyzer flow.
- Read `05_REFERENCE_WORKFLOW/FIRST_REAL_PAGE_INDEPENDENT_ANALYZER_REVIEW_TEMPLATE_V1_0.md` to understand the blank analyzer review template.
- Read `05_REFERENCE_WORKFLOW/CONTROLLER_POST_ANALYZER_DECISION_TEMPLATE_V1_0.md` to understand the blank controller decision template.
- Read `05_REFERENCE_WORKFLOW/ANALYZER_CONTROLLER_DISPOSITION_MATRIX_V1_0.md` to understand the full disposition matrix — severity guidance, category constraints, and final recommendation rules.
- Read `05_REFERENCE_WORKFLOW/CURRENT_WEBSITE_IMPLEMENTATION_HANDOFF_CHECKLIST_V1_0.md` to understand the future-use implementation handoff checklist — 8 sections defining what must be confirmed before and during a governed implementation.
- Read `05_REFERENCE_WORKFLOW/CURRENT_WEBSITE_IMPLEMENTATION_NON_AUTHORIZATION_RULES_V1_0.md` to understand the 10 non-authorization rules governing current website implementation.
- Read `05_REFERENCE_WORKFLOW/CURRENT_WEBSITE_PRE_IMPLEMENTATION_APPROVAL_GATE_V1_0.md` to understand the 7 pre-implementation gates — all currently NOT REACHED.
- Read `05_REFERENCE_WORKFLOW/CURRENT_WEBSITE_POST_IMPLEMENTATION_VERIFICATION_CHECKLIST_V1_0.md` to understand the future-use post-implementation verification steps.
- Read `05_REFERENCE_WORKFLOW/GOVERNED_SAMPLE_RUN_ARTIFACT_POLICY_V1_0.md` to understand the default prohibition on real run artifacts and the conditions under which synthetic or redacted artifacts may be used.
- Read `05_REFERENCE_WORKFLOW/REAL_RUN_ARTIFACT_COMMIT_RULES_V1_0.md` to understand the 7 prohibition rules — real artifacts are prohibited by default until an authorized artifact lane is established.
- Read `05_REFERENCE_WORKFLOW/REDACTED_SAMPLE_ARTIFACT_REQUIREMENTS_V1_0.md` to understand the 8 redaction categories that will apply when a redacted artifact lane is established.
- Read `05_REFERENCE_WORKFLOW/MILESTONE_4_FIRST_REAL_PAGE_RUN_SUPPORT_COMPLETION_AUDIT_V1_0.md` to understand the Milestone 4 completion status and current package posture.
- Read `05_REFERENCE_WORKFLOW/ASTRO_SCHEMA_CARRY_GATE_REFERENCE_V1_0.md` to understand the future 8-gate Astro carry sequence — no gates are currently passed.
- Read `05_REFERENCE_WORKFLOW/ASTRO_SCHEMA_CARRY_NON_AUTHORIZATION_RULES_V1_0.md` to understand the 7 non-authorization rules governing Astro carry and attachment — all in force.
- Read `05_REFERENCE_WORKFLOW/ASTRO_SCHEMA_IDENTITY_MATCH_REQUIREMENTS_V1_0.md` to understand the 12 identity match checks required before any schema carry may proceed.
- Read `05_REFERENCE_WORKFLOW/ASTRO_SCHEMA_CARRY_HOLD_REASON_REFERENCE_V1_0.md` to understand the 15 hold codes for Astro carry — definitions, conditions, and resolution requirements.
- Read `05_REFERENCE_WORKFLOW/RUNTIME_APPENDIX_SCHEMA_CARRY_FIELD_REFERENCE_V1_0.md` to understand the 18 Runtime Appendix carry fields — the metadata bridge between the operator lane and runtime/Astro carry.
- Read `05_REFERENCE_WORKFLOW/RUNTIME_APPENDIX_SCHEMA_CARRY_FIELD_STATUS_ENUMS_V1_0.md` to understand all 13 allowed status enum values for carry fields.
- Read `05_REFERENCE_WORKFLOW/RUNTIME_APPENDIX_SCHEMA_CARRY_NON_AUTHORIZATION_RULES_V1_0.md` to understand the 7 non-authorization rules governing Runtime Appendix carry — all in force.
- Read `06_MACHINE_RULES/RUNTIME_APPENDIX_SCHEMA_CARRY_FIELDS_SCHEMA_V1_0.json` to understand the JSON contract schema defining the required shape of a future Runtime Appendix carry field record.
- Read `05_REFERENCE_WORKFLOW/ASTRO_ATTACHMENT_PACKET_TEMPLATE_V1_0.md` to understand the Astro attachment packet template — 19 packet fields, all defaults, 10 hard rules, non-authorization statement. No real packet has been created.
- Read `05_REFERENCE_WORKFLOW/ASTRO_ATTACHMENT_PACKET_REQUIRED_FIELDS_V1_0.md` to understand the required field contract for all 19 attachment packet fields — type, format, gate dependency, failure hold code.
- Read `05_REFERENCE_WORKFLOW/ASTRO_ATTACHMENT_PACKET_REVIEW_SEQUENCE_V1_0.md` to understand the 9-step sequential review sequence — no step may be skipped; final decision requires all prior steps to complete.
- Read `05_REFERENCE_WORKFLOW/ASTRO_ATTACHMENT_PACKET_HOLD_MATRIX_V1_0.md` to understand the 15 hold codes for the attachment packet — all active by default, none self-resolvable.
- Read `00_START_HERE/FINAL_MODE_1_RUNNABLE_HANDOFF_V1_0.md` to understand the Mode 1 supervised-runnable handoff — Mode 1 is now runnable for intake. Follow the step-by-step operator instructions.
- Read `05_REFERENCE_WORKFLOW/FINAL_MODE_1_SUPERVISED_RUNNABLE_HANDOFF_V1_0.md` to understand the formal reference declaration of supervised-runnable status — what it means and what it does not mean.
- Read `05_REFERENCE_WORKFLOW/MODE_1_RUNNABLE_SCOPE_AND_LIMITS_V1_0.md` to understand the full CAN/CANNOT table for Mode 1 — what operators may do now and what remains blocked until later run approval.
- Read `05_REFERENCE_WORKFLOW/MODE_1_OPERATOR_START_CONDITIONS_V1_0.md` to understand all 14 start conditions (SC-001–SC-014) that must pass before Prompt 00 intake begins.
- Read `05_REFERENCE_WORKFLOW/MILESTONE_5_ASTRO_CARRY_BRIDGE_COMPLETION_AUDIT_V1_0.md` to understand the Milestone 5 completion audit — all components verified, current package posture, mode status.
- Understand which modules are allowed, which are blocked, and which fields are held.
- Review the owner approval worksheet to understand which fields need human owner decisions.
- Review `05_REFERENCE_WORKFLOW/HOMEPAGE_DRAFT_PRECONDITIONS_AND_HOLD_MATRIX_V1_0.md` to understand every gate that must pass before a draft run begins.

---

## What you cannot do right now

> **Mode 1 is supervised-runnable as of PR #26. The operator intake sequence may begin for a confirmed page candidate. However, schema output (JSON-LD, output bundles, production deployment) is not yet authorized. Operators must wait for PR #27 (controlled non-production homepage JSON-LD draft) before generating any schema.**

After PR #26, you must not:

- Generate any JSON-LD
- Execute schema output operator prompts (Prompt 01 and beyond) without PR #27 authorization
- Create any schema output
- Create any production schema bundles
- Attach schema to the current website
- Attach schema to Astro
- Run any schema operator workflow
- Commit real run artifacts
- Create evidence maps or schema profiles outside the governed workflow
- Treat the homepage scoped truth view JSON as schema output or JSON-LD — it is read-only reference material only

---

## When can you run the schema workflow?

After all required PRs are merged and the final runnable handoff is in place, Mode 1 will be fully operational.

The sequence:
- PR #2 adds governing doctrine ✓ Done
- PR #3 adds Phase 0 truth source map and homepage scoped truth view ✓ Done
- PR #4 adds homepage schema profile and blocked module policy ✓ Done
- PR #5 adds standalone schema master flow ✓ Done
- PR #6 adds team quickstart and operator checklist upgrades ✓ Done
- PR #7 adds operator prompts 00 through 04 and 08 ✓ Done
- PR #8 adds final validation, analyzer, and completion prompts ✓ Done
- PR #9 adds output bundle contract schemas ✓ Done
- PR #10 adds controlled homepage non-production JSON-LD draft contract ✓ Done
- PR #11 adds output bundle validator ✓ Done
- PR #12 adds Claude QA finding schema and controller review contracts ✓ Done
- PR #13 adds final schema validation protocol and validator runbook ✓ Done
- PR #14 adds governed run ledger schema and RUN_LEDGER upgrade ✓ Done
- PR #15 adds run ledger append helper and reporter ✓ Done
- PR #16 adds package validator and active-file coherence checks ✓ Done
- PR #17 adds smoke-test fixture contract and canned fixture ✓ Done
- PR #18 adds smoke-test runner and package health reporter ✓ Done — Milestone 3 complete
- PR #19 adds first real page handoff template ✓ Done
- PR #20 adds independent analyzer and controller post-analyzer flow ✓ Done
- PR #21 adds current website implementation handoff checklist ✓ Done
- PR #22 adds governed sample-run artifact policy ✓ Done — Milestone 4 complete
- PR #23 adds Astro schema carry gate reference ✓ Done — Milestone 5 in progress (1/4)
- PR #24 adds Runtime Appendix schema carry field reference ✓ Done — Milestone 5 in progress (2/4)
- PR #25 adds Astro attachment packet template ✓ Done — Milestone 5 in progress (3/4)
- PR #26 adds final Mode 1 runnable handoff ✓ Done — Milestone 5 complete (4/4)

Mode 1 is now supervised-runnable. Intake may begin. Do not execute schema output prompts (Prompt 01 and beyond) or generate schema without PR #27 authorization.

---

## First-page target (for reference — not runnable yet)

When Mode 1 is operational, the first schema target will be:

- **Page:** Homepage
- **Route:** `/`
- **Profile:** `HOMEPAGE_SCHEMA_PROFILE`
- **Allowed modules:** Organization, WebSite, WebPage, BreadcrumbList

No other modules are authorized for the first-page lane. See the README for the full blocked list.

---

## Key rule to remember

Rise Phase 0 is the source of factual truth. This package is downstream of Phase 0. Operators never invent content — they derive schema from approved Phase 0 content and confirmed page evidence.

If Phase 0 does not confirm a field, that field does not go into schema.

---

## Where to find help

1. Read `README_COMPLETE_OPERATOR_PACKAGE.md` first.
2. Check `00_START_HERE/FINAL_STANDALONE_OPERATING_MANUAL_INDEX_V1_0.md` for the full reading order.
3. Check `00_START_HERE/OPERATOR_CHECKLIST_STANDALONE_RUN.md` before attempting any run.
4. Raise questions with the package owner before taking any action not covered by the governing doctrine.
