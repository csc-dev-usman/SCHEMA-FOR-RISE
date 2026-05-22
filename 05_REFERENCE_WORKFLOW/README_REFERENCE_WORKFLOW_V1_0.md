# Reference Workflow — Rise FC Standalone Schema Package

**Status:** `HOMEPAGE_NON_PRODUCTION_DRAFT_CONTRACT_ADDED_NO_SCHEMA_OUTPUT`

> This folder contains reference workflow documents. These are documentation contracts only — they define the rules, preconditions, output file plans, and review sequences for future governed schema runs. No actual schema has been generated. No JSON-LD has been created. No draft exists yet.

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
