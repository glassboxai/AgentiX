# Reference for src/agentix/lab/widget_session.py

Supervisor-owned isolated widget session and framed, multiplexed ASGI transport.

Only the fixed maintained worker and approved bytes are staged. The HTTP bridge never
imports the widget. Child network capabilities remain zero. Legacy tool calls get a
second native boundary; application subclasses stage a reviewed direct-call package. Close cancels the complete widget job and closes all channel handles.

Source fingerprint: a476db1ca67882c221fe913ca0338e251d9c297c40f523f57ffc18afed478175

This reference is generated from maintained source without imports or execution. Assigned values are intentionally omitted. Runtime-dependent types are explicit; the enclosing docstring defines the behavioral contract. See [architecture](../ARCHITECTURE_QUALITY.md) for manually reviewed responsibility and dependency decisions.

## Classes and callables

### HttpResult

Host-observed HTTP response, never an execution authorization.

Kind: class. Declared return: Not declared / class. Source line: 35.

### WidgetSession

One finite native worker with private inherited pipes and bounded dispatch.

Kind: class. Declared return: Not declared / class. Source line: 43.

### WidgetSession.__init__

Select maintained reference or explicitly reviewed widget bytes; perform no native IO.

Kind: callable. Declared return: None. Source line: 46.

### WidgetSession.__enter__

Close partial native staging on every startup exception.

Kind: callable. Declared return: 'WidgetSession'. Source line: 78.

### WidgetSession._start

Stage pinned dependencies, create private handles and await native readiness.

Kind: callable. Declared return: 'WidgetSession'. Source line: 95.

### WidgetSession._stage_payload

Stage only the legacy widget capability; subclasses provide reviewed app snapshots.

Kind: callable. Declared return: None. Source line: 153.

### WidgetSession._worker_arguments

Select maintained worker modes without child-controlled command fragments.

Kind: callable. Declared return: list[str]. Source line: 165.

### WidgetSession._control_message

Accept bounded child timing diagnostics, never treating them as host evidence.

Kind: callable. Declared return: bool. Source line: 169.

### WidgetSession._run_native

Own profile/job lifetime and grant only staged runtime plus private scratch.

Kind: callable. Declared return: None. Source line: 184.

### WidgetSession._child_started

Drop parent copies after inheritance so child death produces pipe EOF.

Kind: callable. Declared return: None. Source line: 240.

### WidgetSession._write

Serialize bounded messages; native cancellation breaks stalled pipe operations.

Kind: callable. Declared return: None. Source line: 246.

### WidgetSession._check_runtime

Allow specialized supervisors to enforce operation budgets during idle polling.

Kind: callable. Declared return: None. Source line: 254.

### WidgetSession._read_exact

Poll available pipe bytes under a finite worker lifetime without blocking reads.

Kind: callable. Declared return: bytes. Source line: 257.

### WidgetSession._read_loop

Dispatch only known message types; unknown/oversized frames terminate the job.

Kind: callable. Declared return: None. Source line: 276.

### WidgetSession._invoke_tool

Validate a single reviewed tool capability; never dispatch arbitrary names/paths.

Kind: callable. Declared return: None. Source line: 326.

### WidgetSession.events

Yield bounded ASGI response messages; cancel disconnected/expired requests.

Kind: callable. Declared return: Not declared / class. Source line: 384.

### WidgetSession.request

Collect one finite response for native tests; the live bridge streams events.

Kind: callable. Declared return: HttpResult. Source line: 452.

### WidgetSession.close

Cancel the owned native job, join workers and remove only its temporary tree.

Kind: callable. Declared return: None. Source line: 462.

### WidgetSession.__exit__

Always close native resources, including failed browser validation runs.

Kind: callable. Declared return: None. Source line: 484.

### run_provisional_tests

Run proposed tests in a distinct native process; reports remain provisional.

Kind: callable. Declared return: dict. Source line: 489.

## Variables and parameters

