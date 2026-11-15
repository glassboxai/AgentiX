"""Opt-in real local retrieval evaluation; never import or execute tool snapshots.

Run explicitly with -m ollama_retrieval. This separate model choice is authorized
for RAG metadata retrieval, not application-generation acceptance.
"""

import json
import logging
import time
from pathlib import Path

import pytest

from agentix.retrieval import (
    OllamaClient,
    OllamaEmbeddings,
    OllamaKeywords,
    ToolRetriever,
    descriptor_from_source,
)

logger = logging.getLogger(__name__)
pytestmark = pytest.mark.ollama_retrieval


def test_local_ollama_retrieval(tmp_path: Path) -> None:
    """Evaluate four reviewed expected top hits with installed local models only.

    Missing/unavailable models fail this explicit evaluation, rather than silently
    skipping or pulling a model. Storage is temporary and fixture code is inert.
    """
    client = OllamaClient()
    service = ToolRetriever(tmp_path, OllamaEmbeddings(client), OllamaKeywords(client))
    root = Path(__file__).parent / "fixtures" / "tool_retrieval"
    manifest = json.loads((root / "provenance.json").read_text(encoding="utf-8"))
    for name in manifest["tools"]:
        source = (root / name / f"{name}_code.py").read_text(encoding="utf-8")
        service.upsert(descriptor_from_source(name, source, artifact_ref=name))
    for case_id, query, expected in (
        ("calculation", "Add or divide two numeric operands", "basic_calculator"),
        ("vowels", "How many vowels occur in a string?", "count_vowels_in_text"),
        ("words", "Count whitespace-separated words in text", "count_words_in_text"),
        ("random", "Draw a random number between two bounds", "random_number_generator"),
    ):
        started = time.perf_counter()
        results = service.search(query)
        logger.info(
            "case=%s duration_ms=%.3f hit=%s",
            case_id,
            (time.perf_counter() - started) * 1000,
            results[0].descriptor.name == expected,
        )
        assert results[0].mode == "hybrid", f"Keyword generation degraded for {case_id}"
        assert results[0].descriptor.name == expected
