# Reference for src/agentix/application/code_cases.py

Suggest bounded schema-3 cases using reviewed JSON values and inert AST matching.

No generated Python is imported, compiled or executed. Only direct assignments,
JSON references and canonical call statements can propagate reviewed expectations.
Unsupported syntax leaves explicit pending fields for human completion.

Source fingerprint: 3b344bbda7de8ccde53ee5c3ab9e85e63238f5d0db9172ee9d556b9a994a9bc2

This reference is generated from maintained source without imports or execution. Assigned values are intentionally omitted. Runtime-dependent types are explicit; the enclosing docstring defines the behavioral contract. See [architecture](../ARCHITECTURE_QUALITY.md) for manually reviewed responsibility and dependency decisions.

## Classes and callables

### _same

Compare JSON values without conflating booleans and integer values.

Kind: callable. Declared return: bool. Source line: 21.

### _reference

Resolve only JSON constants/names/indexing; reject arbitrary Python work.

Kind: callable. Declared return: Any. Source line: 26.

### _match

Match direct calls to reviewed kwargs and copy only their approved results.

Kind: callable. Declared return: dict. Source line: 42.

### propose_cases

Return editable reviewed-data suggestions, provenance and unresolved fields.

Search is bounded and may be incomplete; proposals never authorize execution.
Callers must still validate exact schemas and require explicit human review.
Missing/incompatible cases and unsupported Python remain pending, not predicted.

Kind: callable. Declared return: dict. Source line: 106.

### acceptance_status

Return safe persistent review guidance and validity; never expose case values.

Missing fields are computed from current data, not historical proposal metadata.
A valid shape still requires the existing owner-bound human approval gate.

Kind: callable. Declared return: tuple[bool, str]. Source line: 164.

## Variables and parameters

