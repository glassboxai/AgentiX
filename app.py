"""Legacy Gradio launch entrypoint; import alone never builds or starts a UI."""

from typing import Any

import _agentix_path
from agentix.controllers.state import ANSI_ESCAPE, ConsoleThoughtsCapture, ExecutionState
from agentix.controllers.tool_controller import format_thoughts_markdown

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
    """Lazily expose legacy callbacks and controller state for existing callers."""
    if name in _CALLBACKS:
        from agentix.bootstrap import get_default_ui

        controller = get_default_ui()[0]
        return getattr(controller, name)
    raise AttributeError(name)


def main() -> None:
    """Launch the compatible loopback UI using explicit startup composition."""
    from agentix.bootstrap import run_ui

    run_ui()


if __name__ == "__main__":
    main()
