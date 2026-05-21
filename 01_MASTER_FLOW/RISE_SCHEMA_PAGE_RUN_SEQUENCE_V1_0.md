# Rise Schema Page Run Sequence V1.0

**Status:** `MASTER_FLOW_ADDED_NO_SCHEMA_OUTPUT`

---

## Purpose

This document defines the per-page run sequence for the Rise FC standalone schema operator package. The run sequence covers every step from intake through implementation or Astro handoff. No step may be skipped. No step may be reordered.

This is documentation only. No schema output is produced by reading this document. The run sequence is not yet executable — operator prompts, evidence maps, validators, and the final runnable handoff are pending in later PRs.

---

## Full page run sequence

### Step 1 — Intake

**Goal:** Identify and confirm the target page and operating mode.

| Check | Requirement |
|-------|-------------|
| Target URL | Confirmed current-site or Astro route |
| Target route | Must match an active schema profile |
| Page family | Confirm page type (homepage, program, camps, etc.) |
| Operating mode | Mode 1 (current website) or Mode 2 (future Astro) |
| Session goal | Brief statement of what this run aims to produce |

**Hold conditions:**
- Unknown route → `HOLD_UNKNOWN_ROUTE`
- No active profile for route → `HOLD_MISSING_PROFILE`
- Mode 2 requested without Astro carry gates → `STOP_PREMATURE_ASTRO_ATTACHMENT`

---

### Step 2 — Truth confirmation

**Goal:** Verify Phase 0 source truth and fingerprint before any schema work begins.

| Check | Requirement |
|-------|-------------|
| Phase 0 source reference | Must exist for target page |
| Scoped truth view | Must exist for target page — not invented |
| Truth fingerprint | Must match locked value for target profile |
| Truth freshness | Fingerprint must be current — stale truth triggers hold |

**Hold conditions:**
- Phase 0 source reference missing → `HOLD_MISSING_PHASE0_SOURCE`
- Scoped truth view missing → `HOLD_MISSING_TRUTH_VIEW`
- Fingerprint mismatch → `HOLD_FINGERPRINT_MISMATCH`
- Stale truth → `HOLD_STALE_TRUTH`

---

### Step 3 — Profile confirmation

**Goal:** Confirm the active schema profile and its module/field constraints.

| Check | Requirement |
|-------|-------------|
| Active schema profile | Must exist for target route |
| Allowed modules | Organization, WebSite, WebPage, BreadcrumbList (homepage) |
| Blocked modules | FAQPage, Offer, Event, Review, AggregateRating, Place, GeoCoordinates, testimonial-derived, bilingual, advanced |
| Held field categories | All 15 held field categories must be verified |
| Decision matrix | Run profile decision matrix to confirm PROCEED or HOLD outcome |

**Hold conditions:**
- No profile for target route → `HOLD_MISSING_PROFILE`
- Blocked module requested → `HOLD_BLOCKED_MODULE_REQUESTED`
- Held field requested without approval → `HOLD_HELD_FIELD_REQUESTED`

---

### Step 4 — Block and hold confirmation

**Goal:** Final explicit check before readiness gate — confirm no blocked or held violations.

| Check | Requirement |
|-------|-------------|
| Blocked module sweep | Confirm zero blocked modules in scope |
| Held field sweep | Confirm all held fields are omitted unless owner-approved |
| Owner approval worksheet | Confirm which fields are approved vs. held |

**Action:** If any blocked module is in scope → reject immediately. If any unapproved held field would be emitted → omit it. Do not estimate or infer.

---

### Step 5 — Readiness gate

**Goal:** Confirm page content is ready for schema derivation before any draft begins.

| Check | Requirement |
|-------|-------------|
| Page content confirmed | Target page content confirmed from Phase 0 or page evidence |
| All fields traceable | Every candidate field traces to Phase 0 or confirmed page evidence |
| No guessed fields | No fields inferred from page type, template, or competitor |

