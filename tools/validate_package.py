#!/usr/bin/env python3
"""
validate_package.py — Rise FC Standalone Schema Operator Package

Package-level validator. Checks that the Rise FC standalone schema operator
package directory is structurally sound, contains all expected active files,
has no unauthorized artifacts, and that key JSON files parse correctly.

Usage:
    python tools/validate_package.py [package_dir] [--expected-files PATH]

Arguments:
    package_dir         Root directory of the package. Defaults to the current
                        working directory.
    --expected-files    Path to PACKAGE_EXPECTED_ACTIVE_FILES_V1_0.json.
                        Defaults to 06_MACHINE_RULES/PACKAGE_EXPECTED_ACTIVE_FILES_V1_0.json
                        relative to package_dir.

Exit codes:
    0 — All checks passed. Package is structurally sound.
    1 — One or more checks failed. Package has issues.
    2 — Input error (missing package dir, missing expected files contract, etc.).

Checks performed:
    CHECK_PKG_001 — package_manifest.json present and parses as valid JSON
    CHECK_PKG_002 — RUN_LEDGER.json present and parses as valid JSON
    CHECK_PKG_003 — All required active files are present
    CHECK_PKG_004 — Key JSON schema files in 06_MACHINE_RULES/ parse as valid JSON
    CHECK_PKG_005 — No JSON-LD files present (*.jsonld)
    CHECK_PKG_006 — No sample_runs/ directory present
    CHECK_PKG_007 — package_manifest.json does not claim production readiness
    CHECK_PKG_008 — package_manifest.json does not claim Mode 1 is runnable
                    (unless final runnable handoff explicitly authorizes it)
    CHECK_PKG_009 — package_manifest.json does not claim schema output was created
    CHECK_PKG_010 — RUN_LEDGER.json productionLockStatus is NO_PRODUCTION_LOCKS
                    (when ledger has no entries)
    CHECK_PKG_011 — No fake passing report files present
    CHECK_PKG_012 — Truth-pack scoped truth view parses as valid JSON (read-only check)

Non-authorization statement:
    This tool does not generate schema. It does not create JSON-LD. It does not
    modify any package files. A PASS result confirms structural integrity only —
    it does not authorize schema production, production deployment, or any
    implementation action.
"""

import json
import sys
import os
import glob
import argparse

# ---------------------------------------------------------------------------
# Constants
# ---------------------------------------------------------------------------

KEY_JSON_SCHEMAS = [
    "06_MACHINE_RULES/OUTPUT_BUNDLE_MANIFEST_SCHEMA_V1_0.json",
    "06_MACHINE_RULES/RUN_METADATA_SCHEMA_V1_0.json",
    "06_MACHINE_RULES/CONTROLLER_DECISION_SCHEMA_V1_0.json",
    "06_MACHINE_RULES/VALIDATOR_RESULTS_SCHEMA_V1_0.json",
    "06_MACHINE_RULES/EVIDENCE_MAP_SCHEMA_V1_0.json",
    "06_MACHINE_RULES/RISE_SCHEMA_LINT_RULES_V1_0.json",
    "06_MACHINE_RULES/OUTPUT_BUNDLE_VALIDATOR_EXPECTED_FILES_V1_0.json",
    "06_MACHINE_RULES/CLAUDE_QA_FINDING_SCHEMA_V1_0.json",
    "06_MACHINE_RULES/CONTROLLER_REVIEW_PACKET_SCHEMA_V1_0.json",
    "06_MACHINE_RULES/RUN_LEDGER_SCHEMA_V1_0.json",
    "06_MACHINE_RULES/PACKAGE_EXPECTED_ACTIVE_FILES_V1_0.json",
]

TRUTH_PACK_JSON = "03_TRUTH_PACK/RISE_PHASE0_SCHEMA_TRUTH_VIEW_HOMEPAGE_SCOPED_V1_0.json"

PRODUCTION_READINESS_FLAGS = [
    "currentWebsiteImplementationAuthorized",
    "astroAttachmentAuthorized",
    "productionLocked",
]

FAKE_REPORT_PATTERNS = [
    "**/fake_passing_report*",
    "**/fake_production_approval*",
    "**/mock_schema_output*",
]

