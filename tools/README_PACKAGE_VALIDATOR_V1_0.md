# Package Validator — Rise FC Standalone Schema Package

**Status:** `PACKAGE_VALIDATOR_ADDED_NO_SCHEMA_OUTPUT`

> This README covers the package validator added in PR #16: `tools/validate_package.py`. This tool is for structural integrity checks only. PR #16 adds no real run entries and no schema output. No JSON-LD has been created. No production locks exist.

---

## Purpose

`validate_package.py` checks that the Rise FC standalone schema operator package directory is structurally sound: all expected active files are present, key JSON files parse correctly, and no unauthorized artifacts exist. It enforces that the package does not falsely claim production readiness or schema output.

This tool is read-only. It does not modify any files.

---

## Usage

```
python tools/validate_package.py [package_dir] [--expected-files PATH]
```

### Arguments

| Argument | Description |
|----------|-------------|
| `package_dir` | Root directory of the package. Defaults to the current working directory (`.`). |
| `--expected-files PATH` | Path to `PACKAGE_EXPECTED_ACTIVE_FILES_V1_0.json`. Defaults to `06_MACHINE_RULES/PACKAGE_EXPECTED_ACTIVE_FILES_V1_0.json` relative to `package_dir`. |

### Typical usage

From the package root:
```
python tools/validate_package.py .
```

Or from any directory with an explicit path:
```
python tools/validate_package.py D:/schema-prompts/SCHEMA-FOR-RISE-NEW
```

---

## Exit codes

| Code | Meaning |
|------|---------|
| `0` | All checks passed. Package is structurally sound. |
| `1` | One or more checks failed. Review the output for details. |
| `2` | Input error (package directory not found, expected files contract missing, etc.). |

---

## Checks

| Check | Description |
|-------|-------------|
| CHECK_PKG_001 | `package_manifest.json` present and parses as valid JSON |
| CHECK_PKG_002 | `RUN_LEDGER.json` present and parses as valid JSON |
| CHECK_PKG_003 | All required active files listed in `PACKAGE_EXPECTED_ACTIVE_FILES_V1_0.json` are present |
| CHECK_PKG_004 | All key JSON schema files in `06_MACHINE_RULES/` parse as valid JSON |
| CHECK_PKG_005 | No JSON-LD files (`*.jsonld`) present anywhere in the package |
| CHECK_PKG_006 | No `sample_runs/` directory present |
| CHECK_PKG_007 | `package_manifest.json` does not claim production readiness (`currentWebsiteImplementationAuthorized`, `astroAttachmentAuthorized`, `productionLocked`) |
| CHECK_PKG_008 | `package_manifest.json` does not claim `mode1Runnable: true` without final runnable handoff |
| CHECK_PKG_009 | `package_manifest.json` does not claim schema output was created (`schemaOutputCreated`, `jsonLdCreated`, etc.) |
| CHECK_PKG_010 | `RUN_LEDGER.json` production lock status is correct (no lock without `humanApprovalRef`) |
| CHECK_PKG_011 | No fake passing report files present |
| CHECK_PKG_012 | Homepage scoped truth view (`03_TRUTH_PACK/RISE_PHASE0_SCHEMA_TRUTH_VIEW_HOMEPAGE_SCOPED_V1_0.json`) parses as valid JSON |

For detailed descriptions of each check — what it tests, why it matters, and what failure means — see `06_MACHINE_RULES/PACKAGE_VALIDATION_CHECKLIST_V1_0.md`.

---

## Expected output (passing package)

```
Rise FC Package Validator
Package dir   : /path/to/SCHEMA-FOR-RISE-NEW
Expected files: /path/to/.../PACKAGE_EXPECTED_ACTIVE_FILES_V1_0.json

============================================================
  Check results
============================================================
  [PASS] CHECK_PKG_001 PASS — package_manifest.json present and valid
  [PASS] CHECK_PKG_002 PASS — RUN_LEDGER.json present and valid
  [PASS] CHECK_PKG_003 PASS — All 78 required files present
  [PASS] CHECK_PKG_004 PASS — All 11 key JSON schemas valid
  [PASS] CHECK_PKG_005 PASS — No JSON-LD files present
  [PASS] CHECK_PKG_006 PASS — No blocked directories present
  [PASS] CHECK_PKG_007 PASS — No production readiness claimed
  [PASS] CHECK_PKG_008 PASS — mode1Runnable is false (correct)
  [PASS] CHECK_PKG_009 PASS — No schema output claimed in manifest
  [PASS] CHECK_PKG_010 PASS — Ledger production lock status is correct
  [PASS] CHECK_PKG_011 PASS — No fake report files present
  [PASS] CHECK_PKG_012 PASS — Homepage scoped truth view parses as valid JSON

============================================================
  Summary
============================================================
  Checks run    : 12
  Passed        : 12
  Failed        : 0

RESULT: PASS — All 12 checks passed.

Non-authorization notice:
  PASS confirms structural integrity only.
  This result does not authorize schema production or production deployment.
```

---

## Related files

| File | Purpose |
|------|---------|
| `06_MACHINE_RULES/PACKAGE_EXPECTED_ACTIVE_FILES_V1_0.json` | Machine-readable expected file list contract. Lists all required, optional, and blocked files through PR #16. |
| `06_MACHINE_RULES/PACKAGE_VALIDATION_CHECKLIST_V1_0.md` | Manual checklist describing each check, rationale, and failure meaning. |
| `tools/validate_output_bundle.py` | Output bundle validator — checks future schema output bundle directories for compliance. |
| `tools/report_run_ledger_status.py` | Read-only ledger status reporter. |
| `package_manifest.json` | Machine-readable package manifest — source of truth for package state flags. |

---

## Non-authorization statement

This tool:
- Does **not** generate schema
- Does **not** create JSON-LD
- Does **not** authorize production deployment
- Does **not** authorize schema implementation on the current website
- Does **not** authorize Astro attachment
- Does **not** constitute a governed run
- Does **not** modify any files

PR #16 adds this tool only. No real run entries have been appended. No schema has been generated. No production locks exist. The ledger remains `BOOTSTRAP_EMPTY_NO_RUNS`.
