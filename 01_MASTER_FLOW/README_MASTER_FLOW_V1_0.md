# Rise Master Flow — Folder Index V1.0

**Status:** `MASTER_FLOW_ADDED_NO_SCHEMA_OUTPUT`

---

## Purpose

This folder contains the standalone master flow documents for the Rise FC schema operator package. These documents define the operating sequence, mode-specific flows, page run sequence, and master stop conditions.

PR #5 adds master-flow documentation only. No schema output has been created. No JSON-LD has been created. No prompts have been executed. No evidence maps exist. Mode 1 is documented but not runnable. Mode 2 is documented but not ready.

---

## Reading order

1. `README_MASTER_FLOW_V1_0.md` — this file
2. `RISE_STANDALONE_SCHEMA_MASTER_FLOW_V1_0.md` — root master flow: source-truth hierarchy, modes, homepage lane, sequences, stop conditions
3. `MODE_1_CURRENT_WEBSITE_SCHEMA_OPTIMIZATION_FLOW_V1_0.md` — Mode 1 current-site optimization flow
4. `MODE_2_FUTURE_ASTRO_SCHEMA_CARRY_FLOW_V1_0.md` — Mode 2 future Astro carry flow
5. `RISE_SCHEMA_PAGE_RUN_SEQUENCE_V1_0.md` — per-page run sequence from intake through handoff
6. `RISE_SCHEMA_MASTER_STOP_CONDITIONS_V1_0.md` — all master stop conditions

---

## What this folder is

- Master flow documentation for the Rise FC standalone schema operator package.
- Reference material for operators before any schema work begins.
- A controlled definition of what must happen — and in what order — before schema output is produced.

---

## What this folder is not

- It is **not** a runnable schema workflow yet.
- It is **not** a schema generator.
- It does **not** contain evidence maps.
- It does **not** contain operator prompts.
- It does **not** contain validators.
- It does **not** authorize JSON-LD creation.
- It does **not** authorize Mode 1 to run.
- It does **not** authorize Mode 2 to run.

---

## Non-authorization

This folder does not authorize schema output. It does not authorize JSON-LD generation. It does not authorize current website implementation or Astro attachment.

Mode 1 is documented but not runnable. Mode 2 is documented but not ready. Operator prompts, evidence maps, validators, and the final runnable handoff are pending in later PRs.