JSONLD_PATTERNS = [
    "**/*.jsonld",
]

BLOCKED_DIR_NAMES = [
    "sample_runs",
]


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

def load_json(path):
    """Load and parse a JSON file. Returns (data, error_string)."""
    try:
        with open(path, "r", encoding="utf-8") as f:
            return json.load(f), None
    except json.JSONDecodeError as e:
        return None, str(e)
    except OSError as e:
        return None, str(e)


def find_files_by_pattern(root, pattern):
    """Find files matching a glob pattern under root, excluding .git."""
    matches = []
    for path in glob.glob(os.path.join(root, pattern), recursive=True):
        if ".git" not in path.replace("\\", "/").split("/"):
            matches.append(path)
    return matches


def find_dirs_by_name(root, dirname):
    """Find directories with a given name under root, excluding .git."""
    matches = []
    for dirpath, dirnames, _ in os.walk(root):
        # Skip .git
        dirnames[:] = [d for d in dirnames if d != ".git"]
        if os.path.basename(dirpath) == dirname:
            matches.append(dirpath)
    return matches


def section(title):
    print(f"\n{'=' * 60}")
    print(f"  {title}")
    print(f"{'=' * 60}")


# ---------------------------------------------------------------------------
# Check functions
# ---------------------------------------------------------------------------

def check_manifest(root):
    """CHECK_PKG_001 — package_manifest.json present and valid JSON."""
    path = os.path.join(root, "package_manifest.json")
    if not os.path.isfile(path):
        return False, "CHECK_PKG_001 FAIL — package_manifest.json not found", None
    data, err = load_json(path)
    if err:
        return False, f"CHECK_PKG_001 FAIL — package_manifest.json parse error: {err}", None
    return True, "CHECK_PKG_001 PASS — package_manifest.json present and valid", data


def check_ledger(root):
    """CHECK_PKG_002 — RUN_LEDGER.json present and valid JSON."""
    path = os.path.join(root, "RUN_LEDGER.json")
    if not os.path.isfile(path):
        return False, "CHECK_PKG_002 FAIL — RUN_LEDGER.json not found", None
    data, err = load_json(path)
    if err:
        return False, f"CHECK_PKG_002 FAIL — RUN_LEDGER.json parse error: {err}", None
    return True, "CHECK_PKG_002 PASS — RUN_LEDGER.json present and valid", data


def check_required_files(root, expected_files):
    """CHECK_PKG_003 — All required active files are present."""
    required = expected_files.get("required", [])
    missing = []
    for rel_path in required:
        full_path = os.path.join(root, rel_path.replace("/", os.sep))
        if not os.path.isfile(full_path):
            missing.append(rel_path)
    if missing:
        lines = "\n".join(f"    MISSING: {p}" for p in missing)
        return False, f"CHECK_PKG_003 FAIL — {len(missing)} required file(s) missing:\n{lines}"
    return True, f"CHECK_PKG_003 PASS — All {len(required)} required files present"


def check_key_json_schemas(root):
    """CHECK_PKG_004 — Key JSON schema files parse as valid JSON."""
    failures = []
    for rel_path in KEY_JSON_SCHEMAS:
        full_path = os.path.join(root, rel_path.replace("/", os.sep))
        if not os.path.isfile(full_path):
            failures.append(f"{rel_path} — NOT FOUND")
            continue
        _, err = load_json(full_path)
        if err:
            failures.append(f"{rel_path} — PARSE ERROR: {err}")
    if failures:
        lines = "\n".join(f"    {f}" for f in failures)
        return False, f"CHECK_PKG_004 FAIL — {len(failures)} JSON schema file(s) failed:\n{lines}"
    return True, f"CHECK_PKG_004 PASS — All {len(KEY_JSON_SCHEMAS)} key JSON schemas valid"


def check_no_jsonld_files(root):
    """CHECK_PKG_005 — No JSON-LD files (*.jsonld) present."""
    found = []
    for pattern in JSONLD_PATTERNS:
        found.extend(find_files_by_pattern(root, pattern))
    if found:
        lines = "\n".join(f"    BLOCKED: {p}" for p in found)
        return False, f"CHECK_PKG_005 FAIL — {len(found)} JSON-LD file(s) found (not permitted at bootstrap):\n{lines}"
    return True, "CHECK_PKG_005 PASS — No JSON-LD files present"


