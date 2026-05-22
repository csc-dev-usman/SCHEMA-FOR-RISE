# Homepage Draft Review and Approval Sequence V1.0

**Status:** `HOMEPAGE_NON_PRODUCTION_DRAFT_CONTRACT_ADDED_NO_SCHEMA_OUTPUT`

> This document defines the future 10-step review and approval sequence for the Rise FC homepage non-production JSON-LD draft. No steps have been executed. No schema has been generated.

---

## Purpose

This document defines the exact order in which a governed homepage draft run must proceed, from the page readiness gate through the final implementation handoff. Operators must follow this sequence in full — no steps may be skipped, reordered, or self-approved.

---

## Full review and approval sequence

### Step 1 — Readiness gate (Prompt 08)

**What:** Confirm the current homepage content is adequate for schema derivation.

**How:** Run `PROMPT_08_PAGE_CONTENT_READINESS_GATE_V1_0.txt` against the current risefcsoccer.com homepage.

**Gate:** Must PASS before proceeding to Step 2.

**Documents confirmed:**
- `03_TRUTH_PACK/RISE_PHASE0_SCHEMA_TRUTH_VIEW_HOMEPAGE_SCOPED_V1_0.json` — read-only, not modified
- `03_TRUTH_PACK/RISE_HOMEPAGE_TRUTH_FINGERPRINT_LOCK_V1_0.md` — fingerprint confirmed

**Stop condition:** `STOP_READINESS_GATE_FAIL` — return to Step 1 after content issues are resolved.

---

### Step 2 — Evidence map

**What:** Create the homepage evidence map. Record field-level evidence decisions for all homepage schema fields.

**How:** Use the contract schema in `06_MACHINE_RULES/EVIDENCE_MAP_SCHEMA_V1_0.json` as the required shape. Populate field-level records from confirmed Phase 0 and page evidence only.

**Gate:** Evidence map must be complete with all fields resolved to `EMIT`, `HELD`, `DEFERRED`, `EXCLUDED_BLOCKED_MODULE`, or `EXCLUDED_NO_EVIDENCE` before proceeding to Step 3.

**Planned output:** `sample_runs/RUN_001_HOMEPAGE_MODE1/HOMEPAGE_EVIDENCE_MAP.json`

**Stop condition:** `STOP_MISSING_EVIDENCE_MAP` — do not proceed without a confirmed evidence map.

---

### Step 3 — Non-production JSON-LD draft (Prompt 01)

**What:** Build the first non-production JSON-LD draft from confirmed evidence only.

**How:** Run `PROMPT_01_BUILD_NON_PRODUCTION_JSONLD_DRAFT_V1_0.txt` using the confirmed evidence map and schema profile.

**Constraints:**
- Allowed modules: `Organization`, `WebSite`, `WebPage`, `BreadcrumbList`
- Blocked modules: per `CONTROLLED_HOMEPAGE_NON_PRODUCTION_JSONLD_DRAFT_CONTRACT_V1_0.md`
- Held fields: per hold matrix in `HOMEPAGE_DRAFT_PRECONDITIONS_AND_HOLD_MATRIX_V1_0.md`
- Draft must carry `NON_PRODUCTION` marker (JLSR_010)
- All 10 JLSR safety rules must be satisfied

**Planned output:** `sample_runs/RUN_001_HOMEPAGE_MODE1/HOMEPAGE_NON_PRODUCTION_JSONLD_DRAFT_V1.json`

---

### Step 4 — Lint check

**What:** Check the draft against all rules in `06_MACHINE_RULES/RISE_SCHEMA_LINT_RULES_V1_0.json`.

**How:** Review draft against all 10 JLSR rules manually or with a future validator script.

**Gate:** All 10 JLSR rules must pass before proceeding to Step 5.

| Rule | Check |
|------|-------|
| JLSR_001 | `@context` = `https://schema.org` exactly |
| JLSR_002 | `@graph` present and is array |
| JLSR_003 | All URLs use `https://` |
| JLSR_004 | No duplicate properties per node |
| JLSR_005 | All `@type` values valid schema.org types |
| JLSR_006 | All properties valid for their `@type` |
| JLSR_007 | No blocked module types present |
| JLSR_008 | No held field properties present |
| JLSR_009 | All field values evidence-anchored |
| JLSR_010 | `NON_PRODUCTION` marker present |

---

### Step 5 — Claude external QA one-zip (Prompt 02)

**What:** Submit the draft to an independent Claude QA session for structured review.

**How:** Run `PROMPT_02_CLAUDE_EXTERNAL_QA_ONE_ZIP_V1_0.txt` in a fresh Claude session with the draft and relevant context packaged.

**Gate:** QA result must be returned with a structured finding before proceeding to Step 6.

**Note:** Claude QA is not a source of truth. It does not override Phase 0. It does not approve production.

---

### Step 6 — Controller decision (Prompt 03)

**What:** Issue a formal controller decision on the draft.

**How:** Run `PROMPT_03_CONTROLLER_DECISION_AND_REGENERATION_V1_0.txt` with the QA result and draft.

**Allowed decisions:** `ACCEPT`, `MODIFY`, `REJECT`, `DEFER`, `HUMAN_REVIEW_REQUIRED`

