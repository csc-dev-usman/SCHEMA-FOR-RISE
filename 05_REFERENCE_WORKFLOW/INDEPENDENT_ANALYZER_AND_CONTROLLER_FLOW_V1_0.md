# Independent Analyzer and Controller Post-Analyzer Flow V1.0

**Status:** `INDEPENDENT_ANALYZER_CONTROLLER_FLOW_ADDED_NO_SCHEMA_OUTPUT`

> This document defines the independent analyzer and controller post-analyzer workflow for future governed first real page schema runs. These are workflow definitions only. No analyzer has been run. No findings exist. No controller decisions have been made. No schema has been generated.

---

## Non-authorization statement

This document does not:
- Run the independent analyzer
- Create analyzer findings
- Make a controller decision
- Generate JSON-LD
- Create schema output
- Authorize current website implementation
- Authorize Astro attachment
- Claim production lock
- Mutate Rise Phase 0

---

## Overview

The independent analyzer and controller post-analyzer flow is a two-stage governed review process that occurs after a schema draft has been produced and Claude QA has been completed, and before the human approval gate.

| Stage | Actor | Role |
|-------|-------|------|
| Stage 1 | Independent analyzer (Prompt 13) | Receives run packet; produces findings only |
| Stage 2 | Controller (Prompt 14) | Reviews findings; makes per-finding dispositions; issues final recommendation |

Neither the analyzer nor the controller may:
- Mutate Rise Phase 0
- Mutate source truth
- Self-approve production
- Override human approval

---

## Stage 1 — Independent analyzer

### What the analyzer receives

The analyzer receives a completed future run packet containing:

- The non-production JSON-LD draft
- The evidence map
- The scoped truth view reference and fingerprint
- The schema profile identifier
- The allowed module list
- The blocked module list
- The held field category list
- Claude QA findings (from a prior session)
- The output bundle validator result
- The run metadata record

The analyzer must run in a **fresh session with no prior context** from the schema generation run. This ensures independence.

### What the analyzer checks

The analyzer performs the following checks in order:

| Check | Description |
|-------|-------------|
| 1. Evidence-to-field mapping | Every field in the draft traces to a confirmed entry in the evidence map |
| 2. Truth-view currency | The scoped truth view matches the fingerprint lock |
| 3. Schema profile conformance | Only allowed modules are present; no blocked modules |
| 4. Held field compliance | No held field category has been emitted without recorded owner approval |
| 5. JSON-LD validity | The draft parses as valid JSON-LD; `@context` and `@type` nodes are correct |
| 6. Lint rule compliance | All 10 JSON-LD safety rules (JLSR_001–JLSR_010) are satisfied |
| 7. Validation result review | The output bundle validator returned PASS; no critical Schema.org errors |
| 8. Implementation eligibility | The implementation handoff packet is structurally complete |
| 9. Phase 0 boundary | No field values have been invented or normalized beyond Phase 0 |
| 10. Production lock status | No production lock has been self-claimed |

### What the analyzer produces

The analyzer produces **findings only**. It does not:
- Modify the schema draft
- Approve or reject the run
- Authorize implementation
- Claim production lock

Each finding must conform to `06_MACHINE_RULES/CLAUDE_QA_FINDING_SCHEMA_V1_0.json` with:
- `severity`: BLOCKER, HIGH, MEDIUM, LOW, or INFO
- `category`: SOURCE_TRUTH, HELD_FIELD, BLOCKED_MODULE, JSONLD_VALIDITY, EVIDENCE_MAP, VALIDATOR_RESULT, ASTRO_CARRY, CURRENT_SITE_IMPLEMENTATION, DOCUMENTATION, or OTHER
- `claim`: what the finding asserts
- `evidence`: what supports the finding
- `recommendation`: what the analyzer recommends

The analyzer must not apply its own disposition to findings. Dispositions are the controller's role.

### Analyzer constraints

- Must not mutate Rise Phase 0
- Must not mutate source truth
- Must not self-approve production
- Must not directly authorize current website implementation
- Must not override the governing doctrine
- Operates as a reviewer only — findings are advisory input to the controller

---

## Stage 2 — Controller post-analyzer decision

### What the controller receives

The controller receives:
- The analyzer findings set (from Stage 1)
- The run packet (same as Stage 1)
- All prior Claude QA findings and dispositions

