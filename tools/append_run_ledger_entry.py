#!/usr/bin/env python3
"""
append_run_ledger_entry.py — Rise FC Standalone Schema Operator Package

Safely appends a new entry to RUN_LEDGER.json after running governed safety checks.

Usage:
    python tools/append_run_ledger_entry.py <entry_file> [--ledger <ledger_file>] [--dry-run]

Arguments:
    entry_file          Path to a JSON file containing the candidate run ledger entry.
    --ledger PATH       Path to RUN_LEDGER.json. Defaults to RUN_LEDGER.json in the
                        current directory.
    --dry-run           Run all safety checks and print results, but do not write to
                        the ledger. No files are modified in dry-run mode.

Exit codes:
    0 — Entry passed all checks and was appended (or would be appended in --dry-run).
    1 — Entry failed one or more safety checks. Ledger not modified.
    2 — Input file error (missing file, parse error, etc.).

Safety checks performed:
    CHECK_001 — Required fields present
    CHECK_002 — runId format valid
    CHECK_003 — runId not already in ledger (no duplicates)
    CHECK_004 — pageFamily value allowed
    CHECK_005 — mode value allowed
    CHECK_006 — readinessStatus value allowed
    CHECK_007 — evidenceMapStatus value allowed
    CHECK_008 — draftStatus value allowed
    CHECK_009 — qaStatus value allowed
    CHECK_010 — controllerStatus value allowed
    CHECK_011 — validationStatus value allowed
    CHECK_012 — implementationStatus value allowed
    CHECK_013 — astroCarryStatus value allowed
    CHECK_014 — productionLockStatus value allowed
    CHECK_015 — PRODUCTION_LOCKED requires humanApprovalRef
    CHECK_016 — IMPLEMENTATION_HANDOFF_DELIVERED requires humanApprovalRef
    CHECK_017 — PRODUCTION_LOCKED not self-claimable without prior validation pass
    CHECK_018 — No PRODUCTION_LOCKED on entries with READINESS_GATE_FAILED
    CHECK_019 — No PRODUCTION_LOCKED on entries with EVIDENCE_MAP_MISSING or STALE
    CHECK_020 — No PRODUCTION_LOCKED on entries with VALIDATION_FAILED or NOT_RUN

Non-authorization statement:
    This tool does not generate schema. It does not create JSON-LD. It does not authorize
    production deployment. Appending an entry to the ledger does not constitute production
    lock authorization. productionLockStatus PRODUCTION_LOCKED may only be set when all
    conditions in the run ledger review guide are met and explicit human approval exists.
"""

import json
import sys
import os
import argparse
import re
from datetime import datetime

# ---------------------------------------------------------------------------
# Constants
# ---------------------------------------------------------------------------

REQUIRED_FIELDS = [
    "runId",
    "prNumber",
    "targetUrl",
    "pageFamily",
    "mode",
    "schemaProfile",
    "truthFingerprint",
    "runDate",
    "readinessStatus",
    "evidenceMapStatus",
    "draftStatus",
    "qaStatus",
    "controllerStatus",
    "validationStatus",
    "implementationStatus",
    "astroCarryStatus",
    "productionLockStatus",
]

ALLOWED_PAGE_FAMILIES = [
    "homepage",
    "program_page",
    "about_page",
    "contact_page",
    "other",
]

ALLOWED_MODES = [
    "MODE_1_CURRENT_WEBSITE",
    "MODE_2_ASTRO_CARRY",
]

ALLOWED_READINESS_STATUS = [
    "READINESS_GATE_PASSED",
    "READINESS_GATE_FAILED",
    "READINESS_GATE_NOT_RUN",
]

ALLOWED_EVIDENCE_MAP_STATUS = [
    "EVIDENCE_MAP_CONFIRMED",
    "EVIDENCE_MAP_MISSING",
    "EVIDENCE_MAP_STALE",
]

ALLOWED_DRAFT_STATUS = [
    "DRAFT_PRODUCED",
    "DRAFT_NOT_PRODUCED",
    "DRAFT_PATCHED",
    "DRAFT_REJECTED",
]

ALLOWED_QA_STATUS = [
    "QA_PASSED",
    "QA_PASSED_WITH_FINDINGS",
    "QA_FAILED",
    "QA_NOT_RUN",
]

ALLOWED_CONTROLLER_STATUS = [
    "CONTROLLER_APPROVED",
    "CONTROLLER_PATCH_REQUIRED",
    "CONTROLLER_REJECTED",
    "CONTROLLER_HUMAN_REVIEW_REQUIRED",
    "CONTROLLER_NOT_RUN",
]

ALLOWED_VALIDATION_STATUS = [
    "VALIDATION_PASSED",
    "VALIDATION_PASSED_WITH_WARNINGS",
    "VALIDATION_FAILED",
    "VALIDATION_NOT_RUN",
]

