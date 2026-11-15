"""Authenticated persistent widget reuse; implementation lives beside its installed tool.

Only the maintained host publishes after explicit review and independent success.
Protected records are separate from untrusted tool storage. No source is imported.
"""

import hashlib
import json
import logging
from dataclasses import dataclass
from pathlib import Path
from typing import Any

from agentix.agents.application_agents import validate_source
from agentix.security.approval_store import ApprovalStore
from agentix.security.data_protection import WindowsDataProtection
from agentix.storage.application_catalog import ApprovedTool
from agentix.storage.locations import data_directory

logger = logging.getLogger(__name__)


@dataclass(frozen=True)
class StoredWidget:
    """Proposal bytes and whether the exact current binding retains prior approval."""

    proposal: dict[str, str]
    approved: bool
    css: str = ""


def widget_policy() -> str:
    """Bind runtime and maintained widget/context contracts, never traverse tools."""
    root = Path(__file__).resolve().parents[1]
    digest = hashlib.sha256(b"AgentiX-v5-widget-approval-v1")
    for path in (
        root / "storage/widget_store.py",
        root / "application/templates/code/application_context.py",
        root / "application/templates/code/element_ids.py",
        root / "domain/tool_schema.py",
        root / "widgets/styles.py",
        root.parents[1] / "infra/runtime.lock.txt",
    ):
        digest.update(path.name.encode())
        digest.update(path.read_bytes())
    return digest.hexdigest()


