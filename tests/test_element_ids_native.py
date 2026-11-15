"""Native Gradio duplicate-tool-instance ID test using only a maintained fixture."""

import hashlib
import json

import pytest
import schema3_package

pytestmark = pytest.mark.windows_isolation

DUPLICATE_CONNECTION = '''"""Call one approved tool twice under distinct widget identities."""


def run(payload: dict, call) -> None:
    """Invoke the duplicated widget and the remaining approved tool once each."""
    call("count_words_in_text", text=payload["text"])
    call("count_words_in_text_2", text=payload["text"])
    call("count_vowels_in_text", text=payload["text"])
'''


def test_repeated_widgets_have_distinct_native_controls_and_callbacks(tmp_path):
    """Two copies share an allocator, not control IDs or callback namespaces."""
    from agentix.lab.application_artifacts import application_digest, approve_application
    from agentix.lab.application_session import ApplicationSession

    package = schema3_package.package(tmp_path)
    manifest_path = package / "application.json"
    manifest = json.loads(manifest_path.read_bytes())
    manifest["widgets"] = [
        {"id": "count_words_in_text", "tool": "count_words_in_text"},
        {"id": "count_words_in_text_2", "tool": "count_words_in_text"},
        {"id": "count_vowels_in_text", "tool": "count_vowels_in_text"},
    ]
    logic = package / "application_logic.py"
    logic.write_text(DUPLICATE_CONNECTION, encoding="utf-8")
    manifest["files"]["application_logic.py"] = hashlib.sha256(logic.read_bytes()).hexdigest()
    manifest_path.write_text(json.dumps(manifest), encoding="utf-8")
    approved = approve_application(package, application_digest(package))
    with ApplicationSession(approved) as session:
        config = json.loads(session.request("GET", "/config").body)
        ids = [c["props"]["elem_id"] for c in config["components"] if c["props"].get("elem_id")]
        assert len(ids) == len(set(ids))
        assert "application_count_words_in_text_input" in ids
        assert "application_count_words_in_text_2_input" in ids
        for endpoint, text, count in [
            ("count_count_words_in_text", "Hello World!", 2),
            ("count_count_words_in_text_2", "one two three", 3),
        ]:
            response = session.request(
                "POST", "/gradio_api/run/" + endpoint, json.dumps({"data": [text]}).encode()
            )
            assert response.status == 200
            assert json.loads(response.body)["data"] == [count]
    assert not session.native_thread.is_alive()
