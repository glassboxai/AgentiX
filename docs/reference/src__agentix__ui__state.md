# Reference for src/agentix/ui/state.py

Workflow state and thread-safe stdout capture, without process-wide installation.

Source fingerprint: 4803363cb28043bd21cfde838fb14d700017d15f7e0c89d1929631fbd6e894d0

This reference is generated from maintained source without imports or execution. Assigned values are intentionally omitted. Runtime-dependent types are explicit; the enclosing docstring defines the behavioral contract. See [architecture](../ARCHITECTURE_QUALITY.md) for manually reviewed responsibility and dependency decisions.

## Classes and callables

### ConsoleThoughtsCapture

Mirror output and expose a locked, ANSI-stripped activity snapshot.

Construction never replaces sys.stdout. Retain at most 256 completed lines
and one 4096-character partial line per session. Visible tails are capped at
256 lines, so fragmented SDK output cannot grow indefinitely in memory.

Kind: class. Declared return: Not declared / class. Source line: 13.

### ConsoleThoughtsCapture.__init__

Retain the host stream and create a private lock/buffer.

Kind: callable. Declared return: None. Source line: 21.

### ConsoleThoughtsCapture.write

Retain Unicode activity and mirror it safely to the host console.

Windows redirected consoles may reject CrewAI's emoji panels. Escape
only that console copy instead of losing the owning GUI's verbose text.
Other I/O errors still propagate; diagnostic events keep their own policy.

Kind: callable. Declared return: None. Source line: 28.

### ConsoleThoughtsCapture.flush

Flush the underlying stream so server logs remain visible promptly.

Kind: callable. Declared return: None. Source line: 55.

### ConsoleThoughtsCapture.isatty

Preserve terminal detection used by the server logging framework.

Kind: callable. Declared return: bool. Source line: 59.

### ConsoleThoughtsCapture.__getattr__

Delegate stream metadata such as encoding and file descriptors.

Kind: callable. Declared return: Any. Source line: 63.

### ConsoleThoughtsCapture.get_logs

Return bounded logical lines, including an unfinished streaming line.

Kind: callable. Declared return: str. Source line: 67.

### ConsoleThoughtsCapture.clear

Clear previous activity before a new workflow begins.

Kind: callable. Declared return: None. Source line: 76.

### ExecutionState

Mutable state for one workflow owner, with an independent chat history.

The history factory prevents accidental sharing between instances. Callers
coordinating worker threads must still synchronize access appropriately.

Kind: class. Declared return: Not declared / class. Source line: 84.

## Variables and parameters

