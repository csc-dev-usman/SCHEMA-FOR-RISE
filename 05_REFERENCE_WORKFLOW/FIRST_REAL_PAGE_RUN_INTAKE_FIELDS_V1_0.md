# First Real Page Run Intake Fields V1.0

**Status:** `FIRST_REAL_PAGE_HANDOFF_TEMPLATE_ADDED_NO_SCHEMA_OUTPUT`

> This document defines the required intake fields and validation expectations for a governed first real page schema run. These are contract definitions only. No real run has been started. No schema has been generated.

---

## Non-authorization statement

This document does not start a schema run, generate JSON-LD, create an evidence map, authorize current website implementation, authorize Astro attachment, or claim production lock.

---

## Purpose

Before any governed schema run may begin, all required intake fields must be populated and validated. A run must not proceed if any required field is missing, invalid, or unconfirmed.

---

## Required intake fields

### 1. Run identity fields

| Field | Type | Validation |
|-------|------|------------|
| `runId` | String | Must match format `RISE_RUN_<PAGE_FAMILY>_<DATE_YYYYMMDD>_<SEQ>`. Must be unique in `RUN_LEDGER.json`. Must not be `PLACEHOLDER_RUN_ID`. |
| `targetUrl` | String | Must be a valid URL. Must not use `example.invalid`. Must not be a placeholder. |
| `pageFamily` | String | Must be a recognized page family (e.g., `HOMEPAGE`). |
| `mode` | String | Must be `MODE_1_CURRENT_WEBSITE` or `MODE_2_FUTURE_ASTRO`. |
| `route` | String | Must be a valid route for the target page (e.g., `/`). |
| `runDate` | String | Must be a valid date in `YYYY-MM-DD` format. |
| `operatorId` | String | Must identify the operator running this session. |

### 2. Phase 0 source reference fields

| Field | Type | Validation |
|-------|------|------------|
| `phase0SourceReference` | String | Must point to a confirmed, existing Phase 0 source document. Must not be `NOT_REVIEWED`. |
| `phase0SourceFile` | String | Must be a valid file path to the Phase 0 source document. File must exist. |
| `phase0SourceConfirmed` | Boolean | Must be `true` before any schema work proceeds. |

**Stop condition:** If `phase0SourceConfirmed` is `false`, the run must stop immediately. Do not proceed.

### 3. Truth-view reference fields

| Field | Type | Validation |
|-------|------|------------|
| `scopedTruthViewReference` | String | Must point to a confirmed scoped truth view for the target page. |
| `scopedTruthViewFile` | String | Must be a valid file path to the scoped truth view JSON. File must exist and parse cleanly. |
| `truthViewConfirmed` | Boolean | Must be `true` before any schema work proceeds. |

**Stop condition:** If `truthViewConfirmed` is `false`, the run must stop immediately. Do not proceed.

### 4. Truth fingerprint fields

| Field | Type | Validation |
|-------|------|------------|
| `truthFingerprint` | String | Must be the SHA-256 hash of the current approved scoped truth view. Must not be all zeros. Must not be a placeholder. |
| `fingerprintMatchConfirmed` | Boolean | Must be `true`. The fingerprint in the run record must match the fingerprint lock file. |
| `fingerprintMatchStatus` | String | Must be `MATCH_CONFIRMED`. Any other value is a stop condition. |

**Stop condition:** If the fingerprint does not match the lock file, the run must stop immediately. The truth view may be stale.

### 5. Schema profile fields

| Field | Type | Validation |
|-------|------|------------|
| `activeSchemaProfile` | String | Must be a recognized, approved schema profile identifier (e.g., `HOMEPAGE_SCHEMA_PROFILE`). |
| `schemaProfileConfirmed` | Boolean | Must be `true` before any schema work proceeds. |

**Stop condition:** If `schemaProfileConfirmed` is `false`, the run must stop immediately. Do not proceed.

### 6. Evidence map fields

| Field | Type | Validation |
|-------|------|------------|
| `evidenceMapStatus` | String | Must be `CONFIRMED` before any JSON-LD draft may be produced. |
| `evidenceMapFile` | String | Must be a valid file path to the confirmed evidence map. File must exist and conform to `EVIDENCE_MAP_SCHEMA_V1_0.json`. |

**Stop condition:** If `evidenceMapStatus` is not `CONFIRMED`, the run must stop immediately. No JSON-LD may be generated without a confirmed evidence map.

---

## Validation expectations

### Intake validation sequence

Before proceeding to any operator prompt, an operator must:

1. Confirm `runId` is unique and correctly formatted.
2. Confirm `targetUrl` is not a placeholder and resolves to a real page.
3. Confirm `phase0SourceConfirmed` is `true`.
4. Confirm `truthViewConfirmed` is `true`.
5. Confirm `fingerprintMatchStatus` is `MATCH_CONFIRMED`.
6. Confirm `schemaProfileConfirmed` is `true`.
7. Confirm `evidenceMapStatus` is `CONFIRMED`.
8. Confirm no blocked modules are listed as allowed.
9. Confirm all held field categories default to `HOLD`.

If any check fails: stop. Do not run Prompt 00 or any subsequent prompt.

---

## Intake failure codes

If intake validation fails, record the applicable hold code from `FIRST_REAL_PAGE_RUN_HOLD_REASON_REFERENCE_V1_0.md`.

Do not proceed until the hold is resolved.

---

## Non-authorization reminder

Completing intake validation does not authorize schema production. It confirms that the minimum preconditions exist to begin the governed run sequence. Human approval is still required at every gate.
