"""Editable review regressions use only the maintained temporary fixture package."""

import json

import pytest
from schema3_package import widget_source
from test_application_supervisor import candidate

from agentix.application.app_workflow import ApplicationSupervisor


def reviewed(tmp_path):
    """Return the real schema-3 review snapshot without executing reviewed source."""
    return candidate(tmp_path)


CONNECTION_CODE = "\n".join(
    [
        '"""Connect approved catalog calls."""',
        "def run(payload: dict, call) -> None:",
        '    """Call every approved tool with the shared text input."""',
        '    call("count_words_in_text", text=payload["text"])',
        '    call("count_vowels_in_text", text=payload["text"])',
        "",
    ]
)


def generated(tmp_path):
    """Build a real schema-3 candidate from approved catalog tools without model inference."""
    from test_application_catalog import installed, registry

    from agentix.application.app_workflow import ApplicationPipeline

    root = tmp_path / "tools"
    root.mkdir()
    tools = registry(installed(root)).resolve()

    def factory(folder):
        """Return authored artifacts across the production coordinator boundary."""

        def client(role, content):
            """Never infer with a real model in review regressions."""
            if role == "General Widget Designer":
                module = content["requirements"]["approved_tool_contract"]["module"]
                return {
                    "widget_code": widget_source(module),
                    "tests_code": (
                        "import unittest\n\n\n"
                        "class WidgetTests(unittest.TestCase):\n"
                        "    def test_placeholder(self):\n"
                        "        self.assertTrue(True)\n"
                    ),
                    "notes": "fixture",
                }
            return {
                "inputs": {"text": {"type": "string", "description": "Text to inspect"}},
                "widgets": [
                    {"id": name, "tool": name}
                    for name in sorted(content["requirements"]["approved_catalog"])
                ],
                "connection_code": CONNECTION_CODE,
                "notes": "fixture",
            }

        return client

    return ApplicationPipeline(tmp_path / "applications", factory).generate(
        "Count words and vowels", tools=tools
    )


def service():
    """Import the service at the test boundary so missing behavior fails visibly."""
    from agentix.application.app_review import ApplicationReview

    return ApplicationReview()


def test_review_lists_real_files_and_proposed_tests_separately(tmp_path):
    """A readable file inventory replaces a single JSON dump."""
    item = reviewed(tmp_path)
    names = [name for _, name in service().entries(item)]
    assert "app.py" in names and "count_vowels_in_text_widget.py" in names
    assert "count_words_in_text_widget_tests.py" in names
    text, editable, _ = service().read(item, "count_words_in_text_code.py")
    assert "count_words" in text and not editable


def test_save_widget_invalidates_review_and_updates_exact_manifest(tmp_path):
    """Do not execute modified source under an old application approval."""
    from agentix.lab.application_artifacts import application_digest

    item = reviewed(tmp_path)
    ApplicationSupervisor().approve(item, item.identity, True)
    item.verified = True
    before = item.identity
    source = (item.package / "count_words_in_text_widget.py").read_text(encoding="utf-8")
    service().save(item, "count_words_in_text_widget.py", source + "\n# Reviewed edit\n", before)
    assert item.identity != before and not item.approved and not item.verified
    assert item.snapshot is None and item.digest == application_digest(item.package)
    assert (
        "Reviewed edit"
        in json.loads(item.review_text)["source_files"]["count_words_in_text_widget.py"]
    )


@pytest.mark.parametrize(
    "name",
    ["../outside.py", "count_words_in_text_code.py", "application_context.py", "application.json"],
)
def test_unknown_paths_and_approved_dependencies_cannot_be_edited(tmp_path, name):
    """The editor cannot modify approved tools or supervisor-maintained dependencies."""
    item = reviewed(tmp_path)
    with pytest.raises(ValueError):
        service().save(item, name, "pass", item.identity)
    assert not (tmp_path.parent / "outside.py").exists()


def test_stale_invalid_and_oversized_edits_preserve_the_previous_draft(tmp_path):
    """Reject invalid drafts before changing package bytes or review identity."""
    item = reviewed(tmp_path)
    before = (item.package / "app.py").read_bytes()
    for content, identity in [
        ("pass", "stale"),
        ("def broken(:", item.identity),
        ("x" * 65537, item.identity),
    ]:
        with pytest.raises(ValueError):
            service().save(item, "app.py", content, identity)
    assert (item.package / "app.py").read_bytes() == before


def test_proposed_tests_edit_remains_provisional_and_requires_new_review(tmp_path):
    """Saving test text never executes it or creates an approval."""
    item = reviewed(tmp_path)
    service().save(
        item,
        "count_words_in_text_widget_tests.py",
        'raise RuntimeError("never execute on host")',
        item.identity,
    )
    assert not item.approved
    assert "never execute" in service().read(item, "count_words_in_text_widget_tests.py")[0]


