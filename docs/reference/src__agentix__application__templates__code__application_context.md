# Reference for src/agentix/application/templates/code/application_context.py

Native widget context with readable application-wide unique control identities.

Source fingerprint: 466bb79e15e43d102e74a11373099b609f17b4ac7efa5447e1a12d2e34e1094a

This reference is generated from maintained source without imports or execution. Assigned values are intentionally omitted. Runtime-dependent types are explicit; the enclosing docstring defines the behavioral contract. See [architecture](../ARCHITECTURE_QUALITY.md) for manually reviewed responsibility and dependency decisions.

## Classes and callables

### Context

Allocate semantic controls once; repeated requests for a role are stable.

Kind: class. Declared return: Not declared / class. Source line: 8.

### Context.__init__

Bind a validated widget instance and its exact named parameter vocabulary.

Kind: callable. Declared return: None. Source line: 11.

### Context.elem_id

Return unique semantic IDs; Group IDs are omitted for Gradio compatibility.

Kind: callable. Declared return: str | None. Source line: 19.

## Variables and parameters

| Scope | Name | Role and meaning | Type | Lifetime | Writes |
| --- | --- | --- | --- | --- | --- |
| module | re | Imported dependency for re in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 3 |
| module | ElementIds | Imported dependency for ElementIds in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 5 |
| Context.__init__ | self | Owning instance; its attributes retain state for the instance lifetime. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 11 |
| Context.__init__ | instance | Parameter for instance in Context.__init__; use the enclosing contract and type below. | str | Enclosing invocation or class/instance lifetime | 11 |
| Context.__init__ | ids | Parameter for ids in Context.__init__; use the enclosing contract and type below. | ElementIds | Enclosing invocation or class/instance lifetime | 11 |
| Context.__init__ | parameters | Parameter for parameters in Context.__init__; use the enclosing contract and type below. | list[str] | Enclosing invocation or class/instance lifetime | 11 |
| Context.__init__ | self.ids | Attribute for ids in Context.__init__; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 13 |
| Context.__init__ | self.scope | Attribute for scope in Context.__init__; use the enclosing contract and type below. | Return type of new_widget; see its callable contract | Enclosing invocation or class/instance lifetime | 14 |
| Context.__init__ | self.api_name | Attribute for api name in Context.__init__; use the enclosing contract and type below. | Return type of api_name; see its callable contract | Enclosing invocation or class/instance lifetime | 15 |
| Context.__init__ | self.allowed | Attribute for allowed in Context.__init__; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 16 |
| Context.__init__ | self.controls | Attribute for controls in Context.__init__; use the enclosing contract and type below. | dict | Enclosing invocation or class/instance lifetime | 17 |
| Context.elem_id | self | Owning instance; its attributes retain state for the instance lifetime. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 19 |
| Context.elem_id | role | Parameter for role in Context.elem_id; use the enclosing contract and type below. | str | Enclosing invocation or class/instance lifetime | 19 |
