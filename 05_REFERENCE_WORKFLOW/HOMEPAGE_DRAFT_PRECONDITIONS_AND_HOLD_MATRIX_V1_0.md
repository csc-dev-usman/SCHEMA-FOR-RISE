# Homepage Draft Preconditions and Hold Matrix V1.0

**Status:** `HOMEPAGE_NON_PRODUCTION_DRAFT_CONTRACT_ADDED_NO_SCHEMA_OUTPUT`

> All preconditions below must be confirmed before any operator begins a governed homepage draft run. If any precondition is not met: STOP. Do not proceed.

---

## Precondition checklist

### Source truth and fingerprint

- [ ] **Phase 0 source reference confirmed.** The operator has a confirmed Rise Phase 0 source reference for the homepage.
- [ ] **Homepage scoped truth view present.** `03_TRUTH_PACK/RISE_PHASE0_SCHEMA_TRUTH_VIEW_HOMEPAGE_SCOPED_V1_0.json` is present and parses cleanly.
- [ ] **Truth fingerprint match confirmed.** The SHA-256 fingerprint of the homepage scoped truth view matches the expected value: `80edd829806cae271242c6a8e853edabdb8b2f16ca5a8fa1a3fc69ff5b78d53d`.
- [ ] **Truth view is current.** The truth view has not been superseded by a newer Phase 0 update that would invalidate the fingerprint.

### Schema profile and policies

- [ ] **Homepage schema profile confirmed.** `HOMEPAGE_SCHEMA_PROFILE` is active for route `/`.
- [ ] **Blocked module policy confirmed.** The operator has read `07_REFERENCE_LISTS/RISE_BLOCKED_SCHEMA_MODULES_FIRST_PAGE_V1_0.md` and confirms no blocked modules will be used.
- [ ] **Held field policy confirmed.** The operator has read `07_REFERENCE_LISTS/RISE_HELD_FIELD_CATEGORIES_FIRST_PAGE_V1_0.md` and confirms no held fields will be emitted without owner approval.
- [ ] **Output bundle contract schemas confirmed.** The operator has read all files in `06_MACHINE_RULES/` and confirms the lint rules and contract schemas are understood.

### Operator prompt sequence

- [ ] **Prompt 00 completed.** Intake and run context confirmed. Target URL, truth state, schema profile, blocked modules, held fields, and evidence map status collected.
- [ ] **Prompt 08 passed.** Page content readiness gate passed. Current page content is confirmed adequate for schema derivation.

### Evidence map

- [ ] **Evidence map confirmed present.** A homepage evidence map has been created that satisfies the shape defined in `06_MACHINE_RULES/EVIDENCE_MAP_SCHEMA_V1_0.json`.
- [ ] **Evidence map fields reviewed.** All field-level evidence decisions (EMIT / HELD / DEFERRED / EXCLUDED_BLOCKED_MODULE / EXCLUDED_NO_EVIDENCE) have been confirmed.
- [ ] **No unconfirmed field values.** Every field marked EMIT traces to `PHASE_0_CONFIRMED` or `PAGE_EVIDENCE_CONFIRMED` status in the evidence map.

### Validation and review infrastructure

- [ ] **Output bundle contract schemas present.** `06_MACHINE_RULES/` folder exists with all 7 files from PR #9.
- [ ] **Lint rules loaded.** `06_MACHINE_RULES/RISE_SCHEMA_LINT_RULES_V1_0.json` has been read. All 10 JLSR safety rules understood.
- [ ] **Review and approval sequence understood.** The operator has read `HOMEPAGE_DRAFT_REVIEW_AND_APPROVAL_SEQUENCE_V1_0.md` and understands all 10 review steps.

### Operator confirmations

- [ ] **No invention.** The operator confirms no content fields will be invented.
- [ ] **No Phase 0 mutation.** The operator confirms Rise Phase 0 will not be mutated.
- [ ] **No self-approval.** The operator confirms production authorization requires explicit human approval — no self-approval.
- [ ] **Mode declared.** The operator declares Mode 1 (`MODE_1_CURRENT_WEBSITE`) or Mode 2 (`MODE_2_FUTURE_ASTRO_CARRY`). First run is Mode 1.

