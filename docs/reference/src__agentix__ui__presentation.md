# Reference for src/agentix/ui/presentation.py

Bounded, escaped UI renderers for observations, catalogs and review evidence.

These helpers perform no execution or authorization. Literal result decoding is
data-only, bounded before parsing, and never substitutes model prose for evidence.
Unknown output remains readable text with the exact record in a disclosure.

Source fingerprint: d8153abff576a2d0cefb865917a6d3e7c0cdb8144cc1091fcc120a556e56117e

This reference is generated from maintained source without imports or execution. Assigned values are intentionally omitted. Runtime-dependent types are explicit; the enclosing docstring defines the behavioral contract. See [architecture](../ARCHITECTURE_QUALITY.md) for manually reviewed responsibility and dependency decisions.

## Classes and callables

### _text

Escape bounded display text, including Markdown control punctuation.

Kind: callable. Declared return: str. Source line: 15.

### _label

Turn machine field names into readable headings without adding meaning.

Kind: callable. Declared return: str. Source line: 22.

### _disclosure

Render one initially collapsed native, keyboard-operable disclosure.

Kind: callable. Declared return: str. Source line: 27.

### _value

Format explicit monetary fields only when the query identifies currency.

Kind: callable. Declared return: str. Source line: 32.

### _data

Render a bounded structured result; preserve overflow in raw evidence.

Kind: callable. Declared return: str. Source line: 54.

### format_result

Display an existing host record without executing or certifying its payload.

Ordinary chat/error responses are escaped too. The recognized prefix is a
presentation convention, not a security capability; authorization stays in
the ledger. Original record text remains available, including undecodable data.

Kind: callable. Declared return: str. Source line: 83.

### format_catalog

Fold UI function details while leaving the agent/CLI catalog unchanged.

Kind: callable. Declared return: str. Source line: 107.

### render_validation

Summarize owner-scoped verdicts; expand expected/observed evidence on demand.

Kind: callable. Declared return: str. Source line: 120.

## Variables and parameters

