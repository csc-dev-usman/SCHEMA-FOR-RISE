# Run Ledger Tools — Rise FC Standalone Schema Package

**Status:** `RUN_LEDGER_TOOLS_ADDED_NO_SCHEMA_OUTPUT`

> This README covers the two run ledger tools added in PR #15: the append helper and the read-only reporter. These tools are for future governed runs only. PR #15 adds no real run entries to the ledger. No schema has been generated. No JSON-LD has been created. No production locks exist.

---

## Purpose

These tools support safe, governed management of `RUN_LEDGER.json` after the final runnable handoff is in place. They do not generate schema, modify schema profiles, create JSON-LD, or authorize production deployment.

| Tool | Purpose |
|------|---------|
| `append_run_ledger_entry.py` | Safely append a new entry to `RUN_LEDGER.json` after safety checks |
| `report_run_ledger_status.py` | Read-only ledger status reporter — prints counts and status breakdown |

---

## Tool 1 — `append_run_ledger_entry.py`

### Purpose

Appends a new run ledger entry to `RUN_LEDGER.json` only if the entry passes all governed safety checks. This tool enforces the rules defined in `06_MACHINE_RULES/RUN_LEDGER_SCHEMA_V1_0.json` and `05_REFERENCE_WORKFLOW/RUN_LEDGER_STANDALONE_SCHEMA_REVIEW_GUIDE_V1_0.md`.

### When to use

After a full governed schema run is completed under the final runnable handoff. Do not append entries before the final runnable handoff exists.

### Usage

```
python tools/append_run_ledger_entry.py <entry_file> [--ledger <ledger_file>] [--dry-run]
```

### Arguments

| Argument | Description |
|----------|-------------|
| `entry_file` | Path to a JSON file containing the candidate run ledger entry. Must conform to `RUN_LEDGER_SCHEMA_V1_0.json`. |
| `--ledger PATH` | Path to `RUN_LEDGER.json`. Defaults to `RUN_LEDGER.json` in the current directory. |
| `--dry-run` | Run all checks and print results. Do not write to the ledger. No files are modified. |

### Exit codes

| Code | Meaning |
|------|---------|
| `0` | Entry passed all checks and was appended (or would be appended in `--dry-run`). |
| `1` | One or more checks failed. Ledger not modified. |
| `2` | Input file error (missing file, JSON parse error). |

### Safety checks

| Check | Description |
|-------|-------------|
| CHECK_001 | All required fields are present |
| CHECK_002 | `runId` matches format `RISE_RUN_<PAGE_FAMILY>_<DATE_YYYYMMDD>_<SEQ>` |
| CHECK_003 | `runId` is not already in the ledger (no duplicates) |
| CHECK_004 | `pageFamily` is an allowed value |
| CHECK_005 | `mode` is an allowed value |
| CHECK_006 | `readinessStatus` is an allowed value |
| CHECK_007 | `evidenceMapStatus` is an allowed value |
| CHECK_008 | `draftStatus` is an allowed value |
| CHECK_009 | `qaStatus` is an allowed value |
| CHECK_010 | `controllerStatus` is an allowed value |
| CHECK_011 | `validationStatus` is an allowed value |
| CHECK_012 | `implementationStatus` is an allowed value |
| CHECK_013 | `astroCarryStatus` is an allowed value |
| CHECK_014 | `productionLockStatus` is an allowed value |
| CHECK_015 | `PRODUCTION_LOCKED` requires a non-empty `humanApprovalRef` |
| CHECK_016 | `IMPLEMENTATION_HANDOFF_DELIVERED` requires a non-empty `humanApprovalRef` |
| CHECK_017 | `PRODUCTION_LOCKED` requires `VALIDATION_PASSED` or `VALIDATION_PASSED_WITH_WARNINGS` |
| CHECK_018 | `PRODUCTION_LOCKED` not allowed when `readinessStatus` is `READINESS_GATE_FAILED` |
| CHECK_019 | `PRODUCTION_LOCKED` not allowed when `evidenceMapStatus` is `EVIDENCE_MAP_MISSING` or `EVIDENCE_MAP_STALE` |
| CHECK_020 | `PRODUCTION_LOCKED` not allowed when `validationStatus` is `VALIDATION_FAILED` or `VALIDATION_NOT_RUN` |

### Example candidate entry file shape

