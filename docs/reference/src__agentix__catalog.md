# Reference for src/agentix/catalog.py

Read an AST catalog without importing or executing tool source.

Source fingerprint: 8c3fb9e833128a74cf3aeba79bd1501c39f5f39b435b68c7a8f0d512cc80a9ff

This reference is generated from maintained source without imports or execution. Assigned values are intentionally omitted. Runtime-dependent types are explicit; the enclosing docstring defines the behavioral contract. See [architecture](../ARCHITECTURE_QUALITY.md) for manually reviewed responsibility and dependency decisions.

## Classes and callables

### ToolCatalog

Render the existing Markdown catalog for an explicit storage root.

Kind: class. Declared return: Not declared / class. Source line: 13.

### ToolCatalog.__init__

Remember the root; construction never reads its contents.

Kind: callable. Declared return: None. Source line: 16.

### ToolCatalog.render

Safely inspects generated_tools/ using Python AST (without executing code).
Extracts available tools, standalone functions, argument signatures, and docstrings.

Kind: callable. Declared return: str. Source line: 20.

## Variables and parameters

| Scope | Name | Role and meaning | Type | Lifetime | Writes |
| --- | --- | --- | --- | --- | --- |
| module | ast | Imported dependency for ast in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 3 |
| module | logging | Imported dependency for logging in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 4 |
| module | os | Imported dependency for os in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 5 |
| module | Path | Imported dependency for Path in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 6 |
| module | log_event | Imported dependency for log event in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 8 |
| module | logger | Module logger emitting bounded operation diagnostics rather than artifact bodies. | Return type of getLogger; see its callable contract | Module/process lifetime | 10 |
| ToolCatalog.__init__ | self | Owning instance; its attributes retain state for the instance lifetime. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 16 |
| ToolCatalog.__init__ | root | Explicit root directory against which named paths are resolved. | str &#124; Path | Enclosing invocation or class/instance lifetime | 16 |
| ToolCatalog.__init__ | self.root | Explicit root directory against which named paths are resolved. | Return type of str; see its callable contract | Enclosing invocation or class/instance lifetime | 18 |
| ToolCatalog.render | self | Owning instance; its attributes retain state for the instance lifetime. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 20 |
| ToolCatalog.render | catalog_entries | Local binding for catalog entries in ToolCatalog.render; use the enclosing contract and type below. | list | Enclosing invocation or class/instance lifetime | 29 |
| ToolCatalog.render | item | Loop item for item in ToolCatalog.render; use the enclosing contract and type below. | Element of the declared iterable | Enclosing invocation or class/instance lifetime | 31 |
| ToolCatalog.render | tool_dir | Local binding for tool dir in ToolCatalog.render; use the enclosing contract and type below. | Return type of join; see its callable contract | Enclosing invocation or class/instance lifetime | 32 |
| ToolCatalog.render | code_file | Local binding for code file in ToolCatalog.render; use the enclosing contract and type below. | Return type of join; see its callable contract | Enclosing invocation or class/instance lifetime | 33 |
| ToolCatalog.render | f | Managed resource for f in ToolCatalog.render; use the enclosing contract and type below. | Return type of open; see its callable contract | Context-manager block; exit invokes its cleanup protocol | 37 |
| ToolCatalog.render | tree | Local binding for tree in ToolCatalog.render; use the enclosing contract and type below. | Return type of parse; see its callable contract | Enclosing invocation or class/instance lifetime | 38 |
| ToolCatalog.render | functions_info | Local binding for functions info in ToolCatalog.render; use the enclosing contract and type below. | list | Enclosing invocation or class/instance lifetime | 40 |
| ToolCatalog.render | node | Loop item for node in ToolCatalog.render; use the enclosing contract and type below. | Element of the declared iterable | Enclosing invocation or class/instance lifetime | 41 |
| ToolCatalog.render | args_list | Local binding for args list in ToolCatalog.render; use the enclosing contract and type below. | list | Enclosing invocation or class/instance lifetime | 43 |
| ToolCatalog.render.comprehension_43 | arg | Comprehension item for arg in ToolCatalog.render.comprehension_43; use the enclosing contract and type below. | Element of the declared iterable | This comprehension only; does not leak into its enclosing scope | 43 |
| ToolCatalog.render | doc | Local binding for doc in ToolCatalog.render; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 44 |
| ToolCatalog.render | first_line_doc | Local binding for first line doc in ToolCatalog.render; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 45 |
| ToolCatalog.render | entry | Local binding for entry in ToolCatalog.render; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 52, 54, 56 |
| ToolCatalog.render | e | Caught exception for e in ToolCatalog.render; use the enclosing contract and type below. | Exception | Current exception handler; Python clears this binding afterward | 63 |
