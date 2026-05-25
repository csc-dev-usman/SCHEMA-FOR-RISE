# Astro Schema Carry Non-Authorization Rules V1.0

**Status:** `ASTRO_SCHEMA_CARRY_GATE_REFERENCE_ADDED_NO_SCHEMA_OUTPUT`

---

## Purpose

This document states the non-authorization rules governing Astro schema carry and attachment. These rules are active from PR #23 and remain in force until a future governing doctrine PR explicitly overrides each one.

---

## Current status

**Mode 2 (Astro carry) is not ready.**

As of PR #23:
- No Astro carry gates have been passed
- No schema output bundle exists
- No carry packet exists
- No Astro attachment has been authorized
- `mode2AstroReady: false` in `package_manifest.json`
- `astroAttachmentAuthorized: false` in `package_manifest.json`
- `astroAttachmentCreated: false` in `package_manifest.json`

---

## Non-authorization rules

### Rule ACNA-001 — No Astro code changes

No Astro source files, Astro components, Astro layouts, Astro pages, or Astro configuration files may be modified as part of schema carry work until all carry gates in `ASTRO_SCHEMA_CARRY_GATE_REFERENCE_V1_0.md` have passed and human approval for Astro attachment has been granted.

**Status: IN FORCE**

---

### Rule ACNA-002 — No runtime code changes

No runtime source files, HTML templates, server-side rendering code, or frontend JavaScript bundles may be modified to carry schema until all carry gates have passed and human approval has been granted.

**Status: IN FORCE**

---

### Rule ACNA-003 — No schema attachment

No schema output — including JSON-LD blocks, inline schema markup, or structured data injections — may be attached to any Astro route, HTML page, WordPress page, or runtime template without:

1. A completed, validated schema output bundle
2. Controller approval with `finalRecommendation: PROCEED_TO_HUMAN_APPROVAL`
3. Human approval with `humanApprovalRef` recorded in the run ledger
4. All carry gates in `ASTRO_SCHEMA_CARRY_GATE_REFERENCE_V1_0.md` confirmed

**Status: IN FORCE**

---

### Rule ACNA-004 — No production deployment

No schema produced by this package may be deployed to any production environment — including the current risefcsoccer.com website, any Astro production build, or any CDN — without explicit human approval and a `humanApprovalRef` in the run ledger.

Production deployment is not the same as implementation handoff. Operator may produce an implementation handoff packet, but deployment requires separate human authorization.

**Status: IN FORCE**

---

### Rule ACNA-005 — No Mode 2 readiness

Mode 2 (`MODE_2_FUTURE_ASTRO_SCHEMA_CARRY`) may not be declared ready, operational, or active until:

1. A real Astro route exists for the target page
2. The Runtime Appendix carry field reference is complete and loaded
3. The Astro attachment packet template has been filled with real, confirmed values
4. All carry gates in `ASTRO_SCHEMA_CARRY_GATE_REFERENCE_V1_0.md` have passed
5. `mode2AstroReady: true` is set by a governing PR — not self-set
6. Human approval for Mode 2 activation has been granted

**Status: IN FORCE**

---

### Rule ACNA-006 — Astro does not author schema

Astro may only carry and render approved schema output. Astro may not:

- Invent schema field values
- Repair or normalize schema fields
- Override approved schema values
- Add schema properties not present in the approved output bundle
- Remove schema properties from the approved output bundle

If a schema field is missing or incorrect, the correction must originate in the schema operator lane — not in Astro.

**Status: IN FORCE**

---

### Rule ACNA-007 — No self-authorization of carry

No operator, no automated validator, and no Claude session may self-authorize schema carry, Astro attachment, or production deployment. Human authorization is required at every carry gate that specifies human approval.

**Status: IN FORCE**

---

## Non-authorization history

| PR | Astro attachment authorized? | Mode 2 ready? | Schema created? |
|----|------------------------------|---------------|-----------------|
| PR #1–#22 | NO | NO | NO |
| PR #23 (this PR) | NO | NO | NO |

---

## What this document does not do

- It does not create Astro implementation
- It does not attach schema to Astro
- It does not create JSON-LD
- It does not create schema output
- It does not mark Mode 2 as ready
- It does not mutate Rise Phase 0
- It does not authorize production lock
