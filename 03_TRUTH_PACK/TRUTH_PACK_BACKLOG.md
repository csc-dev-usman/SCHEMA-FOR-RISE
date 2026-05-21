# Truth Pack Backlog — Rise FC Standalone Schema Operator Package

**Status:** `BACKLOG_OPEN_NO_SCHEMA_OUTPUT`

---

## Purpose

This backlog tracks future truth-pack additions needed to support full sitewide schema coverage for the Rise FC standalone schema operator package. Items listed here are not yet created. They require Phase 0 source material to be brought into the standalone package through governed truth-pack update PRs.

---

## Pending source maps

| Item | Status | Dependency |
|------|--------|------------|
| Sitewide Phase 0 schema truth view | NOT_YET_CREATED | Phase 0 full source import |
| Program page truth source map | NOT_YET_CREATED | Phase 0 program truth classes |
| Location / field truth source map | NOT_YET_CREATED | Phase 0 location truth classes |
| Contact page truth source map | NOT_YET_CREATED | Phase 0 contact confirmation + owner approval |
| Camps truth source map | NOT_YET_CREATED | Phase 0 camps truth classes |
| Tryouts truth source map | NOT_YET_CREATED | Phase 0 tryouts truth classes |

---

## Pending scoped truth views

| Truth view | Scope | Status | Dependency |
|-----------|-------|--------|------------|
| Sitewide Phase 0 schema truth view | All routes | NOT_YET_CREATED | Phase 0 full source |
| Program page scoped truth view | Program routes | NOT_YET_CREATED | Phase 0 program truth |
| Camps page scoped truth view | Camps route | NOT_YET_CREATED | Phase 0 camps truth |
| Tryouts page scoped truth view | Tryouts route | NOT_YET_CREATED | Phase 0 tryouts truth |
| Rising Stars page scoped truth view | Rising Stars route | NOT_YET_CREATED | Phase 0 Rising Stars truth |
| Contact page scoped truth view | Contact route | NOT_YET_CREATED | Phase 0 contact + owner approval |
| Field / location page scoped truth view | Location routes | NOT_YET_CREATED | Phase 0 location truth |
| Learning center / article scoped truth views | Article routes | NOT_YET_CREATED | Phase 0 learning center truth |

---

## Pending fingerprints

| Fingerprint | Scope | Status |
|------------|-------|--------|
| Sitewide truth view fingerprint | All routes | NOT_YET_CREATED |
| Program page truth view fingerprint | Program routes | NOT_YET_CREATED |
| Camps page truth view fingerprint | Camps route | NOT_YET_CREATED |
| Tryouts page truth view fingerprint | Tryouts route | NOT_YET_CREATED |
| Rising Stars page truth view fingerprint | Rising Stars route | NOT_YET_CREATED |
| Contact page truth view fingerprint | Contact route | NOT_YET_CREATED |
| Field / location page truth view fingerprint | Location routes | NOT_YET_CREATED |

---

## Pending owner approvals

| Field category | Current status | Expected action |
|---------------|----------------|-----------------|
| Public phone | NOT_REVIEWED | Owner review required |
| Public email | NOT_REVIEWED | Owner review required |
| sameAs / social profile URLs (all platforms) | NOT_REVIEWED | Owner review + Phase 0 confirmation |
| Absolute logo URL | NOT_REVIEWED | Owner review + Phase 0 confirmation |
| Schema description from tagline or mission line | NOT_REVIEWED | Owner review + Phase 0 confirmation |
| Coordinates | NOT_REVIEWED | Owner review + Phase 0 geo confirmation + doctrine authorization |
| Address / place identity | NOT_REVIEWED | Owner review + Phase 0 confirmation + doctrine authorization |

---

## Pending current-site evidence needs

| Evidence item | Status | Notes |
|--------------|--------|-------|
| Homepage evidence map | NOT_YET_CREATED | Needed before HOMEPAGE_SCHEMA_PROFILE can be finalized |
| Program page evidence maps | NOT_YET_CREATED | One per program route |
| Canonical URL inventory for current site | NOT_YET_CREATED | Required for BreadcrumbList and WebPage module accuracy |
| Page-level schema readiness assessment | NOT_YET_CREATED | Signal which pages are evidence-ready |

---

## Pending future Astro evidence needs

| Evidence item | Status | Notes |
|--------------|--------|-------|
| Astro route manifest dependency | NOT_YET_CREATED | Required before any Astro carry gate can be defined |
| Astro carry gate definitions | NOT_YET_CREATED | Required before Mode 2 can begin |
| Astro schema attachment protocol | NOT_YET_CREATED | Defined in a future Mode 2 PR |

---

## Explicitly not included in PR #3

The following items were considered in scope for future truth-pack work but are explicitly not included in this PR:

- Any schema output or JSON-LD
- Homepage JSON-LD draft
- Evidence maps
- Schema profiles
- Operator prompts
- Validators
- Smoke tests
- Real run artifacts
- Owner-approved contact / social / logo fields
- Populated sameAs arrays
- Coordinates or GeoCoordinates data
- Sitewide or multi-page truth views
- Astro carry gates or attachment protocol
