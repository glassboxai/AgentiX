"""Storage roots are owned by the exact coordinator class that configured them.

``SecurityManager`` keeps tool roots in mutable class attributes. A subclass that
only overrides ``TOOLS_ROOT_DIR`` must never inherit a base-class runtime
configuration, otherwise its drafts or publication land in another owner's
catalog. Every path here is a pytest temporary directory.
"""

import os
import subprocess
import sys
import threading
from pathlib import Path

import pytest

from agentix.security import SecurityManager

ROOT = Path(__file__).resolve().parents[2]


def coordinator(base, tools_root: Path, **attributes):
    """Build one isolated coordinator subclass with an explicit tool root."""
    return type(
        "IsolatedSecurity",
        (base,),
        {
            "TOOLS_ROOT_DIR": str(tools_root),
            "auto_approve": True,
            "_approval_event": threading.Event(),
            "_lock": threading.Lock(),
            "_pending_request": None,
            "_edited_content": None,
            "_approval_decision": False,
            **attributes,
        },
    )


def stage(security, tool_name: str = "adder") -> Path:
    """Write the three reviewed members and return the staged tool directory."""
    security.begin_tool_draft(tool_name)
    for suffix, content in (
        ("specifications.md", "Approved specification"),
        ("code.py", f"def {tool_name}(value): return value"),
        ("tests.py", "import unittest\n"),
    ):
        assert security.safe_write_file(tool_name, f"{tool_name}_{suffix}", content).startswith(
            "Success:"
        )
    return Path(security.TOOLS_ROOT_DIR) / tool_name


@pytest.fixture
def base_configured(tmp_path):
    """Configure the base class exactly as a runtime would, then restore it."""
    published = tmp_path / "base" / "tools"
    drafts = tmp_path / "base" / "drafts"
    original = (
        SecurityManager.TOOLS_ROOT_DIR,
        SecurityManager.PUBLISHED_TOOLS_ROOT_DIR,
        SecurityManager.DRAFTS_ROOT_DIR,
        SecurityManager._active_draft_root,
    )
    SecurityManager.configure_tool_storage(published, drafts)
    try:
        yield published, drafts
    finally:
        (
            SecurityManager.TOOLS_ROOT_DIR,
            SecurityManager.PUBLISHED_TOOLS_ROOT_DIR,
            SecurityManager.DRAFTS_ROOT_DIR,
            SecurityManager._active_draft_root,
        ) = original


def test_subclass_ignores_base_roots_for_draft_and_publication(base_configured, tmp_path):
    """A subclass with only its own tool root stages and publishes inside it."""
    base_published, _ = base_configured
    public = tmp_path / "isolated" / "tools"
    security = coordinator(SecurityManager, public)

    staged = stage(security)
    assert staged.is_relative_to(tmp_path / "isolated")
    assert not staged.is_relative_to(base_published)

    security.publish_current_draft("adder")

    assert (public / "adder" / "adder_code.py").is_file()
    assert security.TOOLS_ROOT_DIR == str(public)
    assert not (base_published / "adder").exists()


def test_restore_does_not_replace_subclass_root_with_inherited_base_path(base_configured, tmp_path):
    """Restoration must not adopt a base-class published root."""
    base_published, _ = base_configured
    public = tmp_path / "isolated" / "tools"
    security = coordinator(SecurityManager, public)

    security.restore_public_tool_storage()

    assert security.TOOLS_ROOT_DIR == str(public)
    assert security.TOOLS_ROOT_DIR != str(base_published)


def test_publication_without_an_owned_draft_fails_closed(base_configured, tmp_path):
    """An inherited active draft cannot authorize publication in a subclass."""
    security = coordinator(SecurityManager, tmp_path / "isolated" / "tools")
    SecurityManager._active_draft_root = str(tmp_path / "base" / "drafts" / "legacy" / "legacy")

    with pytest.raises(ValueError, match="No active draft"):
        security.publish_current_draft("adder")


def test_independent_coordinators_keep_independent_roots(base_configured, tmp_path):
    """Two coordinators configured separately never share a catalog."""
    first = coordinator(SecurityManager, tmp_path / "first" / "tools")
    second = coordinator(SecurityManager, tmp_path / "second" / "tools")
    first.configure_tool_storage(tmp_path / "first" / "tools", tmp_path / "first" / "drafts")
    second.configure_tool_storage(tmp_path / "second" / "tools", tmp_path / "second" / "drafts")

    stage(first, "adder")
    stage(second, "adder")
    first.publish_current_draft("adder")
    second.publish_current_draft("adder")

    assert (tmp_path / "first" / "tools" / "adder" / "adder_code.py").is_file()
    assert (tmp_path / "second" / "tools" / "adder" / "adder_code.py").is_file()
    assert first.TOOLS_ROOT_DIR == str(tmp_path / "first" / "tools")
    assert second.TOOLS_ROOT_DIR == str(tmp_path / "second" / "tools")


def test_publication_still_refuses_to_overwrite_an_existing_tool(base_configured, tmp_path):
    """Fail-closed overwrite protection is unchanged by the ownership fix."""
    public = tmp_path / "isolated" / "tools"
    security = coordinator(SecurityManager, public)
    existing = public / "adder"
    existing.mkdir(parents=True)
    original = existing / "adder_code.py"
    original.write_bytes(b"approved bytes")

    stage(security)
    with pytest.raises(ValueError, match="already exists"):
        security.publish_current_draft("adder")

    assert original.read_bytes() == b"approved bytes"


def test_compatibility_then_creation_stage_order_stays_isolated(tmp_path):
    """The reported order must pass without writing to the configured base root."""
    home = tmp_path / "home"
    environment = dict(os.environ, AGENTIX_HOME=str(home), PYTHONDONTWRITEBYTECODE="1")
    environment.pop("AGENTIX_TOOLS_ROOT", None)
    result = subprocess.run(
        [
            sys.executable,
            "-m",
            "pytest",
            "tests/unit/test_compatibility.py",
            "tests/unit/test_creation_stage_gates.py",
            "-q",
            "-p",
            "no:cacheprovider",
        ],
        cwd=ROOT,
        capture_output=True,
        text=True,
        timeout=300,
        env=environment,
    )
    assert result.returncode == 0, result.stdout[-4000:] + result.stderr[-2000:]
    assert not (home / "data" / "tools" / "adder").exists()
