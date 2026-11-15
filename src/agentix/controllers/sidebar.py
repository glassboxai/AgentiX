"""Shared sidebar model/profile backend, independent of tab rendering and Gradio."""

from typing import Any

from agentix.controllers.session_access import SessionOwnerAccess


class SidebarBackend(SessionOwnerAccess):
    """Delegate owner-checked provider/profile operations to protected services."""

    def configure_model(
        self,
        provider: str,
        model: str,
        endpoint: str,
        key: str,
        consent: bool,
        token: str | None,
        request: Any,
    ) -> tuple[str, str, str]:
        """Verify browser ownership; clear the key input on both success and failure."""
        session = self._session(token, request)
        try:
            status = session.controller.configure_model(provider, model, endpoint, key, consent)
        except Exception:
            status = "Model configuration was not applied. Check the provider, key, consent and pending operation/review."
        return "", status, session.token

    def model_menu(
        self,
        action: str,
        identity: str,
        name: str,
        provider: str,
        model: str,
        endpoint: str,
        key: str,
        token: str | None,
        request: Any,
    ) -> tuple[Any, ...]:
        """Dispatch fixed profile actions after owner checks; never return secrets."""
        session = self._session(token, request)
        return (
            *session.controller.profile_action(
                action, identity, name, provider, model, endpoint, key
            ),
            session.token,
        )

    def refresh_models(
        self, endpoint: str, token: str | None, request: Any
    ) -> tuple[list[str], str, str]:
        """Read only the local Ollama catalog after checking the browser owner."""
        from agentix.models.model_profiles import installed_models

        session = self._session(token, request)
        try:
            configuration = session.controller.model_configuration
            reader = configuration.catalog_reader if configuration is not None else None
            names = installed_models(endpoint, reader)
            status = "Installed Ollama models refreshed."
            if "qwen3-coder:30b" not in names:
                status += " Default qwen3-coder:30b is not installed; no download was started."
        except Exception:
            names = []
            status = "Could not read installed models. Check the local Ollama endpoint and service."
        return names, status, session.token

    def inspect_generation_identity(
        self, model: str, endpoint: str, token: str | None, request: Any
    ) -> tuple[str, str, str]:
        """Read a nonsecret local model digest without changing its trusted baseline."""
        from agentix.models.generation_identity import read_generation_identity
        from agentix.models.model_profiles import ModelProfile

        session = self._session(token, request)
        try:
            digest = read_generation_identity(ModelProfile(model=model, endpoint=endpoint))
            return (
                digest,
                f"Generation identity: {model} / {digest}. A local digest baseline is change detection, not authenticity proof.",
                session.token,
            )
        except ValueError:
            return (
                "",
                "Could not read the local model identity. Check the selected model and endpoint.",
                session.token,
            )

    def reset_generation_identity(self, token: str | None, request: Any) -> tuple[str, str]:
        """Explicitly replace a saved local profile's trusted generation baseline."""
        session = self._session(token, request)
        try:
            digest = session.controller.model_configuration.reset_generation_identity()
            return f"Trusted generation identity reset to {digest}.", session.token
        except Exception:
            return (
                "Generation identity was not reset. Apply a saved local profile before resetting its baseline.",
                session.token,
            )
