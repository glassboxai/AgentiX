# Reference for src/agentix/lab/widget_artifacts.py

Review-only widget packages: bounded syntax policy plus exact content binding.

AST checks reduce the supported UI surface; they are not OS isolation. Generated source
is parsed/compiled for syntax only on the host and executed solely in AppContainer.

Source fingerprint: 82865f7cd20d86ac278f5a65d415332cf69df1d3c3ab1fc112be46b037bcf45b

This reference is generated from maintained source without imports or execution. Assigned values are intentionally omitted. Runtime-dependent types are explicit; the enclosing docstring defines the behavioral contract. See [architecture](../ARCHITECTURE_QUALITY.md) for manually reviewed responsibility and dependency decisions.

## Classes and callables

### ApprovedWidget

Engineer-reviewed immutable source snapshots; never load approval from child files.

Kind: class. Declared return: Not declared / class. Source line: 19.

### validate_widget

Accept a narrow widget grammar, rejecting arbitrary imports/callback capabilities.

Kind: callable. Declared return: None. Source line: 28.

### _digest

Bind exact source bytes and fixed contract without ambiguous concatenation.

Kind: callable. Declared return: str. Source line: 175.

### package_digest

Compute the review identity; this does not grant approval or execute source.

Kind: callable. Declared return: str. Source line: 191.

### approve_package

Capture reviewed bytes only if the caller's explicit digest still matches.

Kind: callable. Declared return: ApprovedWidget. Source line: 203.

## Variables and parameters

