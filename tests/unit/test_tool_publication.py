"""Approved tool publication keeps provisional bytes outside the public catalog."""

from pathlib import Path

import pytest


def test_draft_bytes_publish_only_to_an_empty_public_tool_directory(system, tmp_path) -> None:
    """Publish exact reviewed members without exposing a draft in the public catalog."""
    public_root = system.root
    drafts_root = tmp_path / "drafts"
    system.security.configure_tool_storage(public_root, drafts_root)
    system.security.operation_id = "operation-1"
    system.security.auto_approve = True

    system.security.begin_tool_draft("adder")
    for suffix, content in (
        ("specifications.md", "Approved specification"),
        ("code.py", '"""Trusted tool."""\ndef adder(value): return value'),
        ("tests.py", "import unittest\n"),
    ):
        assert system.security.safe_write_file("adder", "adder_" + suffix, content).startswith(
            "Success:"
        )

    assert not (public_root / "adder").exists()
    staged = Path(system.security.TOOLS_ROOT_DIR) / "adder"
    system.security.publish_current_draft("adder")

    assert system.security.TOOLS_ROOT_DIR == str(public_root)
    assert (public_root / "adder" / "adder_code.py").read_bytes() == (
        staged / "adder_code.py"
    ).read_bytes()


def test_publication_never_overwrites_an_existing_tool(system, tmp_path) -> None:
    """A staged proposal cannot replace a public tool with the same identity."""
    public_root = system.root
    drafts_root = tmp_path / "drafts"
    system.security.configure_tool_storage(public_root, drafts_root)
    existing = public_root / "adder"
    existing.mkdir(parents=True)
    original = existing / "adder_code.py"
    original.write_bytes(b"approved bytes")
    system.security.operation_id = "operation-2"
    system.security.auto_approve = True
    system.security.begin_tool_draft("adder")
    for suffix, content in (
        ("specifications.md", "Draft specification"),
        ("code.py", "draft bytes"),
        ("tests.py", "draft tests"),
    ):
        system.security.safe_write_file("adder", "adder_" + suffix, content)

    with pytest.raises(ValueError, match="already exists"):
        system.security.publish_current_draft("adder")

    assert original.read_bytes() == b"approved bytes"
