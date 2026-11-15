"""Shared model sidebar, composed once outside the tab container."""

from typing import Any

SIDEBAR_WIDTH_PIXELS = 390
PROFILE_NAME_MAX_LENGTH = 64
PROFILE_OUTPUT_COUNT = 10
REFRESH_OUTPUT_COUNT = 3
GENERATION_OUTPUT_COUNT = 3
RESET_OUTPUT_COUNT = 2
APPLY_OUTPUT_COUNT = 3


def build_sidebar(
    gr: Any,
    demo: Any,
    callbacks: Any,
    bind: Any,
    session_state: Any,
    progress: Any = None,
    dialog: Any = None,
) -> None:
    """Render persistent session model settings and bind secure profile operations."""
    operation = (
        {"show_progress": "full", "show_progress_on": progress} if progress is not None else {}
    )
    if dialog is None:
        from agentix.ui.message_dialog import MessageDialog

        dialog = MessageDialog(gr)
    with gr.Sidebar(
        label="Model settings", width=SIDEBAR_WIDTH_PIXELS, open=False, elem_id="agentix-sidebar"
    ):
        with gr.Accordion("Model configuration", open=True):
            provider = gr.Dropdown(
                ["Ollama", "OpenAI", "OpenAI-compatible"],
                value="Ollama",
                label="LLM provider",
                elem_id="llm-provider",
            )
            profile_choice = gr.Dropdown(
                choices=[("New profile", "")],
                value="",
                label="Saved profiles",
                elem_id="saved-profiles",
            )
            profile_name = gr.Textbox(
                label="Profile name", elem_id="profile-name", max_length=PROFILE_NAME_MAX_LENGTH
            )
            model_name = gr.Dropdown(
                choices=["qwen3-coder:30b"],
                value="qwen3-coder:30b",
                allow_custom_value=True,
                label="Model",
                elem_id="llm-model",
            )
            external_model = gr.Textbox(
                label="External model", value="", visible=False, elem_id="external-model"
            )
            refresh_models = gr.Button("Refresh models", elem_id="refresh-models")
            inspect_generation = gr.Button(
                "Inspect generation identity", elem_id="inspect-generation-identity"
            )
            generation_digest = gr.Textbox(
                label="Trusted generation digest", interactive=False, elem_id="generation-digest"
            )
            reset_generation = gr.Button(
                "Reset trusted generation identity", elem_id="reset-generation-identity"
            )
            endpoint = gr.Textbox(
                value="http://127.0.0.1:11434", label="API endpoint", elem_id="llm-endpoint"
            )
            api_key = gr.Textbox(
                label="API key",
                type="password",
                value="",
                visible=False,
                elem_id="llm-api-key",
                html_attributes=gr.InputHTMLAttributes(autocomplete="off", spellcheck=False),
            )
            remote_consent = gr.Checkbox(
                label="Allow sending task content to the selected external provider",
                value=False,
                elem_id="llm-remote-consent",
                visible=False,
            )
            with gr.Row():
                save_profile = gr.Button("Save profile", elem_id="save-profile")
                delete_profile = gr.Button("Delete selected profile", elem_id="delete-profile")
            refresh_profiles = gr.Button("Refresh saved profiles", elem_id="refresh-profiles")
            apply_model = gr.Button("Apply model", elem_id="apply-model")
            model_status = gr.Markdown(
                "Default: Ollama / qwen3-coder:30b. Remote providers require consent and a key.",
                elem_id="model-status",
            )
            gr.Markdown(
                "Saved keys are protected by Windows Credential Manager for your Windows user and this PC. They persist until you explicitly delete the profile. Keys are never displayed again. Save external settings before applying them; activation requires consent in this session."
            )

    def provider_defaults(choice: str) -> tuple[Any, ...]:
        """Separate installed local choices from explicit external model names."""
        local = choice == "Ollama"
        return (
            gr.Dropdown(value="qwen3-coder:30b" if local else None, visible=local),
            "http://127.0.0.1:11434"
            if local
            else ("https://api.openai.com/v1" if choice == "OpenAI" else ""),
            gr.Textbox(value="", visible=not local),
            gr.Button(visible=local),
            gr.Checkbox(value=False, visible=not local),
            gr.Textbox(value="", visible=not local),
        )

    provider.input(
        fn=provider_defaults,
        inputs=[provider],
        outputs=[model_name, endpoint, external_model, refresh_models, remote_consent, api_key],
        api_name=False,
    )

    def profile_action(
        action: str,
        identity: str,
        name: str,
        selected_provider: str,
        selected_model: str,
        selected_external_model: str,
        selected_endpoint: str,
        key: str,
        token: str | None,
        request: Any,
    ) -> tuple[Any, ...]:
        """Translate owned profile results into a dropdown update without key data."""
        result = callbacks.model_menu(
            action,
            identity,
            name,
            selected_provider,
            selected_model if selected_provider == "Ollama" else selected_external_model,
            selected_endpoint,
            key,
            token,
            request,
        )
        local = result[3] == "Ollama"
        return (
            gr.Dropdown(choices=result[0], value=result[1]),
            result[2],
            result[3],
            gr.Dropdown(value=result[4] if local else None, visible=local),
            gr.Textbox(value="" if local else result[4], visible=not local),
            result[5],
            gr.Textbox(value="", visible=not local),
            gr.Checkbox(value=False, visible=not local),
            result[8],
            result[9],
        )

    def refresh_local(selected_endpoint: str, token: str | None, request: Any) -> tuple[Any, ...]:
        """Refresh installed names without automatically changing the active model."""
        names, status, owned_token = callbacks.refresh_models(selected_endpoint, token, request)
        return gr.Dropdown(choices=names, allow_custom_value=True), status, owned_token

    profile_inputs = [
        profile_choice,
        profile_name,
        provider,
        model_name,
        external_model,
        endpoint,
        api_key,
        session_state,
    ]
    profile_outputs = [
        profile_choice,
        profile_name,
        provider,
        model_name,
        external_model,
        endpoint,
        api_key,
        remote_consent,
        model_status,
        session_state,
    ]
    for button, action in (
        (save_profile, "save"),
        (delete_profile, "delete"),
        (refresh_profiles, "refresh"),
    ):
        button.click(
            fn=bind(dialog.guard_result(profile_action, PROFILE_OUTPUT_COUNT)),
            inputs=[gr.State(value=action), *profile_inputs],
            outputs=[*profile_outputs, *dialog.outputs()],
            api_name=False,
            **operation,
        )
    profile_choice.input(
        fn=bind(dialog.guard_result(profile_action, 10)),
        inputs=[gr.State(value="select"), *profile_inputs],
        outputs=[*profile_outputs, *dialog.outputs()],
        api_name=False,
    )
    demo.load(
        fn=bind(dialog.guard_result(profile_action, 10)),
        inputs=[gr.State(value="load"), *profile_inputs],
        outputs=[*profile_outputs, *dialog.outputs()],
        api_name=False,
        show_progress="hidden",
    )
    refresh_models.click(
        fn=bind(dialog.guard_result(refresh_local, REFRESH_OUTPUT_COUNT)),
        inputs=[endpoint, session_state],
        outputs=[model_name, model_status, session_state, *dialog.outputs()],
        api_name=False,
        **operation,
    )

    def inspect_local_generation(
        selected_model: str, selected_endpoint: str, token: str | None, request: Any
    ) -> tuple[Any, ...]:
        """Display an inspected digest without persisting trust or activating a model."""
        digest, status, owned_token = callbacks.inspect_generation_identity(
            selected_model, selected_endpoint, token, request
        )
        return digest, status, owned_token

    inspect_generation.click(
        fn=bind(dialog.guard_result(inspect_local_generation, GENERATION_OUTPUT_COUNT)),
        inputs=[model_name, endpoint, session_state],
        outputs=[generation_digest, model_status, session_state, *dialog.outputs()],
        api_name=False,
        **operation,
    )

    reset_generation.click(
        fn=bind(dialog.guard_result(callbacks.reset_generation_identity, RESET_OUTPUT_COUNT)),
        inputs=[session_state],
        outputs=[model_status, session_state, *dialog.outputs()],
        api_name=False,
        **operation,
    )

    demo.load(
        fn=bind(dialog.guard_result(refresh_local, REFRESH_OUTPUT_COUNT)),
        inputs=[endpoint, session_state],
        outputs=[model_name, model_status, session_state, *dialog.outputs()],
        api_name=False,
        show_progress="hidden",
    )

    def apply_selected(
        selected_provider: str,
        local_model: str,
        remote_model: str,
        selected_endpoint: str,
        key: str,
        consent: bool,
        token: str | None,
        request: Any,
    ) -> tuple[str, str, str]:
        """Activate only the model field appropriate to the selected provider."""
        return callbacks.configure_model(
            selected_provider,
            local_model if selected_provider == "Ollama" else remote_model,
            selected_endpoint,
            key,
            consent,
            token,
            request,
        )

    apply_model.click(
        fn=bind(dialog.guard_result(apply_selected, APPLY_OUTPUT_COUNT)),
        inputs=[
            provider,
            model_name,
            external_model,
            endpoint,
            api_key,
            remote_consent,
            session_state,
        ],
        outputs=[api_key, model_status, session_state, *dialog.outputs()],
        api_name=False,
        **operation,
    )
