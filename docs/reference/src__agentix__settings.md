# Reference for src/agentix/settings.py

Immutable settings loaded without initializing external services or storage.

Source fingerprint: 2346d10481f18e6056dffa55f629ef53212dab2eee114a66c09f7f7957fd4dbc

This reference is generated from maintained source without imports or execution. Assigned values are intentionally omitted. Runtime-dependent types are explicit; the enclosing docstring defines the behavioral contract. See [architecture](../ARCHITECTURE_QUALITY.md) for manually reviewed responsibility and dependency decisions.

## Classes and callables

### Settings

Runtime inputs; constructing settings never creates their target paths.

Attributes:
    base_dir: Application checkout root, independent of the working directory.
    tools_root: Artifact storage root used only when services are invoked.
    model: CrewAI model identifier, including the existing Ollama prefix.
    ollama_url: Existing configurable provider endpoint.
    temperature: Existing low-temperature generation setting.
    server_port: Explicit loopback TCP port; occupied ports fail without fallback.
    open_browser: Whether manual GUI launch opens the local browser.

Kind: class. Declared return: Not declared / class. Source line: 10.

### Settings.from_environment

Read configuration values without changing the process environment.

An explicit base directory supports isolated tests. Defaults preserve the
original checkout-relative storage location rather than the package path.

Kind: callable. Declared return: 'Settings'. Source line: 32.

## Variables and parameters

| Scope | Name | Role and meaning | Type | Lifetime | Writes |
| --- | --- | --- | --- | --- | --- |
| module | os | Imported dependency for os in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 3 |
| module | Mapping | Imported dependency for Mapping in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 4 |
| module | dataclass | Imported dependency for dataclass in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 5 |
| module | Path | Imported dependency for Path in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 6 |
| Settings | base_dir | Typed binding for base dir in Settings; use the enclosing contract and type below. | Path | Enclosing invocation or class/instance lifetime | 23 |
| Settings | tools_root | Typed binding for tools root in Settings; use the enclosing contract and type below. | Path | Enclosing invocation or class/instance lifetime | 24 |
| Settings | model | Typed binding for model in Settings; use the enclosing contract and type below. | str | Enclosing invocation or class/instance lifetime | 25 |
| Settings | ollama_url | Typed binding for ollama url in Settings; use the enclosing contract and type below. | str | Enclosing invocation or class/instance lifetime | 26 |
| Settings | temperature | Typed binding for temperature in Settings; use the enclosing contract and type below. | float | Enclosing invocation or class/instance lifetime | 27 |
| Settings | server_port | Typed binding for server port in Settings; use the enclosing contract and type below. | int | Enclosing invocation or class/instance lifetime | 28 |
| Settings | open_browser | Typed binding for open browser in Settings; use the enclosing contract and type below. | bool | Enclosing invocation or class/instance lifetime | 29 |
| Settings.from_environment | cls | Class receiving this class-level operation. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 33 |
| Settings.from_environment | environment | Parameter for environment in Settings.from_environment; use the enclosing contract and type below. | Mapping[str, str] &#124; None | Enclosing invocation or class/instance lifetime | 33 |
| Settings.from_environment | base_dir | Parameter for base dir in Settings.from_environment; use the enclosing contract and type below. | Path &#124; None | Enclosing invocation or class/instance lifetime | 33 |
| Settings.from_environment | values | Local binding for values in Settings.from_environment; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 40 |
| Settings.from_environment | base | Local binding for base in Settings.from_environment; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 41 |
| Settings.from_environment | port_text | Local binding for port text in Settings.from_environment; use the enclosing contract and type below. | Return type of get; see its callable contract | Enclosing invocation or class/instance lifetime | 42 |
| Settings.from_environment | browser_text | Local binding for browser text in Settings.from_environment; use the enclosing contract and type below. | Return type of lower; see its callable contract | Enclosing invocation or class/instance lifetime | 45 |
| Settings.from_environment | tools | Local binding for tools in Settings.from_environment; use the enclosing contract and type below. | Return type of Path; see its callable contract | Enclosing invocation or class/instance lifetime | 48 |
