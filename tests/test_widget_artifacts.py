"""LAB-003 artifact review binds widget, tool and contract before native staging."""

import pytest

from agentix.lab.widget_artifacts import approve_package, package_digest, validate_widget


def test_review_refuses_changed_widget_after_digest(tmp_path):
    """Catch approving one source snapshot and executing a later edit."""
    from pathlib import Path

    source = Path("src/agentix/lab/reference_widget.py").read_bytes()
    (tmp_path / "count_vowels_in_text_widget.py").write_bytes(source)
    (tmp_path / "count_vowels_in_text_code.py").write_bytes(b"def count_vowels(text): return 0\n")
    digest = package_digest(tmp_path)
    (tmp_path / "count_vowels_in_text_widget.py").write_bytes(source + b"\n# changed\n")
    with pytest.raises(ValueError):
        approve_package(tmp_path, digest)


@pytest.mark.parametrize(
    "source",
    [
        "import os\ndef create_widget(context): return os.environ",
        'import gradio as gr\ndef create_widget(context): return gr.HTML("unsafe")',
        "import gradio as gr\ndef create_widget(context): return context.__dict__",
        'import gradio as gr\ndef create_widget(context): return open("secret")',
        "import gradio as gr\ndef create_widget(context): return gr.Blocks().launch()",
    ],
)
def test_generated_widget_policy_rejects_unsupported_capabilities(source):
    """Catch executable imports, host-style access and unsupported browser content."""
    with pytest.raises(ValueError):
        validate_widget(source.encode())


def test_review_accepts_bounded_nonexecutable_presentation_options():
    """Catch rejection of harmless model output without allowing executable options."""
    from pathlib import Path

    source = Path("src/agentix/lab/reference_widget.py").read_text()
    source = source.replace('label="Text to analyze",', 'label="Text to analyze", max_lines=20,')
    source = source.replace("precision=0,", "precision=0, interactive=False,")
    validate_widget(source.encode())


@pytest.mark.parametrize(
    "name",
    [
        "count_vowels_in_text_code.py",
        "count_vowels_in_text_widget_tests.py",
        "tool_definition.json",
    ],
)
def test_review_refuses_changed_related_artifact(tmp_path, name):
    """Catch stale review when tool implementation, proposed tests or contract changes."""
    import json
    from pathlib import Path

    from agentix.lab.widget_artifacts import CONTRACT

    (tmp_path / "count_vowels_in_text_widget.py").write_bytes(
        Path("src/agentix/lab/reference_widget.py").read_bytes()
    )
    (tmp_path / "count_vowels_in_text_code.py").write_bytes(b"def count_vowels(text): return 0\n")
    (tmp_path / "count_vowels_in_text_widget_tests.py").write_bytes(b'"""Provisional tests."""\n')
    (tmp_path / "tool_definition.json").write_text(json.dumps(CONTRACT))
    digest = package_digest(tmp_path)
    with (tmp_path / name).open("ab") as handle:
        handle.write(b"\n ")
    with pytest.raises(ValueError):
        approve_package(tmp_path, digest)
