# Reference for custom_tools.py

Compatibility access to lazily registered CrewAI tools.

Import alone is inert; explicitly requesting a registered tool loads CrewAI.
Framework-free operations are available in agentix.tools.ArtifactTools.

Source fingerprint: 9ec81fb368d2e57176c92c961fa3e38f85b096d3e478bbe39021174cd6370c05

This reference is generated from maintained source without imports or execution. Assigned values are intentionally omitted. Runtime-dependent types are explicit; the enclosing docstring defines the behavioral contract. See [architecture](../ARCHITECTURE_QUALITY.md) for manually reviewed responsibility and dependency decisions.

## Classes and callables

### append_structured_incidence

Preserve the non-decorated incidence helper's public contract.

Kind: callable. Declared return: str. Source line: 26.

### __getattr__

Return a decorated compatibility tool without constructing any model.

Kind: callable. Declared return: Any. Source line: 33.

## Variables and parameters

| Scope | Name | Role and meaning | Type | Lifetime | Writes |
| --- | --- | --- | --- | --- | --- |
| module | Any | Imported dependency for Any in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 7 |
| module | _agentix_path | Imported dependency for agentix path in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 9 |
| module | SecurityManager | Imported dependency for SecurityManager in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 10 |
| module | ArtifactTools | Imported dependency for ArtifactTools in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 11 |
| module | _NAMES | Module binding for NAMES in module; use the enclosing contract and type below. | tuple | Module/process lifetime | 13 |
| module | __all__ | Module binding for all in module; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Module/process lifetime | 23 |
| append_structured_incidence | tool_name | Validated public tool identifier within the configured storage boundary. | str | Enclosing invocation or class/instance lifetime | 26 |
| append_structured_incidence | suffix | Parameter for suffix in append_structured_incidence; use the enclosing contract and type below. | str | Enclosing invocation or class/instance lifetime | 26 |
| append_structured_incidence | title | Parameter for title in append_structured_incidence; use the enclosing contract and type below. | str | Enclosing invocation or class/instance lifetime | 26 |
| append_structured_incidence | details | Parameter for details in append_structured_incidence; use the enclosing contract and type below. | str | Enclosing invocation or class/instance lifetime | 26 |
| __getattr__ | name | Current identifier selected by parsing, lookup or dependency registration. | str | Enclosing invocation or class/instance lifetime | 33 |
| __getattr__ | get_default_tools | Imported dependency for get default tools in __getattr__; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 36 |
