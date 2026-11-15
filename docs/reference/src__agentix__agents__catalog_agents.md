# Reference for src/agentix/agents/catalog_agents.py

Catalog-derived application model roles; proposals never authorize execution.

These roles receive approved tool metadata and produce data/widget source for
explicit human review. They contain no reference widget implementation. Framework,
provider, filesystem, native execution and UI lifecycle concerns are injected or
owned by application services, not these roles.

Source fingerprint: 6be445e947002d7508b2564d6ed8db98d0aaf430ab25ccba972f7f6d03b41396

This reference is generated from maintained source without imports or execution. Assigned values are intentionally omitted. Runtime-dependent types are explicit; the enclosing docstring defines the behavioral contract. See [architecture](../ARCHITECTURE_QUALITY.md) for manually reviewed responsibility and dependency decisions.

## Classes and callables

### CatalogAssembler

Propose bounded connection code from actual installed catalog capabilities.

Kind: class. Declared return: Not declared / class. Source line: 22.

### CatalogAssembler.__init__

Inject the selected model boundary; initialization performs no IO.

Kind: callable. Declared return: None. Source line: 25.

### CatalogAssembler.request

Build original requirements and catalog context without reference implementation.

Kind: callable. Declared return: dict. Source line: 30.

### CatalogAssembler.validate

Validate a structured code proposal before packaging or any generated execution.

Kind: callable. Declared return: dict. Source line: 43.

### CatalogAssembler.generate

Retain an explicitly injected callable boundary for compatibility fixtures.

Kind: callable. Declared return: dict. Source line: 49.

### CatalogWidgetDesigner

Write the Gradio widget implementation and provisional tests once per tool.

Kind: class. Declared return: Not declared / class. Source line: 56.

### CatalogWidgetDesigner.__init__

Inject the model client without reading tool files or importing source.

Kind: callable. Declared return: None. Source line: 59.

### CatalogWidgetDesigner.request

Build one widget task from approved metadata and independent cases only.

Kind: callable. Declared return: dict. Source line: 64.

### CatalogWidgetDesigner.generate

Retain the callable fixture boundary without executing generated source.

Kind: callable. Declared return: dict. Source line: 97.

### CatalogWidgetDesigner.validate

Bound and compile proposal data without importing or executing model code.

Kind: callable. Declared return: None. Source line: 104.

### ApplicationCoordinator

Explicit two-phase creation contract; neither phase approves or executes artifacts.

Kind: class. Declared return: Not declared / class. Source line: 113.

### ApplicationCoordinator.plan

Return the validated catalog plan for the original requirements.

Kind: callable. Declared return: dict. Source line: 116.

### ApplicationCoordinator.widgets

Return proposals only for the requested missing widget identities.

Kind: callable. Declared return: dict[str, dict]. Source line: 120.

### CallableCoordinator

Compatibility for explicitly injected legacy/test callables, never a fallback.

Kind: class. Declared return: Not declared / class. Source line: 125.

### CallableCoordinator.__init__

Construct the caller-supplied model double for one operation.

Kind: callable. Declared return: None. Source line: 128.

### CallableCoordinator.plan

Use the same host contract with the explicitly supplied boundary.

Kind: callable. Declared return: dict. Source line: 132.

### CallableCoordinator.widgets

Preserve existing fixture calls while production uses a sequential crew.

Kind: callable. Declared return: dict[str, dict]. Source line: 136.

## Variables and parameters

