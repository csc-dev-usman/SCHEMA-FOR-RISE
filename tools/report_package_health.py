#!/usr/bin/env python3
"""
Rise FC Standalone Schema Package — Package Health Reporter v1.0

Reads the package directory and prints a human-readable health summary:
manifest status, active file presence, ledger status, validator/tool
presence, smoke-test fixture presence, Mode 1 status, Mode 2 status,
and production lock status.

This script is READ-ONLY. It does not modify any files.

Usage:
    python tools/report_package_health.py [--help] [package_dir]

Arguments:
    package_dir     Path to the package root (default: current directory)

Exit codes:
    0   Clean — all health checks pass
    1   Warnings or integrity issues found
    2   Input/setup error

Non-authorization notice:
    This script does not generate schema, create JSON-LD, create run
    artifacts, append ledger entries, or authorize any schema production
    activity. It is a read-only reporter only.
"""

import sys
import os
import json

# ---------------------------------------------------------------------------
# Spot-check files — a representative sample confirming key areas are present
# ---------------------------------------------------------------------------

SPOT_CHECK_FILES = {
    "Manifest": "package_manifest.json",
    "Run ledger": "RUN_LEDGER.json",
    "Doctrine boundary": "02_GOVERNING_DOCTRINE/RISE_SCHEMA_SOURCE_TRUTH_BOUNDARY_V1_0.md",
    "Truth view": "03_TRUTH_PACK/RISE_PHASE0_SCHEMA_TRUTH_VIEW_HOMEPAGE_SCOPED_V1_0.json",
    "Homepage schema profile": "07_REFERENCE_LISTS/RISE_HOMEPAGE_SCHEMA_PROFILE_V1_0.md",
    "Master flow": "01_MASTER_FLOW/RISE_STANDALONE_SCHEMA_MASTER_FLOW_V1_0.md",
    "Prompt 00": "04_OPERATOR_PROMPTS/PROMPT_00_STANDALONE_URL_REVIEW_START_V1_0.txt",
    "Prompt 01": "04_OPERATOR_PROMPTS/PROMPT_01_BUILD_NON_PRODUCTION_JSONLD_DRAFT_V1_0.txt",
    "Output bundle validator": "tools/validate_output_bundle.py",
    "Run ledger append helper": "tools/append_run_ledger_entry.py",
    "Run ledger reporter": "tools/report_run_ledger_status.py",
    "Package validator": "tools/validate_package.py",
    "Smoke test runner": "tools/run_standalone_smoke_test.py",
    "Package health reporter": "tools/report_package_health.py",
    "Smoke fixture contract": "08_SMOKE_TESTS/STANDALONE_SMOKE_TEST_FIXTURE_CONTRACT_V1_0.md",
    "Smoke fixture manifest": "08_SMOKE_TESTS/fixtures/standalone_v1_0/fixture_manifest.json",
    "Lint rules": "06_MACHINE_RULES/RISE_SCHEMA_LINT_RULES_V1_0.json",
    "Run ledger schema": "06_MACHINE_RULES/RUN_LEDGER_SCHEMA_V1_0.json",
    "Package expected files": "06_MACHINE_RULES/PACKAGE_EXPECTED_ACTIVE_FILES_V1_0.json",
    "Validation protocol": "05_REFERENCE_WORKFLOW/FINAL_SCHEMA_VALIDATION_PROTOCOL_V1_0.md",
    "Milestone 3 audit": "05_REFERENCE_WORKFLOW/MILESTONE_3_LEDGER_AND_HEALTH_TOOLS_COMPLETION_AUDIT_V1_0.md",
}

SEPARATOR = "=" * 60
SEPARATOR_THIN = "-" * 60


def _present(label):
    print(f"    [OK]     {label}")


def _absent(label):
    print(f"    [ABSENT] {label}")


def _ok(label, value=""):
    msg = f"    [OK]     {label}"
    if value:
        msg += f": {value}"
    print(msg)


def _warn(label, detail=""):
    msg = f"    [WARN]   {label}"
    if detail:
        msg += f": {detail}"
    print(msg)


def _section(title):
    print(f"\n{SEPARATOR_THIN}")
    print(f"  {title}")
    print(SEPARATOR_THIN)


