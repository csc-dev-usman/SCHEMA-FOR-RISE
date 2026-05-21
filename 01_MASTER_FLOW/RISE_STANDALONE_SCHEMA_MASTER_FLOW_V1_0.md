# Rise Standalone Schema Master Flow V1.0

**Status:** `MASTER_FLOW_ADDED_NO_SCHEMA_OUTPUT`

---

## Purpose

This document is the root master flow for the Rise FC standalone schema operator package. It defines the source-truth hierarchy, operating modes, homepage lane context, required upstream artifacts, required future artifacts, master sequence, stop conditions, and non-authorization statement.

This is documentation only. No schema output is produced by reading this document.

---

## Source-truth hierarchy

| Level | Source |
|-------|--------|
| 1 | Rise Phase 0 factual truth |
| 2 | Rise generated Phase 0 schema truth view / scoped derivations |
| 3 | Rise evidence maps and schema profile decisions |
| 4 | Rise schema operator package (this package) |
| 5 | Validated schema output bundles |
| 6 | Current website or Astro implementation handoff |

Rise Phase 0 is the source of factual truth. This package is downstream of Phase 0. Schema is a derived read model. This package must not mutate Phase 0.

---

## Operating modes

### Mode 1 — Current website schema optimization

**Goal:** Produce validated schema for pages on the current risefcsoccer.com website.

- Schema is derived from approved Phase 0 content and confirmed page evidence.
- Output is validated before any implementation handoff.
- No guesswork. No invented fields.
- Human approval required at every gate.

**Status: Documented. Not yet runnable. Operator prompts, evidence maps, validators, and runnable handoff are pending.**

### Mode 2 — Future Astro schema carry and attachment

**Goal:** After Astro route and runtime evidence is ready, carry validated schema into the Astro implementation.

- Blocked until Astro carry gates exist.
- No Astro files are created or modified by this package.
- A future PR will define the carry gates and attachment protocol.

**Status: Documented. Not yet ready.**

---

## Homepage lane context

| Field | Value |
|-------|-------|
| First schema lane target | Homepage |
| Route | `/` |
| Schema profile | `HOMEPAGE_SCHEMA_PROFILE` |
| Truth fingerprint | `80edd829806cae271242c6a8e853edabdb8b2f16ca5a8fa1a3fc69ff5b78d53d` |
| Allowed future modules | Organization, WebSite, WebPage, BreadcrumbList |
| Blocked modules | FAQPage, Offer, Event, Review, AggregateRating, Place, GeoCoordinates, testimonial-derived, bilingual, advanced |
| Evidence map | NOT_YET_CREATED |
| Operator prompt | NOT_YET_CREATED |
| Validator | NOT_YET_CREATED |

---

## Required upstream artifacts (already exist)