**Prompt:** `PROMPT_08_PAGE_CONTENT_READINESS_GATE_V1_0.txt` (future — PR #7)

**Hold conditions:**
- Page content not confirmed → `HOLD_READINESS_GATE_FAILED`
- Fields not traceable → `HOLD_MISSING_EVIDENCE`

---

### Step 6 — Evidence map

**Goal:** Confirm field-level evidence map exists before drafting.

| Check | Requirement |
|-------|-------------|
| Evidence map exists | Must exist for target profile |
| Field-level coverage | Every candidate field has a source reference |
| Conflict check | No conflict between Phase 0 and page evidence |
| Held field status | All held fields marked as omitted in evidence map |

**Hold conditions:**
- Evidence map missing → `HOLD_MISSING_EVIDENCE_MAP`
- Field-level gaps → `HOLD_MISSING_EVIDENCE`
- Phase 0 / page evidence conflict → `HOLD_PHASE0_CONFLICT`

---

### Step 7 — Draft

**Goal:** Produce a non-production JSON-LD draft from the evidence map.

| Check | Requirement |
|-------|-------------|
| Allowed modules only | Only Organization, WebSite, WebPage, BreadcrumbList (homepage) |
| Held fields omitted | No held fields emitted |
| Blocked modules excluded | No blocked modules present |
| Non-production marker | Draft must be marked `NON_PRODUCTION` |
| No invented fields | Every field traces to evidence map source |

**Prompt:** `PROMPT_01_BUILD_NON_PRODUCTION_JSONLD_DRAFT_V1_0.txt` (future — PR #7)

---

### Step 8 — External QA

**Goal:** External Claude QA review of the non-production draft.

| Check | Requirement |
|-------|-------------|
| QA one-zip | Draft packaged for Claude QA review |
| QA output | Advisory only — not source truth |
| Corrections | Only corrections with Phase 0 backing are accepted |

**Prompt:** `PROMPT_02_CLAUDE_EXTERNAL_QA_ONE_ZIP_V1_0.txt` (future — PR #7)

---

### Step 9 — Controller decision

**Goal:** Controller reviews QA output and decides whether to proceed.

| Decision | Meaning |
|----------|---------|
| `ACCEPT` | Proceed to validation |
| `MODIFY` | Return to draft with controller notes |
| `REJECT` | Do not proceed — flag issues |
| `DEFER` | Pause — flag for future run |
| `HUMAN_REVIEW_REQUIRED` | Escalate to human owner |

**Prompt:** `PROMPT_03_CONTROLLER_DECISION_AND_REGENERATION_V1_0.txt` (future — PR #7)

**Hold condition:** No schema proceeds to validation without `ACCEPT`.

---

### Step 10 — Validation

**Goal:** Run schema validation protocols against the draft.

| Validation | Requirement |
|------------|-------------|
| Schema.org structured data | Must pass |
| Google Rich Results | Where applicable — must pass |
| Screaming Frog | Where available |
| Output | Pass / Warn / Fail per field |

**Prompt:** `PROMPT_04_VALIDATOR_RESULTS_REVIEW_V1_0.txt` (future — PR #7)

**Hold condition:** Implementation does not proceed if validation fails.

---

### Step 11 — Independent analyzer review

**Goal:** Independent analyzer reviews the validated draft.

| Check | Requirement |
|-------|-------------|
| Analyzer independence | Analyzer has not seen the draft session |
| Mutation prohibition | Analyzer must not mutate source truth |
| Hold conditions | Analyzer raises new block conditions → HOLD |

**Prompt:** `PROMPT_13_FIRST_REAL_PAGE_INDEPENDENT_ANALYZER_REVIEW_V1_0.txt` (future — PR #8)

---

### Step 12 — Controller post-analyzer decision

**Goal:** Controller reviews analyzer output and makes final decision.

| Decision | Meaning |
|----------|---------|
| `ACCEPT` | Proceed to human approval |
| `MODIFY` | Return to draft or QA with controller notes |
| `REJECT` | Do not proceed |
| `DEFER` | Pause — flag for future run |
| `HUMAN_REVIEW_REQUIRED` | Escalate |
| `PATCH_REQUIRED` | Specific patch needed before proceeding |

**Prompt:** `PROMPT_14_CONTROLLER_POST_ANALYZER_DECISION_V1_0.txt` (future — PR #8)

---

### Step 13 — Human approval

**Goal:** Human owner approves the implementation handoff.

| Check | Requirement |
|-------|-------------|
| Human review complete | Human has read the validated draft |
| Human approval | Explicit written approval |
| No self-approval | Operator or agent may not self-approve |

**Hard stop:** No implementation proceeds without explicit human approval.

---

### Step 14 — Implementation or Astro handoff

**Goal:** Deliver the approved schema to the appropriate implementation lane.

| Mode | Handoff |
|------|---------|
| Mode 1 | Current website implementation packet |
| Mode 2 | Future Astro carry packet (requires Astro carry gates) |

**Rules:**
- Operator hands off to HTML/runtime lane (Mode 1) or Astro lane (Mode 2).
- No self-deployment.
- No schema mutation during handoff.
- Astro may not invent, repair, normalize, or override schema values.

---

## Non-authorization

This page run sequence does not authorize schema output. It does not authorize JSON-LD creation. It does not authorize current website implementation or Astro attachment. The sequence is documentation only and is not yet executable.
