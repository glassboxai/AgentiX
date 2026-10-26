# Reference for src/agentix/windows_process.py

Windows AppContainer process lifecycle with explicit native handle ownership.

Imports are inert and portable. Native APIs are loaded only for an explicit run.
No capabilities are granted. A suspended child must have an AppContainer token
and join the limited Job Object before it can execute application code.

Source fingerprint: 3f7905930df298aff696338b1fa10f9f79e3c3eb9d1f1742f853384920665cae

This reference is generated from maintained source without imports or execution. Assigned values are intentionally omitted. Runtime-dependent types are explicit; the enclosing docstring defines the behavioral contract. See [architecture](../ARCHITECTURE_QUALITY.md) for manually reviewed responsibility and dependency decisions.

## Classes and callables

### NativeWindows

Own typed Win32 functions; fail on every unsuccessful security operation.

Kind: class. Declared return: Not declared / class. Source line: 18.

### NativeWindows.__init__

Load native libraries without modifying system or user policy.

Kind: callable. Declared return: None. Source line: 21.

### NativeWindows.api

Declare ABI widths explicitly, including pointer-sized handles.

Kind: callable. Declared return: Any. Source line: 28.

### NativeWindows.checked

Raise a native error without continuing with weakened restrictions.

Kind: callable. Declared return: Any. Source line: 34.

### NativeWindows.close

Close owned handles in reverse order; closing the job kills descendants.

Kind: callable. Declared return: None. Source line: 40.

### NativeWindows.profile

Create a unique no-capability profile, then delete it and free its SID.

Kind: callable. Declared return: Iterator[tuple[Any, str]]. Source line: 47.

### NativeWindows.run

Run a restricted child with bounded pipes and kill the complete job on failure.

Kind: callable. Declared return: tuple[int, bytes, str]. Source line: 84.

### NativeWindows.run.SecurityAttributes

SECURITY_ATTRIBUTES: only deliberately selected pipe handles inherit.

Kind: class. Declared return: Not declared / class. Source line: 100.

### NativeWindows.run.Startup

STARTUPINFOW ABI including the three standard handle slots.

Kind: class. Declared return: Not declared / class. Source line: 105.

### NativeWindows.run.ExtendedStartup

STARTUPINFOEXW holds the validated capability and handle attributes.

Kind: class. Declared return: Not declared / class. Source line: 129.

### NativeWindows.run.Process

PROCESS_INFORMATION handles owned by this invocation.

Kind: class. Declared return: Not declared / class. Source line: 134.

### NativeWindows.run.Capabilities

SECURITY_CAPABILITIES grants the profile SID and zero capabilities.

Kind: class. Declared return: Not declared / class. Source line: 144.

### NativeWindows.run.BasicLimits

JOBOBJECT_BASIC_LIMIT_INFORMATION with native pointer alignment.

Kind: class. Declared return: Not declared / class. Source line: 154.

### NativeWindows.run.Limits

JOBOBJECT_EXTENDED_LIMIT_INFORMATION for memory/process bounds.

Kind: class. Declared return: Not declared / class. Source line: 169.

### NativeWindows.run.drain

Drain the pipe without allowing child-controlled memory growth.

Kind: callable. Declared return: None. Source line: 352.

## Variables and parameters

