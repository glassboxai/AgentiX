"""The widget style window edits six declarations and preserves everything else."""

import json
from types import SimpleNamespace

import pytest

ROLE = "words"
SELECTOR = ':where([id^="application_words_"])'


def test_defaults_are_read_from_the_generated_palette():
    """A freshly generated stylesheet opens on documented defaults."""
    from agentix.widgets.style_editor import read_style
    from agentix.widgets.styles import default_widget_css

    values = read_style(default_widget_css(ROLE), ROLE)
    assert (values.radius, values.width) == (0, 0)
    assert values.border_color == "#5bd9ef"
    assert values.background == "#10141c"
    assert values.font_family == "system-ui"
    assert values.font_size == 16


def test_merge_preserves_unmanaged_declarations_and_hover_blocks():
    """Only the six managed declarations change; the rest of the file survives."""
    from agentix.widgets.style_editor import StyleValues, merge_style

    css = (
        f"{SELECTOR} {{ color: #f1f3f5; padding: 4px; font-size: 18px; }}\n"
        f"{SELECTOR}:hover {{ color: #ffffff; }}\n"
    )
    merged = merge_style(css, ROLE, StyleValues(12, 2, "#abcdef", "#10141c", "Arial", 20))
    assert "color: #f1f3f5" in merged
    assert "padding: 4px" in merged
    assert "border-radius: 12px" in merged
    assert "border-width: 2px" in merged
    assert "border-style: solid" in merged
    assert "font-family: Arial" in merged
    assert "font-size: 20px" in merged
    assert f"{SELECTOR}:hover {{ color: #ffffff; }}" in merged
    assert merged.split("\n")[0].count("font-size") == 1


def test_zero_width_never_draws_a_border():
    """A zero width derives ``none`` so the stored file matches what is shown."""
    from agentix.widgets.style_editor import StyleValues, merge_style

    merged = merge_style(
        f"{SELECTOR} {{ color: #f1f3f5; }}\n",
        ROLE,
        StyleValues(0, 0, "#abcdef", "#10141c", "Arial", 16),
    )
    assert "border-style: none" in merged
    assert "border-style: solid" not in merged


def test_merge_creates_the_base_block_when_only_hover_exists():
    """A hover-only file still receives the editable block in front."""
    from agentix.widgets.style_editor import StyleValues, merge_style

    merged = merge_style(
        f"{SELECTOR}:hover {{ color: #ffffff; }}\n",
        ROLE,
        StyleValues(4, 1, "#abcdef", "#10141c", "Arial", 16),
    )
    assert merged.startswith(SELECTOR + " {")
    assert merged.rstrip().endswith("}")


def test_round_trip_returns_the_saved_values():
    """What the window saves is what the window reads back."""
    from agentix.widgets.style_editor import StyleValues, merge_style, read_style
    from agentix.widgets.styles import default_widget_css

    wanted = StyleValues(16, 3, "#123456", "#abcdef", "Georgia", 24)
    merged = merge_style(default_widget_css(ROLE), ROLE, wanted)
    assert read_style(merged, ROLE) == wanted


def test_field_and_caption_values_round_trip():
    """The field box and the caption keep their own colour, family and size."""
    from agentix.widgets.style_editor import StyleValues, merge_style, read_style
    from agentix.widgets.styles import default_widget_css

    wanted = StyleValues(12, 2, "#abcdef", "#10141c", "Arial", 20, "#26177d", "Georgia", 28)
    merged = merge_style(default_widget_css(ROLE), ROLE, wanted)
    assert f"{SELECTOR} input {{ background-color: #26177d }}" in merged
    assert f"{SELECTOR} textarea {{ background-color: #26177d }}" in merged
    assert f"{SELECTOR} label {{ font-family: Georgia; font-size: 28px }}" in merged
    assert read_style(merged, ROLE) == wanted


def test_merge_preserves_unmanaged_field_declarations():
    """A padding already present on the field block survives the rewrite."""
    from agentix.widgets.style_editor import StyleValues, merge_style

    css = (
        f"{SELECTOR} {{ color: #f1f3f5; }}\n{SELECTOR} input {{ padding: 6px; color: #ffffff; }}\n"
    )
    merged = merge_style(
        css, ROLE, StyleValues(0, 0, "#abcdef", "#10141c", "Arial", 16, "#26177d", "Arial", 16)
    )
    assert "padding: 6px" in merged
    assert "background-color: #26177d" in merged


def test_repeated_saves_never_accumulate_duplicate_blocks():
    """A second save replaces the owned blocks instead of appending new ones."""
    from agentix.widgets.style_editor import StyleValues, merge_style
    from agentix.widgets.styles import default_widget_css

    values = StyleValues(12, 2, "#abcdef", "#10141c", "Arial", 20, "#26177d", "Georgia", 28)
    once = merge_style(default_widget_css(ROLE), ROLE, values)
    twice = merge_style(once, ROLE, values)
    assert twice == once
    assert twice.count(f"{SELECTOR} textarea") == 1
    assert twice.count(f"{SELECTOR} input") == 1
    assert twice.count(f"{SELECTOR} label") == 1


def test_field_and_caption_defaults_are_read_from_a_plain_file():
    """A file without inner blocks opens on documented defaults."""
    from agentix.widgets.style_editor import read_style
    from agentix.widgets.styles import default_widget_css

    values = read_style(default_widget_css(ROLE), ROLE)
    assert values.field_background == "#10141c"
    assert values.label_font_family == "system-ui"
    assert values.label_font_size == 16


