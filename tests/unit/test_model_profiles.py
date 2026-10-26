"""Regression contracts for session model configuration and secret boundaries."""

import importlib
from types import SimpleNamespace

import pytest


def profiles():
    """Load the feature with an actionable failure before implementation."""
    try:
        return importlib.import_module("agentix.model_profiles")
    except ModuleNotFoundError:
        pytest.fail("Approved session model-profile service is missing")


def test_default_local_profile_preserves_required_model():
    """Keep the validated local model as the default."""
    profile = profiles().ModelProfile()
    assert profile.model == "qwen3-coder:30b"
    assert profile.provider == "Ollama"


@pytest.mark.parametrize(
    "url",
    [
        "http://evil.example",
        "https://user:pass@example.com",
        "https://127.0.0.1/v1",
        "https://example.com/v1?key=secret",
        "https://example.com/#x",
    ],
)
def test_remote_endpoint_rejects_unsafe_destinations(url):
    """Reject plaintext, private targets, embedded credentials and URL payloads."""
    with pytest.raises(ValueError):
        profiles().ModelProfile("OpenAI-compatible", "model", url, remote_consent=True).validate(
            lambda host: ["93.184.216.34"]
        )


def test_remote_requires_explicit_consent():
    """Never enable remote data transfer implicitly."""
    with pytest.raises(ValueError, match="consent"):
        profiles().ModelProfile("OpenAI", "gpt-test", "https://api.openai.com/v1").validate()


def test_dns_private_resolution_rejected():
    """Reject a public-looking name that resolves to a private address."""
    with pytest.raises(ValueError):
        profiles().ModelProfile(
            "OpenAI-compatible", "model", "https://example.com/v1", remote_consent=True
        ).validate(lambda host: ["10.0.0.1"])


def test_secret_not_in_profile_repr():
    """Profile data contains a credential reference rather than the API key."""
    profile = profiles().ModelProfile(credential_ref="opaque-reference")
    assert "opaque-reference" not in repr(profile)


def test_local_endpoint_must_be_loopback():
    """Ollama configuration cannot become an arbitrary HTTP request destination."""
    with pytest.raises(ValueError):
        profiles().ModelProfile(endpoint="http://192.168.1.2:11434").validate()


def test_session_configuration_denies_running_and_pending():
    """A model change cannot replace an active or awaiting-review workflow."""
    module = profiles()
    controller = SimpleNamespace(
        state=SimpleNamespace(is_running=True),
        security=SimpleNamespace(get_pending_request=lambda: None),
    )
    with pytest.raises(ValueError, match="operation"):
        module.ensure_configurable(controller)
    controller.state.is_running = False
    controller.security.get_pending_request = lambda: {"request_id": "pending"}
    with pytest.raises(ValueError, match="review"):
        module.ensure_configurable(controller)


def test_remote_client_uses_explicit_key_and_limits():
    """Inject the key without process environment mutation or unbounded retries."""
    module = profiles()
    calls = []
    vault = SimpleNamespace(read=lambda reference: "private-test-key")
    profile = module.ModelProfile("OpenAI", "test-model", "https://api.openai.com/v1", "ref", True)
    module.create_profile_llm(
        profile,
        vault,
        lambda **kwargs: calls.append(kwargs),
        resolver=lambda host: ["93.184.216.34"],
    )
    assert calls[0]["api_key"] == "private-test-key"
    assert calls[0]["model"] == "openai/test-model"
    assert calls[0]["timeout"] <= 120
    assert calls[0]["max_tokens"] <= 8192
    assert calls[0]["max_retries"] == 0


def test_client_failure_is_secret_free():
    """Do not expose provider exceptions that may contain Authorization headers."""
    module = profiles()

    def fail(**kwargs):
        """Simulate a provider leaking credentials into its exception."""
        raise RuntimeError("private-test-key")

    with pytest.raises(ValueError) as failure:
        module.create_profile_llm(module.ModelProfile(), SimpleNamespace(), fail)
    assert "private-test-key" not in str(failure.value)


@pytest.mark.parametrize("model", ["", "../file", "bad\nmodel", "x" * 201])
def test_model_identifiers_are_bounded(model):
    """Reject control characters, path traversal and oversized names."""
    with pytest.raises(ValueError):
        profiles().ModelProfile(model=model).validate()


