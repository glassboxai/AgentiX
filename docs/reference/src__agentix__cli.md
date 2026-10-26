# Reference for src/agentix/cli.py

Interactive command-line entrypoint with lazy runtime construction.

Source fingerprint: 1f7fcaa2411122e64951f93afdf77601c619c5e9b679becffdc7cfeb59ba1174

This reference is generated from maintained source without imports or execution. Assigned values are intentionally omitted. Runtime-dependent types are explicit; the enclosing docstring defines the behavioral contract. See [architecture](../ARCHITECTURE_QUALITY.md) for manually reviewed responsibility and dependency decisions.

## Classes and callables

### display_review

Escape terminal controls in untrusted review text without changing stored bytes.

Printable characters, line breaks and tabs remain readable. Escape sequences,
carriage returns and bidi controls cannot erase or reorder the review prompt.

Kind: callable. Declared return: None. Source line: 16.

### review_request

Display one immutable snapshot and resolve only its original identifiers.

Input is read exclusively on the main thread. Editing never authorizes a
request: a separate explicit approval is required after `.end`.

Kind: callable. Declared return: None. Source line: 29.

### run_with_review

Run the shared workflow while the terminal services owner-bound reviews.

Worker errors propagate to the original CLI recovery loop. On interruption
the caller closes the coordinator; daemonization does not cancel model I/O.

Kind: callable. Declared return: str. Source line: 70.

### run_with_review.worker

Publish a result before signalling completion, with correlated logs.

Kind: callable. Declared return: None. Source line: 82.

### run_cli

Run terminal queries and manual reviews; EOF/Ctrl+C deny and close work.

Injected legacy workflows without a coordinator retain synchronous behavior.
Production uses the same runtime and acceptance services as the browser.

Kind: callable. Declared return: None. Source line: 107.

## Variables and parameters

| Scope | Name | Role and meaning | Type | Lifetime | Writes |
| --- | --- | --- | --- | --- | --- |
| module | json | Imported dependency for json in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 3 |
| module | logging | Imported dependency for logging in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 4 |
| module | sys | Imported dependency for sys in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 5 |
| module | threading | Imported dependency for threading in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 6 |
| module | Callable | Imported dependency for Callable in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 7 |
| module | Any | Imported dependency for Any in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 8 |
| module | uuid4 | Imported dependency for uuid4 in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 9 |
| module | log_event | Imported dependency for log event in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 11 |
| module | operation_scope | Imported dependency for operation scope in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 11 |
| module | logger | Module logger emitting bounded operation diagnostics rather than artifact bodies. | Return type of getLogger; see its callable contract | Module/process lifetime | 13 |
| display_review | text | Parameter for text in display_review; use the enclosing contract and type below. | str | Enclosing invocation or class/instance lifetime | 16 |
| display_review.comprehension_23 | char | Comprehension item for char in display_review.comprehension_23; use the enclosing contract and type below. | Element of the declared iterable | This comprehension only; does not leak into its enclosing scope | 24 |
| review_request | security | Owner-scoped approval and path boundary injected into this service. | Any | Enclosing invocation or class/instance lifetime | 29 |
| review_request | pending | Defensive pending-approval snapshot; never a capability to approve another owner. | dict[str, Any] | Enclosing invocation or class/instance lifetime | 29 |
| review_request | context | Local binding for context in review_request; use the enclosing contract and type below. | Return type of get; see its callable contract | Enclosing invocation or class/instance lifetime | 36 |
| review_request | name | Current identifier selected by parsing, lookup or dependency registration. | Element of the declared iterable | Enclosing invocation or class/instance lifetime | 37 |
| review_request | value | Value at the current validation/rendering boundary; apply the enclosing contract. | Element of the declared iterable | Enclosing invocation or class/instance lifetime | 37 |
| review_request | content | Artifact or review text whose encoding, size and approval state must be checked. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 39, 48 |
| review_request | choice | Local binding for choice in review_request; use the enclosing contract and type below. | Return type of lower; see its callable contract | Enclosing invocation or class/instance lifetime | 42 |
| review_request | lines | Local binding for lines in review_request; use the enclosing contract and type below. | list | Enclosing invocation or class/instance lifetime | 45 |
| review_request | line | Current source or text line scoped to parsing; no implicit execution occurs. | Return type of input; see its callable contract | Enclosing invocation or class/instance lifetime | 46 |
| review_request | accepted | Local binding for accepted in review_request; use the enclosing contract and type below. | Return type of resolve_pending_request; see its callable contract | Enclosing invocation or class/instance lifetime | 54 |
| run_with_review | run_system | Parameter for run system in run_with_review; use the enclosing contract and type below. | Callable[[str], str] | Enclosing invocation or class/instance lifetime | 70 |
| run_with_review | query | Original user request or a trusted test query; avoid payload logging by default. | str | Enclosing invocation or class/instance lifetime | 70 |
| run_with_review | security | Owner-scoped approval and path boundary injected into this service. | Any | Enclosing invocation or class/instance lifetime | 70 |
| run_with_review | completed | Local binding for completed in run_with_review; use the enclosing contract and type below. | Return type of Event; see its callable contract | Enclosing invocation or class/instance lifetime | 76 |
| run_with_review | result | Intermediate or returned outcome; consult the callable contract for trust/validation. | list[Any] | Enclosing invocation or class/instance lifetime | 77 |
| run_with_review | errors | Typed binding for errors in run_with_review; use the enclosing contract and type below. | list[BaseException] | Enclosing invocation or class/instance lifetime | 78 |
| run_with_review | operation | Local binding for operation in run_with_review; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 79 |
| run_with_review | security.operation_id | Attribute for security.operation id in run_with_review; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 80 |
| run_with_review.worker | exc | Caught exception for exc in run_with_review.worker; use the enclosing contract and type below. | BaseException | Current exception handler; Python clears this binding afterward | 88 |
| run_with_review | displayed | Local binding for displayed in run_with_review; use the enclosing contract and type below. | NoneType | Enclosing invocation or class/instance lifetime | 95, 99 |
| run_with_review | pending | Defensive pending-approval snapshot; never a capability to approve another owner. | Return type of get_pending_request; see its callable contract | Enclosing invocation or class/instance lifetime | 97 |
| run_cli | run_system | Parameter for run system in run_cli; use the enclosing contract and type below. | Callable[[str], str] &#124; None | Enclosing invocation or class/instance lifetime | 108, 119 |
| run_cli | security | Owner-scoped approval and path boundary injected into this service. | Any | Enclosing invocation or class/instance lifetime | 108, 120 |
| run_cli | validation | Parameter for validation in run_cli; use the enclosing contract and type below. | Any | Enclosing invocation or class/instance lifetime | 108, 121 |
| run_cli | get_default_runtime | Imported dependency for get default runtime in run_cli; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 116 |
| run_cli | runtime | Explicitly composed application services for one owner or compatibility facade. | Return type of get_default_runtime; see its callable contract | Enclosing invocation or class/instance lifetime | 118 |
| run_cli | user_input | Local binding for user input in run_cli; use the enclosing contract and type below. | Return type of strip; see its callable contract | Enclosing invocation or class/instance lifetime | 128 |
| run_cli | response | Bounded response text to render or validate; it is not executable code. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 136 |
| run_cli | e | Caught exception for e in run_cli; use the enclosing contract and type below. | Exception | Current exception handler; Python clears this binding afterward | 153 |