ALLOWED_IMPLEMENTATION_STATUS = [
    "IMPLEMENTATION_HANDOFF_DELIVERED",
    "IMPLEMENTATION_HANDOFF_PENDING",
    "IMPLEMENTATION_NOT_AUTHORIZED",
    "IMPLEMENTATION_DEFERRED",
]

ALLOWED_ASTRO_CARRY_STATUS = [
    "ASTRO_CARRY_DELIVERED",
    "ASTRO_CARRY_PENDING",
    "ASTRO_CARRY_NOT_AUTHORIZED",
    "ASTRO_CARRY_DEFERRED",
    "ASTRO_CARRY_NOT_APPLICABLE",
]

ALLOWED_PRODUCTION_LOCK_STATUS = [
    "NO_PRODUCTION_LOCKS",
    "PRODUCTION_LOCKED",
]

RUN_ID_PATTERN = re.compile(
    r"^RISE_RUN_[A-Z0-9_]+_\d{8}_\d{3,}$"
)

# ---------------------------------------------------------------------------
# Check functions
# ---------------------------------------------------------------------------

def check_required_fields(entry):
    """CHECK_001 — All required fields present."""
    missing = [f for f in REQUIRED_FIELDS if f not in entry]
    if missing:
        return False, f"CHECK_001 FAIL — Missing required fields: {', '.join(missing)}"
    return True, "CHECK_001 PASS — All required fields present"


def check_run_id_format(entry):
    """CHECK_002 — runId format matches RISE_RUN_<PAGE_FAMILY>_<DATE_YYYYMMDD>_<SEQ>."""
    run_id = entry.get("runId", "")
    if not RUN_ID_PATTERN.match(run_id):
        return False, (
            f"CHECK_002 FAIL — runId '{run_id}' does not match required format "
            "RISE_RUN_<PAGE_FAMILY>_<DATE_YYYYMMDD>_<SEQ> (e.g. RISE_RUN_HOMEPAGE_20260601_001)"
        )
    return True, f"CHECK_002 PASS — runId format valid: {run_id}"


def check_run_id_unique(entry, ledger_entries):
    """CHECK_003 — runId not already in ledger."""
    run_id = entry.get("runId", "")
    existing_ids = [e.get("runId") for e in ledger_entries]
    if run_id in existing_ids:
        return False, f"CHECK_003 FAIL — Duplicate runId '{run_id}' already exists in ledger"
    return True, f"CHECK_003 PASS — runId '{run_id}' is unique"


def check_enum(entry, field, allowed, check_id):
    """Generic enum check."""
    val = entry.get(field)
    if val not in allowed:
        return False, (
            f"{check_id} FAIL — '{field}' value '{val}' not in allowed values: "
            f"{', '.join(allowed)}"
        )
    return True, f"{check_id} PASS — {field}: {val}"


def check_production_lock_has_approval_ref(entry):
    """CHECK_015 — PRODUCTION_LOCKED requires humanApprovalRef."""
    if entry.get("productionLockStatus") == "PRODUCTION_LOCKED":
        ref = entry.get("humanApprovalRef", "").strip() if entry.get("humanApprovalRef") else ""
        if not ref:
            return False, (
                "CHECK_015 FAIL — productionLockStatus is PRODUCTION_LOCKED but "
                "humanApprovalRef is missing or empty. Production lock may not be "
                "self-claimed — an explicit human approval record is required."
            )
    return True, "CHECK_015 PASS — PRODUCTION_LOCKED condition satisfied (or not PRODUCTION_LOCKED)"


def check_implementation_has_approval_ref(entry):
    """CHECK_016 — IMPLEMENTATION_HANDOFF_DELIVERED requires humanApprovalRef."""
    if entry.get("implementationStatus") == "IMPLEMENTATION_HANDOFF_DELIVERED":
        ref = entry.get("humanApprovalRef", "").strip() if entry.get("humanApprovalRef") else ""
        if not ref:
            return False, (
                "CHECK_016 FAIL — implementationStatus is IMPLEMENTATION_HANDOFF_DELIVERED "
                "but humanApprovalRef is missing or empty. No implementation handoff may be "
                "recorded without a human approval reference."
            )
    return True, "CHECK_016 PASS — Implementation handoff condition satisfied"


def check_production_lock_requires_validation_pass(entry):
    """CHECK_017 — PRODUCTION_LOCKED not allowed if validation did not pass."""
    if entry.get("productionLockStatus") == "PRODUCTION_LOCKED":
        val_status = entry.get("validationStatus", "")
        if val_status not in ("VALIDATION_PASSED", "VALIDATION_PASSED_WITH_WARNINGS"):
            return False, (
                f"CHECK_017 FAIL — productionLockStatus is PRODUCTION_LOCKED but "
                f"validationStatus is '{val_status}'. Production lock requires "
                "VALIDATION_PASSED or VALIDATION_PASSED_WITH_WARNINGS."
            )
    return True, "CHECK_017 PASS — Production lock / validation alignment check passed"


