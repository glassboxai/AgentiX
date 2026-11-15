"""Modal message dialog contract: persistent until the user presses Ok."""

from types import SimpleNamespace


def _build_dialog():
    """Construct the dialog with the real Gradio module inside a Blocks context."""
    import gradio as gr

    from agentix.ui.message_dialog import MessageDialog

    with gr.Blocks():
        dialog = MessageDialog(gr)
    return dialog, gr


def test_dialog_starts_hidden_and_toggles_with_ok():
    """The window is hidden by default, shows one message and closes with Ok."""
    dialog, gr = _build_dialog()
    assert dialog.container.visible is False
    update, text = dialog.show("Changes saved.")
    assert update["visible"] is True
    assert text == "Changes saved."
    assert dialog.hide()["visible"] is False
    skipped = dialog.skip()
    skip_type = type(gr.skip())
    assert all(type(item) is skip_type for item in skipped)


def test_stream_wrapper_passes_rows_through_and_routes_validation_errors_to_modal():
    """Successful streams gain skipped dialog outputs; ValueError opens the modal."""
    dialog, gr = _build_dialog()

    def success():
        """Yield one ordinary six-output row."""
        yield ("status", "review", "identity", "frame", False, "token")

    rows = list(dialog.wrap_stream(success, 6)())
    skip_type = type(gr.skip())
    assert rows[0][:6] == ("status", "review", "identity", "frame", False, "token")
    assert all(type(item) is skip_type for item in rows[0][6:])

    def invalid():
        """Raise the same validation error the name check raises."""
        raise ValueError("Application name must contain 1 to 100 characters")
        yield

    rows = list(dialog.wrap_stream(invalid, 6)())
    assert len(rows) == 1
    row = rows[0]
    assert row[0] == "Application name must contain 1 to 100 characters"
    assert all(type(item) is skip_type for item in row[1:6])
    assert row[6]["visible"] is True
    assert row[7] == "Application name must contain 1 to 100 characters"


def test_result_wrapper_shows_status_message_in_modal_and_errors_too():
    """Save confirmations and validation errors persist in the modal until Ok."""
    dialog, gr = _build_dialog()

    def saved(*args):
        """Return the ordinary six-output save tuple."""
        return ("Changes saved. Review the updated files.", "review", "identity", "", False, "t")

    row = dialog.wrap_result(saved, 6)("name", "text")
    assert row[:6] == (
        "Changes saved. Review the updated files.",
        "review",
        "identity",
        "",
        False,
        "t",
    )
    assert row[6]["visible"] is True
    assert row[7] == "Changes saved. Review the updated files."

    def invalid(*args):
        """Raise a validation error instead of returning a row."""
        raise ValueError("No proposal is available")

    row = dialog.wrap_result(invalid, 6)("name", "text")
    assert row[0] == "No proposal is available"
    assert all(type(item) is type(gr.skip()) for item in row[1:6])
    assert row[6]["visible"] is True
    assert row[7] == "No proposal is available"


def test_guard_result_passes_success_through_and_routes_errors_to_modal():
    """Ordinary results keep the dialog hidden; ValueError opens the modal."""
    dialog, gr = _build_dialog()

    def saved(*args):
        """Return an ordinary two-output row."""
        return ("ok", "token")

    row = dialog.guard_result(saved, 2)("a")
    assert row[:2] == ("ok", "token")
    assert all(type(item) is type(gr.skip()) for item in row[2:])

    def silent(*args):
        """Return nothing, as discard-style approval callbacks do."""
        return None

    row = dialog.guard_result(silent, 0)("a")
    assert len(row) == 2
    assert all(type(item) is type(gr.skip()) for item in row)

    def scalar(*args):
        """Return one plain string, as status-only backends do."""
        return "Catalog is busy; retry later"

    row = dialog.guard_result(scalar, 1)("a")
    assert row[0] == "Catalog is busy; retry later"
    assert all(type(item) is type(gr.skip()) for item in row[1:])

    def invalid(*args):
        """Raise a validation error instead of returning a row."""
        raise ValueError("Select an installed application")

    row = dialog.guard_result(invalid, 2)("a")
    assert row[0] == "Select an installed application"
    assert type(row[1]) is type(gr.skip())
    assert row[2]["visible"] is True
    assert row[3] == "Select an installed application"

    row = dialog.guard_result(invalid, 0)("a")
    assert len(row) == 2
    assert row[0]["visible"] is True
    assert row[1] == "Select an installed application"


def test_guard_history_appends_the_dialog_pair_on_success_and_on_error():
    """Both branches must reach the declared output count; only errors empty the history."""
    dialog, gr = _build_dialog()
    skip_type = type(gr.skip())
    expected = 7 + len(dialog.outputs())

    def poll(token, request):
        """Return the seven outputs the Tools poll backend produces."""
        return (
            [{"role": "assistant", "content": "live"}],
            gr.update(visible=False),
            "No pending approval requests.",
            gr.update(),
            "catalog",
            "",
            "token",
        )

    row = dialog.guard_history(poll, 7, 0)(None, None)
    assert len(row) == expected
    assert row[0] == [{"role": "assistant", "content": "live"}]
    assert row[6] == "token"
    assert all(type(item) is skip_type for item in row[7:])

    def rejected(token, request):
        """Raise the ownership diagnostic the guard exists for."""
        raise ValueError("Session token is not owned by this browser")

    row = dialog.guard_history(rejected, 7, 0)(None, None)
    assert len(row) == expected
    assert row[0] == []
    assert all(type(item) is skip_type for item in row[1:7])
    assert row[7]["visible"] is True
    assert row[8] == "Session token is not owned by this browser"


