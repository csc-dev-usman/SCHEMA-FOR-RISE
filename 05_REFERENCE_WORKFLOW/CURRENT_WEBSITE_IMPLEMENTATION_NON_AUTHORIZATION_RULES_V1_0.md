# Current Website Implementation Non-Authorization Rules V1.0

**Status:** `CURRENT_WEBSITE_IMPLEMENTATION_HANDOFF_CHECKLIST_ADDED_NO_SCHEMA_OUTPUT`

---

## Purpose

This document records the non-authorization rules that govern the current website schema implementation lane.

It exists to make explicit — in a dedicated, standalone document — what is and is not authorized at any given stage of the operator package, and what conditions must be met before any implementation action may occur.

---

## Current non-authorization statement (after PR #21)

**No schema has been generated. No JSON-LD has been created. No implementation has occurred.**

After PR #21, nothing in this package authorizes:

- Generating any JSON-LD for the current website
- Attaching schema to any page on risefcsoccer.com
- Implementing schema via inline script tags, CMS fields, file edits, or any other method
- Claiming `PRODUCTION_LOCKED` status for any run
- Approving production deployment of any schema

Mode 1 is still not runnable. The `mode1Runnable` flag in `package_manifest.json` remains `false`. The `currentWebsiteImplementationAuthorized` flag remains `false`.

---

## Non-authorization rules

### Rule CWNAU-001 — No implementation without a validated output bundle

No schema may be implemented on the current website until a validated output bundle exists.

A validated output bundle means:
- All required bundle files are present
- Python output bundle validator (`tools/validate_output_bundle.py`) returns PASS
- JSON-LD validity confirmed
- Lint rules (JLSR_001–JLSR_010) confirmed
- No blocked modules in any JSON-LD
- No held fields emitted without owner approval

### Rule CWNAU-002 — No implementation without controller approval

No schema may be implemented on the current website until the controller review is complete and returns:
- `finalRecommendation: PROCEED_TO_HUMAN_APPROVAL`
- `unresolvedBlockers: 0`

The controller may not self-approve production. The controller may not authorize website implementation directly.

### Rule CWNAU-003 — No implementation without human approval

No schema may be implemented on the current website without explicit human approval.

Human approval means:
- A named human approver has reviewed the validated output bundle
- A named human approver has confirmed controller recommendation
- The approval reference is recorded (approver name/identifier, date, scope)
- The approval is logged before implementation begins

Claude, the controller, or any automated process may not self-approve for production.

### Rule CWNAU-004 — No held fields without owner approval

No held field may be included in any schema implementation without explicit owner approval.

Held field categories (all default to NOT_REVIEWED_HELD):
- phone
- email
- sameAs/social URLs
- absolute logo URL
- schema description from tagline or mission line
- coordinates
- address/place identity
- reviews
- ratings
- prices
- event dates
- offer details
- testimonial-derived claims
- bilingual alternate data

Owner approval must be recorded before any held field can be included.

### Rule CWNAU-005 — No blocked modules

The following modules must never be implemented on the current website under this schema operator package without a future governing doctrine PR explicitly authorizing each one:

- `FAQPage`
- `Offer`
- `Event`
- `Review`
- `AggregateRating`
- `Place`
- `GeoCoordinates`
- Testimonial-derived schema
- Bilingual schema
- Advanced modules

Blocked means: no prompt may reference them, no schema profile may include them, no output bundle may contain them.

### Rule CWNAU-006 — No Phase 0 mutation

This package does not mutate Rise Phase 0. The current website implementation lane does not write to or modify any Phase 0 document, scoped truth view, or truth fingerprint.

Schema is a downstream read model derived from approved Phase 0 truth. The implementation lane reads the truth view — it does not update it.

### Rule CWNAU-007 — No self-merge

All PRs related to current website implementation changes must be human-merged. No self-merge.

### Rule CWNAU-008 — No production lock without human approval reference

The run ledger `productionLockStatus` may not be set to `PRODUCTION_LOCKED` without a recorded `humanApprovalRef` in the run ledger entry.

`PRODUCTION_LOCKED` may never be self-claimed by Claude, a validator, a controller, or any automated process.

### Rule CWNAU-009 — Mode 1 must be runnable before any run begins

The `mode1Runnable` flag in `package_manifest.json` must be `true` before any governed schema run begins.

After PR #21, `mode1Runnable` is still `false`. Mode 1 will not be runnable until a future PR explicitly authorizes it and sets `mode1Runnable: true`.

### Rule CWNAU-010 — Evidence map required before drafting

A confirmed evidence map for the target page must exist before any JSON-LD draft run begins.

After PR #21, no evidence map exists (`evidenceMapAdded: false`). No draft run may begin until a future PR adds a confirmed evidence map for the target page.

---

## What operators may do after PR #21

Operators may:
- Read all documents in this package
- Run `python tools/validate_package.py .` to check structural integrity
- Run `python tools/run_standalone_smoke_test.py .` to check tooling
- Run `python tools/report_package_health.py .` to check package health
- Run `python tools/report_run_ledger_status.py RUN_LEDGER.json` to check ledger state
- Plan future governed runs
- Review the current website implementation handoff checklist for future readiness
- Review the pre-implementation approval gate requirements

Operators must not:
- Generate any JSON-LD
- Create schema output bundles
- Attach schema to the current website
- Implement schema in any form
- Mark Mode 1 as runnable without a governing PR
- Self-approve production lock

---

## Non-authorization history

| Through PR | Implementation authorized? | Schema output created? | JSON-LD created? | mode1Runnable? |
|-----------|-----------------------------|----------------------|-----------------|----------------|
| PR #1–#21 | NO | NO | NO | false |

This table will be updated when a future PR changes any of these values.

---

## Source-truth reminder

Rise Phase 0 remains the source of factual truth. This package is downstream of Phase 0, not above it. No content in this package overrides, repairs, normalizes, or extends Phase 0 truth.
