# Final Mode 1 Supervised Runnable Handoff V1.0

**Status:** `MILESTONE_5_ASTRO_CARRY_BRIDGE_COMPLETE_MODE_1_SUPERVISED_RUNNABLE_NO_SCHEMA_OUTPUT`

---

## Purpose

This document is the formal reference declaration that Mode 1 is now supervised-runnable as of PR #26. It defines what supervised-runnable means, what operators may now do under supervision, and what remains prohibited until later governed run milestones.

This document is a reference contract for the supervised-runnable status. The operator entry point is `00_START_HERE/FINAL_MODE_1_RUNNABLE_HANDOFF_V1_0.md`.

---

## Supervised-runnable declaration

Mode 1 is **supervised-runnable** as of PR #26.

`mode1Runnable: true` and `mode1SupervisedRunnable: true` are now set in `package_manifest.json`.

Milestone 5 (Astro Carry Bridge) is complete. All four Milestone 5 PRs are merged:

- PR #23 — Astro schema carry gate reference ✓
- PR #24 — Runtime Appendix schema carry field reference ✓
- PR #25 — Astro attachment packet template ✓
- PR #26 — Final Mode 1 supervised runnable handoff ✓

---

## What supervised-runnable means

Supervised-runnable means:

1. The operator workflow **intake sequence may begin** for a confirmed page candidate
2. Operators may **start Prompt 00** (`PROMPT_00_STANDALONE_URL_REVIEW_START_V1_0.txt`) to collect target, truth state, profile, blocked modules, held fields, and evidence map status
3. Operators may use the **preflight checklist** and all readiness gates defined in the governed reference documents
4. Operators may **prepare a first real page run packet** using the handoff template (`FIRST_REAL_PAGE_RUN_HANDOFF_TEMPLATE_V1_0.md`)
5. Operators may **apply hold rules** and hold codes as defined in `FIRST_REAL_PAGE_RUN_HOLD_REASON_REFERENCE_V1_0.md`
6. Operators may **prepare and confirm evidence mapping** for a target route during the run intake sequence
7. Operators may route findings to the **controller** and **human approval** gates
8. Operators may **run the package validator** (`python tools/validate_package.py .`) and the **health reporter** (`python tools/report_package_health.py .`) at any time
9. Operators may **run the smoke test** (`python tools/run_standalone_smoke_test.py .`) to verify package integrity before intake

---

## What supervised-runnable does NOT mean

Supervised-runnable does **not** mean:

1. **Schema output is auto-approved** — no schema output has been created; a governed run with evidence mapping, QA, controller review, and human approval is required
2. **JSON-LD has been created** — no `@context`, no `@type` nodes, no JSON-LD
3. **A homepage draft run has occurred** — intake has not started; no draft exists
4. **Website implementation is authorized** — implementation requires a validated output bundle, controller approval, and human approval
5. **Production deployment is authorized** — production lock requires explicit human authorization; `productionLockStatus` remains `NO_PRODUCTION_LOCKS`
6. **Astro attachment is authorized** — Mode 2 is not ready; `mode2AstroReady: false`
7. **Evidence map exists** — the evidence map must be created during the run intake sequence
8. **Any held field is approved** — all 15 held field categories remain `NOT_REVIEWED_HELD`; no held field may be emitted without owner approval
9. **Any blocked module is unblocked** — FAQPage, Offer, Event, Review, AggregateRating, Place, GeoCoordinates, testimonial-derived, bilingual, and advanced modules remain blocked
10. **Phase 0 may be mutated** — Rise Phase 0 remains the source of factual truth and may not be mutated by this package

---

## Scope and limits reference

See `05_REFERENCE_WORKFLOW/MODE_1_RUNNABLE_SCOPE_AND_LIMITS_V1_0.md` for the full CAN/CANNOT table with per-item blocking conditions.

---

## Operator start conditions

See `05_REFERENCE_WORKFLOW/MODE_1_OPERATOR_START_CONDITIONS_V1_0.md` for the complete list of start conditions that must pass before intake begins.

---

## Critical rules preserved

All critical operating rules from the governing doctrine remain in force:

- Rise Phase 0 remains the source of factual truth
- This package is downstream of Phase 0, not above it
- Schema is a downstream read model derived from approved Phase 0 truth and confirmed page evidence
- Operators may not invent content fields
- Held fields remain held until owner approval and supporting Phase 0 / page evidence exist
- Blocked modules remain blocked until a later governing doctrine PR explicitly authorizes each one
- Human merge only — no self-merge
- No self-approval of production lock

---

## Mode 2 status

Mode 2 is **not ready**. `mode2AstroReady: false` remains in `package_manifest.json`.

Astro carry gates have been defined (PR #23), Runtime Appendix fields defined (PR #24), and attachment packet template added (PR #25). No carry gates have been passed. No real packet has been created. No Astro files have been modified. Mode 2 remains fully blocked until all carry gates pass and human approval for Astro attachment is granted.

---

## Next governed run milestone

The next milestone is **PR #27: Controlled non-production homepage JSON-LD draft**.

PR #27 will authorize the first governed draft run for the homepage at route `/` under `HOMEPAGE_SCHEMA_PROFILE`. This requires confirmation of the evidence map for the target route before any draft is produced.

---

## Non-authorization statement

This document does not authorize:
- JSON-LD creation
- Schema output
- Production schema bundle creation
- Current website implementation
- Astro attachment
- Production deployment
- Production lock status change
- Phase 0 mutation
- Source truth mutation
