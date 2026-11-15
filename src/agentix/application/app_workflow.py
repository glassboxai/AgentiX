"""Supervised v5 application lifecycle with explicit legacy pilot compatibility.

All model artifacts remain data on the host. Complete-package review and native
execution are required. Proposed child tests never determine the acceptance verdict.
"""

import json
import logging
from collections.abc import Callable
from dataclasses import dataclass
from functools import partial
from pathlib import Path
from typing import Any
from urllib.parse import urlsplit

from agentix.adapters.application_crewai import make_application_coordinator
from agentix.agents.catalog_agents import ApplicationCoordinator, CallableCoordinator
from agentix.lab.application_artifacts import (
    ApprovedApplication,
    application_digest,
    approve_application,
)
from agentix.lab.application_panel import ApplicationPreview
from agentix.lab.application_session import execute_application

logger = logging.getLogger(__name__)


@dataclass
class Candidate:
    """Owner-bound pending review and verified preview; never serialized to a browser."""

    identity: str
    folder: Path
    package: Path
    digest: str
    review_text: str
    approved: bool = False
    verified: bool = False
    snapshot: ApprovedApplication | None = None
    preview: object | None = None
    dependency_check: Callable[[], None] | None = None
    widget_commit: Callable[["Candidate"], None] | None = None
    catalog_id: str = ""
    display_name: str = "Text analysis"
    library_lease: object | None = None
    runtime_refresh: bool = False

    def close(self) -> None:
        """Stop only this candidate's owned application preview."""
        if self.preview is not None:
            self.preview.close()
            self.preview = None
        if self.library_lease is not None:
            self.library_lease.close()
            self.library_lease = None


class ApplicationPipeline:
    """Persist catalog-driven proposals; retain fixed composition only for legacy fixtures."""

    def __init__(
        self,
        root: Path,
        client_factory: Callable | None = None,
        *,
        widget_store: object | None = None,
        coordinator_factory: Callable[[Path], ApplicationCoordinator] | None = None,
    ) -> None:
        """Inject independent storage/model boundary; construction performs no IO."""
        self.root, self.client_factory = root.resolve(), client_factory
        self.widget_store = widget_store
        if client_factory is not None and coordinator_factory is not None:
            raise ValueError("Inject a coordinator or a legacy client, not both")
        self._uses_default_coordinator = client_factory is None and coordinator_factory is None
        self.coordinator_factory = coordinator_factory or (
            partial(CallableCoordinator, client_factory=client_factory)
            if client_factory is not None
            else make_application_coordinator
        )

    def set_model_client(self, llm: Any) -> None:
        """Use the active session client for the default CrewAI coordinator.

        Explicit legacy client and coordinator factories remain subsystem overrides.
        The method is called before generation and performs no model I/O.
        """
        if self._uses_default_coordinator:
            self.coordinator_factory = partial(make_application_coordinator, llm=llm)

    def generate(
        self, query: str, *, feedback: dict | None = None, tools: dict | None = None
    ) -> Candidate:
        """Propose a workflow and per-tool widgets without approval or host execution.

        Failures preserve the operation directory and any model evidence. No retry
        or repair is automatic. The full source closure is included in review text.
        """
        if not isinstance(query, str) or not query.strip() or len(query) > 16000:
            raise ValueError("Describe an application in at most 16000 characters")
        if not tools:
            raise ValueError(
                "Applications requires approved installed catalog tools; no internal fallback is allowed"
            )
        if any(tool.schema is None for tool in tools.values()):
            raise ValueError("Approved catalog tools require their canonical Annotated contract")
        from agentix.application.general_pipeline import generate

        return generate(self, query, tools, feedback)

    def bind_widget_publication(
        self, candidate: Candidate, tools: dict, store: object, expected_widgets: dict | None = None
    ) -> None:
        """Bind widget publication to exact current tool grants, including approved revisions."""
        if expected_widgets is None:
            expected_widgets = {role: store.load(tool) for role, tool in tools.items()}

        def check_widgets() -> None:
            """Observe co-located widget drift/revocation before reuse or publication."""
            for role, expected in expected_widgets.items():
                if store.load(tools[role]) != expected:
                    raise ValueError(
                        "A stored widget changed during review; request a fresh proposal"
                    )

        def publish_widgets(item: Candidate) -> None:
            """Publish reviewed current bytes only after independent acceptance passes."""
            check_widgets()
            snapshot = json.loads(item.review_text)
            proposals_now = snapshot["proposed_tests_and_notes"]["widgets"]
            for role, tool in tools.items():
                proposal = dict(proposals_now[role])
                filename = tool.tool_name + "_widget.py"
                proposal["widget_code"] = (item.package / filename).read_bytes().decode("utf-8")
                previous = expected_widgets[role]
                css = (item.package / filename).with_suffix(".css").read_text(encoding="utf-8")
                if (
                    previous is None
                    or not previous.approved
                    or previous.proposal != proposal
                    or previous.css != css
                ):
                    store.publish(
                        tool,
                        proposal,
                        css=(item.package / filename)
                        .with_suffix(".css")
                        .read_text(encoding="utf-8"),
                    )
                expected_widgets[role] = store.load(tool)

        candidate.dependency_check = check_widgets
        candidate.widget_commit = publish_widgets


def browser_origin_allowed(url: str, origin: str) -> bool:
    """Permit verification requests only to the maintained local preview origin."""
    try:
        target, expected = urlsplit(url), urlsplit(origin)
        return (
            len(url) <= 8192
            and target.scheme == expected.scheme == "http"
            and target.netloc == expected.netloc
            and expected.hostname == "127.0.0.1"
            and target.username is None
            and target.password is None
        )
    except (TypeError, ValueError):
        return False


