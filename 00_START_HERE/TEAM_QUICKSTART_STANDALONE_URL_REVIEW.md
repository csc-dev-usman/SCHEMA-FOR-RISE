# Team Quickstart — Rise FC Standalone Schema Operator Package

**Status:** `MASTER_FLOW_ADDED_NO_SCHEMA_OUTPUT`

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

## What you can do right now (after PR #5)

- Read the package README and start files.
- Read the governing doctrine in `02_GOVERNING_DOCTRINE/`.
- Read the homepage scoped truth-pack reference in `03_TRUTH_PACK/`.
- Read the homepage schema profile and reference lists in `07_REFERENCE_LISTS/`.
- Read the master flow documents in `01_MASTER_FLOW/` to understand the full operating sequence.
- Understand the page run sequence from intake through implementation or Astro handoff.
- Understand all master stop conditions and when they apply.
- Understand Mode 1 (current website) and Mode 2 (future Astro) flows and their current status.
- Understand which modules are allowed and which are blocked.
- Understand which fields are held and require owner approval.
- Review the owner approval worksheet.
- Understand the source-truth boundary, hierarchy, and lane ownership rules.

---

## What you cannot do right now

> **The source-truth boundary, doctrine, homepage scoped truth-pack reference, homepage schema profile, and master flow now exist. The package is still not runnable for schema production. Operators must wait for operator prompts, evidence maps, output bundle schemas, the draft contract, validators, and the final runnable handoff before generating or implementing any schema.**

Specifically, after PR #5 you must not:

- Generate any JSON-LD
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

After PR #6 merges the final runnable handoff, Mode 1 will be fully operational.

The sequence:
- PR #2 adds governing doctrine ✓ Done
- PR #3 adds Phase 0 truth source map and homepage scoped truth view ✓ Done
- PR #4 adds homepage schema profile and blocked module policy ✓ Done
- PR #5 adds standalone schema master flow ✓ Done
- PR #6 adds team quickstart and operator checklist upgrades
- PR #7 adds operator prompts 00 through 04 and 08
- PR #8 adds final validation, analyzer, and completion prompts
- PR #9 adds output bundle contract schemas
- PR #10 adds controlled homepage non-production JSON-LD draft contract

Until PR #6 is merged, this package is documentation, structure, doctrine, and truth-pack reference only.

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
