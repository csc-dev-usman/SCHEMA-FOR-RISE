# Team Quickstart — Rise FC Standalone Schema Operator Package

**Status:** `BOOTSTRAP_INITIALIZED_NO_SCHEMA_OUTPUT`

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

## What you can do right now (after PR #1)

- Read the package README and start files.
- Understand the operating structure and source truth hierarchy.
- Review the blocked module list.
- Understand the two operating modes (current website vs. Astro).

---

## What you cannot do right now

> **The package is initialized but not yet runnable for schema production. Operators must not generate or implement schema until later PRs add prompts, contracts, validators, and the final runnable handoff.**

Specifically, after PR #1 you must not:

- Generate any JSON-LD
- Create any schema output
- Create any production schema bundles
- Attach schema to the current website
- Attach schema to Astro
- Run any schema operator workflow
- Commit real run artifacts

---

## When can you run the schema workflow?

After PR #5 merges the final runnable handoff, Mode 1 will be fully operational.

The sequence:
- PR #2 adds governing doctrine
- PR #3 adds truth-pack reference
- PR #4 adds operator prompts and machine rules
- PR #5 adds validators, smoke tests, and the runnable handoff

Until then, this package is documentation and structure only.

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
