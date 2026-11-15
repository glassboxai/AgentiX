# Reference for src/agentix/sandbox/windows_process.py

Windows AppContainer process lifecycle with explicit native handle ownership.

Imports are inert and portable. Native APIs are loaded only for an explicit run.
No capabilities are granted. A suspended child must have an AppContainer token
and join the limited Job Object before it can execute application code.

Source fingerprint: 4017936059a5002229de44b70f3c891adfe487f12efd1517d1b9e655eab43f5a

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

### NativeWindows._delete_profile

Delete only a previously ownership-checked native profile during recovery.

Kind: callable. Declared return: bool. Source line: 93.

### NativeWindows._process_alive

Treat access-denied and ambiguous process probes as live; never send signals.

Kind: callable. Declared return: bool. Source line: 98.

### NativeWindows.run

Run a restricted child and kill its complete job on failure.

channel_handles optionally contains exactly two supervisor-owned inherited pipe
handles. They are unrelated to standard input/output and do not grant network,
files or token capabilities. The default tool path inherits no extra handles.
The supervisor owns channel framing, deadlines and closing its own handles.

Kind: callable. Declared return: tuple[int, bytes, str]. Source line: 113.

### NativeWindows.run.SecurityAttributes

SECURITY_ATTRIBUTES: only deliberately selected pipe handles inherit.

Kind: class. Declared return: Not declared / class. Source line: 156.

### NativeWindows.run.Startup

STARTUPINFOW ABI including the three standard handle slots.

Kind: class. Declared return: Not declared / class. Source line: 161.

### NativeWindows.run.ExtendedStartup

STARTUPINFOEXW holds the validated capability and handle attributes.

Kind: class. Declared return: Not declared / class. Source line: 185.

### NativeWindows.run.Process

PROCESS_INFORMATION handles owned by this invocation.

Kind: class. Declared return: Not declared / class. Source line: 190.

### NativeWindows.run.Capabilities

SECURITY_CAPABILITIES grants the profile SID and zero capabilities.

Kind: class. Declared return: Not declared / class. Source line: 200.

### NativeWindows.run.BasicLimits

JOBOBJECT_BASIC_LIMIT_INFORMATION with native pointer alignment.

Kind: class. Declared return: Not declared / class. Source line: 210.

### NativeWindows.run.Limits

JOBOBJECT_EXTENDED_LIMIT_INFORMATION for memory/process bounds.

Kind: class. Declared return: Not declared / class. Source line: 225.

### NativeWindows.run.drain

Drain the pipe without allowing child-controlled memory growth.

Kind: callable. Declared return: None. Source line: 408.

## Variables and parameters

