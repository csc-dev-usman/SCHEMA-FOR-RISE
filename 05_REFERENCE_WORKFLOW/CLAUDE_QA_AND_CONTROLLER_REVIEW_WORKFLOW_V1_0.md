# Claude QA and Controller Review Workflow — V1.0

**Status:** `CLAUDE_QA_CONTROLLER_CONTRACTS_ADDED_NO_SCHEMA_OUTPUT`

---

## Purpose

This document defines the governed workflow for external Claude QA review and controller review of Rise FC schema output bundles.

This is a workflow documentation contract only. No QA has been run. No Claude QA findings exist. No controller review packets exist. No schema has been generated.

---

## What Claude QA is

Claude QA is an **external reviewer** of a future schema output bundle. It is invoked as a fresh Claude session (Prompt 02 or Prompt 13) that has no prior context from the schema generation session.

Claude QA:
- Reads the output bundle files
- Reads the evidence map
- Reads the schema profile and doctrine references
- Identifies findings — potential issues, violations, or concerns
- Records findings conforming to `06_MACHINE_RULES/CLAUDE_QA_FINDING_SCHEMA_V1_0.json`
- Issues an overall recommendation: `PROCEED_TO_CONTROLLER`, `PATCH_REQUIRED_BEFORE_CONTROLLER`, or `HUMAN_REVIEW_REQUIRED`

Claude QA is **not** source truth. Claude QA findings are advisory input to the controller. The controller makes the final decision on each finding.

---

## What Claude QA is not

- Claude QA is **not** a source of factual truth for Rise FC
- Claude QA may **not** invent schema fields, evidence, or Phase 0 facts
- Claude QA may **not** mutate Phase 0 or any source truth
- Claude QA may **not** self-approve production deployment
- Claude QA may **not** override the governing doctrine
- Claude QA may **not** run with prior context from the schema generation session — it must be a fresh session
- Claude QA review does **not** authorize schema output, production deployment, or any implementation action

---

## What the controller is

The controller (Prompt 03 or Prompt 14 post-analyzer) reviews Claude QA findings and makes a disposition decision for each one. The controller:

- Reads the QA finding set
- Makes a disposition decision for each finding: `ACCEPT`, `MODIFY`, `REJECT`, `DEFER`, `HUMAN_REVIEW_REQUIRED`, or `PATCH_REQUIRED`
- Documents rationale for each non-ACCEPT decision
- Issues a final recommendation for the packet: `PROCEED_TO_HUMAN_APPROVAL`, `PATCH_REQUIRED`, `REJECT_RUN`, `HUMAN_REVIEW_REQUIRED`, or `DEFER_TO_LATER_PR`
- Produces a controller review packet conforming to `06_MACHINE_RULES/CONTROLLER_REVIEW_PACKET_SCHEMA_V1_0.json`

---

## What the controller cannot do

- The controller **cannot** mutate Phase 0 or any source truth
- The controller **cannot** self-approve production deployment — human approval is always required
- The controller **cannot** invent schema fields or evidence
- The controller **cannot** override a BLOCKER finding without documented rationale and human review
- The controller **cannot** mark a bundle `PRODUCTION_LOCKED` — only human approval can authorize that
- The controller **cannot** bypass the evidence requirement for held fields

---

## Workflow sequence

The full Claude QA and controller review workflow fits within the 10-step review sequence defined in `05_REFERENCE_WORKFLOW/HOMEPAGE_DRAFT_REVIEW_AND_APPROVAL_SEQUENCE_V1_0.md`:

```
Step 1  — Prompt 08: Page content readiness gate
Step 2  — Evidence map confirmed
Step 3  — Prompt 01: Build non-production JSON-LD draft
Step 4  — Lint check (JLSR_001–JLSR_010)
Step 5  — Prompt 02: Claude external QA one-zip  ← Claude QA review
Step 6  — Prompt 03: Controller decision          ← Controller review (first pass)
Step 7  — Prompt 04: Validator results review
Step 8  — Prompts 13 + 14: Independent analyzer + controller post-analyzer  ← Claude QA + controller (second pass)
Step 9  — Human approval
Step 10 — Prompt 12: Implementation schema
```

Claude QA runs at Steps 5 and 8. Controller review runs at Steps 6 and 14.

---

## Claude QA session rules

When Claude QA is invoked (Prompt 02 or Prompt 13):

1. It must be a **fresh Claude session** — no prior context from the schema generation run
2. The operator provides the output bundle directory and the zip of relevant files (one-zip)
3. Claude QA reads the bundle, identifies findings, and records them using the `findingRecord` shape in `CLAUDE_QA_FINDING_SCHEMA_V1_0.json`
4. Claude QA must not make controller decisions — it records findings and recommendations only
5. Claude QA must state its session nature clearly: it is a reviewer, not a source of truth
6. Claude QA must not produce schema output, JSON-LD, or any run artifact other than the finding set

---

## Controller review rules

When the controller runs (Prompt 03 or Prompt 14):

1. The controller reads the Claude QA finding set
2. For each finding, the controller records a disposition and rationale
3. If any finding has severity BLOCKER and disposition is not `ACCEPT` or `MODIFY`: `patchRequired` or `humanReviewRequired` must be set to true
4. The controller issues a `finalRecommendation`
5. If `finalRecommendation` is `PROCEED_TO_HUMAN_APPROVAL`: all blockers must be resolved (`unresolvedBlockers = 0`)
6. The controller records the packet conforming to `CONTROLLER_REVIEW_PACKET_SCHEMA_V1_0.json`
7. The controller may not mark anything `PRODUCTION_LOCKED` — that requires explicit human approval

---

## Finding severity escalation rules

| Severity | Minimum controller action |
|----------|--------------------------|
| BLOCKER | Must be ACCEPT, MODIFY, or PATCH_REQUIRED/HUMAN_REVIEW_REQUIRED — never silently ignored |
| HIGH | Must be ACCEPT, MODIFY, DEFER, or HUMAN_REVIEW_REQUIRED — rationale required for DEFER |
| MEDIUM | Any disposition allowed — rationale required for REJECT |
| LOW | Any disposition allowed |
| INFO | Any disposition allowed |

---

## Output artifacts

The QA and controller review workflow produces:

| Artifact | File | Shape |
|----------|------|-------|
| Claude QA finding set | `qa_findings.json` (future, in sample_runs) | `CLAUDE_QA_FINDING_SCHEMA_V1_0.json` |
| Controller review packet | `controller_review_packet.json` (future, in sample_runs) | `CONTROLLER_REVIEW_PACKET_SCHEMA_V1_0.json` |
| Controller decision (existing) | `controller_decision.json` | `CONTROLLER_DECISION_SCHEMA_V1_0.json` |

These artifacts do not exist yet. They will be created in a future governed run.

---

## Non-authorization statement

This workflow document does not authorize schema output, production deployment, or any implementation action.

No QA has been run. No Claude QA findings exist. No controller review packets exist. No schema has been generated. No JSON-LD has been created.

Claude QA is a reviewer only. The controller may not self-approve production. Human approval is required at Step 9 before any implementation action may occur.
