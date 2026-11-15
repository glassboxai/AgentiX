"""Owner and cross-tab coordination regressions for Applications backend."""

from threading import RLock
from types import SimpleNamespace

import pytest

from agentix.controllers.applications import ApplicationsBackend
from agentix.controllers.sessions import SessionAccessError, SessionRegistry


def registry():
    """Supply an inert controller; model/native work is never needed for ownership tests."""
    from agentix.models.model_profiles import ModelProfile

    return SessionRegistry(
        lambda identity: SimpleNamespace(
            _lock=RLock(),
            state=SimpleNamespace(
                is_running=False, application_busy=False, application_review_pending=False
            ),
            model_configuration=SimpleNamespace(
                profile=ModelProfile(),
                client=None,
                ensure_generation_identity=lambda: "a" * 64,
            ),
        )
    )


def test_foreign_token_is_rejected_before_model_or_storage():
    """Catch application generation using another browser's Tools session."""
    sessions = registry()
    owner = sessions.resolve(None, "alice")
    backend = ApplicationsBackend(sessions)
    with pytest.raises(SessionAccessError):
        list(
            backend.generate(
                "Count words and vowels", owner.token, SimpleNamespace(session_hash="bob")
            )
        )


def test_active_tools_operation_blocks_application_generation():
    """Catch concurrent model work bypassing the shared controller state."""
    sessions = registry()
    owner = sessions.resolve(None, "alice")
    owner.controller.state.is_running = True
    backend = ApplicationsBackend(sessions)
    rows = list(
        backend.generate(
            "Count words and vowels", owner.token, SimpleNamespace(session_hash="alice")
        )
    )
    assert "Finish" in rows[-1][0]
    assert not owner.controller.state.application_busy


def test_repair_requires_a_failed_reviewed_candidate():
    """Catch automatic/unbounded repair without an independent failure report."""
    sessions = registry()
    owner = sessions.resolve(None, "alice")
    backend = ApplicationsBackend(sessions)
    rows = list(backend.repair(owner.token, SimpleNamespace(session_hash="alice")))
    assert "failed verification" in rows[-1][0]


def test_explicit_rejection_revokes_repair_eligibility():
    """Catch proposing another model repair after the human has rejected the operation."""
    sessions = registry()
    owner = sessions.resolve(None, "alice")
    backend = ApplicationsBackend(sessions)
    request = SimpleNamespace(session_hash="alice")
    _, state = backend._resolve(owner.token, request)
    state.repair_allowed = True
    backend.stop(owner.token, request)
    assert not state.repair_allowed


def test_rejection_revokes_verified_data_execution(tmp_path):
    """Rejecting a verified proposal must revoke its native data-execution grant."""
    from test_application_supervisor import candidate

    from agentix.application.app_workflow import ApplicationSupervisor

    calls = []
    supervisor = ApplicationSupervisor(native=lambda *args: calls.append(args))
    sessions = registry()
    owner = sessions.resolve(None, "alice")
    backend = ApplicationsBackend(sessions, supervisor=supervisor)
    request = SimpleNamespace(session_hash="alice")
    _, state = backend._resolve(owner.token, request)
    state.candidate = candidate(tmp_path)
    supervisor.approve(state.candidate, state.candidate.identity, True)
    state.candidate.verified = True
    backend.stop(owner.token, request)
    result, _, _ = backend.data("Hello World!", owner.token, request)
    assert calls == [], "Rejected content crossed the native execution boundary"
    assert result is None
    assert not state.candidate.approved
    assert not state.candidate.verified
    assert state.candidate.snapshot is None


def test_data_operation_reports_the_json_contract_without_echoing_input(tmp_path):
    """V7-073: a schema-3 payload rejection names the JSON error, never the typed text."""
    from test_application_supervisor import candidate

    from agentix.application.app_workflow import ApplicationSupervisor

    calls = []
    supervisor = ApplicationSupervisor(
        native=lambda approved, payload: calls.append(payload)
        or {"count_words_in_text": 2, "count_vowels_in_text": 3}
    )
    sessions = registry()
    owner = sessions.resolve(None, "alice")
    backend = ApplicationsBackend(sessions, supervisor=supervisor)
    request = SimpleNamespace(session_hash="alice")
    _, state = backend._resolve(owner.token, request)
    state.candidate = candidate(tmp_path)
    supervisor.approve(state.candidate, state.candidate.identity, True)
    state.candidate.verified = True

    value, message, owned = backend.data("hola gola", owner.token, request)
    assert value is None and calls == [] and owned == owner.token
    assert "JSONDecodeError" in message and "Expecting value" in message
    assert "hola gola" not in message

    value, message, _ = backend.data('{"texto": "hola gola"}', owner.token, request)
    assert value is None and calls == []
    assert "Missing or unknown application input" in message

    value, _, _ = backend.data('{"text": "hola gola"}', owner.token, request)
    assert calls == [{"text": "hola gola"}]
    assert value == {"count_words_in_text": 2, "count_vowels_in_text": 3}


