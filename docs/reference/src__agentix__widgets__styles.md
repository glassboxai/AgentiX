# Reference for src/agentix/widgets/styles.py

Conservative tool-scoped CSS grammar with no external resource or global rules.

Source fingerprint: 05a5c92592de75950ab53b6d9622b542630bfd552240dffcec2a970a37fdb6db

This reference is generated from maintained source without imports or execution. Assigned values are intentionally omitted. Runtime-dependent types are explicit; the enclosing docstring defines the behavioral contract. See [architecture](../ARCHITECTURE_QUALITY.md) for manually reviewed responsibility and dependency decisions.

## Classes and callables

### default_widget_css

Provide an independently editable file with the parent's default palette.

Kind: callable. Declared return: str. Source line: 29.

### validate_widget_css

Accept bounded static declarations for only one approved widget ID prefix.

No imports, URLs, escaped tokens, custom properties, nested rules, arbitrary
selectors or properties affecting visibility, positioning or interaction.
This intentionally supports a small customization surface, not arbitrary CSS.

Kind: callable. Declared return: str. Source line: 36.

## Variables and parameters

| Scope | Name | Role and meaning | Type | Lifetime | Writes |
| --- | --- | --- | --- | --- | --- |
| module | re | Imported dependency for re in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 3 |
| module | STYLE_SUFFIX | Module binding for STYLE SUFFIX in module; use the enclosing contract and type below. | str | Module/process lifetime | 5 |
| module | PROPERTIES | Module binding for PROPERTIES in module; use the enclosing contract and type below. | Return type of frozenset; see its callable contract | Module/process lifetime | 7 |
| module | DESCENDANTS | Module binding for DESCENDANTS in module; use the enclosing contract and type below. | tuple | Module/process lifetime | 25 |
| module | _DESCENDANT | Module binding for DESCENDANT in module; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Module/process lifetime | 26 |
| comprehension_26 | suffix | Comprehension item for suffix in comprehension_26; use the enclosing contract and type below. | Element of the declared iterable | This comprehension only; does not leak into its enclosing scope | 26 |
| default_widget_css | role | Parameter for role in default_widget_css; use the enclosing contract and type below. | str | Enclosing invocation or class/instance lifetime | 29 |
| validate_widget_css | css | Parameter for css in validate_widget_css; use the enclosing contract and type below. | str | Enclosing invocation or class/instance lifetime | 36 |
| validate_widget_css | role | Parameter for role in validate_widget_css; use the enclosing contract and type below. | str | Enclosing invocation or class/instance lifetime | 36 |
| validate_widget_css | rest | Local binding for rest in validate_widget_css; use the enclosing contract and type below. | Return type of strip; see its callable contract | Enclosing invocation or class/instance lifetime | 50, 86 |
| validate_widget_css | selector | Local binding for selector in validate_widget_css; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 51 |
| validate_widget_css | match | Local binding for match in validate_widget_css; use the enclosing contract and type below. | Return type of match; see its callable contract | Enclosing invocation or class/instance lifetime | 53 |
| validate_widget_css | declaration | Loop item for declaration in validate_widget_css; use the enclosing contract and type below. | Element of the declared iterable | Enclosing invocation or class/instance lifetime | 56 |
| validate_widget_css | name | Current identifier selected by parsing, lookup or dependency registration. | Return type of partition; see its callable contract | Enclosing invocation or class/instance lifetime | 59 |
| validate_widget_css | separator | Local binding for separator in validate_widget_css; use the enclosing contract and type below. | Return type of partition; see its callable contract | Enclosing invocation or class/instance lifetime | 59 |
| validate_widget_css | value | Value at the current validation/rendering boundary; apply the enclosing contract. | Return type of partition; see its callable contract | Enclosing invocation or class/instance lifetime | 59 |
| validate_widget_css | property_name | Local binding for property name in validate_widget_css; use the enclosing contract and type below. | tuple | Enclosing invocation or class/instance lifetime | 66 |
| validate_widget_css | property_value | Local binding for property value in validate_widget_css; use the enclosing contract and type below. | tuple | Enclosing invocation or class/instance lifetime | 66 |
| validate_widget_css | bounds | Local binding for bounds in validate_widget_css; use the enclosing contract and type below. | dict | Enclosing invocation or class/instance lifetime | 67 |
| validate_widget_css | minimum | Local binding for minimum in validate_widget_css; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 75 |
| validate_widget_css | maximum | Local binding for maximum in validate_widget_css; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 75 |
| validate_widget_css | count | Local binding for count in validate_widget_css; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 75 |
| validate_widget_css | pieces | Local binding for pieces in validate_widget_css; use the enclosing contract and type below. | Return type of split; see its callable contract | Enclosing invocation or class/instance lifetime | 76 |
| validate_widget_css | piece | Loop item for piece in validate_widget_css; use the enclosing contract and type below. | Element of the declared iterable | Enclosing invocation or class/instance lifetime | 79 |
