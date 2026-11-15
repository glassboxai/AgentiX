"""Plan or apply explicitly reviewed catalog relocation, without model inference.

The review digest authorizes only the exact plan. Applications reuse protected
human-reviewed cases and require fresh native/browser gates; no auto-approval
switch, changed-policy tool grant transfer or host-execution fallback exists.
"""

import argparse
import json
import os
import sys
from collections.abc import Callable
from pathlib import Path
from types import SimpleNamespace

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))


from agentix.application.app_workflow import (  # noqa: E402
    ApplicationPipeline,
    ApplicationSupervisor,
    Candidate,
)
from agentix.lab.application_artifacts import application_digest  # noqa: E402
from agentix.sandbox import WindowsSandbox  # noqa: E402
from agentix.security.acceptance import matches_expectation  # noqa: E402
from agentix.security.data_protection import WindowsDataProtection  # noqa: E402
from agentix.storage.application_catalog import ApprovedTool  # noqa: E402
from agentix.storage.catalog_migration import CatalogMigration, fingerprint  # noqa: E402


def verify_application(package: Path, review: dict, evidence: Path) -> bool:
    """Run protected reviewed cases through native and browser production gates.

    No expected value is inferred, altered or sent to a model. The child receives
    inputs only. Always close the verifier's own preview; leave live apps alone.
    """
    candidate = Candidate(
        evidence.name, evidence, package, application_digest(package), json.dumps(review)
    )
    supervisor = ApplicationSupervisor()
    try:
        supervisor.approve(candidate, candidate.identity, True)
        supervisor.verify(candidate, "http://127.0.0.1:7884")
        return candidate.verified
    finally:
        candidate.close()


def verify_exception_cases(
    tool: ApprovedTool, evidence: Path, *, evaluate: Callable | None = None
) -> None:
    """Compare all reviewed exception types on the host, sending child inputs only.

    The injected evaluator is a test seam. Production always uses WindowsSandbox
    without fallback. Retain bounded case IDs and verdicts, not code or arguments.
    Raise ValueError on any child/process mismatch and never silently drop a case.
    """
    observe = evaluate if evaluate is not None else WindowsSandbox().evaluate
    verdicts = []
    for case in tool.reviewed_contract["cases"]:
        if case["expect"]["kind"] == "value":
            continue
        observed = observe(tool.code, tool.tool_name, case["function"], case["kwargs"])
        passed = (
            observed.isolated is True
            and observed.exit_code == 0
            and not observed.failure
            and matches_expectation(observed.report, case["expect"])
        )
        verdicts.append(
            {
                "case_id": case["id"],
                "passed": passed,
                "expected_exception_type": case["expect"].get("type"),
                "observed_exception_type": observed.report.get("exception_type")
                if isinstance(observed.report, dict)
                else None,
            }
        )
        (evidence / "exception-cases.json").write_text(
            json.dumps(verdicts, indent=2), encoding="utf-8"
        )
        if not passed:
            raise ValueError("Independent reviewed exception case failed")


def verify_widget(tool: ApprovedTool, proposal: dict, css: str, evidence: Path) -> bool:
    """Check unchanged widget bytes against every current approved value case.

    Trusted connection code forwards literal reviewed arguments; expected results
    stay in the host review. No model is constructed, no installed code is changed
    and generated child tests are provisional. Exact exception types are checked
    separately through native observations; browser checks use typed value cases.
    """
    reviewed = tool.reviewed_contract["cases"]
    if any(case["function"] != tool.function for case in reviewed):
        raise ValueError("Widget cases must cover the canonical approved function")
    verify_exception_cases(tool, evidence)
    cases = [case for case in reviewed if case["expect"]["kind"] == "value"]
    if not cases:
        raise ValueError("Widget review requires at least one representable value case")
    widgets = [{"id": "case_" + str(i), "tool": tool.tool_name} for i in range(len(cases))]
    lines = [
        '"""Forward independently reviewed migration cases."""',
        "def run(payload: dict, call) -> None:",
        '    """Invoke each reviewed case without calculating expected results."""',
    ]
    for widget, case in zip(widgets, cases, strict=True):
        arguments = ", ".join(name + "=" + repr(value) for name, value in case["kwargs"].items())
        lines.append(
            "    call(" + repr(widget["id"]) + (", " if arguments else "") + arguments + ")"
        )
    plan = {
        "inputs": {"migration_review": {"type": "string"}},
        "widgets": widgets,
        "connection_code": "\n".join(lines) + "\n",
        "notes": "Reviewed migration cases",
    }
    coordinator = SimpleNamespace(
        plan=lambda *args: plan, widgets=lambda *args: {tool.tool_name: proposal}
    )
    candidate = ApplicationPipeline(evidence, coordinator_factory=lambda _: coordinator).generate(
        "Validate the existing widget against current independently reviewed cases",
        tools={tool.tool_name: tool},
    )
    css_path = candidate.package / (tool.tool_name + "_widget.css")
    css_path.write_text(css, encoding="utf-8")
    manifest_path = candidate.package / "application.json"
    manifest = json.loads(manifest_path.read_bytes())
    manifest["files"][css_path.name] = fingerprint(css_path.read_bytes())
    manifest_path.write_text(json.dumps(manifest, indent=2), encoding="utf-8")
    review = json.loads(candidate.review_text)
    review["manifest"] = manifest
    review["source_files"][css_path.name] = css
    review["independent_acceptance"] = {
        "payload": {"migration_review": "reviewed"},
        "expected": {
            widget["id"]: case["expect"]["value"]
            for widget, case in zip(widgets, cases, strict=True)
        },
        "widgets": {widget["id"]: [case] for widget, case in zip(widgets, cases, strict=True)},
    }
    candidate.digest = application_digest(candidate.package)
    candidate.review_text = json.dumps(review)
    (candidate.folder / "review.json").write_text(candidate.review_text, encoding="utf-8")
    supervisor = ApplicationSupervisor()
    try:
        supervisor.approve(candidate, candidate.identity, True)
        supervisor.verify(candidate, "http://127.0.0.1:7884")
        return candidate.verified
    finally:
        candidate.close()


def main() -> int:
    """Print a safe plan or apply its reviewed digest; return 2 for blocked entries."""
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--source-home", type=Path, required=True)
    parser.add_argument("--source-tools", type=Path, required=True)
    parser.add_argument("--target-home", type=Path, required=True)
    parser.add_argument("--review-digest", help="Exact SHA-256 from the reviewed read-only plan")
    args = parser.parse_args()
    # Only this command's services use the destination; existing processes retain their settings.
    os.environ["AGENTIX_HOME"] = str(args.target_home)
    os.environ["AGENTIX_TOOLS_ROOT"] = str(args.target_home / "data/tools")
    migration = CatalogMigration(
        args.source_home,
        args.source_tools,
        args.target_home,
        protector=WindowsDataProtection(),
        application_verifier=verify_application,
        widget_verifier=verify_widget,
    )
    result = migration.apply(args.review_digest) if args.review_digest else migration.plan()
    print(json.dumps(result, indent=2))
    return 2 if any(item["status"] == "blocked" for item in result["items"]) else 0


if __name__ == "__main__":
    raise SystemExit(main())
