# Reference for src/agentix/lab/widget_panel.py

Owner-scoped lifecycle of approved native widgets embedded in an application view.

Only server-owned review configuration supplies package paths and identities. Browser
callbacks select no files or capabilities. Native Gradio stays on a different origin;
its iframe may be embedded only by the explicit parent Lab origin.

Source fingerprint: 1ddc2ba55f3fdc0a6920e08d81611701738cecf9093d041b3de031632f544791

This reference is generated from maintained source without imports or execution. Assigned values are intentionally omitted. Runtime-dependent types are explicit; the enclosing docstring defines the behavioral contract. See [architecture](../ARCHITECTURE_QUALITY.md) for manually reviewed responsibility and dependency decisions.

## Classes and callables

### Preview

Opaque owned native worker and listener; no generated module references.

Kind: class. Declared return: Not declared / class. Source line: 31.

### Preview.alive

Whether the owned worker can still answer requests.

Kind: callable. Declared return: bool. Source line: 37.

### Preview.close

Stop only the owned listener/job and release temporary resources.

Kind: callable. Declared return: None. Source line: 41.

### iframe_html

Render only a supervisor-created loopback address inside a restricted iframe.

Kind: callable. Declared return: str. Source line: 46.

### reviewed_widget

Load the explicitly activated host-owned review; never trust child test reports.

Kind: callable. Declared return: ApprovedWidget. Source line: 54.

### NativePreview

One finite native ASGI worker behind an explicitly bound private origin.

Kind: class. Declared return: Not declared / class. Source line: 74.

### NativePreview.__init__

Start only reviewed bytes; clean up all partial native/listener failures.

Kind: callable. Declared return: None. Source line: 77.

### NativePreview._create_session

Create the legacy gateway widget session; specialized applications use their snapshot.

Kind: callable. Declared return: WidgetSession. Source line: 124.

### NativePreview.alive

Report real worker/channel state rather than the existence of an old URL.

Kind: callable. Declared return: bool. Source line: 131.

### NativePreview._serve

Own listener lifecycle; worker cleanup runs even after HTTP errors.

Kind: callable. Declared return: None. Source line: 142.

### NativePreview._monitor

Expire this listener when its isolated worker ends; no unrelated process work.

Kind: callable. Declared return: None. Source line: 151.

### NativePreview.close

Cancel the owned job and wait a bounded interval for owned cleanup.

Kind: callable. Declared return: None. Source line: 160.

### _Slot

Reserved owner capacity, including an in-flight native startup.

Kind: class. Declared return: Not declared / class. Source line: 176.

### WidgetPanel

Bound native previews per browser owner; callbacks never accept package paths.

Kind: class. Declared return: Not declared / class. Source line: 183.

### WidgetPanel.__init__

Inject review authority and process boundary; construct without IO or servers.

Kind: callable. Declared return: None. Source line: 186.

### WidgetPanel.open

Reuse only the owner's live snapshot; reap expired owners before reserving capacity.

Kind: callable. Declared return: Preview. Source line: 201.

### WidgetPanel.close

Cancel only the requesting owner's live or pending preview.

Kind: callable. Declared return: None. Source line: 245.

### WidgetPanel.status

Return concise UI state without artifacts, hashes, test logs or private paths.

Kind: callable. Declared return: str. Source line: 260.

### WidgetPanel.close_all

Request cleanup only for previews registered by this manager.

Kind: callable. Declared return: None. Source line: 274.

## Variables and parameters

