# Reference for src/agentix/ui/presentation.py

Bounded, escaped UI renderers for observations, catalogs and review evidence.

These helpers perform no execution or authorization. Literal result decoding is
data-only, bounded before parsing, and never substitutes model prose for evidence.
Unknown output remains readable text with the exact record in a disclosure.

Source fingerprint: 05d04b23fa5d2ad1a38cf7bba7383ce636786c70d992a21c45de6cc4d7320f19

This reference is generated from maintained source without imports or execution. Assigned values are intentionally omitted. Runtime-dependent types are explicit; the enclosing docstring defines the behavioral contract. See [architecture](../ARCHITECTURE_QUALITY.md) for manually reviewed responsibility and dependency decisions.

## Classes and callables

### _text

Escape bounded display text, including Markdown control punctuation.

Kind: callable. Declared return: str. Source line: 25.

### _label

Turn machine field names into readable headings without adding meaning.

Kind: callable. Declared return: str. Source line: 34.

### _disclosure

Render one initially collapsed native, keyboard-operable disclosure.

Kind: callable. Declared return: str. Source line: 39.

### _value

Format explicit monetary fields only when the query identifies currency.

Kind: callable. Declared return: str. Source line: 44.

### _data

Render a bounded structured result; preserve overflow in raw evidence.

Kind: callable. Declared return: str. Source line: 66.

### format_result

Display an existing host record without executing or certifying its payload.

Ordinary chat/error responses are escaped too. The recognized prefix is a
presentation convention, not a security capability; authorization stays in
the ledger. Original record text remains available, including undecodable data.

Kind: callable. Declared return: str. Source line: 99.

### format_catalog

Fold UI function details while leaving the agent/CLI catalog unchanged.

Kind: callable. Declared return: str. Source line: 123.

### render_validation

Summarize owner-scoped verdicts; expand expected/observed evidence on demand.

Kind: callable. Declared return: str. Source line: 136.

## Variables and parameters

