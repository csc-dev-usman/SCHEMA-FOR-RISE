"""
Rise FC Standalone Schema Operator Package
Output Bundle Validator — V1.0

Usage:
    python tools/validate_output_bundle.py <bundle_dir>
    python tools/validate_output_bundle.py --help

Exit codes:
    0  PASS  — all checks passed
    1  FAIL  — one or more checks failed (bundle must not be used)
    2  WARN  — checks passed but warnings were raised (review before use)

This validator uses Python standard library only.
It does NOT create or modify output bundles.
It does NOT generate schema.
It does NOT create JSON-LD.
"""

import argparse
import json
import os
import sys

# ---------------------------------------------------------------------------
# CONSTANTS — governed by Rise schema operator package doctrine
# ---------------------------------------------------------------------------

HOMEPAGE_TRUTH_FINGERPRINT = (
    "80edd829806cae271242c6a8e853edabdb8b2f16ca5a8fa1a3fc69ff5b78d53d"
)

HOMEPAGE_PROFILE = "HOMEPAGE_SCHEMA_PROFILE"
HOMEPAGE_ROUTE = "/"

BLOCKED_MODULES = {
    "FAQPage",
    "Question",
    "Answer",
    "Offer",
    "AggregateOffer",
    "Event",
    "SportsEvent",
    "Review",
    "AggregateRating",
    "Place",
    "LocalBusiness",
    "GeoCoordinates",
    "PostalAddress",
}

HELD_PROPERTIES = {
    "telephone",
    "email",
    "sameAs",
    "logo",
    "image",
    "description",
    "geo",
    "latitude",
    "longitude",
    "address",
    "streetAddress",
    "addressLocality",
    "addressRegion",
    "postalCode",
    "review",
    "aggregateRating",
    "ratingValue",
    "ratingCount",
    "price",
    "priceCurrency",
    "priceRange",
    "startDate",
    "endDate",
    "eventSchedule",
    "offers",
    "availability",
}

REQUIRED_JSON_FILES = [
    "output_bundle_manifest.json",
    "run_metadata.json",
    "evidence_map.json",
    "controller_decision.json",
    "validator_results.json",
]

REQUIRED_DOC_FILES = [
    "withheld_schema_report.md",
    "deferred_truth_report.md",
]

CONDITIONAL_FILES = [
    "emitted_schema.jsonld",
    "implementation_handoff.md",
]


# ---------------------------------------------------------------------------
# RESULT TRACKING
# ---------------------------------------------------------------------------

class Results:
    def __init__(self):
        self.failures = []
        self.warnings = []
        self.passes = []

    def fail(self, check, reason):
        self.failures.append((check, reason))

    def warn(self, check, reason):
        self.warnings.append((check, reason))

    def ok(self, check, detail=""):
        self.passes.append((check, detail))

    def exit_code(self):
        if self.failures:
            return 1
        if self.warnings:
            return 2
        return 0

    def print_summary(self):
        for check, detail in self.passes:
            tag = f"  [{detail}]" if detail else ""
            print(f"  PASS  {check}{tag}")
        for check, reason in self.warnings:
            print(f"  WARN  {check} — {reason}")
        for check, reason in self.failures:
            print(f"  FAIL  {check} — {reason}")

        total = len(self.passes) + len(self.warnings) + len(self.failures)
        print()
        print(f"  Checks run : {total}")
        print(f"  Passed     : {len(self.passes)}")
        print(f"  Warnings   : {len(self.warnings)}")
        print(f"  Failures   : {len(self.failures)}")
        print()

        if self.failures:
            print("  RESULT: FAIL — bundle must not be used. See FAIL lines above.")
        elif self.warnings:
            print("  RESULT: WARN — review warnings before proceeding.")
        else:
            print("  RESULT: PASS — all checks passed.")


# ---------------------------------------------------------------------------
# CHECK FUNCTIONS
# ---------------------------------------------------------------------------

