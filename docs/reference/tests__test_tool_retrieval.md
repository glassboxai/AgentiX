# Reference for tests/test_tool_retrieval.py

Exercise hybrid retrieval without executing tool fixtures or contacting models.

Source fingerprint: c4c2eb85e2cfa7828ec98a1f111545fd027508a7bc14b0959610a290e33d5dd9

This reference is generated from maintained source without imports or execution. Assigned values are intentionally omitted. Runtime-dependent types are explicit; the enclosing docstring defines the behavioral contract. See [architecture](../ARCHITECTURE_QUALITY.md) for manually reviewed responsibility and dependency decisions.

## Classes and callables

### FakeEmbeddings

Provide stable semantic vectors without external services.

Kind: class. Declared return: Not declared / class. Source line: 13.

### FakeEmbeddings.embed

Map concepts to finite deterministic vectors.

Kind: callable. Declared return: list[list[float]]. Source line: 18.

### FakeKeywords

Return an injected JSON-equivalent keyword list or a safe simulated error.

Kind: class. Declared return: Not declared / class. Source line: 27.

### FakeKeywords.__init__

Remember the response and count actual generation requests.

Kind: callable. Declared return: None. Source line: 32.

### FakeKeywords.generate

Return configured keywords without logging the query.

Kind: callable. Declared return: list[str]. Source line: 36.

### descriptor

Build an independent complete tool descriptor.

Kind: callable. Declared return: ToolDescriptor. Source line: 44.

### retriever

Compose real temporary Chroma persistence with deterministic model boundaries.

Kind: callable. Declared return: ToolRetriever. Source line: 53.

### test_empty_and_validation

An empty registry avoids model calls and rejects invalid public inputs.

Kind: callable. Declared return: None. Source line: 58.

### test_persistence_update_delete

Descriptors survive reopening; replacement and deletion leave no stale matches.

Kind: callable. Declared return: None. Source line: 71.

### test_hybrid_identifiers_and_generated_keywords

Arbitrary identifiers and model-generated synonyms participate in retrieval.

Kind: callable. Declared return: None. Source line: 85.

### test_degraded_and_private_logs

Keyword failure remains observable without disclosing provider payloads.

Kind: callable. Declared return: None. Source line: 102.

### test_invalid_keyword_output_degrades

Malformed generator output cannot break the original lexical query.

Kind: callable. Declared return: None. Source line: 116.

### test_embedding_mismatch

Model identity and dimensions cannot silently mix in an existing index.

Kind: callable. Declared return: None. Source line: 123.

### test_embedding_failure_is_not_empty_result

Embedding exceptions remain explicit rather than reporting no matching tools.

Kind: callable. Declared return: None. Source line: 133.

### test_real_tool_snapshots

Retrieve all four real snapshots by intent without importing their Python.

Kind: callable. Declared return: None. Source line: 142.

## Variables and parameters

