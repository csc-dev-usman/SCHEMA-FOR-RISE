# Rise Schema Non-Authorization and Hold Rules V1.0

**Status:** `DOCTRINE_BOUNDARY_ADDED_NO_SCHEMA_OUTPUT`

---

## What PR #2 authorizes

PR #2 authorizes:
- Adding the source-truth boundary document
- Adding the governing doctrine document
- Adding the operator lane ownership document
- Adding this non-authorization and hold rules document
- Updating the root README, package manifest, doctrine version ledger, and start files to reflect the doctrine layer

That is the complete authorization scope of PR #2.

---

## What PR #2 does not authorize

PR #2 does not authorize any of the following:

| Not authorized | Explanation |
|---------------|-------------|
| JSON-LD generation | No schema output of any kind |
| Schema output bundles | Not until truth pack, prompts, validators, and runnable handoff exist |
| Production schema bundles | Not until human approval and `PRODUCTION_LOCKED` status |
| Production deployment | Requires human authorization — not granted by PR #2 |
| `PRODUCTION_LOCKED` status | Not granted by PR #2 |
| Current website implementation | Requires validated output bundle and human approval |
| Astro attachment | Requires carry gates, validated output bundle, and human approval |
| Phase 0 mutation | Prohibited at all times from this package |
| Source truth mutation | Prohibited at all times from this package |
| Truth pack JSON files | Added in PR #3 |
| Generated Phase 0 truth views | Added in PR #3 |
| Homepage scoped truth derivations | Added in PR #3 |
| Evidence maps | Added in PR #3 |
| Schema profiles | Added in PR #3 or later |
| Operator prompts | Added in PR #4 |
| Machine rules | Added in PR #4 |
| Validators | Added in PR #5 |
| Smoke tests | Added in PR #5 |
| Real run artifacts | Not authorized until runnable handoff exists |
| Sample-run artifacts | Not authorized |

---

## Mandatory holds

Operators must place a hold and must not proceed with schema work when any of the following conditions are true:

| Hold condition | What to do |
|---------------|------------|
| Missing Phase 0 source reference | HOLD — do not begin schema derivation. Source a Phase 0 anchor first. |
| Missing or stale schema truth view | HOLD — do not generate schema fields. Request an updated truth view. |
| Missing truth fingerprint | HOLD — cannot verify truth-view currency without fingerprint. |
| Missing page evidence map | HOLD — do not create a schema profile without confirmed page evidence. |
| Missing schema profile | HOLD — do not generate output without an approved profile. |
| Phase 0 and page evidence conflict | HOLD — escalate upstream. Do not resolve by overriding Phase 0. |
| Required truth missing for a field | HOLD — omit the field. Do not estimate or infer. |
| Requested schema module is blocked | HOLD — defer until a governing doctrine PR explicitly authorizes the module. |
| Attempted production lock without human approval | HARD STOP |
| Attempted Astro attachment before carry gates exist | HARD STOP |
| Attempted current website implementation before validation | HARD STOP |
| Attempted current website implementation without human approval | HARD STOP |
| Attempted Phase 0 mutation | HARD STOP |
| Attempted source truth mutation | HARD STOP |

---

## Blocked field categories

The following field categories are blocked and must not appear in any schema output unless a governing doctrine PR explicitly authorizes the field with a confirmed Phase 0 evidence basis:

| Blocked field category | Reason |
|-----------------------|--------|
| `telephone` / phone | Requires human confirmation — not to be invented or inferred |
| `email` | Requires human confirmation — not to be invented or inferred |
| `sameAs` / social profile URLs | Must be confirmed by Phase 0 — not to be inferred from convention |
| Absolute logo URL | Must be a confirmed, stable URL — not to be guessed |
| `latitude` / `longitude` / coordinates | Requires Phase 0 geo confirmation — not to be derived from address |
| `Review` content | Blocked module — not sourced from testimonials |
| `ratingValue` / `ratingCount` | Blocked module — `AggregateRating` blocked |
| `price` / `priceRange` / offer details | Blocked module — `Offer` blocked |
| Event dates and event details | Blocked module — `Event` blocked |
| Bilingual alternate data | Blocked until bilingual doctrine is defined |
| Testimonial-derived claims | Blocked — testimonials are not confirmed facts |

---

## Blocked module categories

The following schema modules are blocked for the first-page lane and all pages until a governing doctrine PR explicitly authorizes each one:

| Blocked module | Block reason |
|---------------|-------------|
| `FAQPage` | Requires confirmed FAQ content in Phase 0 — not assumed |
| `Offer` | Requires confirmed pricing — not to be inferred |
| `Event` | Requires confirmed event data — not to be inferred |
| `Review` | Cannot source reviews from testimonials or convention |
| `AggregateRating` | Cannot source aggregate rating data without confirmed review corpus |
| `Place` | Requires confirmed address and geo data from Phase 0 |
| `GeoCoordinates` | Requires confirmed coordinates from Phase 0 |
| Testimonial-derived schema | Testimonials are not confirmed Phase 0 facts |
| Bilingual schema | Requires bilingual doctrine — not yet defined |
| Advanced modules | Requires specific doctrine authorization for each module |

---

## Production lock prohibition

`PRODUCTION_LOCKED` status may not be set by:
- Any operator prompt
- Any validator
- Any automated tool
- Any self-merge

`PRODUCTION_LOCKED` may only be set after:
- A validated output bundle exists
- A human reviewer has reviewed and approved the bundle
- A human has explicitly authorized the production lock

---

## Real artifact prohibition

The following artifact types must not be committed to this repository until the runnable handoff exists and a governed run has been completed:

- JSON-LD output files
- Schema output bundles
- Validator screenshots
- Screaming Frog exports
- Claude QA zips
- Any file in a `sample_runs/` directory
- Any file representing a real schema run output

---

## Patch trigger conditions

The following conditions should trigger a patch PR or a governing doctrine update PR:

| Condition | Patch trigger |
|-----------|--------------|
| A new page route requires a schema module not currently authorized | Governing doctrine PR to authorize the module |
| Phase 0 confirms a previously blocked field category | Governing doctrine PR to unblock the specific field |
| A blocked module becomes confirmable from Phase 0 evidence | Governing doctrine PR to authorize the module |
| A hold condition is encountered repeatedly | Review root cause — may require truth pack or evidence map update |
| A validator produces an unexpected hold result | Validator patch PR |
| The source-truth hierarchy needs clarification | Doctrine patch PR |
