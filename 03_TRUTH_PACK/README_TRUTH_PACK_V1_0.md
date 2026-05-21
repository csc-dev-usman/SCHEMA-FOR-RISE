# Truth Pack — Rise FC Standalone Schema Operator Package

**Status:** `TRUTH_PACK_HOMEPAGE_SCOPED_REFERENCE_ADDED_NO_SCHEMA_OUTPUT`

---

## Purpose

This folder stores read-only truth-pack reference material for schema operations. It provides the governed source material that later PRs will use to build evidence maps, schema profiles, operator prompts, validators, and a controlled non-production homepage schema draft.

This folder does not replace Rise Phase 0. It does not mutate Rise Phase 0. It is a scoped, read-only derivation layer that makes Phase 0 facts available in a schema-relevant format for the operator workflow.

---

## PR #3 scope

PR #3 adds:
- Phase 0 truth source map — defines what truth classes are needed by schema operators
- Homepage scoped Phase 0 schema truth-view reference — read-only JSON reference for the homepage route
- Homepage truth fingerprint lock — locks the truth-view currency for the homepage scope
- Contact/social/logo owner approval worksheet — tracks held fields awaiting human owner approval
- Truth-pack backlog — lists future truth-pack additions needed for other pages and routes

This PR does not generate schema. It does not authorize JSON-LD output. It does not authorize current website implementation. It does not authorize Astro attachment.

---

## What this folder contains

| File | Purpose |
|------|---------|
| `RISE_PHASE0_TRUTH_SOURCE_MAP_V1_0.md` | Source map defining truth classes and dependencies for schema operations |
| `RISE_PHASE0_SCHEMA_TRUTH_VIEW_HOMEPAGE_SCOPED_V1_0.json` | Read-only homepage scoped truth-view reference. Not JSON-LD. Not schema output. |
| `RISE_HOMEPAGE_TRUTH_FINGERPRINT_LOCK_V1_0.md` | Fingerprint lock for the homepage truth-view. Currency verification rules. |
| `RISE_CONTACT_SOCIAL_LOGO_OWNER_APPROVAL_WORKSHEET_V1_0.md` | Owner approval worksheet for held fields. All fields default to NOT_REVIEWED. |
| `TRUTH_PACK_BACKLOG.md` | Backlog of future truth-pack additions for other pages and routes |

---

## What this folder does not contain

- Schema output or JSON-LD files
- Homepage JSON-LD draft
- Evidence maps (added in a later PR)
- Schema profiles (added in a later PR)
- Operator prompts (added in PR #4)
- Validators or smoke tests (added in PR #5)
- Sample runs or run artifacts
- Any production schema bundles

---

## Reading order

1. `RISE_PHASE0_TRUTH_SOURCE_MAP_V1_0.md`
2. `RISE_PHASE0_SCHEMA_TRUTH_VIEW_HOMEPAGE_SCOPED_V1_0.json`
3. `RISE_HOMEPAGE_TRUTH_FINGERPRINT_LOCK_V1_0.md`
4. `RISE_CONTACT_SOCIAL_LOGO_OWNER_APPROVAL_WORKSHEET_V1_0.md`
5. `TRUTH_PACK_BACKLOG.md`

---

## Non-authorization

This folder and all files within it:
- Do not generate schema
- Do not authorize JSON-LD output
- Do not authorize current website implementation
- Do not authorize Astro attachment
- Do not authorize production lock
- Do not mutate Rise Phase 0
- Do not approve held fields (phone, email, social URLs, logo URL, coordinates, reviews, ratings, prices, events, offers, testimonial-derived claims)

All held fields remain held until the owner approval worksheet is updated by the appropriate human owner with Phase 0 support.

---

## Next expected PR

PR #4 should add the Rise homepage schema profile and blocked module policy:
`docs: add Rise homepage schema profile and blocked module policy`
