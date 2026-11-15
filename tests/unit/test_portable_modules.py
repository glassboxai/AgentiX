"""Owner-extensible portable module list regressions; no generated content is read."""

import json

from agentix.security.reuse_policy import (
    allowed_modules,
    computation_only,
    unapproved_imports,
)

REGEX_TOOL = (
    b'"""Trusted regex fixture."""\n'
    b"import typing\n"
    b"import re\n"
    b"\n"
    b"\n"
    b'def count_words_in_text(text: typing.Annotated[str, "Input"]) -> typing.Annotated[int, "Count"]:\n'
    b'    """Count words using a whitespace regex."""\n'
    b'    return len([word for word in re.split(r"\\s+", text.strip()) if word])\n'
)


def test_default_list_fails_closed_without_config(tmp_path):
    """A missing config keeps the maintained default, including re."""
    modules = allowed_modules(tmp_path / "portable_modules.json")
    assert {"typing", "math", "re", "json", "collections"} <= modules
    assert "os" not in modules


def test_valid_config_replaces_default_but_always_keeps_typing(tmp_path):
    """The owner list takes full control; typing remains forced for Annotated contracts."""
    config = tmp_path / "portable_modules.json"
    config.write_text(json.dumps({"allowed_modules": ["re"]}), encoding="utf-8")
    modules = allowed_modules(config)
    assert modules == {"re", "typing"}


def test_corrupt_config_falls_back_to_default(tmp_path):
    """Unreadable or malformed JSON never widens or empties the effective list."""
    config = tmp_path / "portable_modules.json"
    config.write_bytes(b"not json {")
    assert allowed_modules(config) == allowed_modules(tmp_path / "missing.json")


def test_invalid_entries_fall_back_to_default(tmp_path):
    """Non-identifier or uppercase module names reject the whole file."""
    config = tmp_path / "portable_modules.json"
    config.write_text(json.dumps({"allowed_modules": ["re", "OS", 3]}), encoding="utf-8")
    assert "re" in allowed_modules(config) and "statistics" in allowed_modules(config)


def test_unapproved_imports_names_each_unlisted_module(tmp_path):
    """Diagnostics surface the exact rejected imports for the owner message."""
    modules = allowed_modules(tmp_path / "missing.json")
    assert unapproved_imports(b"import os\nimport re\nfrom pathlib import Path\n", modules) == {
        "os",
        "pathlib",
    }


def test_computation_only_accepts_owner_extended_list(tmp_path):
    """The real count_words_in_text source passes once re is owner-approved."""
    assert not computation_only(REGEX_TOOL, modules=frozenset({"typing"}))
    assert computation_only(REGEX_TOOL, modules=frozenset({"typing", "re"}))
    assert computation_only(REGEX_TOOL, modules=allowed_modules(tmp_path / "missing.json"))