def check_production_lock_not_on_failed_readiness(entry):
    """CHECK_018 — No PRODUCTION_LOCKED on entries with READINESS_GATE_FAILED."""
    if (entry.get("productionLockStatus") == "PRODUCTION_LOCKED"
            and entry.get("readinessStatus") == "READINESS_GATE_FAILED"):
        return False, (
            "CHECK_018 FAIL — productionLockStatus is PRODUCTION_LOCKED but "
            "readinessStatus is READINESS_GATE_FAILED. A failed readiness gate "
            "cannot result in a production lock."
        )
    return True, "CHECK_018 PASS — Readiness gate / production lock check passed"


def check_production_lock_not_on_missing_evidence(entry):
    """CHECK_019 — No PRODUCTION_LOCKED if evidence map is missing or stale."""
    if entry.get("productionLockStatus") == "PRODUCTION_LOCKED":
        ev_status = entry.get("evidenceMapStatus", "")
        if ev_status in ("EVIDENCE_MAP_MISSING", "EVIDENCE_MAP_STALE"):
            return False, (
                f"CHECK_019 FAIL — productionLockStatus is PRODUCTION_LOCKED but "
                f"evidenceMapStatus is '{ev_status}'. Production lock requires "
                "EVIDENCE_MAP_CONFIRMED."
            )
    return True, "CHECK_019 PASS — Evidence map / production lock check passed"


def check_production_lock_not_on_validation_failed(entry):
    """CHECK_020 — No PRODUCTION_LOCKED if validation failed or not run."""
    if entry.get("productionLockStatus") == "PRODUCTION_LOCKED":
        val_status = entry.get("validationStatus", "")
        if val_status in ("VALIDATION_FAILED", "VALIDATION_NOT_RUN"):
            return False, (
                f"CHECK_020 FAIL — productionLockStatus is PRODUCTION_LOCKED but "
                f"validationStatus is '{val_status}'. Production lock requires "
                "VALIDATION_PASSED or VALIDATION_PASSED_WITH_WARNINGS."
            )
    return True, "CHECK_020 PASS — Validation / production lock check passed"


