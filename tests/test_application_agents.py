"""Offline agent contract tests; only the local-model network is substituted."""

import pytest

from agentix.agents.application_agents import WidgetDesigner


def test_designer_validates_direct_import_contract_without_executing():
    """Catch running candidate code or accepting a widget with an unknown dependency."""
    candidate = {
        "widget_code": 'import gradio as gr\nfrom count_vowels_in_text_code import count_vowels\nraise RuntimeError("must not execute")\ndef create_widget(context):\n    pass\n',
        "tests_code": "",
        "notes": "fixture",
    }
    prompts = []

    def client(role, content):
        """Return a controlled model-boundary proposal without executing source."""
        prompts.append((role, content))
        return candidate

    result = WidgetDesigner(
        client, contracts={"count_vowels_in_text": {"module": "count_vowels_in_text_code"}}
    ).generate("count_vowels_in_text")
    assert result["widget_code"] == candidate["widget_code"]
    assert "count_vowels" in str(prompts)
    assert "gr.Textbox(" not in str(prompts)
    assert ".click(" not in str(prompts)


def test_designer_rejects_unknown_import():
    """Catch allowing arbitrary dependencies through the widget proposal filter."""
    with pytest.raises(ValueError, match="import"):
        WidgetDesigner(
            lambda *args: {
                "widget_code": "import os\ndef create_widget(context): pass",
                "tests_code": "",
                "notes": "",
            },
            contracts={"count_words_in_text": {"module": "count_words_in_text_code"}},
        ).generate("count_words_in_text")


def test_dynamic_import_is_rejected_before_native_review():
    """Catch bypassing the approved import surface through a dynamic builtin."""
    from agentix.agents.application_agents import validate_source

    with pytest.raises(ValueError, match="dynamic"):
        validate_source(
            'def create_application():\n    return __import__("os")',
            {"gradio"},
            "create_application",
        )


def test_local_client_supplies_a_strict_response_schema(tmp_path, monkeypatch):
    """Catch requesting only valid JSON while accepting wrong workflow/notes types."""
    import json

    from agentix.agents.application_agents import LocalModelClient

    sent = []

    class Response:
        """Provide a bounded HTTP response fixture without network access."""

        def __enter__(self):
            """Open the inert response fixture for a context-managed request."""
            return self

        def __exit__(self, *args):
            """Leave the response fixture without suppressing errors."""
            return False

        def read(self, size):
            """Return a complete fixed response envelope within the requested boundary."""
            return json.dumps(
                {
                    "model": "qwen3-coder:30b",
                    "done": True,
                    "message": {
                        "content": json.dumps(
                            {
                                "inputs": {
                                    "text": {"type": "string", "description": "Text to inspect"}
                                },
                                "widgets": [
                                    {"id": "count_words_in_text", "tool": "count_words_in_text"}
                                ],
                                "connection_code": (
                                    '"""Connect approved catalog calls."""\n'
                                    "def run(payload: dict, call) -> None:\n"
                                    '    """Call the approved tool once."""\n'
                                    '    call("count_words_in_text", text=payload["text"])\n'
                                ),
                                "notes": "",
                            }
                        )
                    },
                }
            ).encode()

    class Opener:
        """Capture the outgoing local request while keeping tests offline."""

        def open(self, request, timeout):
            """Record the request contract and return the controlled response fixture."""
            sent.append(json.loads(request.data))
            return Response()

    monkeypatch.setattr("agentix.agents.application_agents.build_opener", lambda *args: Opener())
    LocalModelClient(tmp_path)("General Assembler", {"system": "schema probe", "requirements": {}})
    schema = sent[0]["format"]
    assert isinstance(schema, dict)
    assert schema["properties"]["notes"]["type"] == "string"
    assert "connection_code" in schema["properties"]
    assert schema["additionalProperties"] is False
    import jsonschema

    valid = {
        "inputs": {"text": {"type": "string", "description": "Text to inspect"}},
        "widgets": [{"id": "count_words_in_text", "tool": "count_words_in_text"}],
        "connection_code": (
            '"""Connect approved catalog calls."""\n'
            "def run(payload: dict, call) -> None:\n"
            '    """Call the approved tool once."""\n'
            '    call("count_words_in_text", text=payload["text"])\n'
        ),
        "notes": "",
    }
    jsonschema.validate(valid, schema)
    valid["widgets"][0]["tool"] = ""
    with pytest.raises(jsonschema.ValidationError):
        jsonschema.validate(valid, schema)
