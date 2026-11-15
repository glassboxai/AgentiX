"""Validate Ollama transport contracts without network or model execution."""

import json
from pathlib import Path

import pytest
from test_tool_retrieval import FakeEmbeddings, FakeKeywords, descriptor, retriever

from agentix.retrieval import OllamaClient, OllamaEmbeddings, OllamaKeywords, ToolRetriever
from agentix.retrieval.lexical import bm25, tokens


class StubClient:
    """Capture generated requests without contacting any endpoint."""

    def __init__(self, response: dict) -> None:
        """Remember a synthetic response and the most recent request."""
        self.response = response
        self.route = ""
        self.payload: dict = {}

    def post(self, route: str, payload: dict) -> dict:
        """Record a request and return the configured response."""
        self.route, self.payload = route, payload
        return self.response


def test_keyword_adapter_contract() -> None:
    """Use bounded structured local generation and preserve arbitrary domain terms."""
    client = StubClient({"response": json.dumps(["PhotonFlux", "photonflux", "spectral density"])})
    assert OllamaKeywords(client).generate("measure light") == ["PhotonFlux", "spectral density"]
    assert client.route == "/api/generate"
    assert client.payload["model"] == "qwen3:14b"
    assert client.payload["options"]["temperature"] == 0
    assert client.payload["stream"] is False
    assert client.payload["format"]["maxItems"] == 20


@pytest.mark.parametrize("response", [None, 7, "not JSON", '{"keywords": []}', '[""]'])
def test_keyword_adapter_rejects_invalid_response(response: object) -> None:
    """Reject malformed output before it can influence lexical ranking."""
    with pytest.raises((ValueError, TypeError)):
        OllamaKeywords(StubClient({"response": response})).generate("words")


def test_embedding_adapter_contract() -> None:
    """Request embeddings without truncation or model installation."""
    client = StubClient({"embeddings": [[1.0, 2.0]]})
    assert OllamaEmbeddings(client).embed(["text"]) == [[1.0, 2.0]]
    assert client.route == "/api/embed"
    assert client.payload["model"] == "nomic-embed-text:latest"
    assert client.payload["truncate"] is False


@pytest.mark.parametrize(
    "endpoint",
    [
        "https://example.com",
        "http://example.com",
        "http://127.0.0.1/other",
        "http://user:password@localhost:11434",
        "http://localhost:11434?x=1",
    ],
)
def test_remote_endpoint_rejected(endpoint: str) -> None:
    """Reject nonlocal destinations and endpoint credentials before any I/O."""
    with pytest.raises(ValueError):
        OllamaClient(endpoint)


def test_http_boundary_is_bounded_and_sanitizes_errors(monkeypatch: pytest.MonkeyPatch) -> None:
    """Never reveal provider exception bodies or silently retry requests."""
    calls = []

    class BrokenOpener:
        """Simulate a failing transport with a sensitive exception message."""

        def open(self, request: object, timeout: float) -> None:
            """Count attempts and fail before network access."""
            calls.append(timeout)
            raise OSError("SECRET_PROMPT")

    monkeypatch.setattr("agentix.retrieval.ollama.build_opener", lambda *args: BrokenOpener())
    with pytest.raises(RuntimeError, match="Local Ollama request failed") as error:
        OllamaClient().post("/api/generate", {"prompt": "SECRET_PROMPT"})
    assert "SECRET_PROMPT" not in str(error.value)
    assert calls == [60]


def test_lexical_segmentation_and_zero_match() -> None:
    """Split arbitrary identifiers while keeping their complete searchable spelling."""
    terms = tokens("computePhotonFlux HTTPClient spectral_density αβ")
    assert {"computephotonflux", "compute", "photon", "flux", "http", "client", "αβ"} <= set(terms)
    assert bm25({"a": "volcano", "b": "photons"}, "unknown") == {}


@pytest.mark.parametrize("vector", [[], [0.0, 0.0], [float("nan")], [float("inf")], [True]])
def test_bad_embeddings_rejected(tmp_path: Path, vector: list) -> None:
    """Malformed model output cannot become a persisted tool entry."""
    provider = FakeEmbeddings()
    provider.embed = lambda texts: [vector]
    service = ToolRetriever(tmp_path, provider, FakeKeywords())
    with pytest.raises(ValueError):
        service.upsert(descriptor())
    assert service.search("words") == []


def test_dimension_change_and_invalid_descriptors(tmp_path: Path) -> None:
    """Reject incompatible vectors and incomplete descriptors without losing old entries."""
    service = retriever(tmp_path)
    service.upsert(descriptor())
    service.embeddings.embed = lambda texts: [[1.0, 2.0]]
    with pytest.raises(ValueError, match="dimension"):
        service.search("words")
    with pytest.raises(ValueError):
        service.upsert(descriptor(name=""))


def test_rrf_ties_are_stable(tmp_path: Path) -> None:
    """Equal candidates are ordered by ID and expose RRF rank contributions."""
    service = retriever(tmp_path)
    service.upsert(descriptor("b", "volcano"))
    service.upsert(descriptor("a", "volcano"))
    matches = service.search("unrelated")
    assert [item.descriptor.name for item in matches] == ["a", "b"]
    assert matches[0].score == pytest.approx(1 / 61)
    assert matches[0].lexical_score is None


def test_fixture_sources_are_not_maintained_code() -> None:
    """Preserved source snapshots are data, not reference-generation targets."""
    from tools.build_reference import maintained_sources

    root = Path(__file__).resolve().parents[1]
    assert not any("tool_retrieval" in path.parts for path in maintained_sources(root))


def test_import_is_inert_and_independent() -> None:
    """Import in a fresh interpreter without loading CrewAI, Chroma or model clients."""
    import subprocess
    import sys

    source = Path(__file__).resolve().parents[1] / "src"
    script = (
        "import sys; sys.path.insert(0, sys.argv[1]); import agentix.retrieval; "
        "assert 'crewai' not in sys.modules; assert 'chromadb' not in sys.modules"
    )
    completed = subprocess.run(
        [sys.executable, "-c", script, str(source)], capture_output=True, text=True, timeout=20
    )
    assert completed.returncode == 0, completed.stderr


def test_finished_stage_durations_are_measured(
    tmp_path: Path, caplog: pytest.LogCaptureFixture
) -> None:
    """Report measured persistence, snapshot and ranking times rather than placeholder zeros."""
    import logging
    import re

    with caplog.at_level(logging.INFO, logger="agentix.retrieval"):
        service = retriever(tmp_path)
        service.upsert(descriptor())
        service.search("words")
    durations = re.findall(
        r"stage=(?:persistence|snapshot|ranking) outcome=finished duration_ms=([0-9.]+)",
        caplog.text,
    )
    assert len(durations) == 3
    assert all(float(value) > 0 for value in durations)
