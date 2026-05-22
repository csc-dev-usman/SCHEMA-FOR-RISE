# Smoke Test Runner and Package Health Reporter — Rise FC Standalone Schema Package V1.0

**Status:** `MILESTONE_3_LEDGER_AND_HEALTH_TOOLS_COMPLETE_NO_SCHEMA_OUTPUT`

> These tools perform synthetic fixture testing and package health reporting. They do not generate schema, create JSON-LD, create run artifacts, or authorize any schema production activity. PASS and CLEAN results confirm tooling integrity only.

---

## Tools in this README

| Tool | Purpose |
|------|---------|
| `tools/run_standalone_smoke_test.py` | Smoke test runner — 12 checks against the canned fake fixture |
| `tools/report_package_health.py` | Package health reporter — read-only summary of package state |

---

## Smoke test runner (`run_standalone_smoke_test.py`)

### Purpose

Runs 12 smoke tests against the canned fake fixture at `08_SMOKE_TESTS/fixtures/standalone_v1_0/`. Verifies that validator tools behave correctly against synthetic inputs. Does **not** test real Rise FC schema.

### Usage

```
python tools/run_standalone_smoke_test.py [package_dir]
python tools/run_standalone_smoke_test.py --help
```

`package_dir` defaults to the current working directory.

### Exit codes

| Code | Meaning |
|------|---------|
| 0 | PASS — all 12 smoke tests passed |
| 1 | FAIL — one or more smoke tests failed |
| 2 | Input/setup error |

### Smoke test check table

| Check | What it verifies |
|-------|-----------------|
| SMOKE_001 | Fixture directory `08_SMOKE_TESTS/fixtures/standalone_v1_0/` exists |
| SMOKE_002 | `fixture_manifest.json` is present |
| SMOKE_003 | All 5 expected fixture data files are present |
| SMOKE_004 | All 5 fixture JSON files parse as valid JSON |
| SMOKE_005 | All fixture files carry `_isFakeFixture: true`, `_notRealRunArtifact: true`, `_fixtureVersion` |
| SMOKE_006 | No real Rise FC URLs in fixture JSON files (no `risefcsoccer.com`) |
| SMOKE_007 | No fixture claims `PRODUCTION_LOCKED` or `productionLockAuthorized: true` |
| SMOKE_008 | No `.jsonld` files in the fixture directory |
| SMOKE_009 | `fixture_manifest.json` `status` field is `FAKE_FIXTURE_ONLY` |
| SMOKE_010 | `fixture_manifest.json` `safetyConstraints` block is correct (all required flags) |
| SMOKE_011 | Package validator (`tools/validate_package.py`) returns exit code 0 (PASS) |
| SMOKE_012 | `RUN_LEDGER.json` is bootstrap-empty (0 entries, `NO_PRODUCTION_LOCKS`) |

### What smoke tests do NOT do

- They do not generate schema or JSON-LD
- They do not create real run artifacts
- They do not append real ledger entries
- They do not exercise real Rise FC schema
- A PASS result does not authorize schema production

---

## Package health reporter (`report_package_health.py`)

### Purpose

Prints a human-readable health summary of the package without modifying any files. Useful for a quick status check at any point in the workflow.

### Usage

```
python tools/report_package_health.py [package_dir]
python tools/report_package_health.py --help
```

`package_dir` defaults to the current working directory.

### Exit codes

| Code | Meaning |
|------|---------|
| 0 | CLEAN — no health warnings |
| 1 | One or more warnings found |
| 2 | Input/setup error |

### Health report sections

| Section | What it checks |
|---------|---------------|
| 1. Package manifest | `package_manifest.json` present, valid JSON, status, version |
| 2. Run ledger | `RUN_LEDGER.json` present, ledger status, production lock status, entry count |
| 3. Mode status | `mode1Runnable`, `mode2AstroReady` from manifest |
| 4. Production safety flags | `schemaOutputCreated`, `jsonLdCreated`, `currentWebsiteImplementationAuthorized`, `astroAttachmentAuthorized`, `mode1Runnable` all false |
| 5. Smoke test fixture | `smokeTestFixtureAdded`, `smokeTestRunnerAdded`, `packageHealthReporterAdded`, `milestone3LedgerAndHealthToolsComplete` from manifest; fixture manifest file presence |
| 6. Validator and tool presence | All 6 tool files present |
| 7. Key file spot-checks | 21 key files across all package folders |
| 8. JSON-LD safety | No `.jsonld` files in the package |

### What the health reporter does NOT do

- It does not modify any files
- It does not generate schema or JSON-LD
- It does not create run artifacts
- A CLEAN result does not authorize schema production

---

## Important: PASS ≠ schema production authorization

A PASS from the smoke test runner and a CLEAN from the health reporter confirm structural and tooling integrity only. Neither result:
- Authorizes schema output
- Authorizes JSON-LD generation
- Authorizes evidence map creation as a run artifact
- Authorizes current website implementation
- Authorizes Astro attachment
- Approves production lock

Human approval is required at every gate. Mode 1 is not runnable until the final runnable handoff PR explicitly authorizes it.

---

## Non-authorization statement

These tools and this README do not authorize schema output, JSON-LD generation, evidence map creation, current website implementation, Astro attachment, or production lock. No governed run has occurred. No real Rise schema exists. `productionLockStatus` remains `NO_PRODUCTION_LOCKS`.
