# Smoke Tests — Rise FC Standalone Schema Package

**Status:** `SMOKE_TEST_FIXTURE_CONTRACT_ADDED_NO_SCHEMA_OUTPUT`

> This folder contains smoke-test fixtures and tooling for the Rise FC standalone schema operator package. Smoke tests are package and tooling integrity checks only. They do not run the schema operator workflow. They do not generate schema. They do not create run artifacts. They use canned fake fixtures with example.invalid data only — no real Rise data.

---

## Purpose

Smoke tests exist to verify that:
- The package validator runs correctly against synthetic inputs
- The output bundle validator runs correctly against synthetic inputs
- The run ledger tools behave correctly with synthetic entries
- The package structure is intact

Smoke tests do **not**:
- Verify real Rise schema output
- Verify real run ledger entries
- Generate JSON-LD
- Create evidence maps
- Authorize schema production
- Prove Mode 1 is runnable

---

## Current state (after PR #17)

The smoke-test fixture contract and canned fake fixture have been added. The smoke-test runner has **not** yet been added — that is PR #18.

| Component | Status |
|-----------|--------|
| Fixture contract | Added (PR #17) |
| Canned fake fixture (`standalone_v1_0`) | Added (PR #17) |
| Smoke-test runner (`tools/run_standalone_smoke_test.py`) | Pending — PR #18 |
| Package health reporter (`tools/report_package_health.py`) | Pending — PR #18 |

---

## Files in this folder

| File | Purpose |
|------|---------|
| `README_SMOKE_TESTS.md` | This file. Index and non-authorization statement. |
| `STANDALONE_SMOKE_TEST_FIXTURE_CONTRACT_V1_0.md` | Contract defining fixture safety rules, required fields, and what fake fixtures may and may not contain. Added PR #17. |
| `fixtures/standalone_v1_0/README_FAKE_FIXTURE.md` | Explanation of what this fixture is, why it exists, and what it does not contain. Added PR #17. |
| `fixtures/standalone_v1_0/fixture_manifest.json` | Fixture index — lists all fixture files, confirms fake status, records fixture version. Added PR #17. |
| `fixtures/standalone_v1_0/fake_run_metadata.json` | Synthetic run metadata record using example.invalid. Added PR #17. |
| `fixtures/standalone_v1_0/fake_output_bundle_manifest.json` | Synthetic output bundle manifest using example.invalid. Added PR #17. |
| `fixtures/standalone_v1_0/fake_controller_decision.json` | Synthetic controller decision record using example.invalid. Added PR #17. |
| `fixtures/standalone_v1_0/fake_validator_results.json` | Synthetic validator results record using example.invalid. Added PR #17. |

---

## Fixture safety rules

Every fixture in this folder must comply with:

1. **example.invalid only** — all URLs use `https://example.invalid/` as the base. No real risefcsoccer.com URLs.
2. **No real Rise data** — no real contact details, social URLs, coordinates, addresses, prices, event dates, reviews, ratings, or testimonials.
3. **Clearly marked fake** — every fixture file contains `"_isFakeFixture": true` and `"_notRealRunArtifact": true`.
4. **No emitted schema** — no `emitted_schema.jsonld` file exists in any fixture directory.
5. **No production lock** — no fixture claims `PRODUCTION_LOCKED`.
6. **No invented Rise content** — fixture field values are generic placeholders only.

---

## Non-authorization statement

This folder and all files within it do not authorize:
- Schema output
- JSON-LD generation
- Evidence map creation as a run artifact
- Current website implementation
- Astro attachment
- Production lock
- Real schema operator runs

The smoke-test fixture added in PR #17 is a synthetic canned fixture for tooling validation only. No real Rise schema has been produced. No governed runs have occurred. The smoke-test runner is not yet available — it will be added in PR #18.
