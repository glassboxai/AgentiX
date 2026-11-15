"""Regress metadata inspection and constrain reporting to local transport."""

import importlib.metadata
import importlib.util
from pathlib import Path
from unittest.mock import Mock

import pytest


def load_helper(name):
    """Load a standalone maintenance helper without application imports."""
    path = Path(__file__).resolve().parents[2] / "tools" / f"{name}.py"
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def test_missing_distribution_does_not_abort_other_versions(monkeypatch):
    """Verify missing distribution does not abort other versions."""
    helper = load_helper("collect_evidence")
    monkeypatch.setattr(
        importlib.metadata,
        "version",
        Mock(side_effect=["1.2", importlib.metadata.PackageNotFoundError("absent"), "3.4"]),
    )
    assert helper.distribution_versions(["present", "absent", "last"]) == {
        "present": "1.2",
        "absent": "distribution metadata unavailable",
        "last": "3.4",
    }


@pytest.mark.parametrize(
    "endpoint",
    [
        "https://example.com",
        "http://192.168.1.2:11434",
        "http://localhost:11434",
        "http://user:password@127.0.0.1",
        "http://127.0.0.1/path",
        "http://127.0.0.1?token=secret",
        "http://127.0.0.1#fragment",
    ],
)
def test_remote_or_ambiguous_report_endpoint_is_rejected(endpoint):
    """Verify remote or ambiguous report endpoint is rejected."""
    with pytest.raises(ValueError):
        load_helper("draft_report").validate_endpoint(endpoint)


@pytest.mark.parametrize("endpoint", ["http://127.0.0.1:11434", "http://[::1]:11434/"])
def test_loopback_report_endpoint_is_allowed(endpoint):
    """Verify loopback report endpoint is allowed."""
    assert load_helper("draft_report").validate_endpoint(endpoint) == endpoint.rstrip("/")


def test_report_redirects_are_refused():
    """Verify report redirects are refused."""
    assert (
        load_helper("draft_report")
        .NoRedirects()
        .redirect_request(None, None, 302, "", {}, "https://remote.invalid")
        is None
    )


def test_report_draft_is_prose_only_and_retains_provenance(monkeypatch):
    """Verify report draft is prose only and retains provenance."""
    helper = load_helper("draft_report")
    response = Mock()
    response.__enter__ = Mock(return_value=response)
    response.__exit__ = Mock(return_value=False)
    response.read.return_value = b'{"response":"Observed test results.","done":true}'
    opener = Mock()
    opener.open.return_value = response
    monkeypatch.setattr(helper, "build_opener", Mock(return_value=opener))
    text, provenance = helper.draft({"passed": 2}, "qwen3:14b", "http://127.0.0.1:11434")
    request = opener.open.call_args.args[0]
    assert "no code or tests" in request.data.decode()
    assert text == "Observed test results."
    assert provenance["review_status"] == "unverified draft"


def test_incomplete_model_output_is_not_reported_as_success(monkeypatch):
    """Verify incomplete model output is not reported as success."""
    helper = load_helper("draft_report")
    response = Mock()
    response.__enter__ = Mock(return_value=response)
    response.__exit__ = Mock(return_value=False)
    response.read.return_value = b'{"response":"partial","done":false}'
    opener = Mock()
    opener.open.return_value = response
    monkeypatch.setattr(helper, "build_opener", Mock(return_value=opener))
    with pytest.raises(RuntimeError, match="completed"):
        helper.draft({}, "model", "http://127.0.0.1:11434")
