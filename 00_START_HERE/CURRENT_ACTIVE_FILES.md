# Current Active Files — Rise FC Standalone Schema Operator Package

**Status:** `TRUTH_PACK_HOMEPAGE_SCOPED_REFERENCE_ADDED_NO_SCHEMA_OUTPUT`

> PR #1 created the package shell. PR #2 added the governing doctrine and source-truth boundary. PR #3 adds the read-only homepage scoped truth-pack reference. The homepage scoped truth view is read-only reference material — it does not authorize schema generation. Prompts, validators, output bundle schemas, smoke tests, and generated schema are still later PRs.

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

## Active placeholder directories

| Directory | Status | Purpose |
|-----------|--------|---------|
| `01_MASTER_FLOW/` | Placeholder only | Future master operator flow documents |
| `04_OPERATOR_PROMPTS/` | Pending PR #5 | Operator prompt files |
| `05_REFERENCE_WORKFLOW/` | Placeholder only | Future reference workflow documents |
| `06_MACHINE_RULES/` | Pending PR #5 | Machine rule files |
| `07_REFERENCE_LISTS/` | Placeholder only | Future reference lists |
| `08_SMOKE_TESTS/` | Pending PR #6 | Smoke test files |
| `tools/` | Placeholder only | Future tooling scripts |

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
- **PR #4:** Homepage schema profile and blocked module policy
- **PR #5:** Operator prompts and machine rules
- **PR #6:** Validators, smoke tests, and final runnable handoff

Generated schema, output bundle schemas, evidence maps, real run artifacts, and smoke tests are still not allowed. They require PR #4 through PR #6.