---

## Hold matrix

The following held field categories apply to the homepage draft. Status is current default — fields may only change status through owner approval.

| Category | Schema properties | Default status | Can be released | Release requirement |
|----------|-------------------|----------------|-----------------|---------------------|
| `phone` | `telephone` | `NOT_REVIEWED_HELD` | Yes | Owner approval + confirmed Phase 0 value |
| `email` | `email` | `NOT_REVIEWED_HELD` | Yes | Owner approval + confirmed Phase 0 value |
| `sameAs` | `sameAs` | `NOT_REVIEWED_HELD` | Yes | Owner approval + confirmed social profile URLs |
| `logoUrl` | `logo`, `image` | `NOT_REVIEWED_HELD` | Yes | Owner approval + confirmed absolute HTTPS logo URL |
| `descriptionFromTagline` | `description` | `NOT_REVIEWED_HELD` | Yes | Owner approval + confirmed factual copy (not tagline or mission line) |
| `coordinates` | `geo`, `latitude`, `longitude` | `NOT_REVIEWED_HELD` | No | Blocked via GeoCoordinates module policy |
| `addressPlaceIdentity` | `address`, `streetAddress`, `addressLocality`, `addressRegion`, `postalCode` | `NOT_REVIEWED_HELD` | No | Blocked via Place module policy |
| `reviews` | `review` | `NOT_REVIEWED_HELD` | No | Blocked via Review module policy |
| `ratings` | `aggregateRating`, `ratingValue`, `ratingCount` | `NOT_REVIEWED_HELD` | No | Blocked via AggregateRating module policy |
| `prices` | `price`, `priceCurrency`, `priceRange` | `NOT_REVIEWED_HELD` | No | Blocked via Offer module policy |
| `eventDates` | `startDate`, `endDate`, `eventSchedule` | `NOT_REVIEWED_HELD` | No | Blocked via Event module policy |
| `offerDetails` | `offers`, `availability` | `NOT_REVIEWED_HELD` | No | Blocked via Offer module policy |
| `testimonialDerivedClaims` | (any field derived from testimonial) | `NOT_REVIEWED_HELD` | No | Blocked category |
| `bilingualAlternateData` | (any bilingual alternate) | `NOT_REVIEWED_HELD` | No | Blocked category |

---

## Owner approval worksheet reference

For fields that `canBeUnblocked: true`, see `03_TRUTH_PACK/RISE_CONTACT_SOCIAL_LOGO_OWNER_APPROVAL_WORKSHEET_V1_0.md` for the owner approval tracking record.

Fields must not change from `NOT_REVIEWED_HELD` to `EMIT` without a matching owner approval entry in that worksheet and a confirmed Phase 0 or page evidence source.

---

## Stop conditions

If any of the following are true at run start, stop immediately:

| Condition | Stop code |
|-----------|-----------|
| Phase 0 source reference is missing | `STOP_MISSING_PHASE0_SOURCE` |
| Homepage truth view JSON is missing or does not parse | `STOP_MISSING_TRUTH_VIEW` |
| Truth fingerprint does not match expected value | `STOP_FINGERPRINT_MISMATCH` |
| Schema profile is not confirmed | `STOP_MISSING_SCHEMA_PROFILE` |
| Evidence map is missing | `STOP_MISSING_EVIDENCE_MAP` |
| Prompt 08 readiness gate did not pass | `STOP_READINESS_GATE_FAIL` |
| Any blocked module appears in planned draft | `STOP_BLOCKED_MODULE_DETECTED` |
| Any held field (non-approved) appears in planned draft | `STOP_HELD_FIELD_VIOLATION` |
| Operator is attempting to self-approve production | `STOP_SELF_APPROVAL_ATTEMPTED` |
| Phase 0 mutation attempted | `STOP_PHASE0_MUTATION_ATTEMPTED` |
