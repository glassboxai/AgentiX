"""Disposable GUI recovery of a real model draft; never a new inference claim.

Operator supplies one already captured v4 review/package. No approval is copied:
complete source is redisplayed, and the new owner must explicitly review it again.
This test-only composition root uses the production frontend/backend/supervisor.
"""

import json
import os
import sys
from pathlib import Path
from uuid import uuid4

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))
os.environ.update(GRADIO_ANALYTICS_ENABLED="False", OTEL_SDK_DISABLED="true")

import gradio as gr  # noqa: E402

from agentix.application.app_workflow import Candidate  # noqa: E402
from agentix.controllers.applications import ApplicationsBackend  # noqa: E402
from agentix.controllers.sessions import SessionRegistry  # noqa: E402
from agentix.controllers.tool_controller import UiController  # noqa: E402
from agentix.lab.application_artifacts import FILES, application_digest  # noqa: E402
from agentix.security import SecurityManager  # noqa: E402
from agentix.ui.branding import launch_options  # noqa: E402
from agentix.ui.shell import build_view  # noqa: E402


def main() -> None:
    """Recover one operator-selected draft; preserve bytes and require a fresh review."""
    port, work, package, captured = (
        int(sys.argv[1]),
        Path(sys.argv[2]).resolve(),
        Path(sys.argv[3]).resolve(),
        Path(sys.argv[4]),
    )
    snapshot = json.loads(captured.read_bytes())
    application_digest(package)
    for name in FILES:
        if (package / name).read_text(encoding="utf-8") != snapshot["source_files"][name]:
            raise ValueError("Recovered source differs from captured GUI snapshot")
    if json.loads((package / "application.json").read_bytes()) != snapshot["manifest"]:
        raise ValueError("Recovered manifest differs from captured snapshot")

    class RecoveryPipeline:
        """Load only this exact real-model draft, with no LLM boundary or inherited grant."""

        def __init__(self, root):
            """Keep production's injected pipeline interface; use owned disposable storage."""
            self.root = work

        def generate(self, query):
            """Copy unchanged bytes into a new review; never label this fresh generation."""
            if query != snapshot["original_request"]:
                raise ValueError("Recovery must retain the original user request")
            identity = uuid4().hex
            folder = self.root / identity
            target = folder / "application"
            target.mkdir(parents=True)
            for name in FILES | {"application.json"}:
                (target / name).write_bytes((package / name).read_bytes())
            (folder / "requirements.txt").write_text(query, encoding="utf-8")
            review = dict(snapshot)
            review["recovery"] = {
                "fresh_model_generation": False,
                "original_review": str(captured),
                "description": "Unchanged artifacts from the actual local-model GUI trial; fresh approval required.",
            }
            return Candidate(
                identity, folder, target, application_digest(target), json.dumps(review, indent=2)
            )

    def controller(identity):
        """Create owner controls without constructing an unused model for this recovery."""
        security = SecurityManager.for_owner(identity)
        security.TOOLS_ROOT_DIR = str(work / "unused-tools" / identity)
        return UiController(
            lambda query: "Recovery-only test server", lambda: "No test tools", security, gr.update
        )

    registry = SessionRegistry(controller)
    backend = ApplicationsBackend(registry, pipeline_factory=RecoveryPipeline, parent_port=port)
    demo = build_view(registry, applications_backend=backend)
    demo.demo.queue().launch(
        server_name="127.0.0.1",
        server_port=port,
        inbrowser=False,
        theme=demo.theme,
        **launch_options(),
    )


if __name__ == "__main__":
    main()
