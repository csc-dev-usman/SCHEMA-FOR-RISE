#!/usr/bin/env python3
"""
Rise FC Standalone Schema Package — Smoke Test Runner v1.0

Runs a suite of smoke tests against the canned fake fixture
(08_SMOKE_TESTS/fixtures/standalone_v1_0/) to verify that
validator tools behave correctly against synthetic inputs.

Usage:
    python tools/run_standalone_smoke_test.py [--help] [package_dir]

Arguments:
    package_dir     Path to the package root (default: current directory)

Exit codes:
    0   PASS — all smoke tests passed
    1   FAIL — one or more smoke tests failed
    2   Input/setup error

Non-authorization notice:
    This script does not generate schema, create JSON-LD, create real
    run artifacts, append real ledger entries, or authorize any schema
    production activity. It runs only against the fake fixture set.
    PASS confirms tooling behaves correctly against synthetic inputs only.
"""

import sys
import os
import json
import subprocess

# ---------------------------------------------------------------------------
# Constants
# ---------------------------------------------------------------------------

FIXTURE_REL_PATH = os.path.join(
    "08_SMOKE_TESTS", "fixtures", "standalone_v1_0"
)

FIXTURE_MANIFEST_REL = os.path.join(FIXTURE_REL_PATH, "fixture_manifest.json")

FIXTURE_DATA_FILES = [
    os.path.join(FIXTURE_REL_PATH, "fixture_manifest.json"),
    os.path.join(FIXTURE_REL_PATH, "fake_run_metadata.json"),
    os.path.join(FIXTURE_REL_PATH, "fake_output_bundle_manifest.json"),
    os.path.join(FIXTURE_REL_PATH, "fake_controller_decision.json"),
    os.path.join(FIXTURE_REL_PATH, "fake_validator_results.json"),
]

REQUIRED_SAFETY_FIELDS = ["_isFakeFixture", "_notRealRunArtifact", "_fixtureVersion"]

BLOCKED_URL_PATTERNS = ["risefcsoccer.com", "risefcsoccer.org"]

PACKAGE_VALIDATOR_REL = os.path.join("tools", "validate_package.py")

SEPARATOR = "=" * 60


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

def _pass(label, detail=""):
    msg = f"  [PASS] {label}"
    if detail:
        msg += f" — {detail}"
    print(msg)
    return True


def _fail(label, reason):
    print(f"  [FAIL] {label} — {reason}")
    return False


def _header(title):
    print(f"\n{SEPARATOR}")
    print(f"  {title}")
    print(SEPARATOR)


# ---------------------------------------------------------------------------
# Smoke test checks
# ---------------------------------------------------------------------------

def check_fixture_dir_present(pkg_dir):
    """SMOKE_001 — Fixture directory exists."""
    fixture_dir = os.path.join(pkg_dir, FIXTURE_REL_PATH)
    if os.path.isdir(fixture_dir):
        return _pass("SMOKE_001", "Fixture directory present")
    return _fail("SMOKE_001 Fixture directory present",
                 f"Not found: {FIXTURE_REL_PATH}")


def check_fixture_manifest_present(pkg_dir):
    """SMOKE_002 — fixture_manifest.json present."""
    path = os.path.join(pkg_dir, FIXTURE_MANIFEST_REL)
    if os.path.isfile(path):
        return _pass("SMOKE_002", "fixture_manifest.json present")
    return _fail("SMOKE_002 fixture_manifest.json present",
                 f"Not found: {FIXTURE_MANIFEST_REL}")


def check_all_fixture_files_present(pkg_dir):
    """SMOKE_003 — All expected fixture data files present."""
    missing = []
    for rel in FIXTURE_DATA_FILES:
        if not os.path.isfile(os.path.join(pkg_dir, rel)):
            missing.append(rel)
    if not missing:
        return _pass("SMOKE_003", f"All {len(FIXTURE_DATA_FILES)} fixture files present")
    return _fail("SMOKE_003 All fixture files present",
                 f"Missing: {missing}")


def check_fixture_files_parse_as_json(pkg_dir):
    """SMOKE_004 — All fixture JSON files parse cleanly."""
    errors = []
    for rel in FIXTURE_DATA_FILES:
        path = os.path.join(pkg_dir, rel)
        if not os.path.isfile(path):
            continue
        try:
            with open(path, "r", encoding="utf-8") as fh:
                json.load(fh)
        except (json.JSONDecodeError, OSError) as exc:
            errors.append(f"{rel}: {exc}")
    if not errors:
        return _pass("SMOKE_004", f"All {len(FIXTURE_DATA_FILES)} fixture files parse as valid JSON")
    return _fail("SMOKE_004 Fixture JSON parse", f"Errors: {errors}")