| Scope | Name | Role and meaning | Type | Lifetime | Writes |
| --- | --- | --- | --- | --- | --- |
| module | c | Imported dependency for c in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 8 |
| module | os | Imported dependency for os in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 9 |
| module | threading | Imported dependency for threading in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 10 |
| module | Callable | Imported dependency for Callable in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 11 |
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
| NativeWindows.profile | ProfileCleanup | Imported dependency for ProfileCleanup in NativeWindows.profile; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 49 |
| NativeWindows.profile | cleanup | Local binding for cleanup in NativeWindows.profile; use the enclosing contract and type below. | Return type of for_user; see its callable contract | Enclosing invocation or class/instance lifetime | 51 |
| NativeWindows.profile | name | Current identifier selected by parsing, lookup or dependency registration. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 53 |
| NativeWindows.profile | sid | Local binding for sid in NativeWindows.profile; use the enclosing contract and type below. | Return type of c_void_p; see its callable contract | Enclosing invocation or class/instance lifetime | 54 |
| NativeWindows.profile | create | Local binding for create in NativeWindows.profile; use the enclosing contract and type below. | Return type of api; see its callable contract | Enclosing invocation or class/instance lifetime | 55 |
| NativeWindows.profile | status | Local binding for status in NativeWindows.profile; use the enclosing contract and type below. | Return type of create; see its callable contract | Enclosing invocation or class/instance lifetime | 66, 84 |
| NativeWindows.profile | text_sid | Local binding for text sid in NativeWindows.profile; use the enclosing contract and type below. | Return type of LPWSTR; see its callable contract | Enclosing invocation or class/instance lifetime | 71 |
| NativeWindows.profile | tracked | Local binding for tracked in NativeWindows.profile; use the enclosing contract and type below. | bool | Enclosing invocation or class/instance lifetime | 72, 75 |
| NativeWindows.profile | convert | Local binding for convert in NativeWindows.profile; use the enclosing contract and type below. | Return type of api; see its callable contract | Enclosing invocation or class/instance lifetime | 76 |
| NativeWindows.profile | delete | Local binding for delete in NativeWindows.profile; use the enclosing contract and type below. | Return type of api; see its callable contract | Enclosing invocation or class/instance lifetime | 83 |
| NativeWindows._delete_profile | self | Owning instance; its attributes retain state for the instance lifetime. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 93 |
| NativeWindows._delete_profile | name | Current identifier selected by parsing, lookup or dependency registration. | str | Enclosing invocation or class/instance lifetime | 93 |
| NativeWindows._delete_profile | delete | Local binding for delete in NativeWindows._delete_profile; use the enclosing contract and type below. | Return type of api; see its callable contract | Enclosing invocation or class/instance lifetime | 95 |
| NativeWindows._process_alive | self | Owning instance; its attributes retain state for the instance lifetime. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 98 |
| NativeWindows._process_alive | pid | Parameter for pid in NativeWindows._process_alive; use the enclosing contract and type below. | int | Enclosing invocation or class/instance lifetime | 98 |
| NativeWindows._process_alive | probe | Local binding for probe in NativeWindows._process_alive; use the enclosing contract and type below. | Return type of api; see its callable contract | Enclosing invocation or class/instance lifetime | 100 |
| NativeWindows._process_alive | handle | Local binding for handle in NativeWindows._process_alive; use the enclosing contract and type below. | Return type of probe; see its callable contract | Enclosing invocation or class/instance lifetime | 101 |
| NativeWindows._process_alive | code | Source snapshot passed through approval, syntax checks and isolated staging. | Return type of DWORD; see its callable contract | Enclosing invocation or class/instance lifetime | 105 |
| NativeWindows._process_alive | query | Original user request or a trusted test query; avoid payload logging by default. | Return type of api; see its callable contract | Enclosing invocation or class/instance lifetime | 106 |
| NativeWindows.run | self | Owning instance; its attributes retain state for the instance lifetime. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 114 |
| NativeWindows.run | executable | Parameter for executable in NativeWindows.run; use the enclosing contract and type below. | str | Enclosing invocation or class/instance lifetime | 115 |
| NativeWindows.run | command | Parameter for command in NativeWindows.run; use the enclosing contract and type below. | str | Enclosing invocation or class/instance lifetime | 116 |
| NativeWindows.run | cwd | Parameter for cwd in NativeWindows.run; use the enclosing contract and type below. | str | Enclosing invocation or class/instance lifetime | 117 |
| NativeWindows.run | sid | Parameter for sid in NativeWindows.run; use the enclosing contract and type below. | Any | Enclosing invocation or class/instance lifetime | 118 |
| NativeWindows.run | timeout | Parameter for timeout in NativeWindows.run; use the enclosing contract and type below. | float &#124; None | Enclosing invocation or class/instance lifetime | 120 |
| NativeWindows.run | memory | Parameter for memory in NativeWindows.run; use the enclosing contract and type below. | int | Enclosing invocation or class/instance lifetime | 121 |
| NativeWindows.run | processes | Parameter for processes in NativeWindows.run; use the enclosing contract and type below. | int | Enclosing invocation or class/instance lifetime | 122 |
| NativeWindows.run | max_output | Parameter for max output in NativeWindows.run; use the enclosing contract and type below. | int | Enclosing invocation or class/instance lifetime | 123 |
| NativeWindows.run | channel_handles | Parameter for channel handles in NativeWindows.run; use the enclosing contract and type below. | tuple[int, ...] | Enclosing invocation or class/instance lifetime | 124 |
| NativeWindows.run | on_started | Parameter for on started in NativeWindows.run; use the enclosing contract and type below. | Callable[[], None] &#124; None | Enclosing invocation or class/instance lifetime | 125 |
| NativeWindows.run | cancel_event | Parameter for cancel event in NativeWindows.run; use the enclosing contract and type below. | threading.Event &#124; None | Enclosing invocation or class/instance lifetime | 126 |
| NativeWindows.run.comprehension_139 | handle | Comprehension item for handle in NativeWindows.run.comprehension_139; use the enclosing contract and type below. | Element of the declared iterable | This comprehension only; does not leak into its enclosing scope | 139 |
| NativeWindows.run | handle | Loop item for handle in NativeWindows.run; use the enclosing contract and type below. | Element of the declared iterable | Enclosing invocation or class/instance lifetime | 143 |
| NativeWindows.run | kind | Local binding for kind in NativeWindows.run; use the enclosing contract and type below. | Return type of callable; see its callable contract | Enclosing invocation or class/instance lifetime | 144 |
| NativeWindows.run | flags | Local binding for flags in NativeWindows.run; use the enclosing contract and type below. | Return type of DWORD; see its callable contract | Enclosing invocation or class/instance lifetime | 145 |
| NativeWindows.run.SecurityAttributes | _fields_ | Local binding for fields in NativeWindows.run.SecurityAttributes; use the enclosing contract and type below. | list | Enclosing invocation or class/instance lifetime | 159 |
| NativeWindows.run.Startup | _fields_ | Local binding for fields in NativeWindows.run.Startup; use the enclosing contract and type below. | list | Enclosing invocation or class/instance lifetime | 164 |
| NativeWindows.run.ExtendedStartup | _fields_ | Local binding for fields in NativeWindows.run.ExtendedStartup; use the enclosing contract and type below. | list | Enclosing invocation or class/instance lifetime | 188 |
| NativeWindows.run.Process | _fields_ | Local binding for fields in NativeWindows.run.Process; use the enclosing contract and type below. | list | Enclosing invocation or class/instance lifetime | 193 |
| NativeWindows.run.Capabilities | _fields_ | Local binding for fields in NativeWindows.run.Capabilities; use the enclosing contract and type below. | list | Enclosing invocation or class/instance lifetime | 203 |
| NativeWindows.run.BasicLimits | _fields_ | Local binding for fields in NativeWindows.run.BasicLimits; use the enclosing contract and type below. | list | Enclosing invocation or class/instance lifetime | 213 |
| NativeWindows.run.Limits | _fields_ | Local binding for fields in NativeWindows.run.Limits; use the enclosing contract and type below. | list | Enclosing invocation or class/instance lifetime | 228 |
| NativeWindows.run | kernel | Local binding for kernel in NativeWindows.run; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 237 |
| NativeWindows.run | close | Local binding for close in NativeWindows.run; use the enclosing contract and type below. | Return type of api; see its callable contract | Enclosing invocation or class/instance lifetime | 238 |
| NativeWindows.run | job | Local binding for job in NativeWindows.run; use the enclosing contract and type below. | Return type of checked; see its callable contract | Enclosing invocation or class/instance lifetime | 239 |
| NativeWindows.run | limits | Local binding for limits in NativeWindows.run; use the enclosing contract and type below. | Return type of Limits; see its callable contract | Enclosing invocation or class/instance lifetime | 243 |
| NativeWindows.run | limits.basic.flags | Attribute for limits.basic.flags in NativeWindows.run; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 244 |
| NativeWindows.run | limits.basic.processes | Attribute for limits.basic.processes in NativeWindows.run; use the enclosing contract and type below. | tuple | Enclosing invocation or class/instance lifetime | 245 |
| NativeWindows.run | limits.job_memory | Attribute for limits.job memory in NativeWindows.run; use the enclosing contract and type below. | tuple | Enclosing invocation or class/instance lifetime | 245 |
| NativeWindows.run | read | Local binding for read in NativeWindows.run; use the enclosing contract and type below. | tuple | Enclosing invocation or class/instance lifetime | 251 |
| NativeWindows.run | write | Local binding for write in NativeWindows.run; use the enclosing contract and type below. | tuple | Enclosing invocation or class/instance lifetime | 251 |
| NativeWindows.run | attrs | Local binding for attrs in NativeWindows.run; use the enclosing contract and type below. | Return type of SecurityAttributes; see its callable contract | Enclosing invocation or class/instance lifetime | 252 |
| NativeWindows.run | nul | Local binding for nul in NativeWindows.run; use the enclosing contract and type below. | Return type of callable; see its callable contract | Enclosing invocation or class/instance lifetime | 268 |
| NativeWindows.run | size | Local binding for size in NativeWindows.run; use the enclosing contract and type below. | Return type of c_size_t; see its callable contract | Enclosing invocation or class/instance lifetime | 283 |
| NativeWindows.run | init | Local binding for init in NativeWindows.run; use the enclosing contract and type below. | Return type of api; see its callable contract | Enclosing invocation or class/instance lifetime | 284 |
| NativeWindows.run | buffer | Local binding for buffer in NativeWindows.run; use the enclosing contract and type below. | Return type of create_string_buffer; see its callable contract | Enclosing invocation or class/instance lifetime | 294 |
| NativeWindows.run | process | Local binding for process in NativeWindows.run; use the enclosing contract and type below. | Return type of Process; see its callable contract | Enclosing invocation or class/instance lifetime | 296 |
| NativeWindows.run | reader | Local binding for reader in NativeWindows.run; use the enclosing contract and type below. | NoneType | Enclosing invocation or class/instance lifetime | 297, 419 |
| NativeWindows.run | output | Local binding for output in NativeWindows.run; use the enclosing contract and type below. | Return type of bytearray; see its callable contract | Enclosing invocation or class/instance lifetime | 298 |
| NativeWindows.run | excessive | Local binding for excessive in NativeWindows.run; use the enclosing contract and type below. | Return type of Event; see its callable contract | Enclosing invocation or class/instance lifetime | 299 |
| NativeWindows.run | terminate | Local binding for terminate in NativeWindows.run; use the enclosing contract and type below. | Return type of api; see its callable contract | Enclosing invocation or class/instance lifetime | 300 |
| NativeWindows.run | update | Local binding for update in NativeWindows.run; use the enclosing contract and type below. | Return type of api; see its callable contract | Enclosing invocation or class/instance lifetime | 302 |
| NativeWindows.run | caps | Local binding for caps in NativeWindows.run; use the enclosing contract and type below. | Return type of Capabilities; see its callable contract | Enclosing invocation or class/instance lifetime | 314 |
| NativeWindows.run | inherited | Local binding for inherited in NativeWindows.run; use the enclosing contract and type below. | Return type of callable; see its callable contract | Enclosing invocation or class/instance lifetime | 316 |
| NativeWindows.run | startup | Local binding for startup in NativeWindows.run; use the enclosing contract and type below. | Return type of ExtendedStartup; see its callable contract | Enclosing invocation or class/instance lifetime | 318 |
| NativeWindows.run | startup.startup.cb | Attribute for startup.startup.cb in NativeWindows.run; use the enclosing contract and type below. | Return type of sizeof; see its callable contract | Enclosing invocation or class/instance lifetime | 319 |
| NativeWindows.run | startup.startup.flags | Attribute for startup.startup.flags in NativeWindows.run; use the enclosing contract and type below. | int | Enclosing invocation or class/instance lifetime | 320 |
| NativeWindows.run | startup.startup.stdin | Attribute for startup.startup.stdin in NativeWindows.run; use the enclosing contract and type below. | tuple | Enclosing invocation or class/instance lifetime | 321 |
| NativeWindows.run | startup.startup.stdout | Attribute for startup.startup.stdout in NativeWindows.run; use the enclosing contract and type below. | tuple | Enclosing invocation or class/instance lifetime | 321 |
| NativeWindows.run | startup.startup.stderr | Attribute for startup.startup.stderr in NativeWindows.run; use the enclosing contract and type below. | tuple | Enclosing invocation or class/instance lifetime | 321 |
| NativeWindows.run | startup.attributes | Attribute for startup.attributes in NativeWindows.run; use the enclosing contract and type below. | Return type of cast; see its callable contract | Enclosing invocation or class/instance lifetime | 326 |
| NativeWindows.run | root | Explicit root directory against which named paths are resolved. | Return type of get; see its callable contract | Enclosing invocation or class/instance lifetime | 328 |
| NativeWindows.run | local_app_data | Local binding for local app data in NativeWindows.run; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 333 |
| NativeWindows.run | environment | Local binding for environment in NativeWindows.run; use the enclosing contract and type below. | Return type of create_unicode_buffer; see its callable contract | Enclosing invocation or class/instance lifetime | 334 |
| NativeWindows.run | create | Local binding for create in NativeWindows.run; use the enclosing contract and type below. | Return type of api; see its callable contract | Enclosing invocation or class/instance lifetime | 337 |
| NativeWindows.run | token | Local binding for token in NativeWindows.run; use the enclosing contract and type below. | Return type of HANDLE; see its callable contract | Enclosing invocation or class/instance lifetime | 368 |
| NativeWindows.run | is_container | Local binding for is container in NativeWindows.run; use the enclosing contract and type below. | tuple | Enclosing invocation or class/instance lifetime | 375 |
| NativeWindows.run | returned | Local binding for returned in NativeWindows.run; use the enclosing contract and type below. | tuple | Enclosing invocation or class/instance lifetime | 375 |
| NativeWindows.run | read_file | Local binding for read file in NativeWindows.run; use the enclosing contract and type below. | Return type of api; see its callable contract | Enclosing invocation or class/instance lifetime | 397 |
| NativeWindows.run.drain | chunk | Local binding for chunk in NativeWindows.run.drain; use the enclosing contract and type below. | tuple | Enclosing invocation or class/instance lifetime | 410 |
| NativeWindows.run.drain | count | Local binding for count in NativeWindows.run.drain; use the enclosing contract and type below. | tuple | Enclosing invocation or class/instance lifetime | 410 |
| NativeWindows.run.drain | available | Local binding for available in NativeWindows.run.drain; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 412 |
| NativeWindows.run | resume | Local binding for resume in NativeWindows.run; use the enclosing contract and type below. | Return type of callable; see its callable contract | Enclosing invocation or class/instance lifetime | 421 |
| NativeWindows.run | wait | Local binding for wait in NativeWindows.run; use the enclosing contract and type below. | Return type of api; see its callable contract | Enclosing invocation or class/instance lifetime | 429 |
| NativeWindows.run | status | Local binding for status in NativeWindows.run; use the enclosing contract and type below. | Return type of wait; see its callable contract | Enclosing invocation or class/instance lifetime | 431, 436, 440, 444 |
| NativeWindows.run | time | Imported dependency for time in NativeWindows.run; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 433 |
| NativeWindows.run | deadline | Local binding for deadline in NativeWindows.run; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 435 |
| NativeWindows.run | failure | Local binding for failure in NativeWindows.run; use the enclosing contract and type below. | str | Enclosing invocation or class/instance lifetime | 445, 447, 451, 456, 458 |
| NativeWindows.run | exit_code | Local binding for exit code in NativeWindows.run; use the enclosing contract and type below. | Return type of DWORD; see its callable contract | Enclosing invocation or class/instance lifetime | 459 |
