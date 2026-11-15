"""Reusable modal message window: one persistent message with an Ok close button.

Presentation only: the dialog never changes backend behavior, it replaces
ephemeral native notifications with an explicit user-dismissed window.
"""

import functools
import inspect
from collections.abc import Callable, Iterator
from typing import Any


class MessageDialog:
    """Modal window bound to a message text and an Ok button, hidden by default."""

    def __init__(self, gr: Any) -> None:
        """Build the hidden window and wire Ok to close it; styling lives in style.css."""
        self._gr = gr
        with gr.Column(visible=False, elem_id="agentix-message-dialog") as container:
            self.container = container
            self.message = gr.Markdown("", elem_id="agentix-message-text")
            self.ok = gr.Button("Ok", elem_id="agentix-message-ok")
        self.ok.click(
            fn=self.hide,
            inputs=None,
            outputs=[self.container],
            api_name=False,
            show_progress="hidden",
        )

    def outputs(self) -> list:
        """Expose the output pair other handlers append to their output lists."""
        return [self.container, self.message]

    def show(self, text: str) -> tuple:
        """Return updates that open the window displaying the given message."""
        return self._gr.update(visible=True), text

    def hide(self) -> Any:
        """Close the window; the message text is retained but never visible."""
        return self._gr.update(visible=False)

    def skip(self) -> tuple:
        """Leave the dialog untouched inside another handler's output row."""
        return self._gr.skip(), self._gr.skip()

    def wrap_stream(self, handler: Callable, size: int) -> Callable:
        """Append dialog outputs to a streaming handler; show ValueError in the modal."""

        @functools.wraps(handler)
        def stream(*args: Any) -> Iterator[tuple]:
            """Pass ordinary rows through; validation errors become a persistent modal."""
            try:
                for row in handler(*args):
                    yield (*row, *self.skip())
            except ValueError as error:
                yield (str(error), *[self._gr.skip()] * (size - 1), *self.show(str(error)))

        return stream

    def wrap_stream_final(self, handler: Callable, size: int, status_index: int = 0) -> Callable:
        """Stream rows untouched; open the modal with the final row's status text."""

        @functools.wraps(handler)
        def stream(*args: Any) -> Iterator[tuple]:
            """Hold one row back so only the stream's last status opens the modal."""
            held = None
            try:
                for row in handler(*args):
                    if held is not None:
                        yield (*held, *self.skip())
                    held = row
            except ValueError as error:
                if held is not None:
                    yield (*held, *self.skip())
                yield (str(error), *[self._gr.skip()] * (size - 1), *self.show(str(error)))
                return
            if held is None:
                return
            text = held[status_index]
            if isinstance(text, str) and text:
                yield (*held, *self.show(text))
            else:
                yield (*held, *self.skip())

        return stream

    def wrap_result(self, handler: Callable, size: int, status_index: int = 0) -> Callable:
        """Append dialog outputs to one plain result; its status message opens the modal."""

        @functools.wraps(handler)
        def call(*args: Any) -> tuple:
            """Mirror the status text into the modal; validation errors open it too."""
            try:
                row = handler(*args)
            except ValueError as error:
                return (str(error), *[self._gr.skip()] * (size - 1), *self.show(str(error)))
            return (*row, *self.show(row[status_index]))

        return call

    def guard_result(self, handler: Callable, size: int) -> Callable:
        """Append dialog outputs to one plain result; only validation errors open the modal."""

        @functools.wraps(handler)
        def call(*args: Any) -> tuple:
            """Pass ordinary rows through untouched; ValueError becomes a persistent modal."""
            try:
                row = handler(*args)
            except ValueError as error:
                head = (str(error), *[self._gr.skip()] * (size - 1)) if size else ()
                return (*head, *self.show(str(error)))
            if inspect.isgenerator(row):
                raise TypeError(
                    "Streaming handlers must be wired with wrap_stream, not guard_result"
                )
            if row is None:
                values = ()
            elif isinstance(row, (tuple, list)):
                values = tuple(row)
            else:
                values = (row,)
            return (*values, *self.skip())

        return call

    def guard_history(self, handler: Callable, size: int, history_index: int) -> Callable:
        """Keep a rejected row renderable by emptying the Chatbot history output.

        Gradio postprocesses every output before the error reaches the browser, so a
        stale or foreign session token would otherwise surface as a Chatbot format
        error instead of the ownership diagnostic. ``size`` counts the handler's own
        outputs; the dialog pair is appended here.
        """

        @functools.wraps(handler)
        def call(*args: Any) -> tuple:
            """Append the dialog pair; on ValueError empty the history and open the modal."""
            try:
                row = handler(*args)
            except ValueError as error:
                values = [self._gr.skip()] * size
                values[history_index] = []
                return (*values, *self.show(str(error)))
            return (*row, *self.skip())

        return call
