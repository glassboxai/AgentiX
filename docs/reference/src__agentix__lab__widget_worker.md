# Reference for src/agentix/lab/widget_worker.py

Native ASGI child entrypoint; imported generated widget code never enters the host.

Only framed JSON uses inherited private pipes. Standard output remains bounded diagnostic
text. This worker opens no network listener. Legacy widget calls use the host gateway;
reviewed application mode imports and calls its tools directly inside this boundary.

Source fingerprint: 26620e1b68e80d525b90b3862b5fdfa4a566d7ebd9f8f46c634d5b75b5352a8a

This reference is generated from maintained source without imports or execution. Assigned values are intentionally omitted. Runtime-dependent types are explicit; the enclosing docstring defines the behavioral contract. See [architecture](../ARCHITECTURE_QUALITY.md) for manually reviewed responsibility and dependency decisions.

## Classes and callables

### emit

Serialize complete framed writes; concurrent responses cannot interleave.

Kind: callable. Declared return: None. Source line: 46.

### exact

Read exactly a bounded frame segment, treating closed parent IPC as shutdown.

Kind: callable. Declared return: bytes. Source line: 55.

### read_message

Reject oversized lengths before allocating payload memory.

Kind: callable. Declared return: dict. Source line: 66.

### Context

Minimal instance-specific capability; Python tool implementations stay outside.

Kind: class. Declared return: Not declared / class. Source line: 74.

### Context.__init__

Bind the reviewed tool to one widget identity and API namespace.

Kind: callable. Declared return: None. Source line: 77.

### Context.elem_id

Permit only reviewed component roles, namespaced per instance.

Kind: callable. Declared return: str. Source line: 82.

### Context.invoke

Request the approved vowel tool, with finite wait and no direct import.

Kind: callable. Declared return: int. Source line: 88.

### main

Run a headless operation or build the reviewed GUI and multiplex private ASGI traffic.

Kind: callable. Declared return: None. Source line: 102.

### main.stop_application

Ask the maintained parent to stop only this owned application job.

Kind: callable. Declared return: None. Source line: 147.

### main.handle

Run one ASGI request; stream bounded response events rather than trusting HTML.

Kind: callable. Declared return: None. Source line: 234.

### main.handle.receive

Deliver one bounded request body; cancellation represents disconnect.

Kind: callable. Declared return: dict. Source line: 239.

### main.handle.send

Normalize only HTTP start/body events into non-executable JSON.

Kind: callable. Declared return: None. Source line: 251.

## Variables and parameters

