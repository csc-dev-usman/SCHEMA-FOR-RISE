# Rise Schema Governing Doctrine V1.0

**Status:** `DOCTRINE_BOUNDARY_ADDED_NO_SCHEMA_OUTPUT`

---

## Operating principle

Schema is a downstream SEO/schema operator output derived from approved page evidence and Rise Phase 0 truth. It is not source truth.

The Rise schema operator package exists to govern how schema is derived, validated, and handed off — not to invent, estimate, or override facts.

---

## Schema is a downstream read model

Schema markup for Rise FC is a derived read model. It reflects approved facts. It does not establish facts.

The derivation chain is:
```
Rise Phase 0 factual truth
  → Generated schema truth view / scoped derivation
    → Approved page evidence map
      → Schema profile decision
        → Schema operator output (this package)
          → Validated output bundle
            → Implementation handoff (current website or future Astro)
```

No step in this chain may invent content, skip a prior step, or work backward to override a higher layer.

---

## Evidence-first generation rule

No schema field value may be written unless it is confirmed by at least one of:
- Rise Phase 0 factual truth (required anchor)
- The generated Phase 0 schema truth view for the relevant page/route
- An approved page evidence map for the target page

If a field value cannot be traced to confirmed evidence, the field must be omitted. It must not be estimated, inferred from convention, or filled with placeholder values.

---

## No invention rule

The following are prohibited at all times:

- Inventing contact information (phone, email, fax)
- Inventing logo URLs or image URLs
- Inventing sameAs / social profile URLs
- Inventing coordinates or GeoCoordinates
- Inventing prices or offer details
- Inventing reviews or ratings
- Inventing event details or dates
- Inventing bilingual alternate data
- Inventing testimonial-derived claims
- Using "common knowledge" to fill schema fields not confirmed by Phase 0

If Phase 0 does not confirm a field, that field does not exist in schema.

---

## No source-truth mutation rule

This package is strictly read-only with respect to all upstream layers. Operators working in this package must not:

- Edit, overwrite, or delete Phase 0 files
- Edit, overwrite, or delete generated schema truth view files
- Edit, overwrite, or delete approved page evidence maps
- Treat schema output as a correction to Phase 0

If a Phase 0 fact appears to be incorrect or incomplete, the correction must flow through the Phase 0 update process — not through this package.

---

## Current website Mode 1 doctrine

**Goal:** Produce validated schema for pages on the current risefcsoccer.com website.

Operating rules for Mode 1:
- Schema is derived from approved Phase 0 content and confirmed page evidence.
- Output must be validated by the package validator before any implementation handoff.
- Human approval is required before any schema is attached to the current website.
- No schema may be attached to the website without a validated output bundle.
- No schema may bypass the validator.
- Mode 1 is not runnable until PR #5 adds the truth pack, prompts, validators, and final runnable handoff.

---

## Future Astro Mode 2 doctrine

**Goal:** Carry validated schema into the Astro implementation after carry gates are defined.

Operating rules for Mode 2:
- Mode 2 is blocked until Astro carry gates are defined in a future PR.
- Astro may carry approved schema only — it may not invent, repair, normalize, or override schema.
- Astro attachment requires a validated output bundle, passed carry gates, and human approval.
- No Astro files are modified by this package.

---

## First-page homepage posture

The first schema lane target is the **homepage**, route `/`, with `HOMEPAGE_SCHEMA_PROFILE`.

This is a future target. It is not runnable after PR #2.

The homepage schema work requires:
- A generated Phase 0 schema truth view scoped to the homepage
- An approved homepage evidence map
- An approved `HOMEPAGE_SCHEMA_PROFILE`
- Operator prompts (PR #4)
- Validators (PR #5)
- Final runnable handoff (PR #5)

---

## Allowed future first-page modules

The following schema modules are authorized for future consideration on the first-page homepage lane, subject to all prior gates:

- `Organization`
- `WebSite`
- `WebPage`
- `BreadcrumbList`

These modules are future-only. They are not authorized for generation in PR #2. They require truth pack files, evidence maps, prompts, validators, and the final runnable handoff before any output can be produced.

---

## Blocked first-page modules

The following schema modules are blocked for the first-page lane. They may not be added to any schema profile, operator prompt, or output bundle without a governing doctrine PR that explicitly authorizes each one:

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

Blocked means: no prompt may reference them, no schema profile may include them, no output bundle may contain them, until a governing doctrine PR explicitly authorizes each one with a confirmed Phase 0 evidence basis.

---

## Human approval requirements

The following actions require explicit human approval before proceeding:

| Action | Approval required |
|--------|------------------|
| Implementing schema on the current website | Human review and approval of validated output bundle |
| Attaching schema in Astro | Human review, carry gate confirmation, and approval |
| Setting `PRODUCTION_LOCKED` status | Human authorization only |
| Adding a currently blocked module | Governing doctrine PR with human merge |
| Adding a currently blocked field category | Governing doctrine PR with human merge |
| Resolving a Phase 0 / page evidence conflict | Phase 0 update process — not resolvable in this package |

---

## Non-production posture

PR #2 does not authorize JSON-LD generation.
PR #2 does not authorize current website implementation.
PR #2 does not authorize Astro attachment.
PR #2 does not authorize production lock.

The package status remains `DOCTRINE_BOUNDARY_ADDED_NO_SCHEMA_OUTPUT` until later PRs add truth packs, prompts, validators, and the final runnable handoff.
