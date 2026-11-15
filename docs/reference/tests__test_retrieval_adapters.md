# Reference for tests/test_retrieval_adapters.py

Validate Ollama transport contracts without network or model execution.

Source fingerprint: c08eb9d9a07f3b7b41a524b5b4c14bd2a5f16063e19cdb71b61160c220ac64ec

This reference is generated from maintained source without imports or execution. Assigned values are intentionally omitted. Runtime-dependent types are explicit; the enclosing docstring defines the behavioral contract. See [architecture](../ARCHITECTURE_QUALITY.md) for manually reviewed responsibility and dependency decisions.

## Classes and callables

### StubClient

Capture generated requests without contacting any endpoint.

Kind: class. Declared return: Not declared / class. Source line: 13.

### StubClient.__init__

Remember a synthetic response and the most recent request.

Kind: callable. Declared return: None. Source line: 16.

### StubClient.post

Record a request and return the configured response.

Kind: callable. Declared return: dict. Source line: 22.

### test_keyword_adapter_contract

Use bounded structured local generation and preserve arbitrary domain terms.

Kind: callable. Declared return: None. Source line: 28.

### test_keyword_adapter_rejects_invalid_response

Reject malformed output before it can influence lexical ranking.

Kind: callable. Declared return: None. Source line: 40.

### test_embedding_adapter_contract

Request embeddings without truncation or model installation.

Kind: callable. Declared return: None. Source line: 46.

### test_remote_endpoint_rejected

Reject nonlocal destinations and endpoint credentials before any I/O.

Kind: callable. Declared return: None. Source line: 65.

### test_http_boundary_is_bounded_and_sanitizes_errors

Never reveal provider exception bodies or silently retry requests.

Kind: callable. Declared return: None. Source line: 71.

### test_http_boundary_is_bounded_and_sanitizes_errors.BrokenOpener

Simulate a failing transport with a sensitive exception message.

Kind: class. Declared return: Not declared / class. Source line: 75.

### test_http_boundary_is_bounded_and_sanitizes_errors.BrokenOpener.open

Count attempts and fail before network access.

Kind: callable. Declared return: None. Source line: 78.

### test_lexical_segmentation_and_zero_match

Split arbitrary identifiers while keeping their complete searchable spelling.

Kind: callable. Declared return: None. Source line: 90.

### test_bad_embeddings_rejected

Malformed model output cannot become a persisted tool entry.

Kind: callable. Declared return: None. Source line: 98.

### test_dimension_change_and_invalid_descriptors

Reject incompatible vectors and incomplete descriptors without losing old entries.

Kind: callable. Declared return: None. Source line: 108.

### test_rrf_ties_are_stable

Equal candidates are ordered by ID and expose RRF rank contributions.

Kind: callable. Declared return: None. Source line: 119.

### test_fixture_sources_are_not_maintained_code

Preserved source snapshots are data, not reference-generation targets.

Kind: callable. Declared return: None. Source line: 130.

### test_import_is_inert_and_independent

Import in a fresh interpreter without loading CrewAI, Chroma or model clients.

Kind: callable. Declared return: None. Source line: 138.

### test_finished_stage_durations_are_measured

Report measured persistence, snapshot and ranking times rather than placeholder zeros.

Kind: callable. Declared return: None. Source line: 154.

## Variables and parameters

