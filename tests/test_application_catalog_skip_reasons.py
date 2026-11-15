"""Portable catalog skip-reason regressions; trusted temporary fixtures only."""

import hashlib
import hmac
import logging
from types import SimpleNamespace

import pytest

from agentix.controllers.application_candidates import present_candidates
from agentix.retrieval import SearchResult, descriptor_from_source
from agentix.security import SecurityManager
from agentix.security.approval_store import ApprovalStore
from agentix.security.verification import VerificationLedger
from agentix.storage.application_catalog import CatalogDependencyError, CatalogToolRegistry
from agentix.storage.catalog import ToolCatalog

CANONICAL = (
    b'"""Trusted portable fixture."""\n'
    b"from typing import Annotated\n"
    b"\n"
    b"\n"
    b'def alpha_tool(text: Annotated[str, "Text to inspect"]) -> Annotated[int, "Word count"]:\n'
    b'    """Count words in the given text."""\n'
    b"    return len(text.split())\n"
)

NON_PORTABLE = (
    b'"""Trusted non-portable fixture."""\n'
    b"from typing import Annotated\n"
    b"import os\n"
    b"\n"
    b"\n"
    b'def alpha_tool(text: Annotated[str, "Text to inspect"]) -> Annotated[int, "Word count"]:\n'
    b'    """Count words in the given text."""\n'
    b"    return len(text.split())\n"
)

WRONG_FUNCTION = (
    b'"""Trusted misnamed fixture."""\n'
    b"from typing import Annotated\n"
    b"\n"
    b"\n"
    b'def other_function(text: Annotated[str, "Text to inspect"]) -> Annotated[int, "Count"]:\n'
    b'    """Count words in the given text."""\n'
    b"    return len(text.split())\n"
)


class FixtureProtector:
    """Authenticate temporary approval records without using Windows credentials."""

    def seal(self, data: bytes) -> bytes:
        """Bind fixture bytes to a test-only key."""
        return hmac.digest(b"catalog-reuse-fixture", data, "sha256") + data

    def unseal(self, data: bytes) -> bytes:
        """Reject modified fixture bytes before decoding them."""
        if not hmac.compare_digest(
            data[:32], hmac.digest(b"catalog-reuse-fixture", data[32:], "sha256")
        ):
            raise ValueError("Invalid fixture seal")
        return data[32:]


def test_durable_approvals_populate_fresh_catalog_and_candidate_context(tmp_path):
    """Six unchanged reviewed grants become candidates without tool execution."""
    root = tmp_path / "catalog"
    root.mkdir()
    store = ApprovalStore(
        tmp_path / "approvals", root, protector=FixtureProtector(), policy="fixed-policy"
    )
    names = tuple(f"count_{index}" for index in range(6))
    sources = {}
    for name in names:
        source = CANONICAL.replace(b"alpha_tool", name.encode())
        tests = b'"""Independent provisional fixture; never executed on reuse."""\n'
        folder = root / name
        folder.mkdir()
        (folder / f"{name}_code.py").write_bytes(source)
        (folder / f"{name}_tests.py").write_bytes(tests)
        store.save(
            name,
            source,
            tests,
            "reviewed-contract",
            frozenset({name}),
            {
                "version": 1,
                "cases": [
                    {
                        "id": "count_case",
                        "purpose": "Count words",
                        "function": name,
                        "kwargs": {"text": "one two"},
                        "expect": {"kind": "value", "value": 2},
                    }
                ],
            },
        )
        sources[name] = source

    security = SecurityManager.for_owner("fresh-catalog-owner")
    security.TOOLS_ROOT_DIR = str(root)
    ledger = VerificationLedger(security, store=store)
    assert ledger.acceptance_context(names[0]) is None
    assert ledger.prepare_reuse(names[0])
    context = ledger.acceptance_context(names[0])
    assert context["contract_digest"] == "reviewed-contract"
    assert context["reviewed_contract"]["cases"][0]["function"] == names[0]
    assert any(item.startswith(f"{names[0]}(") for item in context["approved_functions"])

    registry = CatalogToolRegistry(ToolCatalog(root), ledger)
    assert registry.skip_reasons() == {}
    assert set(registry.resolve()) == set(names)
    results = []
    for name in names[:5]:
        descriptor = descriptor_from_source(name, sources[name].decode(), artifact_ref=name)
        assert descriptor.contract_digest == hashlib.sha256(sources[name]).hexdigest()
        results.append(SearchResult(descriptor, 1, 1 / 61, 0.9, 1.0, "hybrid"))
    view = present_candidates("revision", "count words", 5, results, registry)
    assert view.ready is True
    assert view.eligible_ids == frozenset(names[:5])
    assert view.message == (
        "Found 5 candidate(s) with limit 5. "
        "Accept these candidates to start application generation."
    )


