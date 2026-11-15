# Reference for src/agentix/models/generation_identity.py

Local Ollama generation identity checks without model execution.

Source fingerprint: 750b2a3199c1e484ac5c17ad617da91606202ee342920f6913e34db2892a0ee6

This reference is generated from maintained source without imports or execution. Assigned values are intentionally omitted. Runtime-dependent types are explicit; the enclosing docstring defines the behavioral contract. See [architecture](../ARCHITECTURE_QUALITY.md) for manually reviewed responsibility and dependency decisions.

## Classes and callables

### _NoRedirects

Reject redirects so local model metadata cannot leave the selected endpoint.

Kind: class. Declared return: Not declared / class. Source line: 18.

### _NoRedirects.redirect_request

Deny every redirect without creating a replacement request.

Kind: callable. Declared return: None. Source line: 21.

### _catalog

Read bounded local model metadata without proxies, inference, or model pulls.

Kind: callable. Declared return: dict[str, Any]. Source line: 28.

### verify_generation_identity

Require an exact trusted local model digest before generation.

The check performs a bounded metadata read only. It rejects remote providers,
absent/malformed baselines, unavailable models, and changed identities.

Kind: callable. Declared return: str. Source line: 42.

### read_generation_identity

Return one current local model digest for explicit user review without inference.

Kind: callable. Declared return: str. Source line: 73.

## Variables and parameters

| Scope | Name | Role and meaning | Type | Lifetime | Writes |
| --- | --- | --- | --- | --- | --- |
| module | json | Imported dependency for json in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 3 |
| module | re | Imported dependency for re in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 4 |
| module | Callable | Imported dependency for Callable in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 5 |
| module | Any | Imported dependency for Any in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 6 |
| module | HTTPRedirectHandler | Imported dependency for HTTPRedirectHandler in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 7 |
| module | ProxyHandler | Imported dependency for ProxyHandler in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 7 |
| module | build_opener | Imported dependency for build opener in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 7 |
| module | ModelProfile | Imported dependency for ModelProfile in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 9 |
| module | _DIGEST | Module binding for DIGEST in module; use the enclosing contract and type below. | Return type of compile; see its callable contract | Module/process lifetime | 11 |
| module | CATALOG_TIMEOUT_SECONDS | Module binding for CATALOG TIMEOUT SECONDS in module; use the enclosing contract and type below. | int | Module/process lifetime | 13 |
| module | CATALOG_MAX_BYTES | Module binding for CATALOG MAX BYTES in module; use the enclosing contract and type below. | int | Module/process lifetime | 14 |
| module | CATALOG_READ_BYTES | Module binding for CATALOG READ BYTES in module; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Module/process lifetime | 15 |
| _NoRedirects.redirect_request | self | Owning instance; its attributes retain state for the instance lifetime. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 22 |
| _NoRedirects.redirect_request | req | Parameter for req in _NoRedirects.redirect_request; use the enclosing contract and type below. | Any | Enclosing invocation or class/instance lifetime | 22 |
| _NoRedirects.redirect_request | fp | Parameter for fp in _NoRedirects.redirect_request; use the enclosing contract and type below. | Any | Enclosing invocation or class/instance lifetime | 22 |
| _NoRedirects.redirect_request | code | Source snapshot passed through approval, syntax checks and isolated staging. | int | Enclosing invocation or class/instance lifetime | 22 |
| _NoRedirects.redirect_request | msg | Parameter for msg in _NoRedirects.redirect_request; use the enclosing contract and type below. | str | Enclosing invocation or class/instance lifetime | 22 |
| _NoRedirects.redirect_request | headers | Parameter for headers in _NoRedirects.redirect_request; use the enclosing contract and type below. | Any | Enclosing invocation or class/instance lifetime | 22 |
| _NoRedirects.redirect_request | newurl | Parameter for newurl in _NoRedirects.redirect_request; use the enclosing contract and type below. | str | Enclosing invocation or class/instance lifetime | 22 |
| _catalog | endpoint | Parameter for endpoint in _catalog; use the enclosing contract and type below. | str | Enclosing invocation or class/instance lifetime | 28 |
| _catalog | response | Bounded response text to render or validate; it is not executable code. | Return type of open; see its callable contract | Context-manager block; exit invokes its cleanup protocol | 30 |
| _catalog | body | Local binding for body in _catalog; use the enclosing contract and type below. | Return type of read; see its callable contract | Enclosing invocation or class/instance lifetime | 33 |
| _catalog | result | Intermediate or returned outcome; consult the callable contract for trust/validation. | Return type of loads; see its callable contract | Enclosing invocation or class/instance lifetime | 36 |
| verify_generation_identity | profile | Parameter for profile in verify_generation_identity; use the enclosing contract and type below. | ModelProfile | Enclosing invocation or class/instance lifetime | 43 |
| verify_generation_identity | trusted_digest | Parameter for trusted digest in verify_generation_identity; use the enclosing contract and type below. | str | Enclosing invocation or class/instance lifetime | 44 |
| verify_generation_identity | reader | Parameter for reader in verify_generation_identity; use the enclosing contract and type below. | Callable[[str], dict[str, Any]] | Enclosing invocation or class/instance lifetime | 46 |
| verify_generation_identity | models | Local binding for models in verify_generation_identity; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 61 |
| verify_generation_identity | matches | Local binding for matches in verify_generation_identity; use the enclosing contract and type below. | list | Enclosing invocation or class/instance lifetime | 62 |
| verify_generation_identity.comprehension_62 | item | Comprehension item for item in verify_generation_identity.comprehension_62; use the enclosing contract and type below. | Element of the declared iterable | This comprehension only; does not leak into its enclosing scope | 63 |
| verify_generation_identity | digest | Content fingerprint for change detection; not a substitute for human approval. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 65 |
| read_generation_identity | profile | Parameter for profile in read_generation_identity; use the enclosing contract and type below. | ModelProfile | Enclosing invocation or class/instance lifetime | 74 |
| read_generation_identity | reader | Parameter for reader in read_generation_identity; use the enclosing contract and type below. | Callable[[str], dict[str, Any]] | Enclosing invocation or class/instance lifetime | 74 |
| read_generation_identity | models | Local binding for models in read_generation_identity; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 81 |
| read_generation_identity | matches | Local binding for matches in read_generation_identity; use the enclosing contract and type below. | list | Enclosing invocation or class/instance lifetime | 82 |
| read_generation_identity.comprehension_82 | item | Comprehension item for item in read_generation_identity.comprehension_82; use the enclosing contract and type below. | Element of the declared iterable | This comprehension only; does not leak into its enclosing scope | 83 |
| read_generation_identity | digest | Content fingerprint for change detection; not a substitute for human approval. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 85 |
