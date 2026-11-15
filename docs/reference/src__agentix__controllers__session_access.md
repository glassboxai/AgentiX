# Reference for src/agentix/controllers/session_access.py

Shared owner resolution for tab/sidebar callbacks without framework dependencies.

Source fingerprint: 498b13b8e7f63a4a759433729a01bd35c8a7a2ba987be69b6ed24fe495a2b8eb

This reference is generated from maintained source without imports or execution. Assigned values are intentionally omitted. Runtime-dependent types are explicit; the enclosing docstring defines the behavioral contract. See [architecture](../ARCHITECTURE_QUALITY.md) for manually reviewed responsibility and dependency decisions.

## Classes and callables

### SessionOwnerAccess

Require verified browser routing and token ownership before service access.

Kind: class. Declared return: Not declared / class. Source line: 11.

### SessionOwnerAccess.__init__

Retain only the server registry, never a global active controller.

Kind: callable. Declared return: None. Source line: 14.

### SessionOwnerAccess._session

Resolve trusted framework routing metadata and opaque server State.

Kind: callable. Declared return: Session. Source line: 18.

## Variables and parameters

| Scope | Name | Role and meaning | Type | Lifetime | Writes |
| --- | --- | --- | --- | --- | --- |
| module | annotations | Imported dependency for annotations in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 3 |
| module | TYPE_CHECKING | Imported dependency for TYPE CHECKING in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 5 |
| module | Any | Imported dependency for Any in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 5 |
| module | Session | Imported dependency for Session in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 8 |
| module | SessionRegistry | Imported dependency for SessionRegistry in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 8 |
| SessionOwnerAccess.__init__ | self | Owning instance; its attributes retain state for the instance lifetime. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 14 |
| SessionOwnerAccess.__init__ | registry | Parameter for registry in SessionOwnerAccess.__init__; use the enclosing contract and type below. | SessionRegistry | Enclosing invocation or class/instance lifetime | 14 |
| SessionOwnerAccess.__init__ | self.registry | Attribute for registry in SessionOwnerAccess.__init__; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 16 |
| SessionOwnerAccess._session | self | Owning instance; its attributes retain state for the instance lifetime. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 18 |
| SessionOwnerAccess._session | token | Parameter for token in SessionOwnerAccess._session; use the enclosing contract and type below. | str &#124; None | Enclosing invocation or class/instance lifetime | 18 |
| SessionOwnerAccess._session | request | Parameter for request in SessionOwnerAccess._session; use the enclosing contract and type below. | Any | Enclosing invocation or class/instance lifetime | 18 |
