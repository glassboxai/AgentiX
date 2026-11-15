"""Read-only code explanation uses bounded, explicitly selected context."""

import pytest


def assistant():
    """Resolve the application service without importing Gradio or a provider SDK."""
    try:
        from agentix.application.code_assistance import explain_code
    except ImportError:
        pytest.fail("Read-only contextual assistance is not implemented")
    return explain_code


def test_explanation_receives_selected_source_and_specs_without_execution():
    """Catch omission of the current editor buffer or unexpected source execution."""

    class Client:
        """Synthetic model boundary; no provider SDK or network."""

        def call(self, messages):
            """Observe the exact request or reproduce a provider failure."""
            assert "edited source" in messages[-1]["content"]
            assert "Count ASCII vowels" in messages[-1]["content"]
            assert "untrusted" in messages[0]["content"].lower()
            return "This function counts vowels."

    context = {
        "filename": "count_vowels_in_text_widget.py",
        "source": "edited source",
        "specification": "Count ASCII vowels",
        "contract": {"input": "text", "output": "integer"},
    }
    assert assistant()(context, "What does it do?", Client(), []) == "This function counts vowels."


def test_excessive_context_is_rejected_before_provider_call():
    """Avoid silently sending unbounded files or user input to a model."""
    with pytest.raises(ValueError):
        assistant()(
            {"filename": "x", "source": "x" * 65537, "specification": "", "contract": {}},
            "Explain",
            None,
            [],
        )


def test_provider_exception_is_redacted():
    """SDK error bodies and credentials must not be shown or logged."""

    class Client:
        """Synthetic model boundary; no provider SDK or network."""

        def call(self, messages):
            """Observe the exact request or reproduce a provider failure."""
            raise RuntimeError("secret-api-key")

    with pytest.raises(ValueError, match="could not complete") as error:
        assistant()(
            {"filename": "x.py", "source": "x", "specification": "", "contract": {}},
            "Explain",
            Client(),
            [],
        )
    assert "secret" not in str(error.value)


def test_foreign_session_is_rejected_before_context_access():
    """The helper must not read another browser's candidate or specification."""
    from types import SimpleNamespace

    from test_applications_backend import registry

    from agentix.controllers.applications import ApplicationsBackend
    from agentix.controllers.chathelper import ChatHelperBackend
    from agentix.controllers.sessions import SessionAccessError

    sessions = registry()
    owner = sessions.resolve(None, "alice")
    helper = ChatHelperBackend(sessions, ApplicationsBackend(sessions))
    with pytest.raises(SessionAccessError):
        helper.ask(
            "code",
            "count_words_in_text_code.py",
            "source",
            "Explain",
            owner.token,
            SimpleNamespace(session_hash="bob"),
        )


def test_external_explanation_requires_fresh_remote_consent():
    """A saved provider profile never implicitly authorizes sharing editor content."""
    from agentix.models.model_profiles import ModelProfile, create_profile_llm

    profile = ModelProfile(
        provider="OpenAI",
        model="test-model",
        endpoint="https://api.openai.com/v1",
        credential_ref="synthetic",
        remote_consent=False,
    )
    with pytest.raises(ValueError, match="consent"):
        create_profile_llm(profile, None, resolver=lambda host: ["93.184.216.34"])
