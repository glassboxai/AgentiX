# Reference for src/agentix/host_requirements.py

Explicit recovery for host-owned, reviewed runtime requirements.

The registry is maintained application code. Generated artifacts and browser input
never supply identifiers, commands, URLs or package-manager arguments. A caller
must separately obtain explicit human consent before calling :meth:`install`.

Source fingerprint: df87c31b44c05b334a61a9f7914ed40675d80ce5d3802ab17c7a8c54e31bebfb

This reference is generated from maintained source without imports or execution. Assigned values are intentionally omitted. Runtime-dependent types are explicit; the enclosing docstring defines the behavioral contract. See [architecture](../ARCHITECTURE_QUALITY.md) for manually reviewed responsibility and dependency decisions.

## Classes and callables

### HostRequirementInstallError

Report a bounded, non-sensitive failure while repairing a host requirement.

Kind: class. Declared return: Not declared / class. Source line: 19.

### HostRequirement

Describe one immutable host dependency and its reviewed repair command.

Attributes:
    identifier: Closed registry key, never supplied by generated artifacts.
    user_message: Consent text explaining the local host change.
    command: Exact process arguments, including the active managed Python.

Kind: class. Declared return: Not declared / class. Source line: 24.

### playwright_chromium_path

Return Playwright's selected Chromium path without starting a browser.

Raises:
    RuntimeError: If the installed Playwright package cannot expose its
        browser metadata. The caller treats this as an unavailable host
        requirement and never exposes its implementation detail to users.

Kind: callable. Declared return: Path. Source line: 38.

### installer_environment

Return only Windows variables needed by a reviewed local installer.

Package indexes, targets, proxy settings and arbitrary inherited variables are
deliberately omitted. The command uses an absolute Python executable and
Python isolated mode, so no caller-supplied import location is inherited.

Kind: callable. Declared return: dict[str, str]. Source line: 52.

### HostRequirements

Probe and repair only requirements registered by maintained host code.

Parameters:
    browser_path: Injected browser metadata probe used by tests and the
        application acceptance preflight.
    runner: Injected process boundary. Production uses a bounded subprocess
        call and captures installer output so it cannot leak into logs/UI.
    python: Managed interpreter used for the fixed Playwright command.
    environment_factory: Builds the scrubbed child environment.

Kind: class. Declared return: Not declared / class. Source line: 67.

### HostRequirements.__init__

Build the closed requirement registry without probing or installing.

Kind: callable. Declared return: None. Source line: 79.

### HostRequirements.requirement

Return one registered requirement or reject arbitrary installer requests.

Kind: callable. Declared return: HostRequirement. Source line: 104.

### HostRequirements.missing

Return a registered requirement only when its postcondition is absent.

Kind: callable. Declared return: HostRequirement | None. Source line: 111.

### HostRequirements.install

Run one reviewed installer and require its independent postcondition.

The method does not request consent. Controllers must make the requirement
visible to the owning user and call this only from the explicit install
action. Raises a fixed error after failures and retains no child output.

Kind: callable. Declared return: HostRequirement. Source line: 125.

### HostRequirements._run

Execute the fixed installer with bounded retained diagnostics only.

Kind: callable. Declared return: None. Source line: 156.

## Variables and parameters