| Artifact | Location | Status |
|---------|----------|--------|
| Phase 0 source-truth boundary | `02_GOVERNING_DOCTRINE/` | PRESENT (PR #2) |
| Governing doctrine | `02_GOVERNING_DOCTRINE/` | PRESENT (PR #2) |
| Lane ownership rules | `02_GOVERNING_DOCTRINE/` | PRESENT (PR #2) |
| Hold rules | `02_GOVERNING_DOCTRINE/` | PRESENT (PR #2) |
| Homepage scoped truth view | `03_TRUTH_PACK/` | PRESENT (PR #3) |
| Homepage truth fingerprint lock | `03_TRUTH_PACK/` | PRESENT (PR #3) |
| Owner approval worksheet | `03_TRUTH_PACK/` | PRESENT (PR #3) |
| Homepage schema profile | `07_REFERENCE_LISTS/` | PRESENT (PR #4) |
| Blocked module policy | `07_REFERENCE_LISTS/` | PRESENT (PR #4) |
| Held field categories | `07_REFERENCE_LISTS/` | PRESENT (PR #4) |
| Allowed modules list | `07_REFERENCE_LISTS/` | PRESENT (PR #4) |
| Schema profile decision matrix | `07_REFERENCE_LISTS/` | PRESENT (PR #4) |

---

## Required future artifacts (not yet created)

| Artifact | Target PR | Status |
|---------|-----------|--------|
| Operator prompts | PR #7 | NOT_YET_CREATED |
| Homepage evidence map | Future PR | NOT_YET_CREATED |
| Output bundle contract schemas | PR #9 | NOT_YET_CREATED |
| Homepage non-production draft contract | PR #10 | NOT_YET_CREATED |
| Validator | Future PR | NOT_YET_CREATED |
| Smoke tests | Future PR | NOT_YET_CREATED |
| Final runnable handoff | Future PR | NOT_YET_CREATED |

---

## Master sequence

The master sequence defines the required order of operations before schema output can be produced for any target page. No step may be skipped.

```
Step 1: Intake
  - Confirm target URL and route
  - Confirm target page family
  - Confirm operating mode (Mode 1 or Mode 2)

Step 2: Truth confirmation
  - Verify Phase 0 source reference exists for target page
  - Verify scoped truth view exists or derive from Phase 0
  - Verify truth fingerprint matches locked value
  - Hold if any truth artifact is missing or mismatched

Step 3: Profile confirmation
  - Identify active schema profile for target route
  - Confirm profile is HOMEPAGE_SCHEMA_PROFILE for route /
  - Confirm all allowed modules list is accurate
  - Confirm all blocked modules are still blocked
  - Hold if no profile exists for the target route

Step 4: Block and hold confirmation
  - Confirm no blocked modules are being requested
  - Confirm no held fields will be emitted without owner approval
  - Reject blocked module requests immediately
  - Omit held fields — do not estimate or infer

Step 5: Readiness gate
  - Confirm page content readiness via Prompt 08 (future)
  - Hold if content is not confirmed from Phase 0 or page evidence
  - No schema drafting until readiness gate passes

Step 6: Evidence map
  - Confirm evidence map exists for target profile (future artifact)
  - Hold if evidence map does not exist
  - Evidence map must link every emitted field to its Phase 0 or page evidence source

Step 7: Draft
  - Run Prompt 01 to produce non-production JSON-LD draft (future)
  - No production output at this step
  - Held fields omitted
  - Blocked modules excluded

Step 8: QA
  - Run Prompt 02 external QA one-zip (future)
  - Review QA output
  - Do not treat QA output as source truth

Step 9: Controller decision
  - Run Prompt 03 controller decision (future)
  - Decisions: ACCEPT, MODIFY, REJECT, DEFER, HUMAN_REVIEW_REQUIRED
  - No schema proceeds to validation without ACCEPT

Step 10: Validation
  - Run Prompt 04 validator results review (future)
  - Schema.org validation
  - Google Rich Results validation where applicable
  - No implementation proceeds without validation pass

Step 11: Analyzer review
  - Run Prompt 13 independent analyzer review (future)
  - Analyzer must not mutate source truth
  - Hold if analyzer raises new block conditions

Step 12: Controller post-analyzer decision
  - Run Prompt 14 controller post-analyzer decision (future)
  - Decisions: ACCEPT, MODIFY, REJECT, DEFER, HUMAN_REVIEW_REQUIRED, PATCH_REQUIRED

Step 13: Human approval
  - Human owner approves implementation handoff
  - No production deployment without explicit human approval

Step 14: Implementation or Astro handoff
  - Mode 1: current website implementation packet
  - Mode 2: future Astro carry packet (requires Astro carry gates)
  - No self-deployment by any operator or agent
```

---

## Stop conditions

If any of the following conditions are true, the master flow must stop immediately:

| Condition | Stop code |
|-----------|-----------|
| Phase 0 source reference missing | STOP_MISSING_PHASE0_SOURCE |
| Scoped truth view missing | STOP_MISSING_TRUTH_VIEW |
| Truth fingerprint mismatch | STOP_FINGERPRINT_MISMATCH |
| Schema profile missing for target route | STOP_MISSING_PROFILE |
| Evidence map missing | STOP_MISSING_EVIDENCE_MAP |
| Blocked module requested | STOP_BLOCKED_MODULE |
| Held field requested without owner approval | STOP_HELD_FIELD_NOT_APPROVED |
| Readiness gate failed | STOP_READINESS_GATE_FAILED |
| JSON-LD created before controller ACCEPT | STOP_PREMATURE_JSONLD |
| Implementation before human approval | STOP_PREMATURE_IMPLEMENTATION |
| Astro attachment before carry gates exist | STOP_PREMATURE_ASTRO_ATTACHMENT |
| Production lock without explicit human authorization | STOP_PREMATURE_PRODUCTION_LOCK |
| Phase 0 mutation attempted | STOP_PHASE0_MUTATION |
| Source truth mutation attempted | STOP_SOURCE_TRUTH_MUTATION |

See `RISE_SCHEMA_MASTER_STOP_CONDITIONS_V1_0.md` for full detail.

---

## Non-authorization

This document does not authorize schema output. It does not authorize JSON-LD generation. It does not authorize current website implementation or Astro attachment. It does not authorize production lock.

Mode 1 is documented but not runnable. Mode 2 is documented but not ready. Required future artifacts listed above must exist before the master sequence can run.