**Gate:** Decision must be `ACCEPT` before proceeding to Step 7. `MODIFY` returns to Step 3. `REJECT` returns to Prompt 00/01. `DEFER` suspends run.

**Planned output:** `sample_runs/RUN_001_HOMEPAGE_MODE1/CONTROLLER_DECISION_PROMPT03.json`

**Required values:**
- `selfApprovalAttempted: false`
- `productionAuthorizationGranted: false`

---

### Step 7 — Validator review (Prompt 04)

**What:** Submit the draft to external validators and record results.

**How:** Run `PROMPT_04_VALIDATOR_RESULTS_REVIEW_V1_0.txt` after running:
- Google Rich Results Test
- Schema.org Validator
- Screaming Frog (if available)

**Gate:** `overallValidatorDecision` must be `VALIDATION_PASS` or `VALIDATION_WARN` (with documented warnings) before proceeding to Step 8.

**Planned output:** `sample_runs/RUN_001_HOMEPAGE_MODE1/VALIDATOR_RESULTS.json`

**Required cross-checks:**
- `heldFieldDetectedInValidatorOutput: false`
- `blockedModuleDetectedInValidatorOutput: false`

---

### Step 8 — Independent analyzer review + controller post-analyzer decision (Prompts 13 + 14)

**What:** Run an independent analyzer review in a fresh session, then issue a post-analyzer controller decision.

**How:**
1. Run `PROMPT_13_FIRST_REAL_PAGE_INDEPENDENT_ANALYZER_REVIEW_V1_0.txt` in a **fresh Claude session** with no prior context.
2. Return analyzer result to the main session.
3. Run `PROMPT_14_CONTROLLER_POST_ANALYZER_DECISION_V1_0.txt` with the analyzer result.

**Allowed analyzer decisions:** `ANALYZER_PASS`, `ANALYZER_WARN`, `ANALYZER_FAIL`, `ANALYZER_DISAGREE`

**Allowed post-analyzer controller decisions:** `ACCEPT`, `MODIFY`, `REJECT`, `DEFER`, `HUMAN_REVIEW_REQUIRED`, `PATCH_REQUIRED`

**Gate:** Post-analyzer controller decision must be `ACCEPT` before proceeding to Step 9.

**Planned output:** `sample_runs/RUN_001_HOMEPAGE_MODE1/CONTROLLER_DECISION_PROMPT14.json`

**Required values:**
- `selfApprovalAttempted: false`
- `productionAuthorizationGranted: false`

---

### Step 9 — Human approval

**What:** Obtain explicit human approval from the package owner before any implementation handoff.

**How:** Package owner reviews the complete output bundle:
- Non-production draft
- Evidence map
- Controller decision records (Prompt 03 and Prompt 14)
- Validator results
- Analyzer findings

**Gate:** Explicit human written approval required. No other party may grant this approval.

**Required for:**
- Allowing Prompt 12 to run
- Changing `humanApprovalStatus` from `PENDING` to `GRANTED`
- Allowing `productionStatus` to change from `NON_PRODUCTION` to `PRODUCTION_APPROVED`

**What approval authorizes:** Implementation handoff for Mode 1 (current website) or Astro carry packet for Mode 2.

**What approval does not authorize:** Any action beyond the specific page and version reviewed.

---

### Step 10 — Current website implementation handoff or Astro carry packet (Prompt 12)

**What:** Produce the final implementation schema for Mode 1 (or Astro carry packet for Mode 2).

**How:** Run `PROMPT_12_FINAL_VALIDATION_AND_IMPLEMENTATION_SCHEMA_V1_0.txt` **after human approval is confirmed and documented**.

**Mode 1 output:** Implementation packet for the current risefcsoccer.com website. This packet is a handoff — it is not automatically deployed. The website operator must apply it.

**Mode 2 output:** Astro carry packet. This packet is a handoff — it is not automatically deployed. The Astro developer must apply it.

**Final audit (Prompt 15):** After implementation is confirmed, run `PROMPT_15_MODE_1_LANE_COMPLETION_AUDIT_V1_0.txt` and update `RUN_LEDGER.json` with the completed run record.

---

## Sequence summary

| Step | Prompt | Gate |
|------|--------|------|
| 1 | Prompt 08 — Page readiness gate | PASS required |
| 2 | (Evidence map creation) | Complete evidence map required |
| 3 | Prompt 01 — Non-production draft | Draft must satisfy all JLSR rules |
| 4 | Lint check — JLSR_001–JLSR_010 | All 10 rules must pass |
| 5 | Prompt 02 — Claude external QA | QA result returned |
| 6 | Prompt 03 — Controller decision | ACCEPT required |
| 7 | Prompt 04 — Validator review | VALIDATION_PASS or VALIDATION_WARN |
| 8 | Prompt 13 + 14 — Analyzer + post-analyzer | ACCEPT required |
| 9 | Human approval | Explicit written approval required |
| 10 | Prompt 12 — Implementation handoff | Human approval confirmed |

---

## Non-authorization statement

This document does not authorize any of the steps above. All steps are documented as future governed actions. No step has been executed. No schema has been generated. No draft exists.

No step in this sequence may be self-approved by an operator, QA agent, controller agent, or analyzer agent.
