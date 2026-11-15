"""Readable inline code inside Gradio markdown for the maintained dark palette."""

from pathlib import Path


def test_stylesheet_defines_dark_inline_code_colors() -> None:
    """Catch white-on-white inline code such as File, Action and Stored package values."""
    from agentix.ui.branding import stylesheet

    css = stylesheet()
    assert "--code-background-fill:" in css
    assert "--panel-border-color:" in css
    assert ".gradio-container .prose :not(pre) > code" in css
    assert "color: var(--text) !important" in css


def test_stylesheet_hides_collapsed_group_wrappers_while_editing() -> None:
    """Catch Gradio 6 gr-group borders and fill left visible once children are absolute."""
    from agentix.ui.branding import stylesheet

    css = stylesheet()
    rule = ".application-layout-active .form, .application-layout-active .styler,\n"
    assert rule + ".application-layout-active .gr-group {" in css
    assert (
        "border: 0 !important; box-shadow: none !important; background: transparent !important;"
        in css
    )


def test_stylesheet_keeps_edit_surfaces_and_the_color_legend_readable() -> None:
    """Catch a transparent Edit surface, a hidden checkbox or an unstyled legend."""
    from agentix.ui.branding import stylesheet

    css = stylesheet()
    assert (
        ".application-layout-active .application-editable-element {background: transparent !important;}"
        in css
    )
    assert (
        ".application-layout-editing .application-editable-element {overflow: visible !important; "
        "background: var(--block-background-fill, #0b0d11) !important;}" in css
    )
    assert "padding-left: 28px !important;" in css
    assert "border: 2px solid var(--accent) !important;" in css
    assert "appearance: none !important;" in css
    assert (
        ".gradio-container .application-layout-editing input.application-visibility-toggle"
        '[type="checkbox"] {border-color: var(--accent) !important; '
        "background-color: #050608 !important;}" in css
    )
    assert (
        ".gradio-container .application-layout-editing input.application-visibility-toggle:checked"
        '[type="checkbox"] {border-color: var(--accent) !important; '
        "background-color: var(--accent) !important;}" in css
    )
    assert "#application-color-legend {position: absolute; right: 12px; top: 48px;" in css
    assert "width: max-content !important;" in css
    assert "#application-color-legend {position: absolute;" in css
    assert "#generated-application-web {" in css
    assert "#chathelper-file {" in css


def test_stylesheet_keeps_right_tab_sidebars_resizable() -> None:
    """Catch a right sidebar without its own width, inner border or drag handle."""
    from agentix.ui.branding import stylesheet

    css = stylesheet()
    assert "#tools-sidebar,\n#applications-sidebar {" in css
    assert "width: var(--agentix-sidebar-width, 420px) !important;" in css
    assert "#tools-sidebar { --agentix-sidebar-width: 420px; }" in css
    assert "#applications-sidebar { --agentix-sidebar-width: 380px; }" in css
    assert "right: calc(var(--agentix-sidebar-width, 420px) * -1) !important;" in css
    assert "position: absolute !important;" in css
    assert "transform: none !important;" in css
    assert ".agentix-sidebar-resizer {" in css
    assert "#tools-sidebar:not(.open) .agentix-sidebar-resizer," in css


def test_stylesheet_is_the_only_served_asset() -> None:
    """Keep the maintained stylesheet inside the packaged UI assets directory."""
    from agentix.ui import branding

    assert Path(branding.__file__).with_name("assets").joinpath("style.css").is_file()
