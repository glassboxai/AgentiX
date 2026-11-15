# Reference for src/agentix/controllers/chathelper.py

Owner-checked context chat controller; no Gradio dependency or file editing.

Source fingerprint: 278bbc82362a18544c89d5d47af9f56ec1f25998c14c6522898209fa2c0cfcd4

This reference is generated from maintained source without imports or execution. Assigned values are intentionally omitted. Runtime-dependent types are explicit; the enclosing docstring defines the behavioral contract. See [architecture](../ARCHITECTURE_QUALITY.md) for manually reviewed responsibility and dependency decisions.

## Classes and callables

### ChatHelperBackend

Resolve selected pending-review context and retain history on its session owner.

Kind: class. Declared return: Not declared / class. Source line: 15.

### ChatHelperBackend.__init__

Inject owner registry, application controller and provider composition boundary.

Kind: callable. Declared return: Not declared / class. Source line: 18.

### ChatHelperBackend.ask

Explain current editor text using only its verified tool's specification/contract.

Browser file names are resolved through the application's finite review list.
Source is treated as data, never opened as a path or executed. Histories
remain session-local and reset when the file or editor buffer changes.

Kind: callable. Declared return: Not declared / class. Source line: 23.

## Variables and parameters

| Scope | Name | Role and meaning | Type | Lifetime | Writes |
| --- | --- | --- | --- | --- | --- |
| module | hashlib | Imported dependency for hashlib in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 3 |
| module | json | Imported dependency for json in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 4 |
| module | ApplicationReview | Imported dependency for ApplicationReview in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 6 |
| module | explain_code | Imported dependency for explain code in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 7 |
| module | SessionOwnerAccess | Imported dependency for SessionOwnerAccess in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 8 |
| module | create_profile_llm | Imported dependency for create profile llm in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 9 |
| module | HISTORY_MESSAGE_LIMIT | Module binding for HISTORY MESSAGE LIMIT in module; use the enclosing contract and type below. | int | Module/process lifetime | 11 |
| module | SPECIFICATION_READ_LIMIT | Module binding for SPECIFICATION READ LIMIT in module; use the enclosing contract and type below. | int | Module/process lifetime | 12 |
| ChatHelperBackend.__init__ | self | Owning instance; its attributes retain state for the instance lifetime. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 18 |
| ChatHelperBackend.__init__ | registry | Parameter for registry in ChatHelperBackend.__init__; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 18 |
| ChatHelperBackend.__init__ | applications | Parameter for applications in ChatHelperBackend.__init__; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 18 |
| ChatHelperBackend.__init__ | client_factory | Parameter for client factory in ChatHelperBackend.__init__; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 18 |
| ChatHelperBackend.__init__ | self.applications | Attribute for applications in ChatHelperBackend.__init__; use the enclosing contract and type below. | tuple | Enclosing invocation or class/instance lifetime | 21 |
| ChatHelperBackend.__init__ | self.client_factory | Attribute for client factory in ChatHelperBackend.__init__; use the enclosing contract and type below. | tuple | Enclosing invocation or class/instance lifetime | 21 |
| ChatHelperBackend.ask | self | Owning instance; its attributes retain state for the instance lifetime. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 23 |
| ChatHelperBackend.ask | pane | Parameter for pane in ChatHelperBackend.ask; use the enclosing contract and type below. | str | Enclosing invocation or class/instance lifetime | 23 |
| ChatHelperBackend.ask | selected | Parameter for selected in ChatHelperBackend.ask; use the enclosing contract and type below. | str | Enclosing invocation or class/instance lifetime | 23 |
| ChatHelperBackend.ask | source | Explicit source document or source-code text; never imported for reference generation. | str | Enclosing invocation or class/instance lifetime | 23 |
| ChatHelperBackend.ask | question | Parameter for question in ChatHelperBackend.ask; use the enclosing contract and type below. | str | Enclosing invocation or class/instance lifetime | 23 |
| ChatHelperBackend.ask | token | Parameter for token in ChatHelperBackend.ask; use the enclosing contract and type below. | str &#124; None | Enclosing invocation or class/instance lifetime | 23 |
| ChatHelperBackend.ask | request | Parameter for request in ChatHelperBackend.ask; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 23 |
| ChatHelperBackend.ask | session | Local binding for session in ChatHelperBackend.ask; use the enclosing contract and type below. | Return type of _resolve; see its callable contract | Enclosing invocation or class/instance lifetime | 30 |
| ChatHelperBackend.ask | state | Owner-local mutable workflow/UI state guarded by its documented synchronization. | Return type of _resolve; see its callable contract | Enclosing invocation or class/instance lifetime | 30 |
| ChatHelperBackend.ask | controller | Local binding for controller in ChatHelperBackend.ask; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 31 |
| ChatHelperBackend.ask | related | Local binding for related in ChatHelperBackend.ask; use the enclosing contract and type below. | Return type of panes; see its callable contract | Enclosing invocation or class/instance lifetime | 41 |
| ChatHelperBackend.ask | contract | Validated declarative acceptance data bound to current artifact identities. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 42 |
| ChatHelperBackend.ask | tool_name | Validated public tool identifier within the configured storage boundary. | Return type of removesuffix; see its callable contract | Enclosing invocation or class/instance lifetime | 43 |
| ChatHelperBackend.ask | spec_path | Local binding for spec path in ChatHelperBackend.ask; use the enclosing contract and type below. | Return type of validate_and_resolve_path; see its callable contract | Enclosing invocation or class/instance lifetime | 44 |
| ChatHelperBackend.ask | stream | Managed resource for stream in ChatHelperBackend.ask; use the enclosing contract and type below. | Return type of open; see its callable contract | Context-manager block; exit invokes its cleanup protocol | 47 |
| ChatHelperBackend.ask | specification | Local binding for specification in ChatHelperBackend.ask; use the enclosing contract and type below. | Return type of read; see its callable contract | Enclosing invocation or class/instance lifetime | 48 |
| ChatHelperBackend.ask | suffix | Local binding for suffix in ChatHelperBackend.ask; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 49 |
| ChatHelperBackend.ask | context | Local binding for context in ChatHelperBackend.ask; use the enclosing contract and type below. | dict | Enclosing invocation or class/instance lifetime | 55 |
| ChatHelperBackend.ask | scope | Local binding for scope in ChatHelperBackend.ask; use the enclosing contract and type below. | Return type of hexdigest; see its callable contract | Enclosing invocation or class/instance lifetime | 65 |
| ChatHelperBackend.ask | owned | Local binding for owned in ChatHelperBackend.ask; use the enclosing contract and type below. | Return type of getattr; see its callable contract | Enclosing invocation or class/instance lifetime | 66 |
| ChatHelperBackend.ask | history | Local binding for history in ChatHelperBackend.ask; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 67, 73 |
| ChatHelperBackend.ask | configuration | Local binding for configuration in ChatHelperBackend.ask; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 68 |
| ChatHelperBackend.ask | client | Local binding for client in ChatHelperBackend.ask; use the enclosing contract and type below. | Return type of client_factory; see its callable contract | Enclosing invocation or class/instance lifetime | 69 |
| ChatHelperBackend.ask | answer | Local binding for answer in ChatHelperBackend.ask; use the enclosing contract and type below. | Return type of explain_code; see its callable contract | Enclosing invocation or class/instance lifetime | 72 |
| ChatHelperBackend.ask | controller._code_help | Attribute for controller. code help in ChatHelperBackend.ask; use the enclosing contract and type below. | dict | Enclosing invocation or class/instance lifetime | 78 |
| ChatHelperBackend.ask | transcript | Local binding for transcript in ChatHelperBackend.ask; use the enclosing contract and type below. | Return type of join; see its callable contract | Enclosing invocation or class/instance lifetime | 79 |
| ChatHelperBackend.ask.comprehension_79 | entry | Comprehension item for entry in ChatHelperBackend.ask.comprehension_79; use the enclosing contract and type below. | Element of the declared iterable | This comprehension only; does not leak into its enclosing scope | 81 |
