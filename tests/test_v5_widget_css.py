"""Per-widget styles are reviewed local data, never external resource loaders."""

import pytest


def validator():
    """Fail observably until the maintained scoped-style boundary exists."""
    try:
        from agentix.widgets.styles import validate_widget_css
    except ImportError:
        pytest.fail("Per-widget CSS validation is not implemented")
    return validate_widget_css


def test_scoped_style_is_accepted():
    """A local palette change for this tool remains usable in its own CSS file."""
    css = ':where([id^="application_words_"]) { color: #abcdef; font-size: 16px; }'
    assert validator()(css, "words") == css


@pytest.mark.parametrize(
    "css",
    [
        '@import "https://example.com/a.css";',
        "body { display: none; }",
        ':where([id^="application_vowels_"]) { color: red; }',
        ':where([id^="application_words_"]) { background: url(https://example.com); }',
        ':where([id^="application_words_"]) { position: fixed; }',
    ],
)
def test_unsafe_or_foreign_styles_rejected(css):
    """Reject external transmission and styling unrelated controls or the toolbar."""
    with pytest.raises(ValueError):
        validator()(css, "words")


@pytest.mark.parametrize(
    "suffix",
    [" input", " textarea", " label", " .label-wrap", " .output"],
)
def test_closed_descendant_suffixes_are_accepted(suffix):
    """The field box and the caption are inner elements, not the widget container."""
    css = f':where([id^="application_words_"]){suffix} {{ background-color: #26177d; }}'
    assert validator()(css, "words") == css


@pytest.mark.parametrize(
    "suffix",
    [" div", " span", " *", " > input", " input, textarea", " .other", " #id"],
)
def test_arbitrary_descendants_are_rejected(suffix):
    """Only the documented inner elements may be styled, never any node."""
    css = f':where([id^="application_words_"]){suffix} {{ color: #abcdef; }}'
    with pytest.raises(ValueError):
        validator()(css, "words")


def test_widget_companions_are_colocated_and_changes_revoke_reuse(tmp_path):
    """CSS/tests are real files, and editing either never inherits an old grant."""
    from test_application_catalog import installed, registry
    from test_widget_reuse import store

    root = tmp_path / "tools"
    root.mkdir()
    fixture = installed(root)
    tool = registry(fixture).resolve()["count_words_in_text"]
    service = store(tmp_path, fixture)
    proposal = {
        "widget_code": "def create_widget(context): pass",
        "tests_code": "import unittest",
        "notes": "trusted fixture",
    }
    service.publish(tool, proposal)
    directory = root / tool.tool_name
    css_path = directory / (tool.tool_name + "_widget.css")
    tests_path = directory / (tool.tool_name + "_widget_tests.py")
    assert css_path.is_file() and tests_path.read_text(encoding="utf-8") == "import unittest"
    assert service.load(tool).approved
    css_path.write_text(
        ':where([id^="application_count_words_in_text_"]) { color: #abcdef; }', encoding="utf-8"
    )
    assert not service.load(tool).approved
    service.publish(tool, proposal, css=css_path.read_text(encoding="utf-8"))
    assert service.load(tool).approved
    tests_path.write_text("import unittest\n# changed proposal", encoding="utf-8")
    loaded = service.load(tool)
    assert not loaded.approved and "changed proposal" in loaded.proposal["tests_code"]


def test_widget_publication_never_overwrites_a_linked_companion(tmp_path):
    """A tool-local hard link must not redirect CSS writes into another file."""
    import os

    from test_application_catalog import installed, registry
    from test_widget_reuse import store

    root = tmp_path / "tools"
    root.mkdir()
    fixture = installed(root)
    tool = registry(fixture).resolve()["count_words_in_text"]
    outside = tmp_path / "outside.css"
    outside.write_text("preserve outside bytes", encoding="utf-8")
    alias = root / tool.tool_name / (tool.tool_name + "_widget.css")
    os.link(outside, alias)
    with pytest.raises(ValueError):
        store(tmp_path, fixture).publish(
            tool,
            {
                "widget_code": "def create_widget(context): pass",
                "tests_code": "",
                "notes": "fixture",
            },
        )
    assert outside.read_text(encoding="utf-8") == "preserve outside bytes"


@pytest.mark.parametrize(
    "declaration", ["font-size: 100000px", "margin: -9999px", "padding: 9999px"]
)
def test_style_dimensions_are_bounded(declaration):
    """A small CSS file must not create extreme geometry or overlap lifecycle controls."""
    css = ':where([id^="application_words_"]) { ' + declaration + "; }"
    with pytest.raises(ValueError):
        validator()(css, "words")
