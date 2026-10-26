# Reference for tools/build_reference.py

Build and verify English reference documents without importing application code.

Only named root entrypoints and Python files inside src, tools and tests are read.
Existing generated_tools and dependencies are never traversed. References contain
names, contracts and scope/type information, never assigned values or secrets.

Source fingerprint: 7b2a605e78c509e6eec1074e7933c394291c3900f49615054255d65fbed8f792

This reference is generated from maintained source without imports or execution. Assigned values are intentionally omitted. Runtime-dependent types are explicit; the enclosing docstring defines the behavioral contract. See [architecture](../ARCHITECTURE_QUALITY.md) for manually reviewed responsibility and dependency decisions.

## Classes and callables

### maintained_sources

Enumerate only maintained directories, skipping bytecode and linked paths.

Kind: callable. Declared return: list[Path]. Source line: 70.

### expression_type

Describe static expression shape without exposing assigned literal values.

Kind: callable. Declared return: str. Source line: 84.

### SourceInventory

Collect declarations and scoped bindings without evaluating annotations.

Kind: class. Declared return: Not declared / class. Source line: 103.

### SourceInventory.__init__

Create independent state for one maintained Python module.

Kind: callable. Declared return: None. Source line: 106.

### SourceInventory.binding

Record a named binding's type, role and source location without its value.

Kind: callable. Declared return: None. Source line: 112.

### SourceInventory.target

Flatten tuple bindings and retain explicit attribute ownership.

Kind: callable. Declared return: None. Source line: 144.

### SourceInventory.visit_ClassDef

Capture a class contract and then collect its owned declarations.

Kind: callable. Declared return: None. Source line: 154.

### SourceInventory.visit_FunctionDef

Capture callable contracts, parameters, locals and nested definitions.

Kind: callable. Declared return: None. Source line: 158.

### SourceInventory.definition

Describe a declaration before entering its lexical scope.

Kind: callable. Declared return: None. Source line: 164.

### SourceInventory.visit_Assign

Capture assigned names and statically observable type categories.

Kind: callable. Declared return: None. Source line: 194.

### SourceInventory.visit_AnnAssign

Preserve declared types without resolving generated expressions.

Kind: callable. Declared return: None. Source line: 205.

### SourceInventory.visit_AugAssign

Record updates to existing variables as additional write locations.

Kind: callable. Declared return: None. Source line: 210.

### SourceInventory.visit_For

Document each loop target within the enclosing callable.

Kind: callable. Declared return: None. Source line: 215.

### SourceInventory.visit_comprehension

Document comprehension-local names without executing their iterators.

Kind: callable. Declared return: None. Source line: 222.

### SourceInventory.visit_ListComp

Separate comprehension bindings from the enclosing function's locals.

Kind: callable. Declared return: None. Source line: 229.

### SourceInventory.visit_Lambda

Document anonymous callback parameters under their own lexical scope.

Kind: callable. Declared return: None. Source line: 239.

### SourceInventory.visit_With

Capture context-manager resources and their lexical cleanup boundary.

Kind: callable. Declared return: None. Source line: 252.

### SourceInventory.visit_ExceptHandler

Document exception values without recording sensitive exception text.

Kind: callable. Declared return: None. Source line: 263.

### SourceInventory.visit_NamedExpr

Capture assignment-expression targets as normal scoped bindings.

Kind: callable. Declared return: None. Source line: 274.

### SourceInventory.visit_Import

Describe imported names as explicit module dependencies.

Kind: callable. Declared return: None. Source line: 279.

### scan_source

Return one deterministic source-bound inventory, including its module contract.

Kind: callable. Declared return: dict[str, Any]. Source line: 292.

### escape

Keep table delimiters and line breaks from changing reference structure.

Kind: callable. Declared return: str. Source line: 307.

### module_document

Explain module/callable contracts and every inventoried scoped binding.

Kind: callable. Declared return: str. Source line: 312.

### powershell_documents

Document fixed infrastructure ASTs without importing or executing their source.

The trusted inventory helper uses PowerShell's parser. Missing PowerShell or
malformed source fails this gate rather than silently dropping reference entries.