def check_required_files(bundle_dir, results):
    """Verify all required files exist in the bundle directory."""
    for fname in REQUIRED_JSON_FILES:
        path = os.path.join(bundle_dir, fname)
        if os.path.isfile(path):
            results.ok("required_file_present", fname)
        else:
            results.fail(
                "required_file_present",
                f"Missing required JSON file: {fname}",
            )
    for fname in REQUIRED_DOC_FILES:
        path = os.path.join(bundle_dir, fname)
        if os.path.isfile(path):
            results.ok("required_doc_present", fname)
        else:
            results.fail(
                "required_doc_present",
                f"Missing required doc file: {fname}",
            )


def check_json_parses(bundle_dir, results):
    """Verify all JSON files in the bundle parse as valid JSON."""
    all_files = os.listdir(bundle_dir)
    json_files = [f for f in all_files if f.endswith(".json") or f.endswith(".jsonld")]
    for fname in json_files:
        path = os.path.join(bundle_dir, fname)
        try:
            with open(path, "r", encoding="utf-8") as fh:
                json.load(fh)
            results.ok("json_valid", fname)
        except json.JSONDecodeError as exc:
            results.fail(
                "json_valid",
                f"{fname} is not valid JSON: {exc}",
            )
        except OSError as exc:
            results.fail(
                "json_valid",
                f"{fname} could not be read: {exc}",
            )


def check_truth_fingerprint(bundle_dir, results):
    """
    If run_metadata.json declares schemaProfile=HOMEPAGE_SCHEMA_PROFILE or
    pageRoute='/', verify that truthFingerprint matches the expected value.
    """
    path = os.path.join(bundle_dir, "run_metadata.json")
    if not os.path.isfile(path):
        # already caught by required files check
        return
    try:
        with open(path, "r", encoding="utf-8") as fh:
            data = json.load(fh)
    except (json.JSONDecodeError, OSError):
        # parse failures already caught by check_json_parses
        return

    profile = data.get("schemaProfile", "")
    route = data.get("pageRoute", "")
    fingerprint = data.get("truthFingerprint", "")

    is_homepage = profile == HOMEPAGE_PROFILE or route == HOMEPAGE_ROUTE

    if is_homepage:
        if not fingerprint:
            results.fail(
                "truth_fingerprint",
                "run_metadata.json declares homepage profile/route but "
                "truthFingerprint is missing.",
            )
        elif fingerprint != HOMEPAGE_TRUTH_FINGERPRINT:
            results.fail(
                "truth_fingerprint",
                f"truthFingerprint mismatch. "
                f"Expected: {HOMEPAGE_TRUTH_FINGERPRINT} "
                f"Got: {fingerprint}",
            )
        else:
            results.ok("truth_fingerprint", "homepage fingerprint matches")
    elif fingerprint:
        results.warn(
            "truth_fingerprint",
            "truthFingerprint present but page/profile is not homepage — "
            "no automated check applied. Operator must verify manually.",
        )
    else:
        results.ok("truth_fingerprint", "non-homepage run — fingerprint check skipped")


def _collect_types(obj, found=None):
    """Recursively collect all @type values from a JSON-LD graph."""
    if found is None:
        found = set()
    if isinstance(obj, dict):
        t = obj.get("@type")
        if isinstance(t, str):
            found.add(t)
        elif isinstance(t, list):
            for item in t:
                if isinstance(item, str):
                    found.add(item)
        for val in obj.values():
            _collect_types(val, found)
    elif isinstance(obj, list):
        for item in obj:
            _collect_types(item, found)
    return found


def _collect_properties(obj, found=None):
    """Recursively collect all property keys from a JSON-LD graph (non-@ keys)."""
    if found is None:
        found = set()
    if isinstance(obj, dict):
        for key, val in obj.items():
            if not key.startswith("@") and not key.startswith("_"):
                found.add(key)
            _collect_properties(val, found)
    elif isinstance(obj, list):
        for item in obj:
            _collect_properties(item, found)
    return found


