# Reference for src/agentix/diagnostics.py

Payload-free correlated events and context-local activity routing.

No per-worker stdout replacement is performed. The optional host router only
copies output associated with the current context to its own session capture.
Unrelated/background threads without context never enter another session buffer.

Source fingerprint: cf68a9c449b20f29f38328ed1f1a5031487057fffa104e01dbfd7a3f0e4ef41e

This reference is generated from maintained source without imports or execution. Assigned values are intentionally omitted. Runtime-dependent types are explicit; the enclosing docstring defines the behavioral contract. See [architecture](../ARCHITECTURE_QUALITY.md) for manually reviewed responsibility and dependency decisions.

## Classes and callables

### operation_scope

Bind diagnostic identity/activity and restore the caller's context afterward.

Kind: callable. Declared return: Iterator[str]. Source line: 22.

### log_event

Log fixed event/identity/type fields, never exception text or user payloads.

Kind: callable. Declared return: None. Source line: 40.

### ActivityRouter

One host stdout proxy that routes only explicitly scoped activity.

Kind: class. Declared return: Not declared / class. Source line: 65.

### ActivityRouter.__init__

Retain the actual host stream; never install the proxy implicitly.

Kind: callable. Declared return: None. Source line: 68.

### ActivityRouter.write

Mirror output through its own capture, or directly to the host.

Kind: callable. Declared return: int. Source line: 72.

### ActivityRouter.flush

Flush the actual host stream.

Kind: callable. Declared return: None. Source line: 84.

### ActivityRouter.__getattr__

Preserve encoding, terminal and file-descriptor access.

Kind: callable. Declared return: Any. Source line: 88.

### activity_output

Route verbose stdout for the lifetime of a server, restoring it on exit.

Install once at startup, never per worker. Context-local captures associate
both SDK messages and technical events with the owning GUI session. Nested
startup contexts reuse the existing router instead of duplicating messages.

Kind: callable. Declared return: Iterator[None]. Source line: 94.

## Variables and parameters

| Scope | Name | Role and meaning | Type | Lifetime | Writes |
| --- | --- | --- | --- | --- | --- |
| module | logging | Imported dependency for logging in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 8 |
| module | sys | Imported dependency for sys in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 9 |
| module | Iterator | Imported dependency for Iterator in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 10 |
| module | contextmanager | Imported dependency for contextmanager in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 11 |
| module | ContextVar | Imported dependency for ContextVar in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 12 |
| module | Any | Imported dependency for Any in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 13 |
| module | TextIO | Imported dependency for TextIO in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 13 |
| module | uuid4 | Imported dependency for uuid4 in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 14 |
| module | _session | Typed binding for session in module; use the enclosing contract and type below. | ContextVar[str] | Module/process lifetime | 16 |
| module | _operation | Typed binding for operation in module; use the enclosing contract and type below. | ContextVar[str] | Module/process lifetime | 17 |
| module | _capture | Typed binding for capture in module; use the enclosing contract and type below. | ContextVar[Any] | Module/process lifetime | 18 |
| operation_scope | session_id | Browser or terminal session identifier for state and diagnostic ownership. | str &#124; None | Enclosing invocation or class/instance lifetime | 23 |
| operation_scope | operation_id | Identity of one user operation; new operations invalidate earlier evidence. | str &#124; None | Enclosing invocation or class/instance lifetime | 23 |
| operation_scope | capture | Parameter for capture in operation_scope; use the enclosing contract and type below. | Any | Enclosing invocation or class/instance lifetime | 23 |
| operation_scope | operation | Local binding for operation in operation_scope; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 26 |
| operation_scope | tokens | Local binding for tokens in operation_scope; use the enclosing contract and type below. | tuple | Enclosing invocation or class/instance lifetime | 27 |
| log_event | logger | Module logger emitting bounded operation diagnostics rather than artifact bodies. | logging.Logger | Enclosing invocation or class/instance lifetime | 41 |
| log_event | event | Parameter for event in log_event; use the enclosing contract and type below. | str | Enclosing invocation or class/instance lifetime | 42 |
| log_event | request_id | Displayed approval identity checked against the owner and expiry; not a secret. | str | Enclosing invocation or class/instance lifetime | 44 |
| log_event | error | Parameter for error in log_event; use the enclosing contract and type below. | BaseException &#124; None | Enclosing invocation or class/instance lifetime | 45 |
| log_event | level | Parameter for level in log_event; use the enclosing contract and type below. | int | Enclosing invocation or class/instance lifetime | 46 |
| log_event | line | Current source or text line scoped to parsing; no implicit execution occurs. | int &#124; None | Enclosing invocation or class/instance lifetime | 47 |
| log_event | capture | Local binding for capture in log_event; use the enclosing contract and type below. | Return type of get; see its callable contract | Enclosing invocation or class/instance lifetime | 60 |
| ActivityRouter.__init__ | self | Owning instance; its attributes retain state for the instance lifetime. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 68 |
| ActivityRouter.__init__ | original_stdout | Parameter for original stdout in ActivityRouter.__init__; use the enclosing contract and type below. | TextIO | Enclosing invocation or class/instance lifetime | 68 |
| ActivityRouter.__init__ | self.original_stdout | Attribute for original stdout in ActivityRouter.__init__; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 70 |
| ActivityRouter.write | self | Owning instance; its attributes retain state for the instance lifetime. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 72 |
| ActivityRouter.write | text | Parameter for text in ActivityRouter.write; use the enclosing contract and type below. | str | Enclosing invocation or class/instance lifetime | 72, 76 |
| ActivityRouter.write | redact | Imported dependency for redact in ActivityRouter.write; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 74 |
| ActivityRouter.write | capture | Local binding for capture in ActivityRouter.write; use the enclosing contract and type below. | Return type of get; see its callable contract | Enclosing invocation or class/instance lifetime | 77 |
| ActivityRouter.flush | self | Owning instance; its attributes retain state for the instance lifetime. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 84 |
| ActivityRouter.__getattr__ | self | Owning instance; its attributes retain state for the instance lifetime. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 88 |
| ActivityRouter.__getattr__ | name | Current identifier selected by parsing, lookup or dependency registration. | str | Enclosing invocation or class/instance lifetime | 88 |
| activity_output | original | Local binding for original in activity_output; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 101 |
| activity_output | sys.stdout | Attribute for sys.stdout in activity_output; use the enclosing contract and type below. | Return type of ActivityRouter; see its callable contract | Enclosing invocation or class/instance lifetime | 105, 109 |
