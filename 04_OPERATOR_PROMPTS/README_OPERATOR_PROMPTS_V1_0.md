# Operator Prompts — Rise FC Standalone Schema Package

**Status:** `CORE_OPERATOR_PROMPTS_ADDED_NO_SCHEMA_OUTPUT`

> These prompt files are templates only. They have not been executed. No schema has been generated. No JSON-LD has been created. No evidence maps, output bundles, or real run artifacts exist. Operators must not run any prompt until the final runnable handoff is in place.

---

## Purpose

This folder contains the governed operator prompt templates for the Rise FC standalone schema workflow. Each prompt defines the exact instructions an operator passes to Claude when executing a step in the Mode 1 or Mode 2 flow.

Prompts are templates — they are not executed by reading this file. They are used by a human operator who pastes or references them in a governed run session.

---

## Core rule

Every prompt in this folder preserves the following constraints without exception:

- No content invention — all fields must trace to Phase 0 or confirmed page evidence
- No held fields emitted — all 15 held field categories default to NOT_REVIEWED_HELD
- No blocked modules — FAQPage, Offer, Event, Review, AggregateRating, Place, GeoCoordinates, testimonial-derived, bilingual, advanced modules are blocked
- No Phase 0 mutation — this package is read-only downstream of Phase 0
- No Astro attachment — Mode 2 is not yet authorized
- No production lock without explicit human approval at every gate
- No self-approval — Claude never approves its own output for production

---

## Prompts in this folder (PR #7)

| Prompt file | Prompt number | Purpose |
|-------------|---------------|---------|
| `PROMPT_00_STANDALONE_URL_REVIEW_START_V1_0.txt` | 00 | Standalone URL review start — collect target, scope, and run context |
| `PROMPT_01_BUILD_NON_PRODUCTION_JSONLD_DRAFT_V1_0.txt` | 01 | Build non-production JSON-LD draft from confirmed evidence |
| `PROMPT_02_CLAUDE_EXTERNAL_QA_ONE_ZIP_V1_0.txt` | 02 | Claude external QA one-zip review |
| `PROMPT_03_CONTROLLER_DECISION_AND_REGENERATION_V1_0.txt` | 03 | Controller decision and regeneration |
| `PROMPT_04_VALIDATOR_RESULTS_REVIEW_V1_0.txt` | 04 | Validator results review |
| `PROMPT_08_PAGE_CONTENT_READINESS_GATE_V1_0.txt` | 08 | Page content readiness gate |

---

## Prompts added in later PRs

| Prompt file | Prompt number | Purpose | PR |
|-------------|---------------|---------|-----|
| `PROMPT_12_FINAL_VALIDATION_AND_IMPLEMENTATION_SCHEMA_V1_0.txt` | 12 | Final validation and implementation schema | PR #8 |
| `PROMPT_13_FIRST_REAL_PAGE_INDEPENDENT_ANALYZER_REVIEW_V1_0.txt` | 13 | Independent analyzer review | PR #8 |
| `PROMPT_14_CONTROLLER_POST_ANALYZER_DECISION_V1_0.txt` | 14 | Controller post-analyzer decision | PR #8 |
| `PROMPT_15_MODE_1_LANE_COMPLETION_AUDIT_V1_0.txt` | 15 | Mode 1 lane completion audit | PR #8 |

---

## Run sequence reference

Prompts map to the master flow steps as follows:

| Step | Master flow step | Prompt |
|------|-----------------|--------|
| 1 | Intake and context | Prompt 00 |
| 2–4 | Truth, profile, block/hold confirmation | Prompt 00 (gates within) |
| 5 | Page content readiness gate | Prompt 08 |
| 6 | Evidence map | (evidence map creation — human-driven) |
| 7 | Build non-production JSON-LD draft | Prompt 01 |
| 8 | External QA one-zip | Prompt 02 |
| 9 | Controller decision | Prompt 03 |
| 10 | Validator results review | Prompt 04 |
| 11 | Independent analyzer review | Prompt 13 |
| 12 | Controller post-analyzer decision | Prompt 14 |
| 13 | Human approval | (human gate — no prompt) |
| 14 | Implementation or Astro handoff | Prompt 12 |
| — | Mode 1 lane completion audit | Prompt 15 |

---

## Non-authorization statement

This README and the prompt files in this folder do not authorize:
- Schema output
- JSON-LD generation
- Homepage draft creation
- Evidence map creation as a run artifact
- Current website implementation
- Astro attachment
- Production lock

No governed run has occurred. No real run artifacts exist. Prompt files are templates only.

Future PRs will add the output bundle contract schemas (PR #9), the homepage non-production draft contract (PR #10), and the final runnable handoff.
