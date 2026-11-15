"""Launch a reviewed composite application independently of any laboratory view.

The maintained supervisor enforces native isolation; app.py is never imported here.
Explicit review bytes are required. Standalone mode denies framing by other pages.
"""

import argparse
import json
import logging
import sys
import time
from pathlib import Path

import _agentix_path  # noqa: F401
from agentix.bootstrap import configure_process
from agentix.lab.application_artifacts import approve_application
from agentix.lab.application_panel import ApplicationPreview, reviewed_application
from agentix.lab.application_session import execute_application


def main() -> None:
    """Validate the package and start only its owned loopback listener/native job."""
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--package", type=Path)
    parser.add_argument("--reviewed-digest")
    parser.add_argument("--port", type=int, default=7876)
    parser.add_argument(
        "--duration",
        type=int,
        default=0,
        help="0: until explicit stop; 1..300: finite test session",
    )
    parser.add_argument("--headless-input", help="Strict JSON object containing text")
    parser.add_argument("--evidence", type=Path)
    args = parser.parse_args()
    if not 1024 <= args.port <= 65535:
        parser.error("An explicit unprivileged port is required")
    if bool(args.package) != bool(args.reviewed_digest):
        parser.error("Package and reviewed digest must be supplied together")
    if sys.version_info[:3] != (3, 11, 9):
        parser.error("The reviewed Python 3.11.9 interpreter is required")
    configure_process()
    logging.basicConfig(level=logging.INFO)
    approved = (
        approve_application(args.package, args.reviewed_digest)
        if args.package
        else reviewed_application()
    )
    if args.headless_input is not None:
        print(json.dumps(execute_application(approved, json.loads(args.headless_input))))
        return
    preview = ApplicationPreview(
        approved, None, port=args.port, lifetime=None if args.duration == 0 else args.duration
    )
    try:
        print("Application ready: " + preview.url, flush=True)
        while preview.alive:
            time.sleep(0.2)
    except KeyboardInterrupt:
        pass
    finally:
        preview.close()
        if args.evidence:
            args.evidence.write_text(
                json.dumps(preview.session.diagnostics, default=str, indent=2), encoding="utf-8"
            )


if __name__ == "__main__":
    main()
