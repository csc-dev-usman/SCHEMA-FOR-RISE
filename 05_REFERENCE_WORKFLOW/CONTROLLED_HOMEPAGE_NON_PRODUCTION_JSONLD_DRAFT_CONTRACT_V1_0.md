# Controlled Homepage Non-Production JSON-LD Draft Contract V1.0

**Status:** `HOMEPAGE_NON_PRODUCTION_DRAFT_CONTRACT_ADDED_NO_SCHEMA_OUTPUT`

> **This PR creates no draft.** This document defines the rules for how a future homepage draft will be produced. No JSON-LD has been created. No `@context` exists. No `@type` nodes exist. No schema output exists. This is a governance contract only.

---

## Contract purpose

This contract governs the production of the first Rise FC homepage non-production JSON-LD draft. It defines:

- What the draft is allowed to contain
- What the draft is not allowed to contain
- What conditions must be met before the draft is created
- What approval is required before the draft can be implemented
- What schema modules are allowed
- What schema modules are blocked
- What fields are held

This contract does not authorize schema generation. The actual draft will be created in a future governed run after all preconditions in `HOMEPAGE_DRAFT_PRECONDITIONS_AND_HOLD_MATRIX_V1_0.md` are confirmed.

---

## What the draft is

The homepage non-production JSON-LD draft is a **governed, evidence-anchored, non-production schema draft** for the Rise FC homepage (route `/`) derived from:

1. Confirmed Rise Phase 0 factual content
2. Confirmed page evidence from the current risefcsoccer.com homepage
3. The active `HOMEPAGE_SCHEMA_PROFILE`
4. The confirmed evidence map for the homepage

The draft is marked `NON_PRODUCTION` until explicit human approval is granted. It may not be implemented on the current website or attached to Astro without that approval.

---

## What the draft is not

The draft is **not**:
- A production-ready schema
- An authorization to implement on the current website
- An authorization to attach to Astro
- A mutation of Rise Phase 0
- A source of new facts
- Self-approving at any stage

---

## Allowed schema modules (homepage first-page lane)

| Module | Status |
|--------|--------|
| `Organization` | Allowed |
| `WebSite` | Allowed |
| `WebPage` | Allowed |
| `BreadcrumbList` | Allowed |
| `ListItem` | Allowed as child of BreadcrumbList only |

No other modules are authorized for the first-page lane.

---

## Blocked schema modules

The following modules are **blocked** and must not appear in the draft under any circumstances:

| Module | Block reason |
|--------|-------------|
| `FAQPage` | Blocked — homepage profile |
| `Question` | Blocked — child of FAQPage |
| `Answer` | Blocked — child of FAQPage |
| `Offer` | Blocked — homepage profile |
| `AggregateOffer` | Blocked — homepage profile |
| `Event` | Blocked — homepage profile |
| `SportsEvent` | Blocked — homepage profile |
| `Review` | Blocked — homepage profile |
| `AggregateRating` | Blocked — homepage profile |
| `Place` | Blocked — homepage profile |
| `LocalBusiness` | Blocked — homepage profile |
| `GeoCoordinates` | Blocked — homepage profile |
| `PostalAddress` | Blocked — homepage profile |
| Testimonial-derived schema | Blocked — additional category |
| Bilingual schema | Blocked — additional category |
| Advanced modules not in profile | Blocked — additional category |

---

## Held fields

The following field categories are held and **must not appear** in the draft unless explicitly released by owner approval:

| Category | Schema properties | Can be unblocked |
|----------|-------------------|-----------------|
| `phone` | `telephone` | Yes — requires owner approval |
| `email` | `email` | Yes — requires owner approval |
| `sameAs` | `sameAs` | Yes — requires owner approval |
| `logoUrl` | `logo`, `image` | Yes — requires owner approval |
| `descriptionFromTagline` | `description` | Yes — requires owner approval + confirmed factual copy |
| `coordinates` | `geo`, `latitude`, `longitude` | No — blocked module |
| `addressPlaceIdentity` | `address`, `streetAddress`, etc. | No — blocked module |
| `reviews` | `review` | No — blocked module |
| `ratings` | `aggregateRating`, `ratingValue`, etc. | No — blocked module |
| `prices` | `price`, `priceCurrency`, `priceRange` | No — blocked module |
| `eventDates` | `startDate`, `endDate`, `eventSchedule` | No — blocked module |
| `offerDetails` | `offers`, `availability` | No — blocked module |
| `testimonialDerivedClaims` | (any field derived from testimonial) | No — blocked category |
| `bilingualAlternateData` | (any bilingual alternate) | No — blocked category |

---

## Draft governance rules

1. **Evidence-first only.** Every field value in the draft must trace to a confirmed Phase 0 source reference or confirmed page evidence. No invented values. No inferred values. No speculative values.

2. **NON_PRODUCTION marker required.** The draft must be marked `NON_PRODUCTION` in its output bundle manifest until explicit human approval is granted.

3. **No self-approval.** The operator, QA agent, controller agent, and analyzer agent may not grant production authorization. Human approval is required.

4. **No held fields without owner approval.** None of the 14 held field categories may be emitted until the owner approval worksheet confirms release.

5. **No blocked modules.** None of the blocked modules may appear in the draft for any reason.

6. **Truth fingerprint must match.** The truth fingerprint confirmed at Prompt 00 intake must match the expected value: `80edd829806cae271242c6a8e853edabdb8b2f16ca5a8fa1a3fc69ff5b78d53d`.

7. **Evidence map required before drafting.** A confirmed evidence map must exist before Prompt 01 may run.

8. **JSON-LD structural rules.** The draft must satisfy all 10 JSON-LD safety rules (JLSR_001–JLSR_010) defined in `06_MACHINE_RULES/RISE_SCHEMA_LINT_RULES_V1_0.json`.

9. **Phase 0 read-only.** The draft operator must not mutate Rise Phase 0 or any source truth.

10. **Mode declaration required.** The draft must be produced under Mode 1 (`MODE_1_CURRENT_WEBSITE`) or Mode 2 (`MODE_2_FUTURE_ASTRO_CARRY`), declared at intake. The first draft runs under Mode 1.

---

## Required pre-run confirmations

Before any operator begins a governed homepage draft run, all items in `HOMEPAGE_DRAFT_PRECONDITIONS_AND_HOLD_MATRIX_V1_0.md` must be confirmed. See that document for the full list.

---

## Non-authorization statement

This contract does not authorize:
- JSON-LD generation
- Schema output production
- Implementation on the current risefcsoccer.com website
- Attachment to any Astro file
- Production lock status
- Any mutation of Rise Phase 0 or source truth

The first governed homepage draft will be produced in a future governed run after this contract is reviewed and all preconditions are confirmed.
