"""Security contracts for TOFU local generation identities."""

from types import SimpleNamespace

import pytest


def test_local_generation_identity_requires_matching_trusted_digest():
    """A local model cannot authorize generation until its current digest matches trust."""
    from agentix.models.generation_identity import verify_generation_identity
    from agentix.models.model_profiles import ModelProfile

    profile = ModelProfile(model="local-generator:latest")
    assert (
        verify_generation_identity(
            profile,
            "a" * 64,
            reader=lambda endpoint: {
                "models": [{"name": "local-generator:latest", "digest": "a" * 64}]
            },
        )
        == "a" * 64
    )
    with pytest.raises(ValueError, match="identity"):
        verify_generation_identity(
            profile,
            "a" * 64,
            reader=lambda endpoint: {
                "models": [{"name": "local-generator:latest", "digest": "b" * 64}]
            },
        )


@pytest.mark.parametrize("digest", ["", "not-a-digest", "A" * 64])
def test_local_generation_identity_rejects_missing_or_invalid_trusted_digests(digest):
    """Malformed or absent profile trust never becomes a generation authorization."""
    from agentix.models.generation_identity import verify_generation_identity
    from agentix.models.model_profiles import ModelProfile

    with pytest.raises(ValueError, match="identity"):
        verify_generation_identity(ModelProfile(), digest, reader=lambda endpoint: {"models": []})


def test_saved_local_profile_records_tofu_baseline_and_rejects_changed_digest(tmp_path):
    """A first-use baseline is stable until an explicit reset is requested."""
    from agentix.models.profile_errors import ProfileError
    from agentix.storage.profile_store import SavedProfiles

    store = SavedProfiles(tmp_path, SimpleNamespace())
    saved = store.save(
        "Local generation",
        "Ollama",
        "local-generator:latest",
        "http://127.0.0.1:11434",
        "",
    )
    trusted = store.trust_generation_digest(saved["id"], saved["version"], "a" * 64)
    assert trusted["generation_digest"] == "a" * 64
    with pytest.raises(ProfileError, match="generation_identity_changed"):
        store.trust_generation_digest(saved["id"], trusted["version"], "b" * 64)
    reset = store.trust_generation_digest(saved["id"], trusted["version"], "b" * 64, reset=True)
    assert reset["generation_digest"] == "b" * 64


def test_saved_local_profile_preserves_only_an_unchanged_tofu_identity(tmp_path):
    """Profile edits cannot silently retain a baseline for another model identity."""
    from agentix.storage.profile_store import SavedProfiles

    store = SavedProfiles(tmp_path, SimpleNamespace())
    saved = store.save("Local", "Ollama", "first:latest", "http://127.0.0.1:11434", "")
    trusted = store.trust_generation_digest(saved["id"], saved["version"], "a" * 64)
    renamed = store.save(
        "Renamed",
        "Ollama",
        "first:latest",
        "http://127.0.0.1:11434",
        "",
        trusted["id"],
        trusted["version"],
    )
    assert renamed["generation_digest"] == "a" * 64
    changed = store.save(
        "Renamed",
        "Ollama",
        "second:latest",
        "http://127.0.0.1:11434",
        "",
        renamed["id"],
        renamed["version"],
    )
    assert changed["generation_digest"] == ""