| Scope | Name | Role and meaning | Type | Lifetime | Writes |
| --- | --- | --- | --- | --- | --- |
| module | ast | Imported dependency for ast in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 8 |
| module | itertools | Imported dependency for itertools in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 9 |
| module | json | Imported dependency for json in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 10 |
| module | deepcopy | Imported dependency for deepcopy in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 11 |
| module | Any | Imported dependency for Any in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 12 |
| module | validate_value | Imported dependency for validate value in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 14 |
| module | ApprovedTool | Imported dependency for ApprovedTool in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 15 |
| module | MAX_PROPOSALS | Module binding for MAX PROPOSALS in module; use the enclosing contract and type below. | int | Module/process lifetime | 17 |
| module | MAX_VALUES | Module binding for MAX VALUES in module; use the enclosing contract and type below. | int | Module/process lifetime | 18 |
| _same | left | Parameter for left in _same; use the enclosing contract and type below. | Any | Enclosing invocation or class/instance lifetime | 21 |
| _same | right | Parameter for right in _same; use the enclosing contract and type below. | Any | Enclosing invocation or class/instance lifetime | 21 |
| _reference | node | Parameter for node in _reference; use the enclosing contract and type below. | ast.expr | Enclosing invocation or class/instance lifetime | 26 |
| _reference | payload | Parameter for payload in _reference; use the enclosing contract and type below. | dict | Enclosing invocation or class/instance lifetime | 26 |
| _reference | bindings | Parameter for bindings in _reference; use the enclosing contract and type below. | dict | Enclosing invocation or class/instance lifetime | 26 |
| _reference | value | Value at the current validation/rendering boundary; apply the enclosing contract. | Return type of _reference; see its callable contract | Enclosing invocation or class/instance lifetime | 35 |
| _reference | index | Local binding for index in _reference; use the enclosing contract and type below. | Return type of _reference; see its callable contract | Enclosing invocation or class/instance lifetime | 36 |
| _match | statements | Parameter for statements in _match; use the enclosing contract and type below. | list[ast.stmt] | Enclosing invocation or class/instance lifetime | 43 |
| _match | payload | Parameter for payload in _match; use the enclosing contract and type below. | dict | Enclosing invocation or class/instance lifetime | 43 |
| _match | widgets | Parameter for widgets in _match; use the enclosing contract and type below. | dict | Enclosing invocation or class/instance lifetime | 43 |
| _match | cases | Parameter for cases in _match; use the enclosing contract and type below. | dict | Enclosing invocation or class/instance lifetime | 43 |
| _match | tools | Parameter for tools in _match; use the enclosing contract and type below. | dict | Enclosing invocation or class/instance lifetime | 43 |
| _match | bindings | Local binding for bindings in _match; use the enclosing contract and type below. | tuple | Enclosing invocation or class/instance lifetime | 46 |
| _match | expected | Reviewed expected observation kept outside untrusted child execution. | tuple | Enclosing invocation or class/instance lifetime | 46 |
| _match | statement | Loop item for statement in _match; use the enclosing contract and type below. | Element of the declared iterable | Enclosing invocation or class/instance lifetime | 47 |
| _match | target | Local binding for target in _match; use the enclosing contract and type below. | NoneType | Enclosing invocation or class/instance lifetime | 50, 56 |
| _match | expression | Local binding for expression in _match; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 57, 59 |
| _match | identity | Explicit owner identity used by a session factory or fixture. | Return type of _reference; see its callable contract | Enclosing invocation or class/instance lifetime | 70 |
| _match.comprehension_74 | k | Comprehension item for k in _match.comprehension_74; use the enclosing contract and type below. | Element of the declared iterable | This comprehension only; does not leak into its enclosing scope | 74 |
| _match | schema | Local binding for schema in _match; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 77 |
| _match | kwargs | Bounded JSON keyword arguments; no executable objects are accepted. | Return type of dict; see its callable contract | Enclosing invocation or class/instance lifetime | 78 |
| _match.comprehension_80 | k | Comprehension item for k in _match.comprehension_80; use the enclosing contract and type below. | Element of the declared iterable | This comprehension only; does not leak into its enclosing scope | 80 |
| _match | found | Local binding for found in _match; use the enclosing contract and type below. | Return type of next; see its callable contract | Enclosing invocation or class/instance lifetime | 82 |
| _match.comprehension_83 | case | Comprehension item for case in _match.comprehension_83; use the enclosing contract and type below. | Element of the declared iterable | This comprehension only; does not leak into its enclosing scope | 85 |
| _match | value | Value at the current validation/rendering boundary; apply the enclosing contract. | Return type of deepcopy; see its callable contract | Enclosing invocation or class/instance lifetime | 92, 96 |
| propose_cases | assembly | Parameter for assembly in propose_cases; use the enclosing contract and type below. | dict | Enclosing invocation or class/instance lifetime | 106 |
| propose_cases | tools | Parameter for tools in propose_cases; use the enclosing contract and type below. | dict[str, ApprovedTool] | Enclosing invocation or class/instance lifetime | 106 |
| propose_cases | widgets | Local binding for widgets in propose_cases; use the enclosing contract and type below. | dict | Enclosing invocation or class/instance lifetime | 113 |
| propose_cases.comprehension_113 | item | Comprehension item for item in propose_cases.comprehension_113; use the enclosing contract and type below. | Element of the declared iterable | This comprehension only; does not leak into its enclosing scope | 113 |
| propose_cases | cases | Local binding for cases in propose_cases; use the enclosing contract and type below. | dict | Enclosing invocation or class/instance lifetime | 114 |
| propose_cases.comprehension_114.comprehension_115 | case | Comprehension item for case in propose_cases.comprehension_114.comprehension_115; use the enclosing contract and type below. | Element of the declared iterable | This comprehension only; does not leak into its enclosing scope | 117 |
| propose_cases.comprehension_114 | identity | Explicit owner identity used by a session factory or fixture. | Element of the declared iterable | This comprehension only; does not leak into its enclosing scope | 120 |
| propose_cases.comprehension_114 | name | Current identifier selected by parsing, lookup or dependency registration. | Element of the declared iterable | This comprehension only; does not leak into its enclosing scope | 120 |
| propose_cases | domains | Local binding for domains in propose_cases; use the enclosing contract and type below. | dict | Enclosing invocation or class/instance lifetime | 122 |
| propose_cases | values | Local binding for values in propose_cases; use the enclosing contract and type below. | list | Enclosing invocation or class/instance lifetime | 123, 144 |
| propose_cases.comprehension_123 | choices | Comprehension item for choices in propose_cases.comprehension_123; use the enclosing contract and type below. | Element of the declared iterable | This comprehension only; does not leak into its enclosing scope | 124 |
| propose_cases.comprehension_123 | case | Comprehension item for case in propose_cases.comprehension_123; use the enclosing contract and type below. | Element of the declared iterable | This comprehension only; does not leak into its enclosing scope | 124 |
| propose_cases.comprehension_123 | value | Value at the current validation/rendering boundary; apply the enclosing contract. | Element of the declared iterable | This comprehension only; does not leak into its enclosing scope | 124 |
| propose_cases | name | Current identifier selected by parsing, lookup or dependency registration. | Element of the declared iterable | Enclosing invocation or class/instance lifetime | 126 |
| propose_cases | shape | Loop item for shape in propose_cases; use the enclosing contract and type below. | Element of the declared iterable | Enclosing invocation or class/instance lifetime | 126 |
| propose_cases | value | Value at the current validation/rendering boundary; apply the enclosing contract. | Element of the declared iterable | Enclosing invocation or class/instance lifetime | 128 |
| propose_cases.comprehension_133 | prior | Comprehension item for prior in propose_cases.comprehension_133; use the enclosing contract and type below. | Element of the declared iterable | This comprehension only; does not leak into its enclosing scope | 133 |
| propose_cases | tree | Local binding for tree in propose_cases; use the enclosing contract and type below. | Return type of parse; see its callable contract | Enclosing invocation or class/instance lifetime | 137 |
| propose_cases | entry | Local binding for entry in propose_cases; use the enclosing contract and type below. | Return type of next; see its callable contract | Enclosing invocation or class/instance lifetime | 138 |
| propose_cases.comprehension_139 | node | Comprehension item for node in propose_cases.comprehension_139; use the enclosing contract and type below. | Element of the declared iterable | This comprehension only; does not leak into its enclosing scope | 139 |
| propose_cases | names | Local binding for names in propose_cases; use the enclosing contract and type below. | list | Enclosing invocation or class/instance lifetime | 142 |
| propose_cases.comprehension_142 | name | Current identifier selected by parsing, lookup or dependency registration. | Element of the declared iterable | This comprehension only; does not leak into its enclosing scope | 142 |
| propose_cases.comprehension_142 | choices | Comprehension item for choices in propose_cases.comprehension_142; use the enclosing contract and type below. | Element of the declared iterable | This comprehension only; does not leak into its enclosing scope | 142 |
| propose_cases | best_payload | Local binding for best payload in propose_cases; use the enclosing contract and type below. | tuple | Enclosing invocation or class/instance lifetime | 143, 150 |
| propose_cases | best_expected | Local binding for best expected in propose_cases; use the enclosing contract and type below. | tuple | Enclosing invocation or class/instance lifetime | 143, 150 |
| propose_cases.comprehension_145 | name | Current identifier selected by parsing, lookup or dependency registration. | Element of the declared iterable | This comprehension only; does not leak into its enclosing scope | 145 |
| propose_cases | payload | Local binding for payload in propose_cases; use the enclosing contract and type below. | Return type of dict; see its callable contract | Enclosing invocation or class/instance lifetime | 147 |
| propose_cases | expected | Reviewed expected observation kept outside untrusted child execution. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 148 |
| propose_cases | pending | Defensive pending-approval snapshot; never a capability to approve another owner. | list | Enclosing invocation or class/instance lifetime | 153, 154 |
| propose_cases.comprehension_153 | name | Current identifier selected by parsing, lookup or dependency registration. | Element of the declared iterable | This comprehension only; does not leak into its enclosing scope | 153 |
| propose_cases.comprehension_154 | name | Current identifier selected by parsing, lookup or dependency registration. | Element of the declared iterable | This comprehension only; does not leak into its enclosing scope | 154 |
| propose_cases.comprehension_160 | name | Current identifier selected by parsing, lookup or dependency registration. | Element of the declared iterable | This comprehension only; does not leak into its enclosing scope | 160 |
| acceptance_status | snapshot | Parameter for snapshot in acceptance_status; use the enclosing contract and type below. | dict | Enclosing invocation or class/instance lifetime | 164 |
| acceptance_status | validate_acceptance | Imported dependency for validate acceptance in acceptance_status; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 170 |
| acceptance_status | manifest | Versioned inventory or launch record; not an execution-authorization capability. | Return type of get; see its callable contract | Enclosing invocation or class/instance lifetime | 172 |
| acceptance_status | acceptance | Local binding for acceptance in acceptance_status; use the enclosing contract and type below. | Return type of get; see its callable contract | Enclosing invocation or class/instance lifetime | 175 |
| acceptance_status | payload | Local binding for payload in acceptance_status; use the enclosing contract and type below. | tuple | Enclosing invocation or class/instance lifetime | 176 |
| acceptance_status | expected | Reviewed expected observation kept outside untrusted child execution. | tuple | Enclosing invocation or class/instance lifetime | 176 |
| acceptance_status | missing | Local binding for missing in acceptance_status; use the enclosing contract and type below. | list | Enclosing invocation or class/instance lifetime | 177, 182 |
| acceptance_status.comprehension_177 | name | Current identifier selected by parsing, lookup or dependency registration. | Element of the declared iterable | This comprehension only; does not leak into its enclosing scope | 179 |
| acceptance_status.comprehension_182 | widget | Comprehension item for widget in acceptance_status.comprehension_182; use the enclosing contract and type below. | Element of the declared iterable | This comprehension only; does not leak into its enclosing scope | 184 |
| acceptance_status | instruction | Local binding for instruction in acceptance_status; use the enclosing contract and type below. | str | Enclosing invocation or class/instance lifetime | 187 |
| acceptance_status | details | Local binding for details in acceptance_status; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 191 |
