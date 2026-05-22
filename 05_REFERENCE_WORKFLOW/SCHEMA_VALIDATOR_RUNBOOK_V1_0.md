# Schema Validator Runbook V1.0

**Status:** `FINAL_VALIDATION_PROTOCOL_ADDED_NO_SCHEMA_OUTPUT`

> This runbook defines how to use the Schema.org Structured Data Validator for future governed Rise FC schema output bundles. This is a documentation contract only — no validators have been run, no schema has been generated, and no validator results exist. Validation does not authorize production by itself. Human approval is required before any implementation handoff.

---

## Purpose

This runbook provides step-by-step instructions for using the Schema.org Validator (https://validator.schema.org) as part of Step 4 of the Final Schema Validation Protocol (`FINAL_SCHEMA_VALIDATION_PROTOCOL_V1_0.md`). It defines what to submit, what to look for, what to document, and what constitutes a blocking versus non-blocking result.

---

## Tool

**Schema.org Structured Data Validator**
URL: https://validator.schema.org

This tool validates structured data markup against Schema.org vocabulary definitions. It checks for:
- Valid `@type` values
- Required and recommended properties per type
- Invalid property values or incorrect value types
- Nesting and relationship errors
- `@context` validity

This is a different tool from the Google Rich Results Test. The Schema.org Validator tests schema validity against the Schema.org specification. The Google Rich Results Test tests eligibility for rich results in Google Search — see `GOOGLE_RICH_RESULTS_REVIEW_RUNBOOK_V1_0.md` for that.

---

## Pre-conditions

Before running the Schema.org Validator:

- [ ] Step 1 (output bundle validation) must have passed
- [ ] Step 2 (JSON parse validation) must have passed
- [ ] Step 3 (schema lint rules) must have passed
- [ ] `emitted_schema.jsonld` must be present in the output bundle
- [ ] `emitted_schema.jsonld` must parse as valid JSON-LD

---

## Submission methods

The Schema.org Validator accepts input in three ways:

### Method A — Code snippet (paste directly)

1. Open https://validator.schema.org
2. Select the "Code Snippet" tab
3. Paste the full contents of `emitted_schema.jsonld`
4. Click "Run test"

This is the recommended method for governed schema bundles because it tests the exact emitted schema without page-rendering dependencies.

### Method B — URL fetch

1. Open https://validator.schema.org
2. Select the "Fetch URL" tab
3. Enter the target page URL (e.g., `https://www.risefcsoccer.com/`)
4. Click "Run test"

This method tests what the live page is currently emitting. Useful for post-implementation verification. Not applicable pre-implementation.

### Method C — File upload (if available)

Some versions of the validator support file upload. If available, upload `emitted_schema.jsonld` directly.

---

## What to look for

### Errors (blocking)

Errors indicate schema that does not conform to the Schema.org specification. Common blocking errors:

| Error type | Description | Action |
|-----------|-------------|--------|
| Unknown type | `@type` value is not a valid Schema.org type | Patch schema — remove or correct the type |
| Invalid property | Property does not exist on the declared type | Patch schema — remove or correct the property |
| Invalid value type | Property value is the wrong type (e.g., string where URL expected) | Patch schema — correct the value type |
| Missing required property | A required property for a type is absent | Add the missing property or remove the type |
| Nesting error | Schema entities are incorrectly nested | Correct the nesting structure |

**Stop condition:** Any error is a blocker. Do not proceed to Step 5 until all errors are resolved. Patch the schema, rerun Steps 1–3, then resubmit to the Schema.org Validator.

### Warnings (non-blocking — review required)

Warnings indicate recommended properties that are missing or schema patterns that are suboptimal but not invalid.

| Warning type | Action |
|-------------|--------|
| Missing recommended property | Review against evidence map — add if evidence supports it; document as held if evidence is missing |
| Deprecated property | Review — replace with current property or document as deferred |
| Pattern suggestion | Review — implement if supported by evidence; document disposition |

**All warnings must be reviewed and documented in `validator_results.json` with a disposition:** `resolved`, `deferred`, or `accepted-as-is`.

### Informational messages

Informational messages do not require action but should be noted in `validator_results.json`.

---

## Evidence to capture

After running the Schema.org Validator, capture the following evidence:

1. **Screenshot** of the full validator result page — showing all errors, warnings, and the schema types validated
2. **Error list** — enumerate each error with its field path and the action taken to resolve it
3. **Warning list** — enumerate each warning with its field path and the disposition (`resolved`, `deferred`, `accepted-as-is`)
4. **Result summary** — overall pass/fail determination for Step 4

This evidence must be referenced in `validator_results.json` in the output bundle.

---

## Result documentation

Record the Schema.org Validator result in `validator_results.json` using the following shape:

```
{
  "validatorStep": 4,
  "tool": "schema_org_validator",
  "toolUrl": "https://validator.schema.org",
  "submissionMethod": "<code_snippet | url_fetch>",
  "runDate": "<ISO 8601 date>",
  "result": "<PASS | FAIL | PASS_WITH_WARNINGS>",
  "errorCount": <integer>,
  "warningCount": <integer>,
  "errors": [...],
  "warnings": [...],
  "screenshotRef": "<reference to screenshot file or path>",
  "stepPassed": <true | false>
}
```

---

## What the Schema.org Validator does not check

The Schema.org Validator does not check:

- **Rise FC-specific blocked modules** — Use the lint rules (Step 3) for that
- **Held field policy** — The validator does not know Rise FC's held field categories
- **Truth fingerprint** — The validator has no access to Phase 0 truth
- **Google rich results eligibility** — Use the Google Rich Results Test (Step 5) for that
- **Live page rendering** — Code snippet mode tests the literal schema, not what a browser renders

---

## Non-authorization statement

Running the Schema.org Validator and obtaining a PASS result:
- Does **not** authorize production deployment
- Does **not** authorize Astro attachment
- Does **not** authorize production lock
- Does **not** replace human approval at Step 8 of the validation protocol
- Does **not** replace the output bundle validator (Step 1) or lint rules (Step 3)

A Schema.org Validator PASS result is one of nine required steps in the full validation protocol. All nine steps must be completed and human approval must be obtained before any implementation handoff.
