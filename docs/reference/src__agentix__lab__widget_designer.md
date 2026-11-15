# Reference for src/agentix/lab/widget_designer.py

Real local Ollama Widget Designer; generates runtime artifacts, never engineering code.

Source fingerprint: b7e82dc6e67a91567d7976c148ced9d5a0d97c4da4353d3bdc09c29c5721793c

This reference is generated from maintained source without imports or execution. Assigned values are intentionally omitted. Runtime-dependent types are explicit; the enclosing docstring defines the behavioral contract. See [architecture](../ARCHITECTURE_QUALITY.md) for manually reviewed responsibility and dependency decisions.

## Classes and callables

### NoRedirect

Keep generation requests at the explicitly selected loopback service.

Kind: class. Declared return: Not declared / class. Source line: 11.

### NoRedirect.redirect_request

Reject redirects without forwarding the local prompt.

Kind: callable. Declared return: Not declared / class. Source line: 14.

### generate_widget

Generate one candidate with qwen3-coder:30b, persist and validate; do not approve.

Kind: callable. Declared return: str. Source line: 19.

## Variables and parameters

| Scope | Name | Role and meaning | Type | Lifetime | Writes |
| --- | --- | --- | --- | --- | --- |
| module | json | Imported dependency for json in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 3 |
| module | Path | Imported dependency for Path in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 4 |
| module | HTTPRedirectHandler | Imported dependency for HTTPRedirectHandler in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 5 |
| module | ProxyHandler | Imported dependency for ProxyHandler in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 5 |
| module | Request | Imported dependency for Request in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 5 |
| module | build_opener | Imported dependency for build opener in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 5 |
| module | CONTRACT | Imported dependency for CONTRACT in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 7 |
| module | package_digest | Imported dependency for package digest in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 7 |
| module | validate_widget | Imported dependency for validate widget in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 7 |
| module | TESTS_FILENAME | Imported dependency for TESTS FILENAME in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 8 |
| module | TOOL_FILENAME | Imported dependency for TOOL FILENAME in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 8 |
| module | WIDGET_FILENAME | Imported dependency for WIDGET FILENAME in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 8 |
| NoRedirect.redirect_request | self | Owning instance; its attributes retain state for the instance lifetime. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 14 |
| NoRedirect.redirect_request | args | Parameter for args in NoRedirect.redirect_request; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 14 |
| NoRedirect.redirect_request | kwargs | Bounded JSON keyword arguments; no executable objects are accepted. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 14 |
| generate_widget | folder | Parameter for folder in generate_widget; use the enclosing contract and type below. | Path | Enclosing invocation or class/instance lifetime | 19 |
| generate_widget | system | Local binding for system in generate_widget; use the enclosing contract and type below. | str | Enclosing invocation or class/instance lifetime | 21 |
| generate_widget | payload | Local binding for payload in generate_widget; use the enclosing contract and type below. | dict | Enclosing invocation or class/instance lifetime | 22 |
| generate_widget | request | Local binding for request in generate_widget; use the enclosing contract and type below. | Return type of Request; see its callable contract | Enclosing invocation or class/instance lifetime | 36 |
| generate_widget | opener | Local binding for opener in generate_widget; use the enclosing contract and type below. | Return type of build_opener; see its callable contract | Enclosing invocation or class/instance lifetime | 41 |
| generate_widget | response | Bounded response text to render or validate; it is not executable code. | Return type of open; see its callable contract | Context-manager block; exit invokes its cleanup protocol | 42 |
| generate_widget | raw | Local binding for raw in generate_widget; use the enclosing contract and type below. | Return type of read; see its callable contract | Enclosing invocation or class/instance lifetime | 43 |
| generate_widget | document | Structured reference/Word/AST document owned by the current authoring operation. | Return type of loads; see its callable contract | Enclosing invocation or class/instance lifetime | 46 |
| generate_widget | candidate | Local binding for candidate in generate_widget; use the enclosing contract and type below. | Return type of loads; see its callable contract | Enclosing invocation or class/instance lifetime | 47 |
| generate_widget.comprehension_48 | value | Value at the current validation/rendering boundary; apply the enclosing contract. | Element of the declared iterable | This comprehension only; does not leak into its enclosing scope | 49 |
| generate_widget.comprehension_52 | value | Value at the current validation/rendering boundary; apply the enclosing contract. | Element of the declared iterable | This comprehension only; does not leak into its enclosing scope | 52 |
