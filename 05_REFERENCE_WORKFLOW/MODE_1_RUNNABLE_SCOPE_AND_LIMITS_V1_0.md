# Mode 1 Runnable Scope and Limits V1.0

**Status:** `MILESTONE_5_ASTRO_CARRY_BRIDGE_COMPLETE_MODE_1_SUPERVISED_RUNNABLE_NO_SCHEMA_OUTPUT`

---

## Purpose

This document defines the exact scope and limits of Mode 1 supervised-runnable status as established by PR #26. It provides a definitive CAN/CANNOT reference for operators who have confirmed all start conditions in `MODE_1_OPERATOR_START_CONDITIONS_V1_0.md`.

---

## What operators CAN now do

| Action | Reference |
|--------|-----------|
| Start Prompt 00 intake — collect target URL, truth state, profile, blocked modules, held fields, evidence map status | `04_OPERATOR_PROMPTS/PROMPT_00_STANDALONE_URL_REVIEW_START_V1_0.txt` |
| Use the preflight checklist and readiness gates | `00_START_HERE/RISE_SCHEMA_OPERATOR_PREFLIGHT_CHECKLIST_V1_0.md` |
| Prepare a first real page run packet using the handoff template | `05_REFERENCE_WORKFLOW/FIRST_REAL_PAGE_RUN_HANDOFF_TEMPLATE_V1_0.md` |
| Apply hold codes as defined in the hold reason reference | `05_REFERENCE_WORKFLOW/FIRST_REAL_PAGE_RUN_HOLD_REASON_REFERENCE_V1_0.md` |
| Confirm all run intake fields | `05_REFERENCE_WORKFLOW/FIRST_REAL_PAGE_RUN_INTAKE_FIELDS_V1_0.md` |
| Verify homepage supervision rules for route `/` | `05_REFERENCE_WORKFLOW/HOMEPAGE_FIRST_REAL_RUN_SUPERVISION_RULES_V1_0.md` |
| Prepare and confirm evidence mapping for a target route | `06_MACHINE_RULES/EVIDENCE_MAP_SCHEMA_V1_0.json` |
| Route draft output to external QA | `04_OPERATOR_PROMPTS/PROMPT_02_CLAUDE_EXTERNAL_QA_ONE_ZIP_V1_0.txt` |
| Route QA findings to the controller | `04_OPERATOR_PROMPTS/PROMPT_03_CONTROLLER_DECISION_AND_REGENERATION_V1_0.txt` |
| Route to the independent analyzer review | `04_OPERATOR_PROMPTS/PROMPT_13_FIRST_REAL_PAGE_INDEPENDENT_ANALYZER_REVIEW_V1_0.txt` |
| Route to the controller post-analyzer decision | `04_OPERATOR_PROMPTS/PROMPT_14_CONTROLLER_POST_ANALYZER_DECISION_V1_0.txt` |
| Route to human approval gate | `05_REFERENCE_WORKFLOW/HOMEPAGE_DRAFT_REVIEW_AND_APPROVAL_SEQUENCE_V1_0.md` |
| Run the package validator | `tools/validate_package.py` |
| Run the health reporter | `tools/report_package_health.py` |
| Run the smoke test | `tools/run_standalone_smoke_test.py` |
| Run the run ledger reporter | `tools/report_run_ledger_status.py` |
| Append a new run ledger entry after a completed run | `tools/append_run_ledger_entry.py` (requires prior run completion and all safety checks) |

---

## What operators CANNOT do without later run approval

| Action | Blocking condition |
|--------|--------------------|
| Deploy schema to the current website | Requires validated output bundle, controller ACCEPT, and human approval |
| Claim production lock status | Requires explicit human approval reference; may not be self-claimed |
| Attach schema to Astro | Mode 2 not ready; `mode2AstroReady: false`; all carry gates must pass |
| Emit held fields in a schema draft | Requires owner approval for each held field category before emission |
| Emit blocked modules | Blocked modules may not be unblocked without a governing doctrine PR |
| Create JSON-LD | Requires draft run with confirmed evidence map and all preconditions met |
| Produce a schema output bundle | Requires draft, QA, controller review, validation, and human approval |
| Mutate Phase 0 | Phase 0 is the source of factual truth — read-only from this package |
| Mutate source truth | Source truth is read-only from this package |
| Commit real run artifacts | Requires a governed run with an authorized artifact lane |
| Self-merge a PR | Human merge only |

---

## Scope boundary

Mode 1 supervised-runnable authorizes the **intake and confirmation phase** of the operator workflow. It does not authorize the **output and implementation phase**.

The output and implementation phase requires:

1. A governed draft run (PR #27 target)
2. Evidence map confirmation
3. Non-production JSON-LD draft with approved modules only
4. External QA (Prompt 02)
5. Controller review (Prompt 03)
6. Validation (Prompt 04)
7. Independent analyzer review (Prompt 13)
8. Controller post-analyzer decision (Prompt 14)
9. Human approval
10. Implementation handoff (Prompt 12)
11. Run ledger entry (Prompt 15)

---

## Non-authorization statement

This document does not authorize schema output, JSON-LD creation, website implementation, Astro attachment, production deployment, or production lock status change.
