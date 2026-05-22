# Analyzer Controller Disposition Matrix V1.0

**Status:** `INDEPENDENT_ANALYZER_CONTROLLER_FLOW_ADDED_NO_SCHEMA_OUTPUT`

> This document defines the full disposition matrix for the independent analyzer and controller post-analyzer flow. It maps finding severity and category to the expected disposition range and governing constraints. No real findings or decisions exist. This is a governance reference document only.

---

## Non-authorization statement

This document does not run the analyzer, create findings, make controller decisions, generate JSON-LD, create schema output, authorize current website implementation, authorize Astro attachment, claim production lock, or mutate Rise Phase 0.

---

## Disposition reference

| Disposition | Who assigns | Meaning | Effect on run |
|-------------|-------------|---------|---------------|
| `ACCEPT` | Controller | Finding acknowledged; does not block | Run continues |
| `MODIFY` | Controller | Specific bounded change required to draft or output | Run pauses until change applied |
| `REJECT` | Controller | Finding not sustained; controller disagrees and records reasoning | Run continues |
| `DEFER` | Controller | Finding valid but out of scope; addressed in future PR | Run continues; finding logged for future |
| `HUMAN_REVIEW_REQUIRED` | Controller | Finding requires human judgment | Run pauses until human reviews |
| `PATCH_REQUIRED` | Controller | Targeted patch required to draft or output bundle | Run pauses until patch applied and re-reviewed |
| `HOLD` | Controller | Run placed on hold | Run may not proceed until hold resolved |

---

## Severity-to-disposition guidance

| Severity | Expected disposition range | Notes |
|----------|---------------------------|-------|
| `BLOCKER` | HOLD, PATCH_REQUIRED, HUMAN_REVIEW_REQUIRED, REJECT_RUN | Must not receive ACCEPT or DEFER without explicit reasoning. Run cannot proceed to human approval while an unresolved BLOCKER exists. |
| `HIGH` | PATCH_REQUIRED, MODIFY, HUMAN_REVIEW_REQUIRED, DEFER, REJECT | Controller must document reasoning for ACCEPT. |
| `MEDIUM` | ACCEPT, MODIFY, DEFER, PATCH_REQUIRED | All dispositions available. |
| `LOW` | ACCEPT, DEFER, MODIFY | Typically ACCEPT or DEFER unless pattern indicates systemic issue. |
| `INFO` | ACCEPT, DEFER | Informational only; no block. |

---

## Category-to-disposition guidance

| Category | Governing constraint | Notes |
|----------|---------------------|-------|
| `SOURCE_TRUTH` | Phase 0 is the source of factual truth. Controller cannot override Phase 0. | A SOURCE_TRUTH finding of BLOCKER severity must result in HOLD or PATCH_REQUIRED unless the finding is REJECT with documented reasoning showing it is not sustained. |
| `HELD_FIELD` | Held fields may not be emitted without owner approval and Phase 0/page evidence. | A HELD_FIELD finding of any severity requires PATCH_REQUIRED or HOLD until the field is removed or approval is recorded. |
| `BLOCKED_MODULE` | Blocked modules may not appear in any schema draft or output. | A BLOCKED_MODULE finding of any severity requires PATCH_REQUIRED. Cannot be ACCEPT or DEFER. |
| `JSONLD_VALIDITY` | JSON-LD must parse cleanly; `@context` and `@type` nodes must be correct. | A JSONLD_VALIDITY BLOCKER requires PATCH_REQUIRED or REJECT_RUN. |
| `EVIDENCE_MAP` | Every field must trace to the evidence map. | A finding indicating a field has no evidence map entry requires PATCH_REQUIRED or removal of the field. |
| `VALIDATOR_RESULT` | Output bundle validator must return PASS. | A VALIDATOR_RESULT BLOCKER requires PATCH_REQUIRED or REJECT_RUN. |
| `ASTRO_CARRY` | Mode 2 is not yet authorized. | Any ASTRO_CARRY finding indicating unauthorized Astro attachment requires HOLD or REJECT_RUN. |
| `CURRENT_SITE_IMPLEMENTATION` | Implementation requires validated output, controller approval, and human approval. | Any finding indicating unauthorized implementation requires HOLD or REJECT_RUN. |
| `DOCUMENTATION` | Documentation findings are advisory. | Typically ACCEPT, MODIFY, or DEFER. |
| `OTHER` | General findings not covered above. | All dispositions available. |

---

## Final recommendation matrix

| Condition | Required final recommendation |
|-----------|-------------------------------|
| All findings disposed; zero unresolved BLOCKERs | `PROCEED_TO_HUMAN_APPROVAL` |
| One or more findings require a patch | `PATCH_REQUIRED` |
| One or more findings require human judgment | `HUMAN_REVIEW_REQUIRED` |
| Finding indicates critical non-patchable issue | `REJECT_RUN` |
| Run valid but out of scope for current PR | `DEFER_TO_LATER_PR` |

> `PROCEED_TO_HUMAN_APPROVAL` with `unresolvedBlockers: 0` is required before the human approval gate (Step 8 of the validation protocol). The human approval gate cannot be bypassed.

---

## What neither the analyzer nor the controller may do

| Prohibited action | Governing rule |
|-------------------|----------------|
| Mutate Rise Phase 0 | Phase 0 is the source of factual truth; it is read-only from this package |
| Mutate source truth | This package is downstream of source truth |
| Self-approve production | Production lock requires explicit human approval and `humanApprovalRef` |
| Override Phase 0 field values | Field values must trace to Phase 0 or confirmed page evidence |
| Authorize current website implementation | Requires validated output bundle, controller approval, and human approval |
| Authorize Astro attachment | Mode 2 is not yet authorized |
| Skip the human approval gate | Human approval is required at Step 8 regardless of controller recommendation |

---

## Usage

This matrix is a governance reference for future governed runs. It does not replace the per-finding judgment of the controller. The controller must record disposition reasoning for any finding where the expected range is not followed, particularly for BLOCKER-severity findings that receive ACCEPT or REJECT.

See `INDEPENDENT_ANALYZER_AND_CONTROLLER_FLOW_V1_0.md` for the full flow definition.
See `CONTROLLER_DECISION_ENUM_REFERENCE_V1_0.md` for the complete authoritative controller decision value reference.
