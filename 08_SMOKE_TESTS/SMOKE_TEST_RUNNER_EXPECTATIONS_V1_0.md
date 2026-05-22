# Smoke Test Runner Expectations V1.0

**Status:** `MILESTONE_3_LEDGER_AND_HEALTH_TOOLS_COMPLETE_NO_SCHEMA_OUTPUT`

> This document defines the expected behavior of the smoke test runner (`tools/run_standalone_smoke_test.py`) — what checks it runs, what PASS means, what FAIL means, and what neither result authorizes.

---

## Runner identity

| Property | Value |
|----------|-------|
| Script | `tools/run_standalone_smoke_test.py` |
| Fixture | `08_SMOKE_TESTS/fixtures/standalone_v1_0/` |
| Check count | 12 (SMOKE_001 through SMOKE_012) |
| Added by PR | PR #18 |
| Non-authorization | Explicit — see bottom of this document |

---

## Expected PASS behavior

When the package is in a correct post-PR #18 state, `python tools/run_standalone_smoke_test.py .` must return:

```
RESULT: PASS — All smoke tests passed.
Exit code: 0
```

All 12 checks must pass. No checks may fail or be skipped.

---

## Expected check outcomes (bootstrap state)

| Check | Expected outcome | Reason |
|-------|-----------------|--------|
| SMOKE_001 | PASS | Fixture directory exists after PR #17 |
| SMOKE_002 | PASS | `fixture_manifest.json` exists after PR #17 |
| SMOKE_003 | PASS | All 5 fixture data files exist after PR #17 |
| SMOKE_004 | PASS | All 5 fixture JSON files are valid JSON |
| SMOKE_005 | PASS | All fixture files carry required safety headers |
| SMOKE_006 | PASS | No `risefcsoccer.com` URLs in fixture JSON files |
| SMOKE_007 | PASS | No fixture claims `PRODUCTION_LOCKED` |
| SMOKE_008 | PASS | No `.jsonld` files in fixture directory |
| SMOKE_009 | PASS | `fixture_manifest.json` status is `FAKE_FIXTURE_ONLY` |
| SMOKE_010 | PASS | `fixture_manifest.json` `safetyConstraints` block is correct |
| SMOKE_011 | PASS | Package validator returns exit code 0 |
| SMOKE_012 | PASS | `RUN_LEDGER.json` has 0 entries and `NO_PRODUCTION_LOCKS` |

---

## What PASS means

A PASS result (exit code 0) confirms:
- The fake fixture set is structurally correct and safe
- The fixture files carry all required safety headers
- No real Rise FC data is present in the fixture
- No JSON-LD files exist in the fixture directory
- No production lock is claimed anywhere in the fixture
- The package validator still passes the full 12-check suite
- The run ledger remains bootstrap-empty with no production locks

---

## What PASS does NOT mean

A PASS result does NOT:
- Authorize schema output
- Authorize JSON-LD generation
- Authorize evidence map creation as a run artifact
- Authorize current website implementation
- Authorize Astro attachment
- Approve production lock
- Make Mode 1 runnable
- Constitute a real governed schema run

---

## What FAIL means

A FAIL result (exit code 1) indicates a structural integrity problem. Common causes:

| Failure | Likely cause |
|---------|-------------|
| SMOKE_001/002/003 FAIL | Fixture files were deleted or moved |
| SMOKE_004 FAIL | A fixture JSON file was corrupted or made invalid |
| SMOKE_005 FAIL | Safety headers were removed from a fixture file |
| SMOKE_006 FAIL | Real Rise FC URL was accidentally added to a fixture file |
| SMOKE_007 FAIL | A fixture was incorrectly updated to claim production lock |
| SMOKE_008 FAIL | A `.jsonld` file was added to the fixture directory — not permitted |
| SMOKE_009 FAIL | `fixture_manifest.json` `status` was changed from `FAKE_FIXTURE_ONLY` |
| SMOKE_010 FAIL | `safetyConstraints` block was modified to false values |
| SMOKE_011 FAIL | Package structure was broken — run `python tools/validate_package.py .` to diagnose |
| SMOKE_012 FAIL | Real run entries were added to `RUN_LEDGER.json` outside the governed workflow |

---

## Fixture versioning

The current fixture version is `standalone_v1_0`. Adding a new fixture version requires a governed PR. The runner is pinned to `standalone_v1_0`.

---

## Non-authorization statement

This document and the smoke test runner it governs do not authorize schema output, JSON-LD generation, evidence map creation, current website implementation, Astro attachment, or production lock. No governed run has occurred. No real Rise schema exists.
