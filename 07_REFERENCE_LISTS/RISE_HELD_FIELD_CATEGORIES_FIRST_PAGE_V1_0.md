# Rise Held Field Categories — First Page V1.0

**Status:** `HOMEPAGE_SCHEMA_PROFILE_ADDED_NO_SCHEMA_OUTPUT`

---

## Purpose

This document defines the held field categories for the Rise FC homepage and all first-page schema lanes. A held field is a schema property whose value requires human owner approval and confirmed Phase 0/page evidence before it may be emitted in any schema output. All held fields default to `NOT_REVIEWED_HELD` status.

---

## Held field categories

| Field category | Schema property / module | Default status |
|---------------|--------------------------|----------------|
| Phone | `telephone` (Organization) | NOT_REVIEWED_HELD |
| Email | `email` (Organization) | NOT_REVIEWED_HELD |
| sameAs / social URLs | `sameAs` (Organization) | NOT_REVIEWED_HELD |
| Absolute logo URL | `logo` (Organization) | NOT_REVIEWED_HELD |
| Schema description from tagline | `description` (Organization / WebPage) | NOT_REVIEWED_HELD |
| Schema description from mission line | `description` (Organization / WebPage) | NOT_REVIEWED_HELD |
| Coordinates | `geo` / `GeoCoordinates` | NOT_REVIEWED_HELD |
| Address / place identity | `address` / `Place` | NOT_REVIEWED_HELD |
| Prices | `priceRange` / `Offer` | NOT_REVIEWED_HELD |
| Event dates | `startDate` / `Event` | NOT_REVIEWED_HELD |
| Offer details | `Offer` | NOT_REVIEWED_HELD |
| Reviews | `Review` | NOT_REVIEWED_HELD |
| Ratings | `AggregateRating` | NOT_REVIEWED_HELD |
| Testimonial-derived claims | any property | NOT_REVIEWED_HELD |
| Bilingual alternate data | any bilingual property | NOT_REVIEWED_HELD |

---

## Default status

Every held field category has a default status of:

`NOT_REVIEWED_HELD`

This means:
- The field has not been reviewed by the appropriate human owner.
- The field may not be emitted in any schema output.
- The field may not be estimated, inferred, or filled with a placeholder value.

---

## Approval requirements

A held field may only move out of `NOT_REVIEWED_HELD` status when all of the following are met:

1. The appropriate human owner has reviewed the field.
2. The owner has updated the owner approval worksheet (`03_TRUTH_PACK/RISE_CONTACT_SOCIAL_LOGO_OWNER_APPROVAL_WORKSHEET_V1_0.md`) with `APPROVED` status.
3. Phase 0 source confirmation exists for the specific field value.
4. The field value has been added to the homepage evidence map (later PR).
5. A governed truth-pack update PR records the approval.

---

## Evidence requirements

For each held field, the following evidence is required before emission:

| Field category | Required evidence |
|---------------|------------------|
| Phone | Phase 0 confirmed contact record with phone; owner approval |
| Email | Phase 0 confirmed contact record with email; owner approval |
| sameAs / social URLs | Phase 0 confirmed stable social profile URLs; owner approval per platform |
| Absolute logo URL | Phase 0 confirmed stable logo URL; owner confirmation of URL stability |
| Schema description from tagline | Phase 0 exact approved tagline; owner approval for use as schema description |
| Schema description from mission line | Phase 0 exact approved mission line; owner approval for use as schema description |
| Coordinates | Phase 0 confirmed coordinates (not derived from address); owner approval |
| Address / place identity | Phase 0 confirmed address and place identity; owner approval; doctrine authorization for Place module |
| Prices | Phase 0 confirmed pricing; owner approval; doctrine authorization for Offer module |
| Event dates | Phase 0 confirmed event data with dates; owner approval; doctrine authorization for Event module |
| Offer details | Phase 0 confirmed offer details; owner approval; doctrine authorization for Offer module |
| Reviews | Phase 0 confirmed compliant review source; owner approval; doctrine authorization for Review module |
| Ratings | Phase 0 confirmed review corpus with verifiable count; owner approval; doctrine authorization for AggregateRating |
| Testimonial-derived claims | Explicit governing doctrine authorization required; Phase 0 backing required |
| Bilingual alternate data | Bilingual content policy PR required; Phase 0 confirmed translations; owner approval |

---

## Emission rule

**No held field may be emitted in schema until it is approved by the appropriate human owner and supported by Phase 0 or confirmed page evidence.**

This rule applies without exception to:
- All schema output bundles
- All operator prompts
- All evidence maps
- All schema profiles
- Any JSON-LD draft

Omission is always the correct action when a held field is not approved. Placeholder values, inferred values, and estimates are not permitted.

---

## Non-authorization

This document does not approve any held field. It does not authorize schema output. It does not authorize JSON-LD generation. It does not authorize current website implementation or Astro attachment.

The owner approval worksheet in `03_TRUTH_PACK/RISE_CONTACT_SOCIAL_LOGO_OWNER_APPROVAL_WORKSHEET_V1_0.md` governs individual field approvals. All fields in that worksheet currently show `NOT_REVIEWED` status — no field is approved.