def check_blocked_modules(bundle_dir, results):
    """
    If emitted_schema.jsonld exists, verify it contains no blocked @type values.
    """
    path = os.path.join(bundle_dir, "emitted_schema.jsonld")
    if not os.path.isfile(path):
        results.ok(
            "blocked_modules",
            "emitted_schema.jsonld not present — check skipped",
        )
        return
    try:
        with open(path, "r", encoding="utf-8") as fh:
            data = json.load(fh)
    except (json.JSONDecodeError, OSError):
        # parse failures already caught by check_json_parses
        return

    found_types = _collect_types(data)
    violations = found_types & BLOCKED_MODULES
    if violations:
        results.fail(
            "blocked_modules",
            f"Blocked @type values found in emitted_schema.jsonld: "
            f"{sorted(violations)}. "
            f"These modules are not authorized for the first-page lane.",
        )
    else:
        results.ok("blocked_modules", "no blocked @type values found")


def check_held_fields(bundle_dir, results):
    """
    If emitted_schema.jsonld exists, warn if it contains held properties
    that lack explicit approval metadata in controller_decision.json.
    """
    schema_path = os.path.join(bundle_dir, "emitted_schema.jsonld")
    if not os.path.isfile(schema_path):
        results.ok(
            "held_fields",
            "emitted_schema.jsonld not present — check skipped",
        )
        return

    try:
        with open(schema_path, "r", encoding="utf-8") as fh:
            schema_data = json.load(fh)
    except (json.JSONDecodeError, OSError):
        return

    found_props = _collect_properties(schema_data)
    held_violations = found_props & HELD_PROPERTIES

    if not held_violations:
        results.ok("held_fields", "no held properties found in emitted schema")
        return

    # Check controller_decision.json for approval metadata
    ctrl_path = os.path.join(bundle_dir, "controller_decision.json")
    approved_held = set()
    if os.path.isfile(ctrl_path):
        try:
            with open(ctrl_path, "r", encoding="utf-8") as fh:
                ctrl_data = json.load(fh)
            # Look for heldFieldApprovals or releasedHeldFields section
            approvals = ctrl_data.get("heldFieldApprovals", {})
            if isinstance(approvals, dict):
                for prop, approval in approvals.items():
                    if isinstance(approval, dict):
                        status = approval.get("status", "")
                        if status in ("APPROVED", "OWNER_APPROVED"):
                            approved_held.add(prop)
            released = ctrl_data.get("releasedHeldFields", [])
            if isinstance(released, list):
                approved_held.update(released)
        except (json.JSONDecodeError, OSError):
            pass

    unapproved = held_violations - approved_held
    if unapproved:
        results.fail(
            "held_fields",
            f"Held properties present in emitted_schema.jsonld without "
            f"approval metadata in controller_decision.json: {sorted(unapproved)}. "
            f"Held fields may not be emitted without owner approval and "
            f"supporting Phase 0 / page evidence.",
        )
    else:
        results.warn(
            "held_fields",
            f"Held properties found but appear approved: {sorted(held_violations)}. "
            f"Operator must verify owner approval chain independently.",
        )


def check_production_lock(bundle_dir, results):
    """
    Reject PRODUCTION_LOCKED status unless humanApprovalStatus is GRANTED.
    """
    path = os.path.join(bundle_dir, "output_bundle_manifest.json")
    if not os.path.isfile(path):
        return
    try:
        with open(path, "r", encoding="utf-8") as fh:
            data = json.load(fh)
    except (json.JSONDecodeError, OSError):
        return

    status = data.get("status", "")
    approval = data.get("humanApprovalStatus", "")

    if status == "PRODUCTION_LOCKED":
        if approval == "GRANTED":
            results.warn(
                "production_lock",
                "Bundle is PRODUCTION_LOCKED with humanApprovalStatus=GRANTED. "
                "Operator must independently verify the approval was legitimate "
                "before implementation.",
            )
        else:
            results.fail(
                "production_lock",
                f"Bundle status is PRODUCTION_LOCKED but humanApprovalStatus "
                f"is '{approval}' (must be 'GRANTED'). "
                f"PRODUCTION_LOCKED requires explicit human approval.",
            )
    else:
        results.ok("production_lock", f"status={status or '(not set)'}")


