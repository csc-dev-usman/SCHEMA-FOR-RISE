# Rise FC Output Bundle Validator Rules — V1.0

**Status:** `OUTPUT_BUNDLE_VALIDATOR_ADDED_NO_SCHEMA_OUTPUT`

---

## Purpose

This document defines the validation rules enforced by `tools/validate_output_bundle.py` for Rise FC schema output bundles.

These rules are derived from the governing doctrine in `02_GOVERNING_DOCTRINE/`, the contract schemas in `06_MACHINE_RULES/`, and the homepage schema profile in `07_REFERENCE_LISTS/`.

---

## Rule set

### RULE_VAL_001 — Required files

**Check:** All required files must be present in the output bundle directory.

**Required JSON files:**
- `output_bundle_manifest.json`
- `run_metadata.json`
- `evidence_map.json`
- `controller_decision.json`
- `validator_results.json`

**Required doc files:**
- `withheld_schema_report.md`
- `deferred_truth_report.md`

**Conditional files (if applicable):**
- `emitted_schema.jsonld` — required when `jsonLdCreated: true`
- `implementation_handoff.md` — required when `currentWebsiteImplementationAuthorized: true`

**Failure action:** FAIL — bundle must not be used until all required files are present.

---

### RULE_VAL_002 — JSON validity

**Check:** All `.json` and `.jsonld` files in the bundle directory must parse as valid JSON.

**Failure action:** FAIL — a bundle with invalid JSON cannot be trusted for review or implementation.

---

### RULE_VAL_003 — Truth fingerprint (homepage)

**Check:** When `run_metadata.json` declares `schemaProfile: "HOMEPAGE_SCHEMA_PROFILE"` or `pageRoute: "/"`, the `truthFingerprint` field must equal the locked homepage truth fingerprint.

**Expected fingerprint:**
```
80edd829806cae271242c6a8e853edabdb8b2f16ca5a8fa1a3fc69ff5b78d53d
```

**Fingerprint source:** Locked in PR #3 from `03_TRUTH_PACK/RISE_HOMEPAGE_TRUTH_FINGERPRINT_LOCK_V1_0.md`.

**Failure action:** FAIL — a mismatched fingerprint means the bundle was not derived from the correct Phase 0 source truth snapshot. The bundle must not be used.

---

### RULE_VAL_004 — Blocked modules

**Check:** If `emitted_schema.jsonld` is present, it must contain no `@type` values from the blocked module list.

**Blocked `@type` values (first-page lane):**

| Module | Block reason |
|--------|-------------|
| FAQPage | Not authorized for first page |
| Question | FAQPage child — blocked |
| Answer | FAQPage child — blocked |
| Offer | Not authorized for first page |
| AggregateOffer | Not authorized for first page |
| Event | Not authorized for first page |
| SportsEvent | Event variant — blocked |
| Review | Not authorized for first page |
| AggregateRating | Not authorized for first page |
| Place | Not authorized for first page |
| LocalBusiness | Place variant — blocked |
| GeoCoordinates | Not authorized for first page |
| PostalAddress | Not authorized for first page |

These modules are blocked by `07_REFERENCE_LISTS/RISE_BLOCKED_SCHEMA_MODULES_FIRST_PAGE_V1_0.md` and `07_REFERENCE_LISTS/RISE_HOMEPAGE_SCHEMA_PROFILE_V1_0.md`. A future governing doctrine PR is required to authorize any of them.

**Failure action:** FAIL — no blocked module may appear in an output bundle.

---

### RULE_VAL_005 — Held fields

**Check:** If `emitted_schema.jsonld` is present, all held properties must have explicit approval metadata in `controller_decision.json`.

**Held property categories and examples:**

