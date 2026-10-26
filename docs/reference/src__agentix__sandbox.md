# Reference for src/agentix/sandbox.py

Disposable standard-library Python execution in a native Windows AppContainer.

No host execution fallback exists. Only trusted runtime files, the trusted worker
and explicit input bytes are copied; no project directories are mounted/shared.

Source fingerprint: 0e98fd8b4705f9dd42b6a4e362492b43ba7850a7c0e9466ff75166d23707fee6

This reference is generated from maintained source without imports or execution. Assigned values are intentionally omitted. Runtime-dependent types are explicit; the enclosing docstring defines the behavioral contract. See [architecture](../ARCHITECTURE_QUALITY.md) for manually reviewed responsibility and dependency decisions.

## Classes and callables

### IsolationUnavailable

The requested OS boundary could not be provisioned; execution is denied.

Kind: class. Declared return: Not declared / class. Source line: 25.

### SandboxResult

Host observation plus an explicitly untrusted child-authored report.

Kind: class. Declared return: Not declared / class. Source line: 30.

### decode_report

Require one complete bounded JSON frame; never parse plain success text.

Kind: callable. Declared return: dict[str, Any]. Source line: 40.

### WindowsSandbox

Provision a fresh runtime/profile/job per invocation; never reuse child state.

Kind: class. Declared return: Not declared / class. Source line: 88.

### WindowsSandbox.__init__

Set finite host-enforced bounds without starting native work.

Kind: callable. Declared return: None. Source line: 91.

### WindowsSandbox.execute

Copy inputs and execute only after all OS restrictions are established.

Raises IsolationUnavailable on unsupported hosts/setup failures. A timeout,
failed child or malformed report is returned as an unsuccessful result.
Provisioning time is separate from the child execution deadline.

Kind: callable. Declared return: SandboxResult. Source line: 110.

### WindowsSandbox.evaluate

Observe one function call in a new child without supplying expected values.

Kind: callable. Declared return: SandboxResult. Source line: 206.

### WindowsSandbox._copy_runtime

Stage CPython's standard library; never copy site-packages or the project.

Kind: callable. Declared return: None. Source line: 213.

## Variables and parameters

