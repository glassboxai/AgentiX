# Reference for src/agentix/application/tool_routing.py

Read-only semantic selection before exposing verification/execution capabilities.

Source fingerprint: a73c9a4e7f69a24c8cdd716f1e02b8781d3009ad3bad79f31bf9495a73ad515d

This reference is generated from maintained source without imports or execution. Assigned values are intentionally omitted. Runtime-dependent types are explicit; the enclosing docstring defines the behavioral contract. See [architecture](../ARCHITECTURE_QUALITY.md) for manually reviewed responsibility and dependency decisions.

## Classes and callables

### RoutingModelClient

Use the session-selected bounded client with no agent tools or credentials in prompts.

Kind: class. Declared return: Not declared / class. Source line: 13.

### RoutingModelClient.__init__

Inject the already consent-checked local or external model client.

Kind: callable. Declared return: Not declared / class. Source line: 16.

### RoutingModelClient.__call__

Keep selection strict; acceptance text is bounded data for mandatory review.

Kind: callable. Declared return: dict | str. Source line: 20.

### ToolRouter

Inject read-only catalog metadata and a model boundary without execution tools.

Kind: class. Declared return: Not declared / class. Source line: 58.

### ToolRouter.__init__

Construction performs no catalog IO, model call or filesystem mutation.

Kind: callable. Declared return: Not declared / class. Source line: 61.

### ToolRouter.select

Select a semantically matching API or a new capability; validate argument shape.

Kind: callable. Declared return: dict. Source line: 65.

### ToolRouter.acceptance

Propose declarative cases only after provisional native tests; never auto-approve.

Kind: callable. Declared return: str. Source line: 132.

## Variables and parameters

