"""Session-bound two-step permanent deletion; no Gradio or arbitrary path inputs."""

import logging
import os
import secrets
import stat
import time
from pathlib import Path

from agentix.controllers import explorer_window
from agentix.controllers.session_access import SessionOwnerAccess
from agentix.diagnostics import log_event
from agentix.storage.catalog import ToolCatalog
from agentix.storage.maintenance import CatalogMaintenance
from agentix.storage.widget_store import WidgetStore

logger = logging.getLogger(__name__)

CONFIRMATION_TTL_SECONDS = 120  # Lifetime of one owner/content-bound deletion confirmation.


def open_directory(path: Path) -> None:
    """Open one already-validated folder with the OS file manager, never a shell.

    A refused shell association is reported as ``ValueError`` so the owner sees the
    maintained modal instead of a raw framework error.
    """
    if not hasattr(os, "startfile"):
        raise ValueError("Opening a catalog folder is only supported on Windows")
    try:
        os.startfile(str(path))
    except OSError as error:
        raise ValueError("The catalog folder could not be opened by the file manager") from error


class CatalogMaintenanceBackend(SessionOwnerAccess):
    """Keep one expiring confirmation on its owning controller, never in model context."""

    def __init__(
        self,
        registry,
        applications,
        *,
        service_factory=None,
        clock=time.monotonic,
        opener=None,
        window_snapshot=None,
        focus_window=None,
    ):
        """Inject sessions/application library, clock, folder opener and window focus."""
        super().__init__(registry)
        self.applications, self.service_factory, self.clock = applications, service_factory, clock
        self.opener = opener or open_directory
        self.window_snapshot = window_snapshot or explorer_window.snapshot
        self.focus_window = focus_window or explorer_window.focus_opened_window

    @staticmethod
    def _idle(controller) -> None:
        """Reject mutation while this owner's workflow, generation or review is pending."""
        if getattr(controller, "_closed", False) or any(
            getattr(controller.state, name, False)
            for name in ("is_running", "application_busy", "application_review_pending")
        ):
            raise ValueError("Finish or reject the current operation before catalog removal")

    def _service(self, controller):
        """Compose strict revocation and exact roots, without reading credentials."""
        if self.service_factory is not None:
            return self.service_factory(controller)
        operations = controller.tool_operations

        def revoke(name):
            """Require durable revocation to succeed before removing any package bytes."""
            if operations.verification.store is not None:
                operations.verification.store.revoke(name)
            operations.verification.invalidate(name)

        return CatalogMaintenance(
            Path(controller.security.TOOLS_ROOT_DIR),
            self.applications.library_factory(),
            revoke_tool=revoke,
            revoke_widget=WidgetStore.for_controller(controller).records.revoke,
        )

    def choices(self, kind: str, token: str | None, request):
        """List exact server-owned IDs/names; browser values are never filesystem paths."""
        session = self._session(token, request)
        if kind == "application":
            choices, owned = self.applications.catalog_entries(token, request)
            return choices, owned
        if kind != "tool":
            raise ValueError("Unknown catalog")
        root = Path(session.controller.security.TOOLS_ROOT_DIR)
        catalog = ToolCatalog(root)
        choices = (
            [
                (path.name, path.name)
                for path in sorted(root.iterdir())
                if catalog.contains(path.name)
            ]
            if root.exists()
            else []
        )
        return choices, session.token

    def reseal_tools(self, token: str | None, request):
        """Reseal intact approvals, then run the isolated tests of changed tools.

        A record whose bytes are unchanged is rebound to the current policy without
        executing anything. A missing or changed record is re-verified through the
        isolated test runner, which never imports generated code on the host; the
        batch stops at the first failure. Acceptance review stays mandatory and is
        never granted here.
        """
        session = self._session(token, request)
        controller = session.controller
        with controller._lock:
            self._idle(controller)
            operations = getattr(controller, "tool_operations", None)
            store = getattr(getattr(operations, "verification", None), "store", None)
            if store is None:
                raise ValueError("Durable approval storage is unavailable for this session")
            root = Path(controller.security.TOOLS_ROOT_DIR)
            catalog = ToolCatalog(root)
            names = (
                [path.name for path in sorted(root.iterdir()) if catalog.contains(path.name)]
                if root.exists()
                else []
            )
            if not names:
                return "No installed tools to reseal.", session.token
            resealed, ran = [], []
            for name in names:
                folder = root / name
                code_path, tests_path = folder / f"{name}_code.py", folder / f"{name}_tests.py"
                if not code_path.is_file() or not tests_path.is_file():
                    return (
                        f"Stopped at {name}: its code or tests are missing. "
                        f"Resealed {len(resealed)} tool(s) before that.",
                        session.token,
                    )
                outcome = store.reseal(name, code_path.read_bytes(), tests_path.read_bytes())
                if outcome is None:
                    resealed.append(name)
                    continue
                if outcome == "invalid":
                    return (
                        f"Resealed {len(resealed)} tool(s). Stopped at {name}: its record or "
                        "reviewed contract cannot be revalidated, so run and approve it in Tools.",
                        session.token,
                    )
                status = operations.verify_existing_tool_tool(name)
                if not status.startswith("TESTS_PROVISIONAL_PASSED"):
                    return (
                        f"Resealed {len(resealed)} tool(s). Stopped at {name}: its isolated tests "
                        f"did not pass, so run and approve it in Tools. {status.splitlines()[0]}",
                        session.token,
                    )
                ran.append(name)
            logger.info("event=catalog_reseal_finished count=%s ran=%s", len(resealed), len(ran))
            if ran:
                return (
                    f"Resealed {len(resealed)} tool(s) and re-ran the isolated tests of "
                    f"{len(ran)} changed tool(s): {', '.join(ran)}. Their tests passed; "
                    "complete the acceptance review in Tools to restore reusable approval.",
                    session.token,
                )
            return f"Resealed {len(resealed)} tool(s) under the current policy.", session.token

    def reveal(self, kind: str, token: str | None, request):
        """Open this owner's installed catalog folder without accepting a browser path.

        The root comes from server state, must already exist and must not be a
        symbolic link or reparse point. Opening a folder grants the page no read,
        write or execution capability, and no directory is created here. After a
        completed open the folder window is raised above the browser; a refused
        foreground change is logged and never turns the open into a failure.
        """
        session = self._session(token, request)
        if kind == "tool":
            candidate = Path(session.controller.security.published_tools_root())
            label = "tools"
        elif kind == "application":
            candidate = Path(self.applications.library_factory().root)
            label = "applications"
        else:
            raise ValueError("Unknown catalog")
        if candidate.is_symlink():
            raise ValueError(f"The installed {label} folder is unavailable")
        resolved = candidate.resolve()
        if not resolved.is_dir():
            raise ValueError(f"The installed {label} folder is unavailable")
        attributes = getattr(resolved.stat(follow_symlinks=False), "st_file_attributes", 0)
        if attributes & getattr(stat, "FILE_ATTRIBUTE_REPARSE_POINT", 0):
            raise ValueError(f"The installed {label} folder is unavailable")
        try:
            before = self.window_snapshot()
        except OSError:
            before = frozenset()
        try:
            self.opener(resolved)
        except OSError as error:
            raise ValueError(
                f"The installed {label} folder could not be opened by the file manager"
            ) from error
        try:
            self.focus_window(resolved.name, before)
        except (OSError, ValueError) as error:
            log_event(
                logger,
                "catalog_folder_focus_failed",
                level=logging.WARNING,
                error=error,
            )
        return f"Opened the installed {label} folder."

    def prepare(self, kind: str, selected: str, token: str | None, request):
        """Perform read-only checks and mint a one-use owner/content-bound confirmation."""
        session = self._session(token, request)
        controller = session.controller
        with controller._lock:
            self._idle(controller)
            service = self._service(controller)
            snapshot = (
                service.prepare_tool(selected)
                if kind == "tool"
                else service.prepare_app(selected)
                if kind == "application"
                else None
            )
            if snapshot is None:
                raise ValueError("Unknown catalog")
            confirmation = secrets.token_urlsafe(32)
            controller._catalog_pending = (
                confirmation,
                service,
                snapshot,
                self.clock() + CONFIRMATION_TTL_SECONDS,
            )
        return (
            f"Are you sure you want to permanently delete this {kind}: {snapshot.package.name}? This cannot be undone.",
            confirmation,
            session.token,
        )

    def _pending(self, confirmation: str, session):
        """Check the already-resolved owner while holding only its controller lock."""
        self._idle(session.controller)
        pending = getattr(session.controller, "_catalog_pending", None)
        if (
            not pending
            or not isinstance(confirmation, str)
            or not secrets.compare_digest(pending[0], confirmation)
            or self.clock() >= pending[3]
        ):
            raise ValueError("Deletion confirmation expired or changed")
        return pending

    def cancel(self, confirmation: str, token: str | None, request):
        """Discard only this exact confirmation without touching files or grants."""
        session = self._session(token, request)
        with session.controller._lock:
            self._pending(confirmation, session)
            session.controller._catalog_pending = None
        return "Deletion cancelled.", session.token

    def confirm(self, confirmation: str, token: str | None, request):
        """Consume once; never reacquire the session-registry lock under the owner lock."""
        session = self._session(token, request)
        with session.controller._lock:
            pending = self._pending(confirmation, session)
            session.controller._catalog_pending = None
            pending[1].confirm(pending[2])
        return f"Selected {pending[2].kind} permanently deleted.", session.token
