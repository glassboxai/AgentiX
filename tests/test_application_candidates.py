"""RAG-010: candidate acceptance gates application generation and remains owner-bound."""

import hashlib
import logging
from collections.abc import Iterator
from dataclasses import replace
from pathlib import Path
from types import SimpleNamespace
from typing import Any

import pytest
from test_application_crews import approved_tool
from test_applications_backend import registry

from agentix.controllers.application_candidates import AcceptedCandidates, SelectedToolRegistry
from agentix.controllers.applications import ApplicationsBackend
from agentix.retrieval import SearchResult, descriptor_from_source
from agentix.retrieval.gui import GuiToolRetrieval, RetrieverHandle
from agentix.storage.catalog import ToolCatalog


def match() -> SearchResult:
    """Build a candidate from independently authored trusted source, never importing it."""
    tool = approved_tool()
    descriptor = descriptor_from_source("calculator", tool.code.decode(), artifact_ref="calculator")
    return SearchResult(descriptor, 1, 1 / 61, 0.9, 1.0, "hybrid")


class RetrievalDouble:
    """Capture owner-specific searches without model or persistence access."""

    startup_message = "Fixture index ready."

    def __init__(self) -> None:
        """Record each query and requested result limit."""
        self.calls: list[tuple[str, int]] = []

    def search(
        self, catalog: ToolCatalog, handle: RetrieverHandle, query: str, limit: int
    ) -> list[SearchResult]:
        """Return one stable candidate over the injected local-model boundary."""
        self.calls.append((query, limit))
        return [match()]


def setup_backend(
    tmp_path: Path,
) -> tuple[ApplicationsBackend, Any, SimpleNamespace, dict[str, Any], RetrievalDouble]:
    """Compose the real application backend with independent tool and retrieval doubles."""
    sessions = registry()
    owner = sessions.resolve(None, "alice")
    owner.controller.security = SimpleNamespace(get_pending_request=lambda: None)
    catalog = ToolCatalog(tmp_path)
    owner.controller.get_installed_tools_catalog = catalog.render
    tools = {
        "calculator": approved_tool(),
        "unrelated": replace(approved_tool(), tool_name="unrelated"),
    }
    retrieval = RetrievalDouble()
    backend = ApplicationsBackend(
        sessions,
        retrieval=retrieval,
        registry_factory=lambda controller: SimpleNamespace(resolve=lambda: tools),
        library_factory=lambda: SimpleNamespace(name_available=lambda name: True),
    )
    return backend, owner, SimpleNamespace(session_hash="alice"), tools, retrieval


def test_selected_registry_supplies_exact_subset_and_rechecks() -> None:
    """Unrelated installed tools cannot enter accepted generation dependencies."""
    tool = approved_tool()
    values = {"calculator": tool, "unrelated": replace(tool, tool_name="unrelated")}
    selected = SelectedToolRegistry(
        SimpleNamespace(resolve=lambda: values),
        {"calculator": hashlib.sha256(tool.code).hexdigest()},
    )
    assert selected.resolve() == {"calculator": tool}
    selected.recheck({"calculator": tool})
    values["calculator"] = replace(tool, code=tool.code + b"\n# changed")
    with pytest.raises(ValueError):
        selected.resolve()


def test_search_does_not_generate_and_limit_is_forwarded(tmp_path: Path) -> None:
    """Generate application first requests candidates; changing limit searches again."""
    backend, owner, request, tools, retrieval = setup_backend(tmp_path)
    view, token = backend.request_candidates("PRIVATE_QUERY", 5, owner.token, request)
    assert view.ready and view.results[0].descriptor.name == "calculator"
    assert token == owner.token
    assert backend.states["alice"].candidate is None
    refreshed, _ = backend.request_candidates("PRIVATE_QUERY", 2, token, request)
    assert refreshed.identity != view.identity
    assert retrieval.calls == [("PRIVATE_QUERY", 5), ("PRIVATE_QUERY", 2)]


