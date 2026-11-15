# Reference for src/agentix/lab/application_artifacts.py

Host-only complete package validation; never import application code.

Digests detect changes, not human approval. The reviewed digest comes from the
operator, outside the child-controlled package. The initial surface is fixed.

Source fingerprint: d17993370387479e628d4521d3a6441550e9a1976e05d8ddb223c0488d2fda1d

This reference is generated from maintained source without imports or execution. Assigned values are intentionally omitted. Runtime-dependent types are explicit; the enclosing docstring defines the behavioral contract. See [architecture](../ARCHITECTURE_QUALITY.md) for manually reviewed responsibility and dependency decisions.

## Classes and callables

### ApprovedApplication

Immutable reviewed complete source/manifest snapshot.

Kind: class. Declared return: Not declared / class. Source line: 19.

### validate_result

Reject coercion, negative counts and unknown fields in structured child results.

Kind: callable. Declared return: dict. Source line: 26.

### _capture

Validate the schema-3 package closure, lock, permissions and manifest.

Kind: callable. Declared return: tuple[tuple[str, bytes], ...]. Source line: 33.

### application_digest

Compute validated identity without granting authorization.

Kind: callable. Declared return: str. Source line: 57.

### _identity

Bind executable member names and bytes with unambiguous canonical JSON.

Scoped widget stylesheets are deliberately excluded: their closed grammar in
``agentix.widgets.styles`` is the gate, so a colour, radius or font edit must
not revoke an approval that covers the application's code. The declared style
hashes inside ``application.json`` are dropped for the same reason, while every
executable member hash in that manifest stays bound. The member hash on disk
still ties those bytes to the package, so capture keeps rejecting a stylesheet
edited outside the maintained writer.

Kind: callable. Declared return: str. Source line: 62.

### _manifest_identity_bytes

Drop declared style hashes so a style edit cannot move the identity.

Kind: callable. Declared return: bytes. Source line: 85.

### approve_application

Capture exact reviewed bytes and reject changes before native startup.

``allow_runtime_drift`` is reserved for an explicit owner re-approval of an
installed package whose only drift is a maintained runtime member; the
captured snapshot then carries the current runtime bytes and its own digest.

Kind: callable. Declared return: ApprovedApplication. Source line: 99.

## Variables and parameters

| Scope | Name | Role and meaning | Type | Lifetime | Writes |
| --- | --- | --- | --- | --- | --- |
| module | hashlib | Imported dependency for hashlib in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 7 |
| module | json | Imported dependency for json in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 8 |
| module | stat | Imported dependency for stat in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 9 |
| module | dataclass | Imported dependency for dataclass in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 10 |
| module | Path | Imported dependency for Path in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 11 |
| module | decode_frame | Imported dependency for decode frame in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 13 |
| module | LOCK_PATH | Module binding for LOCK PATH in module; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Module/process lifetime | 15 |
| ApprovedApplication | files | Typed binding for files in ApprovedApplication; use the enclosing contract and type below. | tuple[tuple[str, bytes], ...] | Enclosing invocation or class/instance lifetime | 22 |
| ApprovedApplication | digest | Content fingerprint for change detection; not a substitute for human approval. | str | Enclosing invocation or class/instance lifetime | 23 |
| validate_result | value | Value at the current validation/rendering boundary; apply the enclosing contract. | object | Enclosing invocation or class/instance lifetime | 26 |
| validate_result | manifest | Versioned inventory or launch record; not an execution-authorization capability. | dict | Enclosing invocation or class/instance lifetime | 26 |
| validate_result | validate_results | Imported dependency for validate results in validate_result; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 28 |
| _capture | folder | Parameter for folder in _capture; use the enclosing contract and type below. | Path | Enclosing invocation or class/instance lifetime | 33 |
| _capture.comprehension_37 | part | Comprehension item for part in _capture.comprehension_37; use the enclosing contract and type below. | Element of the declared iterable | This comprehension only; does not leak into its enclosing scope | 37 |
| _capture | manifest_path | Local binding for manifest path in _capture; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 43 |
| _capture | capture | Imported dependency for capture in _capture; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 52 |
| application_digest | folder | Parameter for folder in application_digest; use the enclosing contract and type below. | Path | Enclosing invocation or class/instance lifetime | 57 |
| _identity | files | Parameter for files in _identity; use the enclosing contract and type below. | tuple[tuple[str, bytes], ...] | Enclosing invocation or class/instance lifetime | 62 |
| _identity | STYLE_SUFFIX | Imported dependency for STYLE SUFFIX in _identity; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 73 |
| _identity | bound | Local binding for bound in _identity; use the enclosing contract and type below. | dict | Enclosing invocation or class/instance lifetime | 75 |
| _identity | name | Current identifier selected by parsing, lookup or dependency registration. | Element of the declared iterable | Enclosing invocation or class/instance lifetime | 76 |
| _identity | body | Loop item for body in _identity; use the enclosing contract and type below. | Element of the declared iterable | Enclosing invocation or class/instance lifetime | 76, 80 |
| _manifest_identity_bytes | body | Parameter for body in _manifest_identity_bytes; use the enclosing contract and type below. | bytes | Enclosing invocation or class/instance lifetime | 85 |
| _manifest_identity_bytes | suffix | Parameter for suffix in _manifest_identity_bytes; use the enclosing contract and type below. | str | Enclosing invocation or class/instance lifetime | 85 |
| _manifest_identity_bytes | manifest | Versioned inventory or launch record; not an execution-authorization capability. | Return type of loads; see its callable contract | Enclosing invocation or class/instance lifetime | 88 |
| _manifest_identity_bytes.comprehension_93 | name | Current identifier selected by parsing, lookup or dependency registration. | Element of the declared iterable | This comprehension only; does not leak into its enclosing scope | 94 |
| _manifest_identity_bytes.comprehension_93 | value | Value at the current validation/rendering boundary; apply the enclosing contract. | Element of the declared iterable | This comprehension only; does not leak into its enclosing scope | 94 |
| approve_application | folder | Parameter for folder in approve_application; use the enclosing contract and type below. | Path | Enclosing invocation or class/instance lifetime | 100 |
| approve_application | reviewed_digest | Parameter for reviewed digest in approve_application; use the enclosing contract and type below. | str | Enclosing invocation or class/instance lifetime | 100 |
| approve_application | allow_runtime_drift | Parameter for allow runtime drift in approve_application; use the enclosing contract and type below. | bool | Enclosing invocation or class/instance lifetime | 100 |
| approve_application | capture | Imported dependency for capture in approve_application; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 108 |
| approve_application | capture_with_current_runtime | Imported dependency for capture with current runtime in approve_application; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 108 |
| approve_application | files | Local binding for files in approve_application; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 110 |
| approve_application | digest | Content fingerprint for change detection; not a substitute for human approval. | Return type of _identity; see its callable contract | Enclosing invocation or class/instance lifetime | 111 |
