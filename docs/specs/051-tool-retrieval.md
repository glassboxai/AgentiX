# RAG-001: Independent hybrid tool retrieval

Status: implemented; verification evidence is recorded in the delivery report.

## Requirements and acceptance

| ID | Requirement | Evidence |
| --- | --- | --- |
| RAG-001 | Independent typed upsert/delete/search API, without agent integration or execution grants | Persistence/update/delete and validation tests |
| RAG-002 | Explicit local embedding and keyword providers, no pulls or remote requests | Adapter/transport tests; optional real Ollama evaluation |
| RAG-003 | Semantic cosine and BM25 retrieval fused by equal-weight RRF (constant 60) | Identifier, synonym, stable ranking and fixture tests |
| RAG-004 | Bounded JSON keywords; original-query fallback on generation failure | Invalid-output, timeout/transport and private-log tests |
| RAG-005 | Correlated diagnostics without query/prompt/source bodies | Captured-log regression |
| RAG-006 | Four source/specification snapshots with provenance, never executed | Hash checks, AST extraction and four-intent retrieval |
| RAG-007 | Explicit model/dimension compatibility and bounded input/output | Reopen, incompatible model/dimension and invalid-vector tests |
| RAG-008 | Named typed policies; shared validation/generation bounds and derived BM25 factors | Independent characterization of numeric scores, JSON/prompt limits and byte/character boundaries |
| RAG-009 | Authoritative GUI catalog source, initial load and incremental synchronization before every search | Add/change/delete, invalidation, reopen, failed scan, alias, root identity, CLI and stage-duration regressions |

## Contracts

`ToolRetriever(path, embeddings, keyword_generator, collection_name="agentix_tools")`
creates dedicated local storage. Construction never starts inference. Providers
implement `EmbeddingProvider` or `KeywordProvider`; model IDs are explicit.

`ToolDescriptor` contains tool_id, name, description, entrypoint, input_schema,
output_schema, keywords, artifact_ref and contract_digest. It has no approval,
testing or category fields. Schemas preserve Python type spellings and Annotated
parameter/return descriptions; they are metadata, not executable validators.
`descriptor_from_source` uses AST without imports or annotation evaluation. Its
digest conservatively fingerprints the complete supplied source, so any source
change changes the digest. The future catalog adapter must reconcile its own
contract identity and must independently check current eligibility.

`upsert(descriptor)` replaces by ID. `delete(tool_id)` is idempotent.
`search(query, keywords=None, limit=5)` returns SearchResult objects containing a
complete descriptor, one-based rank, RRF score, optional cosine/BM25 scores, mode
and keyword model identity. Scores are not probabilities or authorization.

## Retrieval policy

Ollama defaults: qwen3:14b for keyword generation, nomic-embed-text:latest for
embeddings, loopback HTTP, no redirects/proxies, 60-second timeout, no retries,
no model downloads. Keyword generation uses temperature zero and structured JSON:
at most 20 nonempty strings, each at most 100 characters. Invalid generation
falls back to the original query plus caller keywords; mode is keyword_fallback.
Invalid caller keywords raise ValueError. Embedding and storage errors propagate.

BM25 uses k1=1.5, b=0.75. Full Unicode identifiers and underscore/camel-case
segments participate, without a domain-specific vocabulary. Generated keywords
expand lexical retrieval; the original query drives semantic retrieval. Each
branch contributes up to min(collection size, max(20, 4*limit)) candidates. Equal
RRF contributions are 1/(60+rank); ties are resolved by tool_id. There is no
relevance threshold; callers receive candidates even for unrelated queries.

Limits: query 32 KiB UTF-8, limit 1..100, descriptor 256 KiB, tool ID 256
characters. Empty storage returns [] without inference. Vectors must be finite,
nonempty, nonzero and dimension-compatible. A changed model requires a separate
rebuilt index. Model tags must identify stable embedding semantics; replacement
of bytes behind an unchanged tag is not detected automatically.

Operations are serialized per instance. Multiple writers/processes are unsupported
without external coordination. BM25 rebuilds from stored descriptors on every
search; large-corpus optimization is deferred. Persisted descriptors are snapshots;
callers must upsert/delete after changes. Unbound registries require explicit updates. RAG-009 optionally binds an authoritative
catalog source and synchronizes before every search, as described below.

## Logging and privacy

Library loggers configure no global handlers. INFO covers operation/stage IDs,
outcomes, model identities, counts and elapsed milliseconds. DEBUG records hashed
tool identifiers, component scores and ranks. WARNING records keyword fallback;
ERROR records safe exception types. Queries, model responses, prompts, code and
exception bodies are omitted. Chroma persistence contains descriptor documents;
this is not an encrypted database. Host logging configuration owns retention.

