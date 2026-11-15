# Reference for src/agentix/ui/result_components.py

Declarative typed read-only Gradio outputs, independent of model code or HTML.

Source fingerprint: 9c59a7a49199c2dbdd48cf26483402ca6a26dab7cd2f5b3b5ea30870dfce18bc

This reference is generated from maintained source without imports or execution. Assigned values are intentionally omitted. Runtime-dependent types are explicit; the enclosing docstring defines the behavioral contract. See [architecture](../ARCHITECTURE_QUALITY.md) for manually reviewed responsibility and dependency decisions.

## Classes and callables

### ResultField

A known output key, readable label and presentation type.

Kind: class. Declared return: Not declared / class. Source line: 17.

### ResultField.__post_init__

Reject arbitrary selectors, unbounded labels and unsupported presentation types.

Kind: callable. Declared return: None. Source line: 24.

### build_results

Build explicit read-only controls, never a generic JSON output block.

Kind: callable. Declared return: list[Any]. Source line: 34.

### _table_cell

Bound table text/numbers and reject objects or nonfinite float values.

Kind: callable. Declared return: bool. Source line: 52.

### result_values

Validate data against presentation contracts; None clears stale results.

Kind: callable. Declared return: list[Any]. Source line: 61.

## Variables and parameters

| Scope | Name | Role and meaning | Type | Lifetime | Writes |
| --- | --- | --- | --- | --- | --- |
| module | math | Imported dependency for math in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 3 |
| module | re | Imported dependency for re in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 4 |
| module | dataclass | Imported dependency for dataclass in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 5 |
| module | Any | Imported dependency for Any in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 6 |
| module | Literal | Imported dependency for Literal in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 6 |
| module | MAX_SAFE_INTEGER | Module binding for MAX SAFE INTEGER in module; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Module/process lifetime | 8 |
| module | MAX_TEXT_LENGTH | Module binding for MAX TEXT LENGTH in module; use the enclosing contract and type below. | int | Module/process lifetime | 9 |
| module | MAX_TABLE_ROWS | Module binding for MAX TABLE ROWS in module; use the enclosing contract and type below. | int | Module/process lifetime | 10 |
| module | MAX_TABLE_COLUMNS | Module binding for MAX TABLE COLUMNS in module; use the enclosing contract and type below. | int | Module/process lifetime | 11 |
| module | MAX_HEADER_LENGTH | Module binding for MAX HEADER LENGTH in module; use the enclosing contract and type below. | int | Module/process lifetime | 12 |
| module | MAX_LABEL_LENGTH | Module binding for MAX LABEL LENGTH in module; use the enclosing contract and type below. | int | Module/process lifetime | 13 |
| ResultField | key | Typed binding for key in ResultField; use the enclosing contract and type below. | str | Enclosing invocation or class/instance lifetime | 20 |
| ResultField | label | Typed binding for label in ResultField; use the enclosing contract and type below. | str | Enclosing invocation or class/instance lifetime | 21 |
| ResultField | kind | Typed binding for kind in ResultField; use the enclosing contract and type below. | Literal['text', 'number', 'boolean', 'table'] | Enclosing invocation or class/instance lifetime | 22 |
| ResultField.__post_init__ | self | Owning instance; its attributes retain state for the instance lifetime. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 24 |
| build_results | gr | Parameter for gr in build_results; use the enclosing contract and type below. | Any | Enclosing invocation or class/instance lifetime | 34 |
| build_results | fields | Parameter for fields in build_results; use the enclosing contract and type below. | list[ResultField] | Enclosing invocation or class/instance lifetime | 34 |
| build_results | prefix | Parameter for prefix in build_results; use the enclosing contract and type below. | str | Enclosing invocation or class/instance lifetime | 34 |
| build_results | factories | Local binding for factories in build_results; use the enclosing contract and type below. | dict | Enclosing invocation or class/instance lifetime | 38 |
| build_results.comprehension_44 | field | Comprehension item for field in build_results.comprehension_44; use the enclosing contract and type below. | Element of the declared iterable | This comprehension only; does not leak into its enclosing scope | 48 |
| _table_cell | value | Value at the current validation/rendering boundary; apply the enclosing contract. | Any | Enclosing invocation or class/instance lifetime | 52 |
| result_values | value | Value at the current validation/rendering boundary; apply the enclosing contract. | dict &#124; None | Enclosing invocation or class/instance lifetime | 61 |
| result_values | fields | Parameter for fields in result_values; use the enclosing contract and type below. | list[ResultField] | Enclosing invocation or class/instance lifetime | 61 |
| result_values.comprehension_64 | field | Comprehension item for field in result_values.comprehension_64; use the enclosing contract and type below. | Element of the declared iterable | This comprehension only; does not leak into its enclosing scope | 64 |
| result_values.comprehension_65 | field | Comprehension item for field in result_values.comprehension_65; use the enclosing contract and type below. | Element of the declared iterable | This comprehension only; does not leak into its enclosing scope | 65 |
| result_values | output | Local binding for output in result_values; use the enclosing contract and type below. | list | Enclosing invocation or class/instance lifetime | 67 |
| result_values | field | Loop item for field in result_values; use the enclosing contract and type below. | Element of the declared iterable | Enclosing invocation or class/instance lifetime | 68 |
| result_values | item | Local binding for item in result_values; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 69, 96, 101 |
| result_values | valid | Local binding for valid in result_values; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 71, 73, 77, 79, 82 |
| result_values | headers | Local binding for headers in result_values; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 81 |
| result_values.comprehension_85 | key | Comprehension item for key in result_values.comprehension_85; use the enclosing contract and type below. | Element of the declared iterable | This comprehension only; does not leak into its enclosing scope | 86 |
| result_values.comprehension_88.comprehension_91 | cell | Comprehension item for cell in result_values.comprehension_88.comprehension_91; use the enclosing contract and type below. | Element of the declared iterable | This comprehension only; does not leak into its enclosing scope | 91 |
| result_values.comprehension_88 | row | Comprehension item for row in result_values.comprehension_88; use the enclosing contract and type below. | Element of the declared iterable | This comprehension only; does not leak into its enclosing scope | 92 |
| result_values.comprehension_98.comprehension_98 | key | Comprehension item for key in result_values.comprehension_98.comprehension_98; use the enclosing contract and type below. | Element of the declared iterable | This comprehension only; does not leak into its enclosing scope | 98 |
| result_values.comprehension_98 | row | Comprehension item for row in result_values.comprehension_98; use the enclosing contract and type below. | Element of the declared iterable | This comprehension only; does not leak into its enclosing scope | 98 |
