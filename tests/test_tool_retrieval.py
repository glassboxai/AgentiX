"""Exercise hybrid retrieval without executing tool fixtures or contacting models."""

import hashlib
import json
import logging
from pathlib import Path

import pytest

from agentix.retrieval import ToolDescriptor, ToolRetriever, descriptor_from_source


class FakeEmbeddings:
    """Provide stable semantic vectors without external services."""

    model_id = "test-embedding-v1"

    def embed(self, texts: list[str]) -> list[list[float]]:
        """Map concepts to finite deterministic vectors."""
        groups = ("calculat arithmetic add sum", "vowel vocal", "word token", "random dice")
        return [
            [float(any(term in text.lower() for term in group.split())) + 0.01 for group in groups]
            for text in texts
        ]


class FakeKeywords:
    """Return an injected JSON-equivalent keyword list or a safe simulated error."""

    model_id = "test-keywords-v1"

    def __init__(self, result: object = None, error: bool = False) -> None:
        """Remember the response and count actual generation requests."""
        self.result, self.error, self.calls = result or [], error, 0

    def generate(self, query: str) -> list[str]:
        """Return configured keywords without logging the query."""
        self.calls += 1
        if self.error:
            raise RuntimeError("SECRET_QUERY must not reach logs")
        return self.result


def descriptor(
    name: str = "count_words_in_text", description: str = "Count words in text"
) -> ToolDescriptor:
    """Build an independent complete tool descriptor."""
    return ToolDescriptor(
        name, name, description, f"{name}_code.py:{name}", {}, {}, [], name, "abc"
    )


def retriever(tmp_path: Path, keywords: FakeKeywords | None = None) -> ToolRetriever:
    """Compose real temporary Chroma persistence with deterministic model boundaries."""
    return ToolRetriever(tmp_path, FakeEmbeddings(), keywords or FakeKeywords())


def test_empty_and_validation(tmp_path: Path) -> None:
    """An empty registry avoids model calls and rejects invalid public inputs."""
    keywords = FakeKeywords()
    service = retriever(tmp_path, keywords)
    assert service.search("words") == []
    assert keywords.calls == 0
    for limit in (0, 101, True):
        with pytest.raises(ValueError):
            service.search("words", limit=limit)
    with pytest.raises(ValueError):
        service.search(" ")


def test_persistence_update_delete(tmp_path: Path) -> None:
    """Descriptors survive reopening; replacement and deletion leave no stale matches."""
    service = retriever(tmp_path)
    service.upsert(descriptor())
    reopened = retriever(tmp_path)
    assert reopened.search("words")[0].descriptor == descriptor()
    updated = descriptor(description="Count tokens and words")
    reopened.upsert(updated)
    assert service.search("tokens")[0].descriptor == updated
    reopened.delete(updated.tool_id)
    reopened.delete(updated.tool_id)
    assert service.search("tokens") == []


def test_hybrid_identifiers_and_generated_keywords(tmp_path: Path) -> None:
    """Arbitrary identifiers and model-generated synonyms participate in retrieval."""
    keywords = FakeKeywords(["count_words_in_text", "count_words_in_text"])
    service = retriever(tmp_path, keywords)
    service.upsert(descriptor())
    service.upsert(descriptor("computePhotonFlux", "Estimate luminous energy"))
    results = service.search("token tally", keywords=["count_words_in_text"])
    assert results[0].descriptor.name == "count_words_in_text"
    assert results[0].lexical_score > 0
    assert keywords.calls == 1
    results = service.search("computePhotonFlux")
    assert any(
        item.descriptor.name == "computePhotonFlux" and item.lexical_score > 0 for item in results
    )
    assert len(service.search("words", limit=1)) == 1


def test_degraded_and_private_logs(tmp_path: Path, caplog: pytest.LogCaptureFixture) -> None:
    """Keyword failure remains observable without disclosing provider payloads."""
    service = retriever(tmp_path, FakeKeywords(error=True))
    service.upsert(descriptor())
    with caplog.at_level(logging.DEBUG, logger="agentix.retrieval"):
        results = service.search("SECRET_QUERY words")
    assert results[0].mode == "keyword_fallback"
    assert "operation=" in caplog.text and "duration_ms=" in caplog.text
    assert "SECRET_QUERY" not in caplog.text
    assert "keyword_generation" in caplog.text and "ranking" in caplog.text
    assert "outcome=selected" in caplog.text


@pytest.mark.parametrize("terms", [["x"] * 21, [1], ["x" * 101], "words"])
def test_invalid_keyword_output_degrades(tmp_path: Path, terms: object) -> None:
    """Malformed generator output cannot break the original lexical query."""
    service = retriever(tmp_path, FakeKeywords(terms))
    service.upsert(descriptor())
    assert service.search("words")[0].mode == "keyword_fallback"


def test_embedding_mismatch(tmp_path: Path) -> None:
    """Model identity and dimensions cannot silently mix in an existing index."""
    service = retriever(tmp_path)
    service.upsert(descriptor())
    other = FakeEmbeddings()
    other.model_id = "different"
    with pytest.raises(ValueError):
        ToolRetriever(tmp_path, other, FakeKeywords())


def test_embedding_failure_is_not_empty_result(tmp_path: Path) -> None:
    """Embedding exceptions remain explicit rather than reporting no matching tools."""
    service = retriever(tmp_path)
    service.upsert(descriptor())
    service.embeddings.embed = lambda texts: (_ for _ in ()).throw(RuntimeError("provider down"))
    with pytest.raises(RuntimeError):
        service.search("words")


def test_real_tool_snapshots(tmp_path: Path) -> None:
    """Retrieve all four real snapshots by intent without importing their Python."""
    root = Path(__file__).parent / "fixtures" / "tool_retrieval"
    manifest = json.loads((root / "provenance.json").read_text(encoding="utf-8"))
    service = retriever(tmp_path)
    for relative, expected in manifest["sha256"].items():
        assert hashlib.sha256((root / relative).read_bytes()).hexdigest() == expected
    for name in manifest["tools"]:
        source = (root / name / f"{name}_code.py").read_text(encoding="utf-8")
        item = descriptor_from_source(name, source, artifact_ref=name)
        assert item.input_schema and item.output_schema
        service.upsert(item)
    for query, name in (
        ("arithmetic calculate sum", "basic_calculator"),
        ("vowel vocal characters", "count_vowels_in_text"),
        ("word token tally", "count_words_in_text"),
        ("random dice number", "random_number_generator"),
    ):
        assert service.search(query)[0].descriptor.name == name
        assert service.search(name)[0].descriptor.name == name
    first = [item.descriptor.tool_id for item in service.search("text count")]
    assert first == [item.descriptor.tool_id for item in service.search("text count")]
