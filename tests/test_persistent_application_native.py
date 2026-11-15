"""Opt-in native lifetime proof; this deliberately lasts longer than five minutes."""

import json
import time

import pytest

from agentix.lab.application_artifacts import application_digest, approve_application
from agentix.lab.application_session import ApplicationSession

pytestmark = pytest.mark.windows_isolation


def test_native_persistent_survives_five_minutes_and_closes(tmp_path):
    """Catch an inherited fixed TTL and verify owned process/temp cleanup after close."""
    from schema3_package import package

    folder = package(tmp_path)
    capability = approve_application(folder, application_digest(folder))
    with ApplicationSession(capability, lifetime=None) as session:
        root = session.root
        started = time.monotonic()
        while time.monotonic() - started < 305:
            assert session.native_thread.is_alive()
            assert not session.cancel.is_set()
            time.sleep(1)
        response = session.request(
            "POST", "/gradio_api/run/count_vowels", json.dumps({"data": ["Hello World!"]}).encode()
        )
        assert json.loads(response.body)["data"] == [3]
    assert not session.native_thread.is_alive()
    assert not session.reader_thread.is_alive()
    assert not root.exists()
