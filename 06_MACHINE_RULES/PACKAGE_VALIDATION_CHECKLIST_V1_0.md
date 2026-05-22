# Package Validation Checklist V1.0

**Status:** `PACKAGE_VALIDATOR_ADDED_NO_SCHEMA_OUTPUT`

> This checklist documents all checks performed by `tools/validate_package.py`. Use it to manually verify package integrity when the automated validator is not available, or to understand what each check does. This is a documentation contract only — it does not generate schema, create JSON-LD, or authorize any production action.

---

## Purpose

The package validator (`tools/validate_package.py`) runs 12 ordered checks against the Rise FC standalone schema operator package directory. These checks confirm:

1. Required files are present
2. Key JSON files parse correctly
3. No unauthorized artifacts exist
4. The package does not falsely claim production readiness or schema output

This checklist explains each check, its rationale, and what a failure means.

---

## Checks

### CHECK_PKG_001 — `package_manifest.json` present and valid JSON

**What it checks:** `package_manifest.json` exists at the package root and parses as valid JSON without errors.

**Why it matters:** The manifest is the machine-readable source of package state. All other checks depend on its presence. A missing or corrupt manifest means the package cannot be validated.

**Failure means:** File is absent, or its JSON is malformed. Fix by ensuring `package_manifest.json` exists and is valid JSON.

---

### CHECK_PKG_002 — `RUN_LEDGER.json` present and valid JSON

**What it checks:** `RUN_LEDGER.json` exists at the package root and parses as valid JSON.

**Why it matters:** The run ledger is the authoritative record of governed schema runs. A missing or corrupt ledger means run history cannot be read.

**Failure means:** File is absent, or its JSON is malformed. Fix by ensuring `RUN_LEDGER.json` exists and is valid JSON.

---

### CHECK_PKG_003 — All required active files present

**What it checks:** Every file listed in `required` in `PACKAGE_EXPECTED_ACTIVE_FILES_V1_0.json` exists on disk.

**Why it matters:** The package is only coherent when all expected governance documents, contracts, prompts, schemas, and tools are present. Missing files mean operators or validators may act on incomplete information.

**Failure means:** One or more required files are absent. The failure message lists each missing file. Fix by ensuring all package files are present.

---

### CHECK_PKG_004 — Key JSON schema files parse as valid JSON

**What it checks:** All JSON contract schemas in `06_MACHINE_RULES/` parse without errors. This covers: `OUTPUT_BUNDLE_MANIFEST_SCHEMA`, `RUN_METADATA_SCHEMA`, `CONTROLLER_DECISION_SCHEMA`, `VALIDATOR_RESULTS_SCHEMA`, `EVIDENCE_MAP_SCHEMA`, `RISE_SCHEMA_LINT_RULES`, `OUTPUT_BUNDLE_VALIDATOR_EXPECTED_FILES`, `CLAUDE_QA_FINDING_SCHEMA`, `CONTROLLER_REVIEW_PACKET_SCHEMA`, `RUN_LEDGER_SCHEMA`, `PACKAGE_EXPECTED_ACTIVE_FILES`.

**Why it matters:** These are machine-readable contracts. A corrupt schema file silently breaks all tooling that depends on it.

**Failure means:** One or more schema files are absent or contain invalid JSON. Fix the malformed file.

---

### CHECK_PKG_005 — No JSON-LD files present

**What it checks:** No files with a `.jsonld` extension exist anywhere in the package directory (excluding `.git`).

**Why it matters:** No JSON-LD may exist in the package at bootstrap status. Any `.jsonld` file is an unauthorized run artifact.

**Failure means:** A `.jsonld` file was found. Remove it — only governed output bundles containing `emitted_schema.jsonld` are permitted, and only after the final runnable handoff and human approval.

---

### CHECK_PKG_006 — No `sample_runs/` directory present

**What it checks:** No directory named `sample_runs` exists anywhere in the package.

**Why it matters:** `sample_runs/` is a blocked artifact directory. Real run artifacts may only be committed through the governed run workflow, not manually created.

**Failure means:** A `sample_runs/` directory was found. Remove it.

---

### CHECK_PKG_007 — Manifest does not claim production readiness

**What it checks:** None of the following manifest flags are `true`: `currentWebsiteImplementationAuthorized`, `astroAttachmentAuthorized`, `productionLocked`.

**Why it matters:** These flags may only be set to `true` through explicit human approval at the appropriate governed gate. Self-assigning these flags bypasses governance.

**Failure means:** A production readiness flag is `true` without authorization. Revert the flag.

---

### CHECK_PKG_008 — Mode 1 not claimed as runnable

**What it checks:** `package_manifest.json` field `mode1Runnable` is `false` (or absent).

**Why it matters:** Mode 1 is only runnable after the final runnable handoff PR is merged. Prematurely setting `mode1Runnable: true` could mislead operators into executing the schema workflow before all preconditions are met.

**Failure means:** `mode1Runnable: true` was found. This flag may only be set to `true` when the final runnable handoff PR explicitly authorizes it.

---

### CHECK_PKG_009 — Manifest does not claim schema output was created

**What it checks:** None of the following manifest flags are `true`: `schemaOutputCreated`, `jsonLdCreated`, `productionSchemaBundleCreated`, `homepageJsonLdDraftCreated`, `astroAttachmentCreated`.

**Why it matters:** These flags may only be set to `true` when actual governed schema output exists in the package. At bootstrap, all are `false`.

**Failure means:** A schema output flag is `true` without actual output existing. Revert the flag.

---

### CHECK_PKG_010 — Ledger production lock status correct

**What it checks:** When `RUN_LEDGER.json` `entries` is empty, `productionLockStatus` must be `NO_PRODUCTION_LOCKS`. When entries exist, no entry may claim `PRODUCTION_LOCKED` without a `humanApprovalRef`.

**Why it matters:** `PRODUCTION_LOCKED` may never be self-claimed. Any lock without an approval reference is a data integrity violation.

**Failure means:** Ledger claims a production lock that is not justified. Correct the ledger — revert the status or add the required `humanApprovalRef`.

---

### CHECK_PKG_011 — No fake passing report files present

**What it checks:** No files matching patterns like `fake_passing_report*`, `fake_production_approval*`, or `mock_schema_output*` exist in the package.

**Why it matters:** Fake reports could mislead operators or bypass governed gates. They are never permitted.

**Failure means:** A fake report file was found. Remove it.

---

### CHECK_PKG_012 — Homepage scoped truth view parses as valid JSON

**What it checks:** `03_TRUTH_PACK/RISE_PHASE0_SCHEMA_TRUTH_VIEW_HOMEPAGE_SCOPED_V1_0.json` exists and parses as valid JSON.

**Why it matters:** The scoped truth view is the read-only reference for all homepage schema operations. A corrupt file means schema operators cannot verify their source truth.

**Failure means:** File is absent or malformed. Fix by ensuring the truth view JSON is intact.

---

## Running the validator

```
python tools/validate_package.py [package_dir]
```

For a full description of arguments and exit codes, see `tools/README_PACKAGE_VALIDATOR_V1_0.md`.

---

## Non-authorization statement

This checklist and the validator it documents:
- Do **not** generate schema
- Do **not** create JSON-LD
- Do **not** authorize production deployment
- Do **not** authorize schema implementation on the current website
- Do **not** authorize Astro attachment
- Do **not** constitute a governed run

A PASS result confirms package structural integrity only. Human approval is required at every governed gate before any schema implementation or production action.
