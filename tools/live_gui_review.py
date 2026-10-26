"""Launch the real Agentix GUI with temporary storage for supervised model testing.

This is an opt-in operational harness, not an offline regression or a simulated
workflow. It uses real CrewAI, local Ollama and the native execution boundary.
No approvals are automated. Existing project-generated artifacts are never used.
"""

import argparse
import json
import os
import sys
import tempfile
from pathlib import Path


def main() -> None:
    """Start a separate loopback UI and record its explicitly temporary storage.

    The caller owns process lifetime. Temporary artifacts are retained for review;
    this launcher never deletes existing directories or restarts another server.
    """
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--port", type=int, default=7861)
    parser.add_argument("--model", default="ollama/qwen3-coder:30b")
    parser.add_argument("--manifest", type=Path, required=True)
    args = parser.parse_args()
    root = Path(__file__).resolve().parents[1]
    sys.path.insert(0, str(root / "src"))
    os.environ["GRADIO_ANALYTICS_ENABLED"] = "False"
    from agentix.bootstrap import configure_process, create_runtime
    from agentix.diagnostics import activity_output
    from agentix.settings import Settings
    from agentix.ui.branding import launch_options
    from agentix.ui.controller import UiController
    from agentix.ui.sessions import SessionRegistry
    from agentix.ui.view import build_view

    configure_process()
    import gradio as gr

    artifacts = Path(tempfile.mkdtemp(prefix="agentix-live-hitl-"))
    settings = Settings(root, artifacts, model=args.model)
    args.manifest.write_text(
        json.dumps(
            {
                "storage": str(artifacts),
                "port": args.port,
                "model": args.model,
                "pid": os.getpid(),
                "real_model": True,
                "native_isolation": True,
                "manual_approvals": True,
            },
            indent=2,
        ),
        encoding="utf-8",
    )

    def create(identity: str) -> UiController:
        """Compose actual agents/services for each browser, without fixture doubles."""
        runtime = create_runtime(settings, owner_id=identity)
        runtime.security.approval_timeout = 900
        controller = UiController(
            runtime.orchestrator.run_system,
            runtime.catalog.render,
            runtime.security,
            gr.update,
            validation=runtime.operations.acceptance,
        )
        controller.state.session_id = identity
        return controller

    view = build_view(SessionRegistry(create), gradio_module=gr)
    with activity_output():
        view.demo.queue().launch(
            server_name="127.0.0.1",
            server_port=args.port,
            theme=view.theme,
            inbrowser=False,
            **launch_options(),
        )


if __name__ == "__main__":
    main()