def check_no_sample_runs(root):
    """CHECK_PKG_006 — No sample_runs/ directory present."""
    found = []
    for dirname in BLOCKED_DIR_NAMES:
        found.extend(find_dirs_by_name(root, dirname))
    if found:
        lines = "\n".join(f"    BLOCKED: {d}" for d in found)
        return False, f"CHECK_PKG_006 FAIL — Blocked directory/directories found:\n{lines}"
    return True, "CHECK_PKG_006 PASS — No blocked directories present"


def check_no_production_readiness(manifest):
    """CHECK_PKG_007 — Manifest does not claim production readiness."""
    if manifest is None:
        return False, "CHECK_PKG_007 FAIL — Cannot check: manifest not loaded"
    violations = []
    for flag in PRODUCTION_READINESS_FLAGS:
        if manifest.get(flag) is True:
            violations.append(f"{flag}: true")
    if violations:
        lines = "\n".join(f"    {v}" for v in violations)
        return False, f"CHECK_PKG_007 FAIL — Production readiness claimed:\n{lines}"
    return True, "CHECK_PKG_007 PASS — No production readiness claimed"


def check_mode1_not_runnable(manifest):
    """CHECK_PKG_008 — Mode 1 not claimed as runnable."""
    if manifest is None:
        return False, "CHECK_PKG_008 FAIL — Cannot check: manifest not loaded"
    if manifest.get("mode1Runnable") is True:
        return False, (
            "CHECK_PKG_008 FAIL — package_manifest.json claims mode1Runnable: true. "
            "Mode 1 may only be runnable when the final runnable handoff explicitly "
            "authorizes it. This flag must remain false until that PR is merged."
        )
    return True, "CHECK_PKG_008 PASS — mode1Runnable is false (correct)"


def check_no_schema_output_claimed(manifest):
    """CHECK_PKG_009 — Manifest does not claim schema output was created."""
    if manifest is None:
        return False, "CHECK_PKG_009 FAIL — Cannot check: manifest not loaded"
    schema_flags = ["schemaOutputCreated", "jsonLdCreated", "productionSchemaBundleCreated",
                    "homepageJsonLdDraftCreated", "astroAttachmentCreated"]
    violations = []
    for flag in schema_flags:
        if manifest.get(flag) is True:
            violations.append(f"{flag}: true")
    if violations:
        lines = "\n".join(f"    {v}" for v in violations)
        return False, f"CHECK_PKG_009 FAIL — Schema output claimed in manifest:\n{lines}"
    return True, "CHECK_PKG_009 PASS — No schema output claimed in manifest"


def check_ledger_production_lock(ledger):
    """CHECK_PKG_010 — Ledger productionLockStatus is NO_PRODUCTION_LOCKS when empty."""
    if ledger is None:
        return False, "CHECK_PKG_010 FAIL — Cannot check: ledger not loaded"
    entries = ledger.get("entries", [])
    lock_status = ledger.get("productionLockStatus", "")
    if not entries and lock_status != "NO_PRODUCTION_LOCKS":
        return False, (
            f"CHECK_PKG_010 FAIL — Ledger has no entries but productionLockStatus "
            f"is '{lock_status}' (expected NO_PRODUCTION_LOCKS)"
        )
    if entries:
        # Warn if any entry claims PRODUCTION_LOCKED without humanApprovalRef
        bad = [
            e.get("runId", "(missing)")
            for e in entries
            if e.get("productionLockStatus") == "PRODUCTION_LOCKED"
            and not e.get("humanApprovalRef", "").strip()
        ]
        if bad:
            return False, (
                f"CHECK_PKG_010 FAIL — {len(bad)} ledger entry/entries claim "
                f"PRODUCTION_LOCKED without humanApprovalRef: {', '.join(bad)}"
            )
    return True, f"CHECK_PKG_010 PASS — Ledger production lock status is correct"


def check_no_fake_reports(root):
    """CHECK_PKG_011 — No fake passing report files present."""
    found = []
    for pattern in FAKE_REPORT_PATTERNS:
        found.extend(find_files_by_pattern(root, pattern))
    if found:
        lines = "\n".join(f"    BLOCKED: {p}" for p in found)
        return False, f"CHECK_PKG_011 FAIL — Fake report file(s) found:\n{lines}"
    return True, "CHECK_PKG_011 PASS — No fake report files present"