| Scope | Name | Role and meaning | Type | Lifetime | Writes |
| --- | --- | --- | --- | --- | --- |
| module | ast | Imported dependency for ast in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 7 |
| module | hashlib | Imported dependency for hashlib in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 8 |
| module | json | Imported dependency for json in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 9 |
| module | dataclass | Imported dependency for dataclass in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 10 |
| module | Path | Imported dependency for Path in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 11 |
| module | CONTRACT | Imported dependency for CONTRACT in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 13 |
| module | TESTS_FILENAME | Imported dependency for TESTS FILENAME in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 13 |
| module | TOOL_FILENAME | Imported dependency for TOOL FILENAME in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 13 |
| module | WIDGET_FILENAME | Imported dependency for WIDGET FILENAME in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 13 |
| module | __all__ | Module binding for all in module; use the enclosing contract and type below. | list | Module/process lifetime | 15 |
| ApprovedWidget | widget | Typed binding for widget in ApprovedWidget; use the enclosing contract and type below. | bytes | Enclosing invocation or class/instance lifetime | 22 |
| ApprovedWidget | tool | Typed binding for tool in ApprovedWidget; use the enclosing contract and type below. | bytes | Enclosing invocation or class/instance lifetime | 23 |
| ApprovedWidget | digest | Content fingerprint for change detection; not a substitute for human approval. | str | Enclosing invocation or class/instance lifetime | 24 |
| ApprovedWidget | tests | Optional unittest source snapshot; child-authored success remains provisional. | bytes | Enclosing invocation or class/instance lifetime | 25 |
| validate_widget | source | Explicit source document or source-code text; never imported for reference generation. | bytes | Enclosing invocation or class/instance lifetime | 28 |
| validate_widget | tree | Local binding for tree in validate_widget; use the enclosing contract and type below. | Return type of parse; see its callable contract | Enclosing invocation or class/instance lifetime | 33 |
| validate_widget | error | Caught exception for error in validate_widget; use the enclosing contract and type below. | (SyntaxError, UnicodeError, RecursionError) | Current exception handler; Python clears this binding afterward | 34 |
| validate_widget | imports | Local binding for imports in validate_widget; use the enclosing contract and type below. | list | Enclosing invocation or class/instance lifetime | 36 |
| validate_widget.comprehension_36 | node | Comprehension item for node in validate_widget.comprehension_36; use the enclosing contract and type below. | Element of the declared iterable | This comprehension only; does not leak into its enclosing scope | 36 |
| validate_widget | functions | Local binding for functions in validate_widget; use the enclosing contract and type below. | list | Enclosing invocation or class/instance lifetime | 37 |
| validate_widget.comprehension_37 | node | Comprehension item for node in validate_widget.comprehension_37; use the enclosing contract and type below. | Element of the declared iterable | This comprehension only; does not leak into its enclosing scope | 37 |
| validate_widget | function | Local binding for function in validate_widget; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 46 |
| validate_widget.comprehension_49 | arg | Comprehension item for arg in validate_widget.comprehension_49; use the enclosing contract and type below. | Element of the declared iterable | This comprehension only; does not leak into its enclosing scope | 49 |
| validate_widget | allowed | Local binding for allowed in validate_widget; use the enclosing contract and type below. | tuple | Enclosing invocation or class/instance lifetime | 57 |
| validate_widget | components | Local binding for components in validate_widget; use the enclosing contract and type below. | dict | Enclosing invocation or class/instance lifetime | 78 |
| validate_widget | roles | Local binding for roles in validate_widget; use the enclosing contract and type below. | Return type of set; see its callable contract | Enclosing invocation or class/instance lifetime | 79 |
| validate_widget | clicks | Local binding for clicks in validate_widget; use the enclosing contract and type below. | int | Enclosing invocation or class/instance lifetime | 80, 144 |
| validate_widget | node | Loop item for node in validate_widget; use the enclosing contract and type below. | Element of the declared iterable | Enclosing invocation or class/instance lifetime | 81, 153, 165 |
| validate_widget | owner | Local binding for owner in validate_widget; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 89, 116 |
| validate_widget | valid | Local binding for valid in validate_widget; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 90 |
| validate_widget | name | Current identifier selected by parsing, lookup or dependency registration. | tuple | Enclosing invocation or class/instance lifetime | 116 |
| validate_widget | keywords | Local binding for keywords in validate_widget; use the enclosing contract and type below. | dict | Enclosing invocation or class/instance lifetime | 127 |
| validate_widget.comprehension_127 | item | Comprehension item for item in validate_widget.comprehension_127; use the enclosing contract and type below. | Element of the declared iterable | This comprehension only; does not leak into its enclosing scope | 127 |
| validate_widget.comprehension_147 | item | Comprehension item for item in validate_widget.comprehension_147; use the enclosing contract and type below. | Element of the declared iterable | This comprehension only; does not leak into its enclosing scope | 150 |
| _digest | widget | Parameter for widget in _digest; use the enclosing contract and type below. | bytes | Enclosing invocation or class/instance lifetime | 175 |
| _digest | tool | Parameter for tool in _digest; use the enclosing contract and type below. | bytes | Enclosing invocation or class/instance lifetime | 175 |
| _digest | tests | Optional unittest source snapshot; child-authored success remains provisional. | bytes | Enclosing invocation or class/instance lifetime | 175 |
| _digest | definition | Parameter for definition in _digest; use the enclosing contract and type below. | bytes | Enclosing invocation or class/instance lifetime | 175 |
| _digest | payload | Local binding for payload in _digest; use the enclosing contract and type below. | Return type of encode; see its callable contract | Enclosing invocation or class/instance lifetime | 177 |
| package_digest | folder | Parameter for folder in package_digest; use the enclosing contract and type below. | Path | Enclosing invocation or class/instance lifetime | 191 |
| approve_package | folder | Parameter for folder in approve_package; use the enclosing contract and type below. | Path | Enclosing invocation or class/instance lifetime | 203 |
| approve_package | reviewed_digest | Parameter for reviewed digest in approve_package; use the enclosing contract and type below. | str | Enclosing invocation or class/instance lifetime | 203 |
| approve_package | widget | Local binding for widget in approve_package; use the enclosing contract and type below. | tuple | Enclosing invocation or class/instance lifetime | 205 |
| approve_package | tool | Local binding for tool in approve_package; use the enclosing contract and type below. | tuple | Enclosing invocation or class/instance lifetime | 205 |
| approve_package | tests | Optional unittest source snapshot; child-authored success remains provisional. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 206 |
| approve_package | definition | Local binding for definition in approve_package; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 207 |
| approve_package | digest | Content fingerprint for change detection; not a substitute for human approval. | Return type of _digest; see its callable contract | Enclosing invocation or class/instance lifetime | 220 |