def test_editor_accepts_the_designers_approved_typing_dependency(tmp_path):
    """Editing a valid model widget must retain the same approved import contract."""
    from agentix.agents.application_agents import WidgetDesigner

    item = reviewed(tmp_path)
    source = '"""Typed reviewed widget."""\nimport gradio as gr\nfrom typing import Any\nfrom count_words_in_text_code import count_words_in_text\ndef create_widget(context: Any) -> dict[str, Any]:\n    return {}\n'
    proposal = {"widget_code": source, "tests_code": "", "notes": "fixture"}
    assert (
        WidgetDesigner(
            lambda *args: proposal,
            contracts={"count_words_in_text": {"module": "count_words_in_text_code"}},
        ).generate("count_words_in_text")["widget_code"]
        == source
    )
    service().save(item, "count_words_in_text_widget.py", source, item.identity)
    assert service().read(item, "count_words_in_text_widget.py")[0] == source
    assert not item.approved


@pytest.mark.parametrize("module", ["os", "socket", "subprocess"])
def test_editor_still_rejects_unapproved_runtime_dependencies(tmp_path, module):
    """The typing consistency fix must not authorize files, networking or processes."""
    item = reviewed(tmp_path)
    with pytest.raises(ValueError, match="import"):
        service().save(
            item,
            "count_words_in_text_widget.py",
            f"import {module}\ndef create_widget(context): pass",
            item.identity,
        )


def test_tool_related_selection_opens_three_consistent_panes(tmp_path):
    """Selecting implementation/widget/tests resolves the same tool triplet."""
    item = reviewed(tmp_path)
    snapshot = json.loads(item.review_text)
    snapshot["approved_tool_tests"] = {"count_words_in_text": "import unittest"}
    snapshot["approved_catalog_dependencies"] = {
        "count_words_in_text": {"function": "count_words_in_text"}
    }
    snapshot["manifest"] = {
        "schema_version": 3,
        "files": ["count_words_in_text_code.py"],
        "tools": {"count_words_in_text": {"module": "count_words_in_text_code"}},
    }
    item.review_text = json.dumps(snapshot)
    for name in (
        "count_words_in_text_code.py",
        "count_words_in_text_widget.py",
        "count_words_in_text_tests.py",
        "proposed_tests/count_words_in_text_tests.py",
    ):
        panes = service().panes(item, name)
        assert panes["role"] == "count_words_in_text"
        assert "count_words" in panes["code"] and "create_widget" in panes["widget"]
        assert panes["tool_tests"] == "import unittest"


def test_batch_save_prevalidates_all_buffers_before_any_file_change(tmp_path):
    """One invalid pane must not partially save another valid pane."""
    item = reviewed(tmp_path)
    panes = service().panes(item, "count_words_in_text_widget.py")
    before = (item.package / "count_words_in_text_widget.py").read_bytes()
    panes["widget"] += "\n# valid proposed edit\n"
    panes["widget_tests"] = "def invalid(:"
    with pytest.raises(ValueError):
        service().save_group(item, panes, item.identity)
    assert (item.package / "count_words_in_text_widget.py").read_bytes() == before


def test_edited_tool_code_is_a_pending_revision_not_an_approved_shared_overwrite(tmp_path):
    """App approval cannot silently authorize altered installed tool implementations."""
    item = reviewed(tmp_path)
    panes = service().panes(item, "count_words_in_text_code.py")
    panes["code"] = (
        '"""Pending tool revision."""\n'
        "from typing import Annotated\n\n\n"
        "def count_words_in_text(\n"
        '    text: Annotated[str, "Text to inspect"]\n'
        ') -> Annotated[int, "Word count"]:\n'
        '    """Return a deliberately wrong count."""\n    return 999\n'
    )
    service().save_group(item, panes, item.identity)
    snapshot = json.loads(item.review_text)
    assert "count_words_in_text" in snapshot["pending_tool_revisions"]
    assert not item.approved and not item.verified
    assert (
        item.folder / "tool-revisions" / "count_words_in_text" / "count_words_in_text_code.py"
    ).is_file()


def test_gradio_outer_whitespace_does_not_create_a_tool_revision(tmp_path):
    """Submitting an unchanged Code pane preserves approved source/test bytes."""
    from test_application_catalog import SOURCES

    item = generated(tmp_path)
    assert (item.package / "count_words_in_text_code.py").read_bytes() == SOURCES[
        "count_words_in_text"
    ]
    panes = service().panes(item, "count_words_in_text_widget.py")
    panes = {key: value.strip() if key != "role" else value for key, value in panes.items()}
    panes["widget"] += "\n# actual widget-only edit\n"
    service().save_group(item, panes, item.identity)
    assert not json.loads(item.review_text).get("pending_tool_revisions")
    assert (item.package / "count_words_in_text_code.py").read_bytes() == SOURCES[
        "count_words_in_text"
    ]


def test_tool_source_inventory_identifies_revision_editor(tmp_path):
    """Tool source selection must not be mislabeled read-only when it opens editable panes."""
    labels = {key: label for label, key in service().entries(reviewed(tmp_path))}
    assert labels["count_words_in_text_code.py"].endswith(" — tool revision")
    assert labels["count_vowels_in_text_code.py"].endswith(" — tool revision")