def test_data_contract_names_declared_inputs_and_an_example_payload(tmp_path):
    """V7-073: the owner sees the closed input schema before typing a payload."""
    from test_application_supervisor import candidate

    from agentix.application.app_workflow import ApplicationSupervisor

    sessions = registry()
    owner = sessions.resolve(None, "alice")
    backend = ApplicationsBackend(sessions, supervisor=ApplicationSupervisor())
    request = SimpleNamespace(session_hash="alice")
    _, state = backend._resolve(owner.token, request)

    empty, owned = backend.data_contract(owner.token, request)
    assert owned == owner.token
    assert "Load and verify an application" in empty

    state.candidate = candidate(tmp_path)
    backend.supervisor.approve(state.candidate, state.candidate.identity, True)
    text, _ = backend.data_contract(owner.token, request)
    assert "`text`" in text and "string" in text
    assert '{"text": "Hello World!"}' in text


def test_repair_control_is_unavailable_until_owned_verification_failure():
    """The UI must not advertise repair before its server-side eligibility exists."""
    sessions = registry()
    owner = sessions.resolve(None, "alice")
    backend = ApplicationsBackend(sessions)
    request = SimpleNamespace(session_hash="alice")
    assert backend.review_state(owner.token, request)["repair_available"] is False


def test_unsaved_editor_changes_block_approval(tmp_path):
    """A checkbox cannot approve older bytes while different source is displayed."""
    from test_application_supervisor import candidate

    sessions = registry()
    owner = sessions.resolve(None, "alice")
    backend = ApplicationsBackend(sessions)
    request = SimpleNamespace(session_hash="alice")
    _, state = backend._resolve(owner.token, request)
    state.candidate = candidate(tmp_path)
    owner.controller.state.application_review_pending = True
    backend.mark_edited("application_logic.py", owner.token, request)
    result = list(backend.approve(True, state.candidate.identity, owner.token, request))
    assert "Save" in result[-1][0]
    assert not state.candidate.approved


def test_missing_registered_host_requirement_keeps_review_pending(tmp_path):
    """A missing host prerequisite must not approve, execute or close reviewed bytes."""
    sessions = registry()
    owner = sessions.resolve(None, "alice")
    request = SimpleNamespace(session_hash="alice")
    approved = []

    class Requirements:
        """Offer only the fixed browser requirement through the injected host boundary."""

        def missing(self, identifier):
            """Return an inert maintained requirement instead of running an installer."""
            assert identifier == "playwright-chromium"
            return SimpleNamespace(
                identifier=identifier, user_message="Install the maintained browser requirement."
            )

    class Supervisor:
        """Fail if approval crosses the host prerequisite boundary."""

        def approve(self, *args):
            """Record an unexpected approval attempt."""
            approved.append(args)

    backend = ApplicationsBackend(
        sessions, supervisor=Supervisor(), host_requirements=Requirements()
    )
    _, state = backend._resolve(owner.token, request)
    state.candidate = SimpleNamespace(
        identity="candidate",
        review_text='{"manifest": {"schema_version": 1}}',
        folder=tmp_path,
        close=lambda: None,
    )
    owner.controller.state.application_review_pending = True

    rows = list(backend.approve(True, "candidate", owner.token, request))

    assert "host dependency" in rows[-1][0].lower()
    assert approved == []
    assert state.pending_host_requirement == "playwright-chromium"
    assert owner.controller.state.application_review_pending


