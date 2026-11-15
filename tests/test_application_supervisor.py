"""Fail-closed supervisor regressions using explicit native/browser doubles."""

import json

import pytest

from agentix.application.app_workflow import ApplicationSupervisor


def candidate(tmp_path):
    """Build a reviewed schema-3 fixture in independently owned storage."""
    from schema3_package import build

    return build(tmp_path)


def test_approval_binds_displayed_identity_and_bytes(tmp_path):
    """Catch stale-click approval and post-review dependency changes."""
    item = candidate(tmp_path)
    supervisor = ApplicationSupervisor()
    with pytest.raises(ValueError):
        supervisor.approve(item, "other", True)
    with pytest.raises(ValueError):
        supervisor.approve(item, item.identity, False)
    (item.package / "app.py").write_text("changed", encoding="utf-8")
    with pytest.raises(ValueError):
        supervisor.approve(item, item.identity, True)
    assert not item.approved


def test_independent_native_mismatch_never_starts_gui(tmp_path):
    """Catch treating a validly shaped wrong result as functional acceptance."""
    item = candidate(tmp_path)

    def forbidden(*args, **kwargs):
        """Fail if a rejected result reaches a boundary that must remain unused."""
        pytest.fail("Wrong native result must not start a GUI")

    supervisor = ApplicationSupervisor(
        native=lambda *args: {"count_words_in_text": 999, "count_vowels_in_text": 3},
        preview_factory=forbidden,
    )
    supervisor.approve(item, item.identity, True)
    with pytest.raises(ValueError, match="native application acceptance"):
        supervisor.verify(item, "http://127.0.0.1:7877")
    assert not item.verified


def test_failed_browser_closes_owned_preview_and_keeps_evidence(tmp_path):
    """Catch leaking a worker or retaining a verified grant after GUI failure."""
    item = candidate(tmp_path)

    class Preview:
        """Represent only the owned native-preview boundary for cleanup assertions."""

        closed = False
        url = "http://127.0.0.1:7877"

        def close(self):
            """Record that the owned preview was closed after verification failure."""
            self.closed = True

    preview = Preview()

    def browser(*args):
        """Write a controlled failed acceptance receipt and propagate the mismatch."""
        (tmp_path / "failure.json").write_text(json.dumps({"status": "failed"}))
        raise AssertionError("independent mismatch")

    supervisor = ApplicationSupervisor(
        native=lambda *args: {"count_words_in_text": 2, "count_vowels_in_text": 2},
        preview_factory=lambda *args, **kwargs: preview,
        browser=browser,
    )
    supervisor.approve(item, item.identity, True)
    with pytest.raises(AssertionError):
        supervisor.verify(item, "http://127.0.0.1:7877")
    assert preview.closed and not item.verified and item.preview is None
    assert (tmp_path / "failure.json").exists()
    report = json.loads((item.folder / "validation.json").read_bytes())
    assert report["stage"] == "catalog_native_browser_acceptance" and report["status"] == "failed"
    with pytest.raises(ValueError):
        supervisor.run_data(item, "text")


def test_failed_verification_never_publishes_widget_approval(tmp_path):
    """A human checkbox alone must not create a persistent reusable widget."""
    item = candidate(tmp_path)
    published = []
    item.widget_commit = lambda item: published.append(item.identity)

    class Preview:
        """Represent owned preview cleanup at the explicit boundary double."""

        url = "http://127.0.0.1:7877"

        def close(self):
            """Dispose the inert fixture after the controlled browser failure."""
            pass

    def fail(*args):
        """Simulate a failed independent result comparison."""
        raise ValueError("Independent mismatch")

    supervisor = ApplicationSupervisor(
        native=lambda *args: {"count_words_in_text": 2, "count_vowels_in_text": 2},
        preview_factory=lambda *args, **kwargs: Preview(),
        browser=fail,
    )
    supervisor.approve(item, item.identity, True)
    with pytest.raises(ValueError):
        supervisor.verify(item, "http://127.0.0.1:7877")
    assert published == [] and not item.verified
