# Machine Rules — Rise FC Standalone Schema Package

**Status:** `PACKAGE_VALIDATOR_ADDED_NO_SCHEMA_OUTPUT`

> This folder contains contract schema definitions and validator tooling. The contract schemas define the expected shape of future governed run outputs. The validator rules and expected-files contract support the Python output bundle validator in `tools/`. The Claude QA finding schema and controller review packet schema define the required shape of future QA and controller review artifacts. The run ledger schema defines the required shape of future run ledger entries. No schema has been generated. No JSON-LD has been created. No evidence maps exist as run artifacts. No QA findings exist. No run entries exist.

---

## Purpose

This folder contains machine-readable contract schemas that define the required structure of future Rise FC schema operator run artifacts. Each contract schema specifies what fields a compliant output bundle, run metadata record, controller decision, validator result set, evidence map, or lint rule set must contain.

These contract schemas are reference definitions. They are used to:
- Define the expected output shape before any real runs occur
- Allow future validators or tooling to check real run artifacts for compliance
- Serve as the authoritative source of field names and value enumerations for run artifacts

---

## Core rule

These contract schemas are not validators. They are not scripts. They do not run anything. They do not generate schema. They are JSON documents that define structure only.

No real run artifacts exist. No governed runs have occurred. No output bundles have been created.

---

## Files in this folder

| File | Purpose |
|------|---------|
| `README_MACHINE_RULES_V1_0.md` | This file. Index and non-authorization statement. |
| `OUTPUT_BUNDLE_MANIFEST_SCHEMA_V1_0.json` | Contract schema for future output bundle manifests |
| `RUN_METADATA_SCHEMA_V1_0.json` | Contract schema for future run metadata records |
| `CONTROLLER_DECISION_SCHEMA_V1_0.json` | Contract schema for controller decision records |
| `VALIDATOR_RESULTS_SCHEMA_V1_0.json` | Contract schema for validator result sets |
| `EVIDENCE_MAP_SCHEMA_V1_0.json` | Contract schema for evidence map records |
| `RISE_SCHEMA_LINT_RULES_V1_0.json` | Lint rules defining blocked modules, held fields, allowed modules, and JSON-LD safety rules |
| `OUTPUT_BUNDLE_VALIDATOR_RULES_V1_0.md` | Validation rules for the output bundle validator (RULE_VAL_001–RULE_VAL_007). Added PR #11. |
| `OUTPUT_BUNDLE_VALIDATOR_EXPECTED_FILES_V1_0.json` | Machine-readable expected file list contract for the validator — required, conditional, and blocked files. Added PR #11. |
| `CLAUDE_QA_FINDING_SCHEMA_V1_0.json` | Contract schema for Claude QA finding records — findingId, severity, category, claim, evidence, recommendation, controllerDisposition. Added PR #12. |
| `CONTROLLER_REVIEW_PACKET_SCHEMA_V1_0.json` | Contract schema for controller review packets — reviewId, qaFindings, controllerDecisions, patchRequired, humanReviewRequired, finalRecommendation. Added PR #12. |
| `RUN_LEDGER_SCHEMA_V1_0.json` | Contract schema for run ledger entries — runId, targetUrl, mode, schemaProfile, truthFingerprint, all status fields, productionLockStatus. Added PR #14. |
| `PACKAGE_VALIDATION_CHECKLIST_V1_0.md` | Manual checklist for all 12 package validator checks — rationale, failure meanings, non-authorization statement. Added PR #16. |
| `PACKAGE_EXPECTED_ACTIVE_FILES_V1_0.json` | Machine-readable expected file list contract — 80 required files through PR #16, optional files, blocked files and patterns, safety constraints. Added PR #16. |

---

## Relationship to other package components

| Component | Relationship |
|-----------|-------------|
| `04_OPERATOR_PROMPTS/` | Prompts produce outputs that must conform to these contract schemas |
| `03_TRUTH_PACK/` | Evidence map schema references truth-pack field names |
| `07_REFERENCE_LISTS/` | Lint rules reference allowed modules, blocked modules, and held field categories |
| `RUN_LEDGER.json` | Completed runs will be recorded using the run metadata schema shape |

---

## Non-authorization statement

This folder and all files within it do not authorize:
- Schema output
- JSON-LD generation
- Evidence map creation as a run artifact
- Current website implementation
- Astro attachment
- Production lock
- Validator script creation (these are contract definitions, not scripts)

No governed run has occurred. No real run artifacts exist. No evidence maps exist as run artifacts. The `evidenceMapSchemaAdded` flag in the package manifest is true — this means the evidence map contract schema exists as a definition. The `evidenceMapAdded` flag remains false — no actual evidence map run artifact has been created.

The output bundle validator (`tools/validate_output_bundle.py`) added in PR #11 uses these contract schemas and rules to check future output bundle directories for compliance. See `tools/README_OUTPUT_BUNDLE_VALIDATOR_V1_0.md` for usage.

The run ledger schema (`RUN_LEDGER_SCHEMA_V1_0.json`) added in PR #14 defines the required shape of future run ledger entries. See `RUN_LEDGER.json` for the current bootstrap-empty ledger and `05_REFERENCE_WORKFLOW/RUN_LEDGER_STANDALONE_SCHEMA_REVIEW_GUIDE_V1_0.md` for guidance on reading and interpreting ledger entries.

The run ledger append helper (`tools/append_run_ledger_entry.py`) and reporter (`tools/report_run_ledger_status.py`) were added in PR #15. The package validator (`tools/validate_package.py`) was added in PR #16, along with this folder's `PACKAGE_VALIDATION_CHECKLIST_V1_0.md` and `PACKAGE_EXPECTED_ACTIVE_FILES_V1_0.json`.

Future PRs will add the smoke-test fixture, the homepage evidence map, and the final runnable handoff.
