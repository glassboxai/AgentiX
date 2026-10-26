"""Persistent profile and local model discovery contracts, with fake external IO."""

import importlib
import json
from types import SimpleNamespace

import pytest


def feature():
    """Produce an explicit missing-feature assertion before implementation."""
    try:
        return importlib.import_module("agentix.profile_store")
    except ModuleNotFoundError:
        pytest.fail("Persistent nonsecret profile repository is not implemented")


@pytest.fixture
def vault():
    """Model credential operations without touching Windows or real keys."""
    data = {}
    return SimpleNamespace(
        data=data,
        write=lambda ref, key: data.update({ref: key}),
        read=lambda ref: data[ref],
        delete=lambda ref: data.pop(ref, None),
    )


def test_profiles_survive_repository_restart_without_plaintext_keys(tmp_path, vault):
    """Persist metadata and reload it without exposing API key bytes."""
    store = feature().SavedProfiles(tmp_path, vault, resolver=lambda host: ["93.184.216.34"])
    saved = store.save(
        "My provider", "OpenAI", "test-model", "https://api.openai.com/v1", "synthetic-profile-key"
    )
    again = feature().SavedProfiles(tmp_path, vault, resolver=lambda host: ["93.184.216.34"])
    assert again.get(saved["id"])["name"] == "My provider"
    assert again.list()[0]["id"] == saved["id"]
    assert "synthetic-profile-key" not in json.dumps(saved)
    assert all("synthetic-profile-key" not in path.read_text() for path in tmp_path.glob("*.json"))
    assert "consent" not in saved


def test_key_update_failure_retains_original_profile_and_key(tmp_path, vault):
    """A rejected vault update cannot invalidate a working saved credential."""
    store = feature().SavedProfiles(tmp_path, vault, resolver=lambda host: ["93.184.216.34"])
    saved = store.save(
        "Provider", "OpenAI", "test-model", "https://api.openai.com/v1", "synthetic-first-key"
    )
    vault.write = lambda ref, key: (_ for _ in ()).throw(RuntimeError("synthetic-second-key"))
    with pytest.raises(ValueError) as failure:
        store.save(
            "Changed",
            "OpenAI",
            "test-model",
            "https://api.openai.com/v1",
            "synthetic-second-key",
            saved["id"],
            saved["version"],
        )
    assert "synthetic-second-key" not in str(failure.value)
    assert store.get(saved["id"])["name"] == "Provider"
    assert vault.read(saved["credential_ref"]) == "synthetic-first-key"


def test_stale_profile_edit_does_not_overwrite_newer_key(tmp_path, vault):
    """Reject a stale browser edit before changing any credential."""
    store = feature().SavedProfiles(tmp_path, vault, resolver=lambda host: ["93.184.216.34"])
    saved = store.save(
        "Provider", "OpenAI", "model", "https://api.openai.com/v1", "synthetic-first-key"
    )
    updated = store.save(
        "Updated",
        "OpenAI",
        "model",
        "https://api.openai.com/v1",
        "synthetic-second-key",
        saved["id"],
        saved["version"],
    )
    with pytest.raises(ValueError, match="changed"):
        store.save(
            "Stale",
            "OpenAI",
            "model",
            "https://api.openai.com/v1",
            "synthetic-third-key",
            saved["id"],
            saved["version"],
        )
    assert store.get(saved["id"])["version"] == updated["version"]
    assert set(vault.data.values()) == {"synthetic-second-key"}


def test_delete_removes_only_selected_owned_profile(tmp_path, vault):
    """Never enumerate or remove unrelated Windows credentials."""
    store = feature().SavedProfiles(tmp_path, vault, resolver=lambda host: ["93.184.216.34"])
    saved = store.save(
        "Provider", "OpenAI", "model", "https://api.openai.com/v1", "synthetic-first-key"
    )
    vault.data["unrelated"] = "unrelated-test-key"
    store.delete(saved["id"], saved["version"])
    assert store.list() == []
    assert vault.data == {"unrelated": "unrelated-test-key"}


@pytest.mark.parametrize("profile_id", ["../bad", "x" * 32, "", "C:/anything"])
def test_profile_identifier_cannot_escape_store(tmp_path, vault, profile_id):
    """Use only closed UUID filenames, never browser-provided paths."""
    store = feature().SavedProfiles(tmp_path, vault)
    with pytest.raises(ValueError):
        store.get(profile_id)


