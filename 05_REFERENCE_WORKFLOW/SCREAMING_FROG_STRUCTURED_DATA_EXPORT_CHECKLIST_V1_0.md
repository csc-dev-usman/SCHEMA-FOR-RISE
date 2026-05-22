# Screaming Frog Structured Data Export Checklist V1.0

**Status:** `FINAL_VALIDATION_PROTOCOL_ADDED_NO_SCHEMA_OUTPUT`

> This checklist defines how to use Screaming Frog to extract and review structured data from the Rise FC website as part of Step 6 of the Final Schema Validation Protocol. This step is optional and where available — it does not block Step 7 if Screaming Frog is unavailable or the target page is not yet crawlable. This is a documentation contract only — no crawls have been run, no data has been exported, and no results exist. Validation does not authorize production by itself. Human approval is required before any implementation handoff.

---

## Purpose

This checklist provides instructions for using Screaming Frog SEO Spider to extract structured data from the Rise FC website as part of Step 6 of `FINAL_SCHEMA_VALIDATION_PROTOCOL_V1_0.md`. It defines what to configure, what to export, how to review the results, and when this step is `N/A`.

---

## Tool

**Screaming Frog SEO Spider**
Website: https://www.screamingfrog.co.uk/seo-spider/

Screaming Frog is a desktop application that crawls websites and extracts on-page data including structured data. It can export JSON-LD, Microdata, and RDFa structured data found on any crawled URL.

**This step is optional and where available.** It requires:
- Screaming Frog SEO Spider to be installed
- The target page to be publicly accessible or crawlable in a staging environment

If Screaming Frog is not installed, or if the target page is not yet crawlable (pre-implementation), mark this step as `N/A` in `validator_results.json` and proceed to Step 7.

---

## When to use this checklist

This checklist applies in two scenarios:

### Scenario A — Pre-implementation review

Before the emitted schema is attached to the current website, Screaming Frog can be used to verify what schema is currently on the target page. This is useful for:
- Confirming the current page has no conflicting schema
- Documenting the baseline schema state before implementation

### Scenario B — Post-implementation verification

After the emitted schema is attached to the current website, Screaming Frog can be used to verify that:
- The correct schema types are present on the page
- No blocked modules are present in the live page
- The emitted schema matches the approved `emitted_schema.jsonld`

Post-implementation use is the primary use case for this checklist.

---

## Pre-conditions

Before running a Screaming Frog crawl:

- [ ] Screaming Frog SEO Spider is installed
- [ ] The target page URL is confirmed (`https://www.risefcsoccer.com/` for homepage)
- [ ] A crawl license is available (or free mode is sufficient for single-URL crawl — free mode crawls up to 500 URLs)

If any pre-condition is not met, mark Step 6 as `N/A` and proceed to Step 7.

---

## Configuration

### Single-URL crawl (recommended for homepage)

1. Open Screaming Frog SEO Spider
2. In the URL field, enter the target URL: `https://www.risefcsoccer.com/`
3. Set crawl mode: **List mode** (crawl a specific list of URLs) for single-page validation
   - Go to Mode → List
   - Upload or paste the target URL
4. Click "Start"

### Structured data extraction settings

Before starting the crawl, ensure structured data extraction is enabled:
1. Go to Configuration → Spider → Extraction
2. Ensure "Extract Structured Data" is checked
3. Optionally enable "Store Raw HTML" if full page source is needed

---

## Export steps

After the crawl completes:

1. In the bottom panel, click the "Structured Data" tab
2. Review the structured data found on the target URL
3. Export the structured data:
   - Go to Export → Structured Data (JSON-LD) → All
   - Save as CSV or copy to clipboard
4. Optionally: In the top panel, select the target URL and click "Structured Data" in the right panel to view the full extracted JSON-LD

---

## Review checklist

After exporting structured data, review the following:

### Blocked modules check

None of the following `@type` values should be present in the live page structured data:

