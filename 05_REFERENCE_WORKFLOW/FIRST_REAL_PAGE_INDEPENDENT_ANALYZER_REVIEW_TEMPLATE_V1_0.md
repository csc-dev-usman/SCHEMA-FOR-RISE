# First Real Page Independent Analyzer Review Template V1.0

**Status:** `INDEPENDENT_ANALYZER_CONTROLLER_FLOW_ADDED_NO_SCHEMA_OUTPUT`

> This is a blank future-use template for independent analyzer reviews of governed first real page schema runs. It is not a completed analyzer review. No analyzer has been run. No findings exist. Operators must not fill in this template until a governed run packet is ready and all intake preconditions are confirmed.

---

## Non-authorization statement

This template does not run the analyzer, create findings, generate JSON-LD, create schema output, authorize current website implementation, authorize Astro attachment, claim production lock, or mutate Rise Phase 0.

---

## Session identity

| Field | Value |
|-------|-------|
| `analyzerSessionId` | `[ANALYZER_SESSION_ID_PLACEHOLDER]` |
| `runId` | `[RUN_ID_PLACEHOLDER]` |
| `targetUrl` | `[TARGET_URL_PLACEHOLDER]` |
| `pageFamily` | `[PAGE_FAMILY_PLACEHOLDER]` |
| `schemaProfile` | `[SCHEMA_PROFILE_PLACEHOLDER]` |
| `analyzerSessionDate` | `[DATE_PLACEHOLDER — YYYY-MM-DD]` |
| `priorContextCarried` | `false` |
| `analyzerStatus` | `NOT_STARTED` |

> The analyzer must run in a fresh session with no prior context from the schema generation run.

---

## Run packet received

| Item | Status |
|------|--------|
| Non-production JSON-LD draft | `NOT_REVIEWED` |
| Evidence map | `NOT_REVIEWED` |
| Scoped truth view reference | `NOT_REVIEWED` |
| Truth fingerprint | `NOT_REVIEWED` |
| Schema profile | `NOT_REVIEWED` |
| Allowed module list | `NOT_REVIEWED` |
| Blocked module list | `NOT_REVIEWED` |
| Held field category list | `NOT_REVIEWED` |
| Claude QA findings | `NOT_REVIEWED` |
| Output bundle validator result | `NOT_REVIEWED` |
| Run metadata record | `NOT_REVIEWED` |

---

## Analyzer checks

| Check | Status | Notes |
|-------|--------|-------|
| 1. Evidence-to-field mapping | `NOT_STARTED` | |
| 2. Truth-view currency | `NOT_STARTED` | |
| 3. Schema profile conformance | `NOT_STARTED` | |
| 4. Held field compliance | `NOT_STARTED` | |
| 5. JSON-LD validity | `NOT_STARTED` | |
| 6. Lint rule compliance | `NOT_STARTED` | |
| 7. Validation result review | `NOT_STARTED` | |
| 8. Implementation eligibility | `NOT_STARTED` | |
| 9. Phase 0 boundary | `NOT_STARTED` | |
| 10. Production lock status | `NOT_STARTED` | |

---

## Findings

> No findings exist yet. Populate after the analyzer runs in a future governed session.

| Finding ID | Severity | Category | Claim | Evidence | Recommendation |
|------------|----------|----------|-------|----------|----------------|
| `[FINDING_ID_PLACEHOLDER]` | `[SEVERITY]` | `[CATEGORY]` | `[CLAIM]` | `[EVIDENCE]` | `[RECOMMENDATION]` |

**Allowed severity values:** BLOCKER, HIGH, MEDIUM, LOW, INFO

**Allowed category values:** SOURCE_TRUTH, HELD_FIELD, BLOCKED_MODULE, JSONLD_VALIDITY, EVIDENCE_MAP, VALIDATOR_RESULT, ASTRO_CARRY, CURRENT_SITE_IMPLEMENTATION, DOCUMENTATION, OTHER

---

## Analyzer summary

| Field | Value |
|-------|-------|
| `totalFindings` | `0` |
| `blockerCount` | `0` |
| `highCount` | `0` |
| `analyzerRecommendation` | `NOT_STARTED` |
| `analyzerCanProceedToController` | `false` |

---

## Analyzer constraints reminder

- Must not mutate Rise Phase 0
- Must not mutate source truth
- Must not self-approve production
- Must not directly authorize current website implementation
- Must not override the governing doctrine
- Operates as a reviewer only — findings are advisory input to the controller
