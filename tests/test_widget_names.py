"""LAB-004 canonical package filenames must be executable and review-bound."""

import json
from pathlib import Path

import pytest

from agentix.lab.widget_artifacts import CONTRACT, approve_package, package_digest


def test_review_loads_canonical_named_widget(tmp_path):
    """Catch loaders still looking for the literal tool_widget.py placeholder."""
    (tmp_path / "count_vowels_in_text_widget.py").write_bytes(
        Path("src/agentix/lab/reference_widget.py").read_bytes()
    )
    (tmp_path / "count_vowels_in_text_code.py").write_bytes(
        Path("src/agentix/lab/fixture_tools.py").read_bytes()
    )
    (tmp_path / "tool_definition.json").write_text(json.dumps(CONTRACT))
    approved = approve_package(tmp_path, package_digest(tmp_path))
    assert b"create_widget" in approved.widget


def test_generic_filename_is_not_accepted_as_active_package(tmp_path):
    """Prevent silently using an obsolete placeholder after the naming correction."""
    (tmp_path / "tool_widget.py").write_bytes(
        Path("src/agentix/lab/reference_widget.py").read_bytes()
    )
    (tmp_path / "tool_code.py").write_bytes(Path("src/agentix/lab/fixture_tools.py").read_bytes())
    with pytest.raises((ValueError, FileNotFoundError)):
        package_digest(tmp_path)


def test_designer_writes_canonical_artifacts_without_executing_proposals(tmp_path, monkeypatch):
    """Exercise real generation storage/parser using only a deterministic network double."""
    import io

    from agentix.lab import widget_designer

    candidate = {
        "widget_code": Path("src/agentix/lab/reference_widget.py").read_text(encoding="utf-8"),
        "tests_code": 'raise AssertionError("Do not run proposed tests on the host")\n',
        "notes": "Fixture response, not real model evidence.",
    }
    raw = json.dumps({"message": {"content": json.dumps(candidate)}}).encode()

    class Opener:
        """Substitute only the local model boundary, preserving actual file behavior."""

        def open(self, request, timeout):
            return io.BytesIO(raw)

    monkeypatch.setattr(widget_designer, "build_opener", lambda *args: Opener())
    folder = tmp_path / "new package with spaces"
    digest = widget_designer.generate_widget(folder)
    assert (folder / "count_vowels_in_text_widget.py").read_bytes() == candidate[
        "widget_code"
    ].encode()
    assert (folder / "count_vowels_in_text_code.py").is_file()
    assert (folder / "count_vowels_in_text_widget_tests.py").read_text() == candidate["tests_code"]
    assert not (folder / "tool_widget.py").exists()
    assert digest == package_digest(folder)
