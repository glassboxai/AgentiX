"""Preview an explicitly reviewed package through native Gradio and a maintained bridge."""

import argparse
import json
from pathlib import Path

import _agentix_path  # noqa: F401
from agentix.bootstrap import configure_process
from agentix.lab.widget_artifacts import approve_package
from agentix.lab.widget_bridge import serve_widget
from agentix.lab.widget_session import WidgetSession, run_provisional_tests


def main() -> None:
    """Require a review digest; never approve a package merely because it exists."""
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--package", type=Path, required=True)
    parser.add_argument("--approved-digest", required=True)
    parser.add_argument("--duration", type=int, default=300)
    parser.add_argument("--evidence", type=Path)
    parser.add_argument("--port", type=int, default=7875)
    args = parser.parse_args()
    if not 1024 <= args.port <= 65535:
        parser.error("An unprivileged explicit port is required")
    approved = approve_package(args.package, args.approved_digest)
    configure_process()
    provisional = run_provisional_tests(approved)
    with WidgetSession(approved, lifetime=args.duration) as session:
        session.diagnostics["provisional_tests"] = provisional
        try:
            serve_widget(session, args.port)
        finally:
            if args.evidence:
                args.evidence.write_text(
                    json.dumps(
                        {
                            "diagnostics": session.diagnostics,
                            "tool_receipts": session.tool_receipts,
                        },
                        default=lambda item: item.decode(errors="replace")
                        if isinstance(item, bytes)
                        else str(item),
                        indent=2,
                    )
                )


if __name__ == "__main__":
    main()
