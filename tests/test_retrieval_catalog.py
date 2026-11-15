"""Exercise authoritative catalog synchronization using trusted temporary sources."""

from pathlib import Path

import pytest
from test_tool_retrieval import FakeEmbeddings, FakeKeywords

from agentix.retrieval import CatalogToolSource, ToolRetriever
from agentix.storage.catalog import ToolCatalog


def write_tool(root: Path, name: str, description: str = "Count words") -> Path:
    """Write a trusted source fixture which must only ever be parsed, never executed."""
    folder = root / name
    folder.mkdir(parents=True, exist_ok=True)
    source = folder / f"{name}_code.py"
    source.write_text(
        f'raise RuntimeError("SOURCE MUST NEVER EXECUTE")\n'
        f'def {name}(text: str) -> int:\n    """{description}"""\n    return len(text)\n',
        encoding="utf-8",
    )
    return source


class CountingEmbeddings(FakeEmbeddings):
    """Count embeddings to distinguish incremental synchronization from full rebuilds."""

    def __init__(self) -> None:
        """Start with no inference requests."""
        self.calls = 0

    def embed(self, texts: list[str]) -> list[list[float]]:
        """Count actual batches and delegate deterministic vectors."""
        self.calls += len(texts)
        return super().embed(texts)


def bound_retriever(
    tmp_path: Path, root: Path, provider: CountingEmbeddings | None = None
) -> ToolRetriever:
    """Bind exactly the ToolCatalog root used by a GUI runtime."""
    return ToolRetriever(
        tmp_path / "index",
        provider or CountingEmbeddings(),
        FakeKeywords(),
        descriptor_source=CatalogToolSource(ToolCatalog(root)),
    )


def test_initial_load_and_unchanged_sync(tmp_path: Path) -> None:
    """Load on binding, then skip embeddings for unchanged descriptors."""
    root = tmp_path / "tools"
    write_tool(root, "word_counter")
    provider = CountingEmbeddings()
    service = bound_retriever(tmp_path, root, provider)
    assert service.last_sync_report.added == 1
    assert provider.calls == 1
    report = service.synchronize()
    assert report.unchanged == 1 and report.updated == 0
    assert provider.calls == 1
    assert service.search("words")[0].descriptor.name == "word_counter"
    assert provider.calls == 2  # The additional inference embeds only the query.


def test_search_reflects_add_modify_delete(tmp_path: Path) -> None:
    """Refresh additions, content changes and deleted source files before querying."""
    root = tmp_path / "tools"
    first = write_tool(root, "word_counter")
    service = bound_retriever(tmp_path, root)
    original = service.search("words")[0].descriptor.contract_digest
    write_tool(root, "word_counter", "Count vowel characters")
    changed = service.search("vowel")[0].descriptor
    assert changed.contract_digest != original
    assert changed.description == "Count vowel characters"
    assert service.last_sync_report.updated == 1
    second = write_tool(root, "random_generator", "Generate random numbers")
    assert len(service.search("random")) == 2
    assert service.last_sync_report.added == 1
    first.unlink()
    assert [result.descriptor.name for result in service.search("words")] == ["random_generator"]
    assert service.last_sync_report.removed == 1
    second.unlink()
    assert service.search("random") == []
    assert service.last_sync_report.removed == 1


def test_invalid_modified_source_removes_stale_entry(tmp_path: Path) -> None:
    """A tool that stops parsing cannot retain its old searchable descriptor."""
    root = tmp_path / "tools"
    source = write_tool(root, "word_counter")
    service = bound_retriever(tmp_path, root)
    source.write_text("invalid python !", encoding="utf-8")
    assert service.search("words") == []
    assert service.last_sync_report.removed == 1
    assert service.last_sync_report.rejected[0].tool_id == "word_counter"


def test_missing_root_is_failure_not_empty_snapshot(tmp_path: Path) -> None:
    """An unavailable root never wipes an index or silently serves stale results."""
    root = tmp_path / "tools"
    source = write_tool(root, "word_counter")
    service = bound_retriever(tmp_path, root)
    moved = tmp_path / "offline"
    root.rename(moved)
    with pytest.raises(OSError):
        service.search("words")
    moved.rename(root)
    assert source.exists()
    assert service.synchronize().unchanged == 1


def test_source_binding_survives_reopen(tmp_path: Path) -> None:
    """Reopening preserves synchronization and rejects unrelated or unbound access."""
    root = tmp_path / "tools"
    write_tool(root, "word_counter")
    bound_retriever(tmp_path, root)
    reopened = bound_retriever(tmp_path, root)
    assert reopened.last_sync_report.unchanged == 1
    with pytest.raises(ValueError, match="source"):
        ToolRetriever(tmp_path / "index", FakeEmbeddings(), FakeKeywords())
    other = tmp_path / "other"
    other.mkdir()
    with pytest.raises(ValueError, match="source"):
        bound_retriever(tmp_path, other)


def test_hardlinked_tool_source_rejected(tmp_path: Path) -> None:
    """Reject source aliases without reading outside the catalog boundary."""
    root = tmp_path / "tools"
    source = write_tool(root, "word_counter")
    outside = tmp_path / "other.py"
    outside.hardlink_to(source)
    service = bound_retriever(tmp_path, root)
    assert service.search("words") == []
    assert service.last_sync_report.rejected[0].reason == "unsafe_path"