def test_corrupt_metadata_is_denied_not_silently_replaced(tmp_path, vault):
    """A mismatched credential namespace cannot authorize a key lookup."""
    store = feature().SavedProfiles(tmp_path, vault, resolver=lambda host: ["93.184.216.34"])
    saved = store.save(
        "Provider", "OpenAI", "model", "https://api.openai.com/v1", "synthetic-first-key"
    )
    saved["credential_ref"] = "AgentiX/v3/" + "a" * 32 + "/" + "b" * 32
    (tmp_path / (saved["id"] + ".json")).write_text(json.dumps(saved))
    with pytest.raises(ValueError):
        store.get(saved["id"])


def test_ollama_discovery_reads_tags_only_and_filters_invalid_names():
    """Discover installed models without model downloads or inference."""
    from agentix import model_profiles

    calls = []

    def read(url):
        """Return a bounded deterministic Ollama response fixture."""
        calls.append(url)
        return {
            "models": [{"name": "qwen3-coder:30b"}, {"name": "qwen3:14b"}, {"name": "../invalid"}]
        }

    assert model_profiles.installed_models("http://127.0.0.1:11434", read) == [
        "qwen3-coder:30b",
        "qwen3:14b",
    ]
    assert calls == ["http://127.0.0.1:11434/api/tags"]


def test_ollama_unavailable_is_payload_free():
    """Network exceptions cannot leak configuration or response bodies."""
    from agentix import model_profiles

    with pytest.raises(ValueError) as failure:
        model_profiles.installed_models(
            "http://127.0.0.1:11434",
            lambda url: (_ for _ in ()).throw(RuntimeError("sensitive-body")),
        )
    assert "sensitive-body" not in str(failure.value)


def test_saved_activation_requires_fresh_consent_and_survives_session_close(tmp_path, vault):
    """Persistence never implies remote startup or remembered task-transfer consent."""
    from agentix.model_profiles import SessionModelConfiguration

    store = feature().SavedProfiles(tmp_path, vault, resolver=lambda host: ["93.184.216.34"])
    saved = store.save(
        "Provider", "OpenAI", "model", "https://api.openai.com/v1", "synthetic-first-key"
    )

    def service():
        """Create another independent browser configuration over shared saved profiles."""
        controller = SimpleNamespace(
            state=SimpleNamespace(is_running=False, session_id="a" * 32),
            security=SimpleNamespace(get_pending_request=lambda: None),
        )
        runtime = SimpleNamespace(
            orchestrator=SimpleNamespace(run_system="new"),
            operations=SimpleNamespace(acceptance="new"),
            catalog=SimpleNamespace(render="new"),
        )
        return SessionModelConfiguration(
            controller,
            lambda llm: runtime,
            vault_factory=lambda: vault,
            llm_factory=lambda **kw: object(),
            resolver=lambda host: ["93.184.216.34"],
            store_factory=lambda vault: store,
        )

    first = service()
    assert first.profile.provider == "Ollama"
    first.select_saved(saved["id"])
    with pytest.raises(ValueError, match="consent"):
        first.configure("OpenAI", "model", "https://api.openai.com/v1", "", False)
    first.configure("OpenAI", "model", "https://api.openai.com/v1", "", True)
    first.close()
    assert vault.read(saved["credential_ref"]) == "synthetic-first-key"
    assert service().profile.provider == "Ollama"


def test_saved_key_cannot_be_sent_to_edited_endpoint(tmp_path, vault):
    """A changed destination requires saving a reviewed profile rather than reusing its key."""
    from agentix.model_profiles import SessionModelConfiguration

    store = feature().SavedProfiles(tmp_path, vault, resolver=lambda host: ["93.184.216.34"])
    saved = store.save(
        "Provider", "OpenAI-compatible", "model", "https://example.com/v1", "synthetic-first-key"
    )
    controller = SimpleNamespace(
        state=SimpleNamespace(is_running=False),
        security=SimpleNamespace(get_pending_request=lambda: None),
    )
    service = SessionModelConfiguration(
        controller,
        lambda llm: pytest.fail("must not build runtime"),
        vault_factory=lambda: vault,
        store_factory=lambda vault: store,
        resolver=lambda host: ["93.184.216.34"],
    )
    service.select_saved(saved["id"])
    with pytest.raises(ValueError, match="Save"):
        service.configure("OpenAI-compatible", "model", "https://other.example/v1", "", True)