| Scope | Name | Role and meaning | Type | Lifetime | Writes |
| --- | --- | --- | --- | --- | --- |
| module | json | Imported dependency for json in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 7 |
| module | logging | Imported dependency for logging in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 8 |
| module | os | Imported dependency for os in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 9 |
| module | re | Imported dependency for re in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 10 |
| module | shutil | Imported dependency for shutil in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 11 |
| module | subprocess | Imported dependency for subprocess in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 12 |
| module | sys | Imported dependency for sys in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 13 |
| module | tempfile | Imported dependency for tempfile in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 14 |
| module | time | Imported dependency for time in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 15 |
| module | dataclass | Imported dependency for dataclass in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 16 |
| module | Path | Imported dependency for Path in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 17 |
| module | Any | Imported dependency for Any in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 18 |
| module | log_event | Imported dependency for log event in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 20 |
| module | logger | Module logger emitting bounded operation diagnostics rather than artifact bodies. | Return type of getLogger; see its callable contract | Module/process lifetime | 22 |
| SandboxResult | exit_code | Typed binding for exit code in SandboxResult; use the enclosing contract and type below. | int | Enclosing invocation or class/instance lifetime | 33 |
| SandboxResult | output | Typed binding for output in SandboxResult; use the enclosing contract and type below. | str | Enclosing invocation or class/instance lifetime | 34 |
| SandboxResult | report | Typed binding for report in SandboxResult; use the enclosing contract and type below. | dict[str, Any] &#124; None | Enclosing invocation or class/instance lifetime | 35 |
| SandboxResult | isolated | Typed binding for isolated in SandboxResult; use the enclosing contract and type below. | bool | Enclosing invocation or class/instance lifetime | 36 |
| SandboxResult | failure | Typed binding for failure in SandboxResult; use the enclosing contract and type below. | str | Enclosing invocation or class/instance lifetime | 37 |
| decode_report | output | Parameter for output in decode_report; use the enclosing contract and type below. | str | Enclosing invocation or class/instance lifetime | 40 |
| decode_report | _unique | Imported dependency for unique in decode_report; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 42 |
| decode_report | frames | Local binding for frames in decode_report; use the enclosing contract and type below. | list | Enclosing invocation or class/instance lifetime | 44 |
| decode_report.comprehension_44 | line | Current source or text line scoped to parsing; no implicit execution occurs. | Element of the declared iterable | This comprehension only; does not leak into its enclosing scope | 46 |
| decode_report | report | Local binding for report in decode_report; use the enclosing contract and type below. | Return type of loads; see its callable contract | Enclosing invocation or class/instance lifetime | 51 |
| decode_report | validate_json | Imported dependency for validate json in decode_report; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 58 |
| decode_report.comprehension_78 | key | Comprehension item for key in decode_report.comprehension_78; use the enclosing contract and type below. | Element of the declared iterable | This comprehension only; does not leak into its enclosing scope | 80 |
| WindowsSandbox.__init__ | self | Owning instance; its attributes retain state for the instance lifetime. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 92 |
| WindowsSandbox.__init__ | timeout | Parameter for timeout in WindowsSandbox.__init__; use the enclosing contract and type below. | float | Enclosing invocation or class/instance lifetime | 94 |
| WindowsSandbox.__init__ | memory | Parameter for memory in WindowsSandbox.__init__; use the enclosing contract and type below. | int | Enclosing invocation or class/instance lifetime | 95 |
| WindowsSandbox.__init__ | processes | Parameter for processes in WindowsSandbox.__init__; use the enclosing contract and type below. | int | Enclosing invocation or class/instance lifetime | 96 |
| WindowsSandbox.__init__ | max_output | Parameter for max output in WindowsSandbox.__init__; use the enclosing contract and type below. | int | Enclosing invocation or class/instance lifetime | 97 |
| WindowsSandbox.__init__ | self.timeout | Attribute for timeout in WindowsSandbox.__init__; use the enclosing contract and type below. | tuple | Enclosing invocation or class/instance lifetime | 107 |
| WindowsSandbox.__init__ | self.memory | Attribute for memory in WindowsSandbox.__init__; use the enclosing contract and type below. | tuple | Enclosing invocation or class/instance lifetime | 107 |
| WindowsSandbox.__init__ | self.processes | Attribute for processes in WindowsSandbox.__init__; use the enclosing contract and type below. | tuple | Enclosing invocation or class/instance lifetime | 108 |
| WindowsSandbox.__init__ | self.max_output | Attribute for max output in WindowsSandbox.__init__; use the enclosing contract and type below. | tuple | Enclosing invocation or class/instance lifetime | 108 |
| WindowsSandbox.execute | self | Owning instance; its attributes retain state for the instance lifetime. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 111 |
| WindowsSandbox.execute | code | Source snapshot passed through approval, syntax checks and isolated staging. | bytes | Enclosing invocation or class/instance lifetime | 112 |
| WindowsSandbox.execute | tests | Optional unittest source snapshot; child-authored success remains provisional. | bytes &#124; None | Enclosing invocation or class/instance lifetime | 113 |
| WindowsSandbox.execute | tool_name | Validated public tool identifier within the configured storage boundary. | str | Enclosing invocation or class/instance lifetime | 114 |
| WindowsSandbox.execute | function_name | Public callable selected for the current operation; empty selects test mode. | str | Enclosing invocation or class/instance lifetime | 115 |
| WindowsSandbox.execute | kwargs | Bounded JSON keyword arguments; no executable objects are accepted. | dict[str, Any] | Enclosing invocation or class/instance lifetime | 116 |
| WindowsSandbox.execute | observation | Parameter for observation in WindowsSandbox.execute; use the enclosing contract and type below. | bool | Enclosing invocation or class/instance lifetime | 118 |
| WindowsSandbox.execute | NativeWindows | Imported dependency for NativeWindows in WindowsSandbox.execute; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 132 |
| WindowsSandbox.execute | started | Local binding for started in WindowsSandbox.execute; use the enclosing contract and type below. | Return type of monotonic; see its callable contract | Enclosing invocation or class/instance lifetime | 134 |
| WindowsSandbox.execute | native | Local binding for native in WindowsSandbox.execute; use the enclosing contract and type below. | Return type of NativeWindows; see its callable contract | Enclosing invocation or class/instance lifetime | 137 |
| WindowsSandbox.execute | sid | Managed resource for sid in WindowsSandbox.execute; use the enclosing contract and type below. | Return type of profile; see its callable contract | Context-manager block; exit invokes its cleanup protocol | 138 |
| WindowsSandbox.execute | sid_text | Managed resource for sid text in WindowsSandbox.execute; use the enclosing contract and type below. | Return type of profile; see its callable contract | Context-manager block; exit invokes its cleanup protocol | 138 |
| WindowsSandbox.execute | temporary | Managed resource for temporary in WindowsSandbox.execute; use the enclosing contract and type below. | Return type of TemporaryDirectory; see its callable contract | Context-manager block; exit invokes its cleanup protocol | 138 |
| WindowsSandbox.execute | root | Explicit root directory against which named paths are resolved. | Return type of Path; see its callable contract | Enclosing invocation or class/instance lifetime | 142 |
| WindowsSandbox.execute | runtime | Explicitly composed application services for one owner or compatibility facade. | tuple | Enclosing invocation or class/instance lifetime | 143 |
| WindowsSandbox.execute | work | Local binding for work in WindowsSandbox.execute; use the enclosing contract and type below. | tuple | Enclosing invocation or class/instance lifetime | 143 |
| WindowsSandbox.execute | request | Local binding for request in WindowsSandbox.execute; use the enclosing contract and type below. | Return type of dict; see its callable contract | Enclosing invocation or class/instance lifetime | 151 |
| WindowsSandbox.execute | icacls | Local binding for icacls in WindowsSandbox.execute; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 160 |
| WindowsSandbox.execute | grant | Local binding for grant in WindowsSandbox.execute; use the enclosing contract and type below. | Return type of run; see its callable contract | Enclosing invocation or class/instance lifetime | 161 |
| WindowsSandbox.execute | executable | Local binding for executable in WindowsSandbox.execute; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 170 |
| WindowsSandbox.execute | command | Local binding for command in WindowsSandbox.execute; use the enclosing contract and type below. | Return type of list2cmdline; see its callable contract | Enclosing invocation or class/instance lifetime | 171 |
| WindowsSandbox.execute | exit_code | Local binding for exit code in WindowsSandbox.execute; use the enclosing contract and type below. | Return type of run; see its callable contract | Enclosing invocation or class/instance lifetime | 174 |
| WindowsSandbox.execute | output | Local binding for output in WindowsSandbox.execute; use the enclosing contract and type below. | Return type of run; see its callable contract | Enclosing invocation or class/instance lifetime | 174 |
| WindowsSandbox.execute | failure | Local binding for failure in WindowsSandbox.execute; use the enclosing contract and type below. | Return type of run; see its callable contract | Enclosing invocation or class/instance lifetime | 174, 190 |
| WindowsSandbox.execute | decoded | Local binding for decoded in WindowsSandbox.execute; use the enclosing contract and type below. | Return type of decode; see its callable contract | Enclosing invocation or class/instance lifetime | 184 |
| WindowsSandbox.execute | report | Local binding for report in WindowsSandbox.execute; use the enclosing contract and type below. | NoneType | Enclosing invocation or class/instance lifetime | 185, 188 |
| WindowsSandbox.execute | result | Intermediate or returned outcome; consult the callable contract for trust/validation. | Return type of SandboxResult; see its callable contract | Enclosing invocation or class/instance lifetime | 191 |
| WindowsSandbox.execute | exc | Caught exception for exc in WindowsSandbox.execute; use the enclosing contract and type below. | Exception | Current exception handler; Python clears this binding afterward | 195 |
| WindowsSandbox.evaluate | self | Owning instance; its attributes retain state for the instance lifetime. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 207 |
| WindowsSandbox.evaluate | code | Source snapshot passed through approval, syntax checks and isolated staging. | bytes | Enclosing invocation or class/instance lifetime | 207 |
| WindowsSandbox.evaluate | tool_name | Validated public tool identifier within the configured storage boundary. | str | Enclosing invocation or class/instance lifetime | 207 |
| WindowsSandbox.evaluate | function_name | Public callable selected for the current operation; empty selects test mode. | str | Enclosing invocation or class/instance lifetime | 207 |
| WindowsSandbox.evaluate | kwargs | Bounded JSON keyword arguments; no executable objects are accepted. | dict[str, Any] | Enclosing invocation or class/instance lifetime | 207 |
| WindowsSandbox._copy_runtime | destination | Parameter for destination in WindowsSandbox._copy_runtime; use the enclosing contract and type below. | Path | Enclosing invocation or class/instance lifetime | 213 |
| WindowsSandbox._copy_runtime | base | Local binding for base in WindowsSandbox._copy_runtime; use the enclosing contract and type below. | Return type of Path; see its callable contract | Enclosing invocation or class/instance lifetime | 215 |
| WindowsSandbox._copy_runtime | filename | Loop item for filename in WindowsSandbox._copy_runtime; use the enclosing contract and type below. | Element of the declared iterable | Enclosing invocation or class/instance lifetime | 217 |
| WindowsSandbox._copy_runtime | ignore | Local binding for ignore in WindowsSandbox._copy_runtime; use the enclosing contract and type below. | Return type of ignore_patterns; see its callable contract | Enclosing invocation or class/instance lifetime | 219 |
| WindowsSandbox._copy_runtime | directory | Loop item for directory in WindowsSandbox._copy_runtime; use the enclosing contract and type below. | Element of the declared iterable | Enclosing invocation or class/instance lifetime | 229 |
