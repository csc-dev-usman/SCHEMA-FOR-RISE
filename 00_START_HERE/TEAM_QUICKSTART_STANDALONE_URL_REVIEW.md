# Team Quickstart — Rise FC Standalone Schema Operator Package

**Status:** `OUTPUT_BUNDLE_VALIDATOR_ADDED_NO_SCHEMA_OUTPUT`

---

## Plain-language overview

This package is the governed workspace for Rise FC schema work. It provides a controlled environment where the team can produce, validate, and hand off schema markup for the Rise FC website — without guessing, inventing content, or bypassing review.

It is modeled after the CSC standalone schema operator pattern. The medical doctrine from CSC does **not** apply here. Rise FC has its own doctrine, which will be added in PR #2.

---

## Why this package exists

The Rise FC website (risefcsoccer.com) needs validated, accurate schema markup for search optimization. Rather than generating schema ad hoc, this package establishes a governed workflow:

1. Factual truth comes from Rise Phase 0.
2. Schema is derived from that truth — not invented.
3. Each output is validated before it touches the website.
4. Human approval is required at every gate.

---

## What you can do right now (after PR #11)

- Use `00_START_HERE/RISE_OPERATOR_NAVIGATION_DECISION_TREE_V1_0.md` to find the right document for your task.
- Use `00_START_HERE/RISE_SCHEMA_OPERATOR_PREFLIGHT_CHECKLIST_V1_0.md` to check all gates before any schema work.
- Use `00_START_HERE/RISE_MODE_STATUS_AND_NEXT_STEP_GUIDE_V1_0.md` to understand the current status of Mode 1 and Mode 2.
- Read the package README and start files.
- Read the governing doctrine in `02_GOVERNING_DOCTRINE/`.
- Read the homepage scoped truth-pack reference in `03_TRUTH_PACK/`.
- Read the homepage schema profile and reference lists in `07_REFERENCE_LISTS/`.
- Read the master flow documents in `01_MASTER_FLOW/` to understand the full operating sequence.
- Read the full operator prompt set in `04_OPERATOR_PROMPTS/` to understand what each governed step will do.
- Read the output bundle contract schemas in `06_MACHINE_RULES/` to understand the required shape of run artifacts.
- Read the lint rules in `06_MACHINE_RULES/RISE_SCHEMA_LINT_RULES_V1_0.json` — all 10 JSON-LD safety rules apply to every schema draft.
- Read the reference workflow documents in `05_REFERENCE_WORKFLOW/` to understand the draft contract, all preconditions, planned output files, and the 10-step review sequence.
- Read `tools/README_OUTPUT_BUNDLE_VALIDATOR_V1_0.md` to understand the output bundle validator and how it enforces governed rules.
- Run `python tools/validate_output_bundle.py --help` to see the validator usage.
- Understand which modules are allowed, which are blocked, and which fields are held.
- Review the owner approval worksheet to understand which fields need human owner decisions.
- Review `05_REFERENCE_WORKFLOW/HOMEPAGE_DRAFT_PRECONDITIONS_AND_HOLD_MATRIX_V1_0.md` to understand every gate that must pass before a draft run begins.

---

## What you cannot do right now

> **The source-truth boundary, doctrine, homepage scoped truth-pack reference, homepage schema profile, master flow, operator navigation documents, full operator prompt set, output bundle contract schemas, homepage draft contract, and output bundle validator now exist. The package is still not runnable for schema production. Operators must wait for evidence maps and the final runnable handoff before generating or implementing any schema.**

Specifically, after PR #11 you must not:

- Generate any JSON-LD
- Execute any operator prompt (prompts are templates only)
- Create any schema output
- Create any production schema bundles
- Attach schema to the current website
- Attach schema to Astro
- Run any schema operator workflow
- Commit real run artifacts
- Create evidence maps or schema profiles outside the governed workflow
- Treat the homepage scoped truth view JSON as schema output or JSON-LD — it is read-only reference material only

---

## When can you run the schema workflow?

After all required PRs are merged and the final runnable handoff is in place, Mode 1 will be fully operational.

The sequence:
- PR #2 adds governing doctrine ✓ Done
- PR #3 adds Phase 0 truth source map and homepage scoped truth view ✓ Done
- PR #4 adds homepage schema profile and blocked module policy ✓ Done
- PR #5 adds standalone schema master flow ✓ Done
- PR #6 adds team quickstart and operator checklist upgrades ✓ Done
- PR #7 adds operator prompts 00 through 04 and 08 ✓ Done
- PR #8 adds final validation, analyzer, and completion prompts ✓ Done
- PR #9 adds output bundle contract schemas ✓ Done
- PR #10 adds controlled homepage non-production JSON-LD draft contract ✓ Done
- PR #11 adds output bundle validator ✓ Done
- PR #12 adds Claude QA finding schema and controller QA review contract

Until all required PRs are merged and the final runnable handoff exists, do not execute any operator prompt or generate schema.

---

## First-page target (for reference — not runnable yet)

When Mode 1 is operational, the first schema target will be:

- **Page:** Homepage
- **Route:** `/`
- **Profile:** `HOMEPAGE_SCHEMA_PROFILE`
- **Allowed modules:** Organization, WebSite, WebPage, BreadcrumbList

No other modules are authorized for the first-page lane. See the README for the full blocked list.

---

## Key rule to remember

Rise Phase 0 is the source of factual truth. This package is downstream of Phase 0. Operators never invent content — they derive schema from approved Phase 0 content and confirmed page evidence.

If Phase 0 does not confirm a field, that field does not go into schema.

---

## Where to find help

1. Read `README_COMPLETE_OPERATOR_PACKAGE.md` first.
2. Check `00_START_HERE/FINAL_STANDALONE_OPERATING_MANUAL_INDEX_V1_0.md` for the full reading order.
3. Check `00_START_HERE/OPERATOR_CHECKLIST_STANDALONE_RUN.md` before attempting any run.
4. Raise questions with the package owner before taking any action not covered by the governing doctrine.