| Scope | Name | Role and meaning | Type | Lifetime | Writes |
| --- | --- | --- | --- | --- | --- |
| module | ast | Imported dependency for ast in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 8 |
| module | html | Imported dependency for html in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 9 |
| module | json | Imported dependency for json in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 10 |
| module | re | Imported dependency for re in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 11 |
| module | Any | Imported dependency for Any in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 12 |
| _text | value | Value at the current validation/rendering boundary; apply the enclosing contract. | Any | Enclosing invocation or class/instance lifetime | 15 |
| _text | text | Local binding for text in _text; use the enclosing contract and type below. | Return type of str; see its callable contract | Enclosing invocation or class/instance lifetime | 17 |
| _text | shortened | Local binding for shortened in _text; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 18 |
| _label | value | Value at the current validation/rendering boundary; apply the enclosing contract. | str | Enclosing invocation or class/instance lifetime | 22 |
| _disclosure | title | Parameter for title in _disclosure; use the enclosing contract and type below. | str | Enclosing invocation or class/instance lifetime | 27 |
| _disclosure | body | Parameter for body in _disclosure; use the enclosing contract and type below. | str | Enclosing invocation or class/instance lifetime | 27 |
| _value | value | Value at the current validation/rendering boundary; apply the enclosing contract. | Any | Enclosing invocation or class/instance lifetime | 32 |
| _value | key | Parameter for key in _value; use the enclosing contract and type below. | str | Enclosing invocation or class/instance lifetime | 32 |
| _value | currency | Parameter for currency in _value; use the enclosing contract and type below. | str | Enclosing invocation or class/instance lifetime | 32 |
| _data | value | Value at the current validation/rendering boundary; apply the enclosing contract. | Any | Enclosing invocation or class/instance lifetime | 54 |
| _data | currency | Parameter for currency in _data; use the enclosing contract and type below. | str | Enclosing invocation or class/instance lifetime | 54 |
| _data | depth | Parameter for depth in _data; use the enclosing contract and type below. | int | Enclosing invocation or class/instance lifetime | 54 |
| _data | parts | Local binding for parts in _data; use the enclosing contract and type below. | list | Enclosing invocation or class/instance lifetime | 59 |
| _data | key | Loop item for key in _data; use the enclosing contract and type below. | Element of the declared iterable | Enclosing invocation or class/instance lifetime | 60 |
| _data | item | Loop item for item in _data; use the enclosing contract and type below. | Element of the declared iterable | Enclosing invocation or class/instance lifetime | 60 |
| _data.comprehension_68 | row | Comprehension item for row in _data.comprehension_68; use the enclosing contract and type below. | Element of the declared iterable | This comprehension only; does not leak into its enclosing scope | 68 |
| _data | keys | Local binding for keys in _data; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 69 |
| _data.comprehension_69 | row | Comprehension item for row in _data.comprehension_69; use the enclosing contract and type below. | Element of the declared iterable | This comprehension only; does not leak into its enclosing scope | 69 |
| _data.comprehension_69 | key | Comprehension item for key in _data.comprehension_69; use the enclosing contract and type below. | Element of the declared iterable | This comprehension only; does not leak into its enclosing scope | 69 |
| _data | header | Local binding for header in _data; use the enclosing contract and type below. | Return type of join; see its callable contract | Enclosing invocation or class/instance lifetime | 70 |
| _data.comprehension_70 | key | Comprehension item for key in _data.comprehension_70; use the enclosing contract and type below. | Element of the declared iterable | This comprehension only; does not leak into its enclosing scope | 70 |
| _data | rows | Local binding for rows in _data; use the enclosing contract and type below. | Return type of join; see its callable contract | Enclosing invocation or class/instance lifetime | 71 |
| _data.comprehension_71.comprehension_73 | key | Comprehension item for key in _data.comprehension_71.comprehension_73; use the enclosing contract and type below. | Element of the declared iterable | This comprehension only; does not leak into its enclosing scope | 73 |
| _data.comprehension_71 | row | Comprehension item for row in _data.comprehension_71; use the enclosing contract and type below. | Element of the declared iterable | This comprehension only; does not leak into its enclosing scope | 75 |
| _data.comprehension_79 | item | Comprehension item for item in _data.comprehension_79; use the enclosing contract and type below. | Element of the declared iterable | This comprehension only; does not leak into its enclosing scope | 79 |
| format_result | response | Bounded response text to render or validate; it is not executable code. | str | Enclosing invocation or class/instance lifetime | 83 |
| format_result | query | Original user request or a trusted test query; avoid payload logging by default. | str | Enclosing invocation or class/instance lifetime | 83 |
| format_result | raw | Local binding for raw in format_result; use the enclosing contract and type below. | Return type of _disclosure; see its callable contract | Enclosing invocation or class/instance lifetime | 92 |
| format_result | match | Local binding for match in format_result; use the enclosing contract and type below. | Return type of search; see its callable contract | Enclosing invocation or class/instance lifetime | 93 |
| format_result | tree | Local binding for tree in format_result; use the enclosing contract and type below. | Return type of parse; see its callable contract | Enclosing invocation or class/instance lifetime | 97 |
| format_result.comprehension_98 | _ | Comprehension item for  in format_result.comprehension_98; use the enclosing contract and type below. | Element of the declared iterable | This comprehension only; does not leak into its enclosing scope | 98 |
| format_result | value | Value at the current validation/rendering boundary; apply the enclosing contract. | Return type of literal_eval; see its callable contract | Enclosing invocation or class/instance lifetime | 100 |
| format_result | currency | Local binding for currency in format_result; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 103 |
| format_catalog | markdown | Parameter for markdown in format_catalog; use the enclosing contract and type below. | str | Enclosing invocation or class/instance lifetime | 107 |
| format_catalog | entries | Local binding for entries in format_catalog; use the enclosing contract and type below. | Return type of split; see its callable contract | Enclosing invocation or class/instance lifetime | 109 |
| format_catalog | rendered | Local binding for rendered in format_catalog; use the enclosing contract and type below. | list | Enclosing invocation or class/instance lifetime | 112 |
| format_catalog | entry | Loop item for entry in format_catalog; use the enclosing contract and type below. | Element of the declared iterable | Enclosing invocation or class/instance lifetime | 113 |
| format_catalog | name | Current identifier selected by parsing, lookup or dependency registration. | Return type of partition; see its callable contract | Enclosing invocation or class/instance lifetime | 114 |
| format_catalog | separator | Local binding for separator in format_catalog; use the enclosing contract and type below. | Return type of partition; see its callable contract | Enclosing invocation or class/instance lifetime | 114 |
| format_catalog | details | Local binding for details in format_catalog; use the enclosing contract and type below. | Return type of partition; see its callable contract | Enclosing invocation or class/instance lifetime | 114 |
| render_validation | status | Parameter for status in render_validation; use the enclosing contract and type below. | dict[str, Any] | Enclosing invocation or class/instance lifetime | 120 |
| render_validation | labels | Local binding for labels in render_validation; use the enclosing contract and type below. | dict | Enclosing invocation or class/instance lifetime | 122 |
| render_validation | stage | Local binding for stage in render_validation; use the enclosing contract and type below. | Return type of get; see its callable contract | Enclosing invocation or class/instance lifetime | 133 |
| render_validation | result | Intermediate or returned outcome; consult the callable contract for trust/validation. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 134, 136, 140, 141, 149, 150 |
| render_validation | cases | Local binding for cases in render_validation; use the enclosing contract and type below. | Return type of get; see its callable contract | Enclosing invocation or class/instance lifetime | 137 |
| render_validation | passed | Local binding for passed in render_validation; use the enclosing contract and type below. | Return type of sum; see its callable contract | Enclosing invocation or class/instance lifetime | 139 |
| render_validation.comprehension_139 | case | Comprehension item for case in render_validation.comprehension_139; use the enclosing contract and type below. | Element of the declared iterable | This comprehension only; does not leak into its enclosing scope | 139 |
| render_validation | case | Loop item for case in render_validation; use the enclosing contract and type below. | Element of the declared iterable | Enclosing invocation or class/instance lifetime | 142 |
| render_validation | title | Local binding for title in render_validation; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 143 |
| render_validation | evidence | Local binding for evidence in render_validation; use the enclosing contract and type below. | Return type of dumps; see its callable contract | Enclosing invocation or class/instance lifetime | 144 |
| render_validation.comprehension_145 | key | Comprehension item for key in render_validation.comprehension_145; use the enclosing contract and type below. | Element of the declared iterable | This comprehension only; does not leak into its enclosing scope | 145 |