def test_failed_metadata_commit_preserves_original_credential(tmp_path, vault, monkeypatch):
    """A disk failure after candidate credential creation must not replace old state."""
    store = feature().SavedProfiles(tmp_path, vault, resolver=lambda host: ["93.184.216.34"])
    saved = store.save(
        "Provider", "OpenAI", "model", "https://api.openai.com/v1", "synthetic-first-key"
    )

    def fail(record):
        """Simulate disk-full while keeping the existing metadata intact."""
        raise OSError("disk full")

    monkeypatch.setattr(store, "_commit", fail)
    with pytest.raises(ValueError):
        store.save(
            "Updated",
            "OpenAI",
            "model",
            "https://api.openai.com/v1",
            "synthetic-second-key",
            saved["id"],
            saved["version"],
        )
    assert store.get(saved["id"]) == saved
    assert set(vault.data.values()) == {"synthetic-first-key"}


def test_stale_displayed_profile_id_cannot_save_another_selection():
    """A queued browser action must match the session's selected profile identity."""
    from unittest.mock import Mock

    from agentix.ui.controller import UiController

    controller = UiController(lambda query: "", lambda: "", SimpleNamespace(), lambda **kw: kw)
    save = Mock(return_value="saved")
    controller.model_configuration = SimpleNamespace(
        saved_id="a" * 32, save_profile=save, saved_choices=lambda: [("Other", "a" * 32)]
    )
    result = controller.profile_action(
        "save", "b" * 32, "Stale", "OpenAI", "model", "https://api.openai.com/v1", "synthetic-key"
    )
    assert "not completed" in result[-1]
    save.assert_not_called()


def test_local_profiles_persist_without_any_credential_operations(tmp_path):
    """Local metadata supports full lifecycle even when Windows credentials are blocked."""

    def deny(*args):
        """Fail if local operations touch a credential boundary."""
        pytest.fail("Local profiles must not access credentials")

    store = feature().SavedProfiles(tmp_path, SimpleNamespace(write=deny, read=deny, delete=deny))
    saved = store.save("Qwen3-coder:30b", "Ollama", "qwen3-coder:30b", "http://127.0.0.1:11434", "")
    assert saved["credential_ref"] == ""
    assert store.get(saved["id"])["provider"] == "Ollama"
    updated = store.save(
        "Perfil local José",
        "Ollama",
        "namespace/qwen3:14b",
        "http://127.0.0.1:11434",
        "",
        saved["id"],
        saved["version"],
    )
    assert store.list()[0]["name"] == "Perfil local José"
    store.delete(updated["id"], updated["version"])
    assert store.list() == []


def test_local_session_profile_does_not_construct_vault(tmp_path):
    """Opening and saving local profiles does not require native credential availability."""
    from agentix.model_profiles import SessionModelConfiguration

    def deny():
        """Represent blocked Windows Credential Manager initialization."""
        pytest.fail("Vault factory must stay lazy for local metadata")

    controller = SimpleNamespace(
        state=SimpleNamespace(is_running=False),
        security=SimpleNamespace(get_pending_request=lambda: None),
    )
    config = SessionModelConfiguration(
        controller,
        lambda llm: None,
        vault_factory=deny,
        store_factory=lambda vault: feature().SavedProfiles(tmp_path, vault),
    )
    config.saved_choices()
    config.save_profile("Local", "Ollama", "qwen3-coder:30b", "http://127.0.0.1:11434", "")
    assert config.saved_choices()[1][0] == "Local"


def test_remote_to_local_conversion_retires_credentials(tmp_path, vault):
    """Provider changes cannot leave an active local credential or lose the old record on failure."""
    store = feature().SavedProfiles(tmp_path, vault, resolver=lambda host: ["93.184.216.34"])
    saved = store.save("Remote", "OpenAI", "model", "https://api.openai.com/v1", "synthetic-key")
    local = store.save(
        "Local",
        "Ollama",
        "qwen3-coder:30b",
        "http://127.0.0.1:11434",
        "",
        saved["id"],
        saved["version"],
    )
    assert local["credential_ref"] == "" and vault.data == {}
    with pytest.raises(ValueError):
        store.save(
            "Remote again",
            "OpenAI",
            "model",
            "https://api.openai.com/v1",
            "",
            local["id"],
            local["version"],
        )