def check_fixture_safety_headers(pkg_dir):
    """SMOKE_005 — All fixture JSON files carry required safety fields."""
    violations = []
    for rel in FIXTURE_DATA_FILES:
        path = os.path.join(pkg_dir, rel)
        if not os.path.isfile(path):
            continue
        try:
            with open(path, "r", encoding="utf-8") as fh:
                data = json.load(fh)
        except (json.JSONDecodeError, OSError):
            continue
        for field in REQUIRED_SAFETY_FIELDS:
            if field not in data:
                violations.append(f"{rel}: missing '{field}'")
            elif field == "_isFakeFixture" and data[field] is not True:
                violations.append(f"{rel}: '_isFakeFixture' must be true")
            elif field == "_notRealRunArtifact" and data[field] is not True:
                violations.append(f"{rel}: '_notRealRunArtifact' must be true")
    if not violations:
        return _pass("SMOKE_005", "All fixture files carry required safety headers")
    return _fail("SMOKE_005 Fixture safety headers", f"Violations: {violations}")


def check_no_real_rise_urls_in_fixtures(pkg_dir):
    """SMOKE_006 — No real Rise FC URLs in fixture data files."""
    fixture_dir = os.path.join(pkg_dir, FIXTURE_REL_PATH)
    if not os.path.isdir(fixture_dir):
        return _fail("SMOKE_006 No real Rise URLs in fixtures",
                     "Fixture directory not found")
    violations = []
    for fname in os.listdir(fixture_dir):
        if not fname.endswith(".json"):
            continue
        fpath = os.path.join(fixture_dir, fname)
        try:
            with open(fpath, "r", encoding="utf-8") as fh:
                content = fh.read()
        except OSError:
            continue
        for pattern in BLOCKED_URL_PATTERNS:
            if pattern in content:
                violations.append(f"{fname}: contains '{pattern}'")
    if not violations:
        return _pass("SMOKE_006", "No real Rise FC URLs found in fixture JSON files")
    return _fail("SMOKE_006 No real Rise URLs in fixtures",
                 f"Violations: {violations}")


def check_no_production_lock_in_fixtures(pkg_dir):
    """SMOKE_007 — No fixture claims PRODUCTION_LOCKED."""
    violations = []
    for rel in FIXTURE_DATA_FILES:
        path = os.path.join(pkg_dir, rel)
        if not os.path.isfile(path):
            continue
        try:
            with open(path, "r", encoding="utf-8") as fh:
                data = json.load(fh)
        except (json.JSONDecodeError, OSError):
            continue
        lock_val = data.get("productionLockStatus", "")
        if lock_val == "PRODUCTION_LOCKED":
            violations.append(f"{rel}: productionLockStatus is PRODUCTION_LOCKED")
        if data.get("productionLockAuthorized") is True:
            violations.append(f"{rel}: productionLockAuthorized is true")
    if not violations:
        return _pass("SMOKE_007", "No fixture claims PRODUCTION_LOCKED")
    return _fail("SMOKE_007 No production lock in fixtures",
                 f"Violations: {violations}")


def check_no_jsonld_in_fixture_dir(pkg_dir):
    """SMOKE_008 — No .jsonld files in fixture directory."""
    fixture_dir = os.path.join(pkg_dir, FIXTURE_REL_PATH)
    if not os.path.isdir(fixture_dir):
        return _pass("SMOKE_008", "Fixture directory absent — no .jsonld files possible")
    found = []
    for root, _dirs, files in os.walk(fixture_dir):
        for fname in files:
            if fname.endswith(".jsonld"):
                found.append(os.path.relpath(os.path.join(root, fname), pkg_dir))
    if not found:
        return _pass("SMOKE_008", "No .jsonld files in fixture directory")
    return _fail("SMOKE_008 No .jsonld in fixture dir",
                 f"Found: {found}")


def check_fixture_manifest_status(pkg_dir):
    """SMOKE_009 — fixture_manifest.json status field is FAKE_FIXTURE_ONLY."""
    path = os.path.join(pkg_dir, FIXTURE_MANIFEST_REL)
    if not os.path.isfile(path):
        return _fail("SMOKE_009 Fixture manifest status",
                     "fixture_manifest.json not found")
    try:
        with open(path, "r", encoding="utf-8") as fh:
            data = json.load(fh)
    except (json.JSONDecodeError, OSError) as exc:
        return _fail("SMOKE_009 Fixture manifest status", str(exc))
    status = data.get("status", "")
    if status == "FAKE_FIXTURE_ONLY":
        return _pass("SMOKE_009", f"fixture_manifest.json status is '{status}'")
    return _fail("SMOKE_009 Fixture manifest status",
                 f"Expected 'FAKE_FIXTURE_ONLY', got '{status}'")


