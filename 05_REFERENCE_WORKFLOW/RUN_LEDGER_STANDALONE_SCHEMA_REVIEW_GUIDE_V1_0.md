# Run Ledger Standalone Schema Review Guide V1.0

**Status:** `RUN_LEDGER_SCHEMA_ADDED_NO_SCHEMA_OUTPUT`

> This guide explains how to read the Rise FC standalone schema run ledger (`RUN_LEDGER.json`), what each field means, and when production lock status may — and may not — be claimed. This is a documentation contract only — no runs have been recorded, no schema has been generated, and no production locks exist. Claiming `PRODUCTION_LOCKED` without explicit human approval is not permitted under any circumstances.

---

## Purpose

The run ledger (`RUN_LEDGER.json`) is the authoritative record of all governed schema runs performed under this package. It tracks the status of each run from readiness gate through implementation handoff and, eventually, production lock. This guide explains how to read the ledger, how to understand each field, and what governance rules apply.

---

## Current ledger state

The ledger is currently bootstrap-empty. No governed runs have been performed. No schema has been generated. No entries exist. The ledger will be populated only after the final runnable handoff is in place and a governed run is completed.

`ledgerStatus: BOOTSTRAP_EMPTY_NO_RUNS`
`productionLockStatus: NO_PRODUCTION_LOCKS`

---

## How to read the ledger

### Ledger-level fields

| Field | Description |
|-------|-------------|
| `ledgerName` | Human-readable name of the ledger |
| `ledgerVersion` | Semantic version of the ledger document |
| `schemaVersion` | Version of `RUN_LEDGER_SCHEMA_V1_0.json` used to validate this ledger |
| `status` | Package status string at time of last ledger update |
| `ledgerStatus` | Current state of the ledger — one of: `BOOTSTRAP_EMPTY_NO_RUNS`, `HAS_DRAFT_RUNS`, `HAS_COMPLETED_RUNS`, `HAS_PRODUCTION_LOCKED_RUNS` |
| `productionLockStatus` | Whether any entry in the ledger has been production-locked — `NO_PRODUCTION_LOCKS` or `HAS_PRODUCTION_LOCKS` |
| `safetyRules` | Object confirming package-level safety constraints |
| `entries` | Array of run ledger entry objects |

### Run entry fields

| Field | Required | Description |
|-------|----------|-------------|
| `runId` | Yes | Unique run identifier. Format: `RISE_RUN_<PAGE_FAMILY>_<DATE_YYYYMMDD>_<SEQ>`. Never reuse. |
| `prNumber` | Yes | PR number that authorized this run |
| `targetUrl` | Yes | Confirmed target page URL |
| `pageFamily` | Yes | Page family: homepage, program_page, about_page, contact_page, other |
| `mode` | Yes | `MODE_1_CURRENT_WEBSITE` or `MODE_2_ASTRO_CARRY` |
| `schemaProfile` | Yes | Confirmed schema profile name (e.g., `HOMEPAGE_SCHEMA_PROFILE`) |
| `truthFingerprint` | Yes | SHA-256 truth fingerprint confirmed at run start |
| `runDate` | Yes | ISO 8601 date of the run |
| `readinessStatus` | Yes | Result of Prompt 08 readiness gate |
| `evidenceMapStatus` | Yes | Status of the evidence map used for this run |
| `draftStatus` | Yes | Status of the non-production JSON-LD draft |
| `qaStatus` | Yes | Result of Claude QA and analyzer review |
| `controllerStatus` | Yes | Result of controller decision |
| `validationStatus` | Yes | Result of full 9-step validation protocol |
| `implementationStatus` | Yes | Status of current website implementation handoff |
| `astroCarryStatus` | Yes | Status of Astro schema carry (typically `ASTRO_CARRY_NOT_APPLICABLE` for Mode 1) |
| `productionLockStatus` | Yes | `NO_PRODUCTION_LOCKS` (default) or `PRODUCTION_LOCKED` (requires human approval) |
| `humanApprovalRef` | No | Required when `implementationStatus` is `IMPLEMENTATION_HANDOFF_DELIVERED` |
| `outputBundleRef` | No | Reference to the output bundle for this run |
| `notes` | No | Optional free-text notes |

---

## Reading a run entry

When reading a run entry, check the following in sequence:

1. **Is `truthFingerprint` correct?** It must match the value in `RISE_HOMEPAGE_TRUTH_FINGERPRINT_LOCK_V1_0.md` for homepage runs. A mismatched fingerprint means the schema was built from stale truth.

2. **Did the readiness gate pass?** `readinessStatus` must be `READINESS_GATE_PASSED`. Any other value means the run was not properly gated.

3. **Was the evidence map confirmed?** `evidenceMapStatus` must be `EVIDENCE_MAP_CONFIRMED`. A missing or stale evidence map is a blocker.

