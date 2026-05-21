# Final Standalone Operating Manual Index V1.0

**Status:** `BOOTSTRAP_INITIALIZED_NO_SCHEMA_OUTPUT`

> This manual index defines the future operator reading order. The full workflow is not yet runnable. Operators must not generate or implement schema until later PRs add prompts, contracts, validators, and the final runnable handoff.

---

## Operator reading order

### Step 1 — Read the root README

File: `README_COMPLETE_OPERATOR_PACKAGE.md`

Understand:
- What this package is and is not
- Source truth hierarchy
- Current operating posture
- Mode 1 vs Mode 2
- Hard blocked modules
- Non-authorization statement

### Step 2 — Read CURRENT_ACTIVE_FILES

File: `00_START_HERE/CURRENT_ACTIVE_FILES.md`

Understand:
- What files exist now
- What is blocked
- What later PRs will add

### Step 3 — Read TEAM_QUICKSTART

File: `00_START_HERE/TEAM_QUICKSTART_STANDALONE_URL_REVIEW.md`

Understand:
- Plain-language operating context
- Why this package exists
- What operators can and cannot do right now

### Step 4 — Read OPERATOR_CHECKLIST

File: `00_START_HERE/OPERATOR_CHECKLIST_STANDALONE_RUN.md`

Understand:
- Pre-run checks
- Current disabled status
- What must be in place before running

### Step 5 — Wait for later PRs before running actual schema workflow

The schema workflow is **not runnable after PR #1**.

Operators must wait for:
- PR #2: Governing doctrine
- PR #3: Truth-pack reference
- PR #4: Operator prompts and machine rules
- PR #5: Validators, smoke tests, and runnable handoff

Do not generate schema. Do not create JSON-LD. Do not implement on the website.

---

## Mode 1 — Current website goal

Produce validated schema for pages on the current risefcsoccer.com website.

- First-page target: homepage, route `/`, with `HOMEPAGE_SCHEMA_PROFILE`
- Allowed first-page modules (future only): Organization, WebSite, WebPage, BreadcrumbList
- Schema is derived from approved Phase 0 content and confirmed page evidence
- Output must be validated before any implementation handoff

**Not runnable yet. Waiting for PR #5 runnable handoff.**

---

## Mode 2 — Future Astro goal

Carry validated schema into the Astro implementation after carry gates are defined.

- Blocked until Astro carry gates exist
- No Astro files are modified by this package at bootstrap
- A future PR will define the carry gates and attachment protocol

**Not yet scoped. Waiting for Astro route and runtime evidence.**

---

## Stop conditions

Operators must stop immediately and not proceed if any of the following are true:

| Condition | Action |
|-----------|--------|
| Missing Phase 0 source reference | STOP — do not proceed without Phase 0 anchor |
| Missing schema truth view or scoped derivation | STOP — derive schema only from approved truth view |
| Missing evidence map | STOP — do not create schema profiles without evidence |
| Missing schema profile | STOP — do not generate output without an approved profile |
| Attempted `Review` schema | STOP — blocked module |
| Attempted `AggregateRating` schema | STOP — blocked module |
| Attempted `FAQPage` schema | STOP — blocked module |
| Attempted `Offer` schema | STOP — blocked module |
| Attempted `Event` schema | STOP — blocked module |
| Attempted `Place` schema | STOP — blocked module |
| Attempted `GeoCoordinates` schema | STOP — blocked module |
| Attempted bilingual schema | STOP — blocked module |
| Attempted testimonial-derived schema | STOP — blocked module |
| Attempted production lock without human approval | STOP — production lock requires explicit human authorization |
| Attempted real artifact commit before governed run | STOP — no real run artifacts until runnable handoff exists |
| Attempted Astro attachment before carry gates exist | STOP — Mode 2 not yet authorized |
| Attempted Phase 0 mutation | STOP — Phase 0 is read-only from this package |
| Attempted source truth mutation | STOP — this package is downstream of source truth |