def check_fixture_safety_constraints_block(pkg_dir):
    """SMOKE_010 — fixture_manifest.json safetyConstraints block is correct."""
    path = os.path.join(pkg_dir, FIXTURE_MANIFEST_REL)
    if not os.path.isfile(path):
        return _fail("SMOKE_010 Fixture safetyConstraints",
                     "fixture_manifest.json not found")
    try:
        with open(path, "r", encoding="utf-8") as fh:
            data = json.load(fh)
    except (json.JSONDecodeError, OSError) as exc:
        return _fail("SMOKE_010 Fixture safetyConstraints", str(exc))
    sc = data.get("safetyConstraints", {})
    violations = []
    must_be_true = [
        "usesExampleInvalidOnly", "noRealRiseData", "noRealContactDetails",
        "noRealSocialUrls", "noRealCoordinates", "noJsonLdOutput",
        "noEmittedSchemaFile", "noProductionLock", "noRealRunId",
    ]
    must_be_false = ["schemaOutputCreated", "jsonLdCreated", "phase0MutationAllowed"]
    for key in must_be_true:
        if sc.get(key) is not True:
            violations.append(f"safetyConstraints.{key} must be true")
    for key in must_be_false:
        if sc.get(key) is not False:
            violations.append(f"safetyConstraints.{key} must be false")
    if not violations:
        return _pass("SMOKE_010", "fixture_manifest.json safetyConstraints block is correct")
    return _fail("SMOKE_010 Fixture safetyConstraints",
                 f"Violations: {violations}")


def check_package_validator_still_passes(pkg_dir):
    """SMOKE_011 — package validator returns exit code 0 (PASS)."""
    validator_path = os.path.join(pkg_dir, PACKAGE_VALIDATOR_REL)
    if not os.path.isfile(validator_path):
        return _fail("SMOKE_011 Package validator pass",
                     f"Validator not found: {PACKAGE_VALIDATOR_REL}")
    try:
        result = subprocess.run(
            [sys.executable, validator_path, pkg_dir],
            capture_output=True,
            text=True,
            timeout=60,
        )
        if result.returncode == 0:
            return _pass("SMOKE_011", "Package validator returns PASS (exit 0)")
        output_tail = (result.stdout + result.stderr).strip()[-300:]
        return _fail("SMOKE_011 Package validator pass",
                     f"Exit code {result.returncode}. Output tail: {output_tail}")
    except subprocess.TimeoutExpired:
        return _fail("SMOKE_011 Package validator pass", "Timed out after 60s")
    except OSError as exc:
        return _fail("SMOKE_011 Package validator pass", str(exc))


def check_run_ledger_bootstrap_empty(pkg_dir):
    """SMOKE_012 — RUN_LEDGER.json is bootstrap-empty (no real run entries)."""
    ledger_path = os.path.join(pkg_dir, "RUN_LEDGER.json")
    if not os.path.isfile(ledger_path):
        return _fail("SMOKE_012 Ledger bootstrap empty", "RUN_LEDGER.json not found")
    try:
        with open(ledger_path, "r", encoding="utf-8") as fh:
            data = json.load(fh)
    except (json.JSONDecodeError, OSError) as exc:
        return _fail("SMOKE_012 Ledger bootstrap empty", str(exc))
    entries = data.get("entries", [])
    lock = data.get("productionLockStatus", "")
    if len(entries) == 0 and lock == "NO_PRODUCTION_LOCKS":
        return _pass("SMOKE_012",
                     f"Ledger has 0 entries and productionLockStatus is '{lock}'")
    return _fail("SMOKE_012 Ledger bootstrap empty",
                 f"entries={len(entries)}, productionLockStatus='{lock}'")


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

CHECKS = [
    check_fixture_dir_present,
    check_fixture_manifest_present,
    check_all_fixture_files_present,
    check_fixture_files_parse_as_json,
    check_fixture_safety_headers,
    check_no_real_rise_urls_in_fixtures,
    check_no_production_lock_in_fixtures,
    check_no_jsonld_in_fixture_dir,
    check_fixture_manifest_status,
    check_fixture_safety_constraints_block,
    check_package_validator_still_passes,
    check_run_ledger_bootstrap_empty,
]


def main():
    if "--help" in sys.argv or "-h" in sys.argv:
        print(__doc__)
        sys.exit(0)

    pkg_dir = sys.argv[1] if len(sys.argv) > 1 else os.getcwd()
    pkg_dir = os.path.abspath(pkg_dir)

    if not os.path.isdir(pkg_dir):
        print(f"ERROR: Package directory not found: {pkg_dir}", file=sys.stderr)
        sys.exit(2)

    print("Rise FC Standalone Smoke Test Runner v1.0")
    print(f"Package dir  : {pkg_dir}")
    print(f"Fixture path : {os.path.join(pkg_dir, FIXTURE_REL_PATH)}")

    _header("Smoke test results")

    passed = 0
    failed = 0
    for check_fn in CHECKS:
        ok = check_fn(pkg_dir)
        if ok:
            passed += 1
        else:
            failed += 1

    _header("Summary")
    print(f"  Checks run : {len(CHECKS)}")
    print(f"  Passed     : {passed}")
    print(f"  Failed     : {failed}")
    print()

    if failed == 0:
        print("RESULT: PASS — All smoke tests passed.")
    else:
        print(f"RESULT: FAIL — {failed} smoke test(s) failed.")

    print()
    print("Non-authorization notice:")
    print("  PASS confirms tooling behaves correctly against synthetic inputs only.")
    print("  This result does not authorize schema production or production deployment.")
    print("  No real Rise FC schema was generated. No real run artifacts were created.")

    sys.exit(0 if failed == 0 else 1)


if __name__ == "__main__":
    main()