| Scope | Name | Role and meaning | Type | Lifetime | Writes |
| --- | --- | --- | --- | --- | --- |
| module | json | Imported dependency for json in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 3 |
| module | Path | Imported dependency for Path in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 4 |
| module | pytest | Imported dependency for pytest in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 6 |
| module | FakeEmbeddings | Imported dependency for FakeEmbeddings in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 7 |
| module | FakeKeywords | Imported dependency for FakeKeywords in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 7 |
| module | descriptor | Imported dependency for descriptor in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 7 |
| module | retriever | Imported dependency for retriever in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 7 |
| module | OllamaClient | Imported dependency for OllamaClient in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 9 |
| module | OllamaEmbeddings | Imported dependency for OllamaEmbeddings in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 9 |
| module | OllamaKeywords | Imported dependency for OllamaKeywords in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 9 |
| module | ToolRetriever | Imported dependency for ToolRetriever in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 9 |
| module | bm25 | Imported dependency for bm25 in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 10 |
| module | tokens | Imported dependency for tokens in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 10 |
| StubClient.__init__ | self | Owning instance; its attributes retain state for the instance lifetime. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 16 |
| StubClient.__init__ | response | Bounded response text to render or validate; it is not executable code. | dict | Enclosing invocation or class/instance lifetime | 16 |
| StubClient.__init__ | self.response | Bounded response text to render or validate; it is not executable code. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 18 |
| StubClient.__init__ | self.route | Attribute for route in StubClient.__init__; use the enclosing contract and type below. | str | Enclosing invocation or class/instance lifetime | 19 |
| StubClient.__init__ | self.payload | Attribute for payload in StubClient.__init__; use the enclosing contract and type below. | dict | Enclosing invocation or class/instance lifetime | 20 |
| StubClient.post | self | Owning instance; its attributes retain state for the instance lifetime. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 22 |
| StubClient.post | route | Parameter for route in StubClient.post; use the enclosing contract and type below. | str | Enclosing invocation or class/instance lifetime | 22 |
| StubClient.post | payload | Parameter for payload in StubClient.post; use the enclosing contract and type below. | dict | Enclosing invocation or class/instance lifetime | 22 |
| StubClient.post | self.route | Attribute for route in StubClient.post; use the enclosing contract and type below. | tuple | Enclosing invocation or class/instance lifetime | 24 |
| StubClient.post | self.payload | Attribute for payload in StubClient.post; use the enclosing contract and type below. | tuple | Enclosing invocation or class/instance lifetime | 24 |
| test_keyword_adapter_contract | client | Local binding for client in test_keyword_adapter_contract; use the enclosing contract and type below. | Return type of StubClient; see its callable contract | Enclosing invocation or class/instance lifetime | 30 |
| test_keyword_adapter_rejects_invalid_response | response | Bounded response text to render or validate; it is not executable code. | object | Enclosing invocation or class/instance lifetime | 40 |
| test_embedding_adapter_contract | client | Local binding for client in test_embedding_adapter_contract; use the enclosing contract and type below. | Return type of StubClient; see its callable contract | Enclosing invocation or class/instance lifetime | 48 |
| test_remote_endpoint_rejected | endpoint | Parameter for endpoint in test_remote_endpoint_rejected; use the enclosing contract and type below. | str | Enclosing invocation or class/instance lifetime | 65 |
| test_http_boundary_is_bounded_and_sanitizes_errors | monkeypatch | Parameter for monkeypatch in test_http_boundary_is_bounded_and_sanitizes_errors; use the enclosing contract and type below. | pytest.MonkeyPatch | Enclosing invocation or class/instance lifetime | 71 |
| test_http_boundary_is_bounded_and_sanitizes_errors | calls | Local binding for calls in test_http_boundary_is_bounded_and_sanitizes_errors; use the enclosing contract and type below. | list | Enclosing invocation or class/instance lifetime | 73 |
| test_http_boundary_is_bounded_and_sanitizes_errors.BrokenOpener.open | self | Owning instance; its attributes retain state for the instance lifetime. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 78 |
| test_http_boundary_is_bounded_and_sanitizes_errors.BrokenOpener.open | request | Parameter for request in test_http_boundary_is_bounded_and_sanitizes_errors.BrokenOpener.open; use the enclosing contract and type below. | object | Enclosing invocation or class/instance lifetime | 78 |
| test_http_boundary_is_bounded_and_sanitizes_errors.BrokenOpener.open | timeout | Parameter for timeout in test_http_boundary_is_bounded_and_sanitizes_errors.BrokenOpener.open; use the enclosing contract and type below. | float | Enclosing invocation or class/instance lifetime | 78 |
| test_http_boundary_is_bounded_and_sanitizes_errors | error | Managed resource for error in test_http_boundary_is_bounded_and_sanitizes_errors; use the enclosing contract and type below. | Return type of raises; see its callable contract | Context-manager block; exit invokes its cleanup protocol | 84 |
| test_lexical_segmentation_and_zero_match | terms | Local binding for terms in test_lexical_segmentation_and_zero_match; use the enclosing contract and type below. | Return type of tokens; see its callable contract | Enclosing invocation or class/instance lifetime | 92 |
| test_bad_embeddings_rejected | tmp_path | Parameter for tmp path in test_bad_embeddings_rejected; use the enclosing contract and type below. | Path | Enclosing invocation or class/instance lifetime | 98 |
| test_bad_embeddings_rejected | vector | Parameter for vector in test_bad_embeddings_rejected; use the enclosing contract and type below. | list | Enclosing invocation or class/instance lifetime | 98 |
| test_bad_embeddings_rejected | provider | Local binding for provider in test_bad_embeddings_rejected; use the enclosing contract and type below. | Return type of FakeEmbeddings; see its callable contract | Enclosing invocation or class/instance lifetime | 100 |
| test_bad_embeddings_rejected | provider.embed | Attribute for provider.embed in test_bad_embeddings_rejected; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 101 |
| test_bad_embeddings_rejected.lambda_101 | texts | Callback parameter for texts in test_bad_embeddings_rejected.lambda_101; use the enclosing contract and type below. | Defined by the enclosing callback contract | Enclosing invocation or class/instance lifetime | 101 |
| test_bad_embeddings_rejected | service | Local binding for service in test_bad_embeddings_rejected; use the enclosing contract and type below. | Return type of ToolRetriever; see its callable contract | Enclosing invocation or class/instance lifetime | 102 |
| test_dimension_change_and_invalid_descriptors | tmp_path | Parameter for tmp path in test_dimension_change_and_invalid_descriptors; use the enclosing contract and type below. | Path | Enclosing invocation or class/instance lifetime | 108 |
| test_dimension_change_and_invalid_descriptors | service | Local binding for service in test_dimension_change_and_invalid_descriptors; use the enclosing contract and type below. | Return type of retriever; see its callable contract | Enclosing invocation or class/instance lifetime | 110 |
| test_dimension_change_and_invalid_descriptors | service.embeddings.embed | Attribute for service.embeddings.embed in test_dimension_change_and_invalid_descriptors; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 112 |
| test_dimension_change_and_invalid_descriptors.lambda_112 | texts | Callback parameter for texts in test_dimension_change_and_invalid_descriptors.lambda_112; use the enclosing contract and type below. | Defined by the enclosing callback contract | Enclosing invocation or class/instance lifetime | 112 |
| test_rrf_ties_are_stable | tmp_path | Parameter for tmp path in test_rrf_ties_are_stable; use the enclosing contract and type below. | Path | Enclosing invocation or class/instance lifetime | 119 |
| test_rrf_ties_are_stable | service | Local binding for service in test_rrf_ties_are_stable; use the enclosing contract and type below. | Return type of retriever; see its callable contract | Enclosing invocation or class/instance lifetime | 121 |
| test_rrf_ties_are_stable | matches | Local binding for matches in test_rrf_ties_are_stable; use the enclosing contract and type below. | Return type of search; see its callable contract | Enclosing invocation or class/instance lifetime | 124 |
| test_rrf_ties_are_stable.comprehension_125 | item | Comprehension item for item in test_rrf_ties_are_stable.comprehension_125; use the enclosing contract and type below. | Element of the declared iterable | This comprehension only; does not leak into its enclosing scope | 125 |
| test_fixture_sources_are_not_maintained_code | maintained_sources | Imported dependency for maintained sources in test_fixture_sources_are_not_maintained_code; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 132 |
| test_fixture_sources_are_not_maintained_code | root | Explicit root directory against which named paths are resolved. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 134 |
| test_fixture_sources_are_not_maintained_code.comprehension_135 | path | Path under validation or an explicitly scoped maintained source path. | Element of the declared iterable | This comprehension only; does not leak into its enclosing scope | 135 |
| test_import_is_inert_and_independent | subprocess | Imported dependency for subprocess in test_import_is_inert_and_independent; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 140 |
| test_import_is_inert_and_independent | sys | Imported dependency for sys in test_import_is_inert_and_independent; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 141 |
| test_import_is_inert_and_independent | source | Explicit source document or source-code text; never imported for reference generation. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 143 |
| test_import_is_inert_and_independent | script | Local binding for script in test_import_is_inert_and_independent; use the enclosing contract and type below. | str | Enclosing invocation or class/instance lifetime | 144 |
| test_import_is_inert_and_independent | completed | Local binding for completed in test_import_is_inert_and_independent; use the enclosing contract and type below. | Return type of run; see its callable contract | Enclosing invocation or class/instance lifetime | 148 |
| test_finished_stage_durations_are_measured | tmp_path | Parameter for tmp path in test_finished_stage_durations_are_measured; use the enclosing contract and type below. | Path | Enclosing invocation or class/instance lifetime | 155 |
| test_finished_stage_durations_are_measured | caplog | Parameter for caplog in test_finished_stage_durations_are_measured; use the enclosing contract and type below. | pytest.LogCaptureFixture | Enclosing invocation or class/instance lifetime | 155 |
| test_finished_stage_durations_are_measured | logging | Imported dependency for logging in test_finished_stage_durations_are_measured; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 158 |
| test_finished_stage_durations_are_measured | re | Imported dependency for re in test_finished_stage_durations_are_measured; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 159 |
| test_finished_stage_durations_are_measured | service | Local binding for service in test_finished_stage_durations_are_measured; use the enclosing contract and type below. | Return type of retriever; see its callable contract | Enclosing invocation or class/instance lifetime | 162 |
| test_finished_stage_durations_are_measured | durations | Local binding for durations in test_finished_stage_durations_are_measured; use the enclosing contract and type below. | Return type of findall; see its callable contract | Enclosing invocation or class/instance lifetime | 165 |
| test_finished_stage_durations_are_measured.comprehension_170 | value | Value at the current validation/rendering boundary; apply the enclosing contract. | Element of the declared iterable | This comprehension only; does not leak into its enclosing scope | 170 |
