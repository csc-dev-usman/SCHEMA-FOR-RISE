# Rise Schema Master Stop Conditions V1.0

**Status:** `MASTER_FLOW_ADDED_NO_SCHEMA_OUTPUT`

---

## Purpose

This document defines all master stop conditions for the Rise FC standalone schema operator package. A stop condition is a state or event that requires the schema operator to halt immediately and not proceed until the condition is resolved through the appropriate upstream process.

Stop conditions are not suggestions. They are hard rules. No stop condition may be overridden by estimation, inference, workaround, or operator judgment.

---

## Stop condition categories

| Category | Description |
|----------|-------------|
| MISSING_TRUTH | Required truth artifact does not exist |
| STALE_TRUTH | Truth artifact exists but is outdated or fingerprint-mismatched |
| MISSING_PROFILE | Required schema profile does not exist for target route |
| MISSING_EVIDENCE_MAP | Evidence map has not been created for target profile |
| BLOCKED_MODULE | A blocked schema module was requested or included |
| HELD_FIELD_VIOLATION | A held field was emitted without owner approval |
| PREMATURE_OUTPUT | Schema output or JSON-LD was produced before all gates passed |
| PREMATURE_IMPLEMENTATION | Implementation was attempted before human approval |
| PREMATURE_ASTRO_ATTACHMENT | Astro attachment was attempted before carry gates exist |
| PREMATURE_PRODUCTION_LOCK | Production lock was attempted without explicit human authorization |
| MUTATION | Phase 0 or source truth mutation was attempted |

---

## Full stop condition table

| Stop code | Condition | Resolution |
|-----------|-----------|------------|
| `STOP_MISSING_PHASE0_SOURCE` | Phase 0 source reference does not exist for target page | Update Phase 0 or wait for Phase 0 confirmation for this page |
| `STOP_MISSING_TRUTH_VIEW` | Scoped truth view does not exist for target page | Create scoped truth view from Phase 0 in a truth-pack update PR |
| `STOP_FINGERPRINT_MISMATCH` | Truth fingerprint does not match locked value | Investigate truth-view change; update fingerprint via governed truth-pack PR |
| `STOP_STALE_TRUTH` | Truth artifact exists but is outdated | Refresh truth view and update fingerprint via governed truth-pack PR |
| `STOP_MISSING_PROFILE` | No active schema profile exists for target route | Create schema profile via a future doctrine PR |
| `STOP_MISSING_EVIDENCE_MAP` | Evidence map does not exist for target profile | Create evidence map in a future PR before any schema drafting |
| `STOP_MISSING_OPERATOR_PROMPT` | Required operator prompt does not exist | Wait for future PR adding the prompt |
| `STOP_MISSING_VALIDATOR` | Validator does not exist | Wait for future PR adding the validator |
| `STOP_BLOCKED_MODULE_REQUESTED` | A blocked module was requested or included in draft | Remove blocked module; a governing doctrine PR must explicitly authorize the module before it may be used |
| `STOP_HELD_FIELD_NOT_APPROVED` | A held field was emitted without owner approval | Omit the field; do not estimate; owner must approve via the approval worksheet before any field may be emitted |
| `STOP_READINESS_GATE_FAILED` | Readiness gate did not pass | Resolve content readiness issues from Phase 0 or page evidence before proceeding |
| `STOP_PHASE0_CONFLICT` | Phase 0 source and page evidence conflict | Escalate upstream; do not proceed until conflict is resolved |
| `STOP_PREMATURE_JSONLD` | JSON-LD produced before controller ACCEPT and all gates passed | Discard premature JSON-LD; restart from the correct gate |
| `STOP_PREMATURE_IMPLEMENTATION` | Implementation attempted before human approval | Halt implementation; obtain explicit human approval before proceeding |
| `STOP_PREMATURE_ASTRO_ATTACHMENT` | Astro attachment attempted before carry gates exist | Halt; Mode 2 requires carry gate doctrine PR before Astro attachment |
| `STOP_PREMATURE_PRODUCTION_LOCK` | Production lock attempted without explicit human authorization | Remove production lock; explicit human authorization is required |
| `STOP_PHASE0_MUTATION` | Phase 0 mutation was attempted | Halt; Phase 0 is read-only from this package; rollback any mutation |
| `STOP_SOURCE_TRUTH_MUTATION` | Source truth mutation was attempted | Halt; source truth is read-only from this package; rollback any mutation |
| `STOP_WRONG_REPO` | Operating in wrong repository | Stop all work; verify repo identity before proceeding |
| `STOP_CONTROLLER_REJECTED` | Controller REJECTED the draft | Do not proceed to validation; address rejection reasons |
| `STOP_VALIDATION_FAILED` | Validation failed | Do not proceed to handoff; fix validation errors |
| `STOP_ANALYZER_RAISED_NEW_BLOCK` | Analyzer raised new block conditions | Halt; resolve block conditions before proceeding |

