# Mode 1 Operator Start Conditions V1.0

**Status:** `MILESTONE_5_ASTRO_CARRY_BRIDGE_COMPLETE_MODE_1_SUPERVISED_RUNNABLE_NO_SCHEMA_OUTPUT`

---

## Purpose

This document defines all required start conditions that must be confirmed before any Mode 1 operator intake begins. All conditions must pass. A failure on any condition is a HOLD — the operator must not proceed until the failed condition is resolved.

These conditions apply to Mode 1 supervised-runnable status only. They are not schema production gates — they are intake readiness gates.

---

## Start conditions

| # | Condition | Pass state | Block if |
|---|-----------|-----------|----------|
| SC-001 | Package validator passes | `python tools/validate_package.py .` returns PASS (exit 0) | Validator returns FAIL or cannot be run |
| SC-002 | Health reporter passes | `python tools/report_package_health.py .` returns CLEAN (exit 0) | Health reporter returns warnings or cannot be run |
| SC-003 | Smoke test passes | `python tools/run_standalone_smoke_test.py .` returns PASS (exit 0) | Smoke test returns FAIL or cannot be run |
| SC-004 | Target URL identified | Operator has confirmed the exact URL of the target page | No URL confirmed |
| SC-005 | Page family identified | Operator has identified the page family (e.g., `HOMEPAGE`) from the active schema profile | No page family confirmed |
| SC-006 | Phase 0 source reference available | The Phase 0 source reference for the target page exists and is accessible | No Phase 0 source reference for the target page |
| SC-007 | Truth view available | The scoped truth view for the target page exists (`03_TRUTH_PACK/RISE_PHASE0_SCHEMA_TRUTH_VIEW_HOMEPAGE_SCOPED_V1_0.json` for the homepage) | No truth view for the target page |
| SC-008 | Truth fingerprint match | The truth view fingerprint matches the locked value in `03_TRUTH_PACK/RISE_HOMEPAGE_TRUTH_FINGERPRINT_LOCK_V1_0.md` | Fingerprint mismatch — truth view may be stale |
| SC-009 | Schema profile available | An active schema profile exists for the target route (e.g., `HOMEPAGE_SCHEMA_PROFILE` for route `/`) | No active profile for the target route |
| SC-010 | Blocked modules reviewed | Operator has confirmed the blocked module list and confirmed no blocked modules will be emitted | Blocked module review not completed |
| SC-011 | Held fields reviewed | Operator has confirmed the held field categories list (`07_REFERENCE_LISTS/RISE_HELD_FIELD_CATEGORIES_FIRST_PAGE_V1_0.md`) and confirmed all held fields will be omitted | Held field review not completed |
| SC-012 | Operator prompt sequence ready | Operator has read all prompts (00, 08, 01, 02, 03, 04, 13, 14, 12, 15) and understands the run order | Prompt sequence not read |
| SC-013 | Run ledger available | `RUN_LEDGER.json` is present, parses cleanly, and `productionLockStatus` is `NO_PRODUCTION_LOCKS` | Ledger missing, corrupt, or has unexpected lock status |
| SC-014 | Mode 2 not started | `mode2AstroReady: false` confirmed in `package_manifest.json` | Mode 2 inadvertently activated |

---

## Start condition resolution guide

| Condition | Resolution if failed |
|-----------|---------------------|
| SC-001 (package validator) | Read `tools/README_PACKAGE_VALIDATOR_V1_0.md` and `06_MACHINE_RULES/PACKAGE_VALIDATION_CHECKLIST_V1_0.md` for failure diagnostics. Resolve all failing checks before proceeding. |
| SC-002 (health reporter) | Read `tools/README_SMOKE_TEST_AND_HEALTH_TOOLS_V1_0.md` for diagnostic guidance. Resolve all warnings before proceeding. |
| SC-003 (smoke test) | Read `08_SMOKE_TESTS/SMOKE_TEST_RUNNER_EXPECTATIONS_V1_0.md` for expected behavior. Resolve failing checks before proceeding. |
| SC-004 (target URL) | Identify the confirmed URL of the target page and confirm it matches a route in the active schema profile. |
| SC-005 (page family) | Identify the page family from the schema profile (`07_REFERENCE_LISTS/RISE_HOMEPAGE_SCHEMA_PROFILE_V1_0.md`). |
| SC-006 (Phase 0 reference) | Locate the Phase 0 source reference for the target page — may require Phase 0 team assistance. Do not proceed without Phase 0 anchor. |
| SC-007 (truth view) | Locate the scoped truth view — for the homepage this is `03_TRUTH_PACK/RISE_PHASE0_SCHEMA_TRUTH_VIEW_HOMEPAGE_SCOPED_V1_0.json`. Do not proceed without truth view. |
| SC-008 (fingerprint match) | Confirm truth view hash matches `80edd829806cae271242c6a8e853edabdb8b2f16ca5a8fa1a3fc69ff5b78d53d` (homepage). On mismatch: do not proceed; raise with Phase 0 team. |
| SC-009 (schema profile) | Confirm `HOMEPAGE_SCHEMA_PROFILE` is active for route `/`. No profile = no run. |
| SC-010 (blocked modules) | Read `07_REFERENCE_LISTS/RISE_BLOCKED_SCHEMA_MODULES_FIRST_PAGE_V1_0.md`. Confirm all modules in the run scope are on the allowed list. |
| SC-011 (held fields) | Read `07_REFERENCE_LISTS/RISE_HELD_FIELD_CATEGORIES_FIRST_PAGE_V1_0.md` and the owner approval worksheet. Confirm all held field categories remain omitted. |
| SC-012 (prompt sequence) | Read `04_OPERATOR_PROMPTS/README_OPERATOR_PROMPTS_V1_0.md` and all prompt files in run order. Do not run prompts out of sequence. |
| SC-013 (run ledger) | Run `python tools/report_run_ledger_status.py RUN_LEDGER.json`. Resolve any lock status anomalies before proceeding. |
| SC-014 (mode 2 not started) | Confirm `mode2AstroReady: false` in `package_manifest.json`. Mode 2 may not be activated until all carry gates pass and human approval is granted. |

---

## Start condition checklist

Before starting Prompt 00 intake, confirm all of the following:

- [ ] SC-001 — `python tools/validate_package.py .` returns PASS
- [ ] SC-002 — `python tools/report_package_health.py .` returns CLEAN
- [ ] SC-003 — `python tools/run_standalone_smoke_test.py .` returns PASS
- [ ] SC-004 — Target URL confirmed
- [ ] SC-005 — Page family confirmed
- [ ] SC-006 — Phase 0 source reference available for target page
- [ ] SC-007 — Scoped truth view available for target page
- [ ] SC-008 — Truth fingerprint matches locked value
- [ ] SC-009 — Active schema profile confirmed for target route
- [ ] SC-010 — Blocked module list reviewed; no blocked modules in scope
- [ ] SC-011 — Held field categories reviewed; all held fields will be omitted
- [ ] SC-012 — All operator prompts read in sequence order
- [ ] SC-013 — `RUN_LEDGER.json` present, parses cleanly, `productionLockStatus` is `NO_PRODUCTION_LOCKS`
- [ ] SC-014 — `mode2AstroReady: false` confirmed in `package_manifest.json`

**If any condition above is not confirmed: HOLD. Do not start Prompt 00.**

---

## Non-authorization statement

This document does not authorize schema output, JSON-LD creation, website implementation, Astro attachment, production deployment, or production lock status change. Confirming all start conditions authorizes intake only — not schema production.