def install(tmp_path, name="alpha_tool", code=CANONICAL, functions=("alpha_tool",), grant=True):
    """Publish a fixture catalog entry with an optional host-boundary reuse grant."""
    security = SecurityManager.for_owner("skip-reason-owner")
    security.TOOLS_ROOT_DIR = str(tmp_path)
    ledger = VerificationLedger(security)
    folder = tmp_path / name
    folder.mkdir()
    (folder / f"{name}_code.py").write_bytes(code)
    tests = b'"""Tests must not run on reuse."""\n'
    (folder / f"{name}_tests.py").write_bytes(tests)
    if grant:
        ledger._reuse[name] = (
            security.owner_id,
            code,
            tests,
            "reviewed-contract",
            frozenset(functions),
            {"version": 1, "cases": []},
        )
    return SimpleNamespace(ledger=ledger, catalog=ToolCatalog(tmp_path))


def test_valid_portable_tool_resolves_with_schema(tmp_path):
    """A canonical approved fixture remains eligible after the diagnostics change."""
    fixture = install(tmp_path)
    tools = CatalogToolRegistry(fixture.catalog, fixture.ledger).resolve()
    assert set(tools) == {"alpha_tool"}
    assert tools["alpha_tool"].schema["function"] == "alpha_tool"


def test_missing_reusable_approval_is_named(tmp_path):
    """An installed but unapproved tool must report its actionable skip reason."""
    fixture = install(tmp_path, grant=False)
    with pytest.raises(CatalogDependencyError, match=r"alpha_tool.*reusable approval"):
        CatalogToolRegistry(fixture.catalog, fixture.ledger).resolve()


def test_unapproved_catalog_skip_is_debug_and_payload_free(tmp_path, caplog):
    """Keep repeated eligibility decisions out of INFO logs and omit tool identity."""
    fixture = install(tmp_path, grant=False)

    with caplog.at_level(logging.INFO):
        with pytest.raises(CatalogDependencyError):
            CatalogToolRegistry(fixture.catalog, fixture.ledger).resolve()

    assert "event=application_tool_skipped" not in caplog.text
    caplog.clear()
    with caplog.at_level(logging.DEBUG):
        with pytest.raises(CatalogDependencyError):
            CatalogToolRegistry(fixture.catalog, fixture.ledger).resolve()

    assert "event=application_tool_skipped" in caplog.text
    assert "alpha_tool" not in caplog.text


def test_non_portable_source_is_named(tmp_path):
    """Computation-policy rejection must name the tool and the rejected imports."""
    fixture = install(tmp_path, code=NON_PORTABLE)
    with pytest.raises(CatalogDependencyError, match=r"alpha_tool.*portable module list \(os\)"):
        CatalogToolRegistry(fixture.catalog, fixture.ledger).resolve()


def test_non_canonical_contract_is_named(tmp_path):
    """A schema failure must name the tool and the canonical contract reason."""
    fixture = install(tmp_path, code=WRONG_FUNCTION, functions=("other_function",))
    with pytest.raises(CatalogDependencyError, match=r"alpha_tool.*canonical"):
        CatalogToolRegistry(fixture.catalog, fixture.ledger).resolve()


def test_uncovered_canonical_function_is_named(tmp_path):
    """Approval covering only another function must report the coverage gap."""
    fixture = install(tmp_path, functions=("unrelated_function",))
    with pytest.raises(CatalogDependencyError, match=r"alpha_tool.*not cover"):
        CatalogToolRegistry(fixture.catalog, fixture.ledger).resolve()
