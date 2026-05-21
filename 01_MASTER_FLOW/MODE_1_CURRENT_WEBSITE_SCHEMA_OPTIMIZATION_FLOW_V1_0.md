# Mode 1 — Current Website Schema Optimization Flow V1.0

**Status:** `MASTER_FLOW_ADDED_NO_SCHEMA_OUTPUT`

---

## Purpose

This document defines the Mode 1 current-website schema optimization flow for the Rise FC standalone schema operator package. Mode 1 produces validated schema for pages on the current risefcsoccer.com website.

**Mode 1 is documented but not runnable yet.** Operator prompts, evidence maps, validators, and the final runnable handoff are pending in later PRs.

---

## Mode 1 goal

Produce validated, non-production JSON-LD schema for pages on the current risefcsoccer.com website, using approved Phase 0 content and confirmed page evidence, ready for human-reviewed implementation handoff.

---

## Mode 1 inputs

| Input | Requirement |
|-------|-------------|
| Target URL | Confirmed current-site URL |
| Phase 0 source reference | Must exist for target page |
| Scoped truth view | Must exist for target page |
| Truth fingerprint | Must match locked value for target profile |
| Schema profile | Must be active for target route (e.g., `HOMEPAGE_SCHEMA_PROFILE` for `/`) |
| Evidence map | Must exist for target profile |
| Blocked module policy | Must be verified — no blocked modules |
| Held field policy | Must be verified — all held fields omitted unless owner-approved |
| Page content readiness | Must pass readiness gate |

---

## Mode 1 flow sequence

```
INTAKE
  ├── Confirm target URL
  ├── Confirm route matches an active schema profile
  └── Confirm Mode 1 (current website, not Astro)

TRUTH CONFIRMATION
  ├── Locate Phase 0 source reference for target page
  ├── Locate or derive scoped truth view
  ├── Verify truth fingerprint matches locked value
  └── HOLD if any truth artifact is missing or mismatched

PROFILE CONFIRMATION
  ├── Identify active schema profile for target route
  ├── Verify allowed modules list (homepage: Organization, WebSite, WebPage, BreadcrumbList)
  ├── Verify blocked modules list (homepage: FAQPage, Offer, Event, Review, etc.)
  └── HOLD if profile does not exist for target route

BLOCK AND HOLD CONFIRMATION
  ├── Confirm no blocked modules requested
  ├── Confirm held fields will be omitted (not estimated, not inferred)
  └── REJECT if blocked module is requested

READINESS GATE (Prompt 08 — future)
  ├── Confirm page content is ready for schema derivation
  ├── Confirm all content fields trace to Phase 0 or page evidence
  └── HOLD if readiness gate fails

EVIDENCE MAP (future artifact)
  ├── Confirm evidence map exists for target profile
  ├── Confirm every field to be emitted is linked to its evidence source
  └── HOLD if evidence map is missing or incomplete

DRAFT (Prompt 01 — future)
  ├── Produce non-production JSON-LD draft
  ├── Apply allowed modules only
  ├── Omit all held fields
  ├── Exclude all blocked modules
  └── Mark output as NON_PRODUCTION

EXTERNAL QA (Prompt 02 — future)
  ├── Create QA one-zip with draft
  ├── Claude reviews draft
  └── QA output is advisory — not source truth

CONTROLLER DECISION (Prompt 03 — future)
  ├── Controller reviews QA output
  ├── Decision: ACCEPT / MODIFY / REJECT / DEFER / HUMAN_REVIEW_REQUIRED
  └── HOLD if controller does not ACCEPT

VALIDATION (Prompt 04 — future)
  ├── Run Schema.org validation
  ├── Run Google Rich Results validation where applicable
  ├── Run Screaming Frog where available
  └── HOLD if validation fails

ANALYZER REVIEW (Prompt 13 — future)
  ├── Independent analyzer reviews validated draft
  ├── Analyzer must not mutate source truth
  └── HOLD if analyzer raises new block conditions

CONTROLLER POST-ANALYZER DECISION (Prompt 14 — future)
  ├── Controller reviews analyzer output
  ├── Decision: ACCEPT / MODIFY / REJECT / DEFER / HUMAN_REVIEW_REQUIRED / PATCH_REQUIRED
  └── HOLD if controller does not ACCEPT

HUMAN APPROVAL
  ├── Human owner reviews and approves implementation handoff
  └── STOP if human has not explicitly approved

IMPLEMENTATION HANDOFF
  ├── Produce implementation packet for current website
  ├── Operator hands off to HTML/runtime lane
  └── No self-deployment
```

---

## Mode 1 outputs

| Output | Status |
|--------|--------|
| Non-production JSON-LD draft | Future — not created in this PR |
| Validated schema bundle | Future — not created in this PR |
| Implementation handoff packet | Future — not created in this PR |
| Run ledger entry | Future — not created in this PR |

---

## Mode 1 stop conditions

| Condition | Action |
|-----------|--------|
| Phase 0 source reference missing | HOLD — do not proceed |
| Truth fingerprint mismatch | HOLD — do not proceed |
| No active profile for target route | HOLD — do not proceed |
| Blocked module requested | REJECT — do not include |
| Held field requested without approval | OMIT — do not estimate |
| Readiness gate failed | HOLD — do not draft |
| Evidence map missing | HOLD — do not draft |
| Controller did not ACCEPT | HOLD — do not proceed to validation |
| Validation failed | HOLD — do not proceed to handoff |
| Human approval not granted | STOP — do not implement |

---

## Mode 1 not-runnable statement

**Mode 1 is not runnable after PR #5.**

The following artifacts are still required:
- Operator prompts (PR #7 and PR #8)
- Homepage evidence map (future PR)
- Output bundle contract schemas (PR #9)
- Homepage non-production draft contract (PR #10)
- Validator (future PR)
- Final runnable handoff (future PR)

No schema output may be produced until all of the above exist and are approved.

---

## Non-authorization

This document does not authorize JSON-LD creation. It does not authorize schema output. It does not authorize current website implementation or Astro attachment.
