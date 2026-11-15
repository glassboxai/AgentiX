"""Characterize retrieval policy boundaries independently of production constants.

Literal expectations intentionally pin the approved contract. Do not derive them
from the implementation's constants: that would hide accidental policy changes.
"""

import json
from pathlib import Path
from urllib.request import Request

import pytest
from test_tool_retrieval import descriptor, retriever

from agentix.retrieval import OllamaClient, OllamaKeywords
from agentix.retrieval.contracts import validate_keywords
from agentix.retrieval.lexical import bm25


def test_keyword_limits_and_generation_contract() -> None:
    """Keep the twenty-term, hundred-character contract in validation and generation."""
    terms = [f"term_{index}" for index in range(20)]
    assert validate_keywords(terms) == terms
    assert validate_keywords(["x" * 100]) == ["x" * 100]
    for invalid in (terms + ["overflow"], ["x" * 101]):
        with pytest.raises(ValueError):
            validate_keywords(invalid)

    class CapturedClient:
        """Capture generation payload data without contacting Ollama."""

        payload: dict

        def post(self, route: str, payload: dict) -> dict:
            """Return a valid keyword response and retain the request contract."""
            self.payload = payload
            return {"response": '["neutrino"]'}

    client = CapturedClient()
    assert OllamaKeywords(client).generate("particle count") == ["neutrino"]
    assert client.payload["format"]["maxItems"] == 20
    assert client.payload["format"]["items"]["maxLength"] == 100
    assert "at most 20" in client.payload["system"]
    assert "at most 100 characters" in client.payload["system"]
    assert client.payload["options"] == {"temperature": 0, "num_predict": 512}


def test_bm25_scores_preserve_approved_formula() -> None:
    """Pin term saturation and length normalization with unequal document lengths."""
    scores = bm25(
        {"short": "neutrino neutrino", "long": "neutrino photon photon photon"}, "neutrino"
    )
    # Independently fixed golden values for k1=1.5, b=0.75 and IDF smoothing=0.5.
    assert scores == pytest.approx(
        {"short": 0.29171449087032736, "long": 0.15854048416865615}, abs=1e-14
    )


def test_query_bytes_and_default_result_limit(tmp_path: Path) -> None:
    """Preserve five default results and the 32 KiB UTF-8 query boundary."""
    service = retriever(tmp_path)
    for index in range(7):
        service.upsert(descriptor(f"word_counter_{index}"))
    assert len(service.search("words")) == 5
    assert len(service.search("é" * 16_384, limit=100)) == 7
    with pytest.raises(ValueError):
        service.search("é" * 16_385)


def test_descriptor_text_character_boundary(tmp_path: Path) -> None:
    """Keep per-field character limits distinct from query byte limits."""
    service = retriever(tmp_path)
    service.upsert(descriptor(description="x" * 32_768))
    with pytest.raises(ValueError):
        service.upsert(descriptor(description="x" * 32_769))


def test_transport_byte_limits_and_overflow_probe(monkeypatch: pytest.MonkeyPatch) -> None:
    """Preserve exact HTTP byte boundaries and detect oversized response bodies."""
    requests: list[int] = []
    reads: list[int] = []
    response_body = b"{}" + b" " * (1_048_576 - 2)

    class Response:
        """Expose a deterministic bounded response stream."""

        def __enter__(self) -> "Response":
            """Return the inert response object."""
            return self

        def __exit__(self, *args: object) -> None:
            """Release no external resources."""

        def read(self, size: int) -> bytes:
            """Record the requested overflow-probe size and return synthetic bytes."""
            reads.append(size)
            return response_body[:size]

    class Opener:
        """Accept transport requests without network access."""

        def open(self, request: Request, timeout: float) -> Response:
            """Record serialized request size and return the inert response."""
            requests.append(len(request.data))
            return Response()

    monkeypatch.setattr("agentix.retrieval.ollama.build_opener", lambda *args: Opener())
    client = OllamaClient()
    overhead = len(json.dumps({"x": ""}).encode("utf-8"))
    assert client.post("/api/generate", {"x": "x" * (2_097_152 - overhead)}) == {}
    assert requests == [2_097_152]
    assert reads == [1_048_577]
    with pytest.raises(RuntimeError):
        client.post("/api/generate", {"x": "x" * (2_097_153 - overhead)})
    assert len(requests) == 1
    response_body += b" "
    with pytest.raises(RuntimeError):
        client.post("/api/generate", {})
