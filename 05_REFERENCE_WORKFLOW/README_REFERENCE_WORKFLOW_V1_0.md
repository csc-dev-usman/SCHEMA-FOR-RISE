# Reference Workflow — Rise FC Standalone Schema Package

**Status:** `INDEPENDENT_ANALYZER_CONTROLLER_FLOW_ADDED_NO_SCHEMA_OUTPUT`

> This folder contains reference workflow documents. These are documentation contracts only — they define the rules, preconditions, output file plans, review sequences, QA/controller review process, the full validation protocol, the run ledger review guide, and the first real page run handoff templates for future governed schema runs. No actual schema has been generated. No JSON-LD has been created. No draft exists yet. No QA findings exist. No validators have been run. No run entries exist.

---

## Purpose

This folder defines the controlled reference workflow for the Rise FC homepage non-production JSON-LD draft. It documents what conditions must be met, what outputs will be produced, and what review steps will be followed — before any actual drafting begins.

These documents serve as a governance checkpoint: the full workflow must be understood and all preconditions confirmed before any operator begins a governed schema run.

---

## Files in this folder

| File | Purpose |
|------|---------|
| `README_REFERENCE_WORKFLOW_V1_0.md` | This file. Folder index. |
| `CONTROLLED_HOMEPAGE_NON_PRODUCTION_JSONLD_DRAFT_CONTRACT_V1_0.md` | The draft contract — rules for how the homepage draft will be produced, what it must and must not contain, and what approval is required. |
| `HOMEPAGE_DRAFT_PRECONDITIONS_AND_HOLD_MATRIX_V1_0.md` | All preconditions that must be met before drafting begins. Hold matrix for fields that require owner approval. |
| `HOMEPAGE_DRAFT_OUTPUT_FILE_LIST_V1_0.md` | Planned output file names and their expected shapes. These are planned names only — no files have been created. |
| `HOMEPAGE_DRAFT_REVIEW_AND_APPROVAL_SEQUENCE_V1_0.md` | The full 10-step review and approval sequence from readiness gate through implementation handoff. |
| `CLAUDE_QA_AND_CONTROLLER_REVIEW_WORKFLOW_V1_0.md` | Claude QA and controller review workflow — what QA is, session rules, what the controller can and cannot do, finding severity rules. Added PR #12. |
| `CONTROLLER_DECISION_ENUM_REFERENCE_V1_0.md` | Authoritative reference for all valid controller decision values — per-finding dispositions, final recommendations, and constraint table. Added PR #12. |
| `FINAL_SCHEMA_VALIDATION_PROTOCOL_V1_0.md` | Ordered 9-step validation protocol — output bundle validation, JSON parse, lint rules, Schema.org Validator, Google Rich Results Test, Screaming Frog, controller review, human approval, implementation handoff. Added PR #13. |
| `SCHEMA_VALIDATOR_RUNBOOK_V1_0.md` | How to use the Schema.org Validator for future schema bundles. Step 4 of the validation protocol. Added PR #13. |
| `GOOGLE_RICH_RESULTS_REVIEW_RUNBOOK_V1_0.md` | How to use the Google Rich Results Test. Rich results eligibility not guaranteed. Step 5 is informational only. Added PR #13. |
| `SCREAMING_FROG_STRUCTURED_DATA_EXPORT_CHECKLIST_V1_0.md` | Screaming Frog structured data extraction checklist — optional/where available. Step 6 of validation protocol. Added PR #13. |
| `VALIDATION_EVIDENCE_HANDOFF_REQUIREMENTS_V1_0.md` | Required evidence metadata shape for the implementation handoff packet. No actual evidence. Added PR #13. |
| `RUN_LEDGER_STANDALONE_SCHEMA_REVIEW_GUIDE_V1_0.md` | How to read the run ledger, field explanations, when PRODUCTION_LOCKED may and may not be claimed. Added PR #14. |
| `FIRST_REAL_PAGE_RUN_HANDOFF_TEMPLATE_V1_0.md` | Blank future-use handoff template for governed first real page runs. All fields default to placeholder, NOT_STARTED, HOLD, or NOT_AUTHORIZED. Added PR #19. |
| `FIRST_REAL_PAGE_RUN_INTAKE_FIELDS_V1_0.md` | Required intake fields and validation expectations for a governed first real page run. Added PR #19. |
| `HOMEPAGE_FIRST_REAL_RUN_SUPERVISION_RULES_V1_0.md` | Supervision rules for the first real homepage schema run — route `/`, `HOMEPAGE_SCHEMA_PROFILE`, fingerprint, allowed modules, blocked modules, held fields, stop conditions. Added PR #19. |
| `FIRST_REAL_PAGE_RUN_HOLD_REASON_REFERENCE_V1_0.md` | All hold codes for governed first real page runs — definitions, conditions, and resolution requirements. Added PR #19. |
| `INDEPENDENT_ANALYZER_AND_CONTROLLER_FLOW_V1_0.md` | Full independent analyzer and controller post-analyzer flow definition — stages, checks, dispositions, constraints. Added PR #20. |
| `FIRST_REAL_PAGE_INDEPENDENT_ANALYZER_REVIEW_TEMPLATE_V1_0.md` | Blank future-use independent analyzer review template. Added PR #20. |
| `CONTROLLER_POST_ANALYZER_DECISION_TEMPLATE_V1_0.md` | Blank future-use controller post-analyzer decision template. Added PR #20. |
| `ANALYZER_CONTROLLER_DISPOSITION_MATRIX_V1_0.md` | Disposition matrix — severity-to-disposition guidance, category constraints, final recommendation rules. Added PR #20. |

