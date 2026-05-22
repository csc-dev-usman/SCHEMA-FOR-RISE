# Controller Decision Enum Reference — V1.0

**Status:** `CLAUDE_QA_CONTROLLER_CONTRACTS_ADDED_NO_SCHEMA_OUTPUT`

---

## Purpose

This document is the authoritative reference for all valid controller decision values used in the Rise FC standalone schema operator package.

These enumerations appear in:
- `06_MACHINE_RULES/CONTROLLER_DECISION_SCHEMA_V1_0.json` — controller decision records (Prompts 03 and 14)
- `06_MACHINE_RULES/CONTROLLER_REVIEW_PACKET_SCHEMA_V1_0.json` — per-finding dispositions and final recommendations
- `06_MACHINE_RULES/CLAUDE_QA_FINDING_SCHEMA_V1_0.json` — controller disposition field on individual findings

---

## Per-finding disposition values

Used in `controllerDecisions[].disposition` within a controller review packet, and in `controllerDisposition` on individual QA findings.

| Value | Meaning | Rationale required |
|-------|---------|-------------------|
| `ACCEPT` | Controller accepts the QA finding and applies the recommendation as-is. | No |
| `MODIFY` | Controller applies a modified version of the recommendation. The actual change must be described. | Yes |
| `REJECT` | Controller rejects the finding. Documented rationale required. Operator must verify rejection is not a doctrine violation. | Yes |
| `DEFER` | Controller defers the finding to a later run or PR. Reason and target must be documented. | Yes |
| `HUMAN_REVIEW_REQUIRED` | Controller escalates this individual finding to human review. Blocks progression for this finding until a human resolves it. | No — but human must act |
| `PATCH_REQUIRED` | This finding requires a corrective patch before the output bundle can proceed. Patch description required. Re-review occurs after patch. | Yes (patch description) |

---

## Final recommendation values

Used in `finalRecommendation` within a controller review packet.

| Value | Meaning | When to use |
|-------|---------|------------|
| `PROCEED_TO_HUMAN_APPROVAL` | All findings resolved. No unresolved blockers. Bundle may proceed to the human approval step (Step 9). | Use when `unresolvedBlockers = 0` and `patchRequired = false` and `humanReviewRequired = false` |
| `PATCH_REQUIRED` | One or more findings have disposition `PATCH_REQUIRED`. The bundle must be patched and re-reviewed before it can proceed. | Use when any finding has disposition `PATCH_REQUIRED` |
| `REJECT_RUN` | The controller rejects the entire run. A new governed run is required from the beginning. | Use when the bundle has fundamental issues that a patch cannot resolve |
| `HUMAN_REVIEW_REQUIRED` | The controller escalates the entire packet to human review before any further action. | Use when any finding has `HUMAN_REVIEW_REQUIRED` or when the controller is uncertain about doctrine compliance |
| `DEFER_TO_LATER_PR` | Controller defers all unresolved findings to a later PR. The deferred findings and their reasons must be documented. | Use for non-blocking findings that are out of scope for the current run |

---

## Controller decision values (Prompts 03 and 14)

Used in `CONTROLLER_DECISION_SCHEMA_V1_0.json` for the controller's top-level decision on an entire draft or analyzer review output.

| Value | Meaning |
|-------|---------|
| `ACCEPT` | Controller accepts the current draft/output and recommends proceeding to the next step. |
| `MODIFY` | Controller accepts with modifications. Changes must be documented and applied before proceeding. |
| `REJECT` | Controller rejects the current draft/output. A new draft is required. |
| `DEFER` | Controller defers the current decision. The reason and conditions for re-evaluation must be documented. |
| `HUMAN_REVIEW_REQUIRED` | Controller escalates to human review. No further automated action until a human resolves. |
| `PATCH_REQUIRED` | Controller identifies a corrective patch requirement. Patch must be applied and re-reviewed. |

---

## Constraint: what the controller cannot decide

The following are **not** valid controller decisions and must never appear in a controller record:

| Invalid action | Why blocked |
|----------------|-------------|
| `PRODUCTION_LOCKED` | Production lock requires explicit human approval — the controller cannot set this |
| `IMPLEMENTATION_AUTHORIZED` | Implementation authorization requires human approval — not a controller decision |
| `PHASE0_MUTATION` | Phase 0 mutation is never allowed from any operator, controller, or Claude session |
| `HELD_FIELD_APPROVED` | Held field approval requires owner approval documented in the owner worksheet — not a controller decision alone |
| `BYPASS_EVIDENCE` | Evidence requirements cannot be bypassed — all emitted fields must have evidence map support |

---

## Escalation ladder

When the controller encounters a situation not covered by existing decisions:

```
1. PATCH_REQUIRED — if a correctable defect exists
2. HUMAN_REVIEW_REQUIRED — if the controller cannot resolve without human input
3. REJECT_RUN — if the run has fundamental doctrine violations
```

The controller must never proceed past a BLOCKER finding with disposition `REJECT` alone. BLOCKER findings that are rejected must be escalated to `HUMAN_REVIEW_REQUIRED` or `REJECT_RUN`.

---

## Cross-references

| Document | Relationship |
|----------|-------------|
| `06_MACHINE_RULES/CONTROLLER_DECISION_SCHEMA_V1_0.json` | Top-level controller decision contract |
| `06_MACHINE_RULES/CONTROLLER_REVIEW_PACKET_SCHEMA_V1_0.json` | Controller review packet schema |
| `06_MACHINE_RULES/CLAUDE_QA_FINDING_SCHEMA_V1_0.json` | QA finding schema with `controllerDisposition` field |
| `05_REFERENCE_WORKFLOW/CLAUDE_QA_AND_CONTROLLER_REVIEW_WORKFLOW_V1_0.md` | Full workflow for QA and controller review |
| `02_GOVERNING_DOCTRINE/RISE_SCHEMA_GOVERNING_DOCTRINE_V1_0.md` | Governing doctrine |
| `02_GOVERNING_DOCTRINE/RISE_SCHEMA_NON_AUTHORIZATION_AND_HOLD_RULES_V1_0.md` | Hold rules and non-authorization |

---

## Non-authorization statement

This reference document does not authorize schema output, production deployment, or any implementation action. Defining valid controller decision values does not authorize any of those decisions to be made. Every controller decision is advisory or preparatory — human approval at Step 9 is required before implementation.
