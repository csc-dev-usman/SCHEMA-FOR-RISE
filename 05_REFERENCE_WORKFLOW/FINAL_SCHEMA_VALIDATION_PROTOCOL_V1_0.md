# Final Schema Validation Protocol V1.0

**Status:** `FINAL_VALIDATION_PROTOCOL_ADDED_NO_SCHEMA_OUTPUT`

> This document defines the ordered validation protocol that every future governed Rise FC schema output bundle must pass before implementation handoff is authorized. This protocol is a documentation contract only — no validators have been run, no schema has been generated, and no results exist. Validation alone does not authorize production. Human approval is required at every gate.

---

## Purpose

This protocol defines the required validation sequence for all Rise FC schema output bundles. It is the authoritative reference for the order and requirements of each validation step. Every step must be completed in sequence before moving to the next. Validation does not replace human approval — it is a prerequisite for it.

---

## Core rule

**Passing this full validation protocol does not authorize production deployment.**

Validation is necessary but not sufficient. Human approval at Step 8 is required before any implementation handoff can occur. The controller cannot self-approve production. Claude QA cannot authorize implementation.

---

## Validation order

### Step 1 — Package and output bundle validation

**Tool:** `tools/validate_output_bundle.py`
**Rule set:** `06_MACHINE_RULES/OUTPUT_BUNDLE_VALIDATOR_RULES_V1_0.md`
**Expected files contract:** `06_MACHINE_RULES/OUTPUT_BUNDLE_VALIDATOR_EXPECTED_FILES_V1_0.json`

Run:
```
python tools/validate_output_bundle.py <bundle_dir>
```

**Required result:** `PASS` (exit code 0)

**Checks performed:**
- All required files are present (`output_bundle_manifest.json`, `run_metadata.json`, `evidence_map.json`, `controller_decision.json`, `validator_results.json`)
- All required doc files are present (`withheld_schema_report.md`, `deferred_truth_report.md`)
- All JSON files parse without error
- Truth fingerprint matches expected homepage fingerprint when profile is `HOMEPAGE_SCHEMA_PROFILE`
- No blocked modules in emitted schema
- No held fields present without approval metadata
- No production lock claimed without required approval fields
- Safety booleans are correctly set

**Stop condition:** If the validator returns `FAIL` (exit code 1), do not proceed to Step 2. Patch the output bundle and rerun.

---

### Step 2 — JSON parse validation

All JSON files in the output bundle must be independently validated as well-formed JSON.

**Check each of the following:**
- `output_bundle_manifest.json` — must parse
- `run_metadata.json` — must parse
- `evidence_map.json` — must parse
- `controller_decision.json` — must parse
- `validator_results.json` — must parse
- `emitted_schema.jsonld` — must parse (when present)

**Command pattern:**
```
python -m json.tool <file>
```

**Required result:** All files parse without error.

**Stop condition:** If any JSON file fails to parse, do not proceed to Step 3. Fix the malformed JSON and rerun Step 1 before continuing.

---

### Step 3 — Schema lint rules

**Lint rules file:** `06_MACHINE_RULES/RISE_SCHEMA_LINT_RULES_V1_0.json`

All 10 JSON-LD safety rules (JLSR_001–JLSR_010) must be satisfied by the emitted schema.

**Manual checks required:**

| Rule | Check |
|------|-------|
| JLSR_001 | No blocked modules present in `@type` values |
| JLSR_002 | No held fields emitted without approval metadata |
| JLSR_003 | No invented content — all fields trace to Phase 0 or confirmed page evidence |
| JLSR_004 | `@context` must be `https://schema.org` |
| JLSR_005 | `truthFingerprint` must match the homepage fingerprint for homepage profile |
| JLSR_006 | No `PRODUCTION_LOCKED` status without human approval record |
| JLSR_007 | No Astro-specific fields unless Astro carry gates are authorized |
| JLSR_008 | No bilingual schema fields |
| JLSR_009 | No testimonial-derived claims |
| JLSR_010 | No `FAQPage`, `Review`, `AggregateRating`, `Offer`, `Event`, `Place`, `GeoCoordinates` |