def test_credential_failure_has_safe_phase_code(tmp_path, vault):
    """Distinguish a native-vault write failure without publishing its exception body."""
    store = feature().SavedProfiles(tmp_path, vault, resolver=lambda host: ["93.184.216.34"])
    vault.write = lambda *args: (_ for _ in ()).throw(RuntimeError("private-key-value"))
    with pytest.raises(ValueError) as caught:
        store.save("Remote", "OpenAI", "model", "https://api.openai.com/v1", "synthetic-key")
    assert getattr(caught.value, "code", None) == "credential_write"
    assert "private-key-value" not in str(caught.value)


def test_metadata_failure_has_distinct_safe_phase_code(tmp_path, vault, monkeypatch):
    """A file-write failure is distinguishable from the credential boundary."""
    store = feature().SavedProfiles(tmp_path, vault, resolver=lambda host: ["93.184.216.34"])
    monkeypatch.setattr(
        store, "_commit", lambda record: (_ for _ in ()).throw(OSError("sensitive-path"))
    )
    with pytest.raises(ValueError) as caught:
        store.save("Remote", "OpenAI", "model", "https://api.openai.com/v1", "synthetic-key")
    assert getattr(caught.value, "code", None) == "metadata_write"
    assert "sensitive-path" not in str(caught.value)
    assert vault.data == {}


def test_invalid_key_error_is_classified_without_key_echo():
    """Key validation has a fixed code rather than an unstructured native error."""
    from agentix.credentials import register_secret

    with pytest.raises(ValueError) as caught:
        register_secret("bad key")
    assert getattr(caught.value, "code", None) == "key_format"
    assert "bad key" not in str(caught.value)


def test_ui_retains_safe_failed_save_reason_after_refresh(tmp_path, vault):
    """The reported Save-then-Refresh path must not erase the useful failure reason."""
    from agentix.model_profiles import SessionModelConfiguration
    from agentix.ui.controller import UiController

    security = SimpleNamespace(get_pending_request=lambda: None)
    controller = UiController(lambda query: "", lambda: "", security, lambda **kw: kw)
    store = feature().SavedProfiles(tmp_path, vault, resolver=lambda host: ["93.184.216.34"])
    controller.model_configuration = SessionModelConfiguration(
        controller,
        lambda llm: None,
        vault_factory=lambda: vault,
        store_factory=lambda boundary: store,
    )
    vault.write = lambda *args: (_ for _ in ()).throw(RuntimeError("private-provider-key"))
    first = controller.profile_action(
        "save", "", "Remote", "OpenAI", "model", "https://api.openai.com/v1", "synthetic-key"
    )
    assert "[credential_write]" in first[-1]
    again = controller.profile_action(
        "refresh", "", "Remote", "OpenAI", "model", "https://api.openai.com/v1", ""
    )
    assert "Last save failed" in again[-1] and "[credential_write]" in again[-1]
    assert "private-provider-key" not in again[-1]


def test_oversized_native_blob_is_rejected_before_windows_call():
    """Preserve legacy encoding while reporting its native byte limit explicitly."""
    from agentix.credentials import WindowsCredentialVault

    vault = object.__new__(WindowsCredentialVault)
    vault.api = SimpleNamespace(
        CredWriteW=lambda *args: pytest.fail("Native write must not run for an oversized blob")
    )
    with pytest.raises(ValueError) as caught:
        vault.write("AgentiX/v3/" + "a" * 32 + "/" + "b" * 32, "x" * 1281)
    assert getattr(caught.value, "code", None) == "key_storage_limit"


def test_candidate_cleanup_failure_preserves_original_safe_reason(tmp_path, vault):
    """A second failure during cleanup must not hide the primary credential failure."""
    from agentix.profile_errors import ProfileError

    store = feature().SavedProfiles(tmp_path, vault, resolver=lambda host: ["93.184.216.34"])
    vault.write = lambda *args: (_ for _ in ()).throw(ProfileError("key_format"))
    vault.delete = lambda *args: (_ for _ in ()).throw(RuntimeError("private-cleanup-body"))
    with pytest.raises(ProfileError) as caught:
        store.save("Remote", "OpenAI", "model", "https://api.openai.com/v1", "synthetic-key")
    assert caught.value.code == "key_format"
    assert "private-cleanup-body" not in str(caught.value)
