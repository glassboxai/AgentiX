"""V5-ERR-041-03: preserve source presence across the actual local-model boundary."""

import json
from pathlib import Path

import jsonschema
import pytest
from test_workflow_bindings import SCHEMAS, workflow

from agentix.agents.application_agents import LocalModelClient
from agentix.agents.catalog_agents import CatalogAssembler


@pytest.mark.parametrize("timeout", [120, 600])
def test_local_http_client_round_trip_keeps_graph_and_timeout(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch, timeout: int
) -> None:
    """Exercise real serialization and parsing with only HTTP replaced by a fixture."""
    proposal = {
        "inputs": {"document": {"type": "string", "description": "Document"}},
        "widgets": [{"id": node["id"], "tool": node["tool"]} for node in workflow()["nodes"]],
        "connection_code": (
            '"""Connect fixture measurements."""\n'
            "def run(payload: dict, call) -> None:\n"
            '    """Call each fixture tool once with the shared document."""\n'
            '    left = call("measure", text=payload["document"])\n'
            '    right = call("measure", text=payload["document"])\n'
            '    draw = call("samples", size=1)\n'
            '    call("combine", x=left, y=draw[0])\n'
            '    call("combine", x=right, y=draw[0])\n'
        ),
        "notes": "Independent fixture",
    }
    seen = []

    class Response:
        """Return one bounded completed Ollama response without network activity."""

        def __enter__(self) -> "Response":
            """Open the authored response."""
            return self

        def __exit__(self, *args: object) -> bool:
            """Propagate failures without suppressing them."""
            return False

        def read(self, size: int) -> bytes:
            """Return reviewed fixture data within the caller's byte boundary."""
            return json.dumps(
                {
                    "model": "qwen3-coder:30b",
                    "done": True,
                    "message": {"content": json.dumps(proposal)},
                }
            ).encode()[:size]

    class Opener:
        """Capture timeout and request schema; never call a model."""

        def open(self, request: object, timeout: int) -> Response:
            """Record the transport options and return the inert response."""
            seen.append((json.loads(request.data), timeout))
            return Response()

    monkeypatch.setattr("agentix.agents.application_agents.build_opener", lambda *args: Opener())
    client = LocalModelClient(tmp_path, timeout=timeout)
    assert CatalogAssembler(client).generate("Compose the independent fixture", SCHEMAS) == proposal
    assert seen[0][1] == timeout
    jsonschema.validate(proposal, seen[0][0]["format"])
    assert seen[0][0]["model"] == "qwen3-coder:30b"
    assert len(list(tmp_path.glob("*.request.json"))) == 1


@pytest.mark.parametrize("timeout", [0, 601, True, "600", 1.5])
def test_timeout_is_bounded_before_any_operation(tmp_path: Path, timeout: object) -> None:
    """No unlimited, coerced or oversized deadline may reach the HTTP boundary."""
    with pytest.raises(ValueError, match="timeout"):
        LocalModelClient(tmp_path, timeout=timeout)
    assert list(tmp_path.iterdir()) == []
