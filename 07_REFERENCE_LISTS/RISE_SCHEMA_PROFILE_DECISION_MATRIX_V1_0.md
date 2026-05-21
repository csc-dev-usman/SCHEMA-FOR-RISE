# Rise Schema Profile Decision Matrix V1.0

**Status:** `HOMEPAGE_SCHEMA_PROFILE_ADDED_NO_SCHEMA_OUTPUT`

---

## Purpose

This document is the schema profile decision matrix for the Rise FC standalone schema operator package. It defines the currently active profile, future profile candidates, what inputs drive profile decisions, and what outputs or hold conditions result from each decision path.

Only `HOMEPAGE_SCHEMA_PROFILE` is documented in PR #4. Future profile candidates are listed but are not active and are not authorized.

---

## Current active profile

| Field | Value |
|-------|-------|
| Profile ID | `HOMEPAGE_SCHEMA_PROFILE` |
| Target page | Homepage |
| Route | `/` |
| Truth fingerprint | `80edd829806cae271242c6a8e853edabdb8b2f16ca5a8fa1a3fc69ff5b78d53d` |
| Allowed future modules | Organization, WebSite, WebPage, BreadcrumbList |
| Blocked modules | FAQPage, Offer, Event, Review, AggregateRating, Place, GeoCoordinates, testimonial-derived, bilingual, advanced |
| Held fields | All 15 held field categories — see `RISE_HELD_FIELD_CATEGORIES_FIRST_PAGE_V1_0.md` |
| Evidence map | NOT_YET_CREATED |
| Operator prompt | NOT_YET_CREATED |
| Validator | NOT_YET_CREATED |
| Schema draft authorized | NO |
| Production authorized | NO |

---

## Future profile candidates

The following profiles are candidates for future PRs. They are not active. They are not authorized. No schema work may begin for these profiles until a governing PR creates the profile document, truth-view reference, evidence map, and other required artifacts.

| Profile ID | Target page | Route | Status |
|-----------|------------|-------|--------|
| `PROGRAM_PAGE_SCHEMA_PROFILE` | Program pages | `/programs/*` | FUTURE_CANDIDATE_NOT_ACTIVE |
| `CAMPS_PAGE_SCHEMA_PROFILE` | Camps page | `/camps` (or similar) | FUTURE_CANDIDATE_NOT_ACTIVE |
| `TRYOUTS_PAGE_SCHEMA_PROFILE` | Tryouts page | `/tryouts` (or similar) | FUTURE_CANDIDATE_NOT_ACTIVE |
| `RISING_STARS_PAGE_SCHEMA_PROFILE` | Rising Stars page | `/rising-stars` (or similar) | FUTURE_CANDIDATE_NOT_ACTIVE |
| `CONTACT_PAGE_SCHEMA_PROFILE` | Contact page | `/contact` (or similar) | FUTURE_CANDIDATE_NOT_ACTIVE |
| `FIELD_LOCATION_PAGE_SCHEMA_PROFILE` | Field/location pages | `/locations/*` (or similar) | FUTURE_CANDIDATE_NOT_ACTIVE |
| `LEARNING_CENTER_ARTICLE_SCHEMA_PROFILE` | Learning center articles | `/learn/*` (or similar) | FUTURE_CANDIDATE_NOT_ACTIVE |

Route patterns above are illustrative. Actual routes must be confirmed from Phase 0 or Astro route manifest before a profile is created.

---

## Decision inputs

When an operator or prompt reaches the profile selection step, the following inputs drive the decision:

| Input | How it affects the decision |
|-------|---------------------------|
| Target page / route | Determines which profile applies. Unknown routes must hold. |
| Truth fingerprint verification | Must match the locked fingerprint for the target profile. Mismatch = HOLD. |
| Evidence map availability | Must exist for the target profile. Missing = HOLD. |
| Operator prompt availability | Must exist for the target profile. Missing = HOLD. |
| Held field status | Any held field requested without owner approval = omit. |
| Blocked module request | Any blocked module requested = reject. |
| Phase 0 / page evidence conflict | Any conflict = HOLD, escalate upstream. |
| Validator availability | Must exist before output is produced. Missing = HOLD. |
| Controller authorization | Must exist before production output. Missing = HOLD. |

---

## Decision outputs

| Outcome | Condition |
|---------|-----------|
| `PROCEED_TO_EVIDENCE_MAP` | Profile exists, fingerprint verified, evidence map exists, prompt exists — operator may proceed to evidence confirmation step |
| `PROCEED_TO_DRAFT` | All gates above plus validator available and no held/blocked issues — operator may proceed to schema draft |
| `PROCEED_TO_VALIDATION` | Draft produced, validator available — operator may proceed to validation |
| `PROCEED_TO_CONTROLLER_REVIEW` | Validation passing, no held/blocked issues — operator may submit to controller for review |
| `HOLD_MISSING_EVIDENCE_MAP` | Evidence map does not exist for this profile |
| `HOLD_MISSING_OPERATOR_PROMPT` | Operator prompt does not exist for this profile |
| `HOLD_FINGERPRINT_MISMATCH` | Fingerprint does not match locked value |
| `HOLD_HELD_FIELD_REQUESTED` | A held field was requested — omit field and continue, or hold if field is required for the module |
| `HOLD_BLOCKED_MODULE_REQUESTED` | A blocked module was requested — reject and hold |
| `HOLD_PHASE0_CONFLICT` | Phase 0 and page evidence conflict — escalate upstream |
| `HOLD_NO_VALIDATOR` | Validator does not exist yet |
| `HOLD_NO_CONTROLLER_AUTH` | Controller authorization not yet granted |
| `HOLD_UNKNOWN_ROUTE` | Target route is not confirmed in any active profile |

---

## Hold outcomes

Any `HOLD_*` outcome means:
- Schema generation does not proceed for the affected scope.
- The hold condition must be resolved through the appropriate upstream process (truth-pack update PR, doctrine PR, owner approval, evidence map creation).
- Holds are not resolved by estimation, inference, or workaround.

---

## Non-authorization

This matrix is a decision reference only. It does not generate schema. It does not authorize JSON-LD output. It does not authorize current website implementation or Astro attachment.

---

## Next matrix expansion

The matrix will be expanded in future PRs as:
- New page profiles are created
- Evidence maps are added for each profile
- Operator prompts are added for each profile
- New routes are confirmed from Phase 0 or Astro route manifest
