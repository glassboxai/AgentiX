"""Timing diagnostics preserve failures without logging source/prompt bodies."""

import pytest

from agentix.lab.widget_session import WidgetSession


def test_failed_staging_keeps_safe_duration_and_cleans_owned_tree(monkeypatch):
    """Catch missing startup failure diagnostics and leaked partial private runtimes."""
    import agentix.lab.widget_session as module

    def failed(root):
        raise RuntimeError("PRIVATE_SYNTHETIC_SOURCE")

    monkeypatch.setattr(module, "stage_runtime", failed)
    session = WidgetSession()
    with pytest.raises(RuntimeError):
        session.__enter__()
    assert session.diagnostics["startup_failure"] == "RuntimeError"
    assert session.timings["startup_failed_after"] >= 0
    assert "PRIVATE_SYNTHETIC_SOURCE" not in str(session.diagnostics)
    assert not session.root.exists()


@pytest.mark.parametrize(
    "value",
    [
        {"gradio_import": -1},
        {"gradio_import": True},
        {"gradio_import": float("nan")},
        {"unknown": 0},
    ],
)
def test_invalid_child_timings_cannot_enter_diagnostics(value):
    """Diagnostic channel rejects arbitrary fields, coercion and nonfinite durations."""
    session = WidgetSession()
    try:
        with pytest.raises(ValueError):
            session._control_message({"type": "startup_timings", "seconds": value})
        assert "child_timings" not in session.diagnostics
    finally:
        session.close()
