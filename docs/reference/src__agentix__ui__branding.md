# Reference for src/agentix/ui/branding.py

Load maintained local branding; never serve an arbitrary filesystem directory.

Source fingerprint: b05065ef18ad6ec45fd0c600f0dd3925ad68a9dd5e857d8ec141f466164dada9

This reference is generated from maintained source without imports or execution. Assigned values are intentionally omitted. Runtime-dependent types are explicit; the enclosing docstring defines the behavioral contract. See [architecture](../ARCHITECTURE_QUALITY.md) for manually reviewed responsibility and dependency decisions.

## Classes and callables

### mermaid_script

Wrap the pinned bundle so Gradio's eval scope still publishes the global.

Gradio executes the launch ``js`` string inside ``eval``, where the bundle's
top-level ``var`` stays local; its own final assignment therefore reads an
undefined ``globalThis`` property. The wrapper keeps that binding in scope and
publishes ``globalThis.mermaid`` from it. The vendored bytes stay unchanged.

Kind: callable. Declared return: str. Source line: 13.

### stylesheet

Return the application CSS for Gradio's launch-time styling API.

Kind: callable. Declared return: str. Source line: 32.

### header

Render the approved identity using a fixed local PNG as an inline image.

Kind: callable. Declared return: str. Source line: 37.

### launch_options

Share appearance across normal and disposable launchers; expose no file roots.

Kind: callable. Declared return: dict[str, object]. Source line: 52.

## Variables and parameters

| Scope | Name | Role and meaning | Type | Lifetime | Writes |
| --- | --- | --- | --- | --- | --- |
| module | base64 | Imported dependency for base64 in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 3 |
| module | Path | Imported dependency for Path in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 4 |
| module | ASSETS | Module binding for ASSETS in module; use the enclosing contract and type below. | Return type of with_name; see its callable contract | Module/process lifetime | 6 |
| module | MERMAID_BUNDLE | Module binding for MERMAID BUNDLE in module; use the enclosing contract and type below. | str | Module/process lifetime | 7 |
| module | MERMAID_GLOBAL_TAIL | Module binding for MERMAID GLOBAL TAIL in module; use the enclosing contract and type below. | str | Module/process lifetime | 8 |
| mermaid_script | bundle | Local binding for bundle in mermaid_script; use the enclosing contract and type below. | Return type of rstrip; see its callable contract | Enclosing invocation or class/instance lifetime | 21 |
| mermaid_script | body | Local binding for body in mermaid_script; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 24 |
| header | logo | Local binding for logo in header; use the enclosing contract and type below. | Return type of decode; see its callable contract | Enclosing invocation or class/instance lifetime | 39 |
| launch_options.comprehension_59 | name | Current identifier selected by parsing, lookup or dependency registration. | Element of the declared iterable | This comprehension only; does not leak into its enclosing scope | 61 |
