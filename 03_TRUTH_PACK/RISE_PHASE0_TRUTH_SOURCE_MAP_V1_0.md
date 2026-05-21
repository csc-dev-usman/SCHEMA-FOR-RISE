# Rise Phase 0 Truth Source Map V1.0

**Status:** `TRUTH_PACK_HOMEPAGE_SCOPED_REFERENCE_ADDED_NO_SCHEMA_OUTPUT`

---

## Purpose

This source map identifies which truth classes are needed by Rise FC schema operators and defines how each layer of the source-truth hierarchy feeds the schema workflow. It does not contain all Rise facts. It is not a substitute for Phase 0. It guides operators on what to look for and what to hold when truth is missing or unconfirmed.

---

## Source truth hierarchy

| Level | Layer | Role in schema workflow |
|-------|-------|------------------------|
| 1 | Rise Phase 0 factual truth | Primary anchor for all field values. If Phase 0 does not confirm a fact, that fact is not schema. |
| 2 | Rise generated Phase 0 schema truth view / scoped derivations | Machine-readable extraction of schema-relevant Phase 0 facts. Read-only. |
| 3 | Approved page evidence maps | Per-page confirmation of which Phase 0 facts apply and are observable on the target page. |
| 4 | Schema profile decisions | Per-page schema shape: modules, fields, values, and explicit module exclusions. |
| 5 | Rise standalone schema operator package | Governed workflow for deriving, validating, and handing off schema output. |
| 6 | Validated schema output bundles | Finalized output confirmed by the package validator. Ready for implementation review. |
| 7 | Current website implementation / future Astro carry | Approved schema attached to the live surface. Strictly carrier — no schema authoring. |

---

## Phase 0 role

Rise Phase 0 is the authoritative factual truth source. All schema field values must trace to Phase 0.

Schema operators must not write a field value unless Phase 0 explicitly confirms it. If Phase 0 is silent on a field, the field is omitted. If Phase 0 is incomplete or potentially outdated, the field is held.

If Phase 0 source references are missing, schema must hold.

---

## Generated schema truth-view role

A generated Phase 0 schema truth view is a read-only scoped derivation that makes Phase 0 facts available in schema-relevant JSON format. It is not JSON-LD. It is not schema output. It does not establish facts — it reflects them.

The homepage scoped truth view in this PR (`RISE_PHASE0_SCHEMA_TRUTH_VIEW_HOMEPAGE_SCOPED_V1_0.json`) is a read-only reference artifact. Operators may read it to understand what is confirmed and what is held. They may not modify it outside a governed truth-pack update PR.

If truth-view freshness cannot be verified against the fingerprint, schema must hold.

---

## Scoped homepage truth-view role

The homepage scoped truth view is the first lane target for schema derivation. It is scoped to:
- Page: homepage
- Route: `/`
- Schema profile: `HOMEPAGE_SCHEMA_PROFILE`

It carries:
- Module list (allowed future-only, blocked)
- Held field categories
- Fingerprint lock
- Authorization flags (all currently false)
- Hold rules

It does not carry completed field values for held categories. Those require owner approval and Phase 0 confirmation before they can be populated in a schema profile.

---

## Evidence map dependency

Before schema can be drafted for the homepage, an approved evidence map must be created. The evidence map:
- Confirms which Phase 0 facts are observable and applicable on the homepage
- Signals readiness for each allowed module
- Identifies any page-specific facts beyond Phase 0 (none may contradict Phase 0)

Evidence maps are not part of PR #3. They are added in a later PR.

If the page evidence map is missing, schema must hold.

---

## Schema profile dependency

Before schema output can be generated, an approved schema profile (`HOMEPAGE_SCHEMA_PROFILE`) must exist. The schema profile:
- Selects the final module set from the allowed list
- Maps confirmed field values to module properties
- Explicitly excludes all blocked modules
- References the confirmed Phase 0 source for each field value

Schema profiles are not part of PR #3. They are added in a later PR.

If the schema profile is missing, schema must hold.

---

## Current website dependency

Before schema is implemented on the current risefcsoccer.com website, all of the following must exist:
- Validated schema output bundle (PR #5+)
- Human approval of the validated bundle
- Explicit implementation authorization

Current website implementation is not authorized by any file in PR #3.

If page evidence conflicts with Phase 0, schema must hold.

---

## Future Astro dependency

Before schema is attached in Astro, all of the following must exist:
- Defined and passed Astro carry gates (future PR)
- Validated schema output bundle
- Human approval

Astro attachment is not authorized by any file in PR #3.

---

## Non-authority of this source map

This source map:
- Does not contain all Rise FC facts
- Does not substitute for Phase 0
- Does not authorize JSON-LD generation
- Does not authorize schema output
- Does not authorize current website implementation
- Does not authorize Astro attachment
- Does not approve held fields
- Does not modify Phase 0

---

## Hold conditions

| Condition | Hold rule |
|-----------|-----------|
| Phase 0 source reference missing | HOLD — do not derive schema |
| Truth-view freshness unverifiable | HOLD — verify fingerprint first |
| Page evidence map missing | HOLD — do not create schema profile |
| Schema profile missing | HOLD — do not generate output |
| Phase 0 / page evidence conflict | HOLD — escalate upstream |
| Held field requested without owner approval | HOLD — omit field |
| Blocked module requested | HOLD — defer |

---

## Next required source material

The following items are required before the homepage schema workflow can proceed:

| Item | Status | Expected PR |
|------|--------|-------------|
| Homepage evidence map | NOT_YET_CREATED | Later PR |
| HOMEPAGE_SCHEMA_PROFILE | NOT_YET_CREATED | PR #4 |
| Owner approval for held fields | NOT_REVIEWED | Owner action required |
| Operator prompts | NOT_YET_CREATED | PR #4 |
| Validators | NOT_YET_CREATED | PR #5 |
| Final runnable handoff | NOT_YET_CREATED | PR #5 |

---

## Dynamic Truth Library — future source dependencies

The following ten truth classes are expected future source dependencies for sitewide schema coverage. None of these are populated in PR #3. They are marked as `FUTURE_SOURCE_DEPENDENCY` until explicitly available in the standalone package from governed Phase 0 source material.

| Truth class | Status |
|-------------|--------|
| Tryout | FUTURE_SOURCE_DEPENDENCY |
| Camp | FUTURE_SOURCE_DEPENDENCY |
| Locations | FUTURE_SOURCE_DEPENDENCY |
| Coaches | FUTURE_SOURCE_DEPENDENCY |
| Academy | FUTURE_SOURCE_DEPENDENCY |
| Special programs | FUTURE_SOURCE_DEPENDENCY |
| Rising Stars | FUTURE_SOURCE_DEPENDENCY |
| Club | FUTURE_SOURCE_DEPENDENCY |
| Service area | FUTURE_SOURCE_DEPENDENCY |
| Learning center | FUTURE_SOURCE_DEPENDENCY |

Do not invent values for these categories. Do not use convention or inference to fill them. They must come from explicit Phase 0 source material when that material is brought into the standalone package through a governed truth-pack update PR.
