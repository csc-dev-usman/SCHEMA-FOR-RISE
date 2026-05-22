# Machine Rules — Rise FC Standalone Schema Package

**Status:** `OUTPUT_BUNDLE_CONTRACT_SCHEMAS_ADDED_NO_SCHEMA_OUTPUT`

> These are contract schema definitions only. They are not validators. They are not scripts. They are not real run artifacts. No schema has been generated. No JSON-LD has been created. No evidence maps exist as run artifacts. These files define the expected shape of future governed run outputs.

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

Future PRs will add the homepage non-production draft contract (PR #10) and the final runnable handoff.
