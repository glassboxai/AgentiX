# Reference for src/agentix/application/tool_repair.py

Explicit repair of rejected tool source/tests; native validation and manual acceptance.

Source fingerprint: e55ecd8643dfc564bd12876c19157b133c9832d41da7a5dbae6ac28288a8d7e7

This reference is generated from maintained source without imports or execution. Assigned values are intentionally omitted. Runtime-dependent types are explicit; the enclosing docstring defines the behavioral contract. See [architecture](../ARCHITECTURE_QUALITY.md) for manually reviewed responsibility and dependency decisions.

## Classes and callables

### RejectedTool

Owner-retained proposed buffers; these values never authorize execution.

Kind: class. Declared return: Not declared / class. Source line: 17.

### _member

Resolve only a conventional member; reject file aliases before reads/writes.

Kind: callable. Declared return: Path. Source line: 26.

### capture_rejection

Retain only an actually denied code/test/specification/acceptance proposal.

Kind: callable. Declared return: RejectedTool | None. Source line: 38.

### ToolRepair

Save user-reviewed buffers and explicitly restart the existing validation gates.

Kind: class. Declared return: Not declared / class. Source line: 76.

### ToolRepair.__init__

Inject metadata, native tool operations and a data-only proposal boundary.

Kind: callable. Declared return: Not declared / class. Source line: 79.

### ToolRepair.save_and_validate

Validate both buffers, revoke old grants, save and perform fresh validation.

Save is an explicit owner action, not an authorization to execute. Native
unittest success remains provisional. The generated cases require manual
review and host comparison. A successful value case is executed through
the normal permission-aware tool executor to establish durable reuse.

Kind: callable. Declared return: str. Source line: 87.

## Variables and parameters