| Scope | Name | Role and meaning | Type | Lifetime | Writes |
| --- | --- | --- | --- | --- | --- |
| module | hashlib | Imported dependency for hashlib in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 3 |
| module | json | Imported dependency for json in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 4 |
| module | logging | Imported dependency for logging in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 5 |
| module | Path | Imported dependency for Path in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 6 |
| module | pytest | Imported dependency for pytest in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 8 |
| module | ToolDescriptor | Imported dependency for ToolDescriptor in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 10 |
| module | ToolRetriever | Imported dependency for ToolRetriever in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 10 |
| module | descriptor_from_source | Imported dependency for descriptor from source in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 10 |
| FakeEmbeddings | model_id | Local binding for model id in FakeEmbeddings; use the enclosing contract and type below. | str | Enclosing invocation or class/instance lifetime | 16 |
| FakeEmbeddings.embed | self | Owning instance; its attributes retain state for the instance lifetime. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 18 |
| FakeEmbeddings.embed | texts | Parameter for texts in FakeEmbeddings.embed; use the enclosing contract and type below. | list[str] | Enclosing invocation or class/instance lifetime | 18 |
| FakeEmbeddings.embed | groups | Local binding for groups in FakeEmbeddings.embed; use the enclosing contract and type below. | tuple | Enclosing invocation or class/instance lifetime | 20 |
| FakeEmbeddings.embed.comprehension_21.comprehension_22.comprehension_22 | term | Comprehension item for term in FakeEmbeddings.embed.comprehension_21.comprehension_22.comprehension_22; use the enclosing contract and type below. | Element of the declared iterable | This comprehension only; does not leak into its enclosing scope | 22 |
| FakeEmbeddings.embed.comprehension_21.comprehension_22 | group | Comprehension item for group in FakeEmbeddings.embed.comprehension_21.comprehension_22; use the enclosing contract and type below. | Element of the declared iterable | This comprehension only; does not leak into its enclosing scope | 22 |
| FakeEmbeddings.embed.comprehension_21 | text | Comprehension item for text in FakeEmbeddings.embed.comprehension_21; use the enclosing contract and type below. | Element of the declared iterable | This comprehension only; does not leak into its enclosing scope | 23 |
| FakeKeywords | model_id | Local binding for model id in FakeKeywords; use the enclosing contract and type below. | str | Enclosing invocation or class/instance lifetime | 30 |
| FakeKeywords.__init__ | self | Owning instance; its attributes retain state for the instance lifetime. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 32 |
| FakeKeywords.__init__ | result | Intermediate or returned outcome; consult the callable contract for trust/validation. | object | Enclosing invocation or class/instance lifetime | 32 |
| FakeKeywords.__init__ | error | Parameter for error in FakeKeywords.__init__; use the enclosing contract and type below. | bool | Enclosing invocation or class/instance lifetime | 32 |
| FakeKeywords.__init__ | self.result | Intermediate or returned outcome; consult the callable contract for trust/validation. | tuple | Enclosing invocation or class/instance lifetime | 34 |
| FakeKeywords.__init__ | self.error | Attribute for error in FakeKeywords.__init__; use the enclosing contract and type below. | tuple | Enclosing invocation or class/instance lifetime | 34 |
| FakeKeywords.__init__ | self.calls | Attribute for calls in FakeKeywords.__init__; use the enclosing contract and type below. | tuple | Enclosing invocation or class/instance lifetime | 34 |
| FakeKeywords.generate | self | Owning instance; its attributes retain state for the instance lifetime. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 36 |
| FakeKeywords.generate | query | Original user request or a trusted test query; avoid payload logging by default. | str | Enclosing invocation or class/instance lifetime | 36 |
| FakeKeywords.generate | self.calls | Attribute for calls in FakeKeywords.generate; use the enclosing contract and type below. | Preserved or operator-dependent type | Enclosing invocation or class/instance lifetime | 38 |
| descriptor | name | Current identifier selected by parsing, lookup or dependency registration. | str | Enclosing invocation or class/instance lifetime | 45 |
| descriptor | description | Parameter for description in descriptor; use the enclosing contract and type below. | str | Enclosing invocation or class/instance lifetime | 45 |
| retriever | tmp_path | Parameter for tmp path in retriever; use the enclosing contract and type below. | Path | Enclosing invocation or class/instance lifetime | 53 |
| retriever | keywords | Parameter for keywords in retriever; use the enclosing contract and type below. | FakeKeywords &#124; None | Enclosing invocation or class/instance lifetime | 53 |
| test_empty_and_validation | tmp_path | Parameter for tmp path in test_empty_and_validation; use the enclosing contract and type below. | Path | Enclosing invocation or class/instance lifetime | 58 |
| test_empty_and_validation | keywords | Local binding for keywords in test_empty_and_validation; use the enclosing contract and type below. | Return type of FakeKeywords; see its callable contract | Enclosing invocation or class/instance lifetime | 60 |
| test_empty_and_validation | service | Local binding for service in test_empty_and_validation; use the enclosing contract and type below. | Return type of retriever; see its callable contract | Enclosing invocation or class/instance lifetime | 61 |
| test_empty_and_validation | limit | Loop item for limit in test_empty_and_validation; use the enclosing contract and type below. | Element of the declared iterable | Enclosing invocation or class/instance lifetime | 64 |
| test_persistence_update_delete | tmp_path | Parameter for tmp path in test_persistence_update_delete; use the enclosing contract and type below. | Path | Enclosing invocation or class/instance lifetime | 71 |
| test_persistence_update_delete | service | Local binding for service in test_persistence_update_delete; use the enclosing contract and type below. | Return type of retriever; see its callable contract | Enclosing invocation or class/instance lifetime | 73 |
| test_persistence_update_delete | reopened | Local binding for reopened in test_persistence_update_delete; use the enclosing contract and type below. | Return type of retriever; see its callable contract | Enclosing invocation or class/instance lifetime | 75 |
| test_persistence_update_delete | updated | Local binding for updated in test_persistence_update_delete; use the enclosing contract and type below. | Return type of descriptor; see its callable contract | Enclosing invocation or class/instance lifetime | 77 |
| test_hybrid_identifiers_and_generated_keywords | tmp_path | Parameter for tmp path in test_hybrid_identifiers_and_generated_keywords; use the enclosing contract and type below. | Path | Enclosing invocation or class/instance lifetime | 85 |
| test_hybrid_identifiers_and_generated_keywords | keywords | Local binding for keywords in test_hybrid_identifiers_and_generated_keywords; use the enclosing contract and type below. | Return type of FakeKeywords; see its callable contract | Enclosing invocation or class/instance lifetime | 87 |
| test_hybrid_identifiers_and_generated_keywords | service | Local binding for service in test_hybrid_identifiers_and_generated_keywords; use the enclosing contract and type below. | Return type of retriever; see its callable contract | Enclosing invocation or class/instance lifetime | 88 |
| test_hybrid_identifiers_and_generated_keywords | results | Local binding for results in test_hybrid_identifiers_and_generated_keywords; use the enclosing contract and type below. | Return type of search; see its callable contract | Enclosing invocation or class/instance lifetime | 91, 95 |
| test_hybrid_identifiers_and_generated_keywords.comprehension_96 | item | Comprehension item for item in test_hybrid_identifiers_and_generated_keywords.comprehension_96; use the enclosing contract and type below. | Element of the declared iterable | This comprehension only; does not leak into its enclosing scope | 97 |
| test_degraded_and_private_logs | tmp_path | Parameter for tmp path in test_degraded_and_private_logs; use the enclosing contract and type below. | Path | Enclosing invocation or class/instance lifetime | 102 |
| test_degraded_and_private_logs | caplog | Parameter for caplog in test_degraded_and_private_logs; use the enclosing contract and type below. | pytest.LogCaptureFixture | Enclosing invocation or class/instance lifetime | 102 |
| test_degraded_and_private_logs | service | Local binding for service in test_degraded_and_private_logs; use the enclosing contract and type below. | Return type of retriever; see its callable contract | Enclosing invocation or class/instance lifetime | 104 |
| test_degraded_and_private_logs | results | Local binding for results in test_degraded_and_private_logs; use the enclosing contract and type below. | Return type of search; see its callable contract | Enclosing invocation or class/instance lifetime | 107 |
| test_invalid_keyword_output_degrades | tmp_path | Parameter for tmp path in test_invalid_keyword_output_degrades; use the enclosing contract and type below. | Path | Enclosing invocation or class/instance lifetime | 116 |
| test_invalid_keyword_output_degrades | terms | Parameter for terms in test_invalid_keyword_output_degrades; use the enclosing contract and type below. | object | Enclosing invocation or class/instance lifetime | 116 |
| test_invalid_keyword_output_degrades | service | Local binding for service in test_invalid_keyword_output_degrades; use the enclosing contract and type below. | Return type of retriever; see its callable contract | Enclosing invocation or class/instance lifetime | 118 |
| test_embedding_mismatch | tmp_path | Parameter for tmp path in test_embedding_mismatch; use the enclosing contract and type below. | Path | Enclosing invocation or class/instance lifetime | 123 |
| test_embedding_mismatch | service | Local binding for service in test_embedding_mismatch; use the enclosing contract and type below. | Return type of retriever; see its callable contract | Enclosing invocation or class/instance lifetime | 125 |
| test_embedding_mismatch | other | Local binding for other in test_embedding_mismatch; use the enclosing contract and type below. | Return type of FakeEmbeddings; see its callable contract | Enclosing invocation or class/instance lifetime | 127 |
| test_embedding_mismatch | other.model_id | Attribute for other.model id in test_embedding_mismatch; use the enclosing contract and type below. | str | Enclosing invocation or class/instance lifetime | 128 |
| test_embedding_failure_is_not_empty_result | tmp_path | Parameter for tmp path in test_embedding_failure_is_not_empty_result; use the enclosing contract and type below. | Path | Enclosing invocation or class/instance lifetime | 133 |
| test_embedding_failure_is_not_empty_result | service | Local binding for service in test_embedding_failure_is_not_empty_result; use the enclosing contract and type below. | Return type of retriever; see its callable contract | Enclosing invocation or class/instance lifetime | 135 |
| test_embedding_failure_is_not_empty_result | service.embeddings.embed | Attribute for service.embeddings.embed in test_embedding_failure_is_not_empty_result; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 137 |
| test_embedding_failure_is_not_empty_result.lambda_137 | texts | Callback parameter for texts in test_embedding_failure_is_not_empty_result.lambda_137; use the enclosing contract and type below. | Defined by the enclosing callback contract | Enclosing invocation or class/instance lifetime | 137 |
| test_embedding_failure_is_not_empty_result.lambda_137.comprehension_137 | _ | Comprehension item for  in test_embedding_failure_is_not_empty_result.lambda_137.comprehension_137; use the enclosing contract and type below. | Element of the declared iterable | This comprehension only; does not leak into its enclosing scope | 137 |
| test_real_tool_snapshots | tmp_path | Parameter for tmp path in test_real_tool_snapshots; use the enclosing contract and type below. | Path | Enclosing invocation or class/instance lifetime | 142 |
| test_real_tool_snapshots | root | Explicit root directory against which named paths are resolved. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 144 |
| test_real_tool_snapshots | manifest | Versioned inventory or launch record; not an execution-authorization capability. | Return type of loads; see its callable contract | Enclosing invocation or class/instance lifetime | 145 |
| test_real_tool_snapshots | service | Local binding for service in test_real_tool_snapshots; use the enclosing contract and type below. | Return type of retriever; see its callable contract | Enclosing invocation or class/instance lifetime | 146 |
| test_real_tool_snapshots | relative | Loop item for relative in test_real_tool_snapshots; use the enclosing contract and type below. | Element of the declared iterable | Enclosing invocation or class/instance lifetime | 147 |
| test_real_tool_snapshots | expected | Reviewed expected observation kept outside untrusted child execution. | Element of the declared iterable | Enclosing invocation or class/instance lifetime | 147 |
| test_real_tool_snapshots | name | Current identifier selected by parsing, lookup or dependency registration. | Element of the declared iterable | Enclosing invocation or class/instance lifetime | 149, 154 |
| test_real_tool_snapshots | source | Explicit source document or source-code text; never imported for reference generation. | Return type of read_text; see its callable contract | Enclosing invocation or class/instance lifetime | 150 |
| test_real_tool_snapshots | item | Local binding for item in test_real_tool_snapshots; use the enclosing contract and type below. | Return type of descriptor_from_source; see its callable contract | Enclosing invocation or class/instance lifetime | 151 |
| test_real_tool_snapshots | query | Original user request or a trusted test query; avoid payload logging by default. | Element of the declared iterable | Enclosing invocation or class/instance lifetime | 154 |
| test_real_tool_snapshots | first | Local binding for first in test_real_tool_snapshots; use the enclosing contract and type below. | list | Enclosing invocation or class/instance lifetime | 162 |
| test_real_tool_snapshots.comprehension_162 | item | Comprehension item for item in test_real_tool_snapshots.comprehension_162; use the enclosing contract and type below. | Element of the declared iterable | This comprehension only; does not leak into its enclosing scope | 162 |
| test_real_tool_snapshots.comprehension_163 | item | Comprehension item for item in test_real_tool_snapshots.comprehension_163; use the enclosing contract and type below. | Element of the declared iterable | This comprehension only; does not leak into its enclosing scope | 163 |