def run_all_checks(entry, ledger_entries):
    """Run all safety checks. Returns (all_passed, results_list)."""
    results = []

    results.append(check_required_fields(entry))
    # Only continue field checks if required fields are present
    if not results[-1][0]:
        return False, results

    results.append(check_run_id_format(entry))
    results.append(check_run_id_unique(entry, ledger_entries))
    results.append(check_enum(entry, "pageFamily", ALLOWED_PAGE_FAMILIES, "CHECK_004"))
    results.append(check_enum(entry, "mode", ALLOWED_MODES, "CHECK_005"))
    results.append(check_enum(entry, "readinessStatus", ALLOWED_READINESS_STATUS, "CHECK_006"))
    results.append(check_enum(entry, "evidenceMapStatus", ALLOWED_EVIDENCE_MAP_STATUS, "CHECK_007"))
    results.append(check_enum(entry, "draftStatus", ALLOWED_DRAFT_STATUS, "CHECK_008"))
    results.append(check_enum(entry, "qaStatus", ALLOWED_QA_STATUS, "CHECK_009"))
    results.append(check_enum(entry, "controllerStatus", ALLOWED_CONTROLLER_STATUS, "CHECK_010"))
    results.append(check_enum(entry, "validationStatus", ALLOWED_VALIDATION_STATUS, "CHECK_011"))
    results.append(check_enum(entry, "implementationStatus", ALLOWED_IMPLEMENTATION_STATUS, "CHECK_012"))
    results.append(check_enum(entry, "astroCarryStatus", ALLOWED_ASTRO_CARRY_STATUS, "CHECK_013"))
    results.append(check_enum(entry, "productionLockStatus", ALLOWED_PRODUCTION_LOCK_STATUS, "CHECK_014"))
    results.append(check_production_lock_has_approval_ref(entry))
    results.append(check_implementation_has_approval_ref(entry))
    results.append(check_production_lock_requires_validation_pass(entry))
    results.append(check_production_lock_not_on_failed_readiness(entry))
    results.append(check_production_lock_not_on_missing_evidence(entry))
    results.append(check_production_lock_not_on_validation_failed(entry))

    all_passed = all(r[0] for r in results)
    return all_passed, results


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main():
    parser = argparse.ArgumentParser(
        description=(
            "Safely append a new entry to RUN_LEDGER.json after governed safety checks. "
            "This tool does not generate schema. It does not create JSON-LD. "
            "It does not authorize production deployment."
        )
    )
    parser.add_argument(
        "entry_file",
        help="Path to a JSON file containing the candidate run ledger entry.",
    )
    parser.add_argument(
        "--ledger",
        default="RUN_LEDGER.json",
        help="Path to RUN_LEDGER.json (default: RUN_LEDGER.json in current directory).",
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help=(
            "Run all safety checks and print results, but do not write to the ledger. "
            "No files are modified."
        ),
    )
    args = parser.parse_args()

    # --- Load entry file ---
    if not os.path.isfile(args.entry_file):
        print(f"ERROR: Entry file not found: {args.entry_file}", file=sys.stderr)
        sys.exit(2)

    try:
        with open(args.entry_file, "r", encoding="utf-8") as f:
            entry = json.load(f)
    except json.JSONDecodeError as e:
        print(f"ERROR: Entry file is not valid JSON: {e}", file=sys.stderr)
        sys.exit(2)

    if not isinstance(entry, dict):
        print("ERROR: Entry file must be a JSON object (dict), not an array or scalar.", file=sys.stderr)
        sys.exit(2)

    # --- Load ledger ---
    if not os.path.isfile(args.ledger):
        print(f"ERROR: Ledger file not found: {args.ledger}", file=sys.stderr)
        sys.exit(2)

    try:
        with open(args.ledger, "r", encoding="utf-8") as f:
            ledger = json.load(f)
    except json.JSONDecodeError as e:
        print(f"ERROR: Ledger file is not valid JSON: {e}", file=sys.stderr)
        sys.exit(2)

    if not isinstance(ledger, dict):
        print("ERROR: Ledger file must be a JSON object.", file=sys.stderr)
        sys.exit(2)

    ledger_entries = ledger.get("entries", [])
    if not isinstance(ledger_entries, list):
        print("ERROR: Ledger 'entries' field must be an array.", file=sys.stderr)
        sys.exit(2)

    # --- Run checks ---
    print(f"\nRise FC Run Ledger Append Helper")
    print(f"Entry file : {args.entry_file}")
    print(f"Ledger     : {args.ledger}")
    print(f"Dry run    : {'YES — ledger will not be modified' if args.dry_run else 'NO — ledger will be written on PASS'}")
    print(f"Timestamp  : {datetime.utcnow().isoformat()}Z")
    print()

    all_passed, results = run_all_checks(entry, ledger_entries)

    for passed, message in results:
        status_tag = "PASS" if passed else "FAIL"
        print(f"  [{status_tag}] {message}")

    print()

    if not all_passed:
        failed = [msg for passed, msg in results if not passed]
        print(f"RESULT: FAIL — {len(failed)} check(s) failed. Ledger not modified.")
        for msg in failed:
            print(f"  -> {msg}")
        sys.exit(1)

    if args.dry_run:
        print(f"RESULT: PASS (DRY RUN) — All {len(results)} checks passed.")
        print("Ledger was not modified (--dry-run mode). Remove --dry-run to append.")
        sys.exit(0)

    # --- Append entry ---
    ledger_entries.append(entry)
    ledger["entries"] = ledger_entries

    # Update ledger-level status fields
    has_production_locked = any(
        e.get("productionLockStatus") == "PRODUCTION_LOCKED" for e in ledger_entries
    )
    ledger["productionLockStatus"] = (
        "HAS_PRODUCTION_LOCKS" if has_production_locked else "NO_PRODUCTION_LOCKS"
    )

    # Update ledgerStatus
    if has_production_locked:
        ledger["ledgerStatus"] = "HAS_PRODUCTION_LOCKED_RUNS"
    elif any(e.get("implementationStatus") == "IMPLEMENTATION_HANDOFF_DELIVERED" for e in ledger_entries):
        ledger["ledgerStatus"] = "HAS_COMPLETED_RUNS"
    else:
        ledger["ledgerStatus"] = "HAS_DRAFT_RUNS"

    try:
        with open(args.ledger, "w", encoding="utf-8") as f:
            json.dump(ledger, f, indent=2, ensure_ascii=False)
            f.write("\n")
    except OSError as e:
        print(f"ERROR: Could not write ledger file: {e}", file=sys.stderr)
        sys.exit(2)

    run_id = entry.get("runId", "(unknown)")
    print(f"RESULT: PASS — All {len(results)} checks passed.")
    print(f"Entry '{run_id}' appended to {args.ledger}.")
    print()
    print("Non-authorization notice:")
    print("  Appending an entry does not authorize production deployment.")
    print("  productionLockStatus PRODUCTION_LOCKED requires explicit human approval.")
    sys.exit(0)


if __name__ == "__main__":
    main()
