# Rise Homepage Schema Profile V1.0

**Status:** `HOMEPAGE_SCHEMA_PROFILE_ADDED_NO_SCHEMA_OUTPUT`

---

## Purpose

This document defines the homepage schema profile (`HOMEPAGE_SCHEMA_PROFILE`) for the Rise FC standalone schema operator package. It specifies the page scope, route, allowed future modules, blocked modules, held fields, and all preconditions that must be met before a schema draft may be generated for this profile.

This document is a policy/profile document only. It does not authorize JSON-LD output. It does not authorize production deployment. It does not authorize current website implementation. It does not authorize Astro attachment.

---

## Page scope

| Field | Value |
|-------|-------|
| Target page | Homepage |
| Route | `/` |
| Profile ID | `HOMEPAGE_SCHEMA_PROFILE` |
| First schema lane target | Yes |
| Mode | Mode 1 (current website) and Mode 2 (future Astro carry reference) |

---

## Fingerprint dependency

The homepage schema profile is anchored to the following locked truth-view fingerprint:

```
80edd829806cae271242c6a8e853edabdb8b2f16ca5a8fa1a3fc69ff5b78d53d
```

If the fingerprint cannot be verified, schema work for this profile must hold.

---

## Required upstream dependencies

All of the following must exist and be confirmed before a schema draft may be generated for `HOMEPAGE_SCHEMA_PROFILE`:

| Dependency | Status | Location |
|-----------|--------|----------|
| Phase 0 source reference | PRESENT (read-only) | `03_TRUTH_PACK/RISE_PHASE0_TRUTH_SOURCE_MAP_V1_0.md` |
| Homepage scoped schema truth view | PRESENT (read-only) | `03_TRUTH_PACK/RISE_PHASE0_SCHEMA_TRUTH_VIEW_HOMEPAGE_SCOPED_V1_0.json` |
| Homepage truth fingerprint | LOCKED | `03_TRUTH_PACK/RISE_HOMEPAGE_TRUTH_FINGERPRINT_LOCK_V1_0.md` |
| Owner approval worksheet for held fields | PRESENT — all fields NOT_REVIEWED | `03_TRUTH_PACK/RISE_CONTACT_SOCIAL_LOGO_OWNER_APPROVAL_WORKSHEET_V1_0.md` |
| Homepage evidence map | NOT_YET_CREATED | Required in a later PR |
| Operator prompt for homepage profile | NOT_YET_CREATED | Required in a later PR |
| Validator protocol | NOT_YET_CREATED | Required in a later PR |
| Controller/human decision for production | NOT_YET_AUTHORIZED | Required after validation |

---

## Allowed future modules

The following schema modules are the authorized future targets for `HOMEPAGE_SCHEMA_PROFILE`. They are allowed future modules only — they are not authorized for JSON-LD output in PR #4.

| Module | Status |
|--------|--------|
| `Organization` | ALLOWED_FUTURE_ONLY — requires evidence map, prompt, validation, and controller approval |
| `WebSite` | ALLOWED_FUTURE_ONLY — requires evidence map, prompt, validation, and controller approval |
| `WebPage` | ALLOWED_FUTURE_ONLY — requires evidence map, prompt, validation, and controller approval |
| `BreadcrumbList` | ALLOWED_FUTURE_ONLY — requires evidence map, prompt, validation, and controller approval |

**Allowed does not mean emitted.** Emission requires a completed evidence map, an approved operator prompt, validation passing, and explicit controller approval — none of which exist after PR #4.

---

## Blocked modules

The following schema modules are blocked for `HOMEPAGE_SCHEMA_PROFILE` and all first-page schema. They may not be added to any evidence map, prompt, or output bundle without a governing doctrine PR that explicitly authorizes each one:

| Blocked module |
|---------------|
| `FAQPage` |
| `Offer` |
| `Event` |
| `Review` |
| `AggregateRating` |
| `Place` |
| `GeoCoordinates` |
| Testimonial-derived schema |
| Bilingual schema |
| Advanced modules |

---

## Held fields

The following field categories are held and must not appear in any schema output for `HOMEPAGE_SCHEMA_PROFILE` unless the owner approval worksheet is updated with `APPROVED` status and Phase 0 support is confirmed:

| Held field category |
|--------------------|
| `telephone` / phone |
| `email` |
| `sameAs` / social profile URLs |
| Absolute logo URL |
| Schema description from tagline |
| Schema description from mission line |
| Coordinates |
| Address / place identity |
| Prices |
| Event dates |
| Offer details |
| Reviews |
| Ratings |
| Testimonial-derived claims |
| Bilingual alternate data |

---

## Drafting preconditions

A schema draft for `HOMEPAGE_SCHEMA_PROFILE` may not begin until all of the following are confirmed:

- [ ] Homepage evidence map exists and is approved
- [ ] Operator prompt for homepage profile exists and is approved
- [ ] Fingerprint matches: `80edd829806cae271242c6a8e853edabdb8b2f16ca5a8fa1a3fc69ff5b78d53d`
- [ ] No held fields are being emitted
- [ ] No blocked modules are being included
- [ ] Validator protocol exists
- [ ] Human controller has authorized schema drafting for this profile

---

## Non-authorization

`HOMEPAGE_SCHEMA_PROFILE` as documented in PR #4:
- Does not authorize JSON-LD draft generation
- Does not authorize production schema output
- Does not authorize current website implementation
- Does not authorize Astro attachment
- Does not authorize production lock (`PRODUCTION_LOCKED`)

---

## Hold conditions

| Condition | Required action |
|-----------|----------------|
| Fingerprint mismatch | HOLD — do not proceed |
| Homepage evidence map missing | HOLD — do not draft |
| Operator prompt missing | HOLD — do not draft |
| Validator protocol missing | HOLD — do not proceed to output |
| Held field requested without owner approval | HOLD — omit field |
| Blocked module requested | HOLD — reject module |
| Phase 0 / page evidence conflict | HOLD — escalate upstream |
| Controller authorization missing | HOLD — do not proceed to production |

---

## Next required artifact

The immediate next artifact required to advance this profile toward a schema draft:

1. Homepage evidence map (later PR)
2. Operator prompt for homepage profile (later PR)
3. Validator protocol (later PR)
4. Final runnable handoff (later PR)