| Scope | Name | Role and meaning | Type | Lifetime | Writes |
| --- | --- | --- | --- | --- | --- |
| module | atexit | Imported dependency for atexit in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 8 |
| module | html | Imported dependency for html in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 9 |
| module | json | Imported dependency for json in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 10 |
| module | logging | Imported dependency for logging in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 11 |
| module | re | Imported dependency for re in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 12 |
| module | socket | Imported dependency for socket in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 13 |
| module | threading | Imported dependency for threading in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 14 |
| module | time | Imported dependency for time in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 15 |
| module | Callable | Imported dependency for Callable in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 16 |
| module | dataclass | Imported dependency for dataclass in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 17 |
| module | field | Imported dependency for field in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 17 |
| module | Path | Imported dependency for Path in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 18 |
| module | Generic | Imported dependency for Generic in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 19 |
| module | Protocol | Imported dependency for Protocol in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 19 |
| module | TypeVar | Imported dependency for TypeVar in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 19 |
| module | ApprovedWidget | Imported dependency for ApprovedWidget in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 21 |
| module | approve_package | Imported dependency for approve package in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 21 |
| module | WidgetBridge | Imported dependency for WidgetBridge in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 22 |
| module | TOOL_NAME | Imported dependency for TOOL NAME in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 23 |
| module | WidgetSession | Imported dependency for WidgetSession in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 24 |
| module | Capability | Module binding for Capability in module; use the enclosing contract and type below. | Return type of TypeVar; see its callable contract | Module/process lifetime | 26 |
| module | logger | Module logger emitting bounded operation diagnostics rather than artifact bodies. | Return type of getLogger; see its callable contract | Module/process lifetime | 28 |
| Preview | url | Typed binding for url in Preview; use the enclosing contract and type below. | str | Enclosing invocation or class/instance lifetime | 34 |
| Preview.alive | self | Owning instance; its attributes retain state for the instance lifetime. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 37 |
| Preview.close | self | Owning instance; its attributes retain state for the instance lifetime. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 41 |
| iframe_html | url | Parameter for url in iframe_html; use the enclosing contract and type below. | str | Enclosing invocation or class/instance lifetime | 46 |
| iframe_html | match | Local binding for match in iframe_html; use the enclosing contract and type below. | Return type of fullmatch; see its callable contract | Enclosing invocation or class/instance lifetime | 48 |
| reviewed_widget | configuration | Local binding for configuration in reviewed_widget; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 56 |
| reviewed_widget | record | Local binding for record in reviewed_widget; use the enclosing contract and type below. | Return type of loads; see its callable contract | Enclosing invocation or class/instance lifetime | 57 |
| reviewed_widget | package | Local binding for package in reviewed_widget; use the enclosing contract and type below. | Return type of Path; see its callable contract | Enclosing invocation or class/instance lifetime | 64 |
| reviewed_widget.comprehension_68 | part | Comprehension item for part in reviewed_widget.comprehension_68; use the enclosing contract and type below. | Element of the declared iterable | This comprehension only; does not leak into its enclosing scope | 68 |
| NativePreview.__init__ | self | Owning instance; its attributes retain state for the instance lifetime. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 77 |
| NativePreview.__init__ | approved | Parameter for approved in NativePreview.__init__; use the enclosing contract and type below. | Capability | Enclosing invocation or class/instance lifetime | 77 |
| NativePreview.__init__ | parent_origin | Parameter for parent origin in NativePreview.__init__; use the enclosing contract and type below. | str &#124; None | Enclosing invocation or class/instance lifetime | 77 |
| NativePreview.__init__ | port | Parameter for port in NativePreview.__init__; use the enclosing contract and type below. | int | Enclosing invocation or class/instance lifetime | 77 |
| NativePreview.__init__ | uvicorn | Imported dependency for uvicorn in NativePreview.__init__; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 79 |
| NativePreview.__init__ | self.approved | Attribute for approved in NativePreview.__init__; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 81 |
| NativePreview.__init__ | self.paused | Attribute for paused in NativePreview.__init__; use the enclosing contract and type below. | bool | Enclosing invocation or class/instance lifetime | 82 |
| NativePreview.__init__ | self.stop | Attribute for stop in NativePreview.__init__; use the enclosing contract and type below. | Return type of Event; see its callable contract | Enclosing invocation or class/instance lifetime | 83 |
| NativePreview.__init__ | self.listener | Attribute for listener in NativePreview.__init__; use the enclosing contract and type below. | Return type of socket; see its callable contract | Enclosing invocation or class/instance lifetime | 84 |
| NativePreview.__init__ | self.port | Attribute for port in NativePreview.__init__; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 91 |
| NativePreview.__init__ | self.url | Attribute for url in NativePreview.__init__; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 92 |
| NativePreview.__init__ | self.session | Attribute for session in NativePreview.__init__; use the enclosing contract and type below. | Return type of _create_session; see its callable contract | Enclosing invocation or class/instance lifetime | 93 |
| NativePreview.__init__ | self.bridge | Attribute for bridge in NativePreview.__init__; use the enclosing contract and type below. | Return type of WidgetBridge; see its callable contract | Enclosing invocation or class/instance lifetime | 96 |
| NativePreview.__init__ | self.server | Attribute for server in NativePreview.__init__; use the enclosing contract and type below. | Return type of Server; see its callable contract | Enclosing invocation or class/instance lifetime | 97 |
| NativePreview.__init__ | self.thread | Attribute for thread in NativePreview.__init__; use the enclosing contract and type below. | Return type of Thread; see its callable contract | Enclosing invocation or class/instance lifetime | 107 |
| NativePreview.__init__ | self.monitor | Attribute for monitor in NativePreview.__init__; use the enclosing contract and type below. | Return type of Thread; see its callable contract | Enclosing invocation or class/instance lifetime | 109 |
| NativePreview.__init__ | deadline | Local binding for deadline in NativePreview.__init__; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 111 |
| NativePreview._create_session | self | Owning instance; its attributes retain state for the instance lifetime. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 124 |
| NativePreview._create_session | approved | Parameter for approved in NativePreview._create_session; use the enclosing contract and type below. | Capability | Enclosing invocation or class/instance lifetime | 124 |
| NativePreview.alive | self | Owning instance; its attributes retain state for the instance lifetime. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 131 |
| NativePreview._serve | self | Owning instance; its attributes retain state for the instance lifetime. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 142 |
| NativePreview._monitor | self | Owning instance; its attributes retain state for the instance lifetime. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 151 |
| NativePreview._monitor | self.server.should_exit | Attribute for server.should exit in NativePreview._monitor; use the enclosing contract and type below. | bool | Enclosing invocation or class/instance lifetime | 158 |
| NativePreview.close | self | Owning instance; its attributes retain state for the instance lifetime. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 160 |
| NativePreview.close | self.server.should_exit | Attribute for server.should exit in NativePreview.close; use the enclosing contract and type below. | bool | Enclosing invocation or class/instance lifetime | 165 |
| _Slot | cancelled | Typed binding for cancelled in _Slot; use the enclosing contract and type below. | threading.Event | Enclosing invocation or class/instance lifetime | 179 |
| _Slot | preview | Typed binding for preview in _Slot; use the enclosing contract and type below. | Preview &#124; None | Enclosing invocation or class/instance lifetime | 180 |
| WidgetPanel.__init__ | self | Owning instance; its attributes retain state for the instance lifetime. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 187 |
| WidgetPanel.__init__ | review | Parameter for review in WidgetPanel.__init__; use the enclosing contract and type below. | Callable[[], Capability] | Enclosing invocation or class/instance lifetime | 188 |
| WidgetPanel.__init__ | start | Parameter for start in WidgetPanel.__init__; use the enclosing contract and type below. | Callable[[Capability, str], Preview] | Enclosing invocation or class/instance lifetime | 189 |
| WidgetPanel.__init__ | capacity | Parameter for capacity in WidgetPanel.__init__; use the enclosing contract and type below. | int | Enclosing invocation or class/instance lifetime | 191 |
| WidgetPanel.__init__ | self.review | Attribute for review in WidgetPanel.__init__; use the enclosing contract and type below. | tuple | Enclosing invocation or class/instance lifetime | 196 |
| WidgetPanel.__init__ | self.start | Attribute for start in WidgetPanel.__init__; use the enclosing contract and type below. | tuple | Enclosing invocation or class/instance lifetime | 196 |
| WidgetPanel.__init__ | self.capacity | Attribute for capacity in WidgetPanel.__init__; use the enclosing contract and type below. | tuple | Enclosing invocation or class/instance lifetime | 196 |
| WidgetPanel.__init__ | self.slots | Attribute for slots in WidgetPanel.__init__; use the enclosing contract and type below. | dict[str, _Slot] | Enclosing invocation or class/instance lifetime | 197 |
| WidgetPanel.__init__ | self.lock | Attribute for lock in WidgetPanel.__init__; use the enclosing contract and type below. | Return type of Lock; see its callable contract | Enclosing invocation or class/instance lifetime | 198 |
| WidgetPanel.open | self | Owning instance; its attributes retain state for the instance lifetime. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 201 |
| WidgetPanel.open | owner | Parameter for owner in WidgetPanel.open; use the enclosing contract and type below. | str | Enclosing invocation or class/instance lifetime | 201 |
| WidgetPanel.open | parent_origin | Parameter for parent origin in WidgetPanel.open; use the enclosing contract and type below. | str | Enclosing invocation or class/instance lifetime | 201 |
| WidgetPanel.open | expired | Local binding for expired in WidgetPanel.open; use the enclosing contract and type below. | tuple | Enclosing invocation or class/instance lifetime | 205 |
| WidgetPanel.open | reusable | Local binding for reusable in WidgetPanel.open; use the enclosing contract and type below. | tuple | Enclosing invocation or class/instance lifetime | 205, 215 |
| WidgetPanel.open | slot | Local binding for slot in WidgetPanel.open; use the enclosing contract and type below. | tuple | Enclosing invocation or class/instance lifetime | 205, 219 |
| WidgetPanel.open | identity | Explicit owner identity used by a session factory or fixture. | Element of the declared iterable | Enclosing invocation or class/instance lifetime | 207 |
| WidgetPanel.open | previous | Loop item for previous in WidgetPanel.open; use the enclosing contract and type below. | Element of the declared iterable | Enclosing invocation or class/instance lifetime | 207, 223 |
| WidgetPanel.open | existing | Local binding for existing in WidgetPanel.open; use the enclosing contract and type below. | Return type of get; see its callable contract | Enclosing invocation or class/instance lifetime | 211 |
| WidgetPanel.open | preview | Local binding for preview in WidgetPanel.open; use the enclosing contract and type below. | NoneType | Enclosing invocation or class/instance lifetime | 221, 230 |
| WidgetPanel.open | approved | Local binding for approved in WidgetPanel.open; use the enclosing contract and type below. | Return type of review; see its callable contract | Enclosing invocation or class/instance lifetime | 227 |
| WidgetPanel.open | slot.preview | Attribute for slot.preview in WidgetPanel.open; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 234 |
| WidgetPanel.close | self | Owning instance; its attributes retain state for the instance lifetime. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 245 |
| WidgetPanel.close | owner | Parameter for owner in WidgetPanel.close; use the enclosing contract and type below. | str | Enclosing invocation or class/instance lifetime | 245 |
| WidgetPanel.close | slot | Local binding for slot in WidgetPanel.close; use the enclosing contract and type below. | Return type of get; see its callable contract | Enclosing invocation or class/instance lifetime | 248 |
| WidgetPanel.close | preview | Local binding for preview in WidgetPanel.close; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 252 |
| WidgetPanel.status | self | Owning instance; its attributes retain state for the instance lifetime. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 260 |
| WidgetPanel.status | owner | Parameter for owner in WidgetPanel.status; use the enclosing contract and type below. | str | Enclosing invocation or class/instance lifetime | 260 |
| WidgetPanel.status | slot | Local binding for slot in WidgetPanel.status; use the enclosing contract and type below. | Return type of get; see its callable contract | Enclosing invocation or class/instance lifetime | 263 |
| WidgetPanel.close_all | self | Owning instance; its attributes retain state for the instance lifetime. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 274 |
| WidgetPanel.close_all | owners | Local binding for owners in WidgetPanel.close_all; use the enclosing contract and type below. | Return type of list; see its callable contract | Enclosing invocation or class/instance lifetime | 277 |
| WidgetPanel.close_all | owner | Loop item for owner in WidgetPanel.close_all; use the enclosing contract and type below. | Element of the declared iterable | Enclosing invocation or class/instance lifetime | 278 |
