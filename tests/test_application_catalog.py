"""Approved catalog dependency regressions; use trusted temporary source only."""

from types import SimpleNamespace

import pytest

from agentix.security import SecurityManager
from agentix.security.verification import VerificationLedger
from agentix.storage.catalog import ToolCatalog

SOURCES = {
    "count_words_in_text": b'"""Trusted words fixture."""\nfrom typing import Annotated\n\n\ndef count_words_in_text(text: Annotated[str, "Text to inspect"]) -> Annotated[int, "Word count"]:\n    """Count words in the given text."""\n    return len(text.split())\n',
    "count_vowels_in_text": b'"""Trusted vowels fixture."""\nfrom typing import Annotated\n\n\ndef count_vowels_in_text(text: Annotated[str, "Text to inspect"]) -> Annotated[int, "Vowel count"]:\n    """Count vowels in the given text."""\n    return sum(c in "aeiouAEIOU" for c in text)\n',
}


def installed(tmp_path, owner_id="catalog-owner"):
    """Publish explicit host-boundary fixture grants, without model/test execution."""
    security = SecurityManager.for_owner(owner_id)
    security.TOOLS_ROOT_DIR = str(tmp_path)
    ledger = VerificationLedger(security)
    for name, code in SOURCES.items():
        folder = tmp_path / name
        folder.mkdir()
        (folder / f"{name}_code.py").write_bytes(code)
        (folder / f"{name}_tests.py").write_bytes(b'"""Tests must not run on reuse."""\n')
        function = name
        ledger._reuse[name] = (
            security.owner_id,
            code,
            (folder / f"{name}_tests.py").read_bytes(),
            "reviewed-contract",
            frozenset({function}),
            {
                "version": 1,
                "cases": [
                    {
                        "id": "fixture",
                        "purpose": "Known fixture text",
                        "function": function,
                        "kwargs": {"text": "Hello World!"},
                        "expect": {"kind": "value", "value": 2},
                    }
                ],
            },
        )
    return SimpleNamespace(ledger=ledger, catalog=ToolCatalog(tmp_path))


def registry(fixture):
    """Resolve the production registry only after the test module can collect."""
    from agentix.storage.application_catalog import ApprovedToolRegistry

    return ApprovedToolRegistry(fixture.catalog, fixture.ledger)


def test_exact_installed_approved_bytes_are_reused_without_running_tests(tmp_path):
    """Catch substitution of internal examples for installed source or test execution."""
    fixture = installed(tmp_path)
    tools = registry(fixture).resolve()
    assert set(tools) == set(SOURCES)
    assert tools["count_words_in_text"].code == SOURCES["count_words_in_text"]
    assert tools["count_words_in_text"].function == "count_words_in_text"
    assert tools["count_words_in_text"].schema["function"] == "count_words_in_text"
    registry(fixture).recheck(tools)


@pytest.mark.parametrize("failure", ["missing", "unapproved", "changed", "foreign_catalog"])
def test_missing_unapproved_drifted_or_foreign_catalog_tool_is_rejected(tmp_path, failure):
    """Both catalog membership and a current owner-bound approval are mandatory."""
    fixture = installed(tmp_path)
    name = "count_words_in_text"
    if failure == "missing":
        (tmp_path / name / f"{name}_code.py").unlink()
    elif failure == "unapproved":
        fixture.ledger._reuse.pop(name)
    elif failure == "changed":
        (tmp_path / name / f"{name}_code.py").write_bytes(b"def count_words(text): return 999")
    else:
        fixture.catalog = ToolCatalog(tmp_path / "other-catalog")
    with pytest.raises(ValueError, match="catalog|approv|changed"):
        registry(fixture).resolve()


def test_recheck_detects_revocation_after_packaging(tmp_path):
    """A package snapshot alone must not retain a revoked installed-tool grant."""
    fixture = installed(tmp_path)
    service = registry(fixture)
    tools = service.resolve()
    fixture.ledger._reuse.clear()
    fixture.ledger._acceptance.clear()
    with pytest.raises(ValueError):
        service.recheck(tools)


def test_pipeline_never_uses_internal_tools_when_no_approved_catalog_is_supplied(tmp_path):
    """Reject before inference rather than silently using a fixed example package."""
    from agentix.application.app_workflow import ApplicationPipeline

    calls = []
    pipeline = ApplicationPipeline(tmp_path, lambda folder: calls.append(folder))
    with pytest.raises(ValueError, match="approved|catalog"):
        pipeline.generate("Count words and vowels")
    assert not calls
