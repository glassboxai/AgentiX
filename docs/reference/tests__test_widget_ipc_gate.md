# Reference for tests/test_widget_ipc_gate.py

LAB-003 native local named-pipe transport prerequisite; no model or host fallback.

Source fingerprint: 26c285ffc0b4693ebe5c2f9f3abed9d16e843ae6cdce0bca12f59ee0136e4162

This reference is generated from maintained source without imports or execution. Assigned values are intentionally omitted. Runtime-dependent types are explicit; the enclosing docstring defines the behavioral contract. See [architecture](../ARCHITECTURE_QUALITY.md) for manually reviewed responsibility and dependency decisions.

## Classes and callables

### test_appcontainer_duplex_named_pipe_round_trip

Require real typed host-child exchange through a profile-scoped local pipe.

Kind: callable. Declared return: Not declared / class. Source line: 24.

### test_appcontainer_duplex_named_pipe_round_trip.run

Own native child handles; job kills all descendants on exit or deadline.

Kind: callable. Declared return: Not declared / class. Source line: 99.

### test_appcontainer_duplex_inherited_pipe_round_trip

Require profile-independent duplex IPC via explicit inherited pipe handles.

Kind: callable. Declared return: Not declared / class. Source line: 186.

### test_appcontainer_duplex_inherited_pipe_round_trip.run

Execute through the same verified token/job lifecycle as ordinary tools.

Kind: callable. Declared return: Not declared / class. Source line: 236.

## Variables and parameters