**Required result:** All 10 rules pass. No violations.

**Stop condition:** Any lint rule violation is a BLOCKER. Do not proceed to Step 4 until all lint violations are resolved.

---

### Step 4 — Schema.org Validator

**Tool:** Schema.org Structured Data Validator (https://validator.schema.org)
**Runbook:** `05_REFERENCE_WORKFLOW/SCHEMA_VALIDATOR_RUNBOOK_V1_0.md`

Submit the emitted schema (from `emitted_schema.jsonld`) to the Schema.org Validator.

**Required result:** No critical errors. Warnings are reviewed and documented in `validator_results.json`.

**Evidence to capture:**
- Screenshot or exported result summary
- Any errors with their field paths
- Any warnings with disposition (resolved / deferred / accepted)

**Stop condition:** Critical errors (invalid `@type`, missing required properties, invalid field values) are blockers. Do not proceed to Step 5 until all critical errors are resolved.

---

### Step 5 — Google Rich Results Test (where applicable)

**Tool:** Google Rich Results Test (https://search.google.com/test/rich-results)
**Runbook:** `05_REFERENCE_WORKFLOW/GOOGLE_RICH_RESULTS_REVIEW_RUNBOOK_V1_0.md`

Test the emitted schema for rich results eligibility where applicable.

**Important:**
- Rich results eligibility is **not guaranteed**
- Not all schema types produce rich results
- A result of "not eligible" does not block validation — it is informational only
- This test is applicable primarily for `WebSite` (sitelinks searchbox) and `BreadcrumbList`

**Evidence to capture:**
- Screenshot or result summary
- Eligibility result per module
- Any warnings

**Stop condition:** None. This step is informational. Proceed to Step 6 regardless of eligibility result. Document the result in `validator_results.json`.

---

### Step 6 — Screaming Frog structured data extraction (where available)

**Checklist:** `05_REFERENCE_WORKFLOW/SCREAMING_FROG_STRUCTURED_DATA_EXPORT_CHECKLIST_V1_0.md`

If Screaming Frog is available and the target page is crawlable, extract and review structured data from the live page (before or after implementation, as applicable).

**Important:**
- This step is **optional and where available** — it does not block Step 7 if Screaming Frog is unavailable
- If unavailable, document as `N/A` in `validator_results.json`
- This step is most useful post-implementation to verify what the page is actually emitting

**Evidence to capture (where available):**
- Screaming Frog structured data export CSV or screenshot
- Any unexpected schema types found on the page
- Confirmation that blocked modules are not present in the live page

**Stop condition:** If Screaming Frog is unavailable or the page is not yet crawlable, mark as `N/A` and proceed to Step 7. If available and critical issues are found (blocked modules in live page, invalid types), those are blockers.

---

### Step 7 — Controller review

**Workflow:** `05_REFERENCE_WORKFLOW/CLAUDE_QA_AND_CONTROLLER_REVIEW_WORKFLOW_V1_0.md`
**Enum reference:** `05_REFERENCE_WORKFLOW/CONTROLLER_DECISION_ENUM_REFERENCE_V1_0.md`
**Schema:** `06_MACHINE_RULES/CONTROLLER_REVIEW_PACKET_SCHEMA_V1_0.json`

The controller reviews all Claude QA findings from Step 6 (Prompt 02 one-zip review) and Steps 9–10 (Prompt 13 analyzer review, Prompt 14 controller post-analyzer decision). The controller produces a controller review packet conforming to `CONTROLLER_REVIEW_PACKET_SCHEMA_V1_0.json`.

**Required result:** Final recommendation of `PROCEED_TO_HUMAN_APPROVAL` with:
- `unresolvedBlockers: 0`
- `patchRequired: false`
- `humanReviewRequired: false` (no outstanding human-review-required findings)

**Stop condition:** If `finalRecommendation` is `PATCH_REQUIRED` or `REJECT_RUN`, do not proceed to Step 8. If `HUMAN_REVIEW_REQUIRED`, escalate to the package owner before proceeding.

---

### Step 8 — Human approval

**Required before:** Any implementation handoff, production lock, or Astro attachment.

A human (package owner or authorized approver) must review:
- The full output bundle
- All validation results (Steps 1–7)
- The controller review packet
- The Claude QA finding set

The human approver must explicitly authorize the implementation handoff.

**No schema may be attached to the current website or to Astro without this explicit human approval.**

**Required result:** Human approval record with:
- Approver identity
- Approval date
- Explicit `IMPLEMENTATION_HANDOFF_AUTHORIZED: true`

**Stop condition:** If human approval is not obtained, do not proceed to Step 9. Mode 1 does not self-approve. No automated process replaces this gate.

---

### Step 9 — Implementation handoff

**Prompt:** `04_OPERATOR_PROMPTS/PROMPT_12_FINAL_VALIDATION_AND_IMPLEMENTATION_SCHEMA_V1_0.txt`
**Requirements:** `05_REFERENCE_WORKFLOW/VALIDATION_EVIDENCE_HANDOFF_REQUIREMENTS_V1_0.md`

After human approval, the implementation handoff packet is produced. This packet is the authorized deliverable for the current website or Astro implementation.

**Required contents:**
- Final validated `emitted_schema.jsonld`
- `implementation_handoff.md` with all required evidence metadata
- Controller review packet reference
- Human approval record reference
- Validation result references (Steps 1–7)

**Constraints:**
- The implementation handoff does not approve production lock by itself
- Astro attachment requires Astro carry gates (Mode 2 — not yet authorized)
- Human approval from Step 8 must be documented in the handoff packet

---

## Non-authorization statement

Completing this validation protocol:
- Does **not** authorize production deployment
- Does **not** authorize Astro attachment
- Does **not** authorize production lock
- Does **not** mutate Rise Phase 0
- Does **not** replace human approval at Step 8

All 9 steps must be completed. Human approval at Step 8 is required. No step may be skipped.

---

## Related documents

| Document | Purpose |
|----------|---------|
| `06_MACHINE_RULES/OUTPUT_BUNDLE_VALIDATOR_RULES_V1_0.md` | Validator rules (RULE_VAL_001–RULE_VAL_007) |
| `06_MACHINE_RULES/RISE_SCHEMA_LINT_RULES_V1_0.json` | Lint rules (JLSR_001–JLSR_010) |
| `05_REFERENCE_WORKFLOW/SCHEMA_VALIDATOR_RUNBOOK_V1_0.md` | Schema.org Validator usage runbook |
| `05_REFERENCE_WORKFLOW/GOOGLE_RICH_RESULTS_REVIEW_RUNBOOK_V1_0.md` | Google Rich Results Test runbook |
| `05_REFERENCE_WORKFLOW/SCREAMING_FROG_STRUCTURED_DATA_EXPORT_CHECKLIST_V1_0.md` | Screaming Frog checklist (optional) |
| `05_REFERENCE_WORKFLOW/VALIDATION_EVIDENCE_HANDOFF_REQUIREMENTS_V1_0.md` | Required evidence metadata for implementation handoff |
| `05_REFERENCE_WORKFLOW/CLAUDE_QA_AND_CONTROLLER_REVIEW_WORKFLOW_V1_0.md` | Claude QA and controller review workflow |
| `05_REFERENCE_WORKFLOW/CONTROLLER_DECISION_ENUM_REFERENCE_V1_0.md` | All valid controller decision values |
| `tools/validate_output_bundle.py` | Output bundle validator script |
