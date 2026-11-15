# RAG-009: Installed catalog loading and synchronization — 2026-11-03

Implemented CatalogToolSource using the exact ToolCatalog root supplied by the GUI
runtime, or the same Settings.tools_root resolved by its launcher configuration.
The optional descriptor_source argument binds a dedicated ToolRetriever collection.
Binding loads immediately and every subsequent search reconciles the complete source
snapshot. Explicit synchronize() is available without a search.

Added/changed descriptors receive embeddings; unchanged vectors are reused.
Deleted files/directories and invalid canonical entries are removed. Content hashes
detect changes even with identical size and mtime. Failed scans/inference/storage
abort search instead of returning stale results. Source identity is persisted and
checked when reopening; unrelated or unbound reuse of that collection is rejected.

## Verification

| Check | Observed result |
| --- | --- |
| Feature red | ImportError for missing CatalogToolSource before implementation |
| Focused retrieval and reference checks | 57 passed; exit 0 |
| Final offline suite | 953 passed, 89 deselected, 59 warnings; exit 0; 81.06 seconds |
| Ruff lint | All checks passed; exit 0 |
| Ruff format --check | 349 files already formatted; exit 0 |
| Reference freshness | No issues; exit 0 |
| Operational initial load with local embeddings | 4 added, 0 rejected; exit 0 |
| Operational reopen using final code | 4 unchanged, 0 added/updated/removed/rejected; exit 0 |
| Operational real search using final code | count_words_in_text ranked first, hybrid mode, 4 candidates; exit 0 |

The 14 catalog synchronization tests use independently authored temporary fixtures,
including a top-level raise to detect accidental source execution. Tests cover
initial load, unchanged inference reuse, add/modify/delete, invalidation, source
unavailability, reopen binding, hard links, provider recovery, preserved mtime/size,
whole-directory deletion, size/canonical rejections, dedicated-index ownership,
GUI Settings composition, mutable-root rejection and stage timing measurements.
No existing generated_tools contents were read or executed by engineering checks.

RAG-ERR-004 and RAG-ERR-005 were reproduced as failing regressions before their
corrections. A changed injected catalog root is rejected before reconciliation,
and catalog stage durations use their own monotonic timers. No assertion was weakened.

## Operational evidence and location

The GUI deployment receipt resolves the previously supplied physical user root:
C:/Users/xpiku/AppData/Local/Packages/OpenAI.Codex_2p2nqsd0c76g0/LocalCache/Local/AgentiX/v5.
The read-only source is data/tools beneath that root. The new persistent index is
data/tool_registry beside it. No source tools, approvals, widgets or live GUI were
modified, imported, executed or restarted. The initial source load was authorized
explicitly; source edits/deletion scenarios were tested only in temporary fixtures.

Raw JSON summaries: RAG_009_INITIAL_SYNC.json, RAG_009_REOPEN_SYNC.json and
RAG_009_REAL_QUERY.json. Initial loading used installed nomic-embed-text:latest.
The final real search also used qwen3:14b for keywords, with no fallback. Reopening
synchronized in approximately 50 ms without document inference; the real query's
pre-search sync took approximately 46 ms. Its first loaded-model search took
approximately 17.172 seconds. These observations are not a broad performance benchmark.

The operational checks establish metadata loading/retrieval and reuse, not tool
functional correctness, approval or execution isolation. Framework/native/browser
markers were not run for this adapter. Chroma embedding-configuration deprecations
and existing CrewAI/Gradio warnings remain visible in the full suite.

Synchronization happens at load/search time, without a background watcher or new
GUI callback wiring. Changes after the source snapshot appear on the next sync.
Writes are not transactional, and multiple writers still need external coordination.
The initial load preceded the two edge-case corrections; the final reopen, real
query and offline checks verify the corrected implementation.

Source fingerprints are recorded separately in RAG_009_SOURCE_HASHES.json; earlier
RAG-001/RAG-008 evidence remains intact. References and source contracts were manually
reviewed for source ownership, file bounds, failure behavior and synchronization.
This report was authored from reviewed local outputs. No model generated engineering
code/tests, and report inputs were not sent to remote endpoints.