| Scope | Name | Role and meaning | Type | Lifetime | Writes |
| --- | --- | --- | --- | --- | --- |
| module | re | Imported dependency for re in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 3 |
| module | threading | Imported dependency for threading in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 4 |
| module | deque | Imported dependency for deque in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 5 |
| module | dataclass | Imported dependency for dataclass in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 6 |
| module | field | Imported dependency for field in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 6 |
| module | Any | Imported dependency for Any in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 7 |
| module | TextIO | Imported dependency for TextIO in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 7 |
| module | uuid4 | Imported dependency for uuid4 in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 8 |
| module | ANSI_ESCAPE | Module binding for ANSI ESCAPE in module; use the enclosing contract and type below. | Return type of compile; see its callable contract | Module/process lifetime | 10 |
| ConsoleThoughtsCapture.__init__ | self | Owning instance; its attributes retain state for the instance lifetime. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 21 |
| ConsoleThoughtsCapture.__init__ | original_stdout | Parameter for original stdout in ConsoleThoughtsCapture.__init__; use the enclosing contract and type below. | TextIO | Enclosing invocation or class/instance lifetime | 21 |
| ConsoleThoughtsCapture.__init__ | self.original_stdout | Attribute for original stdout in ConsoleThoughtsCapture.__init__; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 23 |
| ConsoleThoughtsCapture.__init__ | self.lock | Attribute for lock in ConsoleThoughtsCapture.__init__; use the enclosing contract and type below. | Return type of Lock; see its callable contract | Enclosing invocation or class/instance lifetime | 24 |
| ConsoleThoughtsCapture.__init__ | self.logs_buffer | Attribute for logs buffer in ConsoleThoughtsCapture.__init__; use the enclosing contract and type below. | deque[str] | Enclosing invocation or class/instance lifetime | 25 |
| ConsoleThoughtsCapture.__init__ | self._partial | Attribute for partial in ConsoleThoughtsCapture.__init__; use the enclosing contract and type below. | str | Enclosing invocation or class/instance lifetime | 26 |
| ConsoleThoughtsCapture.write | self | Owning instance; its attributes retain state for the instance lifetime. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 28 |
| ConsoleThoughtsCapture.write | text | Parameter for text in ConsoleThoughtsCapture.write; use the enclosing contract and type below. | str | Enclosing invocation or class/instance lifetime | 28, 37 |
| ConsoleThoughtsCapture.write | redact | Imported dependency for redact in ConsoleThoughtsCapture.write; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 35 |
| ConsoleThoughtsCapture.write | lines | Local binding for lines in ConsoleThoughtsCapture.write; use the enclosing contract and type below. | Return type of split; see its callable contract | Enclosing invocation or class/instance lifetime | 42 |
| ConsoleThoughtsCapture.write | line | Current source or text line scoped to parsing; no implicit execution occurs. | Element of the declared iterable | Enclosing invocation or class/instance lifetime | 43 |
| ConsoleThoughtsCapture.write | clean | Local binding for clean in ConsoleThoughtsCapture.write; use the enclosing contract and type below. | Return type of rstrip; see its callable contract | Enclosing invocation or class/instance lifetime | 44 |
| ConsoleThoughtsCapture.write | self._partial | Attribute for partial in ConsoleThoughtsCapture.write; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 47 |
| ConsoleThoughtsCapture.flush | self | Owning instance; its attributes retain state for the instance lifetime. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 55 |
| ConsoleThoughtsCapture.isatty | self | Owning instance; its attributes retain state for the instance lifetime. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 59 |
| ConsoleThoughtsCapture.__getattr__ | self | Owning instance; its attributes retain state for the instance lifetime. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 63 |
| ConsoleThoughtsCapture.__getattr__ | name | Current identifier selected by parsing, lookup or dependency registration. | str | Enclosing invocation or class/instance lifetime | 63 |
| ConsoleThoughtsCapture.get_logs | self | Owning instance; its attributes retain state for the instance lifetime. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 67 |
| ConsoleThoughtsCapture.get_logs | max_lines | Parameter for max lines in ConsoleThoughtsCapture.get_logs; use the enclosing contract and type below. | int | Enclosing invocation or class/instance lifetime | 67 |
| ConsoleThoughtsCapture.get_logs | lines | Local binding for lines in ConsoleThoughtsCapture.get_logs; use the enclosing contract and type below. | Return type of list; see its callable contract | Enclosing invocation or class/instance lifetime | 70 |
| ConsoleThoughtsCapture.get_logs | partial | Local binding for partial in ConsoleThoughtsCapture.get_logs; use the enclosing contract and type below. | Return type of sub; see its callable contract | Enclosing invocation or class/instance lifetime | 71 |
| ConsoleThoughtsCapture.clear | self | Owning instance; its attributes retain state for the instance lifetime. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 76 |
| ConsoleThoughtsCapture.clear | self._partial | Attribute for partial in ConsoleThoughtsCapture.clear; use the enclosing contract and type below. | str | Enclosing invocation or class/instance lifetime | 80 |
| ExecutionState | is_running | Typed binding for is running in ExecutionState; use the enclosing contract and type below. | bool | Enclosing invocation or class/instance lifetime | 91 |
| ExecutionState | session_id | Browser or terminal session identifier for state and diagnostic ownership. | str | Enclosing invocation or class/instance lifetime | 92 |
| ExecutionState | operation_id | Identity of one user operation; new operations invalidate earlier evidence. | str | Enclosing invocation or class/instance lifetime | 93 |
| ExecutionState | last_response | Typed binding for last response in ExecutionState; use the enclosing contract and type below. | str | Enclosing invocation or class/instance lifetime | 94 |
| ExecutionState | error_message | Typed binding for error message in ExecutionState; use the enclosing contract and type below. | str | Enclosing invocation or class/instance lifetime | 95 |
| ExecutionState | chat_history | Typed binding for chat history in ExecutionState; use the enclosing contract and type below. | list[dict[str, str]] | Enclosing invocation or class/instance lifetime | 96 |
| ExecutionState | last_displayed_filepath | Typed binding for last displayed filepath in ExecutionState; use the enclosing contract and type below. | str &#124; None | Enclosing invocation or class/instance lifetime | 97 |
| ExecutionState | last_displayed_request_id | Typed binding for last displayed request id in ExecutionState; use the enclosing contract and type below. | str &#124; None | Enclosing invocation or class/instance lifetime | 98 |
| ExecutionState | active_message_index | Typed binding for active message index in ExecutionState; use the enclosing contract and type below. | int &#124; None | Enclosing invocation or class/instance lifetime | 99 |
