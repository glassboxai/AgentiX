# Reference for src/agentix/agents/application_agents.py

Bounded local model transport and legacy compatibility application roles.

These agents propose artifacts, never approval. Engineering code/tests are not
produced through this service; only explicit application generation invokes it.

Source fingerprint: 4a6e3dcf57f9001bbf838111aef30f184a2b9b420396ef451541969c9cce23ad

This reference is generated from maintained source without imports or execution. Assigned values are intentionally omitted. Runtime-dependent types are explicit; the enclosing docstring defines the behavioral contract. See [architecture](../ARCHITECTURE_QUALITY.md) for manually reviewed responsibility and dependency decisions.

## Classes and callables

### WidgetProposal

Strict proposed artifact envelope; source remains untrusted data.

Kind: class. Declared return: Not declared / class. Source line: 52.

### LocalModelClient

Legacy pilot/fixture transport; production catalog creation uses CrewAI coordination.

Kind: class. Declared return: Not declared / class. Source line: 61.

### LocalModelClient.__init__

Inject operation evidence and a strict bounded HTTP wait in seconds.

The default remains 120 seconds. A composition root may explicitly allow
up to 600 seconds; invalid values fail before evidence or model activity.

Kind: callable. Declared return: None. Source line: 64.

### LocalModelClient.__call__

Persist exact request/response; propagate errors without automatic retries.

At most one application inference runs process-wide. The injected HTTP timeout
is bounded to 600 seconds; response is bounded; model residency is requested for 30 seconds.
Ollama is shared, so residency is a request, not ownership of the service.

Kind: callable. Declared return: dict. Source line: 76.

### validate_source

Filter syntax/imports/entry without importing generated code on the host.

This is not a sandbox and does not establish semantic correctness. Review
and native execution remain mandatory, including for module-level statements.

Kind: callable. Declared return: None. Source line: 150.

### validate_proposal_fields

Reject missing/extra keys and oversized/nonstring proposal fields.

Kind: callable. Declared return: None. Source line: 179.

### WidgetDesigner

Generate independent widget proposals from approved tool metadata only.

Kind: class. Declared return: Not declared / class. Source line: 193.

### WidgetDesigner.__init__

Inject the model boundary; construction performs no network operation.

Kind: callable. Declared return: None. Source line: 196.

### WidgetDesigner.generate

Request code/tests/notes, preserving the model implementation unchanged.

Kind: callable. Declared return: dict. Source line: 201.

## Variables and parameters