@pytest.mark.parametrize(
    "values",
    [
        (65, 0, "#abcdef", "#10141c", "Arial", 16),
        (0, 9, "#abcdef", "#10141c", "Arial", 16),
        (0, 0, "red", "#10141c", "Arial", 16),
        (0, 0, "#abcdef", "rgb(1,2,3)", "Arial", 16),
        (0, 0, "#abcdef", "#10141c", "Comic Sans", 16),
        (0, 0, "#abcdef", "#10141c", "Arial", 7),
        (0, 0, "#abcdef", "#10141c", "Arial", 73),
    ],
)
def test_out_of_range_values_are_rejected(values):
    """Bounds are enforced before the grammar sees a declaration."""
    from agentix.widgets.style_editor import StyleValues, merge_style
    from agentix.widgets.styles import default_widget_css

    with pytest.raises(ValueError):
        merge_style(default_widget_css(ROLE), ROLE, StyleValues(*values))


class _Applications:
    """Minimal double: only the two calls the style backend may make."""

    def __init__(self, package, identity):
        self.candidate = SimpleNamespace(package=package, identity=identity)
        self.saved = None

    def owned_candidate(self, token, request):
        """Return the fixture proposal without any session registry."""
        return SimpleNamespace(session_id="fixture", token="token"), None, self.candidate

    def save_file(self, name, text, identity, token, request):
        """Record the persisted member instead of touching a real review."""
        self.saved = (name, text)
        return ("Widget style saved.", "", identity, "", False, "token")


def test_backend_load_returns_the_window_values(tmp_path):
    """The window opens on the stored declarations of the right-clicked widget."""
    from agentix.controllers.widget_style import WidgetStyleBackend
    from agentix.widgets.styles import default_widget_css

    (tmp_path / "words_widget.css").write_text(default_widget_css(ROLE), encoding="utf-8")
    backend = WidgetStyleBackend(_Applications(tmp_path, "identity"))
    row = backend.load(ROLE, None, None)
    assert row[1:] == (
        0,
        0,
        "#5bd9ef",
        "#10141c",
        "system-ui",
        16,
        "#10141c",
        "system-ui",
        16,
        "token",
    )


def test_backend_save_persists_the_merged_stylesheet(tmp_path):
    """Saving delegates to the review service with the merged member text."""
    from agentix.controllers.widget_style import WidgetStyleBackend
    from agentix.widgets.styles import default_widget_css

    (tmp_path / "words_widget.css").write_text(default_widget_css(ROLE), encoding="utf-8")
    applications = _Applications(tmp_path, "identity")
    message, token, payload = WidgetStyleBackend(applications).save(
        ROLE, 12, 2, "#abcdef", "#10141c", "Arial", 20, "#26177d", "Georgia", 28, None, None
    )
    assert (message, token) == ("Widget style saved.", "token")
    assert json.loads(payload) == {
        "tool": ROLE,
        "ids": ["words"],
        "css": applications.saved[1],
    }
    name, text = applications.saved
    assert name == "words_widget.css"
    assert "border-radius: 12px" in text and "color: #f1f3f5" in text


def test_backend_payload_carries_the_widget_instance_ids(tmp_path):
    """The live preview scopes CSS to instance ids, not to the tool role."""
    from schema3_package import package

    from agentix.controllers.widget_style import WidgetStyleBackend

    folder = package(tmp_path)
    assert WidgetStyleBackend._instance_ids(folder, "count_words_in_text") == [
        "count_words_in_text"
    ]
    assert WidgetStyleBackend._instance_ids(folder, "absent_tool") == ["absent_tool"]


def test_backend_rejects_an_unknown_widget(tmp_path):
    """Browser text never becomes a path or an arbitrary member name."""
    from agentix.controllers.widget_style import WidgetStyleBackend

    backend = WidgetStyleBackend(_Applications(tmp_path, "identity"))
    for tool in ("../evil", "Words", "", "a" * 65):
        with pytest.raises(ValueError):
            backend.load(tool, None, None)


def test_save_closes_the_window_on_success():
    """A successful save hides the overlay instead of leaving it open."""
    from agentix.ui.widget_style_dialog import WidgetStyleDialog

    dialog = object.__new__(WidgetStyleDialog)
    dialog._gr = SimpleNamespace(update=lambda **value: ("update", value))
    dialog.backend = SimpleNamespace(
        save=lambda *args: ("Widget style saved.", "token", '{"tool": "words", "css": "x"}')
    )
    container, message, token, payload = dialog._saved(
        ROLE, 4, 1, "#abcdef", "#10141c", "Arial", 16, "#26177d", "Georgia", 28, None, None
    )
    assert container == ("update", {"visible": False})
    assert (message, token) == ("Widget style saved.", "token")
    assert json.loads(payload)["tool"] == ROLE


def test_save_keeps_the_window_open_when_a_value_is_rejected():
    """A rejected value raises before any close update is produced."""
    from agentix.ui.widget_style_dialog import WidgetStyleDialog

    def reject(*args):
        """Refuse the write the way the review service does."""
        raise ValueError("Border radius must be a whole number between 0 and 64")

    dialog = object.__new__(WidgetStyleDialog)
    dialog._gr = SimpleNamespace(update=lambda **value: ("update", value))
    dialog.backend = SimpleNamespace(save=reject)
    with pytest.raises(ValueError):
        dialog._saved(
            ROLE, 99, 1, "#abcdef", "#10141c", "Arial", 16, "#26177d", "Georgia", 28, None, None
        )
