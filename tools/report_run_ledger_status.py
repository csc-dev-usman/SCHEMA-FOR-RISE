#!/usr/bin/env python3
"""
report_run_ledger_status.py — Rise FC Standalone Schema Operator Package

Read-only ledger status reporter. Reads RUN_LEDGER.json and prints a human-readable
summary of the ledger state, entry counts, and status breakdown.

This tool is read-only. It does not modify any files.

Usage:
    python tools/report_run_ledger_status.py [ledger_file]

Arguments:
    ledger_file     Path to RUN_LEDGER.json. Defaults to RUN_LEDGER.json in the
                    current directory.

Exit codes:
    0 — Report printed successfully.
    1 — Ledger integrity warning found (entries present with suspicious state).
    2 — Input file error (missing file, parse error, etc.).

Non-authorization statement:
    This tool does not generate schema. It does not create JSON-LD. It does not
    modify the ledger. It does not authorize production deployment. Report output
    is informational only.
"""

import json
import sys
import os
import argparse
from collections import Counter

# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

def load_ledger(path):
    if not os.path.isfile(path):
        print(f"ERROR: Ledger file not found: {path}", file=sys.stderr)
        sys.exit(2)
    try:
        with open(path, "r", encoding="utf-8") as f:
            return json.load(f)
    except json.JSONDecodeError as e:
        print(f"ERROR: Ledger file is not valid JSON: {e}", file=sys.stderr)
        sys.exit(2)


def section(title):
    print(f"\n{'=' * 60}")
    print(f"  {title}")
    print(f"{'=' * 60}")


def row(label, value, width=36):
    print(f"  {label:<{width}} {value}")


def count_breakdown(entries, field):
    counts = Counter(e.get(field, "(missing)") for e in entries)
    return dict(sorted(counts.items()))


# ---------------------------------------------------------------------------
# Report
# ---------------------------------------------------------------------------

def report(ledger, path):
    entries = ledger.get("entries", [])
    total = len(entries)
    warnings = []

    # --- Header ---
    print()
    print(f"Rise FC Run Ledger Status Report")
    print(f"Ledger file : {path}")
    print()

    # --- Ledger-level fields ---
    section("Ledger metadata")
    row("ledgerName:", ledger.get("ledgerName", "(missing)"))
    row("ledgerVersion:", ledger.get("ledgerVersion", "(missing)"))
    row("schemaVersion:", ledger.get("schemaVersion", "(missing)"))
    row("status:", ledger.get("status", "(missing)"))
    row("ledgerStatus:", ledger.get("ledgerStatus", "(missing)"))
    row("productionLockStatus:", ledger.get("productionLockStatus", "(missing)"))
    row("lastUpdatedByPr:", str(ledger.get("lastUpdatedByPr", "(missing)")))

    # --- Safety rules ---
    section("Safety rules (ledger level)")
    safety = ledger.get("safetyRules", {})
    if not safety:
        print("  (no safetyRules block found)")
    else:
        for k, v in safety.items():
            row(f"{k}:", str(v))

    # --- Entry counts ---
    section("Entry summary")
    row("Total entries:", str(total))

    if total == 0:
        print()
        print("  Ledger is bootstrap-empty. No governed runs have been recorded.")
        print("  No schema has been generated. No production locks exist.")
        print()
        print("Non-authorization notice:")
        print("  This report is informational only. No files have been modified.")
        return 0

    # --- Status breakdowns ---
    section("Status breakdowns")

    breakdowns = [
        ("pageFamily", "Page family"),
        ("mode", "Mode"),
        ("readinessStatus", "Readiness gate"),
        ("evidenceMapStatus", "Evidence map"),
        ("draftStatus", "Draft status"),
        ("qaStatus", "QA status"),
        ("controllerStatus", "Controller status"),
        ("validationStatus", "Validation status"),
        ("implementationStatus", "Implementation status"),
        ("astroCarryStatus", "Astro carry status"),
        ("productionLockStatus", "Production lock status"),
    ]

    for field, label in breakdowns:
        counts = count_breakdown(entries, field)
        print(f"\n  {label}:")
        for val, count in counts.items():
            print(f"    {val:<45} {count}")

    # --- Production lock check ---
    section("Production lock integrity")
    production_locked_entries = [
        e for e in entries if e.get("productionLockStatus") == "PRODUCTION_LOCKED"
    ]
    if not production_locked_entries:
        print("  No entries with PRODUCTION_LOCKED. productionLockStatus: NO_PRODUCTION_LOCKS")
    else:
        print(f"  {len(production_locked_entries)} PRODUCTION_LOCKED entry/entries found:")
        for e in production_locked_entries:
            run_id = e.get("runId", "(missing)")
            ref = e.get("humanApprovalRef", "(missing)")
            print(f"    runId: {run_id}")
            print(f"    humanApprovalRef: {ref}")
            if not ref or ref.strip() == "(missing)":
                msg = f"WARNING — PRODUCTION_LOCKED entry '{run_id}' has no humanApprovalRef."
                warnings.append(msg)
                print(f"    *** {msg}")

    # --- Implementation handoff check ---
    section("Implementation handoff integrity")
    delivered = [
        e for e in entries
        if e.get("implementationStatus") == "IMPLEMENTATION_HANDOFF_DELIVERED"
    ]
    if not delivered:
        print("  No entries with IMPLEMENTATION_HANDOFF_DELIVERED.")
    else:
        print(f"  {len(delivered)} IMPLEMENTATION_HANDOFF_DELIVERED entry/entries found:")
        for e in delivered:
            run_id = e.get("runId", "(missing)")
            ref = e.get("humanApprovalRef", "(missing)")
            print(f"    runId: {run_id}")
            print(f"    humanApprovalRef: {ref}")
            if not ref or ref.strip() == "(missing)":
                msg = f"WARNING — IMPLEMENTATION_HANDOFF_DELIVERED entry '{run_id}' has no humanApprovalRef."
                warnings.append(msg)
                print(f"    *** {msg}")

    # --- Run ID list ---
    section("All run IDs")
    for e in entries:
        run_id = e.get("runId", "(missing)")
        run_date = e.get("runDate", "(missing)")
        page = e.get("pageFamily", "(missing)")
        mode = e.get("mode", "(missing)")
        lock = e.get("productionLockStatus", "(missing)")
        print(f"  {run_id}")
        print(f"    date={run_date}  page={page}  mode={mode}  lock={lock}")

    # --- Summary ---
    section("Summary")
    row("Total entries:", str(total))
    row("productionLockStatus (ledger):", ledger.get("productionLockStatus", "(missing)"))
    row("Warnings:", str(len(warnings)))

    if warnings:
        print()
        print("  Warnings:")
        for w in warnings:
            print(f"    -> {w}")

    print()
    print("Non-authorization notice:")
    print("  This report is informational only. No files have been modified.")
    print("  Production lock status must not be set without explicit human approval.")

    return 1 if warnings else 0


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main():
    parser = argparse.ArgumentParser(
        description=(
            "Read-only reporter for RUN_LEDGER.json. Prints ledger state, entry counts, "
            "and status breakdown. Does not modify any files. "
            "This tool does not generate schema or JSON-LD."
        )
    )
    parser.add_argument(
        "ledger_file",
        nargs="?",
        default="RUN_LEDGER.json",
        help="Path to RUN_LEDGER.json (default: RUN_LEDGER.json in current directory).",
    )
    args = parser.parse_args()

    ledger = load_ledger(args.ledger_file)
    exit_code = report(ledger, args.ledger_file)
    sys.exit(exit_code)


if __name__ == "__main__":
    main()