Kind: callable. Declared return: dict[str, str]. Source line: 361.

### expected_documents

Compute expected reference bytes from the complete maintained source inventory.

Kind: callable. Declared return: dict[str, str]. Source line: 415.

### build_documents

Write references or return stale/missing entries without mutating files.

Freshness is exact, including contracts and source fingerprints. Passing the
check establishes inventory consistency, not semantic correctness; meaningful
manual documentation review remains required by AGENTS.md.

Kind: callable. Declared return: list[str]. Source line: 440.

### main

Run the reference generation/freshness gate for this checkout only.

Kind: callable. Declared return: None. Source line: 463.

## Variables and parameters

| Scope | Name | Role and meaning | Type | Lifetime | Writes |
| --- | --- | --- | --- | --- | --- |
| module | argparse | Imported dependency for argparse in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 8 |
| module | ast | Imported dependency for ast in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 9 |
| module | hashlib | Imported dependency for hashlib in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 10 |
| module | json | Imported dependency for json in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 11 |
| module | shutil | Imported dependency for shutil in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 12 |
| module | subprocess | Imported dependency for subprocess in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 13 |
| module | Path | Imported dependency for Path in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 14 |
| module | Any | Imported dependency for Any in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 15 |
| module | ROOT_ENTRIES | Module binding for ROOT ENTRIES in module; use the enclosing contract and type below. | tuple | Module/process lifetime | 17 |
| module | MEANINGS | Module binding for MEANINGS in module; use the enclosing contract and type below. | dict | Module/process lifetime | 25 |
| maintained_sources | root | Explicit root directory against which named paths are resolved. | Path | Enclosing invocation or class/instance lifetime | 70 |
| maintained_sources | result | Intermediate or returned outcome; consult the callable contract for trust/validation. | list | Enclosing invocation or class/instance lifetime | 72 |
| maintained_sources.comprehension_72 | name | Current identifier selected by parsing, lookup or dependency registration. | Element of the declared iterable | This comprehension only; does not leak into its enclosing scope | 72 |
| maintained_sources | folder | Loop item for folder in maintained_sources; use the enclosing contract and type below. | Element of the declared iterable | Enclosing invocation or class/instance lifetime | 73 |
| maintained_sources | base | Local binding for base in maintained_sources; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 74 |
| maintained_sources.comprehension_76 | path | Path under validation or an explicitly scoped maintained source path. | Element of the declared iterable | This comprehension only; does not leak into its enclosing scope | 78 |
| expression_type | node | Parameter for node in expression_type; use the enclosing contract and type below. | ast.AST &#124; None | Enclosing invocation or class/instance lifetime | 84 |
| expression_type | target | Local binding for target in expression_type; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 97 |
| expression_type | label | Local binding for label in expression_type; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 98 |
| SourceInventory.__init__ | self | Owning instance; its attributes retain state for the instance lifetime. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 106 |
| SourceInventory.__init__ | self.scope | Attribute for scope in SourceInventory.__init__; use the enclosing contract and type below. | list[str] | Enclosing invocation or class/instance lifetime | 108 |
| SourceInventory.__init__ | self.symbols | Attribute for symbols in SourceInventory.__init__; use the enclosing contract and type below. | list[dict[str, Any]] | Enclosing invocation or class/instance lifetime | 109 |
| SourceInventory.__init__ | self.variables | Attribute for variables in SourceInventory.__init__; use the enclosing contract and type below. | dict[tuple[str, str], dict[str, Any]] | Enclosing invocation or class/instance lifetime | 110 |
| SourceInventory.binding | self | Owning instance; its attributes retain state for the instance lifetime. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 112 |
| SourceInventory.binding | name | Current identifier selected by parsing, lookup or dependency registration. | str | Enclosing invocation or class/instance lifetime | 112 |
| SourceInventory.binding | node | Parameter for node in SourceInventory.binding; use the enclosing contract and type below. | ast.AST | Enclosing invocation or class/instance lifetime | 112 |
| SourceInventory.binding | kind | Parameter for kind in SourceInventory.binding; use the enclosing contract and type below. | str | Enclosing invocation or class/instance lifetime | 112 |
| SourceInventory.binding | declared | Parameter for declared in SourceInventory.binding; use the enclosing contract and type below. | str | Enclosing invocation or class/instance lifetime | 112 |
| SourceInventory.binding | scope | Local binding for scope in SourceInventory.binding; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 114 |
| SourceInventory.binding | lifecycle | Local binding for lifecycle in SourceInventory.binding; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 115, 121, 123, 125 |
| SourceInventory.binding | meaning | Local binding for meaning in SourceInventory.binding; use the enclosing contract and type below. | Return type of get; see its callable contract | Enclosing invocation or class/instance lifetime | 126, 129 |
| SourceInventory.binding | words | Local binding for words in SourceInventory.binding; use the enclosing contract and type below. | Return type of replace; see its callable contract | Enclosing invocation or class/instance lifetime | 128 |
| SourceInventory.binding | key | Local binding for key in SourceInventory.binding; use the enclosing contract and type below. | tuple | Enclosing invocation or class/instance lifetime | 130 |
| SourceInventory.target | self | Owning instance; its attributes retain state for the instance lifetime. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 144 |
| SourceInventory.target | target | Parameter for target in SourceInventory.target; use the enclosing contract and type below. | ast.AST | Enclosing invocation or class/instance lifetime | 144 |
| SourceInventory.target | node | Parameter for node in SourceInventory.target; use the enclosing contract and type below. | ast.AST | Enclosing invocation or class/instance lifetime | 144 |
| SourceInventory.target | kind | Parameter for kind in SourceInventory.target; use the enclosing contract and type below. | str | Enclosing invocation or class/instance lifetime | 144 |
| SourceInventory.target | declared | Parameter for declared in SourceInventory.target; use the enclosing contract and type below. | str | Enclosing invocation or class/instance lifetime | 144 |
| SourceInventory.target | item | Loop item for item in SourceInventory.target; use the enclosing contract and type below. | Element of the declared iterable | Enclosing invocation or class/instance lifetime | 151 |
| SourceInventory.visit_ClassDef | self | Owning instance; its attributes retain state for the instance lifetime. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 154 |
| SourceInventory.visit_ClassDef | node | Parameter for node in SourceInventory.visit_ClassDef; use the enclosing contract and type below. | ast.ClassDef | Enclosing invocation or class/instance lifetime | 154 |
| SourceInventory.visit_FunctionDef | self | Owning instance; its attributes retain state for the instance lifetime. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 158 |
| SourceInventory.visit_FunctionDef | node | Parameter for node in SourceInventory.visit_FunctionDef; use the enclosing contract and type below. | ast.FunctionDef &#124; ast.AsyncFunctionDef | Enclosing invocation or class/instance lifetime | 158 |
| SourceInventory | visit_AsyncFunctionDef | Local binding for visit AsyncFunctionDef in SourceInventory; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 162 |
| SourceInventory.definition | self | Owning instance; its attributes retain state for the instance lifetime. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 164 |
| SourceInventory.definition | node | Parameter for node in SourceInventory.definition; use the enclosing contract and type below. | Any | Enclosing invocation or class/instance lifetime | 164 |
| SourceInventory.definition | kind | Parameter for kind in SourceInventory.definition; use the enclosing contract and type below. | str | Enclosing invocation or class/instance lifetime | 164 |
| SourceInventory.definition | qualified | Local binding for qualified in SourceInventory.definition; use the enclosing contract and type below. | Return type of join; see its callable contract | Enclosing invocation or class/instance lifetime | 166 |
| SourceInventory.definition | args | Local binding for args in SourceInventory.definition; use the enclosing contract and type below. | list | Enclosing invocation or class/instance lifetime | 180 |
| SourceInventory.definition.comprehension_181 | arg | Comprehension item for arg in SourceInventory.definition.comprehension_181; use the enclosing contract and type below. | Element of the declared iterable | This comprehension only; does not leak into its enclosing scope | 181 |
| SourceInventory.definition | argument | Loop item for argument in SourceInventory.definition; use the enclosing contract and type below. | Element of the declared iterable | Enclosing invocation or class/instance lifetime | 182 |
| SourceInventory.visit_Assign | self | Owning instance; its attributes retain state for the instance lifetime. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 194 |
| SourceInventory.visit_Assign | node | Parameter for node in SourceInventory.visit_Assign; use the enclosing contract and type below. | ast.Assign | Enclosing invocation or class/instance lifetime | 194 |
| SourceInventory.visit_Assign | target | Loop item for target in SourceInventory.visit_Assign; use the enclosing contract and type below. | Element of the declared iterable | Enclosing invocation or class/instance lifetime | 196 |
| SourceInventory.visit_AnnAssign | self | Owning instance; its attributes retain state for the instance lifetime. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 205 |
| SourceInventory.visit_AnnAssign | node | Parameter for node in SourceInventory.visit_AnnAssign; use the enclosing contract and type below. | ast.AnnAssign | Enclosing invocation or class/instance lifetime | 205 |
| SourceInventory.visit_AugAssign | self | Owning instance; its attributes retain state for the instance lifetime. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 210 |
| SourceInventory.visit_AugAssign | node | Parameter for node in SourceInventory.visit_AugAssign; use the enclosing contract and type below. | ast.AugAssign | Enclosing invocation or class/instance lifetime | 210 |
| SourceInventory.visit_For | self | Owning instance; its attributes retain state for the instance lifetime. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 215 |
| SourceInventory.visit_For | node | Parameter for node in SourceInventory.visit_For; use the enclosing contract and type below. | ast.For &#124; ast.AsyncFor | Enclosing invocation or class/instance lifetime | 215 |
| SourceInventory | visit_AsyncFor | Local binding for visit AsyncFor in SourceInventory; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 220 |
| SourceInventory.visit_comprehension | self | Owning instance; its attributes retain state for the instance lifetime. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 222 |
| SourceInventory.visit_comprehension | node | Parameter for node in SourceInventory.visit_comprehension; use the enclosing contract and type below. | ast.comprehension | Enclosing invocation or class/instance lifetime | 222 |
| SourceInventory.visit_ListComp | self | Owning instance; its attributes retain state for the instance lifetime. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 229 |
| SourceInventory.visit_ListComp | node | Parameter for node in SourceInventory.visit_ListComp; use the enclosing contract and type below. | Any | Enclosing invocation or class/instance lifetime | 229 |
| SourceInventory | visit_SetComp | Local binding for visit SetComp in SourceInventory; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 235 |
| SourceInventory | visit_DictComp | Local binding for visit DictComp in SourceInventory; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 236 |
| SourceInventory | visit_GeneratorExp | Local binding for visit GeneratorExp in SourceInventory; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 237 |
| SourceInventory.visit_Lambda | self | Owning instance; its attributes retain state for the instance lifetime. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 239 |
| SourceInventory.visit_Lambda | node | Parameter for node in SourceInventory.visit_Lambda; use the enclosing contract and type below. | ast.Lambda | Enclosing invocation or class/instance lifetime | 239 |
| SourceInventory.visit_Lambda | argument | Loop item for argument in SourceInventory.visit_Lambda; use the enclosing contract and type below. | Element of the declared iterable | Enclosing invocation or class/instance lifetime | 242 |
| SourceInventory.visit_With | self | Owning instance; its attributes retain state for the instance lifetime. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 252 |
| SourceInventory.visit_With | node | Parameter for node in SourceInventory.visit_With; use the enclosing contract and type below. | ast.With &#124; ast.AsyncWith | Enclosing invocation or class/instance lifetime | 252 |
| SourceInventory.visit_With | item | Loop item for item in SourceInventory.visit_With; use the enclosing contract and type below. | Element of the declared iterable | Enclosing invocation or class/instance lifetime | 254 |
| SourceInventory | visit_AsyncWith | Local binding for visit AsyncWith in SourceInventory; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 261 |
| SourceInventory.visit_ExceptHandler | self | Owning instance; its attributes retain state for the instance lifetime. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 263 |
| SourceInventory.visit_ExceptHandler | node | Parameter for node in SourceInventory.visit_ExceptHandler; use the enclosing contract and type below. | ast.ExceptHandler | Enclosing invocation or class/instance lifetime | 263 |
| SourceInventory.visit_NamedExpr | self | Owning instance; its attributes retain state for the instance lifetime. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 274 |
| SourceInventory.visit_NamedExpr | node | Parameter for node in SourceInventory.visit_NamedExpr; use the enclosing contract and type below. | ast.NamedExpr | Enclosing invocation or class/instance lifetime | 274 |
| SourceInventory.visit_Import | self | Owning instance; its attributes retain state for the instance lifetime. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 279 |
| SourceInventory.visit_Import | node | Parameter for node in SourceInventory.visit_Import; use the enclosing contract and type below. | ast.Import &#124; ast.ImportFrom | Enclosing invocation or class/instance lifetime | 279 |
| SourceInventory.visit_Import | alias | Loop item for alias in SourceInventory.visit_Import; use the enclosing contract and type below. | Element of the declared iterable | Enclosing invocation or class/instance lifetime | 281 |
| SourceInventory | visit_ImportFrom | Local binding for visit ImportFrom in SourceInventory; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 289 |
| scan_source | path | Path under validation or an explicitly scoped maintained source path. | Path | Enclosing invocation or class/instance lifetime | 292 |
| scan_source | name | Current identifier selected by parsing, lookup or dependency registration. | str | Enclosing invocation or class/instance lifetime | 292 |
| scan_source | source | Explicit source document or source-code text; never imported for reference generation. | Return type of read_bytes; see its callable contract | Enclosing invocation or class/instance lifetime | 294 |
| scan_source | tree | Local binding for tree in scan_source; use the enclosing contract and type below. | Return type of parse; see its callable contract | Enclosing invocation or class/instance lifetime | 295 |
| scan_source | visitor | Local binding for visitor in scan_source; use the enclosing contract and type below. | Return type of SourceInventory; see its callable contract | Enclosing invocation or class/instance lifetime | 296 |
| escape | text | Parameter for text in escape; use the enclosing contract and type below. | str | Enclosing invocation or class/instance lifetime | 307 |
| module_document | item | Parameter for item in module_document; use the enclosing contract and type below. | dict[str, Any] | Enclosing invocation or class/instance lifetime | 312 |
| module_document | parts | Local binding for parts in module_document; use the enclosing contract and type below. | list | Enclosing invocation or class/instance lifetime | 314 |
| module_document | symbol | Loop item for symbol in module_document; use the enclosing contract and type below. | Element of the declared iterable | Enclosing invocation or class/instance lifetime | 329 |
| module_document | variable | Loop item for variable in module_document; use the enclosing contract and type below. | Element of the declared iterable | Enclosing invocation or class/instance lifetime | 348 |
| module_document | cells | Local binding for cells in module_document; use the enclosing contract and type below. | list | Enclosing invocation or class/instance lifetime | 349 |
| module_document.comprehension_357 | cell | Comprehension item for cell in module_document.comprehension_357; use the enclosing contract and type below. | Element of the declared iterable | This comprehension only; does not leak into its enclosing scope | 357 |
| powershell_documents | root | Explicit root directory against which named paths are resolved. | Path | Enclosing invocation or class/instance lifetime | 361 |
| powershell_documents | helper | Local binding for helper in powershell_documents; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 367 |
| powershell_documents | executable | Local binding for executable in powershell_documents; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 370 |
| powershell_documents | result | Intermediate or returned outcome; consult the callable contract for trust/validation. | Return type of run; see its callable contract | Enclosing invocation or class/instance lifetime | 373 |
| powershell_documents | documents | Local binding for documents in powershell_documents; use the enclosing contract and type below. | dict | Enclosing invocation or class/instance lifetime | 381 |
| powershell_documents | item | Loop item for item in powershell_documents; use the enclosing contract and type below. | Element of the declared iterable | Enclosing invocation or class/instance lifetime | 382 |
| powershell_documents | name | Current identifier selected by parsing, lookup or dependency registration. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 383 |
| powershell_documents | fingerprint | Local binding for fingerprint in powershell_documents; use the enclosing contract and type below. | Return type of hexdigest; see its callable contract | Enclosing invocation or class/instance lifetime | 384 |
| powershell_documents | lines | Local binding for lines in powershell_documents; use the enclosing contract and type below. | list | Enclosing invocation or class/instance lifetime | 385 |
| powershell_documents | function | Loop item for function in powershell_documents; use the enclosing contract and type below. | Element of the declared iterable | Enclosing invocation or class/instance lifetime | 395 |
| powershell_documents | variable | Loop item for variable in powershell_documents; use the enclosing contract and type below. | Element of the declared iterable | Enclosing invocation or class/instance lifetime | 407 |
| expected_documents | root | Explicit root directory against which named paths are resolved. | Path | Enclosing invocation or class/instance lifetime | 415 |
| expected_documents | documents | Local binding for documents in expected_documents; use the enclosing contract and type below. | dict | Enclosing invocation or class/instance lifetime | 417 |
| expected_documents | index | Local binding for index in expected_documents; use the enclosing contract and type below. | list | Enclosing invocation or class/instance lifetime | 418 |
| expected_documents | path | Path under validation or an explicitly scoped maintained source path. | Element of the declared iterable | Enclosing invocation or class/instance lifetime | 427 |
| expected_documents | name | Current identifier selected by parsing, lookup or dependency registration. | Return type of as_posix; see its callable contract | Enclosing invocation or class/instance lifetime | 428 |
| expected_documents | item | Local binding for item in expected_documents; use the enclosing contract and type below. | Return type of scan_source; see its callable contract | Enclosing invocation or class/instance lifetime | 429 |
| expected_documents | target | Local binding for target in expected_documents; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 430 |
| expected_documents | infrastructure | Local binding for infrastructure in expected_documents; use the enclosing contract and type below. | Return type of powershell_documents; see its callable contract | Enclosing invocation or class/instance lifetime | 433 |
| expected_documents.comprehension_435 | name | Current identifier selected by parsing, lookup or dependency registration. | Element of the declared iterable | This comprehension only; does not leak into its enclosing scope | 435 |
| build_documents | root | Explicit root directory against which named paths are resolved. | Path | Enclosing invocation or class/instance lifetime | 440 |
| build_documents | check | Parameter for check in build_documents; use the enclosing contract and type below. | bool | Enclosing invocation or class/instance lifetime | 440 |
| build_documents | destination | Local binding for destination in build_documents; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 447 |
| build_documents | expected | Reviewed expected observation kept outside untrusted child execution. | Return type of expected_documents; see its callable contract | Enclosing invocation or class/instance lifetime | 448 |
| build_documents | issues | Local binding for issues in build_documents; use the enclosing contract and type below. | list | Enclosing invocation or class/instance lifetime | 449 |
| build_documents | name | Current identifier selected by parsing, lookup or dependency registration. | Element of the declared iterable | Enclosing invocation or class/instance lifetime | 450 |
| build_documents | content | Artifact or review text whose encoding, size and approval state must be checked. | Element of the declared iterable | Enclosing invocation or class/instance lifetime | 450 |
| build_documents | target | Local binding for target in build_documents; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 451 |
| build_documents.comprehension_459 | path | Path under validation or an explicitly scoped maintained source path. | Element of the declared iterable | This comprehension only; does not leak into its enclosing scope | 459 |
| main | parser | Local binding for parser in main; use the enclosing contract and type below. | Return type of ArgumentParser; see its callable contract | Enclosing invocation or class/instance lifetime | 465 |
| main | args | Local binding for args in main; use the enclosing contract and type below. | Return type of parse_args; see its callable contract | Enclosing invocation or class/instance lifetime | 467 |
| main | root | Explicit root directory against which named paths are resolved. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 468 |
| main | issues | Local binding for issues in main; use the enclosing contract and type below. | Return type of build_documents; see its callable contract | Enclosing invocation or class/instance lifetime | 469 |
