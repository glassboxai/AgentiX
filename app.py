"""Legacy Gradio launch entrypoint; import alone never builds or starts a UI."""

from typing import Any

import _agentix_path
from agentix.ui.controller import format_thoughts_markdown
from agentix.ui.state import ANSI_ESCAPE, ConsoleThoughtsCapture, ExecutionState

_CALLBACKS = (
    "process_user_query",
    "poll_system_status",
    "on_approve",
    "on_reject",
    "on_toggle_auto_approve",
    "state",
    "captured_stdout",
)


def __getattr__(name: str) -> Any:
    """Lazily expose legacy callbacks, state and Blocks for existing callers."""
    if name in _CALLBACKS or name in ("demo", "custom_theme"):
        from agentix.bootstrap import get_default_ui

        controller, view = get_default_ui()
        if name == "demo":
            return view.demo
        if name == "custom_theme":
            return view.theme
        return getattr(controller, name)
    raise AttributeError(name)


def main() -> None:
    """Launch the compatible loopback UI using explicit startup composition."""
    from agentix.bootstrap import run_ui

    run_ui()


if __name__ == "__main__":
    main()