| Scope | Name | Role and meaning | Type | Lifetime | Writes |
| --- | --- | --- | --- | --- | --- |
| module | ast | Imported dependency for ast in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 8 |
| module | html | Imported dependency for html in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 9 |
| module | json | Imported dependency for json in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 10 |
| module | re | Imported dependency for re in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 11 |
| module | Any | Imported dependency for Any in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 12 |
| module | DISPLAY_TEXT_LIMIT | Module binding for DISPLAY TEXT LIMIT in module; use the enclosing contract and type below. | int | Module/process lifetime | 14 |
| module | MAX_NESTING_DEPTH | Module binding for MAX NESTING DEPTH in module; use the enclosing contract and type below. | int | Module/process lifetime | 15 |
| module | MAX_DICT_ENTRIES | Module binding for MAX DICT ENTRIES in module; use the enclosing contract and type below. | int | Module/process lifetime | 16 |
| module | MAX_TABLE_ROWS | Module binding for MAX TABLE ROWS in module; use the enclosing contract and type below. | int | Module/process lifetime | 17 |
| module | MAX_TABLE_COLUMNS | Module binding for MAX TABLE COLUMNS in module; use the enclosing contract and type below. | int | Module/process lifetime | 18 |
| module | RESULT_PAYLOAD_LIMIT | Module binding for RESULT PAYLOAD LIMIT in module; use the enclosing contract and type below. | int | Module/process lifetime | 19 |
| module | RESULT_NODE_LIMIT | Module binding for RESULT NODE LIMIT in module; use the enclosing contract and type below. | int | Module/process lifetime | 20 |
| module | EXACT_MONEY_LIMIT | Module binding for EXACT MONEY LIMIT in module; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Module/process lifetime | 21 |
| module | CASE_EVIDENCE_LIMIT | Module binding for CASE EVIDENCE LIMIT in module; use the enclosing contract and type below. | int | Module/process lifetime | 22 |
| _text | value | Value at the current validation/rendering boundary; apply the enclosing contract. | Any | Enclosing invocation or class/instance lifetime | 25 |
| _text | text | Local binding for text in _text; use the enclosing contract and type below. | Return type of str; see its callable contract | Enclosing invocation or class/instance lifetime | 27 |
| _text | shortened | Local binding for shortened in _text; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 28 |
| _label | value | Value at the current validation/rendering boundary; apply the enclosing contract. | str | Enclosing invocation or class/instance lifetime | 34 |
| _disclosure | title | Parameter for title in _disclosure; use the enclosing contract and type below. | str | Enclosing invocation or class/instance lifetime | 39 |
| _disclosure | body | Parameter for body in _disclosure; use the enclosing contract and type below. | str | Enclosing invocation or class/instance lifetime | 39 |
| _value | value | Value at the current validation/rendering boundary; apply the enclosing contract. | Any | Enclosing invocation or class/instance lifetime | 44 |
| _value | key | Parameter for key in _value; use the enclosing contract and type below. | str | Enclosing invocation or class/instance lifetime | 44 |
| _value | currency | Parameter for currency in _value; use the enclosing contract and type below. | str | Enclosing invocation or class/instance lifetime | 44 |
| _data | value | Value at the current validation/rendering boundary; apply the enclosing contract. | Any | Enclosing invocation or class/instance lifetime | 66 |
| _data | currency | Parameter for currency in _data; use the enclosing contract and type below. | str | Enclosing invocation or class/instance lifetime | 66 |
| _data | depth | Parameter for depth in _data; use the enclosing contract and type below. | int | Enclosing invocation or class/instance lifetime | 66 |
| _data | parts | Local binding for parts in _data; use the enclosing contract and type below. | list | Enclosing invocation or class/instance lifetime | 71 |
| _data | key | Loop item for key in _data; use the enclosing contract and type below. | Element of the declared iterable | Enclosing invocation or class/instance lifetime | 72 |
| _data | item | Loop item for item in _data; use the enclosing contract and type below. | Element of the declared iterable | Enclosing invocation or class/instance lifetime | 72 |
| _data.comprehension_80 | row | Comprehension item for row in _data.comprehension_80; use the enclosing contract and type below. | Element of the declared iterable | This comprehension only; does not leak into its enclosing scope | 80 |
| _data | keys | Local binding for keys in _data; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 81 |
| _data.comprehension_81 | row | Comprehension item for row in _data.comprehension_81; use the enclosing contract and type below. | Element of the declared iterable | This comprehension only; does not leak into its enclosing scope | 81 |
| _data.comprehension_81 | key | Comprehension item for key in _data.comprehension_81; use the enclosing contract and type below. | Element of the declared iterable | This comprehension only; does not leak into its enclosing scope | 81 |
| _data | header | Local binding for header in _data; use the enclosing contract and type below. | Return type of join; see its callable contract | Enclosing invocation or class/instance lifetime | 84 |
| _data.comprehension_84 | key | Comprehension item for key in _data.comprehension_84; use the enclosing contract and type below. | Element of the declared iterable | This comprehension only; does not leak into its enclosing scope | 84 |
| _data | rows | Local binding for rows in _data; use the enclosing contract and type below. | Return type of join; see its callable contract | Enclosing invocation or class/instance lifetime | 85 |
| _data.comprehension_85.comprehension_87 | key | Comprehension item for key in _data.comprehension_85.comprehension_87; use the enclosing contract and type below. | Element of the declared iterable | This comprehension only; does not leak into its enclosing scope | 87 |
| _data.comprehension_85 | row | Comprehension item for row in _data.comprehension_85; use the enclosing contract and type below. | Element of the declared iterable | This comprehension only; does not leak into its enclosing scope | 89 |
| _data.comprehension_94 | item | Comprehension item for item in _data.comprehension_94; use the enclosing contract and type below. | Element of the declared iterable | This comprehension only; does not leak into its enclosing scope | 94 |
| format_result | response | Bounded response text to render or validate; it is not executable code. | str | Enclosing invocation or class/instance lifetime | 99 |
| format_result | query | Original user request or a trusted test query; avoid payload logging by default. | str | Enclosing invocation or class/instance lifetime | 99 |
| format_result | raw | Local binding for raw in format_result; use the enclosing contract and type below. | Return type of _disclosure; see its callable contract | Enclosing invocation or class/instance lifetime | 108 |
| format_result | match | Local binding for match in format_result; use the enclosing contract and type below. | Return type of search; see its callable contract | Enclosing invocation or class/instance lifetime | 109 |
| format_result | tree | Local binding for tree in format_result; use the enclosing contract and type below. | Return type of parse; see its callable contract | Enclosing invocation or class/instance lifetime | 113 |
| format_result.comprehension_114 | _ | Comprehension item for  in format_result.comprehension_114; use the enclosing contract and type below. | Element of the declared iterable | This comprehension only; does not leak into its enclosing scope | 114 |
| format_result | value | Value at the current validation/rendering boundary; apply the enclosing contract. | Return type of literal_eval; see its callable contract | Enclosing invocation or class/instance lifetime | 116 |
| format_result | currency | Local binding for currency in format_result; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 119 |
| format_catalog | markdown | Parameter for markdown in format_catalog; use the enclosing contract and type below. | str | Enclosing invocation or class/instance lifetime | 123 |
| format_catalog | entries | Local binding for entries in format_catalog; use the enclosing contract and type below. | Return type of split; see its callable contract | Enclosing invocation or class/instance lifetime | 125 |
| format_catalog | rendered | Local binding for rendered in format_catalog; use the enclosing contract and type below. | list | Enclosing invocation or class/instance lifetime | 128 |
| format_catalog | entry | Loop item for entry in format_catalog; use the enclosing contract and type below. | Element of the declared iterable | Enclosing invocation or class/instance lifetime | 129 |
| format_catalog | name | Current identifier selected by parsing, lookup or dependency registration. | Return type of partition; see its callable contract | Enclosing invocation or class/instance lifetime | 130 |
| format_catalog | separator | Local binding for separator in format_catalog; use the enclosing contract and type below. | Return type of partition; see its callable contract | Enclosing invocation or class/instance lifetime | 130 |
| format_catalog | details | Local binding for details in format_catalog; use the enclosing contract and type below. | Return type of partition; see its callable contract | Enclosing invocation or class/instance lifetime | 130 |
| render_validation | status | Parameter for status in render_validation; use the enclosing contract and type below. | dict[str, Any] | Enclosing invocation or class/instance lifetime | 136 |
| render_validation | labels | Local binding for labels in render_validation; use the enclosing contract and type below. | dict | Enclosing invocation or class/instance lifetime | 138 |
| render_validation | stage | Local binding for stage in render_validation; use the enclosing contract and type below. | Return type of get; see its callable contract | Enclosing invocation or class/instance lifetime | 149 |
| render_validation | result | Intermediate or returned outcome; consult the callable contract for trust/validation. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 150, 152, 156, 157, 165, 166 |
| render_validation | cases | Local binding for cases in render_validation; use the enclosing contract and type below. | Return type of get; see its callable contract | Enclosing invocation or class/instance lifetime | 153 |
| render_validation | passed | Local binding for passed in render_validation; use the enclosing contract and type below. | Return type of sum; see its callable contract | Enclosing invocation or class/instance lifetime | 155 |
| render_validation.comprehension_155 | case | Comprehension item for case in render_validation.comprehension_155; use the enclosing contract and type below. | Element of the declared iterable | This comprehension only; does not leak into its enclosing scope | 155 |
| render_validation | case | Loop item for case in render_validation; use the enclosing contract and type below. | Element of the declared iterable | Enclosing invocation or class/instance lifetime | 158 |
| render_validation | title | Local binding for title in render_validation; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 159 |
| render_validation | evidence | Local binding for evidence in render_validation; use the enclosing contract and type below. | Return type of dumps; see its callable contract | Enclosing invocation or class/instance lifetime | 160 |
| render_validation.comprehension_161 | key | Comprehension item for key in render_validation.comprehension_161; use the enclosing contract and type below. | Element of the declared iterable | This comprehension only; does not leak into its enclosing scope | 161 |