| Category | Example properties |
|----------|--------------------|
| phone | `telephone` |
| email | `email` |
| sameAs/social | `sameAs` |
| logo URL | `logo`, `image` |
| schema description | `description` |
| coordinates | `geo`, `latitude`, `longitude` |
| address/place | `address`, `streetAddress`, `addressLocality`, `addressRegion`, `postalCode` |
| reviews | `review`, `aggregateRating`, `ratingValue`, `ratingCount` |
| prices | `price`, `priceCurrency`, `priceRange` |
| event dates | `startDate`, `endDate`, `eventSchedule` |
| offer details | `offers`, `availability` |

Held fields may not be emitted in a schema output bundle without:
1. Owner approval documented in `03_TRUTH_PACK/RISE_CONTACT_SOCIAL_LOGO_OWNER_APPROVAL_WORKSHEET_V1_0.md`
2. Supporting Phase 0 or page evidence in the evidence map
3. Controller decision approval metadata in `controller_decision.json`

**Failure action:** FAIL for unapproved held fields. WARN when approved fields are present (operator must independently verify approval chain).

---

### RULE_VAL_006 — Production lock

**Check:** `output_bundle_manifest.json` with `status: "PRODUCTION_LOCKED"` must also have `humanApprovalStatus: "GRANTED"`.

**Failure action:** FAIL — PRODUCTION_LOCKED without explicit human approval is not permitted under the governing doctrine. Human review is required before any production lock is valid.

---

### RULE_VAL_007 — Safety booleans

**Check:** The following safety booleans in `output_bundle_manifest.json` must be consistent:

| Field | Allowed value | Failure |
|-------|--------------|---------|
| `phase0MutationAllowed` | Must not be `true` | FAIL |
| `sourceTruthMutationAllowed` | Must not be `true` | FAIL |
| `schemaOutputCreated` | Must be consistent with presence of `emitted_schema.jsonld` | WARN |
| `jsonLdCreated` | Must be consistent with presence of `emitted_schema.jsonld` | WARN |

**Failure action:** FAIL for Phase 0 / source truth mutation flags. WARN for schema/JSON-LD presence inconsistencies.

---

## Checks not performed by this validator (operator responsibility)

The following items are not machine-checkable by this validator. Operators must verify them manually:

1. Whether Phase 0 source truth was correctly read before the run (not mutated, not paraphrased)
2. Whether the evidence map was built from confirmed page content
3. Whether held field approvals were legitimately obtained from the content owner
4. Whether schema field values are factually accurate against Phase 0 and page evidence
5. Whether the implementation handoff is appropriate for the target environment
6. Whether Mode 1 or Mode 2 preconditions are all satisfied
7. Whether the controller decision was made correctly
8. Whether the independent analyzer review (Prompt 13/14) was completed

---

## Non-authorization statement

This validator does not authorize schema output, production deployment, or any implementation action. A PASS result from this validator is a necessary but not sufficient condition for use. Human review and explicit human approval are required.

---

## File references

| File | Role |
|------|------|
| `tools/validate_output_bundle.py` | Validator implementation |
| `tools/README_OUTPUT_BUNDLE_VALIDATOR_V1_0.md` | Operator-facing README |
| `06_MACHINE_RULES/OUTPUT_BUNDLE_VALIDATOR_EXPECTED_FILES_V1_0.json` | Machine-readable expected file list |
| `06_MACHINE_RULES/OUTPUT_BUNDLE_MANIFEST_SCHEMA_V1_0.json` | Output bundle manifest contract schema |
| `06_MACHINE_RULES/RISE_SCHEMA_LINT_RULES_V1_0.json` | Lint rules cross-reference |
| `07_REFERENCE_LISTS/RISE_BLOCKED_SCHEMA_MODULES_FIRST_PAGE_V1_0.md` | Blocked module policy |
| `07_REFERENCE_LISTS/RISE_HELD_FIELD_CATEGORIES_FIRST_PAGE_V1_0.md` | Held field categories |
| `03_TRUTH_PACK/RISE_HOMEPAGE_TRUTH_FINGERPRINT_LOCK_V1_0.md` | Homepage fingerprint lock |
