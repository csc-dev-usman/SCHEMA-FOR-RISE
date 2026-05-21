# Rise Blocked Schema Modules — First Page V1.0

**Status:** `HOMEPAGE_SCHEMA_PROFILE_ADDED_NO_SCHEMA_OUTPUT`

---

## Purpose

This document defines the blocked schema modules for the Rise FC homepage and all first-page schema lanes. It specifies why each module is blocked, what would be required to unblock it, and the exception policy governing any future unblocking.

**No blocked module may be emitted from page type, assumptions, scraped snippets, or marketing intent.** Blocking is in effect regardless of what a competitor site, CMS template, or SEO tool suggests.

---

## Blocked first-page modules

| Blocked module | Block status |
|---------------|-------------|
| `FAQPage` | BLOCKED |
| `Offer` | BLOCKED |
| `Event` | BLOCKED |
| `Review` | BLOCKED |
| `AggregateRating` | BLOCKED |
| `Place` | BLOCKED |
| `GeoCoordinates` | BLOCKED |
| Testimonial-derived schema | BLOCKED |
| Bilingual schema | BLOCKED |
| Advanced modules | BLOCKED (by default) |

---

## Reason categories

| Reason code | Meaning |
|-------------|---------|
| `MISSING_PHASE0_TRUTH` | No Phase 0 confirmation exists for the facts this module requires |
| `HELD_FIELD_DEPENDENCY` | The module depends on one or more held field categories |
| `OWNER_APPROVAL_REQUIRED` | A human owner must approve the underlying facts before this module can be used |
| `DOCTRINE_NOT_YET_DEFINED` | A governing doctrine PR must explicitly authorize this module category |
| `RISK_OF_INVENTION` | High risk of inventing facts not confirmed by Phase 0 or page evidence |
| `BLOCKED_BY_DEFAULT` | Module is not an authorized first-page module without specific future authorization |

---

## Module-by-module block notes

### FAQPage

**Block reason:** `MISSING_PHASE0_TRUTH` + `RISK_OF_INVENTION`

FAQPage requires confirmed FAQ content visible on the page and traceable to Phase 0. Rise FC schema operators may not infer FAQ content from marketing copy, headings, or common-question conventions.

**What would be required to unblock:**
- Confirmed FAQ content in Phase 0 for the target page
- Visible FAQ section on the page confirmed by page evidence
- A governing doctrine PR explicitly authorizing FAQPage for the specific page/route
- Owner approval of the FAQ content

---

### Offer

**Block reason:** `MISSING_PHASE0_TRUTH` + `HELD_FIELD_DEPENDENCY` + `OWNER_APPROVAL_REQUIRED`

Offer requires confirmed pricing, program details, and availability confirmed from Phase 0. Price data is a held field category.

**What would be required to unblock:**
- Confirmed pricing and offer details in Phase 0
- Owner approval of price data
- A governing doctrine PR explicitly authorizing Offer for the specific page/route

---

### Event

**Block reason:** `MISSING_PHASE0_TRUTH` + `HELD_FIELD_DEPENDENCY`

Event requires confirmed event data including dates, location, and organizer confirmed from Phase 0. Event dates are a held field category.

**What would be required to unblock:**
- Confirmed event data including dates in Phase 0
- A governing doctrine PR explicitly authorizing Event for the specific page/route
- Owner approval of event date and location data

---

### Review

**Block reason:** `RISK_OF_INVENTION` + `DOCTRINE_NOT_YET_DEFINED`

Review requires a confirmed review source that is not testimonial content. Rise FC schema operators may not source Review schema from customer testimonials, marketing quotes, or informal feedback.

**What would be required to unblock:**
- A confirmed, compliant review source (not testimonials)
- A governing doctrine PR explicitly authorizing Review for specific page/route
- Owner approval of review source and content

---

### AggregateRating

**Block reason:** `RISK_OF_INVENTION` + `MISSING_PHASE0_TRUTH`

AggregateRating requires a confirmed, verifiable review corpus with a known count. This data does not exist in Phase 0.

**What would be required to unblock:**
- Confirmed review corpus in Phase 0 with verifiable count
- A governing doctrine PR explicitly authorizing AggregateRating
- Owner approval of rating data

---

### Place

**Block reason:** `HELD_FIELD_DEPENDENCY` + `OWNER_APPROVAL_REQUIRED`

Place requires confirmed address and place identity data. Address/place identity is a held field category.

**What would be required to unblock:**
- Confirmed address and place identity confirmed from Phase 0
- Owner approval of address data
- A governing doctrine PR explicitly authorizing Place for the specific page/route

---

### GeoCoordinates

**Block reason:** `HELD_FIELD_DEPENDENCY` + `OWNER_APPROVAL_REQUIRED` + `RISK_OF_INVENTION`

GeoCoordinates requires confirmed latitude/longitude from Phase 0. Coordinates may not be derived from an address or estimated from a map service.

**What would be required to unblock:**
- Confirmed coordinates explicitly provided in Phase 0
- Owner approval of coordinate data
- A governing doctrine PR explicitly authorizing GeoCoordinates

---

### Testimonial-derived schema

**Block reason:** `RISK_OF_INVENTION` + `DOCTRINE_NOT_YET_DEFINED`

Testimonials on a website are not confirmed facts. No schema property may be sourced from testimonial content without explicit Phase 0 confirmation and doctrine authorization.

**What would be required to unblock:**
- Explicit governing doctrine PR authorizing a specific testimonial-derived property with Phase 0 backing
- Owner approval

---

### Bilingual schema

**Block reason:** `DOCTRINE_NOT_YET_DEFINED`

Bilingual schema requires alternate-language page content policy, confirmed translations from Phase 0, and a governing doctrine defining the bilingual schema approach.

**What would be required to unblock:**
- Bilingual content policy added in a governing doctrine PR
- Confirmed alternate-language content in Phase 0
- Owner approval of bilingual content

---

### Advanced modules

**Block reason:** `BLOCKED_BY_DEFAULT`

Any schema module not explicitly listed in the allowed-future-modules list is blocked by default. This includes but is not limited to: `HowTo`, `Recipe`, `Product`, `JobPosting`, `Course`, `SportsEvent` at the first-page lane, `MusicEvent`, `Article` (on the homepage), and any other schema.org type not explicitly authorized.

**What would be required to unblock:**
- A governing doctrine PR explicitly authorizing the specific module
- Phase 0 truth basis for the module
- Owner approval if the module involves any held field category

---

## Exception policy

A blocked module may only be unblocked by:

1. A governing doctrine PR that explicitly names the module, the page/route it is authorized for, and the Phase 0 evidence basis.
2. Human merge of that doctrine PR.
3. An updated schema profile that includes the newly authorized module.

No operator, prompt, validator, or automated tool may unblock a module without a merged governing doctrine PR.

---

## Patch trigger conditions

| Condition | Action |
|-----------|--------|
| Phase 0 confirms facts required by a currently blocked module | Governing doctrine PR to authorize the module for the specific page |
| Owner approves a held field that unblocks a module | Governing doctrine PR to update the field status and authorize the module |
| A new page route requires a module not in the allowed list | Governing doctrine PR to authorize the module for that route |