| Scope | Name | Role and meaning | Type | Lifetime | Writes |
| --- | --- | --- | --- | --- | --- |
| module | ast | Imported dependency for ast in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 3 |
| module | hashlib | Imported dependency for hashlib in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 4 |
| module | json | Imported dependency for json in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 5 |
| module | logging | Imported dependency for logging in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 6 |
| module | re | Imported dependency for re in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 7 |
| module | dataclass | Imported dependency for dataclass in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 8 |
| module | Path | Imported dependency for Path in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 9 |
| module | CatalogLock | Imported dependency for CatalogLock in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 11 |
| module | reject_alias | Imported dependency for reject alias in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 11 |
| module | logger | Module logger emitting bounded operation diagnostics rather than artifact bodies. | Return type of getLogger; see its callable contract | Module/process lifetime | 13 |
| RejectedTool | tool_name | Validated public tool identifier within the configured storage boundary. | str | Enclosing invocation or class/instance lifetime | 20 |
| RejectedTool | code | Source snapshot passed through approval, syntax checks and isolated staging. | str | Enclosing invocation or class/instance lifetime | 21 |
| RejectedTool | tests | Optional unittest source snapshot; child-authored success remains provisional. | str | Enclosing invocation or class/instance lifetime | 22 |
| RejectedTool | specification | Typed binding for specification in RejectedTool; use the enclosing contract and type below. | str | Enclosing invocation or class/instance lifetime | 23 |
| _member | security | Owner-scoped approval and path boundary injected into this service. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 26 |
| _member | name | Current identifier selected by parsing, lookup or dependency registration. | str | Enclosing invocation or class/instance lifetime | 26 |
| _member | suffix | Parameter for suffix in _member; use the enclosing contract and type below. | str | Enclosing invocation or class/instance lifetime | 26 |
| _member | expected | Reviewed expected observation kept outside untrusted child execution. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 28 |
| _member | resolved | Local binding for resolved in _member; use the enclosing contract and type below. | Return type of Path; see its callable contract | Enclosing invocation or class/instance lifetime | 29 |
| capture_rejection | controller | Parameter for controller in capture_rejection; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 38 |
| capture_rejection | pending | Defensive pending-approval snapshot; never a capability to approve another owner. | dict | Enclosing invocation or class/instance lifetime | 38 |
| capture_rejection | security | Owner-scoped approval and path boundary injected into this service. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 40 |
| capture_rejection | value | Value at the current validation/rendering boundary; apply the enclosing contract. | Return type of str; see its callable contract | Enclosing invocation or class/instance lifetime | 41 |
| capture_rejection | match | Local binding for match in capture_rejection; use the enclosing contract and type below. | Return type of fullmatch; see its callable contract | Enclosing invocation or class/instance lifetime | 43 |
| capture_rejection | name | Current identifier selected by parsing, lookup or dependency registration. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 44, 47 |
| capture_rejection | candidate | Local binding for candidate in capture_rejection; use the enclosing contract and type below. | Return type of Path; see its callable contract | Enclosing invocation or class/instance lifetime | 46 |
| capture_rejection | buffers | Local binding for buffers in capture_rejection; use the enclosing contract and type below. | dict | Enclosing invocation or class/instance lifetime | 56 |
| capture_rejection | key | Loop item for key in capture_rejection; use the enclosing contract and type below. | Element of the declared iterable | Enclosing invocation or class/instance lifetime | 57 |
| capture_rejection | suffix | Loop item for suffix in capture_rejection; use the enclosing contract and type below. | Element of the declared iterable | Enclosing invocation or class/instance lifetime | 57 |
| capture_rejection | path | Path under validation or an explicitly scoped maintained source path. | Return type of _member; see its callable contract | Enclosing invocation or class/instance lifetime | 62 |
| capture_rejection | text | Local binding for text in capture_rejection; use the enclosing contract and type below. | Return type of get; see its callable contract | Enclosing invocation or class/instance lifetime | 64, 67, 69 |
| capture_rejection | stream | Managed resource for stream in capture_rejection; use the enclosing contract and type below. | Return type of open; see its callable contract | Context-manager block; exit invokes its cleanup protocol | 66 |
| ToolRepair.__init__ | self | Owning instance; its attributes retain state for the instance lifetime. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 79 |
| ToolRepair.__init__ | security | Owner-scoped approval and path boundary injected into this service. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 79 |
| ToolRepair.__init__ | operations | Parameter for operations in ToolRepair.__init__; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 79 |
| ToolRepair.__init__ | apps | Parameter for apps in ToolRepair.__init__; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 79 |
| ToolRepair.__init__ | propose_cases | Parameter for propose cases in ToolRepair.__init__; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 79 |
| ToolRepair.__init__ | on_saved | Parameter for on saved in ToolRepair.__init__; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 79 |
| ToolRepair.__init__ | capacity | Parameter for capacity in ToolRepair.__init__; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 79 |
| ToolRepair.__init__ | _WORK_CAPACITY | Imported dependency for WORK CAPACITY in ToolRepair.__init__; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 81 |
| ToolRepair.__init__ | self.security | Owner-scoped approval and path boundary injected into this service. | tuple | Enclosing invocation or class/instance lifetime | 83 |
| ToolRepair.__init__ | self.operations | Attribute for operations in ToolRepair.__init__; use the enclosing contract and type below. | tuple | Enclosing invocation or class/instance lifetime | 83 |
| ToolRepair.__init__ | self.apps | Attribute for apps in ToolRepair.__init__; use the enclosing contract and type below. | tuple | Enclosing invocation or class/instance lifetime | 83 |
| ToolRepair.__init__ | self.propose_cases | Attribute for propose cases in ToolRepair.__init__; use the enclosing contract and type below. | tuple | Enclosing invocation or class/instance lifetime | 84 |
| ToolRepair.__init__ | self.on_saved | Attribute for on saved in ToolRepair.__init__; use the enclosing contract and type below. | tuple | Enclosing invocation or class/instance lifetime | 84 |
| ToolRepair.__init__ | self.capacity | Attribute for capacity in ToolRepair.__init__; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 85 |
| ToolRepair.save_and_validate | self | Owning instance; its attributes retain state for the instance lifetime. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 87 |
| ToolRepair.save_and_validate | draft | Parameter for draft in ToolRepair.save_and_validate; use the enclosing contract and type below. | RejectedTool | Enclosing invocation or class/instance lifetime | 87 |
| ToolRepair.save_and_validate | code | Source snapshot passed through approval, syntax checks and isolated staging. | str | Enclosing invocation or class/instance lifetime | 87 |
| ToolRepair.save_and_validate | tests | Optional unittest source snapshot; child-authored success remains provisional. | str | Enclosing invocation or class/instance lifetime | 87 |
| ToolRepair.save_and_validate | value | Value at the current validation/rendering boundary; apply the enclosing contract. | Element of the declared iterable | Enclosing invocation or class/instance lifetime | 99 |
| ToolRepair.save_and_validate | extract_tool_schema | Imported dependency for extract tool schema in ToolRepair.save_and_validate; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 112 |
| ToolRepair.save_and_validate | code_path | Local binding for code path in ToolRepair.save_and_validate; use the enclosing contract and type below. | Return type of _member; see its callable contract | Enclosing invocation or class/instance lifetime | 124 |
| ToolRepair.save_and_validate | tests_path | Local binding for tests path in ToolRepair.save_and_validate; use the enclosing contract and type below. | Return type of _member; see its callable contract | Enclosing invocation or class/instance lifetime | 125 |
| ToolRepair.save_and_validate | specification_path | Local binding for specification path in ToolRepair.save_and_validate; use the enclosing contract and type below. | Return type of _member; see its callable contract | Enclosing invocation or class/instance lifetime | 126 |
| ToolRepair.save_and_validate | identity | Explicit owner identity used by a session factory or fixture. | tuple | Enclosing invocation or class/instance lifetime | 132 |
| ToolRepair.save_and_validate | path | Path under validation or an explicitly scoped maintained source path. | Element of the declared iterable | Enclosing invocation or class/instance lifetime | 133 |
| ToolRepair.save_and_validate | provisional | Local binding for provisional in ToolRepair.save_and_validate; use the enclosing contract and type below. | Return type of verify_existing_tool_tool; see its callable contract | Enclosing invocation or class/instance lifetime | 142 |
| ToolRepair.save_and_validate | proposal | Local binding for proposal in ToolRepair.save_and_validate; use the enclosing contract and type below. | Return type of propose_cases; see its callable contract | Enclosing invocation or class/instance lifetime | 146 |
| ToolRepair.save_and_validate.comprehension_152 | node | Comprehension item for node in ToolRepair.save_and_validate.comprehension_152; use the enclosing contract and type below. | Element of the declared iterable | This comprehension only; does not leak into its enclosing scope | 154 |
| ToolRepair.save_and_validate | result | Intermediate or returned outcome; consult the callable contract for trust/validation. | Return type of submit_acceptance_cases_tool; see its callable contract | Enclosing invocation or class/instance lifetime | 161 |
| ToolRepair.save_and_validate | context | Local binding for context in ToolRepair.save_and_validate; use the enclosing contract and type below. | Return type of acceptance_context; see its callable contract | Enclosing invocation or class/instance lifetime | 165 |
| ToolRepair.save_and_validate | case | Loop item for case in ToolRepair.save_and_validate; use the enclosing contract and type below. | Element of the declared iterable | Enclosing invocation or class/instance lifetime | 166 |
| ToolRepair.save_and_validate | sample | Local binding for sample in ToolRepair.save_and_validate; use the enclosing contract and type below. | Return type of execute_generated_tool_tool; see its callable contract | Enclosing invocation or class/instance lifetime | 168 |