| Scope | Name | Role and meaning | Type | Lifetime | Writes |
| --- | --- | --- | --- | --- | --- |
| module | c | Imported dependency for c in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 8 |
| module | os | Imported dependency for os in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 9 |
| module | threading | Imported dependency for threading in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 10 |
| module | Iterator | Imported dependency for Iterator in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 11 |
| module | contextmanager | Imported dependency for contextmanager in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 12 |
| module | w | Imported dependency for w in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 13 |
| module | Any | Imported dependency for Any in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 14 |
| module | uuid4 | Imported dependency for uuid4 in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 15 |
| NativeWindows.__init__ | self | Owning instance; its attributes retain state for the instance lifetime. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 21 |
| NativeWindows.__init__ | self.kernel | Attribute for kernel in NativeWindows.__init__; use the enclosing contract and type below. | Return type of WinDLL; see its callable contract | Enclosing invocation or class/instance lifetime | 23 |
| NativeWindows.__init__ | self.userenv | Attribute for userenv in NativeWindows.__init__; use the enclosing contract and type below. | Return type of WinDLL; see its callable contract | Enclosing invocation or class/instance lifetime | 24 |
| NativeWindows.__init__ | self.advapi | Attribute for advapi in NativeWindows.__init__; use the enclosing contract and type below. | Return type of WinDLL; see its callable contract | Enclosing invocation or class/instance lifetime | 25 |
| NativeWindows.__init__ | self._handles | Attribute for handles in NativeWindows.__init__; use the enclosing contract and type below. | list[Any] | Enclosing invocation or class/instance lifetime | 26 |
| NativeWindows.api | self | Owning instance; its attributes retain state for the instance lifetime. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 28 |
| NativeWindows.api | library | Parameter for library in NativeWindows.api; use the enclosing contract and type below. | Any | Enclosing invocation or class/instance lifetime | 28 |
| NativeWindows.api | name | Current identifier selected by parsing, lookup or dependency registration. | str | Enclosing invocation or class/instance lifetime | 28 |
| NativeWindows.api | result | Intermediate or returned outcome; consult the callable contract for trust/validation. | Any | Enclosing invocation or class/instance lifetime | 28 |
| NativeWindows.api | arguments | Parameter for arguments in NativeWindows.api; use the enclosing contract and type below. | Any | Enclosing invocation or class/instance lifetime | 28 |
| NativeWindows.api | function | Local binding for function in NativeWindows.api; use the enclosing contract and type below. | Return type of getattr; see its callable contract | Enclosing invocation or class/instance lifetime | 30 |
| NativeWindows.api | function.restype | Attribute for function.restype in NativeWindows.api; use the enclosing contract and type below. | tuple | Enclosing invocation or class/instance lifetime | 31 |
| NativeWindows.api | function.argtypes | Attribute for function.argtypes in NativeWindows.api; use the enclosing contract and type below. | tuple | Enclosing invocation or class/instance lifetime | 31 |
| NativeWindows.checked | self | Owning instance; its attributes retain state for the instance lifetime. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 34 |
| NativeWindows.checked | result | Intermediate or returned outcome; consult the callable contract for trust/validation. | Any | Enclosing invocation or class/instance lifetime | 34 |
| NativeWindows.close | self | Owning instance; its attributes retain state for the instance lifetime. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 40 |
| NativeWindows.close | handle | Loop item for handle in NativeWindows.close; use the enclosing contract and type below. | Element of the declared iterable | Enclosing invocation or class/instance lifetime | 42 |
| NativeWindows.profile | self | Owning instance; its attributes retain state for the instance lifetime. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 47 |
| NativeWindows.profile | name | Current identifier selected by parsing, lookup or dependency registration. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 49 |
| NativeWindows.profile | sid | Local binding for sid in NativeWindows.profile; use the enclosing contract and type below. | Return type of c_void_p; see its callable contract | Enclosing invocation or class/instance lifetime | 50 |
| NativeWindows.profile | create | Local binding for create in NativeWindows.profile; use the enclosing contract and type below. | Return type of api; see its callable contract | Enclosing invocation or class/instance lifetime | 51 |
| NativeWindows.profile | status | Local binding for status in NativeWindows.profile; use the enclosing contract and type below. | Return type of create; see its callable contract | Enclosing invocation or class/instance lifetime | 62, 77 |
| NativeWindows.profile | text_sid | Local binding for text sid in NativeWindows.profile; use the enclosing contract and type below. | Return type of LPWSTR; see its callable contract | Enclosing invocation or class/instance lifetime | 67 |
| NativeWindows.profile | convert | Local binding for convert in NativeWindows.profile; use the enclosing contract and type below. | Return type of api; see its callable contract | Enclosing invocation or class/instance lifetime | 69 |
| NativeWindows.profile | delete | Local binding for delete in NativeWindows.profile; use the enclosing contract and type below. | Return type of api; see its callable contract | Enclosing invocation or class/instance lifetime | 76 |
| NativeWindows.run | self | Owning instance; its attributes retain state for the instance lifetime. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 85 |
| NativeWindows.run | executable | Parameter for executable in NativeWindows.run; use the enclosing contract and type below. | str | Enclosing invocation or class/instance lifetime | 86 |
| NativeWindows.run | command | Parameter for command in NativeWindows.run; use the enclosing contract and type below. | str | Enclosing invocation or class/instance lifetime | 87 |
| NativeWindows.run | cwd | Parameter for cwd in NativeWindows.run; use the enclosing contract and type below. | str | Enclosing invocation or class/instance lifetime | 88 |
| NativeWindows.run | sid | Parameter for sid in NativeWindows.run; use the enclosing contract and type below. | Any | Enclosing invocation or class/instance lifetime | 89 |
| NativeWindows.run | timeout | Parameter for timeout in NativeWindows.run; use the enclosing contract and type below. | float | Enclosing invocation or class/instance lifetime | 91 |
| NativeWindows.run | memory | Parameter for memory in NativeWindows.run; use the enclosing contract and type below. | int | Enclosing invocation or class/instance lifetime | 92 |
| NativeWindows.run | processes | Parameter for processes in NativeWindows.run; use the enclosing contract and type below. | int | Enclosing invocation or class/instance lifetime | 93 |
| NativeWindows.run | max_output | Parameter for max output in NativeWindows.run; use the enclosing contract and type below. | int | Enclosing invocation or class/instance lifetime | 94 |
| NativeWindows.run.SecurityAttributes | _fields_ | Local binding for fields in NativeWindows.run.SecurityAttributes; use the enclosing contract and type below. | list | Enclosing invocation or class/instance lifetime | 103 |
| NativeWindows.run.Startup | _fields_ | Local binding for fields in NativeWindows.run.Startup; use the enclosing contract and type below. | list | Enclosing invocation or class/instance lifetime | 108 |
| NativeWindows.run.ExtendedStartup | _fields_ | Local binding for fields in NativeWindows.run.ExtendedStartup; use the enclosing contract and type below. | list | Enclosing invocation or class/instance lifetime | 132 |
| NativeWindows.run.Process | _fields_ | Local binding for fields in NativeWindows.run.Process; use the enclosing contract and type below. | list | Enclosing invocation or class/instance lifetime | 137 |
| NativeWindows.run.Capabilities | _fields_ | Local binding for fields in NativeWindows.run.Capabilities; use the enclosing contract and type below. | list | Enclosing invocation or class/instance lifetime | 147 |
| NativeWindows.run.BasicLimits | _fields_ | Local binding for fields in NativeWindows.run.BasicLimits; use the enclosing contract and type below. | list | Enclosing invocation or class/instance lifetime | 157 |
| NativeWindows.run.Limits | _fields_ | Local binding for fields in NativeWindows.run.Limits; use the enclosing contract and type below. | list | Enclosing invocation or class/instance lifetime | 172 |
| NativeWindows.run | kernel | Local binding for kernel in NativeWindows.run; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 181 |
| NativeWindows.run | close | Local binding for close in NativeWindows.run; use the enclosing contract and type below. | Return type of api; see its callable contract | Enclosing invocation or class/instance lifetime | 182 |
| NativeWindows.run | job | Local binding for job in NativeWindows.run; use the enclosing contract and type below. | Return type of checked; see its callable contract | Enclosing invocation or class/instance lifetime | 183 |
| NativeWindows.run | limits | Local binding for limits in NativeWindows.run; use the enclosing contract and type below. | Return type of Limits; see its callable contract | Enclosing invocation or class/instance lifetime | 187 |
| NativeWindows.run | limits.basic.flags | Attribute for limits.basic.flags in NativeWindows.run; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 188 |
| NativeWindows.run | limits.basic.processes | Attribute for limits.basic.processes in NativeWindows.run; use the enclosing contract and type below. | tuple | Enclosing invocation or class/instance lifetime | 189 |
| NativeWindows.run | limits.job_memory | Attribute for limits.job memory in NativeWindows.run; use the enclosing contract and type below. | tuple | Enclosing invocation or class/instance lifetime | 189 |
| NativeWindows.run | read | Local binding for read in NativeWindows.run; use the enclosing contract and type below. | tuple | Enclosing invocation or class/instance lifetime | 195 |
| NativeWindows.run | write | Local binding for write in NativeWindows.run; use the enclosing contract and type below. | tuple | Enclosing invocation or class/instance lifetime | 195 |
| NativeWindows.run | attrs | Local binding for attrs in NativeWindows.run; use the enclosing contract and type below. | Return type of SecurityAttributes; see its callable contract | Enclosing invocation or class/instance lifetime | 196 |
| NativeWindows.run | nul | Local binding for nul in NativeWindows.run; use the enclosing contract and type below. | Return type of callable; see its callable contract | Enclosing invocation or class/instance lifetime | 212 |
| NativeWindows.run | size | Local binding for size in NativeWindows.run; use the enclosing contract and type below. | Return type of c_size_t; see its callable contract | Enclosing invocation or class/instance lifetime | 227 |
| NativeWindows.run | init | Local binding for init in NativeWindows.run; use the enclosing contract and type below. | Return type of api; see its callable contract | Enclosing invocation or class/instance lifetime | 228 |
| NativeWindows.run | buffer | Local binding for buffer in NativeWindows.run; use the enclosing contract and type below. | Return type of create_string_buffer; see its callable contract | Enclosing invocation or class/instance lifetime | 238 |
| NativeWindows.run | process | Local binding for process in NativeWindows.run; use the enclosing contract and type below. | Return type of Process; see its callable contract | Enclosing invocation or class/instance lifetime | 240 |
| NativeWindows.run | reader | Local binding for reader in NativeWindows.run; use the enclosing contract and type below. | NoneType | Enclosing invocation or class/instance lifetime | 241, 363 |
| NativeWindows.run | output | Local binding for output in NativeWindows.run; use the enclosing contract and type below. | Return type of bytearray; see its callable contract | Enclosing invocation or class/instance lifetime | 242 |
| NativeWindows.run | excessive | Local binding for excessive in NativeWindows.run; use the enclosing contract and type below. | Return type of Event; see its callable contract | Enclosing invocation or class/instance lifetime | 243 |
| NativeWindows.run | terminate | Local binding for terminate in NativeWindows.run; use the enclosing contract and type below. | Return type of api; see its callable contract | Enclosing invocation or class/instance lifetime | 244 |
| NativeWindows.run | update | Local binding for update in NativeWindows.run; use the enclosing contract and type below. | Return type of api; see its callable contract | Enclosing invocation or class/instance lifetime | 246 |
| NativeWindows.run | caps | Local binding for caps in NativeWindows.run; use the enclosing contract and type below. | Return type of Capabilities; see its callable contract | Enclosing invocation or class/instance lifetime | 258 |
| NativeWindows.run | inherited | Local binding for inherited in NativeWindows.run; use the enclosing contract and type below. | Return type of callable; see its callable contract | Enclosing invocation or class/instance lifetime | 260 |
| NativeWindows.run | startup | Local binding for startup in NativeWindows.run; use the enclosing contract and type below. | Return type of ExtendedStartup; see its callable contract | Enclosing invocation or class/instance lifetime | 262 |
| NativeWindows.run | startup.startup.cb | Attribute for startup.startup.cb in NativeWindows.run; use the enclosing contract and type below. | Return type of sizeof; see its callable contract | Enclosing invocation or class/instance lifetime | 263 |
| NativeWindows.run | startup.startup.flags | Attribute for startup.startup.flags in NativeWindows.run; use the enclosing contract and type below. | int | Enclosing invocation or class/instance lifetime | 264 |
| NativeWindows.run | startup.startup.stdin | Attribute for startup.startup.stdin in NativeWindows.run; use the enclosing contract and type below. | tuple | Enclosing invocation or class/instance lifetime | 265 |
| NativeWindows.run | startup.startup.stdout | Attribute for startup.startup.stdout in NativeWindows.run; use the enclosing contract and type below. | tuple | Enclosing invocation or class/instance lifetime | 265 |
| NativeWindows.run | startup.startup.stderr | Attribute for startup.startup.stderr in NativeWindows.run; use the enclosing contract and type below. | tuple | Enclosing invocation or class/instance lifetime | 265 |
| NativeWindows.run | startup.attributes | Attribute for startup.attributes in NativeWindows.run; use the enclosing contract and type below. | Return type of cast; see its callable contract | Enclosing invocation or class/instance lifetime | 270 |
| NativeWindows.run | root | Explicit root directory against which named paths are resolved. | Return type of get; see its callable contract | Enclosing invocation or class/instance lifetime | 272 |
| NativeWindows.run | local_app_data | Local binding for local app data in NativeWindows.run; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 277 |
| NativeWindows.run | environment | Local binding for environment in NativeWindows.run; use the enclosing contract and type below. | Return type of create_unicode_buffer; see its callable contract | Enclosing invocation or class/instance lifetime | 278 |
| NativeWindows.run | create | Local binding for create in NativeWindows.run; use the enclosing contract and type below. | Return type of api; see its callable contract | Enclosing invocation or class/instance lifetime | 281 |
| NativeWindows.run | token | Local binding for token in NativeWindows.run; use the enclosing contract and type below. | Return type of HANDLE; see its callable contract | Enclosing invocation or class/instance lifetime | 312 |
| NativeWindows.run | is_container | Local binding for is container in NativeWindows.run; use the enclosing contract and type below. | tuple | Enclosing invocation or class/instance lifetime | 319 |
| NativeWindows.run | returned | Local binding for returned in NativeWindows.run; use the enclosing contract and type below. | tuple | Enclosing invocation or class/instance lifetime | 319 |
| NativeWindows.run | read_file | Local binding for read file in NativeWindows.run; use the enclosing contract and type below. | Return type of api; see its callable contract | Enclosing invocation or class/instance lifetime | 341 |
| NativeWindows.run.drain | chunk | Local binding for chunk in NativeWindows.run.drain; use the enclosing contract and type below. | tuple | Enclosing invocation or class/instance lifetime | 354 |
| NativeWindows.run.drain | count | Local binding for count in NativeWindows.run.drain; use the enclosing contract and type below. | tuple | Enclosing invocation or class/instance lifetime | 354 |
| NativeWindows.run.drain | available | Local binding for available in NativeWindows.run.drain; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 356 |
| NativeWindows.run | resume | Local binding for resume in NativeWindows.run; use the enclosing contract and type below. | Return type of callable; see its callable contract | Enclosing invocation or class/instance lifetime | 365 |
| NativeWindows.run | wait | Local binding for wait in NativeWindows.run; use the enclosing contract and type below. | Return type of api; see its callable contract | Enclosing invocation or class/instance lifetime | 371 |
| NativeWindows.run | status | Local binding for status in NativeWindows.run; use the enclosing contract and type below. | Return type of wait; see its callable contract | Enclosing invocation or class/instance lifetime | 372 |
| NativeWindows.run | failure | Local binding for failure in NativeWindows.run; use the enclosing contract and type below. | str | Enclosing invocation or class/instance lifetime | 373, 375, 377, 382, 384 |
| NativeWindows.run | exit_code | Local binding for exit code in NativeWindows.run; use the enclosing contract and type below. | Return type of DWORD; see its callable contract | Enclosing invocation or class/instance lifetime | 385 |