| Scope | Name | Role and meaning | Type | Lifetime | Writes |
| --- | --- | --- | --- | --- | --- |
| module | logging | Imported dependency for logging in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 8 |
| module | os | Imported dependency for os in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 9 |
| module | subprocess | Imported dependency for subprocess in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 10 |
| module | sys | Imported dependency for sys in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 11 |
| module | Callable | Imported dependency for Callable in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 12 |
| module | dataclass | Imported dependency for dataclass in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 13 |
| module | Path | Imported dependency for Path in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 14 |
| module | logger | Module logger emitting bounded operation diagnostics rather than artifact bodies. | Return type of getLogger; see its callable contract | Module/process lifetime | 16 |
| HostRequirement | identifier | Typed binding for identifier in HostRequirement; use the enclosing contract and type below. | str | Enclosing invocation or class/instance lifetime | 33 |
| HostRequirement | user_message | Typed binding for user message in HostRequirement; use the enclosing contract and type below. | str | Enclosing invocation or class/instance lifetime | 34 |
| HostRequirement | command | Typed binding for command in HostRequirement; use the enclosing contract and type below. | tuple[str, ...] | Enclosing invocation or class/instance lifetime | 35 |
| playwright_chromium_path | sync_playwright | Imported dependency for sync playwright in playwright_chromium_path; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 46 |
| playwright_chromium_path | driver | Managed resource for driver in playwright_chromium_path; use the enclosing contract and type below. | Return type of sync_playwright; see its callable contract | Context-manager block; exit invokes its cleanup protocol | 48 |
| installer_environment | source | Explicit source document or source-code text; never imported for reference generation. | dict[str, str] &#124; None | Enclosing invocation or class/instance lifetime | 52 |
| installer_environment | values | Local binding for values in installer_environment; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 59 |
| installer_environment.comprehension_60 | name | Current identifier selected by parsing, lookup or dependency registration. | Element of the declared iterable | This comprehension only; does not leak into its enclosing scope | 62 |
| HostRequirements.__init__ | self | Owning instance; its attributes retain state for the instance lifetime. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 80 |
| HostRequirements.__init__ | browser_path | Parameter for browser path in HostRequirements.__init__; use the enclosing contract and type below. | Callable[[], Path] | Enclosing invocation or class/instance lifetime | 82 |
| HostRequirements.__init__ | runner | Parameter for runner in HostRequirements.__init__; use the enclosing contract and type below. | Callable[[tuple[str, ...], dict[str, str]], None] &#124; None | Enclosing invocation or class/instance lifetime | 83 |
| HostRequirements.__init__ | python | Parameter for python in HostRequirements.__init__; use the enclosing contract and type below. | str &#124; None | Enclosing invocation or class/instance lifetime | 84 |
| HostRequirements.__init__ | environment_factory | Parameter for environment factory in HostRequirements.__init__; use the enclosing contract and type below. | Callable[[], dict[str, str]] | Enclosing invocation or class/instance lifetime | 85 |
| HostRequirements.__init__ | executable | Local binding for executable in HostRequirements.__init__; use the enclosing contract and type below. | Return type of str; see its callable contract | Enclosing invocation or class/instance lifetime | 88 |
| HostRequirements.__init__ | self._browser_path | Attribute for browser path in HostRequirements.__init__; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 89 |
| HostRequirements.__init__ | self._runner | Attribute for runner in HostRequirements.__init__; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 90 |
| HostRequirements.__init__ | self._environment_factory | Attribute for environment factory in HostRequirements.__init__; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 91 |
| HostRequirements.__init__ | self._requirements | Attribute for requirements in HostRequirements.__init__; use the enclosing contract and type below. | dict | Enclosing invocation or class/instance lifetime | 92 |
| HostRequirements.requirement | self | Owning instance; its attributes retain state for the instance lifetime. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 104 |
| HostRequirements.requirement | identifier | Parameter for identifier in HostRequirements.requirement; use the enclosing contract and type below. | str | Enclosing invocation or class/instance lifetime | 104 |
| HostRequirements.missing | self | Owning instance; its attributes retain state for the instance lifetime. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 111 |
| HostRequirements.missing | identifier | Parameter for identifier in HostRequirements.missing; use the enclosing contract and type below. | str | Enclosing invocation or class/instance lifetime | 111 |
| HostRequirements.missing | requirement | Local binding for requirement in HostRequirements.missing; use the enclosing contract and type below. | Return type of requirement; see its callable contract | Enclosing invocation or class/instance lifetime | 113 |
| HostRequirements.missing | available | Local binding for available in HostRequirements.missing; use the enclosing contract and type below. | Return type of is_file; see its callable contract | Enclosing invocation or class/instance lifetime | 115, 122 |
| HostRequirements.missing | error | Caught exception for error in HostRequirements.missing; use the enclosing contract and type below. | Exception | Current exception handler; Python clears this binding afterward | 116 |
| HostRequirements.install | self | Owning instance; its attributes retain state for the instance lifetime. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 125 |
| HostRequirements.install | identifier | Parameter for identifier in HostRequirements.install; use the enclosing contract and type below. | str | Enclosing invocation or class/instance lifetime | 125 |
| HostRequirements.install | requirement | Local binding for requirement in HostRequirements.install; use the enclosing contract and type below. | Return type of requirement; see its callable contract | Enclosing invocation or class/instance lifetime | 132 |
| HostRequirements.install | error | Caught exception for error in HostRequirements.install; use the enclosing contract and type below. | Exception | Current exception handler; Python clears this binding afterward | 138 |
| HostRequirements._run | command | Parameter for command in HostRequirements._run; use the enclosing contract and type below. | tuple[str, ...] | Enclosing invocation or class/instance lifetime | 156 |
| HostRequirements._run | environment | Parameter for environment in HostRequirements._run; use the enclosing contract and type below. | dict[str, str] | Enclosing invocation or class/instance lifetime | 156 |
