"""Reusable explicit confirmation controls for permanent catalog deletion."""

from typing import Any


def build_delete_controls(
    gr: Any,
    backend: Any,
    bind: Any,
    kind: str,
    selected: Any,
    session_state: Any,
    status: Any = None,
    dialog: Any = None,
) -> None:
    """Render prepare/confirm/cancel; all authority remains in the owner controller."""
    if dialog is None:
        from agentix.ui.message_dialog import MessageDialog

        dialog = MessageDialog(gr)
    prefix = "tools" if kind == "tool" else "apps"
    select_message = (
        "Please, select an installed tool."
        if kind == "tool"
        else "Please, select an installed application."
    )
    delete = gr.Button(
        "Delete selected tool" if kind == "tool" else "Delete selected application",
        elem_id=prefix + "-delete",
    )
    notice = status if status is not None else gr.Markdown("", elem_id=prefix + "-delete-status")
    nonce = gr.State(value="")
    with gr.Column(visible=False, elem_id=prefix + "-delete-confirmation") as panel:
        prompt = gr.Markdown("")
        with gr.Row():
            confirm = gr.Button(
                "Confirm permanent deletion", variant="stop", elem_id=prefix + "-delete-confirm"
            )
            cancel = gr.Button("Cancel", elem_id=prefix + "-delete-cancel")

    def prepare(identity: str, token: str | None, request: Any):
        """Display dependency failures without exposing native/storage exception bodies."""
        if not identity:
            return (
                select_message,
                gr.update(visible=False),
                "",
                "",
                token,
                *dialog.show(select_message),
            )
        try:
            message, confirmation, owned = backend.prepare(kind, identity, token, request)
            return message, gr.update(visible=True), message, confirmation, owned, *dialog.skip()
        except ValueError as error:
            return str(error), gr.update(visible=False), "", "", token, *dialog.show(str(error))
        except Exception:
            message = "Deletion unavailable; dependency or storage checks failed."
            return message, gr.update(visible=False), "", "", token, *dialog.show(message)

    def commit(confirmation: str, token: str | None, request: Any):
        """Clear selection after success; failed/stale requests require a new confirmation."""
        try:
            message, owned = backend.confirm(confirmation, token, request)
            choices, owned = backend.choices(kind, owned, request)
            return (
                message,
                gr.update(visible=False),
                "",
                gr.Dropdown(choices=choices, value=None),
                owned,
                *dialog.skip(),
            )
        except ValueError as error:
            return (
                str(error),
                gr.update(visible=False),
                "",
                gr.skip(),
                token,
                *dialog.show(str(error)),
            )
        except Exception:
            message = "Removal failed; authorization may be revoked. Check diagnostics."
            return message, gr.update(visible=False), "", gr.skip(), token, *dialog.show(message)

    def dismiss(confirmation: str, token: str | None, request: Any):
        """Cancel without granting deletion even when a prompt became stale."""
        try:
            message, owned = backend.cancel(confirmation, token, request)
            return message, gr.update(visible=False), "", owned, *dialog.skip()
        except ValueError:
            message = "No current deletion confirmation."
            return message, gr.update(visible=False), "", token, *dialog.show(message)

    delete.click(
        fn=bind(prepare),
        inputs=[selected, session_state],
        outputs=[notice, panel, prompt, nonce, session_state, *dialog.outputs()],
        api_name=False,
    )
    confirm.click(
        fn=bind(commit),
        inputs=[nonce, session_state],
        outputs=[notice, panel, nonce, selected, session_state, *dialog.outputs()],
        api_name=False,
    )
    cancel.click(
        fn=bind(dismiss),
        inputs=[nonce, session_state],
        outputs=[notice, panel, nonce, session_state, *dialog.outputs()],
        api_name=False,
    )
