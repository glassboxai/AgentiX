"""Interactive command-line entrypoint with lazy runtime construction."""

import json
import logging
import sys
import threading
from collections.abc import Callable
from typing import Any
from uuid import uuid4

from .diagnostics import log_event, operation_scope

logger = logging.getLogger(__name__)


def display_review(text: str) -> None:
    """Escape terminal controls in untrusted review text without changing stored bytes.

    Printable characters, line breaks and tabs remain readable. Escape sequences,
    carriage returns and bidi controls cannot erase or reorder the review prompt.
    """
    print(
        "".join(
            char if char.isprintable() or char in "\n\t" else f"\\u{ord(char):04x}" for char in text
        )
    )


def review_request(security: Any, pending: dict[str, Any]) -> None:
    """Display one immutable snapshot and resolve only its original identifiers.

    Input is read exclusively on the main thread. Editing never authorizes a
    request: a separate explicit approval is required after `.end`.
    """
    display_review(f"\nREVIEW REQUIRED: {pending['action']} — {pending['filepath']}")
    context = pending.get("review_context", {})
    for name, value in context.items():
        display_review(f"\n{name}:\n{value}")
    content = pending["content"]
    display_review(content)
    while True:
        choice = input("Approve / reject (default) / edit: ").strip().lower()
        if choice == "edit":
            print("Enter replacement content; finish with .end on its own line.")
            lines = []
            while (line := input("| ")) != ".end":
                lines.append(line)
            content = "\n".join(lines)
            display_review(content)
            continue
        if choice not in ("approve", "reject", ""):
            print("Choose approve, reject or edit.")
            continue
        accepted = security.resolve_pending_request(
            choice == "approve",
            content if choice == "approve" else None,
            request_id=pending["request_id"],
            owner_id=pending["owner_id"],
        )
        log_event(
            logger,
            "cli_review_resolved" if accepted else "cli_review_stale",
            request_id=pending["request_id"],
        )
        if not accepted:
            print("Request expired or changed; no decision was accepted.")
        return


def run_with_review(run_system: Callable[[str], str], query: str, security: Any) -> str:
    """Run the shared workflow while the terminal services owner-bound reviews.

    Worker errors propagate to the original CLI recovery loop. On interruption
    the caller closes the coordinator; daemonization does not cancel model I/O.
    """
    completed = threading.Event()
    result: list[Any] = []
    errors: list[BaseException] = []
    operation = uuid4().hex
    security.operation_id = operation

    def worker() -> None:
        """Publish a result before signalling completion, with correlated logs."""
        with operation_scope(security.owner_id, operation):
            log_event(logger, "cli_workflow_started")
            try:
                result.append(run_system(query))
            except BaseException as exc:
                errors.append(exc)
            finally:
                log_event(logger, "cli_workflow_finished")
                completed.set()

    threading.Thread(target=worker, daemon=True).start()
    displayed = None
    while not completed.wait(0.05):
        pending = security.get_pending_request()
        if pending and pending["request_id"] != displayed:
            displayed = pending["request_id"]
            with operation_scope(security.owner_id, operation):
                review_request(security, pending)
    if errors:
        raise errors[0]
    return result[0]


def run_cli(
    run_system: Callable[[str], str] | None = None, *, security: Any = None, validation: Any = None
) -> None:
    """Run terminal queries and manual reviews; EOF/Ctrl+C deny and close work.

    Injected legacy workflows without a coordinator retain synchronous behavior.
    Production uses the same runtime and acceptance services as the browser.
    """
    if run_system is None:
        from .bootstrap import get_default_runtime

        runtime = get_default_runtime()
        run_system = runtime.orchestrator.run_system
        security = runtime.security
        validation = runtime.operations.acceptance
    print("\n" + "=" * 70)
    print("   AUTONOMOUS MULTI-AGENT TOOL BUILDER SYSTEM")
    print("   Type 'quit', 'exit' or 'q' to stop the program.")
    print("=" * 70 + "\n")
    while True:
        try:
            user_input = input("\nEnter your query: ").strip()
            if user_input.lower() in ["quit", "exit", "q"]:
                if security is not None:
                    security.cancel_pending()
                print("\n[INFO] Exiting session. Goodbye!")
                sys.exit(0)
            if not user_input:
                continue
            response = (
                run_with_review(run_system, user_input, security)
                if security is not None
                else run_system(user_input)
            )
            print("\n" + "=" * 50)
            print("FINAL SYSTEM RESPONSE:")
            print("=" * 50)
            print(response)
            if validation is not None:
                print("\nHOST VALIDATION STATUS:")
                print(json.dumps(validation.status(), indent=2, ensure_ascii=True))
        except (KeyboardInterrupt, EOFError):
            if security is not None:
                security.cancel_pending()
            print("\n[INFO] Session ended; pending permissions denied.")
            sys.exit(0)
        except Exception as e:
            log_event(logger, "cli_workflow_failed", error=e, level=logging.ERROR)
            print(f"\n[ERROR] An unexpected error occurred: {e}")