## Test boundaries

Default tests use real temporary ChromaDB and deterministic provider doubles;
they establish persistence and ranking mechanics, not model quality. The four
copied tools are explicitly authorized static data, outside generated_tools;
only their implementations/specifications were copied, byte-for-byte. Source
hashes and origin are in tests/fixtures/tool_retrieval/provenance.json. No tool
source or copied tests are executed. Fixture snapshots are excluded from Ruff and
maintained-source reference generation to preserve original bytes.

Run `python -m pytest -m ollama_retrieval tests/test_retrieval_ollama.py` explicitly
for real local inference. It requires already installed models and fails on
unavailability; it never pulls models or restarts services. This evaluation is
separate from application-generation model acceptance and AppContainer evidence.

## RAG-008: Named policy refactoring

Internal `agentix.retrieval.policy` owns typed Final constants for input/storage/HTTP
limits, generation budgets, candidate counts, algorithm parameters, index version
and diagnostic units/display lengths. Each group documents its meaning and units.
Equal values with different semantics remain separate constants: for example,
keyword count and branch candidate floor are independent policies.

Contracts, JSON schema and keyword prompt share keyword bounds. BM25 computes
`k1 + 1` and `1 - b` instead of retaining separately hard-coded derived factors.
Conventional zeros, mathematical ones, AST positions and one-based ranks remain
literal where their role is intrinsic to the operation. The constants are internal,
not a new configuration API. Existing values, ranking, persistent schema and
exception types remain unchanged. Keyword count validation now prints the numeric
limit in its error message, consistent with other dynamic bound messages.

Characterization tests pin independent expectations before and after refactoring.
They deliberately retain literal expected values instead of importing production
constants, so an accidental policy change still fails the tests. No new inference,
agent integration or source execution is required for this maintenance change.

## RAG-009: Installed catalog synchronization

The optional `descriptor_source` constructor argument implements DescriptorSource:
its stable identity and snapshot() return a complete CatalogSnapshot of descriptors
and safe CatalogRejection records. CatalogToolSource receives the exact ToolCatalog
used by the GUI, or a ToolCatalog built from the same Settings.tools_root. It never
guesses deployment folders, parses GUI Markdown, imports tools or changes approvals.

Binding performs an initial synchronize(), including required document embeddings.
Every valid search synchronizes again while holding the instance lock. New and
changed descriptors are upserted; unchanged descriptors reuse stored vectors. Missing
code, deleted directories and rejected canonical entries are removed. Content hashes
detect changes even when size and mtime are unchanged. Source metadata is authoritative
for that dedicated collection; unrelated manually indexed entries are not adopted.

SyncReport and last_sync_report expose added/updated/removed/unchanged counts and
rejections. Explicit synchronize() refreshes without a search. Source identity is
persisted in collection metadata, and reopening requires the same bound source.
Root mutation, unrelated catalogs and unbound access to a bound index fail explicitly.
Existing schema/version and unbound descriptor APIs remain compatible.

A source snapshot reads only immediate conventional `<name>/<name>_code.py` files.
Canonical public functions become descriptors; legacy/noncanonical or invalid tools
are reported as unsupported instead of silently indexed under invented entrypoints.
Scans are bounded to 512 immediate entries and 64 KiB per source. Alias/hard-link,
regular-file, containment and before/after file-version checks protect ordinary
metadata reads. These checks do not establish race-proof isolation against a hostile
writer. No generated tool is ever imported or executed.

Missing/unreadable roots, incomplete scans, source replacement during a read and
provider/storage failures abort the operation; search never falls back to old results.
An existing empty root means all tools were removed. Completed source scans precede
reconciliation, and removals precede new embeddings. Writes are not transactional:
a failed reconciliation may be partially applied, and the next sync retries it.

This is synchronization at construction/search time, not a background filesystem
watcher. Changes after a snapshot are visible on the next synchronization; no claim
of atomicity with external GUI mutations is made. Multiwriter coordination remains
out of scope. No existing GUI process or agent wiring is changed.

`tools/sync_tool_registry.py` uses Settings.tools_root by default, honoring the same
AGENTIX_HOME/AGENTIX_TOOLS_ROOT inputs as GUI composition. --tools-root supports an
explicit launcher-resolved deployment root; --index selects dedicated Chroma storage
(default: sibling tool_registry). It prints a JSON summary and safe correlated logs.
It never downloads models or restarts services. The approved operational first load
uses the deployment receipt's physical root, not a guessed default shell location.
