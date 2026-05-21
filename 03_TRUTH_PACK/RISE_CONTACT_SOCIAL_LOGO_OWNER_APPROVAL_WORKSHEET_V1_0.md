# Rise Contact, Social, and Logo Owner Approval Worksheet V1.0

**Status:** `ALL_FIELDS_NOT_REVIEWED — NO_FIELDS_APPROVED_FOR_SCHEMA`

---

## Purpose

This worksheet tracks the approval status of field categories that require human owner review before they may be emitted in any Rise FC schema output. Every field listed here is currently held. No field may be added to a schema profile, operator prompt, or output bundle until it has been approved by the appropriate human owner and is supported by Phase 0 or confirmed page evidence.

---

## Fields requiring owner approval

The following field categories are held pending owner review.

**No field listed in this worksheet may be emitted in schema until it is approved by the appropriate human owner and supported by Phase 0 or confirmed page evidence.**

---

## Required owner decision table

| Field category | Schema property / module | Current status | Owner decision | Phase 0 support | Notes |
|---------------|--------------------------|----------------|----------------|-----------------|-------|
| Public phone | `telephone` (Organization) | NOT_REVIEWED | — | — | Must trace to Phase 0 confirmed contact record |
| Public email | `email` (Organization) | NOT_REVIEWED | — | — | Must trace to Phase 0 confirmed contact record |
| sameAs — Facebook | `sameAs` (Organization) | NOT_REVIEWED | — | — | Must be confirmed stable URL from Phase 0 |
| sameAs — Instagram | `sameAs` (Organization) | NOT_REVIEWED | — | — | Must be confirmed stable URL from Phase 0 |
| sameAs — Twitter / X | `sameAs` (Organization) | NOT_REVIEWED | — | — | Must be confirmed stable URL from Phase 0 |
| sameAs — YouTube | `sameAs` (Organization) | NOT_REVIEWED | — | — | Must be confirmed stable URL from Phase 0 |
| sameAs — LinkedIn | `sameAs` (Organization) | NOT_REVIEWED | — | — | Must be confirmed stable URL from Phase 0 |
| sameAs — other | `sameAs` (Organization) | NOT_REVIEWED | — | — | Must be confirmed stable URL from Phase 0 |
| Absolute logo URL | `logo` (Organization) | NOT_REVIEWED | — | — | Must be a stable, confirmed URL — not guessed |
| Schema description from tagline | `description` (Organization / WebPage) | NOT_REVIEWED | — | — | Must be an exact, approved phrase from Phase 0 |
| Schema description from mission line | `description` (Organization / WebPage) | NOT_REVIEWED | — | — | Must be an exact, approved phrase from Phase 0 |
| Coordinates / geo | `geo` / `GeoCoordinates` | NOT_REVIEWED | — | — | Blocked module — requires doctrine authorization + Phase 0 confirmation |
| Address / place identity | `address` / `Place` | NOT_REVIEWED | — | — | Blocked module — requires doctrine authorization + Phase 0 confirmation |
| Prices | `priceRange` / `Offer` | NOT_REVIEWED | — | — | Blocked module |
| Event dates | `startDate` / `Event` | NOT_REVIEWED | — | — | Blocked module |
| Offer details | `Offer` | NOT_REVIEWED | — | — | Blocked module |
| Reviews | `Review` | NOT_REVIEWED | — | — | Blocked module — may not be sourced from testimonials |
| Ratings | `AggregateRating` | NOT_REVIEWED | — | — | Blocked module |
| Testimonial-derived claims | any property | NOT_REVIEWED | — | — | Blocked — testimonials are not confirmed Phase 0 facts |
| Bilingual alternate data | any bilingual property | NOT_REVIEWED | — | — | Blocked until bilingual doctrine is defined |

---

## Approval status values

| Value | Meaning |
|-------|---------|
| `NOT_REVIEWED` | Default. Field has not been reviewed by the owner. Held. |
| `APPROVED` | Owner has reviewed and approved the field value. Phase 0 support confirmed. Field may proceed to schema profile. |
| `REJECTED` | Owner has reviewed and rejected the field. Field must not appear in schema. |
| `DEFERRED` | Owner has reviewed but deferred the decision. Field remains held. |
| `NEEDS_SOURCE` | Field requires additional Phase 0 confirmation before owner can decide. Field remains held. |

---

## How this worksheet affects schema

- Any field with status `NOT_REVIEWED`, `DEFERRED`, or `NEEDS_SOURCE` must be omitted from schema output.
- Any field with status `REJECTED` must never appear in schema output for this property.
- Only fields with status `APPROVED` and confirmed Phase 0 support may proceed to the schema profile.
- Approval of a field in this worksheet does not by itself authorize schema output — the field must also pass through the evidence map and schema profile gates.

---

## Non-authorization

This worksheet:
- Does not authorize JSON-LD generation
- Does not authorize current website implementation
- Does not authorize Astro attachment
- Does not approve any field by default
- Does not modify Phase 0

---

## Next steps

1. Human owner reviews each field category.
2. For fields the owner wants to approve: confirm Phase 0 source, update status to `APPROVED`, record the Phase 0 reference.
3. For fields the owner wants to reject: update status to `REJECTED`.
4. For fields needing more source: update status to `NEEDS_SOURCE` and identify what Phase 0 material is needed.
5. Bring approved fields into a later evidence map and schema profile PR.
6. A governing truth-pack update PR is required to record approved changes to this worksheet.
