"""Native-only probes of an explicitly reviewed external model candidate."""

import json
import os
from pathlib import Path

import pytest

pytestmark = pytest.mark.windows_isolation


def reviewed():
    """Require independent operator review; never infer approval from child tests."""
    from agentix.lab.application_artifacts import approve_application

    folder = os.environ.get("AGENTIX_DESIGNER_REVIEWED_PACKAGE")
    digest = os.environ.get("AGENTIX_DESIGNER_REVIEWED_DIGEST")
    if not folder or not digest:
        pytest.skip("Explicit model candidate review required")
    return approve_application(Path(folder), digest)


def probe(capability, replacements):
    """Review a maintained probe shell while preserving exact model widget bytes."""
    from agentix.lab.application_artifacts import ApprovedApplication

    return ApprovedApplication(
        tuple((name, replacements.get(name, body)) for name, body in capability.files),
        "explicit-native-probe",
    )


def test_generated_widget_two_instances_native():
    """Catch shared IDs, shared callbacks and invalid stale results in actual Gradio."""
    from agentix.lab.application_session import ApplicationSession

    capability = reviewed()
    shell = (
        dict(capability.files)["app.py"]
        .replace(b'create_words(Context("words"))', b'create_vowels(Context("words"))')
        .replace(b'create_words(Context("words", ids))', b'create_vowels(Context("words", ids))')
    )
    with ApplicationSession(probe(capability, {"app.py": shell})) as session:
        config = json.loads(session.request("GET", "/config").body)
        ids = [
            component["props"]["elem_id"]
            for component in config["components"]
            if component["props"].get("elem_id")
        ]
        assert len(ids) == len(set(ids))
        for endpoint, text, expected in [
            ("count_words", "Hello World!", 3),
            ("count_vowels", "AEIOUaeiou", 10),
            ("count_words", "rhythms", 0),
            ("count_vowels", "x" * 16001, None),
        ]:
            response = session.request(
                "POST", "/gradio_api/run/" + endpoint, json.dumps({"data": [text]}).encode()
            )
            assert response.status == 200
            assert json.loads(response.body)["data"] == [expected]
        assert session.tool_calls == 0


def test_proposed_model_tests_really_fail_in_separate_sandbox():
    """Record the model tests' actual failure; never execute them on the host."""
    from agentix.lab.application_session import ApplicationSession

    capability = reviewed()
    folder = Path(os.environ["AGENTIX_DESIGNER_REVIEWED_PACKAGE"]).parent
    shell = b'''"""Maintained native-only provisional-test observation shell."""
import io
import json
import unittest
import gradio as gr
import package_tests

def create_application():
    """Run proposed tests, exposing only bounded child-reported counts."""
    result = unittest.TextTestRunner(stream=io.StringIO()).run(unittest.defaultTestLoader.loadTestsFromModule(package_tests))
    with gr.Blocks() as demo:
        gr.Textbox(value=json.dumps({"run": result.testsRun, "errors": len(result.errors), "failures": len(result.failures)}), elem_id="proposed_report")
    return demo
'''
    with ApplicationSession(
        probe(
            capability,
            {"app.py": shell, "package_tests.py": (folder / "proposed_tests.py").read_bytes()},
        )
    ) as session:
        config = json.loads(session.request("GET", "/config").body)
        report = next(
            json.loads(c["props"]["value"])
            for c in config["components"]
            if c["props"].get("elem_id") == "proposed_report"
        )
        assert report["run"] == 5
        assert report["errors"] > 0
        Path("docs/reports/lab-006-proposed-tests.json").write_text(
            json.dumps(report), encoding="utf-8"
        )
