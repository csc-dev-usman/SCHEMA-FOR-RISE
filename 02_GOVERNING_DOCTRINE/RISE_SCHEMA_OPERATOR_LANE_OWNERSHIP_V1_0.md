# Rise Schema Operator Lane Ownership V1.0

**Status:** `DOCTRINE_BOUNDARY_ADDED_NO_SCHEMA_OUTPUT`

---

## Purpose

This document defines which lane owns which actions in the Rise FC schema workflow. It specifies cross-lane prohibitions and required handoffs to prevent lane violations that could corrupt the source-truth hierarchy.

---

## Writer lane

**Owns:**
- Creating approved page content for the Rise FC website
- Producing readiness metadata that signals which pages are ready for schema derivation
- Confirming factual claims that trace back to Phase 0

**Does not own:**
- Authoring final schema JSON-LD
- Deciding schema module selection or field values
- Overriding Phase 0 factual truth
- Approving schema for production

**Handoff to:** Analyzer/validator lane — submit approved content and readiness metadata.

---

## Analyzer / validator lane

**Owns:**
- Checking page evidence readiness
- Verifying that proposed schema output matches the approved evidence map and Phase 0 truth
- Confirming output quality (valid JSON-LD, correct module structure, no blocked modules, no invented fields)
- Flagging holds and stop conditions

**Does not own:**
- Mutating source truth
- Generating schema draft output
- Approving production deployment

**Handoff to:** SEO/schema operator lane — submit confirmation that evidence and readiness gates pass before schema draft work begins.

---

## SEO / schema operator lane

**Owns:**
- Schema draft generation, operating strictly within:
  - Confirmed Phase 0 truth
  - Approved schema truth view
  - Approved page evidence map
  - Approved schema profile
- Running the validator against the draft output
- Producing the validated output bundle

**Does not own:**
- Inventing field values
- Generating schema without confirmed Phase 0 anchor
- Generating schema without an approved evidence map
- Generating schema without an approved schema profile
- Bypassing the validator
- Approving production deployment

**Hard stops for this lane:**
- Missing Phase 0 source reference → STOP
- Missing schema truth view → STOP
- Missing page evidence map → STOP
- Missing schema profile → STOP
- Phase 0 / page evidence conflict → STOP, escalate upstream

**Handoff to:** Human owner/reviewer lane — submit validated output bundle for approval.

---

## HTML / runtime lane

**Owns:**
- Carrying approved schema references in the current website HTML after human approval
- Rendering schema markup provided by a validated output bundle

**Does not own:**
- Authoring or modifying schema content
- Adding fields, modules, or values not in the validated bundle
- Bypassing the validated output bundle
- Approving implementation without human sign-off

**Hard stops for this lane:**
- No validated output bundle exists → STOP
- Human approval not granted → STOP

---

## Astro lane

**Owns:**
- Attaching approved schema to the correct Astro route after carry gates pass and human approval is granted

**Does not own:**
- Inventing schema content
- Repairing or normalizing schema fields
- Overriding schema values
- Attaching schema before carry gates are defined
- Attaching schema before a validated output bundle exists
- Attaching schema without human approval

**Hard stops for this lane:**
- Astro carry gates not yet defined → STOP
- No validated output bundle → STOP
- Human approval not granted → STOP

---

## Human owner / reviewer lane

**Owns:**
- Approving validated schema output bundles for implementation
- Approving production lock (`PRODUCTION_LOCKED` status)
- Approving carry gate passage for Astro attachment
- Approving governing doctrine changes (PR merge)
- Approving held facts:
  - Contact fields (phone, email)
  - Logo URLs
  - Social profile URLs (sameAs)
  - Coordinate data
  - Reviews and ratings
  - Prices and offer details
  - Any other field category marked as requiring human hold

**Does not own:**
- Self-merge of any PR
- Bypassing the validator

---

## Disallowed cross-lane actions

| Action | Lane violation | Why |
|--------|---------------|-----|
| Writer authors JSON-LD directly | Writer → SEO operator lane | Schema authoring belongs to the SEO operator lane with evidence gates |
| SEO operator invents a field value | SEO operator → Phase 0 | Values must come from Phase 0 and approved evidence |
| HTML/runtime modifies schema content | HTML lane → SEO operator lane | HTML may only carry approved output |
| Astro attaches schema without carry gates | Astro lane jump | Carry gates must be defined and passed first |
| Validator approves production lock | Validator → Human owner lane | Production lock requires human authorization |
| Any lane modifies Phase 0 | Any lane → Phase 0 | Phase 0 is read-only from all lanes below it |

---

## Required handoffs

| From lane | To lane | Handoff artifact |
|-----------|---------|-----------------|
| Writer | Analyzer/validator | Approved content + readiness metadata |
| Analyzer/validator | SEO operator | Evidence gate confirmation + approved schema profile |
| SEO operator | Human owner/reviewer | Validated output bundle |
| Human owner/reviewer | HTML/runtime or Astro | Approval decision + validated output bundle |
