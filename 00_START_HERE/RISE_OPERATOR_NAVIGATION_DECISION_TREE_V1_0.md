# Rise Schema Operator Navigation Decision Tree V1.0

**Status:** `OPERATOR_QUICKSTART_CHECKLIST_UPGRADED_NO_SCHEMA_OUTPUT`

---

## Purpose

This document tells operators which document to read based on what they are trying to do. It is a navigation aid, not a runnable workflow. Use it at the start of any session to orient yourself before reading any other file.

---

## Decision tree

### I am new to this package — where do I start?

Read in this order:
1. `README_COMPLETE_OPERATOR_PACKAGE.md` — what the package is, what it is not, current status
2. `00_START_HERE/CURRENT_ACTIVE_FILES.md` — what files exist right now
3. `00_START_HERE/TEAM_QUICKSTART_STANDALONE_URL_REVIEW.md` — plain-language overview
4. `00_START_HERE/FINAL_STANDALONE_OPERATING_MANUAL_INDEX_V1_0.md` — full reading order

---

### I want to understand the operating rules

Read:
- `02_GOVERNING_DOCTRINE/RISE_SCHEMA_GOVERNING_DOCTRINE_V1_0.md`
- `02_GOVERNING_DOCTRINE/RISE_SCHEMA_SOURCE_TRUTH_BOUNDARY_V1_0.md`
- `02_GOVERNING_DOCTRINE/RISE_SCHEMA_OPERATOR_LANE_OWNERSHIP_V1_0.md`
- `02_GOVERNING_DOCTRINE/RISE_SCHEMA_NON_AUTHORIZATION_AND_HOLD_RULES_V1_0.md`

---

### I want to understand what schema is allowed or blocked for the homepage

Read:
- `07_REFERENCE_LISTS/RISE_HOMEPAGE_SCHEMA_PROFILE_V1_0.md` — active profile for route `/`
- `07_REFERENCE_LISTS/RISE_FIRST_PAGE_ALLOWED_MODULES_V1_0.md` — what is allowed and why
- `07_REFERENCE_LISTS/RISE_BLOCKED_SCHEMA_MODULES_FIRST_PAGE_V1_0.md` — what is blocked and why
- `07_REFERENCE_LISTS/RISE_HELD_FIELD_CATEGORIES_FIRST_PAGE_V1_0.md` — what fields require owner approval
- `07_REFERENCE_LISTS/RISE_SCHEMA_PROFILE_DECISION_MATRIX_V1_0.md` — PROCEED/HOLD decision logic

---

### I want to understand the source truth and what facts are confirmed

Read:
- `03_TRUTH_PACK/RISE_PHASE0_TRUTH_SOURCE_MAP_V1_0.md` — what truth classes exist
- `03_TRUTH_PACK/RISE_PHASE0_SCHEMA_TRUTH_VIEW_HOMEPAGE_SCOPED_V1_0.json` — read-only homepage truth reference (not JSON-LD)
- `03_TRUTH_PACK/RISE_HOMEPAGE_TRUTH_FINGERPRINT_LOCK_V1_0.md` — fingerprint verification
- `03_TRUTH_PACK/RISE_CONTACT_SOCIAL_LOGO_OWNER_APPROVAL_WORKSHEET_V1_0.md` — which contact/social/logo fields are approved vs. held

---

### I want to understand the full operating sequence before schema work begins

Read:
- `01_MASTER_FLOW/RISE_STANDALONE_SCHEMA_MASTER_FLOW_V1_0.md` — root master flow
- `01_MASTER_FLOW/RISE_SCHEMA_PAGE_RUN_SEQUENCE_V1_0.md` — per-page sequence from intake to handoff
- `01_MASTER_FLOW/RISE_SCHEMA_MASTER_STOP_CONDITIONS_V1_0.md` — all stop conditions

---

### I want to understand Mode 1 vs. Mode 2

Read:
- `01_MASTER_FLOW/MODE_1_CURRENT_WEBSITE_SCHEMA_OPTIMIZATION_FLOW_V1_0.md` — current-site flow
- `01_MASTER_FLOW/MODE_2_FUTURE_ASTRO_SCHEMA_CARRY_FLOW_V1_0.md` — future Astro carry flow
- `00_START_HERE/RISE_MODE_STATUS_AND_NEXT_STEP_GUIDE_V1_0.md` — current mode status and what is needed next

---

### I want to check whether the package is ready to run

Read:
- `00_START_HERE/RISE_SCHEMA_OPERATOR_PREFLIGHT_CHECKLIST_V1_0.md` — preflight checklist
- `00_START_HERE/OPERATOR_CHECKLIST_STANDALONE_RUN.md` — run checklist (currently disabled)
- `00_START_HERE/FINAL_MODE_1_RUNNABLE_HANDOFF_V1_0.md` — Mode 1 runnable handoff status

---

### I encountered a stop condition — what do I do?

Read:
- `01_MASTER_FLOW/RISE_SCHEMA_MASTER_STOP_CONDITIONS_V1_0.md` — find your stop code and resolution path
- `02_GOVERNING_DOCTRINE/RISE_SCHEMA_NON_AUTHORIZATION_AND_HOLD_RULES_V1_0.md` — hold rule escalation
- `07_REFERENCE_LISTS/RISE_SCHEMA_PROFILE_DECISION_MATRIX_V1_0.md` — HOLD outcome table

Do not estimate or infer past a stop condition. Resolve upstream first.

---

### I want to know what PRs have been merged and what is coming next

Read:
- `DOCTRINE_VERSION_LEDGER.md` — full PR history and schema output status
- `00_START_HERE/CURRENT_ACTIVE_FILES.md` — what is active right now
- `README_COMPLETE_OPERATOR_PACKAGE.md` — next PRs section

---

### I want to check a specific field or module

| Question | Document |
|----------|----------|
| Is this module allowed for the homepage? | `07_REFERENCE_LISTS/RISE_FIRST_PAGE_ALLOWED_MODULES_V1_0.md` |
| Is this module blocked? | `07_REFERENCE_LISTS/RISE_BLOCKED_SCHEMA_MODULES_FIRST_PAGE_V1_0.md` |
| Is this field held? | `07_REFERENCE_LISTS/RISE_HELD_FIELD_CATEGORIES_FIRST_PAGE_V1_0.md` |
| Has this field been owner-approved? | `03_TRUTH_PACK/RISE_CONTACT_SOCIAL_LOGO_OWNER_APPROVAL_WORKSHEET_V1_0.md` |
| What does the decision matrix say? | `07_REFERENCE_LISTS/RISE_SCHEMA_PROFILE_DECISION_MATRIX_V1_0.md` |

---

## Non-authorization

This document does not authorize schema output. It does not authorize JSON-LD generation. It does not authorize current website implementation or Astro attachment. It is a reading-order navigation aid only.