| Scope | Name | Role and meaning | Type | Lifetime | Writes |
| --- | --- | --- | --- | --- | --- |
| module | base64 | Imported dependency for base64 in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 8 |
| module | json | Imported dependency for json in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 9 |
| module | logging | Imported dependency for logging in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 10 |
| module | queue | Imported dependency for queue in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 11 |
| module | shutil | Imported dependency for shutil in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 12 |
| module | struct | Imported dependency for struct in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 13 |
| module | subprocess | Imported dependency for subprocess in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 14 |
| module | tempfile | Imported dependency for tempfile in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 15 |
| module | threading | Imported dependency for threading in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 16 |
| module | time | Imported dependency for time in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 17 |
| module | ThreadPoolExecutor | Imported dependency for ThreadPoolExecutor in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 18 |
| module | dataclass | Imported dependency for dataclass in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 19 |
| module | Path | Imported dependency for Path in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 20 |
| module | uuid4 | Imported dependency for uuid4 in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 21 |
| module | Text | Imported dependency for Text in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 23 |
| module | decode_frame | Imported dependency for decode frame in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 24 |
| module | encode_frame | Imported dependency for encode frame in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 24 |
| module | validate_http_request | Imported dependency for validate http request in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 24 |
| module | ApprovedWidget | Imported dependency for ApprovedWidget in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 25 |
| module | validate_widget | Imported dependency for validate widget in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 25 |
| module | FUNCTION_NAME | Imported dependency for FUNCTION NAME in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 26 |
| module | TESTS_FILENAME | Imported dependency for TESTS FILENAME in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 26 |
| module | WIDGET_FILENAME | Imported dependency for WIDGET FILENAME in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 26 |
| module | stage_runtime | Imported dependency for stage runtime in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 27 |
| module | WindowsSandbox | Imported dependency for WindowsSandbox in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 28 |
| module | NativeWindows | Imported dependency for NativeWindows in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 29 |
| module | logger | Module logger emitting bounded operation diagnostics rather than artifact bodies. | Return type of getLogger; see its callable contract | Module/process lifetime | 31 |
| HttpResult | status | Typed binding for status in HttpResult; use the enclosing contract and type below. | int | Enclosing invocation or class/instance lifetime | 38 |
| HttpResult | headers | Typed binding for headers in HttpResult; use the enclosing contract and type below. | list | Enclosing invocation or class/instance lifetime | 39 |
| HttpResult | body | Typed binding for body in HttpResult; use the enclosing contract and type below. | bytes | Enclosing invocation or class/instance lifetime | 40 |
| WidgetSession.__init__ | self | Owning instance; its attributes retain state for the instance lifetime. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 47 |
| WidgetSession.__init__ | approved | Parameter for approved in WidgetSession.__init__; use the enclosing contract and type below. | ApprovedWidget &#124; None | Enclosing invocation or class/instance lifetime | 48 |
| WidgetSession.__init__ | tests_only | Parameter for tests only in WidgetSession.__init__; use the enclosing contract and type below. | bool | Enclosing invocation or class/instance lifetime | 50 |
| WidgetSession.__init__ | lifetime | Parameter for lifetime in WidgetSession.__init__; use the enclosing contract and type below. | int &#124; None | Enclosing invocation or class/instance lifetime | 51 |
| WidgetSession.__init__ | self.lifetime | Attribute for lifetime in WidgetSession.__init__; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 56 |
| WidgetSession.__init__ | self.session_id | Browser or terminal session identifier for state and diagnostic ownership. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 57 |
| WidgetSession.__init__ | self.approved | Attribute for approved in WidgetSession.__init__; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 58 |
| WidgetSession.__init__ | self.tests_only | Attribute for tests only in WidgetSession.__init__; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 59 |
| WidgetSession.__init__ | self.responses | Attribute for responses in WidgetSession.__init__; use the enclosing contract and type below. | dict[str, queue.Queue] | Enclosing invocation or class/instance lifetime | 62 |
| WidgetSession.__init__ | self.write_lock | Attribute for write lock in WidgetSession.__init__; use the enclosing contract and type below. | Return type of Lock; see its callable contract | Enclosing invocation or class/instance lifetime | 63 |
| WidgetSession.__init__ | self.state_lock | Attribute for state lock in WidgetSession.__init__; use the enclosing contract and type below. | Return type of Lock; see its callable contract | Enclosing invocation or class/instance lifetime | 64 |
| WidgetSession.__init__ | self.cancel | Attribute for cancel in WidgetSession.__init__; use the enclosing contract and type below. | Return type of Event; see its callable contract | Enclosing invocation or class/instance lifetime | 65 |
| WidgetSession.__init__ | self.ready | Attribute for ready in WidgetSession.__init__; use the enclosing contract and type below. | Return type of Event; see its callable contract | Enclosing invocation or class/instance lifetime | 66 |
| WidgetSession.__init__ | self.closed | Attribute for closed in WidgetSession.__init__; use the enclosing contract and type below. | bool | Enclosing invocation or class/instance lifetime | 67 |
| WidgetSession.__init__ | self.close_lock | Attribute for close lock in WidgetSession.__init__; use the enclosing contract and type below. | Return type of Lock; see its callable contract | Enclosing invocation or class/instance lifetime | 68 |
| WidgetSession.__init__ | self.diagnostics | Attribute for diagnostics in WidgetSession.__init__; use the enclosing contract and type below. | dict | Enclosing invocation or class/instance lifetime | 69 |
| WidgetSession.__init__ | self.timings | Attribute for timings in WidgetSession.__init__; use the enclosing contract and type below. | dict[str, float] | Enclosing invocation or class/instance lifetime | 70 |
| WidgetSession.__init__ | self.tool_receipts | Attribute for tool receipts in WidgetSession.__init__; use the enclosing contract and type below. | list | Enclosing invocation or class/instance lifetime | 72 |
| WidgetSession.__init__ | self.tool_slots | Attribute for tool slots in WidgetSession.__init__; use the enclosing contract and type below. | Return type of BoundedSemaphore; see its callable contract | Enclosing invocation or class/instance lifetime | 73 |
| WidgetSession.__init__ | self.tool_calls | Attribute for tool calls in WidgetSession.__init__; use the enclosing contract and type below. | int | Enclosing invocation or class/instance lifetime | 74 |
| WidgetSession.__init__ | self.pool | Attribute for pool in WidgetSession.__init__; use the enclosing contract and type below. | Return type of ThreadPoolExecutor; see its callable contract | Enclosing invocation or class/instance lifetime | 75 |
| WidgetSession.__init__ | self.temporary | Attribute for temporary in WidgetSession.__init__; use the enclosing contract and type below. | NoneType | Enclosing invocation or class/instance lifetime | 76 |
| WidgetSession.__enter__ | self | Owning instance; its attributes retain state for the instance lifetime. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 78 |
| WidgetSession.__enter__ | error | Caught exception for error in WidgetSession.__enter__; use the enclosing contract and type below. | BaseException | Current exception handler; Python clears this binding afterward | 82 |
| WidgetSession.__enter__ | elapsed | Local binding for elapsed in WidgetSession.__enter__; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 83 |
| WidgetSession._start | self | Owning instance; its attributes retain state for the instance lifetime. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 95 |
| WidgetSession._start | pywintypes | Imported dependency for pywintypes in WidgetSession._start; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 97 |
| WidgetSession._start | win32api | Imported dependency for win32api in WidgetSession._start; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 98 |
| WidgetSession._start | win32con | Imported dependency for win32con in WidgetSession._start; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 99 |
| WidgetSession._start | win32pipe | Imported dependency for win32pipe in WidgetSession._start; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 100 |
| WidgetSession._start | self.temporary | Attribute for temporary in WidgetSession._start; use the enclosing contract and type below. | Return type of TemporaryDirectory; see its callable contract | Enclosing invocation or class/instance lifetime | 102 |
| WidgetSession._start | self.root | Explicit root directory against which named paths are resolved. | Return type of Path; see its callable contract | Enclosing invocation or class/instance lifetime | 103 |
| WidgetSession._start | runtime | Explicitly composed application services for one owner or compatibility facade. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 104 |
| WidgetSession._start | started | Local binding for started in WidgetSession._start; use the enclosing contract and type below. | Return type of monotonic; see its callable contract | Enclosing invocation or class/instance lifetime | 106 |
| WidgetSession._start | self.start_time | Attribute for start time in WidgetSession._start; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 107 |
| WidgetSession._start | name | Current identifier selected by parsing, lookup or dependency registration. | Element of the declared iterable | Enclosing invocation or class/instance lifetime | 116 |
| WidgetSession._start | ui | Local binding for ui in WidgetSession._start; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 123 |
| WidgetSession._start | attributes | Local binding for attributes in WidgetSession._start; use the enclosing contract and type below. | Return type of SECURITY_ATTRIBUTES; see its callable contract | Enclosing invocation or class/instance lifetime | 128 |
| WidgetSession._start | attributes.bInheritHandle | Attribute for attributes.bInheritHandle in WidgetSession._start; use the enclosing contract and type below. | bool | Enclosing invocation or class/instance lifetime | 129 |
| WidgetSession._start | self.child_read | Attribute for child read in WidgetSession._start; use the enclosing contract and type below. | Return type of CreatePipe; see its callable contract | Enclosing invocation or class/instance lifetime | 130 |
| WidgetSession._start | self.host_write | Attribute for host write in WidgetSession._start; use the enclosing contract and type below. | Return type of CreatePipe; see its callable contract | Enclosing invocation or class/instance lifetime | 130 |
| WidgetSession._start | self.host_read | Attribute for host read in WidgetSession._start; use the enclosing contract and type below. | Return type of CreatePipe; see its callable contract | Enclosing invocation or class/instance lifetime | 131 |
| WidgetSession._start | self.child_write | Attribute for child write in WidgetSession._start; use the enclosing contract and type below. | Return type of CreatePipe; see its callable contract | Enclosing invocation or class/instance lifetime | 131 |
| WidgetSession._start | handle | Loop item for handle in WidgetSession._start; use the enclosing contract and type below. | Element of the declared iterable | Enclosing invocation or class/instance lifetime | 132 |
| WidgetSession._start | self.native_thread | Attribute for native thread in WidgetSession._start; use the enclosing contract and type below. | Return type of Thread; see its callable contract | Enclosing invocation or class/instance lifetime | 134 |
| WidgetSession._start | self.reader_thread | Attribute for reader thread in WidgetSession._start; use the enclosing contract and type below. | Return type of Thread; see its callable contract | Enclosing invocation or class/instance lifetime | 135 |
| WidgetSession._start | deadline | Local binding for deadline in WidgetSession._start; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 138 |
| WidgetSession._stage_payload | self | Owning instance; its attributes retain state for the instance lifetime. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 153 |
| WidgetSession._stage_payload | source | Explicit source document or source-code text; never imported for reference generation. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 155 |
| WidgetSession._worker_arguments | self | Owning instance; its attributes retain state for the instance lifetime. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 165 |
| WidgetSession._control_message | self | Owning instance; its attributes retain state for the instance lifetime. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 169 |
| WidgetSession._control_message | message | Parameter for message in WidgetSession._control_message; use the enclosing contract and type below. | dict | Enclosing invocation or class/instance lifetime | 169 |
| WidgetSession._control_message | values | Local binding for values in WidgetSession._control_message; use the enclosing contract and type below. | Return type of get; see its callable contract | Enclosing invocation or class/instance lifetime | 173 |
| WidgetSession._control_message.comprehension_178 | v | Comprehension item for v in WidgetSession._control_message.comprehension_178; use the enclosing contract and type below. | Element of the declared iterable | This comprehension only; does not leak into its enclosing scope | 178 |
| WidgetSession._run_native | self | Owning instance; its attributes retain state for the instance lifetime. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 184 |
| WidgetSession._run_native | native | Local binding for native in WidgetSession._run_native; use the enclosing contract and type below. | Return type of NativeWindows; see its callable contract | Enclosing invocation or class/instance lifetime | 186 |
| WidgetSession._run_native | native_started | Local binding for native started in WidgetSession._run_native; use the enclosing contract and type below. | Return type of monotonic; see its callable contract | Enclosing invocation or class/instance lifetime | 187 |
| WidgetSession._run_native | sid | Managed resource for sid in WidgetSession._run_native; use the enclosing contract and type below. | Return type of profile; see its callable contract | Context-manager block; exit invokes its cleanup protocol | 189 |
| WidgetSession._run_native | sid_text | Managed resource for sid text in WidgetSession._run_native; use the enclosing contract and type below. | Return type of profile; see its callable contract | Context-manager block; exit invokes its cleanup protocol | 189 |
| WidgetSession._run_native | path | Path under validation or an explicitly scoped maintained source path. | Element of the declared iterable | Enclosing invocation or class/instance lifetime | 190 |
| WidgetSession._run_native | permission | Loop item for permission in WidgetSession._run_native; use the enclosing contract and type below. | Element of the declared iterable | Enclosing invocation or class/instance lifetime | 190 |
| WidgetSession._run_native | result | Intermediate or returned outcome; consult the callable contract for trust/validation. | Return type of run; see its callable contract | Enclosing invocation or class/instance lifetime | 191 |
| WidgetSession._run_native | executable | Local binding for executable in WidgetSession._run_native; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 207 |
| WidgetSession._run_native | handles | Local binding for handles in WidgetSession._run_native; use the enclosing contract and type below. | tuple | Enclosing invocation or class/instance lifetime | 208 |
| WidgetSession._run_native | command | Local binding for command in WidgetSession._run_native; use the enclosing contract and type below. | Return type of list2cmdline; see its callable contract | Enclosing invocation or class/instance lifetime | 209 |
| WidgetSession._run_native | error | Caught exception for error in WidgetSession._run_native; use the enclosing contract and type below. | Exception | Current exception handler; Python clears this binding afterward | 233 |
| WidgetSession._run_native | handle | Loop item for handle in WidgetSession._run_native; use the enclosing contract and type below. | Element of the declared iterable | Enclosing invocation or class/instance lifetime | 236 |
| WidgetSession._child_started | self | Owning instance; its attributes retain state for the instance lifetime. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 240 |
| WidgetSession._write | self | Owning instance; its attributes retain state for the instance lifetime. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 246 |
| WidgetSession._write | message | Parameter for message in WidgetSession._write; use the enclosing contract and type below. | dict | Enclosing invocation or class/instance lifetime | 246 |
| WidgetSession._write | win32file | Imported dependency for win32file in WidgetSession._write; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 248 |
| WidgetSession._write | wire | Local binding for wire in WidgetSession._write; use the enclosing contract and type below. | Return type of encode_frame; see its callable contract | Enclosing invocation or class/instance lifetime | 250 |
| WidgetSession._check_runtime | self | Owning instance; its attributes retain state for the instance lifetime. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 254 |
| WidgetSession._read_exact | self | Owning instance; its attributes retain state for the instance lifetime. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 257 |
| WidgetSession._read_exact | size | Parameter for size in WidgetSession._read_exact; use the enclosing contract and type below. | int | Enclosing invocation or class/instance lifetime | 257 |
| WidgetSession._read_exact | win32file | Imported dependency for win32file in WidgetSession._read_exact; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 259 |
| WidgetSession._read_exact | win32pipe | Imported dependency for win32pipe in WidgetSession._read_exact; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 260 |
| WidgetSession._read_exact | data | Local binding for data in WidgetSession._read_exact; use the enclosing contract and type below. | Return type of bytearray; see its callable contract | Enclosing invocation or class/instance lifetime | 262 |
| WidgetSession._read_exact | available | Local binding for available in WidgetSession._read_exact; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 265 |
| WidgetSession._read_loop | self | Owning instance; its attributes retain state for the instance lifetime. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 276 |
| WidgetSession._read_loop | size | Local binding for size in WidgetSession._read_loop; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 280 |
| WidgetSession._read_loop | message | Local binding for message in WidgetSession._read_loop; use the enclosing contract and type below. | Return type of decode_frame; see its callable contract | Enclosing invocation or class/instance lifetime | 283 |
| WidgetSession._read_loop | kind | Local binding for kind in WidgetSession._read_loop; use the enclosing contract and type below. | Return type of get; see its callable contract | Enclosing invocation or class/instance lifetime | 284 |
| WidgetSession._read_loop | self.tool_calls | Attribute for tool calls in WidgetSession._read_loop; use the enclosing contract and type below. | Preserved or operator-dependent type | Enclosing invocation or class/instance lifetime | 296 |
| WidgetSession._read_loop | target | Local binding for target in WidgetSession._read_loop; use the enclosing contract and type below. | Return type of get; see its callable contract | Enclosing invocation or class/instance lifetime | 302 |
| WidgetSession._read_loop | error | Caught exception for error in WidgetSession._read_loop; use the enclosing contract and type below. | Exception | Current exception handler; Python clears this binding afterward | 308 |
| WidgetSession._invoke_tool | self | Owning instance; its attributes retain state for the instance lifetime. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 326 |
| WidgetSession._invoke_tool | message | Parameter for message in WidgetSession._invoke_tool; use the enclosing contract and type below. | dict | Enclosing invocation or class/instance lifetime | 326 |
| WidgetSession._invoke_tool | TypeAdapter | Imported dependency for TypeAdapter in WidgetSession._invoke_tool; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 328 |
| WidgetSession._invoke_tool | result | Intermediate or returned outcome; consult the callable contract for trust/validation. | dict | Enclosing invocation or class/instance lifetime | 330, 360 |
| WidgetSession._invoke_tool | text | Local binding for text in WidgetSession._invoke_tool; use the enclosing contract and type below. | Return type of validate_python; see its callable contract | Enclosing invocation or class/instance lifetime | 340 |
| WidgetSession._invoke_tool | code | Source snapshot passed through approval, syntax checks and isolated staging. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 344 |
| WidgetSession._invoke_tool | observation | Local binding for observation in WidgetSession._invoke_tool; use the enclosing contract and type below. | Return type of evaluate; see its callable contract | Enclosing invocation or class/instance lifetime | 349 |
| WidgetSession._invoke_tool | hashlib | Imported dependency for hashlib in WidgetSession._invoke_tool; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 361 |
| WidgetSession._invoke_tool | self.tool_receipts | Attribute for tool receipts in WidgetSession._invoke_tool; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 372 |
| WidgetSession.events | self | Owning instance; its attributes retain state for the instance lifetime. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 385 |
| WidgetSession.events | method | Parameter for method in WidgetSession.events; use the enclosing contract and type below. | str | Enclosing invocation or class/instance lifetime | 386 |
| WidgetSession.events | path | Path under validation or an explicitly scoped maintained source path. | str | Enclosing invocation or class/instance lifetime | 387 |
| WidgetSession.events | body | Parameter for body in WidgetSession.events; use the enclosing contract and type below. | bytes | Enclosing invocation or class/instance lifetime | 388 |
| WidgetSession.events | query | Original user request or a trusted test query; avoid payload logging by default. | bytes | Enclosing invocation or class/instance lifetime | 390 |
| WidgetSession.events | headers | Parameter for headers in WidgetSession.events; use the enclosing contract and type below. | list &#124; None | Enclosing invocation or class/instance lifetime | 391 |
| WidgetSession.events | identity | Explicit owner identity used by a session factory or fixture. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 397 |
| WidgetSession.events | target | Local binding for target in WidgetSession.events; use the enclosing contract and type below. | Return type of Queue; see its callable contract | Enclosing invocation or class/instance lifetime | 398 |
| WidgetSession.events | scope | Local binding for scope in WidgetSession.events; use the enclosing contract and type below. | dict | Enclosing invocation or class/instance lifetime | 403 |
| WidgetSession.events | total | Local binding for total in WidgetSession.events; use the enclosing contract and type below. | int | Enclosing invocation or class/instance lifetime | 428, 439 |
| WidgetSession.events | deadline | Local binding for deadline in WidgetSession.events; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 429 |
| WidgetSession.events | message | Local binding for message in WidgetSession.events; use the enclosing contract and type below. | Return type of get; see its callable contract | Enclosing invocation or class/instance lifetime | 432 |
| WidgetSession.events | decoded | Local binding for decoded in WidgetSession.events; use the enclosing contract and type below. | Return type of b64decode; see its callable contract | Enclosing invocation or class/instance lifetime | 438 |
| WidgetSession.request | self | Owning instance; its attributes retain state for the instance lifetime. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 452 |
| WidgetSession.request | method | Parameter for method in WidgetSession.request; use the enclosing contract and type below. | str | Enclosing invocation or class/instance lifetime | 452 |
| WidgetSession.request | path | Path under validation or an explicitly scoped maintained source path. | str | Enclosing invocation or class/instance lifetime | 452 |
| WidgetSession.request | body | Parameter for body in WidgetSession.request; use the enclosing contract and type below. | bytes | Enclosing invocation or class/instance lifetime | 452 |
| WidgetSession.request | status | Local binding for status in WidgetSession.request; use the enclosing contract and type below. | tuple | Enclosing invocation or class/instance lifetime | 454, 457 |
| WidgetSession.request | headers | Local binding for headers in WidgetSession.request; use the enclosing contract and type below. | tuple | Enclosing invocation or class/instance lifetime | 454, 457 |
| WidgetSession.request | content | Artifact or review text whose encoding, size and approval state must be checked. | tuple | Enclosing invocation or class/instance lifetime | 454 |
| WidgetSession.request | event | Loop item for event in WidgetSession.request; use the enclosing contract and type below. | Element of the declared iterable | Enclosing invocation or class/instance lifetime | 455 |
| WidgetSession.close | self | Owning instance; its attributes retain state for the instance lifetime. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 462 |
| WidgetSession.close | cleanup_started | Local binding for cleanup started in WidgetSession.close; use the enclosing contract and type below. | Return type of monotonic; see its callable contract | Enclosing invocation or class/instance lifetime | 467 |
| WidgetSession.close | self.closed | Attribute for closed in WidgetSession.close; use the enclosing contract and type below. | bool | Enclosing invocation or class/instance lifetime | 468 |
| WidgetSession.close | name | Current identifier selected by parsing, lookup or dependency registration. | Element of the declared iterable | Enclosing invocation or class/instance lifetime | 475 |
| WidgetSession.close | handle | Local binding for handle in WidgetSession.close; use the enclosing contract and type below. | Return type of getattr; see its callable contract | Enclosing invocation or class/instance lifetime | 476 |
| WidgetSession.__exit__ | self | Owning instance; its attributes retain state for the instance lifetime. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 484 |
| WidgetSession.__exit__ | args | Parameter for args in WidgetSession.__exit__; use the enclosing contract and type below. | object | Enclosing invocation or class/instance lifetime | 484 |
| run_provisional_tests | approved | Parameter for approved in run_provisional_tests; use the enclosing contract and type below. | ApprovedWidget | Enclosing invocation or class/instance lifetime | 489 |
| run_provisional_tests | session | Managed resource for session in run_provisional_tests; use the enclosing contract and type below. | Return type of WidgetSession; see its callable contract | Context-manager block; exit invokes its cleanup protocol | 493 |
| run_provisional_tests | native_result | Local binding for native result in run_provisional_tests; use the enclosing contract and type below. | Return type of get; see its callable contract | Enclosing invocation or class/instance lifetime | 495 |
| run_provisional_tests | report | Local binding for report in run_provisional_tests; use the enclosing contract and type below. | Return type of get; see its callable contract | Enclosing invocation or class/instance lifetime | 501 |
