# Homepage Draft Output File List V1.0

**Status:** `HOMEPAGE_NON_PRODUCTION_DRAFT_CONTRACT_ADDED_NO_SCHEMA_OUTPUT`

> **These are planned output file names only.** None of these files have been created. No JSON-LD exists. No schema output exists. No evidence map run artifact exists. This document defines the expected structure of future governed run outputs.

---

## Purpose

This document lists the file names and expected shapes that a future governed homepage schema run will produce. It exists so operators know in advance exactly what artifacts will be created, where they will go, and what format they must follow.

No files listed here exist yet. They will be created during a future governed run after all preconditions in `HOMEPAGE_DRAFT_PRECONDITIONS_AND_HOLD_MATRIX_V1_0.md` are confirmed.

---

## Planned output directory

All run artifacts for Mode 1 runs will be placed in:

```
sample_runs/RUN_001_HOMEPAGE_MODE1/
```

This directory does not exist yet. It will be created during the first governed run.

---

## Planned output files

### Run metadata

| Planned file | Format | Contract schema |
|-------------|--------|-----------------|
| `sample_runs/RUN_001_HOMEPAGE_MODE1/RUN_METADATA.json` | JSON | `06_MACHINE_RULES/RUN_METADATA_SCHEMA_V1_0.json` |

This file will record the run ID, dates, operator inputs, mode, target URL, schema profile, truth fingerprint, production status, human approval status, and governance compliance flag.

Expected `productionStatus` at draft creation: `NON_PRODUCTION`
Expected `humanApprovalStatus` at draft creation: `NOT_YET_REQUESTED`

---

### Evidence map

| Planned file | Format | Contract schema |
|-------------|--------|-----------------|
| `sample_runs/RUN_001_HOMEPAGE_MODE1/HOMEPAGE_EVIDENCE_MAP.json` | JSON | `06_MACHINE_RULES/EVIDENCE_MAP_SCHEMA_V1_0.json` |

This file will record field-level evidence decisions for all homepage schema fields considered in the run. Every field will have an `emissionDecision` of `EMIT`, `HELD`, `DEFERRED`, `EXCLUDED_BLOCKED_MODULE`, or `EXCLUDED_NO_EVIDENCE`.

---

### Non-production JSON-LD draft

| Planned file | Format | Notes |
|-------------|--------|-------|
| `sample_runs/RUN_001_HOMEPAGE_MODE1/HOMEPAGE_NON_PRODUCTION_JSONLD_DRAFT_V1.json` | JSON-LD | Non-production only. Requires NON_PRODUCTION marker. |

This is the actual schema draft. It will be a JSON-LD document with `@context`, `@graph`, and schema `@type` nodes for the allowed homepage modules (`Organization`, `WebSite`, `WebPage`, `BreadcrumbList`).

**It does not exist yet.** It will only be created after Prompt 01 runs successfully in a governed run with a confirmed evidence map, confirmed truth fingerprint, and confirmed schema profile.

Required properties at creation:
- `@context`: `https://schema.org` (JLSR_001)
- `@graph`: array (JLSR_002)
- All URLs: `https://` only (JLSR_003)
- No blocked module types (JLSR_007)
- No held field properties (JLSR_008)
- All field values evidence-anchored (JLSR_009)
- `NON_PRODUCTION` marker present (JLSR_010)

---

### Controller decision record

| Planned file | Format | Contract schema |
|-------------|--------|-----------------|
| `sample_runs/RUN_001_HOMEPAGE_MODE1/CONTROLLER_DECISION_PROMPT03.json` | JSON | `06_MACHINE_RULES/CONTROLLER_DECISION_SCHEMA_V1_0.json` |

This file will record the Prompt 03 controller decision (`ACCEPT`, `MODIFY`, `REJECT`, `DEFER`, or `HUMAN_REVIEW_REQUIRED`). It will always have `selfApprovalAttempted: false` and `productionAuthorizationGranted: false`.

---

### Validator results

| Planned file | Format | Contract schema |
|-------------|--------|-----------------|
| `sample_runs/RUN_001_HOMEPAGE_MODE1/VALIDATOR_RESULTS.json` | JSON | `06_MACHINE_RULES/VALIDATOR_RESULTS_SCHEMA_V1_0.json` |

This file will record results from Google Rich Results Test, Schema.org Validator, and (if available) Screaming Frog. The `overallValidatorDecision` will be one of `VALIDATION_PASS`, `VALIDATION_WARN`, `VALIDATION_FAIL`, or `VALIDATION_DEFER`.

---

### Analyzer decision record

| Planned file | Format | Contract schema |
|-------------|--------|-----------------|
| `sample_runs/RUN_001_HOMEPAGE_MODE1/CONTROLLER_DECISION_PROMPT14.json` | JSON | `06_MACHINE_RULES/CONTROLLER_DECISION_SCHEMA_V1_0.json` |

This file will record the Prompt 14 post-analyzer controller decision. Adds `PATCH_REQUIRED` as a possible decision.

---

### Output bundle manifest

| Planned file | Format | Contract schema |
|-------------|--------|-----------------|
| `sample_runs/RUN_001_HOMEPAGE_MODE1/OUTPUT_BUNDLE_MANIFEST.json` | JSON | `06_MACHINE_RULES/OUTPUT_BUNDLE_MANIFEST_SCHEMA_V1_0.json` |

This file will be the top-level manifest for the complete run output bundle. It aggregates run metadata, evidence map status, validation status, controller decision status, analyzer decision status, and human approval status into a single record.

---

## What will not exist until human approval

The following artifacts are **gated on explicit human approval** and must not be created before it is granted:

| Artifact | Gate |
|---------|------|
| Final implementation schema (Prompt 12 output) | Human approval of non-production draft |
| Mode 1 lane completion audit record (Prompt 15 output) | Human approval + successful implementation |
| Production lock marker in output bundle manifest | Human approval + all QA/validator passes |

---

## Non-authorization statement

This file list does not authorize:
- Creation of any of the files listed above
- JSON-LD generation
- Schema output production
- Evidence map creation
- Implementation on the current website
- Astro attachment
- Production lock

All planned files will only be created during a future governed run after all preconditions are confirmed.
