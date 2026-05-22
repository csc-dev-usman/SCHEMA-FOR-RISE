# Google Rich Results Review Runbook V1.0

**Status:** `FINAL_VALIDATION_PROTOCOL_ADDED_NO_SCHEMA_OUTPUT`

> This runbook defines how to use the Google Rich Results Test as part of Step 5 of the Final Schema Validation Protocol. This is a documentation contract only — no tests have been run, no schema has been generated, and no test results exist. Rich results eligibility is not guaranteed. Not all schema types produce rich results. A result of "not eligible" does not block the validation protocol. Validation does not authorize production by itself. Human approval is required before any implementation handoff.

---

## Purpose

This runbook provides instructions for using the Google Rich Results Test (https://search.google.com/test/rich-results) as part of Step 5 of `FINAL_SCHEMA_VALIDATION_PROTOCOL_V1_0.md`. It defines what to test, how to interpret results, what evidence to capture, and what constitutes an informational versus blocking result.

---

## Tool

**Google Rich Results Test**
URL: https://search.google.com/test/rich-results

This tool tests whether a page's structured data is eligible for rich results in Google Search. It checks for:
- Schema types that support rich result features
- Required and recommended properties for rich result eligibility
- Errors that would prevent rich results from appearing
- Warnings that may affect rich result quality

**Important distinction:**
- The Schema.org Validator (Step 4) tests schema validity against the Schema.org specification
- The Google Rich Results Test tests eligibility for Google Search rich result features
- A schema can be Schema.org valid but not eligible for Google rich results
- A schema can be eligible for some rich result features but not others

---

## Rich results eligibility for Rise FC homepage schema

The Rise FC homepage schema profile (`HOMEPAGE_SCHEMA_PROFILE`) allows the following modules:
- `Organization`
- `WebSite`
- `WebPage`
- `BreadcrumbList`

### Rich results applicability by module

| Module | Rich results eligibility | Notes |
|--------|------------------------|-------|
| `Organization` | No dedicated rich result | Organization schema supports Knowledge Panel features in some cases, but has no dedicated rich result type. A result of "not eligible" is expected and normal. |
| `WebSite` | Sitelinks Searchbox (conditional) | WebSite schema with `SearchAction` may enable a sitelinks searchbox in Google Search. Eligibility depends on Google's discretion and site authority. Not guaranteed. |
| `WebPage` | No dedicated rich result | WebPage schema has no dedicated rich result feature. A result of "not eligible" is expected and normal. |
| `BreadcrumbList` | Breadcrumb rich result | BreadcrumbList schema may enable breadcrumb display in search results. Eligibility depends on correct `ListItem` nesting and `item`/`name`/`position` properties. |

**Key rule:** A result of "not eligible" for any or all modules does **not block** the validation protocol. Rich results eligibility is informational only. Step 5 is never a blocker unless critical schema errors are discovered through the test.

---

## Pre-conditions

Before running the Google Rich Results Test:

- [ ] Step 1 (output bundle validation) must have passed
- [ ] Step 2 (JSON parse validation) must have passed
- [ ] Step 3 (schema lint rules) must have passed
- [ ] Step 4 (Schema.org Validator) must have passed
- [ ] `emitted_schema.jsonld` must be present in the output bundle

---

## Submission methods

The Google Rich Results Test accepts input in two ways:

### Method A — URL test

1. Open https://search.google.com/test/rich-results
2. Select "URL" tab
3. Enter the target page URL (e.g., `https://www.risefcsoccer.com/`)
4. Click "Test URL"

This method tests what the live page is currently emitting. It requires the page to be publicly accessible and the schema to already be implemented on the page. This is the post-implementation verification method.

### Method B — Code snippet

1. Open https://search.google.com/test/rich-results
2. Select "Code" tab
3. Paste the relevant schema markup
4. Click "Test code"

This method tests the schema directly. It is the pre-implementation validation method. Note that the Google Rich Results Test in code mode tests JSON-LD embedded in an HTML context — you may need to wrap the JSON-LD in a `<script type="application/ld+json">` tag.

---

## Interpreting results

### "Eligible for rich results"

If the tool reports that the page or schema is eligible for a rich result type, this means the schema meets Google's current requirements for that rich result feature.

- Document the eligible rich result type(s) in `validator_results.json`
- Capture a screenshot of the eligibility result
- Note any warnings alongside the eligible result

An eligible result does not guarantee rich result display in Google Search. Google's decision to display rich results depends on additional factors including page authority, crawl status, and user context.

### "Not eligible for rich results"

A result of "not eligible" is normal and expected for most modules in the Rise FC homepage profile. Specifically:
- `Organization` is not expected to be eligible for a dedicated rich result
- `WebPage` is not expected to be eligible for a dedicated rich result
- `WebSite` eligibility for sitelinks searchbox depends on site authority and is not guaranteed

**A "not eligible" result does not block validation.** Document the result in `validator_results.json` with disposition `informational-not-eligible`.

### Errors found

If the Google Rich Results Test identifies errors in the schema that were not caught in Steps 3–4, treat them as potential blockers and evaluate against the Rise FC lint rules and Schema.org specification.

Common errors that may appear:
- Missing required property for a rich result type (e.g., missing `name` for BreadcrumbList `ListItem`)
- Invalid `url` value
- Incorrect nesting

If an error is confirmed against the Schema.org specification (Step 4 cross-reference), it is a blocker. Patch the schema and rerun from Step 1.

If an error is a Google-specific requirement that is not in the Schema.org specification and conflicts with Rise FC held field rules, document it as `deferred-held-field` and do not emit the held field without owner approval.

### Warnings

Warnings in the Google Rich Results Test indicate recommended properties or patterns that may improve rich result quality. Review each warning:

- If the suggested property is supported by Phase 0 evidence and is not held: consider adding it
- If the suggested property is a held field: document as `deferred-held-field` and do not add without owner approval
- If the suggested property is in a blocked module: document as `blocked-module` and do not add

---

## Evidence to capture

After running the Google Rich Results Test, capture the following evidence:

1. **Screenshot** of the full test result page — showing eligibility status and any errors or warnings
2. **Eligibility result per module** — which modules were tested and their eligibility status
3. **Error list** (if any) — each error with field path and disposition
4. **Warning list** (if any) — each warning with field path and disposition
5. **Result summary** — overall assessment for Step 5

This evidence must be referenced in `validator_results.json` in the output bundle.

---

## Result documentation

Record the Google Rich Results Test result in `validator_results.json` using the following shape:

```
{
  "validatorStep": 5,
  "tool": "google_rich_results_test",
  "toolUrl": "https://search.google.com/test/rich-results",
  "submissionMethod": "<url | code_snippet>",
  "runDate": "<ISO 8601 date>",
  "result": "<ELIGIBLE | NOT_ELIGIBLE | ELIGIBLE_WITH_WARNINGS | NOT_APPLICABLE>",
  "modulesTestedWithEligibility": [
    { "module": "Organization", "eligible": false, "disposition": "informational-not-eligible" },
    { "module": "WebSite", "eligible": false, "disposition": "informational-not-eligible" },
    { "module": "WebPage", "eligible": false, "disposition": "informational-not-eligible" },
    { "module": "BreadcrumbList", "eligible": true, "disposition": "eligible" }
  ],
  "errorCount": <integer>,
  "warningCount": <integer>,
  "stepBlocked": false,
  "screenshotRef": "<reference to screenshot file or path>",
  "stepPassed": true
}
```

Note: `stepPassed` should be `true` for Step 5 in all cases except where a confirmed Schema.org-specification error is discovered that was missed in Steps 3–4.

---

## Non-authorization statement

Running the Google Rich Results Test and obtaining any result:
- Does **not** authorize production deployment
- Does **not** authorize Astro attachment
- Does **not** authorize production lock
- Does **not** replace human approval at Step 8 of the validation protocol
- Does **not** guarantee rich result display in Google Search

Rich results eligibility is informational. It does not determine whether the schema is valid, whether it may be implemented, or whether it will appear in Google Search. A schema may be fully valid and correctly implemented without producing any rich results.

Human approval at Step 8 is required before any implementation handoff regardless of rich results eligibility outcome.
