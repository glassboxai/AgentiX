# Reference for src/agentix/application/general_pipeline.py

Catalog-driven model planning and widgets, with maintained native composition.

Source fingerprint: 7da1d76b0275148a93b2e8323474ccd25791ff8f2ee496f82fe83b1cf02e22f8

This reference is generated from maintained source without imports or execution. Assigned values are intentionally omitted. Runtime-dependent types are explicit; the enclosing docstring defines the behavioral contract. See [architecture](../ARCHITECTURE_QUALITY.md) for manually reviewed responsibility and dependency decisions.

## Classes and callables

### generate

Propose a workflow and exact widget files, without approving or importing code.

Kind: callable. Declared return: 'Candidate'. Source line: 20.

### generate.check

Recheck reusable widget bytes before approval/publication.

Kind: callable. Declared return: Not declared / class. Source line: 173.

### generate.commit

Publish each exact widget once after native/browser success.

Kind: callable. Declared return: Not declared / class. Source line: 179.

## Variables and parameters

| Scope | Name | Role and meaning | Type | Lifetime | Writes |
| --- | --- | --- | --- | --- | --- |
| module | hashlib | Imported dependency for hashlib in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 3 |
| module | json | Imported dependency for json in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 4 |
| module | logging | Imported dependency for logging in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 5 |
| module | TYPE_CHECKING | Imported dependency for TYPE CHECKING in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 6 |
| module | uuid4 | Imported dependency for uuid4 in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 7 |
| module | CatalogWidgetDesigner | Imported dependency for CatalogWidgetDesigner in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 9 |
| module | LOCK_PATH | Imported dependency for LOCK PATH in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 10 |
| module | application_digest | Imported dependency for application digest in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 10 |
| module | ApprovedTool | Imported dependency for ApprovedTool in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 11 |
| module | default_widget_css | Imported dependency for default widget css in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 12 |
| module | ApplicationPipeline | Imported dependency for ApplicationPipeline in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 15 |
| module | Candidate | Imported dependency for Candidate in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 15 |
| module | logger | Module logger emitting bounded operation diagnostics rather than artifact bodies. | Return type of getLogger; see its callable contract | Module/process lifetime | 17 |
| generate | pipeline | Parameter for pipeline in generate; use the enclosing contract and type below. | 'ApplicationPipeline' | Enclosing invocation or class/instance lifetime | 21 |
| generate | query | Original user request or a trusted test query; avoid payload logging by default. | str | Enclosing invocation or class/instance lifetime | 22 |
| generate | tools | Parameter for tools in generate; use the enclosing contract and type below. | dict[str, ApprovedTool] | Enclosing invocation or class/instance lifetime | 23, 39 |
| generate | feedback | Parameter for feedback in generate; use the enclosing contract and type below. | dict &#124; None | Enclosing invocation or class/instance lifetime | 24 |
| generate | Candidate | Imported dependency for Candidate in generate; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 27 |
| generate | identity | Explicit owner identity used by a session factory or fixture. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 29 |
| generate | folder | Local binding for folder in generate; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 30 |
| generate | coordinator | Local binding for coordinator in generate; use the enclosing contract and type below. | Return type of coordinator_factory; see its callable contract | Enclosing invocation or class/instance lifetime | 34 |
| generate | schemas | Local binding for schemas in generate; use the enclosing contract and type below. | dict | Enclosing invocation or class/instance lifetime | 35, 40 |
| generate.comprehension_35 | name | Current identifier selected by parsing, lookup or dependency registration. | Element of the declared iterable | This comprehension only; does not leak into its enclosing scope | 35 |
| generate.comprehension_35 | tool | Comprehension item for tool in generate.comprehension_35; use the enclosing contract and type below. | Element of the declared iterable | This comprehension only; does not leak into its enclosing scope | 35 |
| generate | assembly | Local binding for assembly in generate; use the enclosing contract and type below. | Return type of plan; see its callable contract | Enclosing invocation or class/instance lifetime | 36 |
| generate | selected | Local binding for selected in generate; use the enclosing contract and type below. | set | Enclosing invocation or class/instance lifetime | 38 |
| generate.comprehension_38 | widget | Comprehension item for widget in generate.comprehension_38; use the enclosing contract and type below. | Element of the declared iterable | This comprehension only; does not leak into its enclosing scope | 38 |
| generate.comprehension_39 | name | Current identifier selected by parsing, lookup or dependency registration. | Element of the declared iterable | This comprehension only; does not leak into its enclosing scope | 39 |
| generate.comprehension_39 | tool | Comprehension item for tool in generate.comprehension_39; use the enclosing contract and type below. | Element of the declared iterable | This comprehension only; does not leak into its enclosing scope | 39 |
| generate.comprehension_40 | name | Current identifier selected by parsing, lookup or dependency registration. | Element of the declared iterable | This comprehension only; does not leak into its enclosing scope | 40 |
| generate | package | Local binding for package in generate; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 41 |
| generate | CODE_SHARED | Imported dependency for CODE SHARED in generate; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 43 |
| generate | code_template | Imported dependency for code template in generate; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 44 |
| generate | connection_code | Local binding for connection code in generate; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 46 |
| generate | inputs | Local binding for inputs in generate; use the enclosing contract and type below. | tuple | Enclosing invocation or class/instance lifetime | 47 |
| generate | widgets | Local binding for widgets in generate; use the enclosing contract and type below. | tuple | Enclosing invocation or class/instance lifetime | 47 |
| generate | name | Current identifier selected by parsing, lookup or dependency registration. | Element of the declared iterable | Enclosing invocation or class/instance lifetime | 49, 52, 76 |
| generate | proposals | Local binding for proposals in generate; use the enclosing contract and type below. | tuple | Enclosing invocation or class/instance lifetime | 51 |
| generate | previous | Local binding for previous in generate; use the enclosing contract and type below. | tuple | Enclosing invocation or class/instance lifetime | 51 |
| generate | reuse | Local binding for reuse in generate; use the enclosing contract and type below. | tuple | Enclosing invocation or class/instance lifetime | 51 |
| generate | pending | Defensive pending-approval snapshot; never a capability to approve another owner. | tuple | Enclosing invocation or class/instance lifetime | 51 |
| generate | tool | Loop item for tool in generate; use the enclosing contract and type below. | Element of the declared iterable | Enclosing invocation or class/instance lifetime | 52, 76 |
| generate | stored | Local binding for stored in generate; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 53, 77 |
| generate | proposal | Local binding for proposal in generate; use the enclosing contract and type below. | Return type of dict; see its callable contract | Enclosing invocation or class/instance lifetime | 56, 77 |
| generate | generated | Local binding for generated in generate; use the enclosing contract and type below. | Return type of widgets; see its callable contract | Enclosing invocation or class/instance lifetime | 66 |
| generate | files | Local binding for files in generate; use the enclosing contract and type below. | dict | Enclosing invocation or class/instance lifetime | 90 |
| generate.comprehension_90 | path | Path under validation or an explicitly scoped maintained source path. | Element of the declared iterable | This comprehension only; does not leak into its enclosing scope | 90 |
| generate | manifest | Versioned inventory or launch record; not an execution-authorization capability. | dict | Enclosing invocation or class/instance lifetime | 91 |
| generate | propose_cases | Imported dependency for propose cases in generate; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 110 |
| generate | suggested | Local binding for suggested in generate; use the enclosing contract and type below. | Return type of propose_cases; see its callable contract | Enclosing invocation or class/instance lifetime | 112 |
| generate | acceptance | Local binding for acceptance in generate; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 113 |
| generate | payload | Local binding for payload in generate; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 113 |
| generate | expected | Reviewed expected observation kept outside untrusted child execution. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 113 |
| generate.comprehension_113 | key | Comprehension item for key in generate.comprehension_113; use the enclosing contract and type below. | Element of the declared iterable | This comprehension only; does not leak into its enclosing scope | 113 |
| generate | dependencies | Local binding for dependencies in generate; use the enclosing contract and type below. | dict | Enclosing invocation or class/instance lifetime | 127 |
| generate.comprehension_127 | name | Current identifier selected by parsing, lookup or dependency registration. | Element of the declared iterable | This comprehension only; does not leak into its enclosing scope | 136 |
| generate.comprehension_127 | tool | Comprehension item for tool in generate.comprehension_127; use the enclosing contract and type below. | Element of the declared iterable | This comprehension only; does not leak into its enclosing scope | 136 |
| generate | review | Local binding for review in generate; use the enclosing contract and type below. | dict | Enclosing invocation or class/instance lifetime | 138 |
| generate.comprehension_141 | name | Current identifier selected by parsing, lookup or dependency registration. | Element of the declared iterable | This comprehension only; does not leak into its enclosing scope | 149 |
| generate.comprehension_151 | name | Current identifier selected by parsing, lookup or dependency registration. | Element of the declared iterable | This comprehension only; does not leak into its enclosing scope | 151 |
| generate.comprehension_153 | name | Current identifier selected by parsing, lookup or dependency registration. | Element of the declared iterable | This comprehension only; does not leak into its enclosing scope | 153 |
| generate.comprehension_153 | tool | Comprehension item for tool in generate.comprehension_153; use the enclosing contract and type below. | Element of the declared iterable | This comprehension only; does not leak into its enclosing scope | 153 |
| generate.comprehension_155 | name | Current identifier selected by parsing, lookup or dependency registration. | Element of the declared iterable | This comprehension only; does not leak into its enclosing scope | 155 |
| generate.comprehension_155 | tool | Comprehension item for tool in generate.comprehension_155; use the enclosing contract and type below. | Element of the declared iterable | This comprehension only; does not leak into its enclosing scope | 155 |
| generate.comprehension_159 | key | Comprehension item for key in generate.comprehension_159; use the enclosing contract and type below. | Element of the declared iterable | This comprehension only; does not leak into its enclosing scope | 159 |
| generate | digest | Content fingerprint for change detection; not a substitute for human approval. | Return type of application_digest; see its callable contract | Enclosing invocation or class/instance lifetime | 165 |
| generate | candidate | Local binding for candidate in generate; use the enclosing contract and type below. | Return type of Candidate; see its callable contract | Enclosing invocation or class/instance lifetime | 169 |
| generate.check | name | Current identifier selected by parsing, lookup or dependency registration. | Element of the declared iterable | Enclosing invocation or class/instance lifetime | 175 |
| generate.check | tool | Loop item for tool in generate.check; use the enclosing contract and type below. | Element of the declared iterable | Enclosing invocation or class/instance lifetime | 175 |
| generate.commit | item | Parameter for item in generate.commit; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 179 |
| generate.commit | current | Local binding for current in generate.commit; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 182 |
| generate.commit | name | Current identifier selected by parsing, lookup or dependency registration. | Element of the declared iterable | Enclosing invocation or class/instance lifetime | 183 |
| generate.commit | tool | Loop item for tool in generate.commit; use the enclosing contract and type below. | Element of the declared iterable | Enclosing invocation or class/instance lifetime | 183 |
| generate.commit | proposal | Local binding for proposal in generate.commit; use the enclosing contract and type below. | Return type of dict; see its callable contract | Enclosing invocation or class/instance lifetime | 184 |
| generate.commit | css | Local binding for css in generate.commit; use the enclosing contract and type below. | Return type of decode; see its callable contract | Enclosing invocation or class/instance lifetime | 188 |
| generate.commit | published | Local binding for published in generate.commit; use the enclosing contract and type below. | Return type of load; see its callable contract | Enclosing invocation or class/instance lifetime | 196 |
| generate | candidate.dependency_check | Attribute for candidate.dependency check in generate; use the enclosing contract and type below. | tuple | Enclosing invocation or class/instance lifetime | 206 |
| generate | candidate.widget_commit | Attribute for candidate.widget commit in generate; use the enclosing contract and type below. | tuple | Enclosing invocation or class/instance lifetime | 206 |
