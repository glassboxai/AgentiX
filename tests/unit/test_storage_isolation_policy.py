"""v7 storage isolation: explicit configuration, no v5 fallback, no v5 namespace.

Every path here is a pytest temporary directory. The tests resolve configuration
only; they never create, publish, approve or migrate persistent artifacts.
"""

import subprocess
import sys
from pathlib import Path

import pytest

from agentix.settings import Settings
from agentix.storage.locations import data_directory, require_v7_namespace, user_home

ROOT = Path(__file__).resolve().parents[2]


def test_missing_home_fails_with_actionable_error():
    """No legacy profile is substituted when AGENTIX_HOME is absent."""
    with pytest.raises(ValueError, match="AGENTIX_HOME must name the AgentiX v7 data root"):
        user_home({})
    with pytest.raises(ValueError, match="AGENTIX_HOME"):
        data_directory({})


def test_missing_tools_root_fails_with_actionable_error(tmp_path):
    """The published Tools root is never derived from a default home."""
    with pytest.raises(ValueError, match="AGENTIX_TOOLS_ROOT must name the published Tools"):
        Settings.from_environment({"AGENTIX_HOME": str(tmp_path / "home")}, base_dir=tmp_path)


@pytest.mark.parametrize(
    "legacy",
    [
        "C:/Users/example/AppData/Local/AgentiX/v5",
        "C:/Users/example/AppData/Local/AgentiX/v5/data",
        "D:/AI/Agentix-data/v5",
        "D:/AI/Agentix-data/v5/data/drafts",
    ],
)
def test_legacy_v5_roots_are_rejected(legacy):
    """Resolved legacy namespaces fail closed before any storage access."""
    with pytest.raises(ValueError, match="retired AgentiX v5 storage namespace"):
        require_v7_namespace(Path(legacy), "AGENTIX_HOME")


@pytest.mark.parametrize(
    "allowed",
    [
        "D:/AI/Agentix-data/v7",
        "D:/AI/Agentix-data/v7/data",
        "D:/AI/AgentiX_v7/generated_tools",
        "C:/work/v5-migration-notes",
        "C:/work/project/v5",
    ],
)
def test_unrelated_v5_substrings_are_accepted(allowed):
    """Only whole legacy path segments are rejected, not incidental substrings."""
    assert require_v7_namespace(Path(allowed), "path") == Path(allowed).resolve()


def test_configured_v7_paths_resolve_as_established(tmp_path):
    """The IaC variables resolve to the established v7 layout."""
    home = tmp_path / "Agentix-data" / "v7"
    tools = tmp_path / "AgentiX_v7" / "generated_tools"
    settings = Settings.from_environment(
        {"AGENTIX_HOME": str(home), "AGENTIX_TOOLS_ROOT": str(tools)}, base_dir=tmp_path
    )
    assert settings.tools_root == tools
    assert settings.data_root == home / "data"
    assert (settings.data_root or settings.tools_root.parent) / "drafts" == home / "data" / "drafts"


def test_legacy_home_is_rejected_by_settings(tmp_path):
    """A v5 AGENTIX_HOME cannot configure a v7 runtime."""
    with pytest.raises(ValueError, match="retired AgentiX v5 storage namespace"):
        Settings.from_environment(
            {
                "AGENTIX_HOME": str(tmp_path / "AgentiX" / "v5"),
                "AGENTIX_TOOLS_ROOT": str(tmp_path / "tools"),
            },
            base_dir=tmp_path,
        )


def test_legacy_tools_root_is_rejected_by_settings(tmp_path):
    """A v5 published Tools root cannot be configured."""
    with pytest.raises(ValueError, match="retired AgentiX v5 storage namespace"):
        Settings.from_environment(
            {
                "AGENTIX_HOME": str(tmp_path / "Agentix-data" / "v7"),
                "AGENTIX_TOOLS_ROOT": str(tmp_path / "Agentix-data" / "v5" / "data" / "tools"),
            },
            base_dir=tmp_path,
        )


def test_runtime_rejects_legacy_roots_from_direct_settings(tmp_path):
    """Direct Settings construction cannot bypass the namespace guard."""
    from agentix.bootstrap import create_runtime

    with pytest.raises(ValueError, match="retired AgentiX v5 storage namespace"):
        create_runtime(
            Settings(
                tmp_path,
                tmp_path / "Agentix-data" / "v5" / "data" / "tools",
                data_root=tmp_path / "Agentix-data" / "v7" / "data",
            ),
            llm=object(),
            tool_factory=lambda operations: object(),
            agent_factory=lambda model, tools: object(),
            backend=object(),
        )


def test_default_security_manager_resolves_configured_tools_root(tmp_path, monkeypatch):
    """An unconfigured coordinator resolves AGENTIX_TOOLS_ROOT lazily."""
    from agentix.security import SecurityManager

    tools = tmp_path / "generated_tools"
    monkeypatch.setenv("AGENTIX_HOME", str(tmp_path / "home"))
    monkeypatch.setenv("AGENTIX_TOOLS_ROOT", str(tools))
    unconfigured = type("UnconfiguredSecurity", (SecurityManager,), {"TOOLS_ROOT_DIR": ""})
    assert unconfigured._tools_root() == str(tools)


def test_default_security_manager_fails_closed_without_configuration(monkeypatch):
    """An unconfigured coordinator raises instead of adopting any fallback root."""
    from agentix.security import SecurityManager

    monkeypatch.delenv("AGENTIX_HOME", raising=False)
    monkeypatch.delenv("AGENTIX_TOOLS_ROOT", raising=False)
    unconfigured = type("UnconfiguredSecurity", (SecurityManager,), {"TOOLS_ROOT_DIR": ""})
    with pytest.raises(ValueError, match="AGENTIX_HOME"):
        unconfigured._tools_root()


def test_import_without_configuration_stays_inert(tmp_path):
    """Importing the package must not require deployment configuration."""
    environment = {
        key: value
        for key, value in __import__("os").environ.items()
        if key not in ("AGENTIX_HOME", "AGENTIX_TOOLS_ROOT")
    }
    environment["PYTHONDONTWRITEBYTECODE"] = "1"
    result = subprocess.run(
        [
            sys.executable,
            "-c",
            "import _agentix_path, agentix.security, agentix.settings; print('inert')",
        ],
        cwd=ROOT,
        capture_output=True,
        text=True,
        timeout=60,
        env=environment,
    )
    assert result.returncode == 0, result.stderr
    assert result.stdout.strip() == "inert"
