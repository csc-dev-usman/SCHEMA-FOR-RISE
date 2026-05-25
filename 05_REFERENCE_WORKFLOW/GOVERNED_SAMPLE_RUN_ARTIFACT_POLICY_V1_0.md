# Governed Sample-Run Artifact Policy V1.0

**Status:** `MILESTONE_4_FIRST_REAL_PAGE_RUN_SUPPORT_COMPLETE_NO_SCHEMA_OUTPUT`

---

## Purpose

This document defines the governing policy for sample run artifacts in the Rise FC standalone schema operator package.

It answers three questions:
1. Are real run artifacts allowed in this repository?
2. Are redacted or synthetic sample artifacts allowed, and under what conditions?
3. What must be done before any artifact may be committed?

---

## Default rule

**Real generated schema, validator screenshots, QA zips, current website implementation evidence, and real run artifacts must not be committed to this repository unless a future governed artifact lane explicitly allows them.**

This default applies:
- At bootstrap (PR #1)
- Through Milestone 3 (PR #18)
- Through Milestone 4 (PR #22)
- At any future stage, until a governing doctrine PR explicitly establishes an authorized artifact lane

The absence of an authorized artifact lane means no real run artifacts may be committed — regardless of whether a governed run has occurred.

---

## What counts as a real run artifact

Real run artifacts include:

| Artifact type | Examples | Allowed by default? |
|---------------|---------|---------------------|
| Generated JSON-LD | `homepage.jsonld`, `rise_homepage_schema.json` | NO |
| Output bundle | any `output_bundles/` directory with real data | NO |
| Schema validator screenshots | Schema.org Validator results, Google Rich Results Test screenshots | NO |
| Claude QA zip | any `.zip` containing real QA output | NO |
| Controller decision records with real findings | filled `controller_decision.json` | NO |
| Validator results records with real data | filled `validator_results.json` | NO |
| Run metadata records with real run IDs | filled `run_metadata.json` with real `runId` | NO |
| Current website implementation evidence | deployment screenshots, page source exports | NO |
| Screaming Frog exports with real data | structured data exports from risefcsoccer.com | NO |

---

## Synthetic artifacts

Synthetic artifacts (using `example.invalid` or clearly fake data) are allowed under the following conditions:

1. The artifact is created only for tooling tests or smoke tests
2. The artifact uses `example.invalid` for all URLs
3. The artifact uses clearly placeholder values for all Rise FC fields
4. The artifact carries a `safetyNote` or header clearly marking it as `FAKE_FIXTURE_ONLY` or equivalent
5. The artifact does not claim `PRODUCTION_LOCKED` status
6. The artifact does not contain real Rise FC contact data, addresses, coordinates, social URLs, phone numbers, or email addresses
7. The artifact is placed in `08_SMOKE_TESTS/fixtures/` or an equivalent designated fake-data directory — not in `05_REFERENCE_WORKFLOW/`, `output_bundles/`, or any production-adjacent directory

The existing canned fixture (`08_SMOKE_TESTS/fixtures/standalone_v1_0/`) satisfies all seven conditions and is the approved model for synthetic artifacts.

---

## Redacted sample artifacts

Redacted sample artifacts — real artifacts with sensitive or governed fields removed — are not currently authorized.

A future PR may establish a redacted sample artifact lane with explicit redaction requirements. Until that PR is merged, no redacted artifacts may be committed.

See `REDACTED_SAMPLE_ARTIFACT_REQUIREMENTS_V1_0.md` for the redaction standards that will apply when that lane is established.

---

## `sample_runs/` directory

No `sample_runs/` directory is created by PR #22.

A `sample_runs/` directory must not be created unless it contains only a `README.md` or prohibition policy file, and the directory does not contain any real run artifacts.

Preference: do not create `sample_runs/` until a future authorized artifact lane explicitly requires it.

---

## Authorized artifact lane

An authorized artifact lane is a future governing doctrine PR that:
- Explicitly names the artifact type(s) allowed
- Defines the artifact directory structure
- Defines the naming convention for artifact files
- Defines the redaction requirements (if applicable)
- Defines the commit gate (what approvals are required before commit)
- Sets `realRunArtifactsCommitted: true` in `package_manifest.json`
- Is human-merged

No authorized artifact lane exists as of PR #22.

---

## Artifact commit gate (future use)

When an authorized artifact lane is established, the following gate must be confirmed before committing any real run artifact:

| Gate | Requirement |
|------|-------------|
| Governed run completed | A real governed run with a valid `runId` exists |
| Output bundle validated | `tools/validate_output_bundle.py` returns PASS |
| Controller review complete | `finalRecommendation: PROCEED_TO_HUMAN_APPROVAL`, `unresolvedBlockers: 0` |
| Human approval recorded | Human approver name, date, and scope confirmed |
| Run ledger entry appended | `tools/append_run_ledger_entry.py` used with valid entry |
| Authorized artifact lane exists | Future governing PR has established the lane |
| Redaction requirements confirmed | If artifact contains real data, all required fields are redacted |

This gate does not apply until an authorized artifact lane exists.

---

## What this policy does not do

- It does not create any run artifacts
- It does not authorize real artifact commits
- It does not establish a `sample_runs/` directory
- It does not generate schema
- It does not create JSON-LD
- It does not authorize current website implementation
- It does not authorize production lock
- It does not mutate Rise Phase 0
