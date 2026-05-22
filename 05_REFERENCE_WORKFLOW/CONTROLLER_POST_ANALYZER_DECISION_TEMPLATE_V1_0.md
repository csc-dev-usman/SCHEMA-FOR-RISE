# Controller Post-Analyzer Decision Template V1.0

**Status:** `INDEPENDENT_ANALYZER_CONTROLLER_FLOW_ADDED_NO_SCHEMA_OUTPUT`

> This is a blank future-use template for controller post-analyzer decisions on governed first real page schema runs. It is not a completed controller decision. No controller decision has been made. No findings have been disposed. Operators must not fill in this template until an independent analyzer review is complete.

---

## Non-authorization statement

This template does not make a controller decision, dispose findings, generate JSON-LD, create schema output, authorize current website implementation, authorize Astro attachment, claim production lock, or mutate Rise Phase 0.

---

## Session identity

| Field | Value |
|-------|-------|
| `controllerSessionId` | `[CONTROLLER_SESSION_ID_PLACEHOLDER]` |
| `runId` | `[RUN_ID_PLACEHOLDER]` |
| `targetUrl` | `[TARGET_URL_PLACEHOLDER]` |
| `pageFamily` | `[PAGE_FAMILY_PLACEHOLDER]` |
| `schemaProfile` | `[SCHEMA_PROFILE_PLACEHOLDER]` |
| `controllerSessionDate` | `[DATE_PLACEHOLDER — YYYY-MM-DD]` |
| `analyzerSessionRef` | `[ANALYZER_SESSION_ID_PLACEHOLDER]` |
| `controllerStatus` | `NOT_STARTED` |

---

## Input received

| Item | Status |
|------|--------|
| Analyzer findings set | `NOT_REVIEWED` |
| Run packet | `NOT_REVIEWED` |
| Prior Claude QA findings | `NOT_REVIEWED` |
| Output bundle validator result | `NOT_REVIEWED` |

---

## Per-finding dispositions

> No findings exist yet. Populate after the independent analyzer review is complete.

| Finding ID | Severity | Category | Controller disposition | Controller notes |
|------------|----------|----------|------------------------|-----------------|
| `[FINDING_ID_PLACEHOLDER]` | `[SEVERITY]` | `[CATEGORY]` | `[DISPOSITION]` | `[NOTES]` |

**Allowed dispositions:** ACCEPT, MODIFY, REJECT, DEFER, HUMAN_REVIEW_REQUIRED, PATCH_REQUIRED, HOLD

---

## Disposition summary

| Disposition | Count |
|-------------|-------|
| `ACCEPT` | `0` |
| `MODIFY` | `0` |
| `REJECT` | `0` |
| `DEFER` | `0` |
| `HUMAN_REVIEW_REQUIRED` | `0` |
| `PATCH_REQUIRED` | `0` |
| `HOLD` | `0` |
| `unresolvedBlockers` | `0` |

---

## Final recommendation

| Field | Value |
|-------|-------|
| `finalRecommendation` | `NOT_STARTED` |
| `unresolvedBlockers` | `0` |
| `patchRequired` | `false` |
| `humanReviewRequired` | `false` |
| `runRejected` | `false` |
| `runDeferred` | `false` |

**Allowed final recommendation values:**
- `PROCEED_TO_HUMAN_APPROVAL` — all findings disposed; no unresolved blockers
- `PATCH_REQUIRED` — one or more findings require a patch before proceeding
- `REJECT_RUN` — critical issue that cannot be patched; run abandoned
- `HUMAN_REVIEW_REQUIRED` — requires human judgment before run can proceed
- `DEFER_TO_LATER_PR` — run is valid but out of scope; defer to future PR

---

## Controller notes

```
[CONTROLLER_NOTES_PLACEHOLDER]
```

---

## Controller constraints reminder

- Must not mutate Rise Phase 0
- Must not override Phase 0 field values
- Must not self-approve production
- Must not bypass the human approval gate
- `PROCEED_TO_HUMAN_APPROVAL` with `unresolvedBlockers: 0` is required before the human approval gate
- The controller review packet must conform to `06_MACHINE_RULES/CONTROLLER_REVIEW_PACKET_SCHEMA_V1_0.json`
