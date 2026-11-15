# Reference for src/agentix/application/templates/code/element_ids.py

Thread-safe readable widget IDs; structural Gradio Groups deliberately get no ID.

Source fingerprint: d885b1684f1296dd012a3ace3a1051201ef824c27caadd39cddbb9219edcfb76

This reference is generated from maintained source without imports or execution. Assigned values are intentionally omitted. Runtime-dependent types are explicit; the enclosing docstring defines the behavioral contract. See [architecture](../ARCHITECTURE_QUALITY.md) for manually reviewed responsibility and dependency decisions.

## Classes and callables

### ElementIds

Own one application's allocated widget scopes and stable control selectors.

Kind: class. Declared return: Not declared / class. Source line: 7.

### ElementIds.__init__

Create an empty registry; reuse this instance across the application's widgets.

Kind: callable. Declared return: None. Source line: 10.

### ElementIds.new_widget

Allocate a semantic instance scope; reject ambiguous or unsafe names.

Kind: callable. Declared return: str. Source line: 18.

### ElementIds.control

Return a stable allocated selector; Group duplication cannot be fixed by naming.

Kind: callable. Declared return: str | None. Source line: 42.

### ElementIds.api_name

Return the unique readable event namespace paired with an allocated scope.

Kind: callable. Declared return: str. Source line: 59.

## Variables and parameters

| Scope | Name | Role and meaning | Type | Lifetime | Writes |
| --- | --- | --- | --- | --- | --- |
| module | re | Imported dependency for re in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 3 |
| module | threading | Imported dependency for threading in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 4 |
| ElementIds.__init__ | self | Owning instance; its attributes retain state for the instance lifetime. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 10 |
| ElementIds.__init__ | self._lock | Attribute for lock in ElementIds.__init__; use the enclosing contract and type below. | Return type of RLock; see its callable contract | Enclosing invocation or class/instance lifetime | 12 |
| ElementIds.__init__ | self._scopes | Attribute for scopes in ElementIds.__init__; use the enclosing contract and type below. | set[str] | Enclosing invocation or class/instance lifetime | 13 |
| ElementIds.__init__ | self._used | Attribute for used in ElementIds.__init__; use the enclosing contract and type below. | set[str] | Enclosing invocation or class/instance lifetime | 14 |
| ElementIds.__init__ | self._controls | Attribute for controls in ElementIds.__init__; use the enclosing contract and type below. | dict[tuple[str, str], str] | Enclosing invocation or class/instance lifetime | 15 |
| ElementIds.__init__ | self._roles | Attribute for roles in ElementIds.__init__; use the enclosing contract and type below. | dict[str, set[str]] | Enclosing invocation or class/instance lifetime | 16 |
| ElementIds.new_widget | self | Owning instance; its attributes retain state for the instance lifetime. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 18 |
| ElementIds.new_widget | tool | Parameter for tool in ElementIds.new_widget; use the enclosing contract and type below. | str | Enclosing invocation or class/instance lifetime | 18 |
| ElementIds.new_widget | parameters | Parameter for parameters in ElementIds.new_widget; use the enclosing contract and type below. | list[str] &#124; None | Enclosing invocation or class/instance lifetime | 18 |
| ElementIds.new_widget | roles | Local binding for roles in ElementIds.new_widget; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 22 |
| ElementIds.new_widget.comprehension_23 | role | Comprehension item for role in ElementIds.new_widget.comprehension_23; use the enclosing contract and type below. | Element of the declared iterable | This comprehension only; does not leak into its enclosing scope | 25 |
| ElementIds.new_widget | number | Local binding for number in ElementIds.new_widget; use the enclosing contract and type below. | int | Enclosing invocation or class/instance lifetime | 29, 40 |
| ElementIds.new_widget | scope | Local binding for scope in ElementIds.new_widget; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 31 |
| ElementIds.new_widget | names | Local binding for names in ElementIds.new_widget; use the enclosing contract and type below. | set | Enclosing invocation or class/instance lifetime | 32 |
| ElementIds.new_widget.comprehension_32 | role | Comprehension item for role in ElementIds.new_widget.comprehension_32; use the enclosing contract and type below. | Element of the declared iterable | This comprehension only; does not leak into its enclosing scope | 32 |
| ElementIds.new_widget | role | Loop item for role in ElementIds.new_widget; use the enclosing contract and type below. | Element of the declared iterable | Enclosing invocation or class/instance lifetime | 37 |
| ElementIds.control | self | Owning instance; its attributes retain state for the instance lifetime. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 42 |
| ElementIds.control | scope | Parameter for scope in ElementIds.control; use the enclosing contract and type below. | str | Enclosing invocation or class/instance lifetime | 42 |
| ElementIds.control | role | Parameter for role in ElementIds.control; use the enclosing contract and type below. | str | Enclosing invocation or class/instance lifetime | 42 |
| ElementIds.control | key | Local binding for key in ElementIds.control; use the enclosing contract and type below. | tuple | Enclosing invocation or class/instance lifetime | 49 |
| ElementIds.control | candidate | Local binding for candidate in ElementIds.control; use the enclosing contract and type below. | tuple | Enclosing invocation or class/instance lifetime | 51, 53 |
| ElementIds.control | suffix | Local binding for suffix in ElementIds.control; use the enclosing contract and type below. | tuple | Enclosing invocation or class/instance lifetime | 51, 54 |
| ElementIds.api_name | self | Owning instance; its attributes retain state for the instance lifetime. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 59 |
| ElementIds.api_name | scope | Parameter for scope in ElementIds.api_name; use the enclosing contract and type below. | str | Enclosing invocation or class/instance lifetime | 59 |