def test_embedding_failure_blocks_search_and_retries(tmp_path: Path) -> None:
    """Failed synchronization cannot return old matches; a later attempt recovers."""
    root = tmp_path / "tools"
    write_tool(root, "word_counter")
    provider = CountingEmbeddings()
    service = bound_retriever(tmp_path, root, provider)
    write_tool(root, "word_counter", "Count vowels")
    original = provider.embed

    def fail(texts: list[str]) -> list[list[float]]:
        """Simulate an explicit unavailable embedding boundary."""
        raise RuntimeError("embedding unavailable")

    provider.embed = fail
    with pytest.raises(RuntimeError):
        service.search("vowels")
    provider.embed = original
    assert service.search("vowels")[0].descriptor.description == "Count vowels"
    assert service.last_sync_report.updated == 1


def test_same_size_and_mtime_change_is_detected(tmp_path: Path) -> None:
    """Use source content identity rather than trusting timestamps and file sizes."""
    import os

    root = tmp_path / "tools"
    source = write_tool(root, "word_counter", "Count words")
    service = bound_retriever(tmp_path, root)
    before = source.stat()
    write_tool(root, "word_counter", "Count vowel")
    os.utime(source, ns=(before.st_atime_ns, before.st_mtime_ns))
    assert source.stat().st_size == before.st_size
    assert service.search("vowel")[0].descriptor.description == "Count vowel"
    assert service.last_sync_report.updated == 1


def test_deleted_directory_is_removed(tmp_path: Path) -> None:
    """Remove a whole tool directory from results on the next search."""
    root = tmp_path / "tools"
    source = write_tool(root, "word_counter")
    service = bound_retriever(tmp_path, root)
    source.unlink()
    source.parent.rmdir()
    assert service.search("words") == []
    assert service.last_sync_report.removed == 1


def test_reject_oversized_and_noncanonical_sources(tmp_path: Path) -> None:
    """Report unsafe resource sizes and unsupported canonical contracts explicitly."""
    root = tmp_path / "tools"
    source = write_tool(root, "oversized")
    source.write_bytes(b"x" * 65_537)
    write_tool(root, "missing_function").write_text("def other(): pass", encoding="utf-8")
    service = bound_retriever(tmp_path, root)
    assert {entry.reason for entry in service.last_sync_report.rejected} == {
        "source_limit",
        "unsupported_contract",
    }
    assert service.search("words") == []


def test_nonempty_manual_index_is_not_adopted(tmp_path: Path) -> None:
    """Do not silently prune unrelated manually indexed tools when binding a catalog."""
    from test_tool_retrieval import descriptor

    manual = ToolRetriever(tmp_path / "index", FakeEmbeddings(), FakeKeywords())
    manual.upsert(descriptor())
    root = tmp_path / "tools"
    root.mkdir()
    with pytest.raises(ValueError, match="dedicated empty index"):
        bound_retriever(tmp_path, root)
    assert manual.search("words")[0].descriptor.name == "count_words_in_text"


def test_cli_uses_gui_settings_root(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch, capsys: pytest.CaptureFixture[str]
) -> None:
    """Resolve the source from the same Settings field as GUI runtime composition."""
    import json
    from types import SimpleNamespace

    from tools import sync_tool_registry

    root = tmp_path / "configured_tools"
    write_tool(root, "word_counter")
    monkeypatch.setattr(
        sync_tool_registry.Settings,
        "from_environment",
        lambda: SimpleNamespace(tools_root=root, ollama_url="http://127.0.0.1:11434"),
    )
    monkeypatch.setattr(sync_tool_registry, "OllamaEmbeddings", lambda client: CountingEmbeddings())
    monkeypatch.setattr(sync_tool_registry, "OllamaKeywords", lambda client: FakeKeywords())
    sync_tool_registry.main(["--index", str(tmp_path / "configured_index")])
    summary = json.loads(capsys.readouterr().out)
    assert summary["sync"]["added"] == 1
    assert summary["sync"]["rejected"] == []


def test_bound_catalog_root_cannot_change_silently(tmp_path: Path) -> None:
    """Reject a redirected catalog object instead of pruning the originally bound index."""
    root = tmp_path / "tools"
    write_tool(root, "word_counter")
    catalog = ToolCatalog(root)
    adapter = CatalogToolSource(catalog)
    service = ToolRetriever(
        tmp_path / "index", CountingEmbeddings(), FakeKeywords(), descriptor_source=adapter
    )
    other = tmp_path / "other"
    other.mkdir()
    catalog.root = str(other)
    with pytest.raises(ValueError, match="root changed"):
        service.synchronize()
    catalog.root = str(root)
    assert service.synchronize().unchanged == 1


def test_catalog_stage_durations_are_measured(
    tmp_path: Path, caplog: pytest.LogCaptureFixture
) -> None:
    """Measure both the complete catalog scan and index reconciliation stages."""
    import logging
    import re

    root = tmp_path / "tools"
    write_tool(root, "word_counter")
    with caplog.at_level(logging.INFO, logger="agentix.retrieval"):
        bound_retriever(tmp_path, root)
    durations = re.findall(
        r"stage=(?:catalog_scan|catalog_reconcile) outcome=finished duration_ms=([0-9.]+)",
        caplog.text,
    )
    assert len(durations) == 2
    assert all(float(value) > 0 for value in durations)
