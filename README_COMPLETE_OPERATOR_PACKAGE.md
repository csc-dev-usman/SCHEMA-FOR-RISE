# Rise FC Complete Schema Operator Package V1.0.0

**Status:** `MASTER_FLOW_ADDED_NO_SCHEMA_OUTPUT`

---

## Purpose

This package provides a governed operator workflow for Rise FC schema work. It is modeled after the CSC standalone schema operator pattern and exists to support two modes of operation:

- **Mode 1 (current):** Short-term schema optimization for the current risefcsoccer.com website.
- **Mode 2 (future):** Astro schema carry and attachment after Astro route and runtime evidence is ready.

Schema produced by this package is a **derived read model** from approved Rise Phase 0 content and approved page evidence. It is not an invention, a guess, or an independent source of truth.

---

## What this package is

- A governed operator package for Rise FC schema work.
- A controlled workflow environment where schema is derived from Rise Phase 0 and approved Rise content.
- A staging area for schema decisions, profiles, and validated output bundles.
- A single place for team members to understand the schema operating rules for Rise FC.

---

## What this package is not

- It is **not** the public website.
- It is **not** the Astro implementation.
- It is **not** a schema generator by itself.
- It does **not** approve production deployment.
- It does **not** mutate Rise Phase 0 or any source truth.
- It does **not** contain live schema or JSON-LD output at bootstrap.

---

## Source truth hierarchy

1. Rise Phase 0 factual truth
2. Rise generated Phase 0 schema truth view / scoped derivations
3. Rise evidence maps and schema profile decisions
4. Rise schema operator package (this package)
5. Validated schema output bundles
6. Current website or Astro implementation handoff

Rise Phase 0 remains the source of factual truth. This package is downstream of Phase 0, not above it. Visual Phase 0 and HTML/Astro runtime can carry or render approved output, but they do not author schema.

---

## Current operating posture

PR #5 adds the standalone schema master flow.

- The governing doctrine is in `02_GOVERNING_DOCTRINE/`.
- The homepage scoped truth-pack is in `03_TRUTH_PACK/`.
- The homepage schema profile, blocked module policy, held field policy, and decision matrix are in `07_REFERENCE_LISTS/`.
- The standalone master flow, Mode 1 flow, Mode 2 flow, page run sequence, and master stop conditions are now in `01_MASTER_FLOW/`.
- The active homepage schema profile is `HOMEPAGE_SCHEMA_PROFILE` for route `/`.
- No JSON-LD has been created.
- No schema output has been created.
- No production schema bundles have been created.
- No schema has been attached to any page.
- No Astro files have been modified.
- No Phase 0 or source truth files have been mutated.
- Mode 1 is documented but not runnable yet.
- Mode 2 is documented but not ready.

Status is `MASTER_FLOW_ADDED_NO_SCHEMA_OUTPUT`. The package will remain non-runnable until later PRs add operator prompts, evidence maps, output bundle schemas, the draft contract, validators, and the final runnable handoff.

---

## Mode 1: Current website standalone schema optimization

**Goal:** Identify and produce validated schema for pages on the current risefcsoccer.com website.

- Schema is derived from approved Phase 0 content and confirmed page evidence.
- Output is validated before any implementation handoff.
- No guesswork. No invented fields.
- Operators must not implement or attach schema without a validated output bundle and human approval.

---

## Mode 2: Future Astro schema carry and attachment

**Goal:** After Astro route and runtime evidence is ready, carry validated schema into the Astro implementation.

- This mode is **blocked** until Astro carry gates exist.
- No Astro files are created or modified in this package at bootstrap.
- A future PR will define the carry gates and attachment protocol.

---

## First-page target

The first schema lane target is the **homepage**, route `/`, with `HOMEPAGE_SCHEMA_PROFILE`.

Allowed first-page schema modules (future only, not yet in this PR):

- `Organization`
- `WebSite`
- `WebPage`
- `BreadcrumbList`

---

## Hard blocked modules

The following schema modules are blocked for the first-page lane and may not be added without explicit authorization in a future doctrine PR:

- `FAQPage`
- `Offer`
- `Event`
- `Review`
- `AggregateRating`
- `Place`
- `GeoCoordinates`
- Testimonial-derived schema
- Bilingual schema
- Advanced modules

Blocked means: no prompt may reference them, no schema profile may include them, no output bundle may contain them, until a governing doctrine PR explicitly authorizes each one.

---

## Current non-authorization statement

No JSON-LD has been created. No schema output has been created.

No content in this package (through PR #2) authorizes any schema to be deployed to the current website or to any Astro implementation. No content through PR #2 approves `PRODUCTION_LOCKED` status. Human merge is required. No self-merge.

---

## First files to read

1. `README_COMPLETE_OPERATOR_PACKAGE.md` (this file)
2. `00_START_HERE/CURRENT_ACTIVE_FILES.md`
3. `00_START_HERE/FINAL_STANDALONE_OPERATING_MANUAL_INDEX_V1_0.md`
4. `00_START_HERE/TEAM_QUICKSTART_STANDALONE_URL_REVIEW.md`
5. `00_START_HERE/OPERATOR_CHECKLIST_STANDALONE_RUN.md`
6. `00_START_HERE/FINAL_MODE_1_RUNNABLE_HANDOFF_V1_0.md`

---

## Next PRs

- **PR #2:** ~~Add Rise schema source-truth boundary and governing doctrine~~ ✓ Merged
- **PR #3:** ~~Add Phase 0 truth source map and homepage scoped truth view~~ ✓ Merged
- **PR #4:** ~~Add Rise homepage schema profile and blocked module policy~~ ✓ Merged
- **PR #5:** Add Rise standalone schema master flow
  `docs: add Rise standalone schema master flow`
- **PR #6:** Add team quickstart and operator checklist upgrades
- **PR #7:** Add operator prompts 00 through 04 and 08
- **PR #8:** Add final validation, analyzer, and completion prompts
- **PR #9:** Add output bundle contract schemas
- **PR #10:** Add controlled homepage non-production JSON-LD draft contract
