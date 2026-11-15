# Reference for src/agentix/retrieval/ollama.py

Local-only bounded Ollama adapters; no model pulls, retries or remote endpoints.

Source fingerprint: 345dadc7b3c2f57bab8fecd9dcf868e6e004c1b3c1164aa2606768d70942839c

This reference is generated from maintained source without imports or execution. Assigned values are intentionally omitted. Runtime-dependent types are explicit; the enclosing docstring defines the behavioral contract. See [architecture](../ARCHITECTURE_QUALITY.md) for manually reviewed responsibility and dependency decisions.

## Classes and callables

### _NoRedirects

Prevent a local provider from redirecting payloads to another destination.

Kind: class. Declared return: Not declared / class. Source line: 14.

### _NoRedirects.redirect_request

Reject every redirect rather than forwarding prompts or source metadata.

Kind: callable. Declared return: None. Source line: 17.

### OllamaClient

Perform bounded JSON POSTs to explicitly local Ollama endpoints.

No environment proxy is used. Responses are limited to 1 MiB and requests to
2 MiB. Provider exceptions are sanitized, with no raw response/prompt logging.

Kind: class. Declared return: Not declared / class. Source line: 24.

### OllamaClient.__init__

Validate a loopback endpoint and positive finite timeout; perform no I/O.

Kind: callable. Declared return: None. Source line: 31.

### OllamaClient.post

Return bounded JSON from a fixed API route or raise a sanitized RuntimeError.

Kind: callable. Declared return: dict. Source line: 56.

### OllamaKeywords

Generate search terms with an installed local model and strict JSON validation.

Kind: class. Declared return: Not declared / class. Source line: 82.

### OllamaKeywords.__init__

Inject the HTTP boundary and explicit model; never download models.

Kind: callable. Declared return: None. Source line: 85.

### OllamaKeywords.generate

Extract at most twenty terms; malformed or oversized responses raise ValueError.

Kind: callable. Declared return: list[str]. Source line: 89.

### OllamaEmbeddings

Embed explicit text batches using an installed local embedding model.

Kind: class. Declared return: Not declared / class. Source line: 123.

### OllamaEmbeddings.__init__

Inject HTTP and model identity without inference during construction.

Kind: callable. Declared return: None. Source line: 126.

### OllamaEmbeddings.embed

Return Ollama vectors; the retriever validates shape, finiteness and dimension.

Kind: callable. Declared return: list[list[float]]. Source line: 130.

## Variables and parameters