class WidgetStore:
    """Protect reusable widget approval and exact per-tool source under Windows user scope."""

    def __init__(
        self, security: Any, directory: Path, *, protector: Any = None, policy: str | None = None
    ) -> None:
        """Inject protection/storage; construction never reads or writes tool artifacts."""
        self.security = security
        self.records = ApprovalStore(
            directory,
            Path(security.TOOLS_ROOT_DIR),
            protector=protector if protector is not None else WindowsDataProtection(),
            policy=policy if policy is not None else widget_policy(),
        )

    @classmethod
    def for_controller(cls, controller: Any) -> "WidgetStore":
        """Compose persistent user-local records outside installed tool storage."""
        root = data_directory() / "approvals" / "widgets"
        return cls(controller.security, root)

    def _binding(self, tool: ApprovedTool) -> dict:
        """Describe exact reviewed dependencies without persisting executable trust markers."""
        return {
            "schema": 1,
            "root": self.records.root,
            "tool": tool.tool_name,
            "function": tool.function,
            "code": hashlib.sha256(tool.code).hexdigest(),
            "tests": hashlib.sha256(tool.tests).hexdigest(),
            "contract": tool.contract_digest,
            "policy": self.records.policy,
        }

    def _companion(self, tool: ApprovedTool, suffix: str) -> Path:
        """Resolve one exact widget member and reject links before reads or writes."""
        if suffix not in {"_widget.py", "_widget.css", "_widget_tests.py"}:
            raise ValueError("Unknown widget member")
        expected = (
            Path(self.security.TOOLS_ROOT_DIR).resolve()
            / tool.tool_name
            / (tool.tool_name + suffix)
        )
        resolved = Path(
            self.security.validate_and_resolve_path(tool.tool_name, tool.tool_name + suffix)
        )
        if (
            resolved != expected
            or expected.is_symlink()
            or (expected.exists() and (not expected.is_file() or expected.stat().st_nlink != 1))
        ):
            raise ValueError("Widget member aliases are forbidden")
        return expected

    def load(self, tool: ApprovedTool) -> StoredWidget | None:
        """Reuse exact approvals, or present changed source as unapproved without regeneration.

        Authentication failures are explicit errors; ordinary absence means no widget
        has been published. Reads are bounded and never execute source or tests.
        """
        path, record_path = self._companion(tool, "_widget.py"), self.records._path(tool.tool_name)
        if not record_path.exists() and not path.exists():
            return None
        if not record_path.exists():
            raise ValueError(
                "Existing widget has no protected approval metadata; explicit review is required"
            )
        with record_path.open("rb") as stream:
            sealed = stream.read(262145)
        if len(sealed) > 262144:
            raise ValueError("Widget approval exceeds limit")
        raw = self.records.protector.unseal(sealed)
        if len(raw) > 196608:
            raise ValueError("Widget approval exceeds limit")
        record = json.loads(raw)
        if set(record) != {"binding", "widget", "proposal", "css", "tests"} or not isinstance(
            record["proposal"], dict
        ):
            raise ValueError("Invalid widget approval metadata")
        proposal = dict(record["proposal"])
        self._validate(tool, proposal)
        with path.open("rb") as stream:
            source = stream.read(65537)
        if len(source) > 65536:
            raise ValueError("Widget exceeds limit")
        from agentix.widgets.styles import validate_widget_css

        css_path = self._companion(tool, "_widget.css")
        tests_path = self._companion(tool, "_widget_tests.py")
        for member in (css_path, tests_path):
            if member.is_symlink() or member.resolve() != member or member.stat().st_size > 65536:
                raise ValueError("Invalid widget companion file")
        css = validate_widget_css(css_path.read_bytes().decode("utf-8"), tool.role)
        approved = (
            record["css"] == hashlib.sha256(css_path.read_bytes()).hexdigest()
            and record["tests"] == hashlib.sha256(tests_path.read_bytes()).hexdigest()
            and tests_path.read_bytes() == proposal["tests_code"].encode("utf-8")
            and record["binding"] == self._binding(tool)
            and record["widget"] == hashlib.sha256(source).hexdigest()
            and source == proposal["widget_code"].encode("utf-8")
        )
        proposal["widget_code"] = source.decode("utf-8")
        proposal["tests_code"] = tests_path.read_bytes().decode("utf-8")
        self._validate(tool, proposal)
        return StoredWidget(proposal, approved, css)

    def _validate(self, tool: ApprovedTool, proposal: dict) -> None:
        """Check bounded proposal data and static interface before any persistence."""
        if set(proposal) != {"widget_code", "tests_code", "notes"} or any(
            not isinstance(value, str) or len(value.encode("utf-8")) > 65536
            for value in proposal.values()
        ):
            raise ValueError("Invalid widget proposal")
        module = tool.schema["module"] if tool.schema is not None else tool.tool_name + "_code"
        validate_source(proposal["widget_code"], {"gradio", "typing", module}, "create_widget")
        compile(proposal["tests_code"], "proposed_widget_tests.py", "exec")

    def publish(
        self, tool: ApprovedTool, proposal: dict[str, str], *, css: str | None = None
    ) -> None:
        """Publish only after the caller's human/native/browser gates succeed.

        This trusted internal method is not a model/UI API. A partial filesystem
        failure cannot create a valid old grant for changed bytes. Existing tool
        source and tests are never modified; only its conventional widget is written.
        """
        self._validate(tool, proposal)
        from agentix.widgets.styles import default_widget_css, validate_widget_css

        css = validate_widget_css(default_widget_css(tool.role) if css is None else css, tool.role)
        source = proposal["widget_code"].encode("utf-8")
        record = {
            "binding": self._binding(tool),
            "widget": hashlib.sha256(source).hexdigest(),
            "proposal": proposal,
            "css": hashlib.sha256(css.encode("utf-8")).hexdigest(),
            "tests": hashlib.sha256(proposal["tests_code"].encode("utf-8")).hexdigest(),
        }
        raw = json.dumps(record, sort_keys=True).encode()
        if len(raw) > 196608:
            raise ValueError("Widget approval exceeds limit")
        sealed = self.records.protector.seal(raw)
        if len(sealed) > 262144:
            raise ValueError("Widget approval exceeds limit")
        target = self._companion(tool, "_widget.py")
        css_target = self._companion(tool, "_widget.css")
        tests_target = self._companion(tool, "_widget_tests.py")
        record_path = self.records._path(tool.tool_name)
        record_path.parent.mkdir(parents=True, exist_ok=True)
        css_target.write_bytes(css.encode("utf-8"))
        tests_target.write_bytes(proposal["tests_code"].encode("utf-8"))
        target.write_bytes(source)
        record_path.write_bytes(sealed)
        logger.info("event=approved_widget_published role=%s", tool.role)
