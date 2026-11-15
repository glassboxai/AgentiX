# Reference for src/agentix/ui/application_presentation.py

Maintained presentation for generated applications; no executable child HTML.

Source fingerprint: 269b933a406b3762166a268eb3a2969bb641227d454a9f84cf8f9e4e32524d4c

This reference is generated from maintained source without imports or execution. Assigned values are intentionally omitted. Runtime-dependent types are explicit; the enclosing docstring defines the behavioral contract. See [architecture](../ARCHITECTURE_QUALITY.md) for manually reviewed responsibility and dependency decisions.

## Classes and callables

### _safe_description

Keep a bounded single-line description; drop markup characters from model text.

Kind: callable. Declared return: str. Source line: 32.

### _example_value

Derive one JSON example from the declared closed shape, never from child code.

Kind: callable. Declared return: object. Source line: 43.

### describe_data_inputs

Render the reviewed input contract and one example payload as Markdown.

Only the closed ``inputs`` mapping is read; no child module is imported and no
value is executed. Keys are validated identifiers and descriptions are bounded
to inert text, so the result is safe for a Gradio Markdown output.

Kind: callable. Declared return: str. Source line: 63.

### named_result_rows

Render observed named results as bounded table cells for one execution.

The mapping is host-observed output from the isolated worker; every cell is
converted to bounded text so no object, NaN or oversized body reaches the UI.

Kind: callable. Declared return: dict. Source line: 89.

### generated_application_frame

Frame only the validated supervisor URL, without a reactive Gradio Group ID.

The heading keeps the maintained cyan label and offers the same already
validated loopback origin as a separate browser tab. The optional application
name only labels that section and link; the isolated page titles itself from
its own staged snapshot, never from a query parameter.

Kind: callable. Declared return: str. Source line: 108.

## Variables and parameters

| Scope | Name | Role and meaning | Type | Lifetime | Writes |
| --- | --- | --- | --- | --- | --- |
| module | html | Imported dependency for html in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 3 |
| module | json | Imported dependency for json in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 4 |
| module | iframe_html | Imported dependency for iframe html in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 6 |
| module | MAX_DESCRIPTION_LENGTH | Module binding for MAX DESCRIPTION LENGTH in module; use the enclosing contract and type below. | int | Module/process lifetime | 8 |
| module | MAX_RESULT_ROWS | Module binding for MAX RESULT ROWS in module; use the enclosing contract and type below. | int | Module/process lifetime | 9 |
| module | MAX_RESULT_CELL_LENGTH | Module binding for MAX RESULT CELL LENGTH in module; use the enclosing contract and type below. | int | Module/process lifetime | 10 |
| module | SAFE_DESCRIPTION | Module binding for SAFE DESCRIPTION in module; use the enclosing contract and type below. | Return type of frozenset; see its callable contract | Module/process lifetime | 11 |
| module | JSON_TYPE_NAMES | Module binding for JSON TYPE NAMES in module; use the enclosing contract and type below. | dict | Module/process lifetime | 14 |
| module | RESULT_TYPE_NAMES | Module binding for RESULT TYPE NAMES in module; use the enclosing contract and type below. | dict | Module/process lifetime | 21 |
| _safe_description | shape | Parameter for shape in _safe_description; use the enclosing contract and type below. | dict | Enclosing invocation or class/instance lifetime | 32 |
| _safe_description | text | Local binding for text in _safe_description; use the enclosing contract and type below. | Return type of get; see its callable contract | Enclosing invocation or class/instance lifetime | 34 |
| _safe_description | kept | Local binding for kept in _safe_description; use the enclosing contract and type below. | Return type of join; see its callable contract | Enclosing invocation or class/instance lifetime | 37 |
| _safe_description.comprehension_37 | character | Comprehension item for character in _safe_description.comprehension_37; use the enclosing contract and type below. | Element of the declared iterable | This comprehension only; does not leak into its enclosing scope | 38 |
| _example_value | shape | Parameter for shape in _example_value; use the enclosing contract and type below. | dict | Enclosing invocation or class/instance lifetime | 43 |
| _example_value | enum | Local binding for enum in _example_value; use the enclosing contract and type below. | Return type of get; see its callable contract | Enclosing invocation or class/instance lifetime | 45 |
| _example_value | kind | Local binding for kind in _example_value; use the enclosing contract and type below. | Return type of get; see its callable contract | Enclosing invocation or class/instance lifetime | 48 |
| _example_value | items | Local binding for items in _example_value; use the enclosing contract and type below. | Return type of get; see its callable contract | Enclosing invocation or class/instance lifetime | 58 |
| describe_data_inputs | manifest | Versioned inventory or launch record; not an execution-authorization capability. | dict | Enclosing invocation or class/instance lifetime | 63 |
| describe_data_inputs | inputs | Local binding for inputs in describe_data_inputs; use the enclosing contract and type below. | Return type of get; see its callable contract | Enclosing invocation or class/instance lifetime | 70 |
| describe_data_inputs | lines | Local binding for lines in describe_data_inputs; use the enclosing contract and type below. | list | Enclosing invocation or class/instance lifetime | 73 |
| describe_data_inputs | name | Current identifier selected by parsing, lookup or dependency registration. | Element of the declared iterable | Enclosing invocation or class/instance lifetime | 79 |
| describe_data_inputs | shape | Loop item for shape in describe_data_inputs; use the enclosing contract and type below. | Element of the declared iterable | Enclosing invocation or class/instance lifetime | 79 |
| describe_data_inputs | kind | Local binding for kind in describe_data_inputs; use the enclosing contract and type below. | Return type of get; see its callable contract | Enclosing invocation or class/instance lifetime | 80 |
| describe_data_inputs | example | Local binding for example in describe_data_inputs; use the enclosing contract and type below. | Return type of dumps; see its callable contract | Enclosing invocation or class/instance lifetime | 82 |
| describe_data_inputs.comprehension_83 | name | Current identifier selected by parsing, lookup or dependency registration. | Element of the declared iterable | This comprehension only; does not leak into its enclosing scope | 83 |
| describe_data_inputs.comprehension_83 | shape | Comprehension item for shape in describe_data_inputs.comprehension_83; use the enclosing contract and type below. | Element of the declared iterable | This comprehension only; does not leak into its enclosing scope | 83 |
| named_result_rows | value | Value at the current validation/rendering boundary; apply the enclosing contract. | dict | Enclosing invocation or class/instance lifetime | 89 |
| named_result_rows | rows | Local binding for rows in named_result_rows; use the enclosing contract and type below. | list | Enclosing invocation or class/instance lifetime | 95 |
| named_result_rows | name | Current identifier selected by parsing, lookup or dependency registration. | Element of the declared iterable | Enclosing invocation or class/instance lifetime | 96 |
| named_result_rows | item | Loop item for item in named_result_rows; use the enclosing contract and type below. | Element of the declared iterable | Enclosing invocation or class/instance lifetime | 96 |
| named_result_rows | rendered | Local binding for rendered in named_result_rows; use the enclosing contract and type below. | Return type of dumps; see its callable contract | Enclosing invocation or class/instance lifetime | 97 |
| generated_application_frame | url | Parameter for url in generated_application_frame; use the enclosing contract and type below. | str | Enclosing invocation or class/instance lifetime | 108 |
| generated_application_frame | name | Current identifier selected by parsing, lookup or dependency registration. | str | Enclosing invocation or class/instance lifetime | 108 |
| generated_application_frame | label | Local binding for label in generated_application_frame; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 116 |
