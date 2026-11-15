# Reference for src/agentix/storage/application_catalog.py

Resolve Applications dependencies from the installed catalog and approval ledger.

No generated source is imported and no tool tests are executed. This adapter is
invoked by normal runtime only; engineering tests inject temporary trusted tools.

Source fingerprint: 12075f6c9a928dd9661a13a48adb53cb69e0e7d49b88c5891656dc62965e6ea5

This reference is generated from maintained source without imports or execution. Assigned values are intentionally omitted. Runtime-dependent types are explicit; the enclosing docstring defines the behavioral contract. See [architecture](../ARCHITECTURE_QUALITY.md) for manually reviewed responsibility and dependency decisions.

## Classes and callables

### CatalogDependencyError

Expose only maintained actionable catalog/approval errors to the owner UI.

Kind: class. Declared return: Not declared / class. Source line: 19.

### ApprovedTool

Exact installed source and reviewed identity; never a browser-supplied path.

Kind: class. Declared return: Not declared / class. Source line: 24.

### ApprovedToolRegistry

Require catalog membership and reusable approval before packaging a tool.

Kind: class. Declared return: Not declared / class. Source line: 37.

### ApprovedToolRegistry.__init__

Inject the same catalog and owner ledger used by the Tools controller.

Kind: callable. Declared return: None. Source line: 40.

### ApprovedToolRegistry.for_controller

Resolve services from the controller's actual catalog/validation adapters.

Kind: callable. Declared return: 'ApprovedToolRegistry'. Source line: 45.

### ApprovedToolRegistry.resolve

Return approved portable computation tools, or fail before model inference.

Roles are the approved catalog tool names themselves, so no fixed semantic
role registry or example tool name is required. Each entry carries the
canonical schema derived from its exact approved source.

Kind: callable. Declared return: dict[str, ApprovedTool]. Source line: 59.

### ApprovedToolRegistry.recheck

Reject removal, revocation or changed bytes/contracts without rerunning tests.

Kind: callable. Declared return: None. Source line: 110.

### CatalogToolRegistry

Discover approved canonical Annotated APIs; no fixed semantic role registry.

Kind: class. Declared return: Not declared / class. Source line: 118.

### CatalogToolRegistry.resolve

List a bounded portable approved catalog, skipping unapproved/legacy APIs.

This never runs tool tests or imports source. Unsupported entries remain
visible in Tools but are not offered as executable application dependencies.

Kind: callable. Declared return: dict[str, ApprovedTool]. Source line: 121.

### CatalogToolRegistry._scan

Resolve eligible entries and collect one owner-actionable reason per skip.

Kind: callable. Declared return: tuple[dict[str, ApprovedTool], dict[str, str]]. Source line: 150.

### CatalogToolRegistry.skip_reasons

Return bounded per-tool ineligibility reasons without raising or executing code.

Candidate presentation needs the cause behind an ineligible row so an owner is
never told to approve a tool whose approval is already current. Missing or
unreadable roots yield an empty mapping; no source bytes are included.

Kind: callable. Declared return: dict[str, str]. Source line: 178.

### CatalogToolRegistry._skip_reason

Return why one installed entry is ineligible, or None when it resolves.

Reasons are maintained owner-actionable categories only; source bytes,
prompts and approval internals are never included. No generated source is
imported and no tool tests are executed.

Kind: callable. Declared return: str | None. Source line: 199.

### CatalogToolRegistry.recheck

Only selected dependencies must match; unrelated catalog additions are allowed.

Kind: callable. Declared return: None. Source line: 247.

## Variables and parameters