def check_safety_booleans(bundle_dir, results):
    """
    Check that output_bundle_manifest.json safety booleans are consistent.
    Warn if schemaOutputCreated=true but no emitted_schema.jsonld exists.
    Warn if jsonLdCreated=true but no emitted_schema.jsonld exists.
    Fail if phase0MutationAllowed=true.
    Fail if sourceTruthMutationAllowed=true.
    """
    path = os.path.join(bundle_dir, "output_bundle_manifest.json")
    if not os.path.isfile(path):
        return
    try:
        with open(path, "r", encoding="utf-8") as fh:
            data = json.load(fh)
    except (json.JSONDecodeError, OSError):
        return

    schema_path = os.path.join(bundle_dir, "emitted_schema.jsonld")
    has_schema = os.path.isfile(schema_path)

    if data.get("phase0MutationAllowed") is True:
        results.fail(
            "safety_booleans",
            "phase0MutationAllowed is true. Phase 0 mutation is never allowed.",
        )
    else:
        results.ok("safety_booleans", "phase0MutationAllowed is not true")

    if data.get("sourceTruthMutationAllowed") is True:
        results.fail(
            "safety_booleans",
            "sourceTruthMutationAllowed is true. Source truth mutation is never allowed.",
        )
    else:
        results.ok("safety_booleans", "sourceTruthMutationAllowed is not true")

    if data.get("schemaOutputCreated") is True and not has_schema:
        results.warn(
            "safety_booleans",
            "schemaOutputCreated=true but emitted_schema.jsonld not found in bundle.",
        )
    if data.get("jsonLdCreated") is True and not has_schema:
        results.warn(
            "safety_booleans",
            "jsonLdCreated=true but emitted_schema.jsonld not found in bundle.",
        )


# ---------------------------------------------------------------------------
# MAIN
# ---------------------------------------------------------------------------

def build_parser():
    parser = argparse.ArgumentParser(
        prog="validate_output_bundle",
        description=(
            "Rise FC standalone schema operator — output bundle validator.\n\n"
            "Validates a future output bundle directory against the governed\n"
            "Rise schema operator rules. Uses Python standard library only.\n\n"
            "This tool does NOT create or modify output bundles.\n"
            "This tool does NOT generate schema.\n"
            "This tool does NOT create JSON-LD."
        ),
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=(
            "Exit codes:\n"
            "  0  PASS — all checks passed\n"
            "  1  FAIL — one or more checks failed (bundle must not be used)\n"
            "  2  WARN — checks passed but warnings were raised\n\n"
            "Example:\n"
            "  python tools/validate_output_bundle.py sample_runs/RUN_001_HOMEPAGE_MODE1"
        ),
    )
    parser.add_argument(
        "bundle_dir",
        nargs="?",
        metavar="BUNDLE_DIR",
        help="Path to the output bundle directory to validate.",
    )
    return parser


def main():
    parser = build_parser()
    args = parser.parse_args()

    if args.bundle_dir is None:
        parser.print_help()
        sys.exit(0)

    bundle_dir = args.bundle_dir

    if not os.path.isdir(bundle_dir):
        print(f"\n  ERROR: '{bundle_dir}' is not a directory or does not exist.\n")
        sys.exit(1)

    print()
    print("  Rise FC — Output Bundle Validator V1.0")
    print(f"  Bundle dir : {bundle_dir}")
    print()

    results = Results()

    check_required_files(bundle_dir, results)
    check_json_parses(bundle_dir, results)
    check_truth_fingerprint(bundle_dir, results)
    check_blocked_modules(bundle_dir, results)
    check_held_fields(bundle_dir, results)
    check_production_lock(bundle_dir, results)
    check_safety_booleans(bundle_dir, results)

    results.print_summary()

    sys.exit(results.exit_code())


if __name__ == "__main__":
    main()