def test_explicit_host_dependency_install_requires_pending_owner_consent():
    """Only the owning pending review can invoke the fixed registered installer."""
    sessions = registry()
    owner = sessions.resolve(None, "alice")
    request = SimpleNamespace(session_hash="alice")
    installed = []

    class Requirements:
        """Record the one injected installer identity without exposing command choice."""

        def install(self, identifier):
            """Record an explicit installation request and return its reviewed metadata."""
            installed.append(identifier)
            return SimpleNamespace(identifier=identifier)

    backend = ApplicationsBackend(sessions, host_requirements=Requirements())
    _, state = backend._resolve(owner.token, request)
    state.pending_host_requirement = "playwright-chromium"
    state.candidate = SimpleNamespace(identity="candidate", close=lambda: None)
    owner.controller.state.application_review_pending = True

    message, owned = backend.install_host_requirement(owner.token, request)

    assert "installed and verified" in message.lower()
    assert owned == owner.token
    assert installed == ["playwright-chromium"]
    assert state.pending_host_requirement is None
    with pytest.raises(ValueError, match="No confirmed host dependency"):
        backend.install_host_requirement(owner.token, request)


def test_generation_only_exposes_safe_catalog_dependency_diagnostics():
    """An arbitrary model/parser ValueError must not be mistaken for a safe diagnostic."""
    sessions = registry()
    owner = sessions.resolve(None, "alice")
    owner.controller.security = SimpleNamespace(get_pending_request=lambda: None)

    def fail(root):
        """Simulate a parser error whose untrusted body mentions catalog."""
        raise ValueError("catalog PRIVATE_MODEL_BODY")

    backend = ApplicationsBackend(
        sessions,
        pipeline_factory=fail,
        registry_factory=lambda controller: SimpleNamespace(resolve=lambda: {}),
    )
    rows = list(
        backend.generate(
            "Count words and vowels", owner.token, SimpleNamespace(session_hash="alice")
        )
    )
    assert "PRIVATE_MODEL_BODY" not in rows[-1][0]
    assert "ValueError" in rows[-1][0]


def test_generation_names_an_unsupported_public_input_key():
    """V7-059: a closed contract rejection reaches the owner with its bounded reason."""
    from agentix.domain.application_code import ApplicationContractError

    sessions = registry()
    owner = sessions.resolve(None, "alice")
    owner.controller.security = SimpleNamespace(get_pending_request=lambda: None)

    def fail(root):
        """Simulate a model proposal whose input schema carries a numeric bound."""
        raise ApplicationContractError(
            "Application input 'repeat_count': unsupported keys minimum. "
            "Allowed: type, description, enum, items."
        )

    backend = ApplicationsBackend(
        sessions,
        pipeline_factory=fail,
        registry_factory=lambda controller: SimpleNamespace(resolve=lambda: {}),
    )
    rows = list(
        backend.generate(
            "Count words and vowels", owner.token, SimpleNamespace(session_hash="alice")
        )
    )
    assert "unsupported keys minimum" in rows[-1][0]
    assert "ValueError" not in rows[-1][0]
    assert "Evidence retained; no retry or approval occurred." in rows[-1][0]


def test_generation_passes_the_active_session_llm_to_the_pipeline():
    """Applications use the already configured session client, not a new default."""
    from agentix.models.model_profiles import ModelProfile

    sessions = registry()
    owner = sessions.resolve(None, "alice")
    client = object()
    owner.controller.security = SimpleNamespace(get_pending_request=lambda: None)
    owner.controller.model_configuration = SimpleNamespace(
        profile=ModelProfile(),
        client=client,
        ensure_generation_identity=lambda: "a" * 64,
    )
    received = []

    class Pipeline:
        """Capture the configured client before the controlled generation failure."""

        def set_model_client(self, value):
            """Record the model boundary received from the owning session."""
            received.append(value)

        def generate(self, *args, **kwargs):
            """Stop after the injection boundary without creating an artifact."""
            raise ValueError("controlled")

    backend = ApplicationsBackend(
        sessions,
        pipeline_factory=lambda root: Pipeline(),
        registry_factory=lambda controller: SimpleNamespace(resolve=lambda: {}),
    )
    list(
        backend.generate("Build an application", owner.token, SimpleNamespace(session_hash="alice"))
    )
    assert received == [client]