| Scope | Name | Role and meaning | Type | Lifetime | Writes |
| --- | --- | --- | --- | --- | --- |
| module | ast | Imported dependency for ast in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 7 |
| module | json | Imported dependency for json in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 8 |
| module | logging | Imported dependency for logging in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 9 |
| module | threading | Imported dependency for threading in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 10 |
| module | time | Imported dependency for time in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 11 |
| module | Callable | Imported dependency for Callable in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 12 |
| module | Path | Imported dependency for Path in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 13 |
| module | ProxyHandler | Imported dependency for ProxyHandler in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 14 |
| module | Request | Imported dependency for Request in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 14 |
| module | build_opener | Imported dependency for build opener in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 14 |
| module | uuid4 | Imported dependency for uuid4 in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 15 |
| module | BaseModel | Imported dependency for BaseModel in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 17 |
| module | ConfigDict | Imported dependency for ConfigDict in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 17 |
| module | Field | Imported dependency for Field in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 17 |
| module | decode_frame | Imported dependency for decode frame in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 19 |
| module | NoRedirect | Imported dependency for NoRedirect in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 20 |
| module | logger | Module logger emitting bounded operation diagnostics rather than artifact bodies. | Return type of getLogger; see its callable contract | Module/process lifetime | 22 |
| module | DEFAULT_MODEL_TIMEOUT_SECONDS | Module binding for DEFAULT MODEL TIMEOUT SECONDS in module; use the enclosing contract and type below. | int | Module/process lifetime | 25 |
| module | MAX_MODEL_TIMEOUT_SECONDS | Module binding for MAX MODEL TIMEOUT SECONDS in module; use the enclosing contract and type below. | int | Module/process lifetime | 26 |
| module | MODEL_KEEP_ALIVE | Module binding for MODEL KEEP ALIVE in module; use the enclosing contract and type below. | str | Module/process lifetime | 27 |
| module | MODEL_TEMPERATURE | Module binding for MODEL TEMPERATURE in module; use the enclosing contract and type below. | float | Module/process lifetime | 28 |
| module | MAX_MODEL_OUTPUT_TOKENS | Module binding for MAX MODEL OUTPUT TOKENS in module; use the enclosing contract and type below. | int | Module/process lifetime | 29 |
| module | MAX_MODEL_RESPONSE_BYTES | Module binding for MAX MODEL RESPONSE BYTES in module; use the enclosing contract and type below. | int | Module/process lifetime | 30 |
| module | MAX_PROPOSAL_FIELD_LENGTH | Module binding for MAX PROPOSAL FIELD LENGTH in module; use the enclosing contract and type below. | int | Module/process lifetime | 33 |
| module | MAX_PROPOSAL_FIELD_BYTES | Module binding for MAX PROPOSAL FIELD BYTES in module; use the enclosing contract and type below. | int | Module/process lifetime | 34 |
| module | MAX_APPLICATION_QUERY_LENGTH | Module binding for MAX APPLICATION QUERY LENGTH in module; use the enclosing contract and type below. | int | Module/process lifetime | 35 |
| module | ROLE_WIDGET_DESIGNER | Module binding for ROLE WIDGET DESIGNER in module; use the enclosing contract and type below. | str | Module/process lifetime | 38 |
| module | ROLE_GENERAL_WIDGET_DESIGNER | Module binding for ROLE GENERAL WIDGET DESIGNER in module; use the enclosing contract and type below. | str | Module/process lifetime | 39 |
| module | ROLE_GENERAL_ASSEMBLER | Module binding for ROLE GENERAL ASSEMBLER in module; use the enclosing contract and type below. | str | Module/process lifetime | 40 |
| module | APPLICATION_ROLES | Module binding for APPLICATION ROLES in module; use the enclosing contract and type below. | Return type of frozenset; see its callable contract | Module/process lifetime | 41 |
| module | MODEL_GATE | Module binding for MODEL GATE in module; use the enclosing contract and type below. | Return type of BoundedSemaphore; see its callable contract | Module/process lifetime | 49 |
| WidgetProposal | model_config | Local binding for model config in WidgetProposal; use the enclosing contract and type below. | Return type of ConfigDict; see its callable contract | Enclosing invocation or class/instance lifetime | 55 |
| WidgetProposal | widget_code | Typed binding for widget code in WidgetProposal; use the enclosing contract and type below. | str | Enclosing invocation or class/instance lifetime | 56 |
| WidgetProposal | tests_code | Typed binding for tests code in WidgetProposal; use the enclosing contract and type below. | str | Enclosing invocation or class/instance lifetime | 57 |
| WidgetProposal | notes | Typed binding for notes in WidgetProposal; use the enclosing contract and type below. | str | Enclosing invocation or class/instance lifetime | 58 |
| LocalModelClient.__init__ | self | Owning instance; its attributes retain state for the instance lifetime. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 64 |
| LocalModelClient.__init__ | evidence | Parameter for evidence in LocalModelClient.__init__; use the enclosing contract and type below. | Path | Enclosing invocation or class/instance lifetime | 64 |
| LocalModelClient.__init__ | timeout | Parameter for timeout in LocalModelClient.__init__; use the enclosing contract and type below. | int | Enclosing invocation or class/instance lifetime | 64 |
| LocalModelClient.__init__ | self.evidence | Attribute for evidence in LocalModelClient.__init__; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 72 |
| LocalModelClient.__init__ | self.timeout | Attribute for timeout in LocalModelClient.__init__; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 74 |
| LocalModelClient.__call__ | self | Owning instance; its attributes retain state for the instance lifetime. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 76 |
| LocalModelClient.__call__ | role | Parameter for role in LocalModelClient.__call__; use the enclosing contract and type below. | str | Enclosing invocation or class/instance lifetime | 76 |
| LocalModelClient.__call__ | content | Artifact or review text whose encoding, size and approval state must be checked. | dict | Enclosing invocation or class/instance lifetime | 76, 129 |
| LocalModelClient.__call__ | identity | Explicit owner identity used by a session factory or fixture. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 87 |
| LocalModelClient.__call__ | started | Local binding for started in LocalModelClient.__call__; use the enclosing contract and type below. | Return type of monotonic; see its callable contract | Enclosing invocation or class/instance lifetime | 88 |
| LocalModelClient.__call__ | ApplicationCode | Imported dependency for ApplicationCode in LocalModelClient.__call__; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 91 |
| LocalModelClient.__call__ | response_contract | Local binding for response contract in LocalModelClient.__call__; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 93 |
| LocalModelClient.__call__ | schema | Local binding for schema in LocalModelClient.__call__; use the enclosing contract and type below. | Return type of model_json_schema; see its callable contract | Enclosing invocation or class/instance lifetime | 94 |
| LocalModelClient.__call__ | payload | Local binding for payload in LocalModelClient.__call__; use the enclosing contract and type below. | dict | Enclosing invocation or class/instance lifetime | 95 |
| LocalModelClient.__call__ | stem | Local binding for stem in LocalModelClient.__call__; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 109 |
| LocalModelClient.__call__ | request | Local binding for request in LocalModelClient.__call__; use the enclosing contract and type below. | Return type of Request; see its callable contract | Enclosing invocation or class/instance lifetime | 114 |
| LocalModelClient.__call__ | response | Bounded response text to render or validate; it is not executable code. | Return type of open; see its callable contract | Context-manager block; exit invokes its cleanup protocol | 119 |
| LocalModelClient.__call__ | raw | Local binding for raw in LocalModelClient.__call__; use the enclosing contract and type below. | Return type of read; see its callable contract | Enclosing invocation or class/instance lifetime | 122 |
| LocalModelClient.__call__ | document | Structured reference/Word/AST document owned by the current authoring operation. | Return type of decode_frame; see its callable contract | Enclosing invocation or class/instance lifetime | 126 |
| LocalModelClient.__call__ | error | Caught exception for error in LocalModelClient.__call__; use the enclosing contract and type below. | Exception | Current exception handler; Python clears this binding afterward | 132 |
| validate_source | source | Explicit source document or source-code text; never imported for reference generation. | str | Enclosing invocation or class/instance lifetime | 150 |
| validate_source | imports | Parameter for imports in validate_source; use the enclosing contract and type below. | set[str] | Enclosing invocation or class/instance lifetime | 150 |
| validate_source | entry | Parameter for entry in validate_source; use the enclosing contract and type below. | str | Enclosing invocation or class/instance lifetime | 150 |
| validate_source | tree | Local binding for tree in validate_source; use the enclosing contract and type below. | Return type of parse; see its callable contract | Enclosing invocation or class/instance lifetime | 162 |
| validate_source | node | Loop item for node in validate_source; use the enclosing contract and type below. | Element of the declared iterable | Enclosing invocation or class/instance lifetime | 163 |
| validate_source.comprehension_170 | item | Comprehension item for item in validate_source.comprehension_170; use the enclosing contract and type below. | Element of the declared iterable | This comprehension only; does not leak into its enclosing scope | 170 |
| validate_source.comprehension_174 | node | Comprehension item for node in validate_source.comprehension_174; use the enclosing contract and type below. | Element of the declared iterable | This comprehension only; does not leak into its enclosing scope | 174 |
| validate_proposal_fields | candidate | Parameter for candidate in validate_proposal_fields; use the enclosing contract and type below. | dict | Enclosing invocation or class/instance lifetime | 179 |
| validate_proposal_fields | names | Parameter for names in validate_proposal_fields; use the enclosing contract and type below. | set[str] | Enclosing invocation or class/instance lifetime | 179 |
| validate_proposal_fields.comprehension_184 | name | Current identifier selected by parsing, lookup or dependency registration. | Element of the declared iterable | This comprehension only; does not leak into its enclosing scope | 187 |
| WidgetDesigner.__init__ | self | Owning instance; its attributes retain state for the instance lifetime. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 196 |
| WidgetDesigner.__init__ | client | Parameter for client in WidgetDesigner.__init__; use the enclosing contract and type below. | Callable | Enclosing invocation or class/instance lifetime | 196 |
| WidgetDesigner.__init__ | contracts | Parameter for contracts in WidgetDesigner.__init__; use the enclosing contract and type below. | dict &#124; None | Enclosing invocation or class/instance lifetime | 196 |
| WidgetDesigner.__init__ | self.client | Attribute for client in WidgetDesigner.__init__; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 198 |
| WidgetDesigner.__init__ | self.contracts | Attribute for contracts in WidgetDesigner.__init__; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 199 |
| WidgetDesigner.generate | self | Owning instance; its attributes retain state for the instance lifetime. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 201 |
| WidgetDesigner.generate | tool | Parameter for tool in WidgetDesigner.generate; use the enclosing contract and type below. | str | Enclosing invocation or class/instance lifetime | 201 |
| WidgetDesigner.generate | contract | Validated declarative acceptance data bound to current artifact identities. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 205 |
| WidgetDesigner.generate | content | Artifact or review text whose encoding, size and approval state must be checked. | dict | Enclosing invocation or class/instance lifetime | 206 |
| WidgetDesigner.generate | candidate | Local binding for candidate in WidgetDesigner.generate; use the enclosing contract and type below. | Return type of client; see its callable contract | Enclosing invocation or class/instance lifetime | 221 |
| module | _strings | Module binding for strings in module; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Module/process lifetime | 231 |
