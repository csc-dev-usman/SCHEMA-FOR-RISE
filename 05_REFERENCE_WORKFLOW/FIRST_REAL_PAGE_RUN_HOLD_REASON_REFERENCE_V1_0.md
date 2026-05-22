# First Real Page Run Hold Reason Reference V1.0

**Status:** `FIRST_REAL_PAGE_HANDOFF_TEMPLATE_ADDED_NO_SCHEMA_OUTPUT`

> This document defines all hold codes for governed first real page schema runs. When a hold condition is detected, the applicable hold code must be recorded and the run must stop until the hold is resolved. These are governance reference codes only — no real run has been started and no schema has been generated.

---

## Non-authorization statement

This document does not start a schema run, generate JSON-LD, create an evidence map, authorize current website implementation, authorize Astro attachment, or claim production lock.

---

## Hold code index

| Hold code | Condition | Resolution requirement |
|-----------|-----------|------------------------|
| `HOLD_PHASE0_SOURCE_MISSING` | Phase 0 source reference is absent or unconfirmed | Confirm and document the Phase 0 source before proceeding |
| `HOLD_TRUTH_VIEW_MISSING` | Scoped truth view is absent or not located | Confirm the scoped truth view file exists and parses cleanly |
| `HOLD_TRUTH_VIEW_STALE` | Scoped truth view exists but content is out of date with Phase 0 | Re-derive the scoped truth view from current Phase 0 and re-lock the fingerprint |
| `HOLD_FINGERPRINT_MISMATCH` | Run fingerprint does not match the fingerprint lock file | Verify the correct fingerprint lock file; re-confirm truth view currency |
| `HOLD_PROFILE_MISSING` | Schema profile is absent or not confirmed for the target route | Confirm the schema profile identifier and ensure the profile document exists |
| `HOLD_EVIDENCE_MAP_MISSING` | Evidence map for the target page does not exist | Create a governed evidence map conforming to `EVIDENCE_MAP_SCHEMA_V1_0.json` and confirm it before proceeding |
| `HOLD_READINESS_NOT_PASSED` | Page content readiness gate (Prompt 08) has not passed | Run Prompt 08 and confirm the readiness gate passes before proceeding to Prompt 01 |
| `HOLD_BLOCKED_MODULE_REQUESTED` | A blocked schema module has been included in the draft or output | Remove the blocked module and regenerate; consult `RISE_BLOCKED_SCHEMA_MODULES_FIRST_PAGE_V1_0.md` |
| `HOLD_HELD_FIELD_UNAPPROVED` | A held field category has been emitted in the draft without owner approval | Remove the held field; it may not be emitted until owner approval and supporting Phase 0/page evidence exist |
| `HOLD_VALIDATION_MISSING` | The validation protocol (final 9-step sequence) has not been completed | Complete the validation protocol as defined in `FINAL_SCHEMA_VALIDATION_PROTOCOL_V1_0.md` |
| `HOLD_CONTROLLER_DECISION_MISSING` | No controller review decision exists for this run | Complete the controller review (Prompt 03 or Prompt 14) and record the decision before proceeding |
| `HOLD_HUMAN_APPROVAL_MISSING` | Human approval for implementation handoff has not been obtained | Obtain explicit human approval with a recorded approval reference before proceeding to Prompt 12 |
| `HOLD_IMPLEMENTATION_NOT_AUTHORIZED` | Current website implementation has been attempted without authorization | Stop — current website implementation requires a validated output bundle, controller approval, and human approval |
| `HOLD_ASTRO_CARRY_NOT_READY` | Astro schema carry has been attempted before carry gates are defined | Stop — Mode 2 is not yet authorized; Astro carry gates must be defined in a future PR before any Astro attachment |

---

## Hold code detail

### HOLD_PHASE0_SOURCE_MISSING

**Condition:** The run does not have a confirmed, documented Phase 0 source reference for the target page.

**Why it matters:** Every schema field must trace to Phase 0 or confirmed page evidence. Without a Phase 0 anchor, schema cannot be produced without risk of invention.

**Resolution:** Confirm the Phase 0 source document. Record the file path in the run intake fields. Set `phase0SourceConfirmed: true`.

---

### HOLD_TRUTH_VIEW_MISSING

**Condition:** The scoped truth view JSON for the target page is absent or cannot be located.

**Why it matters:** The scoped truth view is the primary reference for what fields are available and what their Phase 0-confirmed values are. Without it, schema derivation has no basis.

**Resolution:** Confirm the scoped truth view exists and parses cleanly. For the homepage, this is `03_TRUTH_PACK/RISE_PHASE0_SCHEMA_TRUTH_VIEW_HOMEPAGE_SCOPED_V1_0.json`.

---

### HOLD_TRUTH_VIEW_STALE

**Condition:** The scoped truth view file exists but its content does not reflect the current approved Phase 0 content for the target page.

**Why it matters:** A stale truth view may produce schema that does not match current Phase 0 reality. This is a source-truth boundary violation.

**Resolution:** Re-derive the scoped truth view from current Phase 0. Update the fingerprint lock. Confirm the new fingerprint before proceeding.

---

### HOLD_FINGERPRINT_MISMATCH

**Condition:** The fingerprint recorded in the run does not match the fingerprint in the lock file.