| Scope | Name | Role and meaning | Type | Lifetime | Writes |
| --- | --- | --- | --- | --- | --- |
| module | logging | Imported dependency for logging in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 7 |
| module | Mapping | Imported dependency for Mapping in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 8 |
| module | dataclass | Imported dependency for dataclass in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 9 |
| module | Path | Imported dependency for Path in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 10 |
| module | Any | Imported dependency for Any in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 11 |
| module | allowed_modules | Imported dependency for allowed modules in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 13 |
| module | computation_only | Imported dependency for computation only in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 13 |
| module | unapproved_imports | Imported dependency for unapproved imports in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 13 |
| module | ToolCatalog | Imported dependency for ToolCatalog in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 14 |
| module | logger | Module logger emitting bounded operation diagnostics rather than artifact bodies. | Return type of getLogger; see its callable contract | Module/process lifetime | 16 |
| ApprovedTool | role | Typed binding for role in ApprovedTool; use the enclosing contract and type below. | str | Enclosing invocation or class/instance lifetime | 27 |
| ApprovedTool | tool_name | Validated public tool identifier within the configured storage boundary. | str | Enclosing invocation or class/instance lifetime | 28 |
| ApprovedTool | function | Typed binding for function in ApprovedTool; use the enclosing contract and type below. | str | Enclosing invocation or class/instance lifetime | 29 |
| ApprovedTool | code | Source snapshot passed through approval, syntax checks and isolated staging. | bytes | Enclosing invocation or class/instance lifetime | 30 |
| ApprovedTool | tests | Optional unittest source snapshot; child-authored success remains provisional. | bytes | Enclosing invocation or class/instance lifetime | 31 |
| ApprovedTool | contract_digest | Typed binding for contract digest in ApprovedTool; use the enclosing contract and type below. | str | Enclosing invocation or class/instance lifetime | 32 |
| ApprovedTool | reviewed_contract | Typed binding for reviewed contract in ApprovedTool; use the enclosing contract and type below. | dict &#124; None | Enclosing invocation or class/instance lifetime | 33 |
| ApprovedTool | schema | Typed binding for schema in ApprovedTool; use the enclosing contract and type below. | dict &#124; None | Enclosing invocation or class/instance lifetime | 34 |
| ApprovedToolRegistry.__init__ | self | Owning instance; its attributes retain state for the instance lifetime. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 40 |
| ApprovedToolRegistry.__init__ | catalog | Parameter for catalog in ApprovedToolRegistry.__init__; use the enclosing contract and type below. | ToolCatalog | Enclosing invocation or class/instance lifetime | 40 |
| ApprovedToolRegistry.__init__ | ledger | Parameter for ledger in ApprovedToolRegistry.__init__; use the enclosing contract and type below. | Any | Enclosing invocation or class/instance lifetime | 40 |
| ApprovedToolRegistry.__init__ | self.catalog | Attribute for catalog in ApprovedToolRegistry.__init__; use the enclosing contract and type below. | tuple | Enclosing invocation or class/instance lifetime | 42 |
| ApprovedToolRegistry.__init__ | self.ledger | Attribute for ledger in ApprovedToolRegistry.__init__; use the enclosing contract and type below. | tuple | Enclosing invocation or class/instance lifetime | 42 |
| ApprovedToolRegistry.for_controller | cls | Class receiving this class-level operation. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 45 |
| ApprovedToolRegistry.for_controller | controller | Parameter for controller in ApprovedToolRegistry.for_controller; use the enclosing contract and type below. | Any | Enclosing invocation or class/instance lifetime | 45 |
| ApprovedToolRegistry.for_controller | catalog | Local binding for catalog in ApprovedToolRegistry.for_controller; use the enclosing contract and type below. | Return type of getattr; see its callable contract | Enclosing invocation or class/instance lifetime | 47 |
| ApprovedToolRegistry.for_controller | ledger | Local binding for ledger in ApprovedToolRegistry.for_controller; use the enclosing contract and type below. | Return type of getattr; see its callable contract | Enclosing invocation or class/instance lifetime | 48 |
| ApprovedToolRegistry.resolve | self | Owning instance; its attributes retain state for the instance lifetime. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 59 |
| ApprovedToolRegistry.resolve | Path | Imported dependency for Path in ApprovedToolRegistry.resolve; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 66 |
| ApprovedToolRegistry.resolve | extract_tool_schema | Imported dependency for extract tool schema in ApprovedToolRegistry.resolve; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 68 |
| ApprovedToolRegistry.resolve | root | Explicit root directory against which named paths are resolved. | Return type of Path; see its callable contract | Enclosing invocation or class/instance lifetime | 70 |
| ApprovedToolRegistry.resolve | result | Intermediate or returned outcome; consult the callable contract for trust/validation. | dict | Enclosing invocation or class/instance lifetime | 75 |
| ApprovedToolRegistry.resolve | name | Current identifier selected by parsing, lookup or dependency registration. | Element of the declared iterable | Enclosing invocation or class/instance lifetime | 76 |
| ApprovedToolRegistry.resolve | code | Source snapshot passed through approval, syntax checks and isolated staging. | Return type of snapshot; see its callable contract | Enclosing invocation or class/instance lifetime | 81 |
| ApprovedToolRegistry.resolve | tests | Optional unittest source snapshot; child-authored success remains provisional. | Return type of snapshot; see its callable contract | Enclosing invocation or class/instance lifetime | 81 |
| ApprovedToolRegistry.resolve | context | Local binding for context in ApprovedToolRegistry.resolve; use the enclosing contract and type below. | Return type of acceptance_context; see its callable contract | Enclosing invocation or class/instance lifetime | 82 |
| ApprovedToolRegistry.resolve | schema | Local binding for schema in ApprovedToolRegistry.resolve; use the enclosing contract and type below. | Return type of extract_tool_schema; see its callable contract | Enclosing invocation or class/instance lifetime | 88 |
| ApprovedToolRegistry.resolve | exc | Caught exception for exc in ApprovedToolRegistry.resolve; use the enclosing contract and type below. | (ValueError, SyntaxError) | Current exception handler; Python clears this binding afterward | 89 |
| ApprovedToolRegistry.recheck | self | Owning instance; its attributes retain state for the instance lifetime. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 110 |
| ApprovedToolRegistry.recheck | expected | Reviewed expected observation kept outside untrusted child execution. | Mapping[str, ApprovedTool] | Enclosing invocation or class/instance lifetime | 110 |
| CatalogToolRegistry.resolve | self | Owning instance; its attributes retain state for the instance lifetime. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 121 |
| CatalogToolRegistry.resolve | Path | Imported dependency for Path in CatalogToolRegistry.resolve; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 127 |
| CatalogToolRegistry.resolve | root | Explicit root directory against which named paths are resolved. | Return type of Path; see its callable contract | Enclosing invocation or class/instance lifetime | 129 |
| CatalogToolRegistry.resolve | entries | Local binding for entries in CatalogToolRegistry.resolve; use the enclosing contract and type below. | Return type of list; see its callable contract | Enclosing invocation or class/instance lifetime | 134 |
| CatalogToolRegistry.resolve | result | Intermediate or returned outcome; consult the callable contract for trust/validation. | Return type of _scan; see its callable contract | Enclosing invocation or class/instance lifetime | 137 |
| CatalogToolRegistry.resolve | skipped | Local binding for skipped in CatalogToolRegistry.resolve; use the enclosing contract and type below. | Return type of _scan; see its callable contract | Enclosing invocation or class/instance lifetime | 137 |
| CatalogToolRegistry.resolve | detail | Local binding for detail in CatalogToolRegistry.resolve; use the enclosing contract and type below. | Return type of join; see its callable contract | Enclosing invocation or class/instance lifetime | 139 |
| CatalogToolRegistry.resolve.comprehension_139 | name | Current identifier selected by parsing, lookup or dependency registration. | Element of the declared iterable | This comprehension only; does not leak into its enclosing scope | 139 |
| CatalogToolRegistry.resolve.comprehension_139 | reason | Comprehension item for reason in CatalogToolRegistry.resolve.comprehension_139; use the enclosing contract and type below. | Element of the declared iterable | This comprehension only; does not leak into its enclosing scope | 139 |
| CatalogToolRegistry._scan | self | Owning instance; its attributes retain state for the instance lifetime. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 150 |
| CatalogToolRegistry._scan | entries | Parameter for entries in CatalogToolRegistry._scan; use the enclosing contract and type below. | list[Path] | Enclosing invocation or class/instance lifetime | 150 |
| CatalogToolRegistry._scan | extract_tool_schema | Imported dependency for extract tool schema in CatalogToolRegistry._scan; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 152 |
| CatalogToolRegistry._scan | result | Intermediate or returned outcome; consult the callable contract for trust/validation. | dict[str, ApprovedTool] | Enclosing invocation or class/instance lifetime | 154 |
| CatalogToolRegistry._scan | skipped | Typed binding for skipped in CatalogToolRegistry._scan; use the enclosing contract and type below. | dict[str, str] | Enclosing invocation or class/instance lifetime | 155 |
| CatalogToolRegistry._scan | directory | Loop item for directory in CatalogToolRegistry._scan; use the enclosing contract and type below. | Element of the declared iterable | Enclosing invocation or class/instance lifetime | 156 |
| CatalogToolRegistry._scan | name | Current identifier selected by parsing, lookup or dependency registration. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 157 |
| CatalogToolRegistry._scan | reason | Local binding for reason in CatalogToolRegistry._scan; use the enclosing contract and type below. | Return type of _skip_reason; see its callable contract | Enclosing invocation or class/instance lifetime | 158 |
| CatalogToolRegistry._scan | code | Source snapshot passed through approval, syntax checks and isolated staging. | Return type of snapshot; see its callable contract | Enclosing invocation or class/instance lifetime | 160 |
| CatalogToolRegistry._scan | tests | Optional unittest source snapshot; child-authored success remains provisional. | Return type of snapshot; see its callable contract | Enclosing invocation or class/instance lifetime | 160 |
| CatalogToolRegistry._scan | context | Local binding for context in CatalogToolRegistry._scan; use the enclosing contract and type below. | Return type of acceptance_context; see its callable contract | Enclosing invocation or class/instance lifetime | 161 |
| CatalogToolRegistry._scan | schema | Local binding for schema in CatalogToolRegistry._scan; use the enclosing contract and type below. | Return type of extract_tool_schema; see its callable contract | Enclosing invocation or class/instance lifetime | 162 |
| CatalogToolRegistry.skip_reasons | self | Owning instance; its attributes retain state for the instance lifetime. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 178 |
| CatalogToolRegistry.skip_reasons | root | Explicit root directory against which named paths are resolved. | Return type of Path; see its callable contract | Enclosing invocation or class/instance lifetime | 185 |
| CatalogToolRegistry.skip_reasons | entries | Local binding for entries in CatalogToolRegistry.skip_reasons; use the enclosing contract and type below. | Return type of list; see its callable contract | Enclosing invocation or class/instance lifetime | 189 |
| CatalogToolRegistry._skip_reason | self | Owning instance; its attributes retain state for the instance lifetime. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 199 |
| CatalogToolRegistry._skip_reason | name | Current identifier selected by parsing, lookup or dependency registration. | str | Enclosing invocation or class/instance lifetime | 199 |
| CatalogToolRegistry._skip_reason | extract_tool_schema | Imported dependency for extract tool schema in CatalogToolRegistry._skip_reason; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 206 |
| CatalogToolRegistry._skip_reason | store | Local binding for store in CatalogToolRegistry._skip_reason; use the enclosing contract and type below. | Return type of getattr; see its callable contract | Enclosing invocation or class/instance lifetime | 210 |
| CatalogToolRegistry._skip_reason | code_bytes | Local binding for code bytes in CatalogToolRegistry._skip_reason; use the enclosing contract and type below. | Return type of snapshot; see its callable contract | Enclosing invocation or class/instance lifetime | 215 |
| CatalogToolRegistry._skip_reason | tests_bytes | Local binding for tests bytes in CatalogToolRegistry._skip_reason; use the enclosing contract and type below. | Return type of snapshot; see its callable contract | Enclosing invocation or class/instance lifetime | 215 |
| CatalogToolRegistry._skip_reason | code | Source snapshot passed through approval, syntax checks and isolated staging. | Return type of snapshot; see its callable contract | Enclosing invocation or class/instance lifetime | 224 |
| CatalogToolRegistry._skip_reason | _tests | Local binding for tests in CatalogToolRegistry._skip_reason; use the enclosing contract and type below. | Return type of snapshot; see its callable contract | Enclosing invocation or class/instance lifetime | 224 |
| CatalogToolRegistry._skip_reason | context | Local binding for context in CatalogToolRegistry._skip_reason; use the enclosing contract and type below. | Return type of acceptance_context; see its callable contract | Enclosing invocation or class/instance lifetime | 225 |
| CatalogToolRegistry._skip_reason | rejected | Local binding for rejected in CatalogToolRegistry._skip_reason; use the enclosing contract and type below. | Return type of join; see its callable contract | Enclosing invocation or class/instance lifetime | 229 |
| CatalogToolRegistry._skip_reason | detail | Local binding for detail in CatalogToolRegistry._skip_reason; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 230 |
| CatalogToolRegistry._skip_reason | covered | Local binding for covered in CatalogToolRegistry._skip_reason; use the enclosing contract and type below. | set | Enclosing invocation or class/instance lifetime | 242 |
| CatalogToolRegistry._skip_reason.comprehension_242 | signature | Comprehension item for signature in CatalogToolRegistry._skip_reason.comprehension_242; use the enclosing contract and type below. | Element of the declared iterable | This comprehension only; does not leak into its enclosing scope | 242 |
| CatalogToolRegistry.recheck | self | Owning instance; its attributes retain state for the instance lifetime. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 247 |
| CatalogToolRegistry.recheck | expected | Reviewed expected observation kept outside untrusted child execution. | Mapping[str, ApprovedTool] | Enclosing invocation or class/instance lifetime | 247 |
| CatalogToolRegistry.recheck | current | Local binding for current in CatalogToolRegistry.recheck; use the enclosing contract and type below. | Return type of resolve; see its callable contract | Enclosing invocation or class/instance lifetime | 249 |
| CatalogToolRegistry.recheck.comprehension_250 | name | Current identifier selected by parsing, lookup or dependency registration. | Element of the declared iterable | This comprehension only; does not leak into its enclosing scope | 250 |
| CatalogToolRegistry.recheck.comprehension_250 | tool | Comprehension item for tool in CatalogToolRegistry.recheck.comprehension_250; use the enclosing contract and type below. | Element of the declared iterable | This comprehension only; does not leak into its enclosing scope | 250 |