- [ ] `FAQPage` — BLOCKED
- [ ] `Question` — BLOCKED
- [ ] `Answer` — BLOCKED
- [ ] `Offer` — BLOCKED
- [ ] `AggregateOffer` — BLOCKED
- [ ] `Event` — BLOCKED
- [ ] `SportsEvent` — BLOCKED
- [ ] `Review` — BLOCKED
- [ ] `AggregateRating` — BLOCKED
- [ ] `Place` — BLOCKED
- [ ] `LocalBusiness` — BLOCKED
- [ ] `GeoCoordinates` — BLOCKED
- [ ] `PostalAddress` — BLOCKED

If any blocked module is found in the live page, this is a blocker. Do not proceed to Step 7 until the blocked module is removed.

### Allowed modules check

Only the following `@type` values should be present in the Rise FC homepage schema (if schema has been implemented):

- [ ] `Organization` — allowed
- [ ] `WebSite` — allowed
- [ ] `WebPage` — allowed
- [ ] `BreadcrumbList` — allowed

Unexpected types not in this list should be investigated and documented.

### Held field check

Review the exported structured data for any held fields that should not be present without owner approval:

- [ ] `telephone` — held
- [ ] `email` — held
- [ ] `sameAs` — held (social URLs)
- [ ] `logo` — held
- [ ] `image` — held (in context of brand logo/identity)
- [ ] `description` — held (tagline/mission-derived)
- [ ] `geo` / `latitude` / `longitude` — held
- [ ] `address` / `streetAddress` / `addressLocality` / `addressRegion` / `postalCode` — held
- [ ] `review` / `aggregateRating` / `ratingValue` / `ratingCount` — held
- [ ] `price` / `priceCurrency` / `priceRange` — held
- [ ] `startDate` / `endDate` / `eventSchedule` — held
- [ ] `offers` / `availability` — held

If any held field is found on the live page without approved owner authorization and confirmed evidence, this is a potential blocker. Document and escalate to the package owner.

### Consistency check

If this is post-implementation:
- [ ] The `@type` values in the Screaming Frog export match the `@type` values in `emitted_schema.jsonld`
- [ ] The `name` values match the approved truth-pack values
- [ ] The `url` values are correct for the target route
- [ ] No extra schema types were introduced by the CMS or template system

---

## Evidence to capture

After reviewing the export:

1. **CSV export or screenshot** of the structured data tab showing all types found
2. **Blocked module check result** — PASS (none found) or FAIL (with details)
3. **Consistency check result** — PASS or deviation notes
4. **Result summary** — overall assessment for Step 6

This evidence must be referenced in `validator_results.json` in the output bundle.

---

## Result documentation

Record the Screaming Frog result in `validator_results.json` using the following shape:

```
{
  "validatorStep": 6,
  "tool": "screaming_frog_seo_spider",
  "toolUrl": "https://www.screamingfrog.co.uk/seo-spider/",
  "targetUrl": "https://www.risefcsoccer.com/",
  "runDate": "<ISO 8601 date | N/A>",
  "available": <true | false>,
  "result": "<PASS | FAIL | N/A>",
  "blockedModulesFound": [],
  "heldFieldsFound": [],
  "typesFound": ["Organization", "WebSite", "WebPage", "BreadcrumbList"],
  "consistencyCheckPassed": <true | false | null>,
  "exportRef": "<reference to export file or screenshot | N/A>",
  "stepPassed": <true | false | null>,
  "notes": ""
}
```

If Screaming Frog is unavailable: set `available: false`, `result: "N/A"`, `stepPassed: null`.

---

## Non-authorization statement

Running a Screaming Frog structured data crawl and obtaining any result:
- Does **not** authorize production deployment
- Does **not** authorize Astro attachment
- Does **not** authorize production lock
- Does **not** replace human approval at Step 8 of the validation protocol

This step is optional and informational. A `N/A` result (Screaming Frog unavailable) does not block the validation protocol. Human approval at Step 8 is required before any implementation handoff regardless of this step's outcome.
