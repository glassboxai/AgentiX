"""LAB-003 actual Gradio ASGI transported through an isolated native process."""

import pytest


@pytest.mark.windows_isolation
def test_native_gradio_asgi_root_and_event():
    """Require real pinned Gradio in AppContainer, not a host-rendered substitute."""
    from agentix.lab.widget_session import WidgetSession

    with WidgetSession() as session:
        root = session.request("GET", "/")
        assert root.status == 200
        assert b"gradio" in root.body.lower()
        result = session.request(
            "POST", "/gradio_api/run/vowels_first", b'{"data":["Hello World!"]}'
        )
        assert result.status == 200
        import json

        assert json.loads(result.body)["data"] == [3]


@pytest.mark.windows_isolation
def test_provisional_tests_cannot_modify_serving_process(tmp_path):
    """Generated tests must run in a different native worker from the served widget."""
    from pathlib import Path

    from agentix.lab.widget_artifacts import approve_package, package_digest
    from agentix.lab.widget_session import WidgetSession, run_provisional_tests

    (tmp_path / "count_vowels_in_text_widget.py").write_bytes(
        Path("src/agentix/lab/reference_widget.py").read_bytes()
    )
    (tmp_path / "count_vowels_in_text_code.py").write_bytes(
        Path("src/agentix/lab/fixture_tools.py").read_bytes()
    )
    (tmp_path / "count_vowels_in_text_widget_tests.py").write_text("""import unittest,gradio as gr
class MutatingTest(unittest.TestCase):
    def test_process_local_mutation(self):
        def broken(*args, **kwargs):
            raise RuntimeError("provisional test altered Gradio")
        gr.Textbox.__init__ = broken
        self.assertTrue(True)
""")
    approved = approve_package(tmp_path, package_digest(tmp_path))
    assert run_provisional_tests(approved)["successful"]
    with WidgetSession(approved) as session:
        assert session.request("GET", "/").status == 200
