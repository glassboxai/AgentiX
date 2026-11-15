# Reference for src/agentix/application/general_package.py

Validate version-3 catalog-driven package closures without importing their code.

Source fingerprint: 94664ba1325485a4fe622fbeadbc38713399c3376b967631a37ca6ec60cced0c

This reference is generated from maintained source without imports or execution. Assigned values are intentionally omitted. Runtime-dependent types are explicit; the enclosing docstring defines the behavioral contract. See [architecture](../ARCHITECTURE_QUALITY.md) for manually reviewed responsibility and dependency decisions.

## Classes and callables

### RuntimeSourceChanged

A maintained runtime member differs from the exact installed package copy.

Callers distinguish this drift from tampered application bytes; it stays a
``ValueError`` so existing bounded rejection paths keep working unchanged.

Kind: class. Declared return: Not declared / class. Source line: 12.

### runtime_template

Return one maintained version-3 runtime member from the connection-code set.

The version-3 package has a single maintained runtime generation, so every
allowlisted member resolves inside ``templates/code`` through the
connection-code contract; no legacy template path remains resolvable.

Kind: callable. Declared return: Path. Source line: 20.

### validate_manifest

Require the bounded exact unprivileged manifest and its typed catalog closure.

Kind: callable. Declared return: set[str]. Source line: 32.

### capture

Capture bounded exact files; reject aliases, changed hashes and tool schemas.

Kind: callable. Declared return: tuple[tuple[str, bytes], ...]. Source line: 41.

### capture_with_current_runtime

Capture an installed package, replacing only drifted maintained runtime members.

The caller must already hold an explicit human decision for this exact
application and must re-run the independent gates on the returned bytes.
Application-owned members keep their exact installed bytes and are still
checked against the manifest, so this never authorizes changed application
source. The returned snapshot therefore has a different identity than the
installed digest, and no record may be resealed from it.

Kind: callable. Declared return: tuple[tuple[str, bytes], ...]. Source line: 46.

### _capture

Validate one package closure; runtime drift is either rejected or refreshed.

Kind: callable. Declared return: tuple[tuple[str, bytes], ...]. Source line: 59.

### validate_payload

Validate external values against the exact schema-3 inputs without coercion.

Kind: callable. Declared return: dict. Source line: 115.

### validate_results

Reject missing, extra, oversized or incorrectly typed structured results.

Kind: callable. Declared return: dict. Source line: 122.

## Variables and parameters

| Scope | Name | Role and meaning | Type | Lifetime | Writes |
| --- | --- | --- | --- | --- | --- |
| module | hashlib | Imported dependency for hashlib in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 3 |
| module | json | Imported dependency for json in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 4 |
| module | Path | Imported dependency for Path in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 5 |
| module | extract_tool_schema | Imported dependency for extract tool schema in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 7 |
| module | reject_alias | Imported dependency for reject alias in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 8 |
| module | validate_widget_css | Imported dependency for validate widget css in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 9 |
| runtime_template | name | Current identifier selected by parsing, lookup or dependency registration. | str | Enclosing invocation or class/instance lifetime | 20 |
| runtime_template | code_template | Imported dependency for code template in runtime_template; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 27 |
| validate_manifest | manifest | Versioned inventory or launch record; not an execution-authorization capability. | dict | Enclosing invocation or class/instance lifetime | 32 |
| validate_manifest | validate_code_manifest | Imported dependency for validate code manifest in validate_manifest; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 36 |
| capture | folder | Parameter for folder in capture; use the enclosing contract and type below. | Path | Enclosing invocation or class/instance lifetime | 41 |
| capture_with_current_runtime | folder | Parameter for folder in capture_with_current_runtime; use the enclosing contract and type below. | Path | Enclosing invocation or class/instance lifetime | 46 |
| _capture | folder | Parameter for folder in _capture; use the enclosing contract and type below. | Path | Enclosing invocation or class/instance lifetime | 59 |
| _capture | allow_runtime_drift | Parameter for allow runtime drift in _capture; use the enclosing contract and type below. | bool | Enclosing invocation or class/instance lifetime | 59 |
| _capture | CODE_SHARED | Imported dependency for CODE SHARED in _capture; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 61 |
| _capture | manifest_path | Local binding for manifest path in _capture; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 64 |
| _capture | manifest | Versioned inventory or launch record; not an execution-authorization capability. | Return type of loads; see its callable contract | Enclosing invocation or class/instance lifetime | 68 |
| _capture | expected | Reviewed expected observation kept outside untrusted child execution. | Return type of validate_manifest; see its callable contract | Enclosing invocation or class/instance lifetime | 69 |
| _capture.comprehension_70 | member | Comprehension item for member in _capture.comprehension_70; use the enclosing contract and type below. | Element of the declared iterable | This comprehension only; does not leak into its enclosing scope | 70 |
| _capture | layout | Local binding for layout in _capture; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 74 |
| _capture | data | Local binding for data in _capture; use the enclosing contract and type below. | dict | Enclosing invocation or class/instance lifetime | 79 |
| _capture | replaced | Typed binding for replaced in _capture; use the enclosing contract and type below. | list[str] | Enclosing invocation or class/instance lifetime | 80 |
| _capture | name | Current identifier selected by parsing, lookup or dependency registration. | Element of the declared iterable | Enclosing invocation or class/instance lifetime | 81, 105, 108 |
| _capture | member | Local binding for member in _capture; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 82 |
| _capture | body | Local binding for body in _capture; use the enclosing contract and type below. | Return type of read_bytes; see its callable contract | Enclosing invocation or class/instance lifetime | 86, 100 |
| _capture | validate_connection_source | Imported dependency for validate connection source in _capture; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 92 |
| _capture | current | Local binding for current in _capture; use the enclosing contract and type below. | Return type of read_bytes; see its callable contract | Enclosing invocation or class/instance lifetime | 96 |
| _capture | schema | Loop item for schema in _capture; use the enclosing contract and type below. | Element of the declared iterable | Enclosing invocation or class/instance lifetime | 108 |
| validate_payload | payload | Parameter for payload in validate_payload; use the enclosing contract and type below. | dict | Enclosing invocation or class/instance lifetime | 115 |
| validate_payload | manifest | Versioned inventory or launch record; not an execution-authorization capability. | dict | Enclosing invocation or class/instance lifetime | 115 |
| validate_payload | validate_code_payload | Imported dependency for validate code payload in validate_payload; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 117 |
| validate_results | value | Value at the current validation/rendering boundary; apply the enclosing contract. | dict | Enclosing invocation or class/instance lifetime | 122 |
| validate_results | manifest | Versioned inventory or launch record; not an execution-authorization capability. | dict | Enclosing invocation or class/instance lifetime | 122 |
| validate_results | validate_code_results | Imported dependency for validate code results in validate_results; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 124 |
