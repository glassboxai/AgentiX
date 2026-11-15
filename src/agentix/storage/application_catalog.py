"""Resolve Applications dependencies from the installed catalog and approval ledger.

No generated source is imported and no tool tests are executed. This adapter is
invoked by normal runtime only; engineering tests inject temporary trusted tools.
"""

import logging
from collections.abc import Mapping
from dataclasses import dataclass
from pathlib import Path
from typing import Any

from agentix.security.reuse_policy import allowed_modules, computation_only, unapproved_imports
from agentix.storage.catalog import ToolCatalog

logger = logging.getLogger(__name__)


class CatalogDependencyError(ValueError):
    """Expose only maintained actionable catalog/approval errors to the owner UI."""


@dataclass(frozen=True)
class ApprovedTool:
    """Exact installed source and reviewed identity; never a browser-supplied path."""

    role: str
    tool_name: str
    function: str
    code: bytes
    tests: bytes
    contract_digest: str
    reviewed_contract: dict | None = None
    schema: dict | None = None


class ApprovedToolRegistry:
    """Require catalog membership and reusable approval before packaging a tool."""

    def __init__(self, catalog: ToolCatalog, ledger: Any) -> None:
        """Inject the same catalog and owner ledger used by the Tools controller."""
        self.catalog, self.ledger = catalog, ledger

    @classmethod
    def for_controller(cls, controller: Any) -> "ApprovedToolRegistry":
        """Resolve services from the controller's actual catalog/validation adapters."""
        catalog = getattr(controller.get_installed_tools_catalog, "__self__", None)
        ledger = getattr(controller.validation, "ledger", None)
        if not isinstance(catalog, ToolCatalog) or ledger is None:
            raise CatalogDependencyError(
                "Applications requires the installed catalog and approved tools. Create and approve the required tools in Tools first."
            )
        return (
            CatalogToolRegistry(catalog, ledger)
            if getattr(controller.security, "strict_tool_contract", False)
            else cls(catalog, ledger)
        )

    def resolve(self) -> dict[str, ApprovedTool]:
        """Return approved portable computation tools, or fail before model inference.

        Roles are the approved catalog tool names themselves, so no fixed semantic
        role registry or example tool name is required. Each entry carries the
        canonical schema derived from its exact approved source.
        """
        from pathlib import Path

        from agentix.domain.tool_schema import extract_tool_schema

        root = Path(self.catalog.root)
        if not root.is_dir():
            raise CatalogDependencyError(
                "No approved tools are installed. Create and approve them in Tools first."
            )
        result = {}
        for name in sorted(root.iterdir()):
            if not self.catalog.contains(name.name) or not self.ledger.prepare_reuse(name.name):
                raise CatalogDependencyError(
                    f"Required catalog tool {name.name} has no current reusable approval. Approve and validate it in Tools first."
                )
            code, tests = self.ledger.snapshot(name.name)
            context = self.ledger.acceptance_context(name.name)
            if not context or not computation_only(code.decode("utf-8")):
                raise CatalogDependencyError(
                    f"Approved catalog tool {name.name} is not supported by this computation-only application contract."
                )
            try:
                schema = extract_tool_schema(name.name, code.decode("utf-8"))
            except (ValueError, SyntaxError) as exc:
                raise CatalogDependencyError(
                    f"Catalog tool {name.name} requires one canonical Annotated public function."
                ) from exc
            logger.debug("event=application_catalog_dependency_verified role=%s", name.name)
            result[name.name] = ApprovedTool(
                name.name,
                name.name,
                schema["function"],
                code,
                tests,
                context["contract_digest"],
                context.get("reviewed_contract"),
                schema,
            )
        if not result:
            raise CatalogDependencyError(
                "No approved tools are installed. Create and approve them in Tools first."
            )
        return result

    def recheck(self, expected: Mapping[str, ApprovedTool]) -> None:
        """Reject removal, revocation or changed bytes/contracts without rerunning tests."""
        if self.resolve() != dict(expected):
            raise CatalogDependencyError(
                "Installed catalog tools or their approvals changed; generate a new reviewed application."
            )