def test_model_switch_is_transactional_and_invalidates_old_services():
    """Commit fresh services only after successful provider initialization."""
    module = profiles()
    values = {}
    vault = SimpleNamespace(
        write=lambda ref, key: values.update({ref: key}),
        read=lambda ref: values[ref],
        delete=lambda ref: values.pop(ref, None),
    )
    security = SimpleNamespace(get_pending_request=lambda: None)
    controller = SimpleNamespace(
        state=SimpleNamespace(is_running=False, session_id="a" * 32),
        security=security,
        run_system="old",
        validation="old-verdict",
        get_installed_tools_catalog="old-catalog",
    )
    runtime = SimpleNamespace(
        orchestrator=SimpleNamespace(run_system="new"),
        operations=SimpleNamespace(acceptance="fresh-verdict"),
        catalog=SimpleNamespace(render="new-catalog"),
    )
    service = module.SessionModelConfiguration(
        controller,
        lambda llm: runtime,
        vault_factory=lambda: vault,
        llm_factory=lambda **kw: object(),
        resolver=lambda host: ["93.184.216.34"],
    )
    assert "OpenAI" in service.configure(
        "OpenAI", "model", "https://api.openai.com/v1", "test-private-key", True
    )
    assert controller.run_system == "new"
    assert controller.validation == "fresh-verdict"
    assert len(values) == 1
    service.close()
    assert values == {}


def test_failed_model_switch_removes_new_credential_and_retains_old_runtime():
    """A provider failure cannot leave a stored key or partially swap services."""
    module = profiles()
    values = {}
    vault = SimpleNamespace(
        write=lambda ref, key: values.update({ref: key}),
        read=lambda ref: values[ref],
        delete=lambda ref: values.pop(ref, None),
    )
    controller = SimpleNamespace(
        state=SimpleNamespace(is_running=False, session_id="b" * 32),
        security=SimpleNamespace(get_pending_request=lambda: None),
        run_system="old",
    )

    def fail(llm):
        """Deny runtime composition after client creation."""
        raise RuntimeError("test-private-key")

    service = module.SessionModelConfiguration(
        controller,
        fail,
        vault_factory=lambda: vault,
        llm_factory=lambda **kw: object(),
        resolver=lambda host: ["93.184.216.34"],
    )
    with pytest.raises(ValueError) as error:
        service.configure("OpenAI", "model", "https://api.openai.com/v1", "test-private-key", True)
    assert "test-private-key" not in str(error.value)
    assert values == {} and controller.run_system == "old"


def test_host_redacts_vendor_exception_and_activity():
    """Keys cannot appear in formatted application/vendor logs or activity."""
    import logging

    import agentix.credentials as credentials

    credentials.register_secret("test-redaction-key")
    record = logging.LogRecord(
        "vendor", logging.ERROR, "", 1, "Authorization: %s", ("test-redaction-key",), None
    )
    credentials.SecretFilter().filter(record)
    assert "test-redaction-key" not in record.getMessage()
    assert "[REDACTED]" in record.getMessage()


@pytest.mark.frameworks
def test_review_container_is_single_below_validation_and_outside_sidebar():
    """Inspect actual Gradio component ancestry, rather than matching source text."""
    import gradio as gr

    from agentix.ui.sessions import SessionRegistry
    from agentix.ui.view import build_view

    view = build_view(SessionRegistry(lambda identity: None), gradio_module=gr)
    config = view.demo.get_config_file()
    components = {item["id"]: item for item in config["components"]}
    sidebar_ids = [key for key, item in components.items() if item["type"] == "sidebar"]
    assert len(sidebar_ids) == 1
    editor_ids = [
        key
        for key, item in components.items()
        if item["props"].get("label")
        == "Review and edit file content or acceptance cases before approving"
    ]
    assert len(editor_ids) == 1
    validation = next(
        key
        for key, item in components.items()
        if item["props"].get("elem_id") == "validation-panel"
    )
    chains = {}

    def visit(node, ancestors):
        """Record real layout ancestry for each rendered native component."""
        chains[node["id"]] = ancestors
        for child in node.get("children", []):
            visit(child, ancestors + [node["id"]])

    visit(config["layout"], [])
    editor = editor_ids[0]
    assert sidebar_ids[0] not in chains[editor]
    validation_parent = chains[validation][-1]
    assert components[validation_parent]["type"] == "column"
    assert validation_parent in chains[editor]
    assert validation < editor  # Construction order places review below validation.
    assert (
        sum(
            item["props"].get("value") == "Approve Reviewed Content" for item in components.values()
        )
        == 1
    )


