"""Gradio view with server-owned sessions and browser-snapshot approval IDs."""

import functools
import inspect
from dataclasses import dataclass
from typing import Any

from .branding import header, launch_options
from .sessions import SessionCallbacks, SessionRegistry


@dataclass(frozen=True)
class View:
    """Constructed Blocks object and launch-time theme, without a running server."""

    demo: Any
    theme: Any


def build_view(sessions: SessionRegistry, gradio_module: Any = None) -> View:
    """Build widgets/bindings on demand; importing this module never loads Gradio."""
    if gradio_module is None:
        import gradio as gradio_module
    gr = gradio_module
    callbacks = SessionCallbacks(sessions)

    def bind(method: Any, *, discard_result: bool = False) -> Any:
        """Tell Gradio to inject Request instead of treating it as a user input."""

        @functools.wraps(method)
        def callback(*args: Any, **kwargs: Any) -> Any:
            """Dispatch only after the session callback checks token ownership."""
            result = method(*args, **kwargs)
            return None if discard_result else result

        callback.__annotations__ = dict(method.__annotations__, request=gr.Request)
        signature = inspect.signature(method)
        callback.__signature__ = signature.replace(
            parameters=[
                parameter.replace(annotation=gr.Request)
                if parameter.name == "request"
                else parameter
                for parameter in signature.parameters.values()
            ]
        )
        return callback

    theme = gr.themes.Base(
        primary_hue="cyan",
        secondary_hue="slate",
        font=["Inter", "Arial", "sans-serif"],
        font_mono=["Inter", "Arial", "sans-serif"],
    )

    with gr.Blocks(title="AgentiX", fill_width=True) as demo:
        # State values stay on the server; client submissions cannot choose owners.
        session_state = gr.State(
            value=None, time_to_live=1800, delete_callback=sessions.close_state
        )
        # The clicked ID must travel with the browser's displayed editor snapshot.
        # Mutable server State could otherwise relabel a queued stale click.
        # This identifier is not a secret; server ownership/expiry checks remain mandatory.
        request_state = gr.Textbox(value="", visible=False, interactive=False)
        gr.HTML(header())

        with gr.Sidebar(label="Model settings", width=390, open=True, elem_id="agentix-sidebar"):
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
                    label="Profile name", elem_id="profile-name", max_length=64
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
        with gr.Row(elem_id="agentix-workspace"):
            # ----------------------------------------------------------------------
            # LEFT COLUMN: Conversational Chat
            # ----------------------------------------------------------------------
            with gr.Column(scale=3):
                chatbot = gr.Chatbot(
                    label="Conversation", height=580, elem_id="agentix-chat", buttons=[]
                )
                with gr.Row(elem_id="query-composer"):
                    msg_input = gr.Textbox(
                        placeholder="Enter your calculation or query here...",
                        label="User Query",
                        lines=2,
                        scale=4,
                    )
                    submit_btn = gr.Button(
                        "Send query", variant="primary", scale=0, min_width=46, elem_id="send-query"
                    )

            # ----------------------------------------------------------------------
            # RIGHT COLUMN: Security Sandbox & Catalog
            # ----------------------------------------------------------------------
            with gr.Column(scale=2):
                with gr.Accordion("Installed Tools Catalog", open=True):
                    catalog_display = gr.Markdown(value="Catalog loads for the current session.")
                validation_display = gr.Markdown(
                    "### Tool validation\n\nNo validation started.", elem_id="validation-panel"
                )
                with gr.Accordion("Authorization & Test Review", open=True):
                    auto_approve_check = gr.Checkbox(
                        label="Auto-approve file writes for this session",
                        value=False,
                        info="If checked, file writes within generated_tools/ are authorized automatically.",
                    )

                    # Interactive Approval Panel with Editable Text Box
                    with gr.Group(visible=False, elem_id="authorization-review") as approval_group:
                        gr.Markdown("### Authorization & Review Required")
                        pending_info = gr.Markdown("No pending approval requests.")
                        preview_box = gr.TextArea(
                            label="Review and edit file content or acceptance cases before approving",
                            lines=14,
                            interactive=True,  # Enables manual editing
                        )
                        with gr.Row():
                            approve_btn = gr.Button("Approve Reviewed Content", variant="primary")
                            reject_btn = gr.Button("Reject Operation", variant="stop")

        # --------------------------------------------------------------------------
        # EVENT BINDINGS
        # --------------------------------------------------------------------------
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

        def refresh_local(
            selected_endpoint: str, token: str | None, request: Any
        ) -> tuple[Any, ...]:
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
                fn=bind(profile_action),
                inputs=[gr.State(value=action), *profile_inputs],
                outputs=profile_outputs,
                api_name=False,
            )
        profile_choice.input(
            fn=bind(profile_action),
            inputs=[gr.State(value="select"), *profile_inputs],
            outputs=profile_outputs,
            api_name=False,
        )
        demo.load(
            fn=bind(profile_action),
            inputs=[gr.State(value="refresh"), *profile_inputs],
            outputs=profile_outputs,
            api_name=False,
        )
        refresh_models.click(
            fn=bind(refresh_local),
            inputs=[endpoint, session_state],
            outputs=[model_name, model_status, session_state],
            api_name=False,
        )

        demo.load(
            fn=bind(refresh_local),
            inputs=[endpoint, session_state],
            outputs=[model_name, model_status, session_state],
            api_name=False,
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
            fn=bind(apply_selected),
            inputs=[
                provider,
                model_name,
                external_model,
                endpoint,
                api_key,
                remote_consent,
                session_state,
            ],
            outputs=[api_key, model_status, session_state],
            api_name=False,
        )
        auto_approve_check.change(
            fn=bind(callbacks.toggle),
            inputs=[auto_approve_check, session_state],
            outputs=[session_state],
        )
        submit_btn.click(
            fn=bind(callbacks.submit),
            inputs=[msg_input, session_state],
            outputs=[msg_input, chatbot, session_state],
        )
        msg_input.submit(
            fn=bind(callbacks.submit),
            inputs=[msg_input, session_state],
            outputs=[msg_input, chatbot, session_state],
        )
        approve_btn.click(
            fn=bind(callbacks.approve, discard_result=True),
            inputs=[preview_box, request_state, session_state],
            outputs=None,
        )
        reject_btn.click(
            fn=bind(callbacks.reject, discard_result=True),
            inputs=[request_state, session_state],
            outputs=None,
        )
        status_timer = gr.Timer(value=1.0)
        status_timer.tick(
            fn=bind(callbacks.poll),
            inputs=[session_state],
            outputs=[
                chatbot,
                approval_group,
                pending_info,
                preview_box,
                catalog_display,
                request_state,
                session_state,
            ],
        )
        status_timer.tick(
            fn=bind(callbacks.validation_status),
            inputs=[session_state],
            outputs=[validation_display],
        )

    # Request is framework-injected; unload callbacks take no browser inputs.
    demo.unload(fn=bind(callbacks.unload))
    return View(demo, theme)


def launch(view: View, *, server_port: int = 7860, open_browser: bool = True) -> None:
    """Start the existing queued loopback UI and open the browser."""
    view.demo.queue().launch(
        server_name="127.0.0.1",
        server_port=server_port,
        theme=view.theme,
        inbrowser=open_browser,
        **launch_options(),
    )