**Why it matters:** The fingerprint is the integrity check for the scoped truth view. A mismatch means either the truth view has changed or the wrong fingerprint was recorded.

**Resolution:** Verify the fingerprint lock file (`03_TRUTH_PACK/RISE_HOMEPAGE_TRUTH_FINGERPRINT_LOCK_V1_0.md`). Confirm the correct fingerprint. Do not proceed until the mismatch is explained and resolved.

---

### HOLD_PROFILE_MISSING

**Condition:** No schema profile has been confirmed for the target route.

**Why it matters:** The schema profile defines which modules are allowed and which are blocked for this page. Without a confirmed profile, there is no governed scope for schema production.

**Resolution:** Confirm the schema profile identifier and ensure the profile document exists in `07_REFERENCE_LISTS/`. For the homepage, the profile is `HOMEPAGE_SCHEMA_PROFILE`.

---

### HOLD_EVIDENCE_MAP_MISSING

**Condition:** No confirmed evidence map exists for the target page route.

**Why it matters:** The evidence map provides field-level evidence for each schema property. Without it, schema production cannot be tied to confirmed evidence.

**Resolution:** Create a governed evidence map conforming to `06_MACHINE_RULES/EVIDENCE_MAP_SCHEMA_V1_0.json`. The evidence map must exist and be confirmed before proceeding to Prompt 01.

---

### HOLD_READINESS_NOT_PASSED

**Condition:** The page content readiness gate (Prompt 08) has not been run or has not returned a PASS result.

**Why it matters:** Prompt 08 confirms that the page content is ready for schema derivation. If readiness is not confirmed, the page may not have enough confirmed evidence to produce a valid schema draft.

**Resolution:** Run Prompt 08 against the target page. Confirm that the readiness gate passes before proceeding to Prompt 01. Do not skip this gate.

---

### HOLD_BLOCKED_MODULE_REQUESTED

**Condition:** A blocked schema module has been included in a draft, output bundle, or implementation artifact.

**Why it matters:** Blocked modules are prohibited by the governing doctrine and the schema profile. Their inclusion would violate the source-truth boundary and the non-authorization rules.

**Resolution:** Remove the blocked module from the draft or output. Consult `07_REFERENCE_LISTS/RISE_BLOCKED_SCHEMA_MODULES_FIRST_PAGE_V1_0.md` for the complete blocked list and block reasons. Do not include any blocked module without an explicit future doctrine PR authorizing it.

---

### HOLD_HELD_FIELD_UNAPPROVED

**Condition:** A held field category has been emitted in the schema draft or output without owner approval and supporting evidence.

**Why it matters:** Held fields may contain sensitive, unverified, or owner-specific information. Emitting them without approval violates the hold rules.

**Resolution:** Remove the held field from the draft or output. The field may not be emitted until:
1. The Rise owner has reviewed and approved the field value.
2. A confirmed Phase 0 or page evidence record supports the field.
3. The approval is recorded in the owner approval worksheet.

---

### HOLD_VALIDATION_MISSING

**Condition:** The final 9-step validation protocol has not been completed for the run output bundle.

**Why it matters:** The validation protocol is required before any implementation handoff. Skipping validation leaves schema in an unverified state.

**Resolution:** Complete the validation protocol as defined in `FINAL_SCHEMA_VALIDATION_PROTOCOL_V1_0.md`. All 9 steps must be completed in order. Do not proceed to human approval until validation is complete.

---

### HOLD_CONTROLLER_DECISION_MISSING

**Condition:** No controller review decision record exists for this run.

**Why it matters:** The controller review (via Prompt 03 or Prompt 14) is a required governance checkpoint. Without it, findings from Claude QA have not been resolved and the run cannot proceed to human approval.

**Resolution:** Complete the controller review. The final recommendation must be `PROCEED_TO_HUMAN_APPROVAL` with `unresolvedBlockers: 0` before proceeding to Step 8.

---

### HOLD_HUMAN_APPROVAL_MISSING

**Condition:** Explicit human approval for implementation handoff has not been obtained.

**Why it matters:** Human approval is required before any schema is implemented on the current website or carried into Astro. No automated process may substitute for human approval.

**Resolution:** Obtain explicit human approval. Record the approval reference in the run record. Do not proceed to Prompt 12 or any implementation action without a recorded approval reference.

---

### HOLD_IMPLEMENTATION_NOT_AUTHORIZED

**Condition:** Current website implementation has been attempted or requested without a validated output bundle, controller approval, and human approval.

**Why it matters:** Implementing schema without completing the full governed workflow may result in inaccurate, invalid, or unauthorized schema being attached to the public website.

**Resolution:** Complete the full governed run sequence. Obtain human approval. Produce the implementation handoff packet (Prompt 12). Only then may implementation proceed.

---

### HOLD_ASTRO_CARRY_NOT_READY

**Condition:** Mode 2 Astro schema carry has been attempted before carry gates are defined.

**Why it matters:** The Astro carry workflow is not yet authorized. No carry gates, attachment protocols, or Astro route evidence exist. Attaching schema to Astro before these exist is a governance violation.

**Resolution:** Stop. Mode 2 is blocked until a future PR defines the Astro carry gates and attachment protocol. Do not modify any Astro files from this package.