def test_generation_blocks_a_changed_tofu_identity_before_the_pipeline():
    """A changed local baseline cannot reach application model orchestration."""
    from agentix.models.model_profiles import ModelProfile
    from agentix.models.profile_errors import ProfileError

    sessions = registry()
    owner = sessions.resolve(None, "alice")
    owner.controller.security = SimpleNamespace(get_pending_request=lambda: None)

    def changed_identity() -> str:
        """Simulate the fixed local-profile change diagnostic."""
        raise ProfileError("generation_identity_changed")

    owner.controller.model_configuration = SimpleNamespace(
        profile=ModelProfile(), client=None, ensure_generation_identity=changed_identity
    )
    backend = ApplicationsBackend(
        sessions, pipeline_factory=lambda root: pytest.fail("pipeline used")
    )
    rows = list(
        backend.generate("Build an application", owner.token, SimpleNamespace(session_hash="alice"))
    )
    assert "[generation_identity_changed]" in rows[-1][0]
    assert "reset the trusted generation identity" in rows[-1][0]


def test_generation_names_the_missing_profile_selection(caplog):
    """A missing saved selection reports its own action instead of a changed digest."""
    import logging

    from agentix.models.model_profiles import ModelProfile
    from agentix.models.profile_errors import ProfileError

    sessions = registry()
    owner = sessions.resolve(None, "alice")
    owner.controller.security = SimpleNamespace(get_pending_request=lambda: None)

    def missing_selection() -> str:
        """Simulate the closed missing-selection diagnostic."""
        raise ProfileError("profile_not_selected")

    owner.controller.model_configuration = SimpleNamespace(
        profile=ModelProfile(), client=None, ensure_generation_identity=missing_selection
    )
    backend = ApplicationsBackend(
        sessions, pipeline_factory=lambda root: pytest.fail("pipeline used")
    )
    with caplog.at_level(logging.INFO, logger="agentix.controllers.applications"):
        rows = list(
            backend.generate(
                "Build an application", owner.token, SimpleNamespace(session_hash="alice")
            )
        )
    assert "[profile_not_selected]" in rows[-1][0]
    assert "Select a saved local profile" in rows[-1][0]
    assert "identity is unavailable or changed" not in rows[-1][0]
    assert "reason=profile_not_selected" in caplog.text


def test_poll_does_not_race_with_widget_publication():
    """Only the verifier owns dependency checks while publishing a new widget grant."""
    sessions = registry()
    owner = sessions.resolve(None, "alice")
    backend = ApplicationsBackend(sessions)
    request = SimpleNamespace(session_hash="alice")
    _, state = backend._resolve(owner.token, request)
    owner.controller.state.application_busy = True

    def partial_write():
        """Model the short interval between widget source and protected record writes."""
        raise ValueError("Publication in progress")

    state.candidate = SimpleNamespace(
        preview=SimpleNamespace(alive=True),
        dependency_check=partial_write,
        approved=True,
        verified=False,
        snapshot=object(),
        close=lambda: None,
    )
    message, _, _ = backend.poll(owner.token, request)
    assert message is None
    assert state.candidate.approved


def test_saved_group_clears_dirty_marker_and_can_enter_new_review(tmp_path):
    """Explicit group save must not leave a stale dirty flag blocking approval."""
    from test_application_review import generated

    from agentix.application.app_review import ApplicationReview

    sessions = registry()
    owner = sessions.resolve(None, "alice")
    backend = ApplicationsBackend(sessions)
    request = SimpleNamespace(session_hash="alice")
    _, state = backend._resolve(owner.token, request)
    state.candidate = generated(tmp_path)
    panes = ApplicationReview().panes(state.candidate, "count_words_in_text_widget.py")
    panes["widget"] += "\n# reviewed comment\n"
    panes["tool_tests"] = "import unittest\n# reviewed tool tests\n"

    backend.mark_group_edited("count_words_in_text_widget.py", owner.token, request)
    backend.save_review(
        "count_words_in_text_widget.py",
        "",
        panes["code"],
        panes["widget"],
        panes["tool_tests"],
        panes["widget_tests"],
        state.candidate.identity,
        owner.token,
        request,
    )
    assert not state.unsaved_file
    assert owner.controller.state.application_review_pending


def test_streaming_callbacks_never_suspend_while_holding_owner_lock():
    """Gradio may resume a generator on another thread; lexical locks must release."""
    import ast
    import inspect

    import agentix.controllers.applications as module

    tree = ast.parse(inspect.getsource(module))
    for node in ast.walk(tree):
        if isinstance(node, ast.With) and any(
            "_lock" in ast.unparse(item.context_expr) for item in node.items
        ):
            assert not any(
                isinstance(child, (ast.Yield, ast.YieldFrom)) for child in ast.walk(node)
            )
