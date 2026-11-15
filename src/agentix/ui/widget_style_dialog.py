"""Overlay window that edits one widget's scoped stylesheet from a right-click.

Presentation only: the window collects six values, the backend merges them into
``<tool>_widget.css`` and the review service persists the file. Gradio 6 has no
modal component, so the window is a hidden column positioned by ``style.css``.
"""

from typing import Any

from agentix.widgets.style_editor import FONTS


class WidgetStyleDialog:
    """Hidden overlay bound to one widget stylesheet, opened by the parent bridge."""

    def __init__(self, gr: Any, backend: Any, bind: Any, session_state: Any) -> None:
        """Build the window and wire open, save and cancel; no IO happens here."""
        self._gr = gr
        self.session_state = session_state
        self.backend = backend
        self.tool = gr.Textbox(
            value="",
            elem_classes=["agentix-internal-input"],
            elem_id="applications-widget-style-tool",
        )
        self.open = gr.Button(
            "Edit widget style",
            elem_classes=["agentix-internal-input"],
            elem_id="applications-widget-style-open",
        )
        self.apply = gr.Textbox(
            value="",
            elem_classes=["agentix-internal-input"],
            elem_id="applications-widget-style-apply",
        )
        with gr.Column(visible=False, elem_id="agentix-widget-style-dialog") as container:
            self.container = container
            gr.Markdown("### Widget style", elem_id="agentix-widget-style-title")
            self.status = gr.Markdown("", elem_id="agentix-widget-style-status")
            with gr.Row():
                self.radius = gr.Number(
                    label="Radius (px)",
                    value=0,
                    minimum=0,
                    maximum=64,
                    precision=0,
                    elem_id="agentix-widget-style-radius",
                )
                self.width = gr.Number(
                    label="Border (px)",
                    value=0,
                    minimum=0,
                    maximum=8,
                    precision=0,
                    elem_id="agentix-widget-style-width",
                )
            with gr.Row():
                self.border_color = gr.ColorPicker(
                    label="Border color",
                    value="#5bd9ef",
                    elem_id="agentix-widget-style-border-color",
                )
                self.background = gr.ColorPicker(
                    label="Background",
                    value="#10141c",
                    elem_id="agentix-widget-style-background",
                )
            gr.HTML(
                '<p class="agentix-widget-style-caption">'
                "Value text typed or shown inside the widget</p>"
            )
            with gr.Row():
                self.font_family = gr.Dropdown(
                    label="Value font",
                    choices=list(FONTS),
                    value=FONTS[0],
                    elem_id="agentix-widget-style-font",
                )
                self.font_size = gr.Number(
                    label="Value size (px)",
                    value=16,
                    minimum=8,
                    maximum=72,
                    precision=0,
                    elem_id="agentix-widget-style-size",
                )
            self.field_background = gr.ColorPicker(
                label="Field color",
                value="#10141c",
                elem_id="agentix-widget-style-field",
            )
            gr.HTML('<p class="agentix-widget-style-caption">Caption above the widget</p>')
            with gr.Row():
                self.label_font_family = gr.Dropdown(
                    label="Caption font",
                    choices=list(FONTS),
                    value=FONTS[0],
                    elem_id="agentix-widget-style-label-font",
                )
                self.label_font_size = gr.Number(
                    label="Caption size (px)",
                    value=16,
                    minimum=8,
                    maximum=72,
                    precision=0,
                    elem_id="agentix-widget-style-label-size",
                )
            with gr.Row():
                self.save = gr.Button("Save style", elem_id="agentix-widget-style-save")
                self.cancel = gr.Button("Cancel", elem_id="agentix-widget-style-cancel")
        self.open.click(
            fn=bind(self._opened),
            inputs=[self.tool, session_state],
            outputs=self.outputs(),
            api_name=False,
            show_progress="hidden",
        )
        self.save.click(
            fn=bind(self._saved),
            inputs=[
                self.tool,
                self.radius,
                self.width,
                self.border_color,
                self.background,
                self.font_family,
                self.font_size,
                self.field_background,
                self.label_font_family,
                self.label_font_size,
                session_state,
            ],
            outputs=[self.container, self.status, session_state, self.apply],
            api_name=False,
            show_progress="hidden",
        )
        self.cancel.click(
            fn=self.hide,
            inputs=None,
            outputs=[self.container],
            api_name=False,
            show_progress="hidden",
        )

    def _opened(self, tool: str, token: str | None, request: Any) -> tuple:
        """Reveal the window with the stored values of the right-clicked widget.

        The container output must be an update, not a value: Gradio renders a
        hidden column only when an update makes it visible.
        """
        (
            status,
            radius,
            width,
            border,
            background,
            font,
            size,
            field,
            label_font,
            label_size,
            (token_out),
        ) = self.backend.load(tool, token, request)
        return (
            self._gr.update(visible=True),
            status,
            radius,
            width,
            border,
            background,
            font,
            size,
            field,
            label_font,
            label_size,
            token_out,
        )

    def outputs(self) -> list:
        """Expose the window outputs the open handler fills in one row."""
        return [
            self.container,
            self.status,
            self.radius,
            self.width,
            self.border_color,
            self.background,
            self.font_family,
            self.font_size,
            self.field_background,
            self.label_font_family,
            self.label_font_size,
            self.session_state,
        ]

    def _saved(
        self,
        tool: str,
        radius: float,
        width: float,
        border_color: str,
        background: str,
        font_family: str,
        font_size: float,
        field_background: str,
        label_font_family: str,
        label_font_size: float,
        token: str | None,
        request: Any,
    ) -> tuple:
        """Persist the style, close the window and hand the merged CSS to the bridge.

        A rejected value raises before the update is produced, so the window stays
        open with the user's input instead of closing on a failed save.
        """
        message, token_out, payload = self.backend.save(
            tool,
            radius,
            width,
            border_color,
            background,
            font_family,
            font_size,
            field_background,
            label_font_family,
            label_font_size,
            token,
            request,
        )
        return self._gr.update(visible=False), message, token_out, payload

    def hide(self) -> Any:
        """Close the window; the collected values stay until the next open."""
        return self._gr.update(visible=False)
