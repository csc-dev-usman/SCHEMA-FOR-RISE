# Rise Schema Source-Truth Boundary V1.0

**Status:** `DOCTRINE_BOUNDARY_ADDED_NO_SCHEMA_OUTPUT`

---

## Purpose

This document defines the source-truth hierarchy for the Rise FC standalone schema operator package and specifies exactly what each layer owns, what it may not do, and when schema work must stop.

---

## Source truth hierarchy

| Level | Layer | Owns |
|-------|-------|------|
| 1 | Rise Phase 0 factual truth | All factual claims about the club, people, programs, locations, and operations |
| 2 | Rise generated Phase 0 schema truth view / scoped derivations | Machine-readable schema-relevant extractions derived strictly from Phase 0 |
| 3 | Approved page evidence maps | Confirmed per-page facts drawn from Phase 0 and observable page content |
| 4 | Schema profile decisions | Per-page schema shape: which modules, which fields, which values are authorized |
| 5 | Rise standalone schema operator package | Governed workflow for deriving, validating, and handing off schema output |
| 6 | Validated schema output bundles | Finalized JSON-LD ready for implementation review |
| 7 | Current website implementation handoff / future Astro carry and attachment | Implementation of approved validated schema into the live surface |

Each lower level is strictly downstream of all levels above it. No lower level may override, extend, or contradict a higher level.

---

## What Phase 0 owns

Rise Phase 0 is the authoritative factual truth source for all Rise FC schema work.

Phase 0 owns:
- Club name, legal name, and any trade names
- Location facts (city, region, country — not coordinates unless Phase 0 explicitly provides them)
- Program names, types, and age groups
- Staff and coaching roster facts
- Founding dates or other temporal facts
- Any other factual claims about the organization

Phase 0 does not own:
- Schema shape or module selection (those are schema profile decisions)
- Implementation format (that belongs to the output bundle and handoff layers)

---

## What generated Phase 0 schema truth views own

A generated Phase 0 schema truth view is a machine-readable extraction derived strictly from Phase 0. It is not a new source of truth. It is a scoped derivation that makes Phase 0 facts available in schema-relevant format.

A schema truth view owns:
- Confirmed field values for schema modules, sourced directly from Phase 0
- Scoped derivations for specific pages or routes

A schema truth view does not own:
- Any field values not present in Phase 0
- Authority to override Phase 0
- Authority to invent or estimate field values

---

## What page evidence maps own

An approved page evidence map documents what is confirmed, observable, and verifiable for a specific page or route.

A page evidence map owns:
- Per-page confirmation of which Phase 0 facts are relevant and applicable
- Readiness signal for which schema modules can be supported by evidence
- Any page-specific facts that are confirmed and observable (not inferred)

A page evidence map does not own:
- Facts that contradict Phase 0
- Facts that Phase 0 has not confirmed
- Authority to unlock blocked schema modules

---

## What schema profile decisions own

A schema profile decision defines the schema shape for a specific page.

A schema profile owns:
- Module selection (e.g., Organization, WebSite, WebPage, BreadcrumbList for the homepage)
- Field list for each module
- Value assignments for authorized fields
- Explicit exclusion of blocked modules

A schema profile does not own:
- Field values not traceable to Phase 0 or approved page evidence
- Authorization of blocked modules
- Production deployment approval

---

## What the standalone schema operator package owns

The standalone schema operator package owns:
- The governed workflow for schema derivation, validation, and handoff
- Doctrine, boundaries, and operating rules
- Operator prompts and machine rules (added in later PRs)
- Validators and smoke tests (added in later PRs)

The standalone schema operator package does not own:
- Factual truth about Rise FC
- Authority to override Phase 0
- Authority to invent field values
- Authority to approve production deployment by itself
- Authority to mutate Phase 0 or any source truth

---

## What validated schema output bundles own

A validated schema output bundle owns:
- The finalized JSON-LD for a specific page, confirmed by the package validator
- Readiness signal for implementation review

A validated schema output bundle does not own:
- Production deployment authorization (that requires human approval)
- Authority to override approved doctrine

---

## What current website implementation handoff owns

The current website implementation handoff owns:
- Placement and rendering of an approved validated schema bundle on the live site

The current website implementation handoff does not own:
- Authority to modify schema content
- Authority to add fields, modules, or values not in the validated bundle
- Authority to bypass human approval

---

## What future Astro carry and attachment owns

Astro carry and attachment owns:
- Attaching a validated schema bundle to the correct Astro route after carry gates pass

Astro carry and attachment does not own:
- Authority to invent, repair, normalize, or override schema content
- Authority to attach schema before carry gates are defined and passed

---

## Explicit non-authority of this package

The standalone schema operator package explicitly is not:
- Rise Phase 0
- The public website (risefcsoccer.com)
- The Astro implementation
- A live schema generator by itself
- A production deployment authority by itself

The standalone schema operator package explicitly cannot:
- Mutate Phase 0 or any source truth
- Invent field values not confirmed by Phase 0 or approved page evidence
- Approve production deployment without human authorization
- Unlock blocked schema modules without a governing doctrine PR
- Attach schema to any surface without a validated output bundle and human approval

---

## Mutation prohibitions

| Prohibited action | Reason |
|------------------|--------|
| Modifying Phase 0 files | Phase 0 is the factual truth source — this package is read-only downstream |
| Modifying source truth files | Source truth is immutable from this package |
| Inventing field values | All values must trace to Phase 0 or approved page evidence |
| Adding blocked modules | Blocked until governing doctrine explicitly authorizes them |
| Committing real run artifacts | Not authorized until runnable handoff exists |
| Self-approving production lock | Production lock requires human authorization |
| Attaching schema before validation | Validation is required before any implementation handoff |

---

## Stop conditions

Operators must stop and must not proceed with any schema work if any of the following are true:

| Condition | Stop reason |
|-----------|-------------|
| Missing Phase 0 source reference | Cannot derive schema without Phase 0 anchor |
| Missing or stale schema truth view | Cannot derive schema without confirmed truth view |
| Missing truth fingerprint | Cannot verify truth-view currency |
| Missing page evidence map | Cannot confirm per-page schema readiness |
| Missing schema profile | Cannot generate output without an approved profile |
| Phase 0 truth and page evidence conflict | Schema must hold until conflict is resolved upstream |
| Required truth is missing for a field | Field must be omitted, not estimated |
| Requested schema module is blocked | Module must be held or deferred |
| Attempted production lock without human approval | Hard stop |
| Attempted Astro attachment before carry gates exist | Hard stop |
| Attempted current website implementation before validation and human approval | Hard stop |
| Attempted Phase 0 mutation | Hard stop |
| Attempted source truth mutation | Hard stop |