def main():
    if "--help" in sys.argv or "-h" in sys.argv:
        print(__doc__)
        sys.exit(0)

    pkg_dir = sys.argv[1] if len(sys.argv) > 1 else os.getcwd()
    pkg_dir = os.path.abspath(pkg_dir)

    if not os.path.isdir(pkg_dir):
        print(f"ERROR: Package directory not found: {pkg_dir}", file=sys.stderr)
        sys.exit(2)

    warnings = 0

    print(f"\n{SEPARATOR}")
    print("  Rise FC Standalone Schema Package — Health Report")
    print(SEPARATOR)
    print(f"  Package dir : {pkg_dir}")

    # ------------------------------------------------------------------
    # 1. Package manifest
    # ------------------------------------------------------------------
    _section("1. Package manifest")
    manifest_path = os.path.join(pkg_dir, "package_manifest.json")
    manifest = None
    if os.path.isfile(manifest_path):
        try:
            with open(manifest_path, "r", encoding="utf-8") as fh:
                manifest = json.load(fh)
            _ok("package_manifest.json", "present and valid JSON")
            _ok("Status", manifest.get("status", "(missing)"))
            _ok("Package version", manifest.get("packageVersion", "(missing)"))
        except (json.JSONDecodeError, OSError) as exc:
            _warn("package_manifest.json parse error", str(exc))
            warnings += 1
    else:
        _warn("package_manifest.json", "NOT FOUND")
        warnings += 1

    # ------------------------------------------------------------------
    # 2. Run ledger
    # ------------------------------------------------------------------
    _section("2. Run ledger")
    ledger_path = os.path.join(pkg_dir, "RUN_LEDGER.json")
    if os.path.isfile(ledger_path):
        try:
            with open(ledger_path, "r", encoding="utf-8") as fh:
                ledger = json.load(fh)
            ledger_status = ledger.get("ledgerStatus", "(missing)")
            lock_status = ledger.get("productionLockStatus", "(missing)")
            entry_count = len(ledger.get("entries", []))
            _ok("RUN_LEDGER.json", "present and valid JSON")
            _ok("Ledger status", ledger_status)
            _ok("Production lock status", lock_status)
            _ok("Run entries", str(entry_count))
            if lock_status == "HAS_PRODUCTION_LOCKS":
                _warn("Production locks are present — review before any schema work")
                warnings += 1
        except (json.JSONDecodeError, OSError) as exc:
            _warn("RUN_LEDGER.json parse error", str(exc))
            warnings += 1
    else:
        _warn("RUN_LEDGER.json", "NOT FOUND")
        warnings += 1

    # ------------------------------------------------------------------
    # 3. Mode 1 and Mode 2 status
    # ------------------------------------------------------------------
    _section("3. Mode status")
    if manifest:
        mode1 = manifest.get("mode1Runnable", False)
        mode2 = manifest.get("mode2AstroReady", False)
        if mode1:
            _ok("Mode 1 (current website)", "RUNNABLE")
        else:
            _ok("Mode 1 (current website)", "NOT RUNNABLE — waiting for final runnable handoff")
        if mode2:
            _ok("Mode 2 (Astro carry)", "READY")
        else:
            _ok("Mode 2 (Astro carry)", "NOT READY — waiting for Astro carry gates")
    else:
        _warn("Mode status", "Cannot determine — manifest unavailable")
        warnings += 1

    # ------------------------------------------------------------------
    # 4. Production safety flags
    # ------------------------------------------------------------------
    _section("4. Production safety flags")
    if manifest:
        safety_flags = {
            "schemaOutputCreated": False,
            "jsonLdCreated": False,
            "currentWebsiteImplementationAuthorized": False,
            "astroAttachmentAuthorized": False,
            "mode1Runnable": False,
        }
        all_safe = True
        for flag, expected_false in safety_flags.items():
            actual = manifest.get(flag, False)
            if actual is expected_false:
                _ok(flag, str(actual))
            else:
                _warn(flag, f"UNEXPECTED VALUE: {actual}")
                warnings += 1
                all_safe = False
        if all_safe:
            _ok("All production safety flags", "correct")
    else:
        _warn("Production safety flags", "Cannot check — manifest unavailable")
        warnings += 1

    # ------------------------------------------------------------------
    # 5. Smoke test fixture presence
    # ------------------------------------------------------------------
    _section("5. Smoke test fixture")
    if manifest:
        stf = manifest.get("smokeTestFixtureAdded", False)
        str_ = manifest.get("smokeTestRunnerAdded", False)
        ph = manifest.get("packageHealthReporterAdded", False)
        m3 = manifest.get("milestone3LedgerAndHealthToolsComplete", False)
        _ok("smokeTestFixtureAdded", str(stf))
        _ok("smokeTestRunnerAdded", str(str_))
        _ok("packageHealthReporterAdded", str(ph))
        _ok("milestone3LedgerAndHealthToolsComplete", str(m3))
    else:
        _warn("Smoke test fixture flags", "Cannot check — manifest unavailable")
        warnings += 1

    fixture_manifest_path = os.path.join(
        pkg_dir, "08_SMOKE_TESTS", "fixtures", "standalone_v1_0", "fixture_manifest.json"
    )
    if os.path.isfile(fixture_manifest_path):
        _ok("Fixture manifest file", "present")
    else:
        _warn("Fixture manifest file", "NOT FOUND at 08_SMOKE_TESTS/fixtures/standalone_v1_0/fixture_manifest.json")
        warnings += 1

    # ------------------------------------------------------------------
    # 6. Validator and tool presence
    # ------------------------------------------------------------------
    _section("6. Validator and tool presence")
    tools_to_check = [
        ("Output bundle validator", "tools/validate_output_bundle.py"),
        ("Run ledger append helper", "tools/append_run_ledger_entry.py"),
        ("Run ledger reporter", "tools/report_run_ledger_status.py"),
        ("Package validator", "tools/validate_package.py"),
        ("Smoke test runner", "tools/run_standalone_smoke_test.py"),
        ("Package health reporter", "tools/report_package_health.py"),
    ]
    for label, rel in tools_to_check:
        if os.path.isfile(os.path.join(pkg_dir, rel)):
            _present(f"{label} ({rel})")
        else:
            _warn(f"{label} ({rel})", "NOT FOUND")
            warnings += 1

    # ------------------------------------------------------------------
    # 7. Spot-check key files
    # ------------------------------------------------------------------
    _section("7. Key file spot-checks")
    absent_count = 0
    for label, rel in SPOT_CHECK_FILES.items():
        path = os.path.join(pkg_dir, rel)
        if os.path.isfile(path):
            _present(f"{label}")
        else:
            _absent(f"{label} ({rel})")
            absent_count += 1
    if absent_count > 0:
        _warn(f"{absent_count} expected file(s) absent")
        warnings += 1

    # ------------------------------------------------------------------
    # 8. No JSON-LD files
    # ------------------------------------------------------------------
    _section("8. JSON-LD safety check")
    jsonld_files = []
    for root, _dirs, files in os.walk(pkg_dir):
        # Skip .git
        _dirs[:] = [d for d in _dirs if d != ".git"]
        for fname in files:
            if fname.endswith(".jsonld"):
                jsonld_files.append(os.path.relpath(os.path.join(root, fname), pkg_dir))
    if not jsonld_files:
        _ok("No .jsonld files", "package is clean")
    else:
        _warn(f"{len(jsonld_files)} .jsonld file(s) found — UNEXPECTED", str(jsonld_files))
        warnings += 1

    # ------------------------------------------------------------------
    # Summary
    # ------------------------------------------------------------------
    print(f"\n{SEPARATOR}")
    print("  Health report summary")
    print(SEPARATOR)
    if warnings == 0:
        print("  RESULT: CLEAN — No health warnings.")
    else:
        print(f"  RESULT: {warnings} WARNING(S) — Review items above.")

    print()
    print("  Non-authorization notice:")
    print("  This report does not authorize schema production or production deployment.")
    print("  It is a read-only structural health check only. No files were modified.")
    print()

    sys.exit(0 if warnings == 0 else 1)


if __name__ == "__main__":
    main()