| Scope | Name | Role and meaning | Type | Lifetime | Writes |
| --- | --- | --- | --- | --- | --- |
| module | asyncio | Imported dependency for asyncio in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 8 |
| module | base64 | Imported dependency for base64 in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 9 |
| module | importlib | Imported dependency for importlib in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 10 |
| module | json | Imported dependency for json in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 11 |
| module | os | Imported dependency for os in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 12 |
| module | struct | Imported dependency for struct in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 13 |
| module | sys | Imported dependency for sys in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 14 |
| module | threading | Imported dependency for threading in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 15 |
| module | time | Imported dependency for time in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 16 |
| module | Path | Imported dependency for Path in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 17 |
| module | uuid4 | Imported dependency for uuid4 in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 18 |
| module | ROOT | Module binding for ROOT in module; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Module/process lifetime | 20 |
| module | msvcrt | Imported dependency for msvcrt in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 35 |
| module | decode_frame | Imported dependency for decode frame in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 37 |
| module | encode_frame | Imported dependency for encode frame in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 37 |
| module | TESTS_FILENAME | Imported dependency for TESTS FILENAME in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 38 |
| module | WIDGET_FILENAME | Imported dependency for WIDGET FILENAME in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 38 |
| module | READER | Module binding for READER in module; use the enclosing contract and type below. | Return type of open_osfhandle; see its callable contract | Module/process lifetime | 40 |
| module | WRITER | Module binding for WRITER in module; use the enclosing contract and type below. | Return type of open_osfhandle; see its callable contract | Module/process lifetime | 41 |
| module | WRITE_LOCK | Module binding for WRITE LOCK in module; use the enclosing contract and type below. | Return type of Lock; see its callable contract | Module/process lifetime | 42 |
| module | TOOLS | Module binding for TOOLS in module; use the enclosing contract and type below. | dict | Module/process lifetime | 43 |
| emit | message | Parameter for message in emit; use the enclosing contract and type below. | dict | Enclosing invocation or class/instance lifetime | 46 |
| emit | wire | Local binding for wire in emit; use the enclosing contract and type below. | Return type of encode_frame; see its callable contract | Enclosing invocation or class/instance lifetime | 48, 52 |
| emit | count | Local binding for count in emit; use the enclosing contract and type below. | Return type of write; see its callable contract | Enclosing invocation or class/instance lifetime | 51 |
| exact | size | Parameter for size in exact; use the enclosing contract and type below. | int | Enclosing invocation or class/instance lifetime | 55 |
| exact | data | Local binding for data in exact; use the enclosing contract and type below. | Return type of bytearray; see its callable contract | Enclosing invocation or class/instance lifetime | 57 |
| exact | part | Local binding for part in exact; use the enclosing contract and type below. | Return type of read; see its callable contract | Enclosing invocation or class/instance lifetime | 59 |
| read_message | size | Local binding for size in read_message; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 68 |
| Context.__init__ | self | Owning instance; its attributes retain state for the instance lifetime. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 77 |
| Context.__init__ | instance | Parameter for instance in Context.__init__; use the enclosing contract and type below. | str | Enclosing invocation or class/instance lifetime | 77 |
| Context.__init__ | self.instance | Attribute for instance in Context.__init__; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 79 |
| Context.__init__ | self.api_name | Attribute for api name in Context.__init__; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 80 |
| Context.elem_id | self | Owning instance; its attributes retain state for the instance lifetime. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 82 |
| Context.elem_id | control | Parameter for control in Context.elem_id; use the enclosing contract and type below. | str | Enclosing invocation or class/instance lifetime | 82 |
| Context.invoke | self | Owning instance; its attributes retain state for the instance lifetime. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 88 |
| Context.invoke | text | Parameter for text in Context.invoke; use the enclosing contract and type below. | str | Enclosing invocation or class/instance lifetime | 88 |
| Context.invoke | identity | Explicit owner identity used by a session factory or fixture. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 90 |
| Context.invoke | event | Local binding for event in Context.invoke; use the enclosing contract and type below. | tuple | Enclosing invocation or class/instance lifetime | 91 |
| Context.invoke | result | Intermediate or returned outcome; consult the callable contract for trust/validation. | tuple | Enclosing invocation or class/instance lifetime | 91 |
| main | analyze_text | Imported dependency for analyze text in main; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 105 |
| main | value | Value at the current validation/rendering boundary; apply the enclosing contract. | Return type of analyze_text; see its callable contract | Enclosing invocation or class/instance lifetime | 107 |
| main | io | Imported dependency for io in main; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 111, 184 |
| main | unittest | Imported dependency for unittest in main; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 112, 185 |
| main | suite | Local binding for suite in main; use the enclosing contract and type below. | Return type of TestSuite; see its callable contract | Enclosing invocation or class/instance lifetime | 114 |
| main | names | Local binding for names in main; use the enclosing contract and type below. | Return type of loads; see its callable contract | Enclosing invocation or class/instance lifetime | 115 |
| main | name | Current identifier selected by parsing, lookup or dependency registration. | Element of the declared iterable | Enclosing invocation or class/instance lifetime | 116 |
| main | test_spec | Local binding for test spec in main; use the enclosing contract and type below. | Return type of spec_from_file_location; see its callable contract | Enclosing invocation or class/instance lifetime | 117, 187 |
| main | module | Local binding for module in main; use the enclosing contract and type below. | Return type of module_from_spec; see its callable contract | Enclosing invocation or class/instance lifetime | 120 |
| main | result | Intermediate or returned outcome; consult the callable contract for trust/validation. | Return type of run; see its callable contract | Enclosing invocation or class/instance lifetime | 123, 190 |
| main | import_started | Local binding for import started in main; use the enclosing contract and type below. | Return type of monotonic; see its callable contract | Enclosing invocation or class/instance lifetime | 137 |
| main | gr | Imported dependency for gr in main; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 138 |
| main | FastAPI | Imported dependency for FastAPI in main; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 139 |
| main | imported | Local binding for imported in main; use the enclosing contract and type below. | Return type of monotonic; see its callable contract | Enclosing invocation or class/instance lifetime | 141 |
| main | create_application | Imported dependency for create application in main; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 143 |
| main | demo | Local binding for demo in main; use the enclosing contract and type below. | Return type of create_application; see its callable contract | Enclosing invocation or class/instance lifetime | 145, 206 |
| main | supervise_callback | Imported dependency for supervise callback in main; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 173 |
| main | block | Loop item for block in main; use the enclosing contract and type below. | Element of the declared iterable | Enclosing invocation or class/instance lifetime | 175 |
| main | block.fn | Attribute for block.fn in main; use the enclosing contract and type below. | Return type of supervise_callback; see its callable contract | Enclosing invocation or class/instance lifetime | 177 |
| main | spec | Local binding for spec in main; use the enclosing contract and type below. | Return type of spec_from_file_location; see its callable contract | Enclosing invocation or class/instance lifetime | 179 |
| main | widget | Local binding for widget in main; use the enclosing contract and type below. | Return type of module_from_spec; see its callable contract | Enclosing invocation or class/instance lifetime | 180 |
| main | tests_path | Local binding for tests path in main; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 182 |
| main | test_module | Local binding for test module in main; use the enclosing contract and type below. | Return type of module_from_spec; see its callable contract | Enclosing invocation or class/instance lifetime | 188 |
| main | create_theme | Imported dependency for create theme in main; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 218 |
| main | app | Local binding for app in main; use the enclosing contract and type below. | Return type of mount_gradio_app; see its callable contract | Enclosing invocation or class/instance lifetime | 220 |
| main | tasks | Local binding for tasks in main; use the enclosing contract and type below. | dict | Enclosing invocation or class/instance lifetime | 232 |
| main.handle | message | Parameter for message in main.handle; use the enclosing contract and type below. | dict | Enclosing invocation or class/instance lifetime | 234 |
| main.handle | identity | Explicit owner identity used by a session factory or fixture. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 236 |
| main.handle | delivered | Local binding for delivered in main.handle; use the enclosing contract and type below. | bool | Enclosing invocation or class/instance lifetime | 237 |
| main.handle.receive | delivered | Local binding for delivered in main.handle.receive; use the enclosing contract and type below. | bool | Enclosing invocation or class/instance lifetime | 243 |
| main.handle.send | event | Parameter for event in main.handle.send; use the enclosing contract and type below. | dict | Enclosing invocation or class/instance lifetime | 251 |
| main.handle.send.comprehension_259 | a | Comprehension item for a in main.handle.send.comprehension_259; use the enclosing contract and type below. | Element of the declared iterable | This comprehension only; does not leak into its enclosing scope | 261 |
| main.handle.send.comprehension_259 | b | Comprehension item for b in main.handle.send.comprehension_259; use the enclosing contract and type below. | Element of the declared iterable | This comprehension only; does not leak into its enclosing scope | 261 |
| main.handle.send | data | Local binding for data in main.handle.send; use the enclosing contract and type below. | Return type of get; see its callable contract | Enclosing invocation or class/instance lifetime | 266 |
| main.handle.send | offset | Loop item for offset in main.handle.send; use the enclosing contract and type below. | Element of the declared iterable | Enclosing invocation or class/instance lifetime | 267 |
| main.handle | scope | Local binding for scope in main.handle; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 280 |
| main.handle.comprehension_282 | a | Comprehension item for a in main.handle.comprehension_282; use the enclosing contract and type below. | Element of the declared iterable | This comprehension only; does not leak into its enclosing scope | 283 |
| main.handle.comprehension_282 | b | Comprehension item for b in main.handle.comprehension_282; use the enclosing contract and type below. | Element of the declared iterable | This comprehension only; does not leak into its enclosing scope | 283 |
| main | message | Local binding for message in main; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 295 |
| main | task | Local binding for task in main; use the enclosing contract and type below. | Return type of get; see its callable contract | Enclosing invocation or class/instance lifetime | 299, 312 |
| main | pending | Defensive pending-approval snapshot; never a capability to approve another owner. | Return type of get; see its callable contract | Enclosing invocation or class/instance lifetime | 303 |