```json
{
  "runId": "RISE_RUN_HOMEPAGE_20260601_001",
  "prNumber": 20,
  "targetUrl": "https://www.risefcsoccer.com/",
  "pageFamily": "homepage",
  "mode": "MODE_1_CURRENT_WEBSITE",
  "schemaProfile": "HOMEPAGE_SCHEMA_PROFILE",
  "truthFingerprint": "80edd829806cae271242c6a8e853edabdb8b2f16ca5a8fa1a3fc69ff5b78d53d",
  "runDate": "2026-06-01",
  "readinessStatus": "READINESS_GATE_PASSED",
  "evidenceMapStatus": "EVIDENCE_MAP_CONFIRMED",
  "draftStatus": "DRAFT_PRODUCED",
  "qaStatus": "QA_PASSED",
  "controllerStatus": "CONTROLLER_APPROVED",
  "validationStatus": "VALIDATION_PASSED",
  "implementationStatus": "IMPLEMENTATION_HANDOFF_PENDING",
  "astroCarryStatus": "ASTRO_CARRY_NOT_APPLICABLE",
  "productionLockStatus": "NO_PRODUCTION_LOCKS",
  "notes": "First governed homepage schema run under final runnable handoff."
}
```

### What the tool does when checks pass

When all checks pass and `--dry-run` is not set, the tool:
1. Appends the entry to `ledger["entries"]`
2. Updates `ledger["productionLockStatus"]` based on entry states
3. Updates `ledger["ledgerStatus"]` based on entry states
4. Writes the updated ledger to disk as formatted JSON

The tool does **not** generate schema, create JSON-LD, or authorize production deployment.

---

## Tool 2 — `report_run_ledger_status.py`

### Purpose

Reads `RUN_LEDGER.json` and prints a human-readable summary of the ledger state, entry counts, status breakdowns, and integrity checks. This tool is read-only and does not modify any files.

### Usage

```
python tools/report_run_ledger_status.py [ledger_file]
```

### Arguments

| Argument | Description |
|----------|-------------|
| `ledger_file` | Path to `RUN_LEDGER.json`. Defaults to `RUN_LEDGER.json` in the current directory. |

### Exit codes

| Code | Meaning |
|------|---------|
| `0` | Report printed. No integrity warnings. |
| `1` | Report printed. One or more integrity warnings found (e.g., `PRODUCTION_LOCKED` without `humanApprovalRef`). |
| `2` | Input file error (missing file, JSON parse error). |

### What the reporter prints

1. Ledger-level metadata (ledgerName, ledgerVersion, schemaVersion, status, ledgerStatus, productionLockStatus, lastUpdatedByPr)
2. Safety rules block
3. Entry count summary
4. Status breakdowns for all 11 status fields
5. Production lock integrity check
6. Implementation handoff integrity check
7. All run IDs with key fields
8. Summary with warning count

### Current expected output (bootstrap-empty ledger)

```
Rise FC Run Ledger Status Report
Ledger file : RUN_LEDGER.json

...

Entry summary
  Total entries:                       0

  Ledger is bootstrap-empty. No governed runs have been recorded.
  No schema has been generated. No production locks exist.
```

---

## Non-authorization statement

These tools:
- Do **not** generate schema
- Do **not** create JSON-LD
- Do **not** authorize production deployment
- Do **not** authorize Astro attachment
- Do **not** authorize schema implementation on the current website
- Do **not** constitute a governed run
- Do **not** set or claim `PRODUCTION_LOCKED` without full safety check compliance

PR #15 adds these tools only. No real run entries have been appended. No schema has been generated. No production locks exist. The ledger remains `BOOTSTRAP_EMPTY_NO_RUNS`.

---

## Related documents

| Document | Purpose |
|----------|---------|
| `06_MACHINE_RULES/RUN_LEDGER_SCHEMA_V1_0.json` | Contract schema — required shape of ledger entries |
| `05_REFERENCE_WORKFLOW/RUN_LEDGER_STANDALONE_SCHEMA_REVIEW_GUIDE_V1_0.md` | How to read the ledger and when PRODUCTION_LOCKED may be claimed |
| `RUN_LEDGER.json` | The run ledger — currently bootstrap-empty |
| `00_START_HERE/FINAL_MODE_1_RUNNABLE_HANDOFF_V1_0.md` | Mode 1 runnable handoff — required before any real run entries |