| Scope | Name | Role and meaning | Type | Lifetime | Writes |
| --- | --- | --- | --- | --- | --- |
| module | ctypes | Imported dependency for ctypes in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 3 |
| module | json | Imported dependency for json in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 4 |
| module | subprocess | Imported dependency for subprocess in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 5 |
| module | tempfile | Imported dependency for tempfile in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 6 |
| module | threading | Imported dependency for threading in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 7 |
| module | wintypes | Imported dependency for wintypes in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 8 |
| module | Path | Imported dependency for Path in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 9 |
| module | uuid4 | Imported dependency for uuid4 in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 10 |
| module | pytest | Imported dependency for pytest in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 12 |
| module | WindowsSandbox | Imported dependency for WindowsSandbox in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 14 |
| module | NativeWindows | Imported dependency for NativeWindows in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 15 |
| test_appcontainer_duplex_named_pipe_round_trip | pywintypes | Imported dependency for pywintypes in test_appcontainer_duplex_named_pipe_round_trip; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 26 |
| test_appcontainer_duplex_named_pipe_round_trip | win32api | Imported dependency for win32api in test_appcontainer_duplex_named_pipe_round_trip; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 27 |
| test_appcontainer_duplex_named_pipe_round_trip | win32con | Imported dependency for win32con in test_appcontainer_duplex_named_pipe_round_trip; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 28 |
| test_appcontainer_duplex_named_pipe_round_trip | win32event | Imported dependency for win32event in test_appcontainer_duplex_named_pipe_round_trip; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 29 |
| test_appcontainer_duplex_named_pipe_round_trip | win32file | Imported dependency for win32file in test_appcontainer_duplex_named_pipe_round_trip; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 30 |
| test_appcontainer_duplex_named_pipe_round_trip | win32pipe | Imported dependency for win32pipe in test_appcontainer_duplex_named_pipe_round_trip; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 31 |
| test_appcontainer_duplex_named_pipe_round_trip | win32security | Imported dependency for win32security in test_appcontainer_duplex_named_pipe_round_trip; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 32 |
| test_appcontainer_duplex_named_pipe_round_trip | native | Local binding for native in test_appcontainer_duplex_named_pipe_round_trip; use the enclosing contract and type below. | Return type of NativeWindows; see its callable contract | Enclosing invocation or class/instance lifetime | 34 |
| test_appcontainer_duplex_named_pipe_round_trip | sid | Managed resource for sid in test_appcontainer_duplex_named_pipe_round_trip; use the enclosing contract and type below. | Return type of profile; see its callable contract | Context-manager block; exit invokes its cleanup protocol | 35 |
| test_appcontainer_duplex_named_pipe_round_trip | sid_text | Managed resource for sid text in test_appcontainer_duplex_named_pipe_round_trip; use the enclosing contract and type below. | Return type of profile; see its callable contract | Context-manager block; exit invokes its cleanup protocol | 35 |
| test_appcontainer_duplex_named_pipe_round_trip | temporary | Managed resource for temporary in test_appcontainer_duplex_named_pipe_round_trip; use the enclosing contract and type below. | Return type of TemporaryDirectory; see its callable contract | Context-manager block; exit invokes its cleanup protocol | 35 |
| test_appcontainer_duplex_named_pipe_round_trip | root | Explicit root directory against which named paths are resolved. | Return type of Path; see its callable contract | Enclosing invocation or class/instance lifetime | 39 |
| test_appcontainer_duplex_named_pipe_round_trip | runtime | Explicitly composed application services for one owner or compatibility facade. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 40 |
| test_appcontainer_duplex_named_pipe_round_trip | pipe_name | Local binding for pipe name in test_appcontainer_duplex_named_pipe_round_trip; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 43 |
| test_appcontainer_duplex_named_pipe_round_trip | token | Local binding for token in test_appcontainer_duplex_named_pipe_round_trip; use the enclosing contract and type below. | Return type of OpenProcessToken; see its callable contract | Enclosing invocation or class/instance lifetime | 44 |
| test_appcontainer_duplex_named_pipe_round_trip | owner | Local binding for owner in test_appcontainer_duplex_named_pipe_round_trip; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 46 |
| test_appcontainer_duplex_named_pipe_round_trip | owner_text | Local binding for owner text in test_appcontainer_duplex_named_pipe_round_trip; use the enclosing contract and type below. | Return type of ConvertSidToStringSid; see its callable contract | Enclosing invocation or class/instance lifetime | 47 |
| test_appcontainer_duplex_named_pipe_round_trip | descriptor | Local binding for descriptor in test_appcontainer_duplex_named_pipe_round_trip; use the enclosing contract and type below. | Return type of ConvertStringSecurityDescriptorToSecurityDescriptor; see its callable contract | Enclosing invocation or class/instance lifetime | 50 |
| test_appcontainer_duplex_named_pipe_round_trip | attributes | Local binding for attributes in test_appcontainer_duplex_named_pipe_round_trip; use the enclosing contract and type below. | Return type of SECURITY_ATTRIBUTES; see its callable contract | Enclosing invocation or class/instance lifetime | 53 |
| test_appcontainer_duplex_named_pipe_round_trip | attributes.SECURITY_DESCRIPTOR | Attribute for attributes.SECURITY DESCRIPTOR in test_appcontainer_duplex_named_pipe_round_trip; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 54 |
| test_appcontainer_duplex_named_pipe_round_trip | pipe | Local binding for pipe in test_appcontainer_duplex_named_pipe_round_trip; use the enclosing contract and type below. | Return type of CreateNamedPipe; see its callable contract | Enclosing invocation or class/instance lifetime | 55 |
| test_appcontainer_duplex_named_pipe_round_trip | source | Explicit source document or source-code text; never imported for reference generation. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 65 |
| test_appcontainer_duplex_named_pipe_round_trip | worker | Local binding for worker in test_appcontainer_duplex_named_pipe_round_trip; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 81 |
| test_appcontainer_duplex_named_pipe_round_trip | grant | Local binding for grant in test_appcontainer_duplex_named_pipe_round_trip; use the enclosing contract and type below. | Return type of run; see its callable contract | Enclosing invocation or class/instance lifetime | 83 |
| test_appcontainer_duplex_named_pipe_round_trip | observation | Local binding for observation in test_appcontainer_duplex_named_pipe_round_trip; use the enclosing contract and type below. | dict | Enclosing invocation or class/instance lifetime | 97 |
| test_appcontainer_duplex_named_pipe_round_trip.run | error | Caught exception for error in test_appcontainer_duplex_named_pipe_round_trip.run; use the enclosing contract and type below. | Exception | Current exception handler; Python clears this binding afterward | 114 |
| test_appcontainer_duplex_named_pipe_round_trip | connect | Local binding for connect in test_appcontainer_duplex_named_pipe_round_trip; use the enclosing contract and type below. | Return type of OVERLAPPED; see its callable contract | Enclosing invocation or class/instance lifetime | 117 |
| test_appcontainer_duplex_named_pipe_round_trip | connect.hEvent | Attribute for connect.hEvent in test_appcontainer_duplex_named_pipe_round_trip; use the enclosing contract and type below. | Return type of CreateEvent; see its callable contract | Enclosing invocation or class/instance lifetime | 118 |
| test_appcontainer_duplex_named_pipe_round_trip | connected | Local binding for connected in test_appcontainer_duplex_named_pipe_round_trip; use the enclosing contract and type below. | bool | Enclosing invocation or class/instance lifetime | 119, 128 |
| test_appcontainer_duplex_named_pipe_round_trip | thread | Local binding for thread in test_appcontainer_duplex_named_pipe_round_trip; use the enclosing contract and type below. | Return type of Thread; see its callable contract | Enclosing invocation or class/instance lifetime | 120 |
| test_appcontainer_duplex_named_pipe_round_trip | error | Caught exception for error in test_appcontainer_duplex_named_pipe_round_trip; use the enclosing contract and type below. | pywintypes.error | Current exception handler; Python clears this binding afterward | 124 |
| test_appcontainer_duplex_named_pipe_round_trip | read | Local binding for read in test_appcontainer_duplex_named_pipe_round_trip; use the enclosing contract and type below. | Return type of OVERLAPPED; see its callable contract | Enclosing invocation or class/instance lifetime | 132 |
| test_appcontainer_duplex_named_pipe_round_trip | read.hEvent | Attribute for read.hEvent in test_appcontainer_duplex_named_pipe_round_trip; use the enclosing contract and type below. | Return type of CreateEvent; see its callable contract | Enclosing invocation or class/instance lifetime | 133 |
| test_appcontainer_duplex_named_pipe_round_trip | _ | Local binding for  in test_appcontainer_duplex_named_pipe_round_trip; use the enclosing contract and type below. | Return type of ReadFile; see its callable contract | Enclosing invocation or class/instance lifetime | 135 |
| test_appcontainer_duplex_named_pipe_round_trip | data | Local binding for data in test_appcontainer_duplex_named_pipe_round_trip; use the enclosing contract and type below. | Return type of ReadFile; see its callable contract | Enclosing invocation or class/instance lifetime | 135 |
| test_appcontainer_duplex_named_pipe_round_trip | count | Local binding for count in test_appcontainer_duplex_named_pipe_round_trip; use the enclosing contract and type below. | Return type of GetOverlappedResult; see its callable contract | Enclosing invocation or class/instance lifetime | 141 |
| test_appcontainer_duplex_named_pipe_round_trip | write | Local binding for write in test_appcontainer_duplex_named_pipe_round_trip; use the enclosing contract and type below. | Return type of OVERLAPPED; see its callable contract | Enclosing invocation or class/instance lifetime | 145 |
| test_appcontainer_duplex_named_pipe_round_trip | write.hEvent | Attribute for write.hEvent in test_appcontainer_duplex_named_pipe_round_trip; use the enclosing contract and type below. | Return type of CreateEvent; see its callable contract | Enclosing invocation or class/instance lifetime | 146 |
| test_appcontainer_duplex_named_pipe_round_trip.lambda_172 | value | Value at the current validation/rendering boundary; apply the enclosing contract. | Defined by the enclosing callback contract | Enclosing invocation or class/instance lifetime | 172 |
| test_appcontainer_duplex_inherited_pipe_round_trip | time | Imported dependency for time in test_appcontainer_duplex_inherited_pipe_round_trip; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 188 |
| test_appcontainer_duplex_inherited_pipe_round_trip | pywintypes | Imported dependency for pywintypes in test_appcontainer_duplex_inherited_pipe_round_trip; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 190 |
| test_appcontainer_duplex_inherited_pipe_round_trip | win32api | Imported dependency for win32api in test_appcontainer_duplex_inherited_pipe_round_trip; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 191 |
| test_appcontainer_duplex_inherited_pipe_round_trip | win32con | Imported dependency for win32con in test_appcontainer_duplex_inherited_pipe_round_trip; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 192 |
| test_appcontainer_duplex_inherited_pipe_round_trip | win32file | Imported dependency for win32file in test_appcontainer_duplex_inherited_pipe_round_trip; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 193 |
| test_appcontainer_duplex_inherited_pipe_round_trip | win32pipe | Imported dependency for win32pipe in test_appcontainer_duplex_inherited_pipe_round_trip; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 194 |
| test_appcontainer_duplex_inherited_pipe_round_trip | native | Local binding for native in test_appcontainer_duplex_inherited_pipe_round_trip; use the enclosing contract and type below. | Return type of NativeWindows; see its callable contract | Enclosing invocation or class/instance lifetime | 196 |
| test_appcontainer_duplex_inherited_pipe_round_trip | attributes | Local binding for attributes in test_appcontainer_duplex_inherited_pipe_round_trip; use the enclosing contract and type below. | Return type of SECURITY_ATTRIBUTES; see its callable contract | Enclosing invocation or class/instance lifetime | 197 |
| test_appcontainer_duplex_inherited_pipe_round_trip | attributes.bInheritHandle | Attribute for attributes.bInheritHandle in test_appcontainer_duplex_inherited_pipe_round_trip; use the enclosing contract and type below. | bool | Enclosing invocation or class/instance lifetime | 198 |
| test_appcontainer_duplex_inherited_pipe_round_trip | child_read | Local binding for child read in test_appcontainer_duplex_inherited_pipe_round_trip; use the enclosing contract and type below. | Return type of CreatePipe; see its callable contract | Enclosing invocation or class/instance lifetime | 199 |
| test_appcontainer_duplex_inherited_pipe_round_trip | host_write | Local binding for host write in test_appcontainer_duplex_inherited_pipe_round_trip; use the enclosing contract and type below. | Return type of CreatePipe; see its callable contract | Enclosing invocation or class/instance lifetime | 199 |
| test_appcontainer_duplex_inherited_pipe_round_trip | host_read | Local binding for host read in test_appcontainer_duplex_inherited_pipe_round_trip; use the enclosing contract and type below. | Return type of CreatePipe; see its callable contract | Enclosing invocation or class/instance lifetime | 200 |
| test_appcontainer_duplex_inherited_pipe_round_trip | child_write | Local binding for child write in test_appcontainer_duplex_inherited_pipe_round_trip; use the enclosing contract and type below. | Return type of CreatePipe; see its callable contract | Enclosing invocation or class/instance lifetime | 200 |
| test_appcontainer_duplex_inherited_pipe_round_trip | handle | Loop item for handle in test_appcontainer_duplex_inherited_pipe_round_trip; use the enclosing contract and type below. | Element of the declared iterable | Enclosing invocation or class/instance lifetime | 201, 271 |
| test_appcontainer_duplex_inherited_pipe_round_trip | sid | Managed resource for sid in test_appcontainer_duplex_inherited_pipe_round_trip; use the enclosing contract and type below. | Return type of profile; see its callable contract | Context-manager block; exit invokes its cleanup protocol | 203 |
| test_appcontainer_duplex_inherited_pipe_round_trip | sid_text | Managed resource for sid text in test_appcontainer_duplex_inherited_pipe_round_trip; use the enclosing contract and type below. | Return type of profile; see its callable contract | Context-manager block; exit invokes its cleanup protocol | 203 |
| test_appcontainer_duplex_inherited_pipe_round_trip | temporary | Managed resource for temporary in test_appcontainer_duplex_inherited_pipe_round_trip; use the enclosing contract and type below. | Return type of TemporaryDirectory; see its callable contract | Context-manager block; exit invokes its cleanup protocol | 203 |
| test_appcontainer_duplex_inherited_pipe_round_trip | root | Explicit root directory against which named paths are resolved. | Return type of Path; see its callable contract | Enclosing invocation or class/instance lifetime | 207 |
| test_appcontainer_duplex_inherited_pipe_round_trip | runtime | Explicitly composed application services for one owner or compatibility facade. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 208 |
| test_appcontainer_duplex_inherited_pipe_round_trip | worker | Local binding for worker in test_appcontainer_duplex_inherited_pipe_round_trip; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 211 |
| test_appcontainer_duplex_inherited_pipe_round_trip | grant | Local binding for grant in test_appcontainer_duplex_inherited_pipe_round_trip; use the enclosing contract and type below. | Return type of run; see its callable contract | Enclosing invocation or class/instance lifetime | 219 |
| test_appcontainer_duplex_inherited_pipe_round_trip | observation | Local binding for observation in test_appcontainer_duplex_inherited_pipe_round_trip; use the enclosing contract and type below. | dict | Enclosing invocation or class/instance lifetime | 234 |
| test_appcontainer_duplex_inherited_pipe_round_trip.run | error | Caught exception for error in test_appcontainer_duplex_inherited_pipe_round_trip.run; use the enclosing contract and type below. | Exception | Current exception handler; Python clears this binding afterward | 252 |
| test_appcontainer_duplex_inherited_pipe_round_trip | thread | Local binding for thread in test_appcontainer_duplex_inherited_pipe_round_trip; use the enclosing contract and type below. | Return type of Thread; see its callable contract | Enclosing invocation or class/instance lifetime | 255 |
| test_appcontainer_duplex_inherited_pipe_round_trip | response | Bounded response text to render or validate; it is not executable code. | bytes | Enclosing invocation or class/instance lifetime | 257, 264 |
| test_appcontainer_duplex_inherited_pipe_round_trip | deadline | Local binding for deadline in test_appcontainer_duplex_inherited_pipe_round_trip; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 260 |
| test_appcontainer_duplex_inherited_pipe_round_trip | available | Local binding for available in test_appcontainer_duplex_inherited_pipe_round_trip; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 262 |
| test_appcontainer_duplex_inherited_pipe_round_trip.lambda_280 | value | Value at the current validation/rendering boundary; apply the enclosing contract. | Defined by the enclosing callback contract | Enclosing invocation or class/instance lifetime | 280 |
