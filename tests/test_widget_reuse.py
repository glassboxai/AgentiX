"""Persistent widget reuse tests use trusted temporary tools and explicit protection doubles."""

import json
from types import SimpleNamespace
from unittest.mock import patch

import pytest
from schema3_package import widget_source
from test_application_catalog import installed, registry


class Protector:
    """Authenticated fixture boundary; not a claim of Windows DPAPI execution."""

    def seal(self, data):
        """Encode one trusted fixture record."""
        return b"fixture-auth:" + data

    def unseal(self, data):
        """Reject unsigned fixture metadata."""
        if not data.startswith(b"fixture-auth:"):
            raise ValueError("Invalid metadata")
        return data.removeprefix(b"fixture-auth:")


def store(tmp_path, fixture):
    """Build the production store over trusted fixture directories."""
    from agentix.storage.widget_store import WidgetStore

    return WidgetStore(
        fixture.ledger.security,
        tmp_path / "protected",
        protector=Protector(),
        policy="fixture-policy",
    )


def test_widget_is_colocated_and_reused_after_store_recreation(tmp_path):
    """Exact approved widget bytes survive a fresh host adapter without a designer call."""
    root = tmp_path / "tools"
    root.mkdir()
    fixture = installed(root)
    tool = registry(fixture).resolve()["count_words_in_text"]
    proposal = {
        "widget_code": '"""Reviewed widget."""\ndef create_widget(context): pass\n',
        "tests_code": "import unittest",
        "notes": "reviewed fixture",
    }
    service = store(tmp_path, fixture)
    assert service.load(tool) is None
    service.publish(tool, proposal)
    saved = root / tool.tool_name / f"{tool.tool_name}_widget.py"
    assert saved.read_bytes() == proposal["widget_code"].encode()
    loaded = store(tmp_path, fixture).load(tool)
    assert loaded.approved and loaded.proposal == proposal


def test_changed_widget_is_not_still_approved(tmp_path):
    """Human edits become a fresh unapproved proposal, never an inherited grant."""
    root = tmp_path / "tools"
    root.mkdir()
    fixture = installed(root)
    tool = registry(fixture).resolve()["count_words_in_text"]
    service = store(tmp_path, fixture)
    proposal = {
        "widget_code": "def create_widget(context): pass",
        "tests_code": "",
        "notes": "fixture",
    }
    service.publish(tool, proposal)
    path = root / tool.tool_name / f"{tool.tool_name}_widget.py"
    path.write_bytes(b"def create_widget(context): return None")
    assert not service.load(tool).approved
    assert "return None" in service.load(tool).proposal["widget_code"]


def test_corrupt_protected_metadata_cannot_authorize_a_widget(tmp_path):
    """An untrusted local metadata edit cannot publish a trusted widget grant."""
    root = tmp_path / "tools"
    root.mkdir()
    fixture = installed(root)
    tool = registry(fixture).resolve()["count_words_in_text"]
    service = store(tmp_path, fixture)
    service.publish(
        tool, {"widget_code": "def create_widget(context): pass", "tests_code": "", "notes": ""}
    )
    record = next((tmp_path / "protected").rglob("*.approval"))
    record.write_bytes(b"untrusted")
    with pytest.raises(ValueError):
        service.load(tool)


def test_pipeline_reuses_published_widgets_without_another_designer_call(tmp_path):
    """A new application may call Assembler, but must not regenerate approved widgets."""
    from agentix.application.app_workflow import ApplicationPipeline, ApplicationSupervisor

    root = tmp_path / "tools"
    root.mkdir()
    fixture = installed(root)
    tools = registry(fixture).resolve()
    service = store(tmp_path, fixture)
    calls = []

    def factory(folder):
        """Count model role calls while returning independently authored source fixtures."""

        def client(role, content):
            """Never use a real model in ordinary persistence tests."""
            calls.append(role)
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
            catalog = content["requirements"]["approved_catalog"]
            return {
                "inputs": {"text": {"type": "string", "description": "Text to inspect"}},
                "widgets": [{"id": name, "tool": name} for name in sorted(catalog)],
                "connection_code": (
                    '"""Connect approved catalog calls."""\n'
                    "def run(payload: dict, call) -> None:\n"
                    '    """Call every approved tool with the shared text input."""\n'
                    + "".join(
                        f'    call("{name}", text=payload["text"])\n' for name in sorted(catalog)
                    )
                ),
                "notes": "fixture",
            }

        return client

    pipeline = ApplicationPipeline(tmp_path / "applications", factory, widget_store=service)
    item = pipeline.generate("Count words and vowels", tools=tools)
    assert service.load(tools["count_words_in_text"]) is None
    supervisor = ApplicationSupervisor(
        native=lambda *args: {"count_words_in_text": 2, "count_vowels_in_text": 2},
        preview_factory=lambda *args, **kwargs: SimpleNamespace(
            url="http://127.0.0.1:7877", close=lambda: None
        ),
        browser=lambda *args: None,
    )
    supervisor.approve(item, item.identity, True)
    with patch("agentix.application.general_acceptance.browser_verify"):
        supervisor.verify(item, "http://127.0.0.1:7877")
    assert service.load(tools["count_words_in_text"]).approved
    second = pipeline.generate("Count another text", tools=tools)
    assert calls == [
        "General Assembler",
        "General Widget Designer",
        "General Widget Designer",
        "General Assembler",
    ]
    assert not second.approved and not second.verified
    assert (
        json.loads(second.review_text)["widget_reuse"]["count_words_in_text"]
        == "approved widget reused"
    )


def test_widget_write_cannot_alias_the_approved_tool_source(tmp_path):
    """Reject a resolved widget filename alias before any tool code can be overwritten."""
    root = tmp_path / "tools"
    root.mkdir()
    fixture = installed(root)
    tool = registry(fixture).resolve()["count_words_in_text"]
    service = store(tmp_path, fixture)
    target = root / tool.tool_name / f"{tool.tool_name}_code.py"
    fixture.ledger.security.validate_and_resolve_path = lambda *args: str(target)
    with pytest.raises(ValueError, match="alias|widget"):
        service.publish(
            tool, {"widget_code": "def create_widget(context): pass", "tests_code": "", "notes": ""}
        )
    assert target.read_bytes() == tool.code


def test_changed_tool_contract_or_widget_policy_requires_new_review(tmp_path):
    """Persisted widget approval cannot survive a changed dependency or runtime policy."""
    from dataclasses import replace

    from agentix.storage.widget_store import WidgetStore

    root = tmp_path / "tools"
    root.mkdir()
    fixture = installed(root)
    tool = registry(fixture).resolve()["count_words_in_text"]
    service = store(tmp_path, fixture)
    service.publish(
        tool, {"widget_code": "def create_widget(context): pass", "tests_code": "", "notes": ""}
    )
    assert not service.load(replace(tool, contract_digest="changed-contract")).approved
    other = WidgetStore(
        fixture.ledger.security,
        tmp_path / "protected",
        protector=Protector(),
        policy="changed-policy",
    )
    assert not other.load(tool).approved
