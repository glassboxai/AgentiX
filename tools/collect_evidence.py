"""Inspect historical baseline XML and compare current entrypoint hashes.

This helper is retained for the original baseline workflow. Current refactoring
evidence is recorded separately and includes package files, not just entrypoints.
"""

import hashlib
import importlib.metadata
import json
import platform
import xml.etree.ElementTree as ET
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PRODUCTION = ("app.py", "security_manager.py", "custom_tools.py", "main.py", "config.py")


def distribution_versions(names):
    """Return available versions and explicit missing metadata without aborting."""
    result = {}
    for name in names:
        try:
            result[name] = importlib.metadata.version(name)
        except importlib.metadata.PackageNotFoundError:
            result[name] = "distribution metadata unavailable"
    return result


def collect():
    """Read test XML and compare production hashes with the pre-test baseline."""
    baseline = json.loads(
        (ROOT / "docs/reports/production-baseline.json").read_text(encoding="utf-8-sig")
    )
    current = {
        name: hashlib.sha256((ROOT / name).read_bytes()).hexdigest().upper() for name in PRODUCTION
    }
    suites = ET.parse(ROOT / "docs/reports/baseline-tests.xml").getroot()
    cases = list(suites.iter("testcase"))
    expected = [case.attrib["name"] for case in cases if case.find("skipped") is not None]
    return {
        "python": platform.python_version(),
        "platform": platform.platform(),
        "dependencies": distribution_versions(["pytest", "gradio", "crewai", "litellm"]),
        "tests": {
            "collected": len(cases),
            "passed": sum(
                all(case.find(tag) is None for tag in ("failure", "error", "skipped"))
                for case in cases
            ),
            "failures": sum(case.find("failure") is not None for case in cases),
            "errors": sum(case.find("error") is not None for case in cases),
            "expected_failures": expected,
        },
        "production_unchanged": current == baseline,
        "production_sha256": current,
        "limitations": [
            "Framework and LLM boundaries are doubled in unit tests.",
            "Component tests execute trusted temporary Python only.",
            "No coverage percentage, live browser, live agent, installer or OS isolation validation.",
            "Historical baseline XML is not the current suite; consult REFACTOR.md and refactor-tests.xml.",
        ],
    }


if __name__ == "__main__":
    print(json.dumps(collect(), indent=2))
