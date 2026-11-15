# Reference for src/agentix/storage/catalog.py

Read an AST catalog without importing or executing tool source.

Source fingerprint: 6d5a8d734afed034389a6378359bfe345028e1da6f0e8e06e8ee3bfe04fcf86a

This reference is generated from maintained source without imports or execution. Assigned values are intentionally omitted. Runtime-dependent types are explicit; the enclosing docstring defines the behavioral contract. See [architecture](../ARCHITECTURE_QUALITY.md) for manually reviewed responsibility and dependency decisions.

## Classes and callables

### ToolCatalog

Render the existing Markdown catalog for an explicit storage root.

Kind: class. Declared return: Not declared / class. Source line: 15.

### ToolCatalog.__init__

Remember the root; construction never reads its contents.

Kind: callable. Declared return: None. Source line: 18.

### ToolCatalog.contains

Check exact catalog membership without importing or enumerating source.

Path containment/links are independently enforced by the approval ledger.
Membership alone never establishes authorization or functional correctness.

Kind: callable. Declared return: bool. Source line: 22.

### ToolCatalog.render

Safely inspects generated_tools/ using Python AST (without executing code).
Extracts available tools, standalone functions, argument signatures, and docstrings.

Kind: callable. Declared return: str. Source line: 35.

### ToolCatalog.contracts

Read a bounded canonical metadata catalog without imports or test execution.

Kind: callable. Declared return: dict. Source line: 95.

## Variables and parameters

| Scope | Name | Role and meaning | Type | Lifetime | Writes |
| --- | --- | --- | --- | --- | --- |
| module | ast | Imported dependency for ast in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 3 |
| module | json | Imported dependency for json in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 4 |
| module | logging | Imported dependency for logging in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 5 |
| module | os | Imported dependency for os in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 6 |
| module | re | Imported dependency for re in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 7 |
| module | Path | Imported dependency for Path in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 8 |
| module | log_event | Imported dependency for log event in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 10 |
| module | logger | Module logger emitting bounded operation diagnostics rather than artifact bodies. | Return type of getLogger; see its callable contract | Module/process lifetime | 12 |
| ToolCatalog.__init__ | self | Owning instance; its attributes retain state for the instance lifetime. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 18 |
| ToolCatalog.__init__ | root | Explicit root directory against which named paths are resolved. | str &#124; Path | Enclosing invocation or class/instance lifetime | 18 |
| ToolCatalog.__init__ | self.root | Explicit root directory against which named paths are resolved. | Return type of str; see its callable contract | Enclosing invocation or class/instance lifetime | 20 |
| ToolCatalog.contains | self | Owning instance; its attributes retain state for the instance lifetime. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 22 |
| ToolCatalog.contains | tool_name | Validated public tool identifier within the configured storage boundary. | str | Enclosing invocation or class/instance lifetime | 22 |
| ToolCatalog.contains | folder | Local binding for folder in ToolCatalog.contains; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 32 |
| ToolCatalog.render | self | Owning instance; its attributes retain state for the instance lifetime. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 35 |
| ToolCatalog.render | catalog_entries | Local binding for catalog entries in ToolCatalog.render; use the enclosing contract and type below. | list | Enclosing invocation or class/instance lifetime | 44 |
| ToolCatalog.render | item | Loop item for item in ToolCatalog.render; use the enclosing contract and type below. | Element of the declared iterable | Enclosing invocation or class/instance lifetime | 46 |
| ToolCatalog.render | tool_dir | Local binding for tool dir in ToolCatalog.render; use the enclosing contract and type below. | Return type of join; see its callable contract | Enclosing invocation or class/instance lifetime | 47 |
| ToolCatalog.render | code_file | Local binding for code file in ToolCatalog.render; use the enclosing contract and type below. | Return type of join; see its callable contract | Enclosing invocation or class/instance lifetime | 48 |
| ToolCatalog.render | f | Managed resource for f in ToolCatalog.render; use the enclosing contract and type below. | Return type of open; see its callable contract | Context-manager block; exit invokes its cleanup protocol | 52 |
| ToolCatalog.render | tree | Local binding for tree in ToolCatalog.render; use the enclosing contract and type below. | Return type of parse; see its callable contract | Enclosing invocation or class/instance lifetime | 53 |
| ToolCatalog.render | functions_info | Local binding for functions info in ToolCatalog.render; use the enclosing contract and type below. | list | Enclosing invocation or class/instance lifetime | 55 |
| ToolCatalog.render | node | Loop item for node in ToolCatalog.render; use the enclosing contract and type below. | Element of the declared iterable | Enclosing invocation or class/instance lifetime | 56 |
| ToolCatalog.render | args_list | Local binding for args list in ToolCatalog.render; use the enclosing contract and type below. | list | Enclosing invocation or class/instance lifetime | 58 |
| ToolCatalog.render.comprehension_58 | arg | Comprehension item for arg in ToolCatalog.render.comprehension_58; use the enclosing contract and type below. | Element of the declared iterable | This comprehension only; does not leak into its enclosing scope | 58 |
| ToolCatalog.render | doc | Local binding for doc in ToolCatalog.render; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 59 |
| ToolCatalog.render | first_line_doc | Local binding for first line doc in ToolCatalog.render; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 60 |
| ToolCatalog.render | entry | Local binding for entry in ToolCatalog.render; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 67, 69, 78, 81 |
| ToolCatalog.render | extract_tool_schema | Imported dependency for extract tool schema in ToolCatalog.render; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 72 |
| ToolCatalog.render | contract | Validated declarative acceptance data bound to current artifact identities. | Return type of extract_tool_schema; see its callable contract | Enclosing invocation or class/instance lifetime | 74, 76 |
| ToolCatalog.render | e | Caught exception for e in ToolCatalog.render; use the enclosing contract and type below. | Exception | Current exception handler; Python clears this binding afterward | 88 |
| ToolCatalog.contracts | self | Owning instance; its attributes retain state for the instance lifetime. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 95 |
| ToolCatalog.contracts | extract_tool_schema | Imported dependency for extract tool schema in ToolCatalog.contracts; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 97 |
| ToolCatalog.contracts | root | Explicit root directory against which named paths are resolved. | Return type of Path; see its callable contract | Enclosing invocation or class/instance lifetime | 99 |
| ToolCatalog.contracts | entries | Local binding for entries in ToolCatalog.contracts; use the enclosing contract and type below. | Return type of list; see its callable contract | Enclosing invocation or class/instance lifetime | 102 |
| ToolCatalog.contracts | contracts | Local binding for contracts in ToolCatalog.contracts; use the enclosing contract and type below. | dict | Enclosing invocation or class/instance lifetime | 105 |
| ToolCatalog.contracts | folder | Loop item for folder in ToolCatalog.contracts; use the enclosing contract and type below. | Element of the declared iterable | Enclosing invocation or class/instance lifetime | 106 |
| ToolCatalog.contracts | source | Explicit source document or source-code text; never imported for reference generation. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 109 |
