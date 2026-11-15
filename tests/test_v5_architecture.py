"""Canonical imports are the only supported internal import paths.

The retired compatibility layer is recorded here as a frozen contract so that a
reintroduced ``sys.modules[__name__]`` alias or a legacy import path fails the
offline suite instead of silently returning.
"""

import ast
import importlib
import subprocess
import sys
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "src" / "agentix"

RETIRED_LEGACY_MODULES = (
    "agentix.acceptance",
    "agentix.app_invocation",
    "agentix.application_agents",
    "agentix.application_catalog",
    "agentix.application_controls",
    "agentix.application_pipeline",
    "agentix.application_review",
    "agentix.approval_store",
    "agentix.approvals",
    "agentix.catalog",
    "agentix.contracts",
    "agentix.credentials",
    "agentix.data_protection",
    "agentix.installed_apps",
    "agentix.model_profiles",
    "agentix.orchestration",
    "agentix.paths",
    "agentix.profile_errors",
    "agentix.profile_store",
    "agentix.reuse_policy",
    "agentix.storage",
    "agentix.ui.activity",
    "agentix.ui.applications_backend",
    "agentix.ui.applications_frontend",
    "agentix.ui.controller",
    "agentix.ui.session_access",
    "agentix.ui.sessions",
    "agentix.ui.sidebar_backend",
    "agentix.ui.sidebar_frontend",
    "agentix.ui.state",
    "agentix.ui.tools_backend",
    "agentix.ui.tools_frontend",
    "agentix.verification",
    "agentix.widget_store",
    "agentix.windows_process",
    "agentix.workflow_policy",
)


def maintained_sources():
    """Yield every maintained module under the source package, skipping bytecode."""
    for path in sorted(SOURCE.rglob("*.py")):
        if "__pycache__" not in path.parts:
            yield path


@pytest.mark.parametrize(
    "module,symbol",
    [
        ("agentix.controllers.applications", "ApplicationsBackend"),
        ("agentix.controllers.sidebar", "SidebarBackend"),
        ("agentix.controllers.tools", "ToolsBackend"),
        ("agentix.controllers.tool_controller", "format_thoughts_markdown"),
        ("agentix.application.tool_workflow", "Orchestrator"),
        ("agentix.security.paths", "SecurityViolationError"),
        ("agentix.storage.artifacts", "ArtifactStore"),
        ("agentix.domain.contracts", "ExecutionBackend"),
    ],
)
def test_canonical_modules_expose_their_public_symbols(module, symbol):
    """Each responsibility package must be importable and expose its public contract."""
    imported = importlib.import_module(module)
    assert sys.modules[module] is imported
    assert hasattr(imported, symbol)


def test_no_legacy_sys_modules_alias_assignment_remains():
    """A compatibility alias is an assignment to ``sys.modules[__name__]``."""
    offenders = []
    for path in maintained_sources():
        tree = ast.parse(path.read_text(encoding="utf-8"), filename=str(path))
        for node in ast.walk(tree):
            targets = node.targets if isinstance(node, ast.Assign) else []
            for target in targets:
                if not isinstance(target, ast.Subscript):
                    continue
                value = target.value
                if (
                    isinstance(value, ast.Attribute)
                    and value.attr == "modules"
                    and isinstance(value.value, ast.Name)
                    and value.value.id == "sys"
                    and isinstance(target.slice, ast.Name)
                    and target.slice.id == "__name__"
                ):
                    offenders.append(f"{path.relative_to(ROOT)}:{node.lineno}")
    assert offenders == []


def test_no_maintained_module_imports_a_retired_legacy_path():
    """Retired paths must not return through a static import in maintained source."""
    retired = set(RETIRED_LEGACY_MODULES)
    offenders = []
    for path in maintained_sources():
        tree = ast.parse(path.read_text(encoding="utf-8"), filename=str(path))
        for node in ast.walk(tree):
            names = []
            if isinstance(node, ast.Import):
                names = [alias.name for alias in node.names]
            elif isinstance(node, ast.ImportFrom) and node.module and not node.level:
                names = [node.module] + [f"{node.module}.{alias.name}" for alias in node.names]
            for name in names:
                if name in retired:
                    offenders.append(f"{path.relative_to(ROOT)}:{node.lineno}:{name}")
    assert offenders == []


def test_canonical_storage_package_is_not_shadowed_by_a_compatibility_alias():
    """The storage package must resolve to its package, never to a legacy alias module."""
    package = importlib.import_module("agentix.storage")
    artifacts = importlib.import_module("agentix.storage.artifacts")
    assert package.__file__.replace("\\", "/").endswith("agentix/storage/__init__.py")
    assert package.__path__
    assert package is not artifacts
    assert artifacts.ArtifactStore is not None


@pytest.mark.parametrize(
    "order",
    [
        ("agentix.security", "agentix.storage", "agentix.storage.artifacts"),
        ("agentix.storage", "agentix.security", "agentix.storage.artifacts"),
    ],
)
def test_security_and_storage_import_without_circular_failure(order):
    """Either import order must finish; a partially initialized module raises ImportError."""
    script = (
        "import _agentix_path\n"
        + "".join(f"import {name}\n" for name in order)
        + "import agentix.storage\n"
        + "assert agentix.storage.__path__, 'storage resolved to a module, not a package'\n"
        + "print('ok')\n"
    )
    result = subprocess.run(
        [sys.executable, "-c", script], cwd=ROOT, capture_output=True, text=True, timeout=60
    )
    assert result.returncode == 0, result.stderr
    assert result.stdout.strip() == "ok"
