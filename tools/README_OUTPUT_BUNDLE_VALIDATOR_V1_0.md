# Rise FC Output Bundle Validator — V1.0

**Status:** `OUTPUT_BUNDLE_VALIDATOR_ADDED_NO_SCHEMA_OUTPUT`

---

## What this tool is

`tools/validate_output_bundle.py` is a Python standard-library validator for Rise FC schema output bundles.

It checks a future output bundle directory against the governed Rise schema operator rules. It produces a PASS / WARN / FAIL result with reasons.

This tool is part of the Rise FC standalone schema operator package. It enforces the doctrine rules from `02_GOVERNING_DOCTRINE/` and the contract schemas from `06_MACHINE_RULES/`.

---

## What this tool is not

- It is **not** a schema generator.
- It does **not** create JSON-LD.
- It does **not** create or modify output bundles.
- It does **not** approve production deployment.
- It does **not** mutate Phase 0 or any source truth.
- It does **not** replace human review and approval.

---

## Requirements

- Python 3.8 or later
- Python standard library only (no third-party packages required)

---

## Usage

```
python tools/validate_output_bundle.py <BUNDLE_DIR>
python tools/validate_output_bundle.py --help
```

**Example:**

```
python tools/validate_output_bundle.py sample_runs/RUN_001_HOMEPAGE_MODE1
```

**Help output:**

```
python tools/validate_output_bundle.py --help
```

---

## Exit codes

| Code | Result | Meaning |
|------|--------|---------|
| 0 | PASS | All checks passed |
| 1 | FAIL | One or more checks failed — bundle must not be used |
| 2 | WARN | All checks passed but warnings were raised — review before use |

---

## What the validator checks

### 1. Required files present

Verifies that the following required files exist in the bundle directory:

**Required JSON files:**
- `output_bundle_manifest.json`
- `run_metadata.json`
- `evidence_map.json`
- `controller_decision.json`
- `validator_results.json`

**Required doc files:**
- `withheld_schema_report.md`
- `deferred_truth_report.md`

### 2. JSON files parse as valid JSON

All `.json` and `.jsonld` files in the bundle directory must parse as valid JSON.

### 3. Truth fingerprint (homepage only)

If `run_metadata.json` declares `schemaProfile: "HOMEPAGE_SCHEMA_PROFILE"` or `pageRoute: "/"`, the `truthFingerprint` field must match:

```
80edd829806cae271242c6a8e853edabdb8b2f16ca5a8fa1a3fc69ff5b78d53d
```

This fingerprint is locked from PR #3 and must not change without a governing doctrine PR.

### 4. Blocked modules

If `emitted_schema.jsonld` exists, verifies it contains none of the blocked `@type` values:

```
FAQPage, Question, Answer, Offer, AggregateOffer, Event, SportsEvent,
Review, AggregateRating, Place, LocalBusiness, GeoCoordinates, PostalAddress
```

These modules are blocked for the first-page lane. They may not appear in an output bundle without an explicit future doctrine PR authorizing them.

### 5. Held fields without approval

If `emitted_schema.jsonld` exists, checks whether it contains held properties (e.g., `telephone`, `email`, `sameAs`, `logo`, `image`, `description`, `geo`, `address`, `review`, `aggregateRating`, `price`, `offers`, etc.).

If held properties are present, checks `controller_decision.json` for explicit approval metadata (`heldFieldApprovals` or `releasedHeldFields`). Held properties without approval metadata cause a FAIL.

### 6. Production lock

If `output_bundle_manifest.json` has `status: "PRODUCTION_LOCKED"`, verifies that `humanApprovalStatus` is `"GRANTED"`. PRODUCTION_LOCKED without human approval causes a FAIL.

### 7. Safety booleans

Verifies from `output_bundle_manifest.json` that:
- `phase0MutationAllowed` is not `true` (FAIL if true)
- `sourceTruthMutationAllowed` is not `true` (FAIL if true)
- `schemaOutputCreated` and `jsonLdCreated` are consistent with the presence of `emitted_schema.jsonld` (WARN if inconsistent)

---

## What the validator does not check (operator responsibility)

- Whether Phase 0 source truth was correctly read before the run
- Whether the evidence map was built from confirmed page content
- Whether held field approvals were legitimately obtained
- Whether the owner approval chain is real and documented
- Whether schema field values are factually accurate
- Whether the implementation handoff is appropriate for the target environment
- Whether Mode 1 or Mode 2 gates are all satisfied

These items require human operator review. This tool is a machine pre-check only.

---

## Governed by

- `02_GOVERNING_DOCTRINE/RISE_SCHEMA_SOURCE_TRUTH_BOUNDARY_V1_0.md`
- `02_GOVERNING_DOCTRINE/RISE_SCHEMA_GOVERNING_DOCTRINE_V1_0.md`
- `06_MACHINE_RULES/OUTPUT_BUNDLE_VALIDATOR_RULES_V1_0.md`
- `06_MACHINE_RULES/OUTPUT_BUNDLE_VALIDATOR_EXPECTED_FILES_V1_0.json`
- `06_MACHINE_RULES/OUTPUT_BUNDLE_MANIFEST_SCHEMA_V1_0.json`
- `06_MACHINE_RULES/RISE_SCHEMA_LINT_RULES_V1_0.json`

---

## Non-authorization statement

This tool does not authorize schema output, production deployment, or any implementation action. Human review and explicit human approval are required before any validated output bundle may be used for implementation.