4. **Did validation pass?** `validationStatus` must be `VALIDATION_PASSED` or `VALIDATION_PASSED_WITH_WARNINGS`. `VALIDATION_FAILED` or `VALIDATION_NOT_RUN` means the schema was not properly validated before any handoff.

5. **Was human approval obtained?** If `implementationStatus` is `IMPLEMENTATION_HANDOFF_DELIVERED`, `humanApprovalRef` must be present and non-empty. No implementation handoff may be recorded without a human approval reference.

6. **Is `productionLockStatus` justified?** See section below — `PRODUCTION_LOCKED` requires strict conditions.

---

## When `PRODUCTION_LOCKED` may be claimed

`PRODUCTION_LOCKED` is the most restricted status in the ledger. It may **only** be claimed when all of the following are true:

- [ ] A governed run was completed under the final runnable handoff
- [ ] All 9 steps of the validation protocol passed
- [ ] Controller review returned `PROCEED_TO_HUMAN_APPROVAL` with `unresolvedBlockers: 0`
- [ ] A human (package owner or authorized approver) has explicitly reviewed the full output bundle
- [ ] The human approver has set `implementationHandoffAuthorized: true` AND `productionLockAuthorized: true` in the approval record
- [ ] The `humanApprovalRef` field in the ledger entry points to the actual approval record
- [ ] The schema has been successfully implemented on the target page
- [ ] No post-implementation issues have been identified

**`PRODUCTION_LOCKED` may never be:**
- Self-claimed by Claude, a validator, or any automated process
- Set without a `humanApprovalRef`
- Set before validation is complete
- Set before human approval is obtained
- Set on the basis of a partial run or a non-governed run
- Set retroactively without supporting evidence

If `PRODUCTION_LOCKED` appears in the ledger without all conditions being met, treat it as a data integrity violation and escalate to the package owner.

---

## When `productionLockStatus` stays `NO_PRODUCTION_LOCKS`

In all of the following cases, `productionLockStatus` must remain `NO_PRODUCTION_LOCKS`:

| Situation | Status |
|-----------|--------|
| Bootstrap — no runs performed | `NO_PRODUCTION_LOCKS` |
| Run in progress | `NO_PRODUCTION_LOCKS` |
| Draft produced but not yet validated | `NO_PRODUCTION_LOCKS` |
| Validation passed but human approval not yet obtained | `NO_PRODUCTION_LOCKS` |
| Implementation handoff delivered but production not yet live | `NO_PRODUCTION_LOCKS` |
| Any run without confirmed `humanApprovalRef` | `NO_PRODUCTION_LOCKS` |
| Mode 2 Astro carry runs before Astro carry gates are defined | `NO_PRODUCTION_LOCKS` |

---

## Ledger integrity rules

The run ledger must not be manually edited outside the governed append workflow. When the ledger append helper is available (PR #15), all entries must be added through that tool, which enforces the safety rules before writing.

Until the append helper exists:
- Do not add fake run entries to the ledger
- Do not add entries claiming `PRODUCTION_LOCKED` without all conditions met
- Do not add duplicate `runId` values
- Do not modify or delete existing entries
- Do not add `entries` while `ledgerStatus` is `BOOTSTRAP_EMPTY_NO_RUNS` unless a real governed run has been completed under the final runnable handoff

---

## Related documents

| Document | Purpose |
|----------|---------|
| `06_MACHINE_RULES/RUN_LEDGER_SCHEMA_V1_0.json` | Contract schema defining the required shape of ledger entries |
| `05_REFERENCE_WORKFLOW/FINAL_SCHEMA_VALIDATION_PROTOCOL_V1_0.md` | The 9-step validation protocol that must complete before any production lock |
| `05_REFERENCE_WORKFLOW/VALIDATION_EVIDENCE_HANDOFF_REQUIREMENTS_V1_0.md` | Required evidence metadata for implementation handoff |
| `00_START_HERE/FINAL_MODE_1_RUNNABLE_HANDOFF_V1_0.md` | Mode 1 runnable handoff — required before any real run entries |
| `03_TRUTH_PACK/RISE_HOMEPAGE_TRUTH_FINGERPRINT_LOCK_V1_0.md` | Homepage truth fingerprint — must match `truthFingerprint` in ledger entries |

---

## Non-authorization statement

This guide:
- Does **not** authorize production deployment
- Does **not** authorize any schema implementation
- Does **not** authorize Astro attachment
- Does **not** authorize production lock
- Does **not** constitute a run entry

No governed run has been performed. No schema has been generated. No production lock has been claimed. The ledger is bootstrap-empty. The first real run entry may only be added after the final runnable handoff is in place and a full governed run is completed.