| Scope | Name | Role and meaning | Type | Lifetime | Writes |
| --- | --- | --- | --- | --- | --- |
| module | json | Imported dependency for json in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 3 |
| module | logging | Imported dependency for logging in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 4 |
| module | Path | Imported dependency for Path in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 5 |
| module | CreateRoute | Imported dependency for CreateRoute in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 7 |
| module | ToolRoute | Imported dependency for ToolRoute in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 7 |
| module | validate_value | Imported dependency for validate value in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 8 |
| module | logger | Module logger emitting bounded operation diagnostics rather than artifact bodies. | Return type of getLogger; see its callable contract | Module/process lifetime | 10 |
| RoutingModelClient.__init__ | self | Owning instance; its attributes retain state for the instance lifetime. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 16 |
| RoutingModelClient.__init__ | model | Parameter for model in RoutingModelClient.__init__; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 16 |
| RoutingModelClient.__init__ | self.model | Attribute for model in RoutingModelClient.__init__; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 18 |
| RoutingModelClient.__call__ | self | Owning instance; its attributes retain state for the instance lifetime. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 20 |
| RoutingModelClient.__call__ | role | Parameter for role in RoutingModelClient.__call__; use the enclosing contract and type below. | str | Enclosing invocation or class/instance lifetime | 20 |
| RoutingModelClient.__call__ | content | Artifact or review text whose encoding, size and approval state must be checked. | dict | Enclosing invocation or class/instance lifetime | 20 |
| RoutingModelClient.__call__ | value | Value at the current validation/rendering boundary; apply the enclosing contract. | Return type of call; see its callable contract | Enclosing invocation or class/instance lifetime | 23, 40, 45, 47 |
| RoutingModelClient.__call__ | error | Caught exception for error in RoutingModelClient.__call__; use the enclosing contract and type below. | Exception | Current exception handler; Python clears this binding afterward | 34 |
| RoutingModelClient.__call__ | decode_frame | Imported dependency for decode frame in RoutingModelClient.__call__; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 52 |
| RoutingModelClient.__call__ | parsed | Local binding for parsed in RoutingModelClient.__call__; use the enclosing contract and type below. | Return type of decode_frame; see its callable contract | Enclosing invocation or class/instance lifetime | 54 |
| ToolRouter.__init__ | self | Owning instance; its attributes retain state for the instance lifetime. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 61 |
| ToolRouter.__init__ | catalog | Parameter for catalog in ToolRouter.__init__; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 61 |
| ToolRouter.__init__ | root | Explicit root directory against which named paths are resolved. | Path | Enclosing invocation or class/instance lifetime | 61 |
| ToolRouter.__init__ | client_factory | Parameter for client factory in ToolRouter.__init__; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 61 |
| ToolRouter.__init__ | self.catalog | Attribute for catalog in ToolRouter.__init__; use the enclosing contract and type below. | tuple | Enclosing invocation or class/instance lifetime | 63 |
| ToolRouter.__init__ | self.root | Explicit root directory against which named paths are resolved. | tuple | Enclosing invocation or class/instance lifetime | 63 |
| ToolRouter.__init__ | self.client_factory | Attribute for client factory in ToolRouter.__init__; use the enclosing contract and type below. | tuple | Enclosing invocation or class/instance lifetime | 63 |
| ToolRouter.select | self | Owning instance; its attributes retain state for the instance lifetime. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 65 |
| ToolRouter.select | query | Original user request or a trusted test query; avoid payload logging by default. | str | Enclosing invocation or class/instance lifetime | 65 |
| ToolRouter.select | catalog | Local binding for catalog in ToolRouter.select; use the enclosing contract and type below. | Return type of contracts; see its callable contract | Enclosing invocation or class/instance lifetime | 67 |
| ToolRouter.select | content | Artifact or review text whose encoding, size and approval state must be checked. | dict | Enclosing invocation or class/instance lifetime | 68 |
| ToolRouter.select | proposal | Local binding for proposal in ToolRouter.select; use the enclosing contract and type below. | Return type of callable; see its callable contract | Enclosing invocation or class/instance lifetime | 72 |
| ToolRouter.select | ValidationError | Imported dependency for ValidationError in ToolRouter.select; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 73 |
| ToolRouter.select | creation | Local binding for creation in ToolRouter.select; use the enclosing contract and type below. | Return type of dict; see its callable contract | Enclosing invocation or class/instance lifetime | 81 |
| ToolRouter.select | transport | Local binding for transport in ToolRouter.select; use the enclosing contract and type below. | Return type of pop; see its callable contract | Enclosing invocation or class/instance lifetime | 82 |
| ToolRouter.select | route | Local binding for route in ToolRouter.select; use the enclosing contract and type below. | Return type of model_dump; see its callable contract | Enclosing invocation or class/instance lifetime | 83, 90 |
| ToolRouter.select | arguments | Typed binding for arguments in ToolRouter.select; use the enclosing contract and type below. | dict | Enclosing invocation or class/instance lifetime | 97 |
| ToolRouter.select | pair | Loop item for pair in ToolRouter.select; use the enclosing contract and type below. | Element of the declared iterable | Enclosing invocation or class/instance lifetime | 98 |
| ToolRouter.select | name | Current identifier selected by parsing, lookup or dependency registration. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 103 |
| ToolRouter.select | contract | Validated declarative acceptance data bound to current artifact identities. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 112 |
| ToolRouter.select | params | Local binding for params in ToolRouter.select; use the enclosing contract and type below. | tuple | Enclosing invocation or class/instance lifetime | 113 |
| ToolRouter.select | defaults | Local binding for defaults in ToolRouter.select; use the enclosing contract and type below. | tuple | Enclosing invocation or class/instance lifetime | 113 |
| ToolRouter.select | parameter | Loop item for parameter in ToolRouter.select; use the enclosing contract and type below. | Element of the declared iterable | Enclosing invocation or class/instance lifetime | 118 |
| ToolRouter.select | value | Value at the current validation/rendering boundary; apply the enclosing contract. | Element of the declared iterable | Enclosing invocation or class/instance lifetime | 118 |
| ToolRouter.acceptance | self | Owning instance; its attributes retain state for the instance lifetime. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 132 |
| ToolRouter.acceptance | name | Current identifier selected by parsing, lookup or dependency registration. | str | Enclosing invocation or class/instance lifetime | 132 |
| ToolRouter.acceptance | code | Source snapshot passed through approval, syntax checks and isolated staging. | str | Enclosing invocation or class/instance lifetime | 132 |
| ToolRouter.acceptance | specification | Parameter for specification in ToolRouter.acceptance; use the enclosing contract and type below. | str | Enclosing invocation or class/instance lifetime | 132 |
| ToolRouter.acceptance | content | Artifact or review text whose encoding, size and approval state must be checked. | dict | Enclosing invocation or class/instance lifetime | 134 |
| ToolRouter.acceptance | proposal | Local binding for proposal in ToolRouter.acceptance; use the enclosing contract and type below. | Return type of callable; see its callable contract | Enclosing invocation or class/instance lifetime | 144 |
