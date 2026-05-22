# Standalone Smoke-Test Fixture Contract V1.0

**Status:** `SMOKE_TEST_FIXTURE_CONTRACT_ADDED_NO_SCHEMA_OUTPUT`

> This contract defines the required structure and safety constraints for all smoke-test fixtures in the Rise FC standalone schema operator package. Fixtures must pass all rules in this contract before being accepted into the `08_SMOKE_TESTS/fixtures/` directory.

---

## Purpose

This contract exists to ensure that:
- All smoke-test fixtures are clearly synthetic and non-real
- No real Rise data enters the test fixture layer
- Future tooling (PR #18 smoke-test runner) can rely on a stable, governed fixture interface
- The package validator and output bundle validator can be exercised without triggering governed run rules

---

## Fixture directory naming convention

Every fixture set lives under a versioned subdirectory:

```
08_SMOKE_TESTS/fixtures/<fixture_version>/
```

The current canned fixture is `standalone_v1_0`.

Version format: `standalone_v<major>_<minor>` (e.g., `standalone_v1_0`, `standalone_v1_1`, `standalone_v2_0`).

New fixture versions require a governed PR. Fixture directories must not be created outside the governed PR workflow.

---

## Required files in every fixture version

| File | Required | Purpose |
|------|----------|---------|
| `README_FAKE_FIXTURE.md` | Yes | Explains fixture purpose and non-authorization |
| `fixture_manifest.json` | Yes | Index of all fixture files with fake/version metadata |
| `fake_run_metadata.json` | Yes | Synthetic run metadata conforming to RUN_METADATA_SCHEMA_V1_0 shape |
| `fake_output_bundle_manifest.json` | Yes | Synthetic output bundle manifest conforming to OUTPUT_BUNDLE_MANIFEST_SCHEMA_V1_0 shape |
| `fake_controller_decision.json` | Yes | Synthetic controller decision conforming to CONTROLLER_DECISION_SCHEMA_V1_0 shape |
| `fake_validator_results.json` | Yes | Synthetic validator results conforming to VALIDATOR_RESULTS_SCHEMA_V1_0 shape |

---

## Prohibited files in fixture directories

No fixture directory may contain:

| File | Why blocked |
|------|-------------|
| `emitted_schema.jsonld` | JSON-LD output is never a fixture artifact |
| `evidence_map.json` with real Rise data | Evidence maps are governed run artifacts |
| Any `.jsonld` file | JSON-LD generation is never permitted in the test fixture layer |
| Files claiming `PRODUCTION_LOCKED` | Production lock requires a real governed run and human approval |
| Files containing real Rise contact details | Real data must never enter the test fixture layer |
| Files containing real risefcsoccer.com URLs | All URLs in fixtures use example.invalid |

---

## Required field rules for all fixture JSON files

Every fixture JSON file must include the following top-level safety fields:

| Field | Required value |
|-------|---------------|
| `_isFakeFixture` | `true` |
| `_notRealRunArtifact` | `true` |
| `_fixtureVersion` | The fixture version string (e.g., `"standalone_v1_0"`) |

---

## URL safety rule

All URLs in fixture files must use `example.invalid` as the domain:

```
https://example.invalid/
https://example.invalid/team
```

No real domain names are permitted in fixture files. Not `risefcsoccer.com`. Not any real social or third-party URL.

---

## Held field rules in fixtures

Fixture files must not include values for held field categories, even as placeholders:

- Phone numbers — blocked
- Email addresses — blocked
- Social/sameAs URLs — blocked (use empty array or omit)
- Absolute logo URL (real) — blocked (use `https://example.invalid/logo.png`)
- Coordinates — blocked
- Address/place identity (real) — blocked
- Reviews, ratings — blocked
- Prices — blocked
- Event dates — blocked
- Offer details — blocked
- Testimonial-derived claims — blocked
- Bilingual alternate data — blocked

---

## Fixture manifest required fields

`fixture_manifest.json` must include:

| Field | Description |
|-------|-------------|
| `_isFakeFixture` | `true` |
| `_notRealRunArtifact` | `true` |
| `_fixtureVersion` | Version string |
| `fixtureSetId` | Unique ID for this fixture set |
| `createdByPr` | PR number that created this fixture |
| `status` | `FAKE_FIXTURE_ONLY` |
| `files` | Array of all files in this fixture set with path and purpose |
| `safetyConstraints` | Object confirming safety rules |

---

## Relationship to the smoke-test runner (PR #18)

The smoke-test runner (`tools/run_standalone_smoke_test.py`, added in PR #18) will:
1. Load the fixture manifest from `08_SMOKE_TESTS/fixtures/standalone_v1_0/fixture_manifest.json`
2. Validate each fixture file against the corresponding contract schema shape
3. Run the output bundle validator against the fixture set
4. Run package-level checks
5. Report PASS/WARN/FAIL

The runner does not generate schema. It does not create run artifacts. It confirms tooling behaves correctly against synthetic inputs.

---

## Non-authorization statement

This contract and all fixture files it governs do not authorize:
- Schema output
- JSON-LD generation
- Evidence map creation as a run artifact
- Current website implementation
- Astro attachment
- Production lock
- Real schema operator runs

Fixtures are synthetic tooling artifacts only. No real Rise schema has been produced. No governed runs have occurred.