def test_ineligible_candidate_names_portability_instead_of_approval() -> None:
    """An approved but non-portable tool must not be reported as unapproved."""
    from agentix.controllers.application_candidates import present_candidates
    from agentix.storage.application_catalog import CatalogDependencyError

    def resolve() -> dict[str, Any]:
        """Mirror the registry excluding every installed entry."""
        raise CatalogDependencyError(
            "No approved portable tools with canonical Annotated contracts."
        )

    registry = SimpleNamespace(
        resolve=resolve,
        skip_reasons=lambda: {
            "calculator": "imports outside the portable module list; add them to portable_modules.json"
        },
    )

    view = present_candidates("revision", "count words", 5, [match()], registry)

    assert view.ready is False
    assert view.eligible_ids == frozenset()
    assert "portable" in view.message.lower()
    assert "approve them in tools" not in view.message.lower()
    assert view.rows[0][3] == "Not portable for applications"


def test_generate_without_name_reports_the_missing_name_before_search(tmp_path: Path) -> None:
    """The name warning must appear at Generate, before any retrieval inference."""
    backend, owner, request, _tools, retrieval = setup_backend(tmp_path)

    with pytest.raises(ValueError, match="Application name must contain 1 to 100 characters"):
        backend.request_candidates("calculate", 5, owner.token, request, name="")

    assert retrieval.calls == []