class ApplicationSupervisor:
    """Maintain approval, native/data/browser gates and owned preview lifecycle."""

    def __init__(
        self,
        *,
        native: Callable = execute_application,
        browser: Callable | None = None,
        preview_factory: Callable = ApplicationPreview,
    ) -> None:
        """Inject expensive boundaries for offline tests; production remains native-only."""
        self.native, self.browser, self.preview_factory = native, browser, preview_factory

    def approve(self, candidate: Candidate, identity: str, reviewed: bool) -> None:
        """Bind explicit human review to the displayed candidate and unchanged bytes."""
        logger.info("event=application_approval_checks_started identity=%s", candidate.identity)
        if candidate.dependency_check is not None:
            candidate.dependency_check()
        logger.info("event=application_dependencies_rechecked")
        if not reviewed or identity != candidate.identity:
            logger.warning("event=application_approval_rejected reason=stale_or_unchecked_review")
            raise ValueError("Review the displayed candidate before approval")
        snapshot = approve_application(
            candidate.package,
            candidate.digest,
            allow_runtime_drift=getattr(candidate, "runtime_refresh", False),
        )
        manifest = json.loads(dict(snapshot.files)["application.json"])
        if manifest.get("schema_version") == 3:
            review = json.loads(candidate.review_text)
            from agentix.application.code_package import validate_acceptance

            acceptance = review["independent_acceptance"]
            validate_acceptance({key: acceptance[key] for key in ("payload", "expected")}, manifest)
            logger.info("event=application_acceptance_cases_validated")
        candidate.snapshot = snapshot
        candidate.approved = True
        logger.info("event=application_approved")

    def verify(self, candidate: Candidate, parent_origin: str) -> object:
        """Publish only after independent native and real browser checks pass."""
        self._snapshot(candidate)
        stage = "native_data"
        preview = None
        try:
            manifest = json.loads(dict(candidate.snapshot.files)["application.json"])
            if manifest.get("schema_version") == 3:
                from agentix.application.general_acceptance import verify

                stage = "catalog_native_browser_acceptance"
                logger.info("event=application_verify_stage stage=%s", stage)
                return verify(self, candidate, parent_origin)
            if self.native(candidate.snapshot, {"text": "Hello World!"}) != {
                "words": 2,
                "vowels": 3,
            }:
                raise ValueError("Independent native acceptance failed")
            stage = "native_gui_startup"
            preview = self.preview_factory(
                candidate.snapshot, parent_origin, display_name=candidate.display_name
            )
            candidate.preview = preview
            stage = "browser"
            self.browser(preview, candidate.folder)
            self._snapshot(candidate)
            stage = "widget_publication"
            if candidate.widget_commit is not None:
                candidate.widget_commit(candidate)
            candidate.verified = True
            (candidate.folder / "validation.json").write_text(
                json.dumps({"status": "passed", "stage": "independent_acceptance"}),
                encoding="utf-8",
            )
            return preview
        except BaseException as error:
            logger.warning(
                "event=application_verify_failed stage=%s error_type=%s",
                stage,
                type(error).__name__,
                exc_info=True,
            )
            (candidate.folder / "validation.json").write_text(
                json.dumps(
                    {
                        "status": "failed",
                        "stage": stage,
                        "error_type": type(error).__name__,
                        "required_contract": (
                            "All selected catalog widgets, typed connection-code inputs, stable unique control IDs, cleared invalid results and combined outputs must satisfy the original reviewed request and independent acceptance cases. Do not alter approved tool code or weaken expectations."
                            if manifest.get("schema_version") == 3
                            else "Both widget callbacks, exact stable control IDs, literal word/vowel counts, cleared invalid results and combined result/status must satisfy the original reviewed contract."
                        ),
                    }
                ),
                encoding="utf-8",
            )
            if preview is not None:
                preview.close()
            candidate.preview = None
            candidate.verified = False
            raise

    def _snapshot(self, candidate: Candidate) -> None:
        """Recheck the complete dependency closure before each permitted operation."""
        if candidate.dependency_check is not None:
            candidate.dependency_check()
        if (
            not candidate.approved
            or candidate.snapshot is None
            or application_digest(candidate.package) != candidate.digest
            or candidate.snapshot.digest != candidate.digest
        ):
            raise ValueError("Application is unapproved or changed after review")

    def open_verified(self, candidate: Candidate, parent_origin: str) -> object:
        """Open a protected installed snapshot without repeating prior test suites."""
        self._snapshot(candidate)
        if not candidate.verified:
            raise ValueError("Load an independently verified application first")
        candidate.preview = self.preview_factory(
            candidate.snapshot, parent_origin, display_name=candidate.display_name
        )
        return candidate.preview

    def run_data(self, candidate: Candidate, text: str) -> dict:
        """Reuse the verified application's strict data entrypoint without its GUI."""
        self._snapshot(candidate)
        if not candidate.verified:
            raise ValueError("Independent acceptance is required")
        manifest = json.loads(dict(candidate.snapshot.files)["application.json"])
        if manifest.get("schema_version") == 3:
            from agentix.application.general_package import validate_payload

            payload = json.loads(text) if isinstance(text, str) else text
            return self.native(candidate.snapshot, validate_payload(payload, manifest))
        return self.native(candidate.snapshot, {"text": text})