### What the controller does

The controller reviews each analyzer finding and assigns a **per-finding disposition** from:

| Disposition | Meaning |
|-------------|---------|
| `ACCEPT` | Finding is acknowledged and does not block the run |
| `MODIFY` | Finding requires a specific, bounded change to the draft or output |
| `REJECT` | Finding is not sustained — the controller disagrees and records reasoning |
| `DEFER` | Finding is valid but out of scope for this run — will be addressed in a future PR |
| `HUMAN_REVIEW_REQUIRED` | Finding requires human judgment before the controller can dispose it |
| `PATCH_REQUIRED` | Finding requires a targeted patch to the draft or output bundle before proceeding |
| `HOLD` | Finding places the run on hold — run may not proceed until the hold is resolved |

After all per-finding dispositions, the controller issues a **final recommendation**:

| Final recommendation | Meaning |
|---------------------|---------|
| `PROCEED_TO_HUMAN_APPROVAL` | All findings disposed; no unresolved blockers; run may proceed to human approval gate |
| `PATCH_REQUIRED` | One or more findings require a patch; run must pause until patch is applied and re-reviewed |
| `REJECT_RUN` | Run has a critical issue that cannot be patched; the run must be abandoned |
| `HUMAN_REVIEW_REQUIRED` | One or more findings require human judgment before the run can proceed |
| `DEFER_TO_LATER_PR` | Run is valid but out of scope; defer to a future PR |

### Controller constraints

- Must not mutate Rise Phase 0
- Must not override Phase 0 field values
- Must not self-approve production
- Must not bypass the human approval gate
- `PROCEED_TO_HUMAN_APPROVAL` with `unresolvedBlockers: 0` is required before the human approval gate
- The controller review packet must conform to `06_MACHINE_RULES/CONTROLLER_REVIEW_PACKET_SCHEMA_V1_0.json`

---

## Flow sequence

```
Run packet ready
      │
      ▼
[Prompt 13] Independent analyzer
  Fresh session — no prior context
  Checks evidence, truth, profile, blocked modules,
  held fields, validation, JSON-LD, implementation eligibility
  Produces findings only
      │
      ▼
[Prompt 14] Controller post-analyzer decision
  Reviews each finding
  Assigns per-finding disposition
  Issues final recommendation
      │
      ├─ PROCEED_TO_HUMAN_APPROVAL → Human approval gate (Step 8)
      ├─ PATCH_REQUIRED → Apply patch → Re-run analyzer → Re-run controller
      ├─ REJECT_RUN → Run abandoned
      ├─ HUMAN_REVIEW_REQUIRED → Human review → Controller resumes
      └─ DEFER_TO_LATER_PR → Run deferred
```

---

## Templates

For future governed runs, use:

- `FIRST_REAL_PAGE_INDEPENDENT_ANALYZER_REVIEW_TEMPLATE_V1_0.md` — blank analyzer review template
- `CONTROLLER_POST_ANALYZER_DECISION_TEMPLATE_V1_0.md` — blank controller decision template
- `ANALYZER_CONTROLLER_DISPOSITION_MATRIX_V1_0.md` — disposition reference matrix

---

## Reference documents

| Document | Purpose |
|----------|---------|
| `04_OPERATOR_PROMPTS/PROMPT_13_FIRST_REAL_PAGE_INDEPENDENT_ANALYZER_REVIEW_V1_0.txt` | Prompt 13 — the governed analyzer prompt template |
| `04_OPERATOR_PROMPTS/PROMPT_14_CONTROLLER_POST_ANALYZER_DECISION_V1_0.txt` | Prompt 14 — the governed controller post-analyzer prompt template |
| `05_REFERENCE_WORKFLOW/CLAUDE_QA_AND_CONTROLLER_REVIEW_WORKFLOW_V1_0.md` | Full Claude QA and controller review workflow |
| `05_REFERENCE_WORKFLOW/CONTROLLER_DECISION_ENUM_REFERENCE_V1_0.md` | All valid controller decision values |
| `06_MACHINE_RULES/CLAUDE_QA_FINDING_SCHEMA_V1_0.json` | Required shape of a finding record |
| `06_MACHINE_RULES/CONTROLLER_REVIEW_PACKET_SCHEMA_V1_0.json` | Required shape of a controller review packet |