def test_acceptance_passes_only_server_snapshot(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    """Acceptance consumes the exact shown selection and passes it to generation once."""
    backend, owner, request, tools, retrieval = setup_backend(tmp_path)
    view, token = backend.request_candidates("calculate", 5, owner.token, request)
    calls = []

    def generate(
        name: str,
        query: str,
        token: str,
        request: Any,
        *,
        selected: AcceptedCandidates | None = None,
    ) -> Iterator[tuple[Any, ...]]:
        """Capture the selected server-owned dependency contract without generation."""
        calls.append(selected)
        yield ("started", "", "", "", False, token)

    monkeypatch.setattr(backend, "generate_named", generate)
    assert list(
        backend.accept_candidates("Calculator app", "calculate", 5, view.identity, token, request)
    )
    assert calls[0].expected == {"calculator": match().descriptor.contract_digest}
    with pytest.raises(ValueError):
        list(
            backend.accept_candidates(
                "Calculator app", "calculate", 5, view.identity, token, request
            )
        )


@pytest.mark.parametrize("change", ["query", "limit", "source", "owner"])
def test_changed_or_foreign_selection_cannot_generate(tmp_path: Path, change: str) -> None:
    """Changed descriptions, limits, source bytes and owners invalidate acceptance."""
    backend, owner, request, tools, retrieval = setup_backend(tmp_path)
    view, token = backend.request_candidates("calculate", 5, owner.token, request)
    query, limit = "calculate", 5
    if change == "query":
        query = "changed"
    elif change == "limit":
        limit = 2
    elif change == "source":
        tools["calculator"] = replace(tools["calculator"], code=b"changed")
    else:
        request = SimpleNamespace(session_hash="bob")
    with pytest.raises(ValueError):
        list(backend.accept_candidates("App", query, limit, view.identity, token, request))
    assert backend.states["alice"].candidate is None


def test_startup_failure_is_retriable_and_clients_are_private(tmp_path: Path) -> None:
    """Startup failure keeps the GUI available; later owner clients are distinct."""
    calls = []

    def factory(catalog: ToolCatalog) -> Any:
        """Fail startup once, then create inert owner-scoped provider clients."""
        calls.append(object())
        if len(calls) == 1:
            raise RuntimeError("PRIVATE_PROVIDER_BODY")
        return SimpleNamespace(search=lambda query, limit: [match()], last_sync_report=None)

    service = GuiToolRetrieval(factory=factory)
    assert "unavailable" in service.initialize(ToolCatalog(tmp_path)).lower()
    first, second = RetrieverHandle(), RetrieverHandle()
    assert service.search(ToolCatalog(tmp_path), first, "calculate", 5)
    assert service.search(ToolCatalog(tmp_path), second, "calculate", 5)
    assert first.retriever is not second.retriever


def test_candidate_logs_omit_description(tmp_path: Path, caplog: pytest.LogCaptureFixture) -> None:
    """Record retrieval/acceptance decisions without logging original request bodies."""
    import logging

    backend, owner, request, tools, retrieval = setup_backend(tmp_path)
    with caplog.at_level(logging.INFO):
        backend.request_candidates("PRIVATE_QUERY", 5, owner.token, request)
    assert "candidate_search" in caplog.text
    assert "operation_id=" in caplog.text
    assert "PRIVATE_QUERY" not in caplog.text


def test_retrieval_handle_transition_is_correlated_and_payload_free(
    tmp_path: Path, caplog: pytest.LogCaptureFixture
) -> None:
    """Expose retriever creation without recording the application description."""
    from agentix.diagnostics import operation_scope

    service = GuiToolRetrieval(
        factory=lambda _catalog: SimpleNamespace(search=lambda _query, limit: [match()][:limit])
    )
    with caplog.at_level(logging.DEBUG):
        with operation_scope("diagnostic-session", "diagnostic-operation"):
            service.search(ToolCatalog(tmp_path), RetrieverHandle(), "PRIVATE_DESCRIPTION", 5)

    assert "event=retrieval_handle_creating session_id=diagnostic-session" in caplog.text
    assert "event=retrieval_handle_ready session_id=diagnostic-session" in caplog.text
    assert "PRIVATE_DESCRIPTION" not in caplog.text


def test_selected_registry_preserves_legacy_role_keys() -> None:
    """Selection constrains tools without changing existing adapter role contracts."""
    tool = approved_tool()
    selected = SelectedToolRegistry(
        SimpleNamespace(resolve=lambda: {"legacy_role": tool}),
        {tool.tool_name: hashlib.sha256(tool.code).hexdigest()},
    )
    assert selected.resolve() == {"legacy_role": tool}


def test_real_generation_boundary_receives_only_candidates(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    """Exercise production generation orchestration with a model-boundary spy."""
    from test_application_supervisor import candidate

    backend, owner, request, tools, retrieval = setup_backend(tmp_path)
    item = candidate(tmp_path)
    item.review_text = "{}"
    calls = []

    def generate(query: str, *, tools: dict) -> Any:
        """Record dependencies without invoking agents or executing source."""
        calls.append(tools)
        return item

    backend.pipeline_factory = lambda root: SimpleNamespace(generate=generate)
    view, token = backend.request_candidates("calculate", 5, owner.token, request)
    rows = list(
        backend.accept_candidates("Calculator app", "calculate", 5, view.identity, token, request)
    )
    assert "Human review required" in rows[-1][0]
    assert set(calls[0]) == {"calculator"}
    assert owner.controller.state.application_review_pending


def test_candidate_labels_preserve_metadata_as_plain_text() -> None:
    """Labels preserve bounded tool metadata while values carry only snapshot IDs."""
    from agentix.ui.application_candidates import candidate_choices

    choices = candidate_choices(
        SimpleNamespace(results=[match()], rows=[("<script>", "a & b", 0.1, "Ready")])
    )
    assert choices == [("<script> - a & b (score 0.1000; Ready)", "calculator")]


@pytest.mark.parametrize("failure", [False, True])
def test_obsolete_search_does_not_replace_newer_description(tmp_path: Path, failure: bool) -> None:
    """Discard both successful and failed inference after the user edits the request."""
    backend, owner, request, tools, retrieval = setup_backend(tmp_path)

    def slow(
        catalog: ToolCatalog, handle: RetrieverHandle, query: str, limit: int
    ) -> list[SearchResult]:
        """Simulate an edit arriving during retrieval without timing-dependent threads."""
        backend.invalidate_candidates(owner.token, request)
        if failure:
            raise RuntimeError("obsolete provider failure")
        return [match()]

    retrieval.search = slow
    view, token = backend.request_candidates("old description", 5, owner.token, request)
    assert view is None and token == owner.token
    assert not backend.candidate_controls(token, request)[1]


@pytest.mark.frameworks
def test_real_gradio_candidate_callback_contract(tmp_path: Path) -> None:
    """Construct actual controls and invoke their registered streaming callback in memory."""
    import gradio as gr

    from agentix.ui.shell import build_view

    backend, owner, request, tools, retrieval = setup_backend(tmp_path)
    demo = build_view(backend.sessions, applications_backend=backend).demo
    callback = next(
        item for item in demo.fns.values() if item.fn and item.fn.__name__ == "search_candidates"
    )
    rows = list(callback.fn("calculate", 5, owner.token, gr.Request(session_hash="alice")))
    assert len(rows[-1]) == len(callback.outputs)
    assert rows[-1][1]["value"] == ["calculator"]
    controls = {item["props"].get("elem_id"): item for item in demo.config["components"]}
    number = controls["application-candidate-limit"]["props"]
    assert number["minimum"] == 1 and number["maximum"] == 100
    assert number["precision"] == 0 and number["step"] == 1


@pytest.mark.frameworks
def test_real_gradio_accept_label_explains_a_blocked_selection(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    """The disabled accept button must state the blocking reason in its own label."""
    import gradio as gr

    from agentix.ui.shell import build_view

    backend, owner, request, tools, retrieval = setup_backend(tmp_path)
    bad = replace(match(), descriptor=replace(match().descriptor, tool_id="unapproved"))
    monkeypatch.setattr(retrieval, "search", lambda *args: [match(), bad])
    view, token = backend.request_candidates("calculate", 5, owner.token, request)
    demo = build_view(backend.sessions, applications_backend=backend).demo
    callback = next(
        item for item in demo.fns.values() if item.fn and item.fn.__name__ == "refresh_controls"
    )
    blocked = callback.fn(["calculator", "unapproved"], token, gr.Request(session_hash="alice"))
    assert blocked[1]["interactive"] is False
    assert blocked[1]["value"] == (
        "Accept 2 selected tools and generate - approve the selected tools in Tools first"
    )
    allowed = callback.fn(["calculator"], token, gr.Request(session_hash="alice"))
    assert allowed[1]["interactive"] is True
    assert allowed[1]["value"] == "Accept 1 selected tools and generate"


def test_bootstrap_initializes_retrieval_once_before_view(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    """Startup invokes index loading once and passes the same service to the backend."""
    import sys
    from types import ModuleType

    from agentix import bootstrap
    from agentix.settings import Settings

    events = []
    catalog = ToolCatalog(tmp_path)
    runtime = SimpleNamespace(
        settings=Settings(tmp_path, tmp_path),
        security=SimpleNamespace(),
        orchestrator=SimpleNamespace(run_system=lambda query: "unused"),
        catalog=catalog,
        operations=SimpleNamespace(acceptance=object()),
    )

    class Startup:
        """Observe composition without opening storage, servers or model clients."""

        def initialize(self, actual_catalog: ToolCatalog) -> None:
            """Record exactly the runtime catalog selected by the GUI startup."""
            events.append(("startup", actual_catalog))

    service = Startup()

    def factory() -> Startup:
        """Provide the explicit startup test boundary."""
        return service

    monkeypatch.setattr(bootstrap, "get_default_runtime", lambda: runtime)
    gr = ModuleType("gradio")
    gr.update = lambda **kwargs: kwargs
    monkeypatch.setitem(sys.modules, "gradio", gr)

    def build(sessions: Any, **kwargs: Any) -> Any:
        """Check startup ordering and injected retrieval identity."""
        assert events == [("startup", catalog)]
        assert kwargs["applications_backend"].retrieval is service
        events.append(("view", None))
        return object()

    monkeypatch.setattr("agentix.ui.view.build_view", build)
    bootstrap.get_default_ui.cache_clear()
    try:
        first = bootstrap.get_default_ui(retrieval_service_factory=factory)
        assert bootstrap.get_default_ui(retrieval_service_factory=factory) is first
        assert events == [("startup", catalog), ("view", None)]
    finally:
        bootstrap.get_default_ui.cache_clear()


def test_retrieval_serializes_owner_index_operations(tmp_path: Path) -> None:
    """Two independent owner clients cannot mutate/query their shared index concurrently."""
    from concurrent.futures import ThreadPoolExecutor
    from threading import Event

    entered, release = Event(), Event()
    sequence = []

    class Client:
        """Observe overlap at the real GUI service's injected retrieval boundary."""

        def search(self, query: str, *, limit: int) -> list[SearchResult]:
            """Block the first owner until the second has attempted access."""
            sequence.append((query, "enter"))
            if query == "first":
                entered.set()
                assert release.wait(5)
            sequence.append((query, "exit"))
            return [match()]

    service = GuiToolRetrieval(factory=lambda catalog: Client())
    catalog = ToolCatalog(tmp_path)
    with ThreadPoolExecutor(max_workers=2) as pool:
        first = pool.submit(service.search, catalog, RetrieverHandle(), "first", 5)
        assert entered.wait(5)
        second = pool.submit(service.search, catalog, RetrieverHandle(), "second", 5)
        try:
            assert not second.done()
        finally:
            release.set()
        assert first.result() and second.result()
    assert sequence == [
        ("first", "enter"),
        ("first", "exit"),
        ("second", "enter"),
        ("second", "exit"),
    ]


def test_acceptance_storage_failure_is_safe_and_logged(
    tmp_path: Path, caplog: pytest.LogCaptureFixture
) -> None:
    """Unavailable approval storage cannot escape as a raw exception or start generation."""
    import logging

    backend, owner, request, tools, retrieval = setup_backend(tmp_path)
    view, token = backend.request_candidates("calculate", 5, owner.token, request)

    def unavailable() -> dict[str, Any]:
        """Simulate inaccessible current approval metadata with a sensitive error body."""
        raise PermissionError("PRIVATE_PROVIDER_BODY")

    backend.registry_factory = lambda controller: SimpleNamespace(resolve=unavailable)
    with caplog.at_level(logging.INFO):
        with pytest.raises(ValueError, match="acceptance unavailable"):
            list(backend.accept_candidates("App", "calculate", 5, view.identity, token, request))
    assert "candidate_accept_rejected" in caplog.text
    assert "PRIVATE_PROVIDER_BODY" not in caplog.text
    assert backend.states["alice"].candidate is None


def test_closed_owner_discards_inflight_candidate_result(tmp_path: Path) -> None:
    """Closing an application session invalidates its outstanding retrieval revision."""
    backend, owner, request, tools, retrieval = setup_backend(tmp_path)

    def closing(
        catalog: ToolCatalog, handle: RetrieverHandle, query: str, limit: int
    ) -> list[SearchResult]:
        """Simulate owner cleanup completing before a pending model response returns."""
        backend.close_owner("alice")
        return [match()]

    retrieval.search = closing
    view, token = backend.request_candidates("calculate", 5, owner.token, request)
    assert view is None
    assert "alice" not in backend.states


@pytest.mark.parametrize("changed", [False, True])
def test_repair_keeps_accepted_scope_and_rechecks_source(tmp_path: Path, changed: bool) -> None:
    """Repairs reuse the accepted dependency set and cannot adopt modified selected code."""
    import json

    from test_application_supervisor import candidate

    backend, owner, request, tools, retrieval = setup_backend(tmp_path)
    item = candidate(tmp_path)
    item.review_text = "{}"
    calls = []

    def generate(query: str, *, tools: dict, feedback: dict | None = None) -> Any:
        """Record original and repair inputs without inference or source execution."""
        calls.append((query, set(tools), feedback))
        return item

    backend.pipeline_factory = lambda root: SimpleNamespace(generate=generate)
    view, token = backend.request_candidates("calculate", 5, owner.token, request)
    list(backend.accept_candidates("App", "calculate", 5, view.identity, token, request))
    item.folder.joinpath("requirements.txt").write_text("calculate", encoding="utf-8")
    item.folder.joinpath("validation.json").write_text(
        json.dumps({"failure": "fixture"}), encoding="utf-8"
    )
    state = backend.states["alice"]
    state.repair_allowed = True
    owner.controller.state.application_review_pending = False
    if changed:
        tools["calculator"] = replace(tools["calculator"], code=b"changed")
    rows = list(backend.repair(token, request))
    if changed:
        assert len(calls) == 1
        assert "generation failed" in rows[-1][0]
    else:
        assert len(calls) == 2
        assert all(query == "calculate" and names == {"calculator"} for query, names, _ in calls)
        assert calls[-1][2] == {"failure": "fixture"}


def test_reviewed_tool_revision_invalidates_candidate_application(tmp_path: Path) -> None:
    """Publishing revised tool bytes requires a fresh candidate choice, never a broader catalog."""
    import json

    from test_application_supervisor import candidate

    backend, owner, request, tools, retrieval = setup_backend(tmp_path)
    item = candidate(tmp_path)
    item.review_text = "{}"
    backend.pipeline_factory = lambda root: SimpleNamespace(generate=lambda query, **kwargs: item)
    view, token = backend.request_candidates("calculate", 5, owner.token, request)
    list(backend.accept_candidates("App", "calculate", 5, view.identity, token, request))
    contract = {
        "version": 1,
        "cases": [
            {
                "id": "normal",
                "purpose": "Add two values",
                "function": "calculator",
                "kwargs": {"a": 2, "b": 3},
                "expect": {"kind": "value", "value": 5},
            }
        ],
    }
    item.review_text = json.dumps(
        {
            "pending_tool_revisions": {
                "calculator": {
                    "tool_name": "calculator",
                    "code": tools["calculator"].code.decode() + "\n# revised",
                    "tests": "# independently authored test fixture",
                }
            },
            "tool_acceptance_contracts": {"calculator": contract},
            "manifest": {"tools": {"calculator": {"module": "calculator_code"}}, "files": []},
        }
    )
    owner.controller.tool_operations = SimpleNamespace(
        compile_and_save_code_tool=lambda *args: "Success: fixture",
        run_and_save_tests_tool=lambda *args: "TESTS_PROVISIONAL_PASSED: fixture",
        submit_acceptance_cases_tool=lambda *args: "ACCEPTANCE_VERIFIED: fixture",
        execute_generated_tool_tool=lambda *args: "Tool Execution Result: 5",
    )
    rows = list(backend.review_tools(token, request))
    assert "selection invalidated" in rows[-1][0]
    assert backend.states["alice"].candidate is None
    assert backend.states["alice"].accepted_dependencies is None
    assert item.package.exists(), "Prior proposal evidence must be preserved"


def test_busy_invalidation_is_logged_as_ignored(
    tmp_path: Path, caplog: pytest.LogCaptureFixture
) -> None:
    """Log the actual outcome when an active generation retains its original context."""
    import logging

    backend, owner, request, tools, retrieval = setup_backend(tmp_path)
    view, token = backend.request_candidates("calculate", 5, owner.token, request)
    owner.controller.state.application_busy = True
    owner.controller.state.application_phase = "generating"
    with caplog.at_level(logging.INFO):
        backend.invalidate_candidates(token, request)
    assert backend.states["alice"].retrieval_state.selection is view
    assert "candidate_invalidation_ignored" in caplog.text
    assert "event=candidate_invalidated" not in caplog.text


@pytest.mark.parametrize("chosen", [[], ["unknown"], ["calculator", "calculator"]])
def test_candidate_subset_rejects_invalid_ids(tmp_path: Path, chosen: list[str]) -> None:
    """Empty, foreign and duplicate browser IDs cannot authorize generation."""
    backend, owner, request, tools, retrieval = setup_backend(tmp_path)
    view, token = backend.request_candidates("calculate", 5, owner.token, request)
    with pytest.raises(ValueError):
        list(
            backend.accept_candidates(
                "App", "calculate", 5, view.identity, token, request, selected_ids=chosen
            )
        )
    assert backend.states["alice"].candidate is None


def test_candidate_subset_excludes_unchecked_tool(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    """Only checked snapshot IDs reach generation, with current source hashes."""
    backend, owner, request, tools, retrieval = setup_backend(tmp_path)
    extra = replace(
        match(), descriptor=replace(match().descriptor, tool_id="unrelated", name="unrelated")
    )
    monkeypatch.setattr(retrieval, "search", lambda *args: [match(), extra])
    view, token = backend.request_candidates("calculate", 5, owner.token, request)
    captured = []

    def generate(
        *args: Any, selected: AcceptedCandidates, **kwargs: Any
    ) -> Iterator[tuple[Any, ...]]:
        """Capture accepted dependencies without starting agents."""
        captured.append(selected)
        yield ("started",)

    monkeypatch.setattr(backend, "generate_named", generate)
    list(
        backend.accept_candidates(
            "App", "calculate", 5, view.identity, token, request, selected_ids=["calculator"]
        )
    )
    assert captured[0].expected == {"calculator": match().descriptor.contract_digest}
    assert backend.candidate_controls(token, request, selected_ids=[])[1] is False


def test_unchecked_ineligible_candidate_does_not_block_valid_subset(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    """An unapproved result cannot be selected but may be excluded from generation."""
    backend, owner, request, tools, retrieval = setup_backend(tmp_path)
    bad = replace(match(), descriptor=replace(match().descriptor, tool_id="unapproved"))
    monkeypatch.setattr(retrieval, "search", lambda *args: [match(), bad])
    view, token = backend.request_candidates("calculate", 5, owner.token, request)
    assert not view.ready
    assert not backend.candidate_controls(
        token, request, selected_ids=["calculator", "unapproved"]
    )[1]
    assert backend.candidate_controls(token, request, selected_ids=["calculator"])[1]
    assert view.selected_expected(["calculator"]) == {
        "calculator": match().descriptor.contract_digest
    }


def test_blocked_acceptance_names_its_reason(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    """A disabled accept button must explain why instead of failing silently."""
    backend, owner, request, tools, retrieval = setup_backend(tmp_path)
    bad = replace(match(), descriptor=replace(match().descriptor, tool_id="unapproved"))
    monkeypatch.setattr(retrieval, "search", lambda *args: [match(), bad])
    view, token = backend.request_candidates("calculate", 5, owner.token, request)
    idle, ready, owned, reason = backend.candidate_controls(
        token, request, selected_ids=["calculator", "unapproved"]
    )
    assert idle is True and ready is False and owned == token
    assert reason == "approve the selected tools in Tools first"
    assert backend.candidate_controls(token, request, selected_ids=["calculator"])[3] == ""
    assert backend.candidate_controls(token, request, selected_ids=[])[3] == (
        "select at least one current candidate"
    )
    assert backend.candidate_controls(token, request)[3] == (
        "approve the selected tools in Tools first"
    )
    backend.invalidate_candidates(token, request)
    assert backend.candidate_controls(token, request, selected_ids=["calculator"])[3] == (
        "search for candidates first"
    )
