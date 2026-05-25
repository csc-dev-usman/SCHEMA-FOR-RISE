# Redacted Sample Artifact Requirements V1.0

**Status:** `MILESTONE_4_FIRST_REAL_PAGE_RUN_SUPPORT_COMPLETE_NO_SCHEMA_OUTPUT`

---

## Purpose

This document defines the redaction requirements that will apply to any redacted sample artifact committed to this repository under a future authorized artifact lane.

These requirements are defined now — before any artifact lane exists — so that when a future PR establishes a redacted artifact lane, the redaction standard is already governed and unambiguous.

---

## Current status

**No redacted sample artifacts are currently authorized.**

This document is a forward-looking governance reference only. No redacted artifacts may be committed until a future PR explicitly establishes a redacted artifact lane and references this document as the controlling redaction standard.

---

## What a redacted sample artifact is

A redacted sample artifact is a real run artifact (output bundle, JSON-LD draft, controller decision record, or similar) from which all sensitive, held, or owner-governed fields have been removed before committing.

Redaction is not the same as synthetic data. A synthetic artifact uses entirely fake data (`example.invalid`). A redacted artifact is derived from a real run but has had governed fields stripped.

---

## Required redactions

Any redacted sample artifact committed to this repository must have the following fields removed or replaced with `[REDACTED]`:

### Category 1 — Contact and identity fields

| Field | Redaction |
|-------|-----------|
| Phone number | Replace with `[REDACTED_PHONE]` |
| Email address | Replace with `[REDACTED_EMAIL]` |
| Fax number | Replace with `[REDACTED_FAX]` |
| Contact point data | Replace with `[REDACTED_CONTACT]` |

### Category 2 — Social and sameAs URLs

| Field | Redaction |
|-------|-----------|
| `sameAs` array entries (social URLs) | Replace each entry with `[REDACTED_SAME_AS]` |
| Facebook URL | Replace with `[REDACTED_FACEBOOK]` |
| Twitter/X URL | Replace with `[REDACTED_TWITTER]` |
| Instagram URL | Replace with `[REDACTED_INSTAGRAM]` |
| LinkedIn URL | Replace with `[REDACTED_LINKEDIN]` |
| YouTube URL | Replace with `[REDACTED_YOUTUBE]` |
| Any other social platform URL | Replace with `[REDACTED_SOCIAL_URL]` |

### Category 3 — Logo and image URLs

| Field | Redaction |
|-------|-----------|
| Absolute logo URL | Replace with `[REDACTED_LOGO_URL]` |
| Organization image URL | Replace with `[REDACTED_IMAGE_URL]` |

### Category 4 — Location and coordinates

| Field | Redaction |
|-------|-----------|
| `latitude` | Replace with `[REDACTED_LAT]` |
| `longitude` | Replace with `[REDACTED_LNG]` |
| Street address | Replace with `[REDACTED_ADDRESS]` |
| Postal code | Replace with `[REDACTED_POSTAL]` |
| City / locality | Replace with `[REDACTED_LOCALITY]` |
| State / region | Replace with `[REDACTED_REGION]` |
| Country | Retain if non-sensitive (e.g., `US`); redact if combined with other location data |

### Category 5 — Review and rating data

| Field | Redaction |
|-------|-----------|
| Individual review text | Replace with `[REDACTED_REVIEW]` |
| Reviewer name | Replace with `[REDACTED_REVIEWER]` |
| Aggregate rating value | Replace with `[REDACTED_RATING]` |
| Review count | Replace with `[REDACTED_COUNT]` |

### Category 6 — Price and offer data

| Field | Redaction |
|-------|-----------|
| Price values | Replace with `[REDACTED_PRICE]` |
| Offer details | Replace with `[REDACTED_OFFER]` |
| Currency | Replace with `[REDACTED_CURRENCY]` |

### Category 7 — Event data

| Field | Redaction |
|-------|-----------|
| Event dates | Replace with `[REDACTED_DATE]` |
| Event location | Replace with `[REDACTED_EVENT_LOCATION]` |
| Event price | Replace with `[REDACTED_EVENT_PRICE]` |

### Category 8 — Owner-only and testimonial data

| Field | Redaction |
|-------|-----------|
| Testimonial-derived claims | Replace with `[REDACTED_TESTIMONIAL]` |
| Bilingual alternate data | Replace with `[REDACTED_BILINGUAL]` |
| Internal operator notes referencing sensitive data | Replace with `[REDACTED_NOTE]` |

---

## Required redacted artifact header

Every redacted sample artifact must carry a header block in its JSON or at the top of its Markdown file:

For JSON artifacts:
```json
{
  "safetyNote": "REDACTED_SAMPLE_ARTIFACT — all sensitive, held, and owner-governed fields have been replaced with [REDACTED_*] placeholders. This artifact was derived from a real governed run. It does not represent production-ready schema. It does not authorize implementation.",
  "redactionVersion": "REDACTED_SAMPLE_ARTIFACT_REQUIREMENTS_V1_0",
  "productionLockStatus": "NO_PRODUCTION_LOCKS"
}
```

For Markdown artifacts, the header must appear as a blockquote at the top:

```
> REDACTED SAMPLE ARTIFACT — All sensitive, held, and owner-governed fields have been
> replaced with [REDACTED_*] placeholders per REDACTED_SAMPLE_ARTIFACT_REQUIREMENTS_V1_0.
> This artifact does not authorize implementation or production lock.
```

---

## Redaction verification checklist

Before committing a redacted sample artifact, confirm:

- [ ] All Category 1–8 fields are redacted or absent
- [ ] No real phone number, email, or contact data remains
- [ ] No real social URL remains in any `sameAs` or equivalent field
- [ ] No real absolute logo URL remains
- [ ] No real coordinates, address, or postal code remains
- [ ] No real review text or reviewer name remains
- [ ] No real price or offer data remains
- [ ] No real event date or event location remains
- [ ] No testimonial-derived or bilingual data remains
- [ ] Redacted artifact header is present
- [ ] `productionLockStatus` is `NO_PRODUCTION_LOCKS`
- [ ] Authorized artifact lane exists (future PR confirmed)
- [ ] Human approval obtained for artifact commit

---

## What redaction does not permit

Redaction does not permit:
- Including blocked schema modules (FAQPage, Offer, Event, Review, AggregateRating, Place, GeoCoordinates) in any sample artifact
- Claiming `PRODUCTION_LOCKED` on a redacted artifact
- Using a redacted artifact as a substitute for a real governed run
- Committing a redacted artifact without an authorized artifact lane

---

## What this document does not do

- It does not authorize redacted artifact commits
- It does not establish an artifact lane
- It does not create any artifacts
- It does not generate schema
- It does not create JSON-LD
- It does not mutate Rise Phase 0