class CatalogToolRegistry(ApprovedToolRegistry):
    """Discover approved canonical Annotated APIs; no fixed semantic role registry."""

    def resolve(self) -> dict[str, ApprovedTool]:
        """List a bounded portable approved catalog, skipping unapproved/legacy APIs.

        This never runs tool tests or imports source. Unsupported entries remain
        visible in Tools but are not offered as executable application dependencies.
        """
        from pathlib import Path

        root = Path(self.catalog.root)
        if not root.exists():
            raise CatalogDependencyError(
                "No approved tools are installed. Create and approve them in Tools first."
            )
        entries = list(root.iterdir())
        if len(entries) > 512:
            raise CatalogDependencyError("Application tool catalog exceeds its limit")
        result, skipped = self._scan(entries)
        if not result:
            detail = "; ".join(f"{name} ({reason})" for name, reason in skipped.items())
            raise CatalogDependencyError(
                "No approved portable tools with canonical Annotated contracts. "
                + (
                    f"Skipped installed tools: {detail}."
                    if detail
                    else "Create and approve compatible tools in Tools first."
                )
            )
        return result

    def _scan(self, entries: list[Path]) -> tuple[dict[str, ApprovedTool], dict[str, str]]:
        """Resolve eligible entries and collect one owner-actionable reason per skip."""
        from agentix.domain.tool_schema import extract_tool_schema

        result: dict[str, ApprovedTool] = {}
        skipped: dict[str, str] = {}
        for directory in sorted(entries):
            name = directory.name
            reason = self._skip_reason(name)
            if reason is None:
                code, tests = self.ledger.snapshot(name)
                context = self.ledger.acceptance_context(name)
                schema = extract_tool_schema(name, code.decode("utf-8"))
                result[name] = ApprovedTool(
                    name,
                    name,
                    name,
                    code,
                    tests,
                    context["contract_digest"],
                    context.get("reviewed_contract"),
                    schema,
                )
                continue
            skipped[name] = reason
            logger.debug("event=application_tool_skipped")
        return result, skipped

    def skip_reasons(self) -> dict[str, str]:
        """Return bounded per-tool ineligibility reasons without raising or executing code.

        Candidate presentation needs the cause behind an ineligible row so an owner is
        never told to approve a tool whose approval is already current. Missing or
        unreadable roots yield an empty mapping; no source bytes are included.
        """
        root = Path(self.catalog.root)
        if not root.is_dir():
            return {}
        try:
            entries = list(root.iterdir())
        except OSError:
            return {}
        if len(entries) > 512:
            return {}
        try:
            return self._scan(entries)[1]
        except (OSError, ValueError):
            return {}

    def _skip_reason(self, name: str) -> str | None:
        """Return why one installed entry is ineligible, or None when it resolves.

        Reasons are maintained owner-actionable categories only; source bytes,
        prompts and approval internals are never included. No generated source is
        imported and no tool tests are executed.
        """
        from agentix.domain.tool_schema import extract_tool_schema

        if not self.catalog.contains(name):
            return "no current reusable approval; execute and approve it in Tools first"
        store = getattr(self.ledger, "store", None)
        if store is not None:
            # Presentation is read-only: peek never revokes, so opening the catalog
            # cannot destroy an owner grant that a later reseal could recover.
            try:
                code_bytes, tests_bytes = self.ledger.snapshot(name)
            except (OSError, ValueError):
                return "no current reusable approval; execute and approve it in Tools first"
            if store.peek(name, code_bytes, tests_bytes) is None or not self.ledger.prepare_reuse(
                name
            ):
                return "no current reusable approval; execute and approve it in Tools first"
        elif not self.ledger.prepare_reuse(name):
            return "no current reusable approval; execute and approve it in Tools first"
        code, _tests = self.ledger.snapshot(name)
        context = self.ledger.acceptance_context(name)
        if not context:
            return "no current acceptance context; complete its approval in Tools first"
        if not computation_only(code):
            rejected = ", ".join(sorted(unapproved_imports(code, allowed_modules())))
            detail = f" ({rejected})" if rejected else ""
            return (
                "imports outside the portable module list"
                + detail
                + "; add them to portable_modules.json in the AgentiX data folder"
                + " (third-party packages also need installation, not yet supported)"
            )
        try:
            extract_tool_schema(name, code.decode("utf-8"))
        except (ValueError, SyntaxError):
            logger.info("event=application_contract_unavailable")
            return "no canonical Annotated contract; the single public function must have the tool name"
        covered = {signature.split("(")[0] for signature in context["approved_functions"]}
        if name not in covered:
            return "approved functions do not cover the canonical tool function"
        return None

    def recheck(self, expected: Mapping[str, ApprovedTool]) -> None:
        """Only selected dependencies must match; unrelated catalog additions are allowed."""
        current = self.resolve()
        if any(current.get(name) != tool for name, tool in expected.items()):
            raise CatalogDependencyError(
                "Selected application dependencies changed or were revoked"
            )