| Scope | Name | Role and meaning | Type | Lifetime | Writes |
| --- | --- | --- | --- | --- | --- |
| module | Callable | Imported dependency for Callable in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 9 |
| module | Path | Imported dependency for Path in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 10 |
| module | Protocol | Imported dependency for Protocol in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 11 |
| module | ROLE_GENERAL_ASSEMBLER | Imported dependency for ROLE GENERAL ASSEMBLER in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 13 |
| module | ROLE_GENERAL_WIDGET_DESIGNER | Imported dependency for ROLE GENERAL WIDGET DESIGNER in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 13 |
| module | validate_proposal_fields | Imported dependency for validate proposal fields in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 13 |
| module | validate_source | Imported dependency for validate source in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 13 |
| module | ApprovedTool | Imported dependency for ApprovedTool in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 19 |
| CatalogAssembler.__init__ | self | Owning instance; its attributes retain state for the instance lifetime. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 25 |
| CatalogAssembler.__init__ | client | Parameter for client in CatalogAssembler.__init__; use the enclosing contract and type below. | Callable[[str, dict], dict] | Enclosing invocation or class/instance lifetime | 25 |
| CatalogAssembler.__init__ | self.client | Attribute for client in CatalogAssembler.__init__; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 27 |
| CatalogAssembler.request | query | Original user request or a trusted test query; avoid payload logging by default. | str | Enclosing invocation or class/instance lifetime | 30 |
| CatalogAssembler.request | schemas | Parameter for schemas in CatalogAssembler.request; use the enclosing contract and type below. | dict | Enclosing invocation or class/instance lifetime | 30 |
| CatalogAssembler.request | feedback | Parameter for feedback in CatalogAssembler.request; use the enclosing contract and type below. | dict &#124; None | Enclosing invocation or class/instance lifetime | 30 |
| CatalogAssembler.request | content | Artifact or review text whose encoding, size and approval state must be checked. | dict | Enclosing invocation or class/instance lifetime | 32 |
| CatalogAssembler.validate | proposal | Parameter for proposal in CatalogAssembler.validate; use the enclosing contract and type below. | dict | Enclosing invocation or class/instance lifetime | 43 |
| CatalogAssembler.validate | schemas | Parameter for schemas in CatalogAssembler.validate; use the enclosing contract and type below. | dict | Enclosing invocation or class/instance lifetime | 43 |
| CatalogAssembler.validate | ApplicationCode | Imported dependency for ApplicationCode in CatalogAssembler.validate; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 45 |
| CatalogAssembler.generate | self | Owning instance; its attributes retain state for the instance lifetime. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 49 |
| CatalogAssembler.generate | query | Original user request or a trusted test query; avoid payload logging by default. | str | Enclosing invocation or class/instance lifetime | 49 |
| CatalogAssembler.generate | schemas | Parameter for schemas in CatalogAssembler.generate; use the enclosing contract and type below. | dict | Enclosing invocation or class/instance lifetime | 49 |
| CatalogAssembler.generate | feedback | Parameter for feedback in CatalogAssembler.generate; use the enclosing contract and type below. | dict &#124; None | Enclosing invocation or class/instance lifetime | 49 |
| CatalogWidgetDesigner.__init__ | self | Owning instance; its attributes retain state for the instance lifetime. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 59 |
| CatalogWidgetDesigner.__init__ | client | Parameter for client in CatalogWidgetDesigner.__init__; use the enclosing contract and type below. | Callable[[str, dict], dict] | Enclosing invocation or class/instance lifetime | 59 |
| CatalogWidgetDesigner.__init__ | self.client | Attribute for client in CatalogWidgetDesigner.__init__; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 61 |
| CatalogWidgetDesigner.request | tool | Parameter for tool in CatalogWidgetDesigner.request; use the enclosing contract and type below. | ApprovedTool | Enclosing invocation or class/instance lifetime | 64 |
| CatalogWidgetDesigner.request | feedback | Parameter for feedback in CatalogWidgetDesigner.request; use the enclosing contract and type below. | dict &#124; None | Enclosing invocation or class/instance lifetime | 64 |
| CatalogWidgetDesigner.request | name | Current identifier selected by parsing, lookup or dependency registration. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 66 |
| CatalogWidgetDesigner.request | request | Local binding for request in CatalogWidgetDesigner.request; use the enclosing contract and type below. | dict | Enclosing invocation or class/instance lifetime | 67 |
| CatalogWidgetDesigner.generate | self | Owning instance; its attributes retain state for the instance lifetime. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 97 |
| CatalogWidgetDesigner.generate | tool | Parameter for tool in CatalogWidgetDesigner.generate; use the enclosing contract and type below. | ApprovedTool | Enclosing invocation or class/instance lifetime | 97 |
| CatalogWidgetDesigner.generate | feedback | Parameter for feedback in CatalogWidgetDesigner.generate; use the enclosing contract and type below. | dict &#124; None | Enclosing invocation or class/instance lifetime | 97 |
| CatalogWidgetDesigner.generate | proposal | Local binding for proposal in CatalogWidgetDesigner.generate; use the enclosing contract and type below. | Return type of client; see its callable contract | Enclosing invocation or class/instance lifetime | 99 |
| CatalogWidgetDesigner.validate | name | Current identifier selected by parsing, lookup or dependency registration. | str | Enclosing invocation or class/instance lifetime | 104 |
| CatalogWidgetDesigner.validate | proposal | Parameter for proposal in CatalogWidgetDesigner.validate; use the enclosing contract and type below. | dict | Enclosing invocation or class/instance lifetime | 104 |
| ApplicationCoordinator.plan | self | Owning instance; its attributes retain state for the instance lifetime. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 116 |
| ApplicationCoordinator.plan | query | Original user request or a trusted test query; avoid payload logging by default. | str | Enclosing invocation or class/instance lifetime | 116 |
| ApplicationCoordinator.plan | schemas | Parameter for schemas in ApplicationCoordinator.plan; use the enclosing contract and type below. | dict | Enclosing invocation or class/instance lifetime | 116 |
| ApplicationCoordinator.plan | feedback | Parameter for feedback in ApplicationCoordinator.plan; use the enclosing contract and type below. | dict &#124; None | Enclosing invocation or class/instance lifetime | 116 |
| ApplicationCoordinator.widgets | self | Owning instance; its attributes retain state for the instance lifetime. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 120 |
| ApplicationCoordinator.widgets | tools | Parameter for tools in ApplicationCoordinator.widgets; use the enclosing contract and type below. | dict[str, ApprovedTool] | Enclosing invocation or class/instance lifetime | 120 |
| ApplicationCoordinator.widgets | feedback | Parameter for feedback in ApplicationCoordinator.widgets; use the enclosing contract and type below. | dict &#124; None | Enclosing invocation or class/instance lifetime | 120 |
| CallableCoordinator.__init__ | self | Owning instance; its attributes retain state for the instance lifetime. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 128 |
| CallableCoordinator.__init__ | evidence | Parameter for evidence in CallableCoordinator.__init__; use the enclosing contract and type below. | Path | Enclosing invocation or class/instance lifetime | 128 |
| CallableCoordinator.__init__ | client_factory | Parameter for client factory in CallableCoordinator.__init__; use the enclosing contract and type below. | Callable | Enclosing invocation or class/instance lifetime | 128 |
| CallableCoordinator.__init__ | self.client | Attribute for client in CallableCoordinator.__init__; use the enclosing contract and type below. | Return type of client_factory; see its callable contract | Enclosing invocation or class/instance lifetime | 130 |
| CallableCoordinator.plan | self | Owning instance; its attributes retain state for the instance lifetime. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 132 |
| CallableCoordinator.plan | query | Original user request or a trusted test query; avoid payload logging by default. | str | Enclosing invocation or class/instance lifetime | 132 |
| CallableCoordinator.plan | schemas | Parameter for schemas in CallableCoordinator.plan; use the enclosing contract and type below. | dict | Enclosing invocation or class/instance lifetime | 132 |
| CallableCoordinator.plan | feedback | Parameter for feedback in CallableCoordinator.plan; use the enclosing contract and type below. | dict &#124; None | Enclosing invocation or class/instance lifetime | 132 |
| CallableCoordinator.widgets | self | Owning instance; its attributes retain state for the instance lifetime. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 136 |
| CallableCoordinator.widgets | tools | Parameter for tools in CallableCoordinator.widgets; use the enclosing contract and type below. | dict[str, ApprovedTool] | Enclosing invocation or class/instance lifetime | 136 |
| CallableCoordinator.widgets | feedback | Parameter for feedback in CallableCoordinator.widgets; use the enclosing contract and type below. | dict &#124; None | Enclosing invocation or class/instance lifetime | 136 |
| CallableCoordinator.widgets | designer | Local binding for designer in CallableCoordinator.widgets; use the enclosing contract and type below. | Return type of CatalogWidgetDesigner; see its callable contract | Enclosing invocation or class/instance lifetime | 138 |
| CallableCoordinator.widgets.comprehension_139 | name | Current identifier selected by parsing, lookup or dependency registration. | Element of the declared iterable | This comprehension only; does not leak into its enclosing scope | 139 |
| CallableCoordinator.widgets.comprehension_139 | tool | Comprehension item for tool in CallableCoordinator.widgets.comprehension_139; use the enclosing contract and type below. | Element of the declared iterable | This comprehension only; does not leak into its enclosing scope | 139 |
