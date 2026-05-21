# Current Active Files — Rise FC Standalone Schema Operator Package

**Status:** `BOOTSTRAP_INITIALIZED_NO_SCHEMA_OUTPUT`

> This first PR intentionally does not include prompts, validators, output bundle schemas, smoke tests, or generated schema. Those are later PRs.

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

---

## Active placeholder directories

| Directory | Status | Purpose |
|-----------|--------|---------|
| `01_MASTER_FLOW/` | Placeholder only | Future master operator flow documents |
| `02_GOVERNING_DOCTRINE/` | Placeholder only | Future governing doctrine files (PR #2) |
| `03_TRUTH_PACK/` | Placeholder only | Future Phase 0 truth-pack reference files |
| `04_OPERATOR_PROMPTS/` | Placeholder only | Future operator prompt files |
| `05_REFERENCE_WORKFLOW/` | Placeholder only | Future reference workflow documents |
| `06_MACHINE_RULES/` | Placeholder only | Future machine rule files |
| `07_REFERENCE_LISTS/` | Placeholder only | Future reference lists |
| `08_SMOKE_TESTS/` | Placeholder only | Future smoke test files |
| `tools/` | Placeholder only | Future tooling scripts |

All placeholder directories contain only a `.gitkeep` file. No content files exist yet.

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

- **PR #2:** Governing doctrine and source-truth boundary
- **PR #3:** Phase 0 truth-pack reference and schema truth view boundary
- **PR #4:** Operator prompts and machine rules
- **PR #5:** Validators, smoke tests, and final runnable handoff
