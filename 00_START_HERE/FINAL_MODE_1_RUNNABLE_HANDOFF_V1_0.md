# Final Mode 1 Runnable Handoff V1.0

**Status:** `MILESTONE_5_ASTRO_CARRY_BRIDGE_COMPLETE_MODE_1_SUPERVISED_RUNNABLE_NO_SCHEMA_OUTPUT`

---

## Mode 1 supervised-runnable declaration

**Mode 1 is supervised-runnable as of PR #26.**

`mode1Runnable: true` and `mode1SupervisedRunnable: true` are now set in `package_manifest.json`. Milestone 5 (Astro Carry Bridge) is complete. All prerequisite PRs are merged.

This is a supervised runnable status. Mode 1 intake may begin for a confirmed page candidate. Schema output is not yet authorized — a separate governed draft run (PR #27) is required before any JSON-LD is created.

---

## What to do now

If you are an operator starting the Mode 1 workflow, follow this sequence:

**Step 1 — Confirm all start conditions (required before Prompt 00).**

Read `05_REFERENCE_WORKFLOW/MODE_1_OPERATOR_START_CONDITIONS_V1_0.md` and confirm all 14 start conditions (SC-001 through SC-014) pass. Do not start Prompt 00 until all conditions are confirmed.

**Step 2 — Review the scope and limits.**

Read `05_REFERENCE_WORKFLOW/MODE_1_RUNNABLE_SCOPE_AND_LIMITS_V1_0.md`. Understand what you CAN and CANNOT do under supervised-runnable status before starting intake.

**Step 3 — Run the package validator and health reporter.**

```
python tools/validate_package.py .
python tools/report_package_health.py .
python tools/run_standalone_smoke_test.py .
```

All must return PASS or CLEAN before proceeding.

**Step 4 — Start Prompt 00 intake.**

Open `04_OPERATOR_PROMPTS/PROMPT_00_STANDALONE_URL_REVIEW_START_V1_0.txt`.

Prompt 00 collects:
- Target URL
- Phase 0 source reference
- Truth state and fingerprint verification
- Active schema profile
- Blocked modules confirmation
- Held fields confirmation
- Evidence map status

**Step 5 — Apply hold rules if any precondition fails.**

If any intake check fails, apply the appropriate hold code from `05_REFERENCE_WORKFLOW/FIRST_REAL_PAGE_RUN_HOLD_REASON_REFERENCE_V1_0.md`. Do not proceed until all holds are resolved.

**Step 6 — Wait for PR #27 before drafting.**

The governed draft run is not yet authorized. After intake completes and all preconditions pass, the next milestone is PR #27 (controlled non-production homepage JSON-LD draft). Do not produce JSON-LD without PR #27 authorization.

---

## What supervised-runnable does NOT mean

- Schema output is **not** auto-approved
- JSON-LD has **not** been created — no `@context`, no `@type` nodes
- Website implementation is **not** authorized
- Production deployment is **not** authorized — `productionLockStatus` is `NO_PRODUCTION_LOCKS`
- Astro attachment is **not** authorized — `mode2AstroReady: false`
- Any held field is **not** approved — all 15 categories remain `NOT_REVIEWED_HELD`
- Any blocked module is **not** unblocked

For the full list, see `05_REFERENCE_WORKFLOW/FINAL_MODE_1_SUPERVISED_RUNNABLE_HANDOFF_V1_0.md`.

---

## Prerequisite status

All dependencies for the Mode 1 runnable handoff are met:

| Dependency | PR | Status |
|-----------|-----|--------|
| Governing doctrine | PR #2 | ✓ Done |
| Source-truth boundary | PR #2 | ✓ Done |
| Phase 0 truth-pack reference | PR #3 | ✓ Done |
| Homepage schema profile | PR #4 | ✓ Done |
| Blocked module policy | PR #4 | ✓ Done |
| Standalone master flow | PR #5 | ✓ Done |
| Team quickstart and checklist upgrades | PR #6 | ✓ Done |
| Operator prompts 00–04, 08 | PR #7 | ✓ Done |
| Final validation and analyzer prompts | PR #8 | ✓ Done |
| Output bundle contract schemas | PR #9 | ✓ Done |
| Homepage non-production draft contract | PR #10 | ✓ Done |
| Output bundle validator | PR #11 | ✓ Done |
| Claude QA and controller review contracts | PR #12 | ✓ Done |
| Final schema validation protocol | PR #13 | ✓ Done |
| Governed run ledger schema | PR #14 | ✓ Done |
| Run ledger append helper and reporter | PR #15 | ✓ Done |
| Package validator and active-file checks | PR #16 | ✓ Done |
| Smoke-test fixture contract and canned fixture | PR #17 | ✓ Done |
| Smoke-test runner and package health reporter | PR #18 | ✓ Done |
| First real page handoff template | PR #19 | ✓ Done |
| Independent analyzer and controller post-analyzer flow | PR #20 | ✓ Done |
| Current website implementation handoff checklist | PR #21 | ✓ Done |
| Governed sample-run artifact policy | PR #22 | ✓ Done |
| Astro schema carry gate reference | PR #23 | ✓ Done |
| Runtime Appendix carry field reference | PR #24 | ✓ Done |
| Astro attachment packet template | PR #25 | ✓ Done |
| Final Mode 1 runnable handoff | PR #26 | ✓ Done |

---

## Mode 1 governed run sequence (for intake reference)

When the intake sequence starts, Mode 1 will follow this sequence:

1. Confirm page candidate (starting with homepage `/`)
2. Confirm Phase 0 source reference and truth fingerprint
3. Load approved schema profile (`HOMEPAGE_SCHEMA_PROFILE`)
4. Run page content readiness gate (Prompt 08)
5. Build non-production JSON-LD draft from confirmed evidence (Prompt 01) — requires PR #27
6. Run external QA one-zip (Prompt 02)
7. Run controller decision (Prompt 03)
8. Run validation (Prompt 04)
9. Run independent analyzer review (Prompt 13)
10. Run controller post-analyzer decision (Prompt 14)
11. Obtain human approval for implementation handoff
12. Deliver implementation packet for current website (Prompt 12)
13. Append run ledger entry (Prompt 15)

Steps 1–4 are available under supervised-runnable status. Steps 5–13 require PR #27 authorization.

---

## What Mode 1 will not do

- Invent content fields
- Include blocked modules (FAQPage, Offer, Event, Review, AggregateRating, Place, GeoCoordinates, testimonial-derived schema, bilingual schema, advanced modules)
- Emit held fields without owner approval
- Mutate Rise Phase 0
- Attach schema to the website without human approval
- Self-approve production lock

---

## Reference documents for this handoff

| Document | Purpose |
|----------|---------|
| `05_REFERENCE_WORKFLOW/FINAL_MODE_1_SUPERVISED_RUNNABLE_HANDOFF_V1_0.md` | Formal reference declaration of supervised-runnable status |
| `05_REFERENCE_WORKFLOW/MODE_1_RUNNABLE_SCOPE_AND_LIMITS_V1_0.md` | Full CAN/CANNOT table with blocking conditions |
| `05_REFERENCE_WORKFLOW/MODE_1_OPERATOR_START_CONDITIONS_V1_0.md` | All 14 start conditions with resolution guide |
| `05_REFERENCE_WORKFLOW/MILESTONE_5_ASTRO_CARRY_BRIDGE_COMPLETION_AUDIT_V1_0.md` | Milestone 5 completion audit — all components verified |
