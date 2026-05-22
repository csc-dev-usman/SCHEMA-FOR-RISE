# Fake Fixture — standalone_v1_0

**Status:** `SMOKE_TEST_FIXTURE_CONTRACT_ADDED_NO_SCHEMA_OUTPUT`

> THIS IS A FAKE FIXTURE. It contains no real Rise FC data. All URLs use example.invalid. All field values are synthetic placeholders. This fixture exists only to allow smoke tests and tooling validation — not to represent any real Rise FC schema output or governed run.

---

## What this fixture is

`standalone_v1_0` is the first canned synthetic fixture set for the Rise FC standalone schema operator package. It provides fake JSON records that conform to the shape of governed run artifacts, so that the smoke-test runner (PR #18) can exercise the validator tools against realistic-looking but entirely synthetic data.

---

## What this fixture is NOT

- This is **not** a real Rise FC governed run output
- This is **not** a schema draft or JSON-LD output
- This is **not** an evidence map
- This is **not** an approved or validated schema bundle
- This is **not** a real run ledger entry
- This does **not** contain real Rise FC content, URLs, contact details, or social links

---

## Files in this fixture set

| File | What it contains |
|------|-----------------|
| `README_FAKE_FIXTURE.md` | This file |
| `fixture_manifest.json` | Index of all fixture files with safety metadata |
| `fake_run_metadata.json` | Synthetic run metadata — shape only, no real data |
| `fake_output_bundle_manifest.json` | Synthetic output bundle manifest — shape only, no real data |
| `fake_controller_decision.json` | Synthetic controller decision record — shape only, no real data |
| `fake_validator_results.json` | Synthetic validator results — shape only, no real data |

---

## What is deliberately absent

- `emitted_schema.jsonld` — no JSON-LD output is ever created in a fixture
- Real `evidence_map.json` — evidence maps are governed run artifacts only
- Real Rise FC URLs — all URLs use `example.invalid`
- Real contact details, social links, coordinates, prices, event dates

---

## Non-authorization statement

This fixture and all files within it do not authorize schema output, JSON-LD generation, evidence map creation, current website implementation, Astro attachment, or production lock. No governed run has occurred. No real Rise schema exists.
