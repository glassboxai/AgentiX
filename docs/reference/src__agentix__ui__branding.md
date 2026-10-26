# Reference for src/agentix/ui/branding.py

Load maintained local branding; never serve an arbitrary filesystem directory.

Source fingerprint: 1f5dbfc695a03c0ddaba5fe125301f634c58753a07a7b0ab1a1297ee5f193a9a

This reference is generated from maintained source without imports or execution. Assigned values are intentionally omitted. Runtime-dependent types are explicit; the enclosing docstring defines the behavioral contract. See [architecture](../ARCHITECTURE_QUALITY.md) for manually reviewed responsibility and dependency decisions.

## Classes and callables

### stylesheet

Return the application CSS for Gradio's launch-time styling API.

Kind: callable. Declared return: str. Source line: 9.

### header

Render the approved identity using a fixed local PNG as an inline image.

Kind: callable. Declared return: str. Source line: 14.

### launch_options

Share appearance across normal and disposable launchers; expose no file roots.

Kind: callable. Declared return: dict[str, object]. Source line: 29.

## Variables and parameters

| Scope | Name | Role and meaning | Type | Lifetime | Writes |
| --- | --- | --- | --- | --- | --- |
| module | base64 | Imported dependency for base64 in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 3 |
| module | Path | Imported dependency for Path in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 4 |
| module | ASSETS | Module binding for ASSETS in module; use the enclosing contract and type below. | Return type of with_name; see its callable contract | Module/process lifetime | 6 |
| header | logo | Local binding for logo in header; use the enclosing contract and type below. | Return type of decode; see its callable contract | Enclosing invocation or class/instance lifetime | 16 |