---

## Stop condition resolution rules

**A stop condition is resolved only when:**

1. The root cause is identified.
2. The resolution goes through the appropriate upstream process (truth-pack update PR, doctrine PR, owner approval, evidence map creation, etc.).
3. A governed PR records the resolution.
4. Human merge confirms the resolution.

Stop conditions are **not** resolved by:
- Estimation or inference
- Workarounds
- Operator judgment calls
- Placeholder values
- Skipping the gate that triggered the condition

---

## Blocked module stop detail

When `STOP_BLOCKED_MODULE_REQUESTED` is triggered:

1. The blocked module is removed from scope immediately.
2. No output is produced for that module.
3. The block reason is noted.
4. If the module is legitimately needed, a governing doctrine PR must explicitly authorize it with Phase 0 evidence basis and human merge.

Blocked modules for the homepage first-page lane:
- `FAQPage` — `MISSING_PHASE0_TRUTH` + `RISK_OF_INVENTION`
- `Offer` — `MISSING_PHASE0_TRUTH` + `HELD_FIELD_DEPENDENCY` + `OWNER_APPROVAL_REQUIRED`
- `Event` — `MISSING_PHASE0_TRUTH` + `HELD_FIELD_DEPENDENCY`
- `Review` — `RISK_OF_INVENTION` + `DOCTRINE_NOT_YET_DEFINED`
- `AggregateRating` — `RISK_OF_INVENTION` + `MISSING_PHASE0_TRUTH`
- `Place` — `HELD_FIELD_DEPENDENCY` + `OWNER_APPROVAL_REQUIRED`
- `GeoCoordinates` — `HELD_FIELD_DEPENDENCY` + `OWNER_APPROVAL_REQUIRED` + `RISK_OF_INVENTION`
- Testimonial-derived schema — `RISK_OF_INVENTION` + `DOCTRINE_NOT_YET_DEFINED`
- Bilingual schema — `DOCTRINE_NOT_YET_DEFINED`
- Advanced modules — `BLOCKED_BY_DEFAULT`

---

## Held field stop detail

When `STOP_HELD_FIELD_NOT_APPROVED` is triggered:

1. The held field is omitted immediately.
2. No placeholder, inferred value, or estimate is used.
3. The held field category is noted.
4. If the field is needed, the owner must approve it via the owner approval worksheet in `03_TRUTH_PACK/RISE_CONTACT_SOCIAL_LOGO_OWNER_APPROVAL_WORKSHEET_V1_0.md`.

All 15 held field categories default to `NOT_REVIEWED_HELD`:
- Phone
- Email
- sameAs / social URLs
- Absolute logo URL
- Schema description from tagline
- Schema description from mission line
- Coordinates
- Address / place identity
- Prices
- Event dates
- Offer details
- Reviews
- Ratings
- Testimonial-derived claims
- Bilingual alternate data

---

## Mutation stop detail

When `STOP_PHASE0_MUTATION` or `STOP_SOURCE_TRUTH_MUTATION` is triggered:

1. All work stops immediately.
2. The mutation is identified and rolled back.
3. The root cause is investigated.
4. No schema work resumes until the mutation is resolved and confirmed not to have affected Phase 0 content.

This package is strictly downstream of Phase 0. It may read Phase 0. It may not write to Phase 0.

---

## Non-authorization

This document does not authorize schema output. It does not authorize JSON-LD creation. It does not authorize current website implementation or Astro attachment. Stop conditions defined here are in effect regardless of PR number, operating mode, or operator preference.