def check_truth_view_json(root):
    """CHECK_PKG_012 — Homepage scoped truth view parses as valid JSON."""
    path = os.path.join(root, TRUTH_PACK_JSON.replace("/", os.sep))
    if not os.path.isfile(path):
        return False, f"CHECK_PKG_012 FAIL — Truth view file not found: {TRUTH_PACK_JSON}"
    _, err = load_json(path)
    if err:
        return False, f"CHECK_PKG_012 FAIL — Truth view parse error: {err}"
    return True, "CHECK_PKG_012 PASS — Homepage scoped truth view parses as valid JSON"


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main():
    parser = argparse.ArgumentParser(
        description=(
            "Package-level validator for the Rise FC standalone schema operator package. "
            "Checks structural integrity, required files, JSON validity, and safety constraints. "
            "Does not generate schema. Does not create JSON-LD. Does not modify any files. "
            "A PASS result confirms structural integrity only — it does not authorize schema "
            "production, production deployment, or any implementation action."
        )
    )
    parser.add_argument(
        "package_dir",
        nargs="?",
        default=".",
        help="Root directory of the package (default: current directory).",
    )
    parser.add_argument(
        "--expected-files",
        default=None,
        help=(
            "Path to PACKAGE_EXPECTED_ACTIVE_FILES_V1_0.json. "
            "Defaults to 06_MACHINE_RULES/PACKAGE_EXPECTED_ACTIVE_FILES_V1_0.json "
            "relative to package_dir."
        ),
    )
    args = parser.parse_args()

    root = os.path.abspath(args.package_dir)
    if not os.path.isdir(root):
        print(f"ERROR: Package directory not found: {root}", file=sys.stderr)
        sys.exit(2)

    expected_files_path = args.expected_files or os.path.join(
        root,
        "06_MACHINE_RULES",
        "PACKAGE_EXPECTED_ACTIVE_FILES_V1_0.json"
    )
    if not os.path.isfile(expected_files_path):
        print(f"ERROR: Expected files contract not found: {expected_files_path}", file=sys.stderr)
        sys.exit(2)

    expected_files_data, err = load_json(expected_files_path)
    if err:
        print(f"ERROR: Expected files contract is not valid JSON: {err}", file=sys.stderr)
        sys.exit(2)

    print(f"\nRise FC Package Validator")
    print(f"Package dir   : {root}")
    print(f"Expected files: {expected_files_path}")
    print()

    # --- Run checks ---
    results = []

    passed, msg, manifest = check_manifest(root)
    results.append((passed, msg))

    passed, msg, ledger = check_ledger(root)
    results.append((passed, msg))

    results.append(check_required_files(root, expected_files_data))
    results.append(check_key_json_schemas(root))
    results.append(check_no_jsonld_files(root))
    results.append(check_no_sample_runs(root))
    results.append(check_no_production_readiness(manifest))
    results.append(check_mode1_not_runnable(manifest))
    results.append(check_no_schema_output_claimed(manifest))
    results.append(check_ledger_production_lock(ledger))
    results.append(check_no_fake_reports(root))
    results.append(check_truth_view_json(root))

    # --- Print results ---
    section("Check results")
    for passed, msg in results:
        tag = "PASS" if passed else "FAIL"
        print(f"  [{tag}] {msg}")

    # --- Summary ---
    total = len(results)
    passed_count = sum(1 for p, _ in results if p)
    failed_count = total - passed_count

    section("Summary")
    print(f"  Checks run    : {total}")
    print(f"  Passed        : {passed_count}")
    print(f"  Failed        : {failed_count}")
    print()

    if failed_count == 0:
        print(f"RESULT: PASS — All {total} checks passed.")
        print()
        print("Non-authorization notice:")
        print("  PASS confirms structural integrity only.")
        print("  This result does not authorize schema production or production deployment.")
        sys.exit(0)
    else:
        print(f"RESULT: FAIL — {failed_count} check(s) failed. Review issues above.")
        sys.exit(1)


if __name__ == "__main__":
    main()