def test_wrappers_preserve_the_handler_signature_for_request_injection():
    """Wrapped handlers keep their signature so Gradio still injects the Request slot."""
    import inspect

    from gradio import helpers

    dialog, gr = _build_dialog()

    def handler(message, token, request):
        """Plain handler shaped like a session-owned backend method."""
        return (token,)

    def streaming(message, token, request):
        """Streaming handler shaped like a generating backend method."""
        yield (token,)

    assert inspect.isgeneratorfunction(dialog.wrap_stream(streaming, 1))
    for wrapped in (
        dialog.wrap_result(handler, 1),
        dialog.guard_result(handler, 1),
        dialog.wrap_stream(streaming, 1),
    ):
        inputs, *_ = helpers.special_args(wrapped, inputs=["x", "t"])
        assert len(inputs) == 3


def test_guard_result_rejects_streaming_handlers():
    """Generators must use wrap_stream; guard_result fails loudly instead of corrupting outputs."""
    dialog, gr = _build_dialog()

    def streaming():
        """Stand-in for a streaming backend handler."""
        yield ("status", "frame", "token")

    wrapped = dialog.guard_result(streaming, 3)
    try:
        wrapped()
    except TypeError as error:
        assert "wrap_stream" in str(error)
    else:
        raise AssertionError("guard_result must reject generator handlers")


def test_wrappers_preserve_the_wrapped_signature_for_request_injection():
    """The shell's bind rewrites request annotations; wrappers must expose them."""
    import inspect
    from typing import Any

    dialog, gr = _build_dialog()

    def handler(name: str, query: str, token: str | None, request: Any) -> tuple:
        """Stand-in with the same parameter names as a bound backend method."""
        return ("status", "review", "identity", "", False, "t")

    for wrapper in (
        dialog.wrap_stream(handler, 6),
        dialog.wrap_result(handler, 6),
    ):
        parameters = inspect.signature(wrapper).parameters
        assert list(parameters) == ["name", "query", "token", "request"]
        assert parameters["request"].annotation is Any


def test_stream_final_wrapper_opens_modal_only_with_the_last_status():
    """Intermediate rows leave the dialog untouched; the final status opens it."""
    dialog, gr = _build_dialog()

    def progress():
        """Yield two ordinary rows, the last carrying the visible status."""
        yield ("Checking gates", "", "token")
        yield ("Verification failed: review the incident", "", "token")

    rows = list(dialog.wrap_stream_final(progress, 3)())
    skip_type = type(gr.skip())
    assert len(rows) == 2
    assert rows[0][:3] == ("Checking gates", "", "token")
    assert all(type(item) is skip_type for item in rows[0][3:])
    assert rows[1][:3] == ("Verification failed: review the incident", "", "token")
    assert rows[1][3]["visible"] is True
    assert rows[1][4] == "Verification failed: review the incident"

    def empty_status():
        """Yield rows whose final status is empty; no empty modal may open."""
        yield ("working", "", "token")
        yield ("", "content", "token")

    rows = list(dialog.wrap_stream_final(empty_status, 3)())
    assert all(type(item) is skip_type for item in rows[-1][3:])

    def invalid():
        """Raise after progress; the pending row flushes before the modal error."""
        yield ("Checking gates", "", "token")
        raise ValueError("Select an installed application")

    rows = list(dialog.wrap_stream_final(invalid, 3)())
    assert len(rows) == 2
    assert rows[0][:3] == ("Checking gates", "", "token")
    assert all(type(item) is skip_type for item in rows[0][3:])
    assert rows[1][0] == "Select an installed application"
    assert rows[1][3]["visible"] is True
    assert rows[1][4] == "Select an installed application"


def test_result_wrapper_can_mirror_a_custom_status_position():
    """Composite results open the modal with the message at the chosen index."""
    dialog, gr = _build_dialog()

    def computed(*args):
        """Return typed results followed by visibility, status and ownership."""
        return (1, 2, gr.update(visible=False), gr.update(visible=False), "Completed", "token")

    row = dialog.wrap_result(computed, 6, status_index=4)("input")
    assert row[:5] == (1, 2, gr.update(visible=False), gr.update(visible=False), "Completed")
    assert row[6]["visible"] is True
    assert row[7] == "Completed"


def test_sidebar_starts_closed():
    """The shared model sidebar is collapsed at startup for a cleaner first view."""
    created = []

    class Component:
        """Record constructor kwargs and absorb event bindings."""

        def __init__(self, *args, **kwargs):
            self.kwargs = kwargs
            created.append(self)

        def __enter__(self):
            return self

        def __exit__(self, *args):
            return False

        def __getattr__(self, name):
            def event(**kwargs):
                return self

            return event

    gr = SimpleNamespace(
        **{
            name: Component
            for name in (
                "Sidebar",
                "Accordion",
                "Dropdown",
                "Textbox",
                "Button",
                "Row",
                "Checkbox",
                "Markdown",
                "InputHTMLAttributes",
                "State",
            )
        }
    )

    class DialogStub:
        """Absorb dialog wrapping without building real modal components."""

        def guard_result(self, fn, size):
            return fn

        def outputs(self):
            return []

    from agentix.ui.sidebar import build_sidebar

    build_sidebar(
        gr,
        Component(),
        SimpleNamespace(reset_generation_identity=lambda *args: ()),
        lambda fn: fn,
        Component(),
        None,
        DialogStub(),
    )
    sidebar = next(item for item in created if item.kwargs.get("elem_id") == "agentix-sidebar")
    assert sidebar.kwargs["open"] is False