def test_oversized_query_cannot_start_worker():
    """Deny oversized task data before logging, history retention or model work."""
    from agentix.ui.controller import UiController

    controller = UiController(
        lambda query: pytest.fail("must not call model"),
        lambda: "",
        SimpleNamespace(),
        lambda **kw: kw,
    )
    with pytest.raises(ValueError, match="limit"):
        controller.process_user_query("x" * 16001)
    assert controller.state.chat_history == []


@pytest.mark.parametrize(
    "destination",
    [
        "https://evil.example/v1/chat/completions",
        "http://api.openai.com/v1/chat/completions",
        "https://api.openai.com/other",
    ],
)
def test_remote_request_policy_denies_destination_changes(destination):
    """No credential-bearing request can change its approved origin or base path."""
    module = profiles()
    policy = module.RemoteRequestPolicy(
        module.ModelProfile("OpenAI", "model", "https://api.openai.com/v1", remote_consent=True),
        lambda host: ["93.184.216.34"],
    )
    with pytest.raises(ValueError):
        policy.validate_url(destination)


def test_remote_policy_rejects_redirect_and_rechecks_dns():
    """Prevent redirect following and detect private resolution on later calls."""
    module = profiles()
    addresses = ["93.184.216.34"]
    policy = module.RemoteRequestPolicy(
        module.ModelProfile("OpenAI", "model", "https://api.openai.com/v1", remote_consent=True),
        lambda host: addresses,
    )
    policy.validate_url("https://api.openai.com/v1/chat/completions")
    addresses[:] = ["127.0.0.1"]
    with pytest.raises(ValueError):
        policy.validate_url("https://api.openai.com/v1/chat/completions")
    with pytest.raises(ValueError):
        policy.validate_response(302)


def test_agents_have_finite_work_limits(system):
    """All roles retain verbose output but have bounded iteration/time/retry policy."""
    for call in system.crewai.Agent.call_args_list:
        assert call.kwargs["max_iter"] == 12
        assert call.kwargs["max_execution_time"] == 600
        assert call.kwargs["max_retry_limit"] == 0


def test_foreign_session_cannot_configure_model():
    """Reject a stolen token before touching model or credential services."""
    from agentix.ui.sessions import SessionAccessError, SessionCallbacks, SessionRegistry

    calls = []
    registry = SessionRegistry(
        lambda identity: SimpleNamespace(
            state=SimpleNamespace(is_running=False),
            configure_model=lambda *args: calls.append(args),
        )
    )
    alice = registry.resolve(None, "alice")
    with pytest.raises(SessionAccessError):
        SessionCallbacks(registry).configure_model(
            "Ollama",
            "model",
            "http://127.0.0.1:11434",
            "",
            False,
            alice.token,
            SimpleNamespace(session_hash="bob"),
        )
    assert calls == []


def test_global_work_capacity_rejects_without_contacting_model(system, monkeypatch):
    """Overload is denied immediately instead of queueing unlimited model work."""
    import agentix.orchestration as module

    gate = SimpleNamespace(acquire=lambda **kw: False)
    monkeypatch.setattr(module, "_WORK_CAPACITY", gate, raising=False)
    with pytest.raises(ValueError, match="capacity"):
        system.main.run_system("hello")
    system.crewai.Crew.assert_not_called()


def test_cli_query_limit_precedes_model_work(system):
    """The shared orchestration service also bounds terminal requests."""
    with pytest.raises(ValueError, match="limit"):
        system.main.run_system("x" * 16001)
    system.crewai.Crew.assert_not_called()


def test_namespaced_installed_model_identifiers_are_supported():
    """Accept ordinary Ollama/provider namespaces without permitting traversal."""
    profiles().ModelProfile(model="namespace/qwen3-coder:30b").validate()


@pytest.mark.parametrize("address", ["224.0.0.1", "ff0e::1"])
def test_remote_resolution_rejects_multicast_addresses(address):
    """Python is_global alone includes multicast, which is not a public API host."""
    with pytest.raises(ValueError):
        profiles().ModelProfile(
            "OpenAI-compatible", "model", "https://example.com/v1", remote_consent=True
        ).validate(lambda host: [address])
