# Real Run Artifact Commit Rules V1.0

**Status:** `MILESTONE_4_FIRST_REAL_PAGE_RUN_SUPPORT_COMPLETE_NO_SCHEMA_OUTPUT`

---

## Purpose

This document states the commit rules for real run artifacts in the Rise FC standalone schema operator package.

It is a prohibition-first reference: the default answer to "may I commit this real artifact?" is **NO** until an authorized artifact lane exists.

---

## Current status

**REAL RUN ARTIFACTS ARE PROHIBITED BY DEFAULT.**

As of PR #22:
- `realRunArtifactsCommitted` in `package_manifest.json` is `false`
- No authorized artifact lane exists
- No real run artifacts may be committed to this repository

---

## What is prohibited

The following may not be committed to this repository without an authorized artifact lane:

### Rule RAC-001 — No real JSON-LD files

No `.jsonld` files containing real Rise FC schema data may be committed.

This includes:
- Homepage JSON-LD drafts
- Any schema output for any route on risefcsoccer.com
- Any JSON-LD file containing real Rise FC organization data, URL data, or breadcrumb data

### Rule RAC-002 — No real output bundles

No `output_bundles/` directory or equivalent containing real run outputs may be committed.

A real output bundle is any directory or archive containing:
- A generated JSON-LD file for a real Rise FC route
- A run metadata record with a real `runId`
- A controller decision record with real findings
- A validator results record with real validation data

### Rule RAC-003 — No validator screenshots or exports

No screenshots from the Schema.org Validator, Google Rich Results Test, or Screaming Frog containing real Rise FC URLs or real schema output may be committed.

### Rule RAC-004 — No Claude QA zips

No `.zip` file or archive containing real Claude QA output for a real Rise FC route may be committed.

### Rule RAC-005 — No real controller or validator records

No filled `controller_decision.json`, `validator_results.json`, or `run_metadata.json` records containing real Rise FC data may be committed outside an authorized artifact lane.

### Rule RAC-006 — No current website implementation evidence

No screenshots, page source exports, or deployment records from risefcsoccer.com confirming live schema may be committed without an authorized artifact lane.

### Rule RAC-007 — No `sample_runs/` directory with real data

No `sample_runs/` directory may be created containing real run artifacts. If `sample_runs/` is created, it must contain only a README or prohibition policy file.

---

## What is permitted

| Artifact type | Conditions |
|---------------|-----------|
| Synthetic fixtures | `example.invalid` URLs, clearly fake data, placed in `08_SMOKE_TESTS/fixtures/`, no real Rise FC fields, `FAKE_FIXTURE_ONLY` header |
| Blank templates | All fields NOT_STARTED or placeholder, no real data |
| Policy and governance documents | This file and related governance contracts |
| Tool scripts | Python validator and helper scripts that process but do not contain real run data |

---

## How real artifact commit prohibition is enforced

1. `package_manifest.json` carries `realRunArtifactsCommitted: false` — the package validator checks this flag
2. The package validator (`tools/validate_package.py`) checks for `.jsonld` files and blocked directories (CHECK_PKG_005, CHECK_PKG_006)
3. The package validator checks that no production readiness is claimed (CHECK_PKG_007)
4. The smoke test runner checks that no real Rise FC URLs appear in fixture files (SMOKE_006)
5. The smoke test runner checks that no fixture claims `PRODUCTION_LOCKED` (SMOKE_007)
6. Human review is required at every PR gate — no self-merge

These enforcement mechanisms are structural. They catch prohibited artifacts at validation time, before any PR merge.

---

## How to establish a real artifact commit lane (future)

To authorize real artifact commits, a future governing PR must:

1. Define the artifact type(s) to be allowed
2. Define the artifact directory and naming convention
3. Define commit gate requirements (governed run complete, validated, controller-approved, human-approved)
4. Set `realRunArtifactsCommitted: true` in `package_manifest.json`
5. Update the package validator expected files contract if new required files are introduced
6. Be human-merged

Until such a PR exists, this prohibition document governs.

---

## What this document does not do

- It does not create any artifacts
- It does not establish an artifact lane
- It does not generate schema
- It does not create JSON-LD
- It does not authorize any commit of real run data
- It does not mutate Rise Phase 0