---

## Non-authorization statement

No file in this folder:
- Contains JSON-LD
- Creates a homepage draft
- Produces schema output
- Authorizes implementation on the current website
- Authorizes Astro attachment
- Authorizes production lock
- Mutates Rise Phase 0

All files in this folder are documentation-only governance contracts. The actual homepage draft will be created in a future governed run after all preconditions in `HOMEPAGE_DRAFT_PRECONDITIONS_AND_HOLD_MATRIX_V1_0.md` are confirmed.

---

## Reading order

1. This file
2. `CONTROLLED_HOMEPAGE_NON_PRODUCTION_JSONLD_DRAFT_CONTRACT_V1_0.md` — understand the contract rules
3. `HOMEPAGE_DRAFT_PRECONDITIONS_AND_HOLD_MATRIX_V1_0.md` — understand all preconditions
4. `HOMEPAGE_DRAFT_OUTPUT_FILE_LIST_V1_0.md` — understand planned outputs
5. `HOMEPAGE_DRAFT_REVIEW_AND_APPROVAL_SEQUENCE_V1_0.md` — understand the full review sequence
6. `CLAUDE_QA_AND_CONTROLLER_REVIEW_WORKFLOW_V1_0.md` — understand the Claude QA and controller review process
7. `CONTROLLER_DECISION_ENUM_REFERENCE_V1_0.md` — understand all valid controller decision values
8. `FINAL_SCHEMA_VALIDATION_PROTOCOL_V1_0.md` — understand the required 9-step validation sequence
9. `SCHEMA_VALIDATOR_RUNBOOK_V1_0.md` — Schema.org Validator usage (Step 4)
10. `GOOGLE_RICH_RESULTS_REVIEW_RUNBOOK_V1_0.md` — Google Rich Results Test usage (Step 5)
11. `SCREAMING_FROG_STRUCTURED_DATA_EXPORT_CHECKLIST_V1_0.md` — Screaming Frog extraction (Step 6, optional)
12. `VALIDATION_EVIDENCE_HANDOFF_REQUIREMENTS_V1_0.md` — required evidence metadata for implementation handoff
13. `RUN_LEDGER_STANDALONE_SCHEMA_REVIEW_GUIDE_V1_0.md` — how to read the run ledger and when PRODUCTION_LOCKED may be claimed
14. `FIRST_REAL_PAGE_RUN_HANDOFF_TEMPLATE_V1_0.md` — blank future-use handoff template (Added PR #19)
15. `FIRST_REAL_PAGE_RUN_INTAKE_FIELDS_V1_0.md` — required intake fields and validation expectations (Added PR #19)
16. `HOMEPAGE_FIRST_REAL_RUN_SUPERVISION_RULES_V1_0.md` — homepage lane supervision rules (Added PR #19)
17. `FIRST_REAL_PAGE_RUN_HOLD_REASON_REFERENCE_V1_0.md` — all hold codes and resolution requirements (Added PR #19)
18. `INDEPENDENT_ANALYZER_AND_CONTROLLER_FLOW_V1_0.md` — full analyzer and controller flow (Added PR #20)
19. `FIRST_REAL_PAGE_INDEPENDENT_ANALYZER_REVIEW_TEMPLATE_V1_0.md` — blank analyzer review template (Added PR #20)
20. `CONTROLLER_POST_ANALYZER_DECISION_TEMPLATE_V1_0.md` — blank controller decision template (Added PR #20)
21. `ANALYZER_CONTROLLER_DISPOSITION_MATRIX_V1_0.md` — disposition matrix (Added PR #20)