| Scope | Name | Role and meaning | Type | Lifetime | Writes |
| --- | --- | --- | --- | --- | --- |
| module | json | Imported dependency for json in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 3 |
| module | math | Imported dependency for math in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 4 |
| module | ip_address | Imported dependency for ip address in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 5 |
| module | Any | Imported dependency for Any in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 6 |
| module | urlsplit | Imported dependency for urlsplit in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 7 |
| module | HTTPRedirectHandler | Imported dependency for HTTPRedirectHandler in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 8 |
| module | ProxyHandler | Imported dependency for ProxyHandler in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 8 |
| module | Request | Imported dependency for Request in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 8 |
| module | build_opener | Imported dependency for build opener in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 8 |
| module | policy | Imported dependency for policy in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 10 |
| module | validate_keywords | Imported dependency for validate keywords in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 11 |
| _NoRedirects.redirect_request | self | Owning instance; its attributes retain state for the instance lifetime. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 18 |
| _NoRedirects.redirect_request | req | Parameter for req in _NoRedirects.redirect_request; use the enclosing contract and type below. | Any | Enclosing invocation or class/instance lifetime | 18 |
| _NoRedirects.redirect_request | fp | Parameter for fp in _NoRedirects.redirect_request; use the enclosing contract and type below. | Any | Enclosing invocation or class/instance lifetime | 18 |
| _NoRedirects.redirect_request | code | Source snapshot passed through approval, syntax checks and isolated staging. | int | Enclosing invocation or class/instance lifetime | 18 |
| _NoRedirects.redirect_request | msg | Parameter for msg in _NoRedirects.redirect_request; use the enclosing contract and type below. | str | Enclosing invocation or class/instance lifetime | 18 |
| _NoRedirects.redirect_request | headers | Parameter for headers in _NoRedirects.redirect_request; use the enclosing contract and type below. | Any | Enclosing invocation or class/instance lifetime | 18 |
| _NoRedirects.redirect_request | newurl | Parameter for newurl in _NoRedirects.redirect_request; use the enclosing contract and type below. | str | Enclosing invocation or class/instance lifetime | 18 |
| OllamaClient.__init__ | self | Owning instance; its attributes retain state for the instance lifetime. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 32 |
| OllamaClient.__init__ | endpoint | Parameter for endpoint in OllamaClient.__init__; use the enclosing contract and type below. | str | Enclosing invocation or class/instance lifetime | 33 |
| OllamaClient.__init__ | timeout | Parameter for timeout in OllamaClient.__init__; use the enclosing contract and type below. | float | Enclosing invocation or class/instance lifetime | 34 |
| OllamaClient.__init__ | parsed | Local binding for parsed in OllamaClient.__init__; use the enclosing contract and type below. | Return type of urlsplit; see its callable contract | Enclosing invocation or class/instance lifetime | 37 |
| OllamaClient.__init__ | local | Local binding for local in OllamaClient.__init__; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 39, 41 |
| OllamaClient.__init__ | self.endpoint | Attribute for endpoint in OllamaClient.__init__; use the enclosing contract and type below. | tuple | Enclosing invocation or class/instance lifetime | 54 |
| OllamaClient.__init__ | self.timeout | Attribute for timeout in OllamaClient.__init__; use the enclosing contract and type below. | tuple | Enclosing invocation or class/instance lifetime | 54 |
| OllamaClient.post | self | Owning instance; its attributes retain state for the instance lifetime. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 56 |
| OllamaClient.post | route | Parameter for route in OllamaClient.post; use the enclosing contract and type below. | str | Enclosing invocation or class/instance lifetime | 56 |
| OllamaClient.post | payload | Parameter for payload in OllamaClient.post; use the enclosing contract and type below. | dict | Enclosing invocation or class/instance lifetime | 56 |
| OllamaClient.post | data | Local binding for data in OllamaClient.post; use the enclosing contract and type below. | Return type of encode; see its callable contract | Enclosing invocation or class/instance lifetime | 61 |
| OllamaClient.post | request | Local binding for request in OllamaClient.post; use the enclosing contract and type below. | Return type of Request; see its callable contract | Enclosing invocation or class/instance lifetime | 64 |
| OllamaClient.post | response | Bounded response text to render or validate; it is not executable code. | Return type of open; see its callable contract | Context-manager block; exit invokes its cleanup protocol | 67 |
| OllamaClient.post | raw | Local binding for raw in OllamaClient.post; use the enclosing contract and type below. | Return type of read; see its callable contract | Enclosing invocation or class/instance lifetime | 71 |
| OllamaClient.post | result | Intermediate or returned outcome; consult the callable contract for trust/validation. | Return type of loads; see its callable contract | Enclosing invocation or class/instance lifetime | 74 |
| OllamaKeywords.__init__ | self | Owning instance; its attributes retain state for the instance lifetime. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 85 |
| OllamaKeywords.__init__ | client | Parameter for client in OllamaKeywords.__init__; use the enclosing contract and type below. | OllamaClient | Enclosing invocation or class/instance lifetime | 85 |
| OllamaKeywords.__init__ | model | Parameter for model in OllamaKeywords.__init__; use the enclosing contract and type below. | str | Enclosing invocation or class/instance lifetime | 85 |
| OllamaKeywords.__init__ | self.client | Attribute for client in OllamaKeywords.__init__; use the enclosing contract and type below. | tuple | Enclosing invocation or class/instance lifetime | 87 |
| OllamaKeywords.__init__ | self.model_id | Attribute for model id in OllamaKeywords.__init__; use the enclosing contract and type below. | tuple | Enclosing invocation or class/instance lifetime | 87 |
| OllamaKeywords.generate | self | Owning instance; its attributes retain state for the instance lifetime. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 89 |
| OllamaKeywords.generate | query | Original user request or a trusted test query; avoid payload logging by default. | str | Enclosing invocation or class/instance lifetime | 89 |
| OllamaKeywords.generate | result | Intermediate or returned outcome; consult the callable contract for trust/validation. | Return type of post; see its callable contract | Enclosing invocation or class/instance lifetime | 91 |
| OllamaKeywords.generate | response | Bounded response text to render or validate; it is not executable code. | Return type of get; see its callable contract | Enclosing invocation or class/instance lifetime | 117 |
| OllamaEmbeddings.__init__ | self | Owning instance; its attributes retain state for the instance lifetime. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 126 |
| OllamaEmbeddings.__init__ | client | Parameter for client in OllamaEmbeddings.__init__; use the enclosing contract and type below. | OllamaClient | Enclosing invocation or class/instance lifetime | 126 |
| OllamaEmbeddings.__init__ | model | Parameter for model in OllamaEmbeddings.__init__; use the enclosing contract and type below. | str | Enclosing invocation or class/instance lifetime | 126 |
| OllamaEmbeddings.__init__ | self.client | Attribute for client in OllamaEmbeddings.__init__; use the enclosing contract and type below. | tuple | Enclosing invocation or class/instance lifetime | 128 |
| OllamaEmbeddings.__init__ | self.model_id | Attribute for model id in OllamaEmbeddings.__init__; use the enclosing contract and type below. | tuple | Enclosing invocation or class/instance lifetime | 128 |
| OllamaEmbeddings.embed | self | Owning instance; its attributes retain state for the instance lifetime. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 130 |
| OllamaEmbeddings.embed | texts | Parameter for texts in OllamaEmbeddings.embed; use the enclosing contract and type below. | list[str] | Enclosing invocation or class/instance lifetime | 130 |
| OllamaEmbeddings.embed | result | Intermediate or returned outcome; consult the callable contract for trust/validation. | Return type of post; see its callable contract | Enclosing invocation or class/instance lifetime | 132 |
