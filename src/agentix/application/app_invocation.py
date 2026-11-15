"""Catalog-only application invocation with exact current tool approvals and native data."""

import hashlib
import json
from typing import Any

from agentix.lab.application_artifacts import approve_application, validate_result
from agentix.lab.application_session import execute_application
from agentix.storage.application_catalog import ApprovedToolRegistry, CatalogDependencyError
from agentix.storage.installed_apps import InstalledApp, InstalledApps


def check_dependencies(app: InstalledApp, registry: ApprovedToolRegistry) -> dict:
    """Require the approved installed tool versions used by this exact app snapshot.

    A missing tool is reported as ``CatalogDependencyError`` naming the tool and
    the maintained skip reason, so the owner sees the recovery step instead of a
    generic review message. Reasons never include source, prompts or approval
    internals.
    """
    tools = registry.resolve()
    missing = [name for name in app.dependencies if name not in tools]
    if missing:
        reason_of = getattr(registry, "_skip_reason", None)
        detail = "; ".join(
            f"{name} ({reason_of(name) or 'no current reusable approval'})" for name in missing
        )
        raise CatalogDependencyError(
            "Application dependencies require current tool approvals. "
            f"Skipped installed tools: {detail}."
        )
    for role, expected in app.dependencies.items():
        tool = tools[role]
        if (
            expected.get("tool_name") != tool.tool_name
            or expected.get("function") != tool.function
            or expected.get("contract_digest") != tool.contract_digest
            or expected.get("code_sha256") != hashlib.sha256(tool.code).hexdigest()
            or expected.get("tests_sha256") != hashlib.sha256(tool.tests).hexdigest()
        ):
            raise ValueError("An installed application tool or its approval changed")
    return {name: tools[name] for name in app.dependencies}


def rebind_dependencies(app: InstalledApp, registry: ApprovedToolRegistry) -> dict:
    """Re-derive tool digests for unchanged role and function identities.

    Only the approved bytes and contract digest may move; a renamed tool or a
    changed function identity still requires a new application review.
    """
    tools = registry.resolve()
    rebound = {}
    for role, expected in app.dependencies.items():
        tool = tools.get(role)
        if tool is None:
            raise ValueError("Application dependencies require fresh review")
        if expected.get("tool_name") != tool.tool_name or expected.get("function") != tool.function:
            raise ValueError("Application dependencies require fresh review")
        rebound[role] = {
            **expected,
            "contract_digest": tool.contract_digest,
            "code_sha256": hashlib.sha256(tool.code).hexdigest(),
            "tests_sha256": hashlib.sha256(tool.tests).hexdigest(),
        }
    return rebound


class AppInvocation:
    """Inject library, owner registry and OS boundary; expose no arbitrary file entrypoint."""

    def __init__(
        self,
        library: InstalledApps,
        registry: ApprovedToolRegistry,
        *,
        native: Any = execute_application,
    ) -> None:
        """Construct an inert per-owner invocation service without reading artifacts."""
        self.library, self.registry, self.native = library, registry, native

    def catalog(self) -> list[dict]:
        """Return safe metadata for approved compatible apps, never source or keys."""
        result = []
        for app in self.library.list():
            try:
                check_dependencies(app, self.registry)
            except (OSError, ValueError):
                continue
            result.append(
                {
                    "id": app.id,
                    "name": app.name,
                    "description": app.description,
                    "input": self._input_contract(app),
                    "output": json.loads((app.package / "application.json").read_bytes()).get(
                        "tools", {"words": "integer", "vowels": "integer"}
                    ),
                }
            )
        return result[:32]

    def candidates(self) -> list[dict]:
        """Return minimal approved metadata for a suggestion prompt.

        Only the current catalog identity, display name and description are
        exposed. Input contracts, node IDs, parameter names, arguments, source and
        results stay host-side, so a recommendation cannot leak or rebuild them.
        """
        result = []
        for app in self.library.list():
            try:
                check_dependencies(app, self.registry)
            except (OSError, ValueError):
                continue
            result.append({"id": app.id, "name": app.name, "description": app.description})
        return result[:32]

    @staticmethod
    def _input_contract(app: InstalledApp) -> dict:
        """Describe only the schema-3 public inputs to the model selector."""
        manifest = json.loads((app.package / "application.json").read_bytes())
        return manifest["inputs"]

    def execute(self, identity: str, arguments: dict) -> dict:
        """Hold a cross-process usage lease for the entire native data operation."""
        with self.library.open_lease(identity):
            return self._execute(identity, arguments)

    def _execute(self, identity: str, arguments: dict) -> dict:
        """Recheck catalog/source/tool grants before and after isolated execution."""
        app = self.library.get(identity)
        manifest = json.loads((app.package / "application.json").read_bytes())
        if manifest.get("schema_version") == 3:
            from agentix.application.general_package import validate_payload

            arguments = validate_payload(arguments, manifest)
        elif (
            not isinstance(arguments, dict)
            or set(arguments) != {"text"}
            or not isinstance(arguments["text"], str)
            or len(arguments["text"]) > 16000
        ):
            raise ValueError("Application requires one text input")
        check_dependencies(app, self.registry)
        snapshot = approve_application(app.package, app.digest)
        result = validate_result(self.native(snapshot, arguments), manifest)
        current = self.library.get(identity)
        if current.digest != app.digest:
            raise ValueError("Application changed during execution")
        check_dependencies(current, self.registry)
        return result

    def observed_answer(self, identity: str, arguments: dict) -> str:
        """Format only the observed native result; model prose cannot substitute it."""
        result = self.execute(identity, arguments)
        return f"Host-observed execution: application.{identity}\nArguments: {json.dumps(arguments, ensure_ascii=True)}\nResult: {result!r}"
