# Reference for src/agentix/storage/widget_store.py

Authenticated persistent widget reuse; implementation lives beside its installed tool.

Only the maintained host publishes after explicit review and independent success.
Protected records are separate from untrusted tool storage. No source is imported.

Source fingerprint: c36f81cf6178d9a40d73a5d6da7a6c385c630b8e77150a1419b14a461c0c5437

This reference is generated from maintained source without imports or execution. Assigned values are intentionally omitted. Runtime-dependent types are explicit; the enclosing docstring defines the behavioral contract. See [architecture](../ARCHITECTURE_QUALITY.md) for manually reviewed responsibility and dependency decisions.

## Classes and callables

### StoredWidget

Proposal bytes and whether the exact current binding retains prior approval.

Kind: class. Declared return: Not declared / class. Source line: 24.

### widget_policy

Bind runtime and maintained widget/context contracts, never traverse tools.

Kind: callable. Declared return: str. Source line: 32.

### WidgetStore

Protect reusable widget approval and exact per-tool source under Windows user scope.

Kind: class. Declared return: Not declared / class. Source line: 49.

### WidgetStore.__init__

Inject protection/storage; construction never reads or writes tool artifacts.

Kind: callable. Declared return: None. Source line: 52.

### WidgetStore.for_controller

Compose persistent user-local records outside installed tool storage.

Kind: callable. Declared return: 'WidgetStore'. Source line: 65.

### WidgetStore._binding

Describe exact reviewed dependencies without persisting executable trust markers.

Kind: callable. Declared return: dict. Source line: 70.

### WidgetStore._companion

Resolve one exact widget member and reject links before reads or writes.

Kind: callable. Declared return: Path. Source line: 83.

### WidgetStore.load

Reuse exact approvals, or present changed source as unapproved without regeneration.

Authentication failures are explicit errors; ordinary absence means no widget
has been published. Reads are bounded and never execute source or tests.

Kind: callable. Declared return: StoredWidget | None. Source line: 103.

### WidgetStore._validate

Check bounded proposal data and static interface before any persistence.

Kind: callable. Declared return: None. Source line: 155.

### WidgetStore.publish

Publish only after the caller's human/native/browser gates succeed.

This trusted internal method is not a model/UI API. A partial filesystem
failure cannot create a valid old grant for changed bytes. Existing tool
source and tests are never modified; only its conventional widget is written.

Kind: callable. Declared return: None. Source line: 166.

## Variables and parameters

| Scope | Name | Role and meaning | Type | Lifetime | Writes |
| --- | --- | --- | --- | --- | --- |
| module | hashlib | Imported dependency for hashlib in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 7 |
| module | json | Imported dependency for json in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 8 |
| module | logging | Imported dependency for logging in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 9 |
| module | dataclass | Imported dependency for dataclass in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 10 |
| module | Path | Imported dependency for Path in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 11 |
| module | Any | Imported dependency for Any in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 12 |
| module | validate_source | Imported dependency for validate source in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 14 |
| module | ApprovalStore | Imported dependency for ApprovalStore in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 15 |
| module | WindowsDataProtection | Imported dependency for WindowsDataProtection in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 16 |
| module | ApprovedTool | Imported dependency for ApprovedTool in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 17 |
| module | data_directory | Imported dependency for data directory in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 18 |
| module | logger | Module logger emitting bounded operation diagnostics rather than artifact bodies. | Return type of getLogger; see its callable contract | Module/process lifetime | 20 |
| StoredWidget | proposal | Typed binding for proposal in StoredWidget; use the enclosing contract and type below. | dict[str, str] | Enclosing invocation or class/instance lifetime | 27 |
| StoredWidget | approved | Typed binding for approved in StoredWidget; use the enclosing contract and type below. | bool | Enclosing invocation or class/instance lifetime | 28 |
| StoredWidget | css | Typed binding for css in StoredWidget; use the enclosing contract and type below. | str | Enclosing invocation or class/instance lifetime | 29 |
| widget_policy | root | Explicit root directory against which named paths are resolved. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 34 |
| widget_policy | digest | Content fingerprint for change detection; not a substitute for human approval. | Return type of sha256; see its callable contract | Enclosing invocation or class/instance lifetime | 35 |
| widget_policy | path | Path under validation or an explicitly scoped maintained source path. | Element of the declared iterable | Enclosing invocation or class/instance lifetime | 36 |
| WidgetStore.__init__ | self | Owning instance; its attributes retain state for the instance lifetime. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 53 |
| WidgetStore.__init__ | security | Owner-scoped approval and path boundary injected into this service. | Any | Enclosing invocation or class/instance lifetime | 53 |
| WidgetStore.__init__ | directory | Parameter for directory in WidgetStore.__init__; use the enclosing contract and type below. | Path | Enclosing invocation or class/instance lifetime | 53 |
| WidgetStore.__init__ | protector | Parameter for protector in WidgetStore.__init__; use the enclosing contract and type below. | Any | Enclosing invocation or class/instance lifetime | 53 |
| WidgetStore.__init__ | policy | Parameter for policy in WidgetStore.__init__; use the enclosing contract and type below. | str &#124; None | Enclosing invocation or class/instance lifetime | 53 |
| WidgetStore.__init__ | self.security | Owner-scoped approval and path boundary injected into this service. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 56 |
| WidgetStore.__init__ | self.records | Attribute for records in WidgetStore.__init__; use the enclosing contract and type below. | Return type of ApprovalStore; see its callable contract | Enclosing invocation or class/instance lifetime | 57 |
| WidgetStore.for_controller | cls | Class receiving this class-level operation. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 65 |
| WidgetStore.for_controller | controller | Parameter for controller in WidgetStore.for_controller; use the enclosing contract and type below. | Any | Enclosing invocation or class/instance lifetime | 65 |
| WidgetStore.for_controller | root | Explicit root directory against which named paths are resolved. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 67 |
| WidgetStore._binding | self | Owning instance; its attributes retain state for the instance lifetime. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 70 |
| WidgetStore._binding | tool | Parameter for tool in WidgetStore._binding; use the enclosing contract and type below. | ApprovedTool | Enclosing invocation or class/instance lifetime | 70 |
| WidgetStore._companion | self | Owning instance; its attributes retain state for the instance lifetime. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 83 |
| WidgetStore._companion | tool | Parameter for tool in WidgetStore._companion; use the enclosing contract and type below. | ApprovedTool | Enclosing invocation or class/instance lifetime | 83 |
| WidgetStore._companion | suffix | Parameter for suffix in WidgetStore._companion; use the enclosing contract and type below. | str | Enclosing invocation or class/instance lifetime | 83 |
| WidgetStore._companion | expected | Reviewed expected observation kept outside untrusted child execution. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 87 |
| WidgetStore._companion | resolved | Local binding for resolved in WidgetStore._companion; use the enclosing contract and type below. | Return type of Path; see its callable contract | Enclosing invocation or class/instance lifetime | 92 |
| WidgetStore.load | self | Owning instance; its attributes retain state for the instance lifetime. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 103 |
| WidgetStore.load | tool | Parameter for tool in WidgetStore.load; use the enclosing contract and type below. | ApprovedTool | Enclosing invocation or class/instance lifetime | 103 |
| WidgetStore.load | path | Path under validation or an explicitly scoped maintained source path. | tuple | Enclosing invocation or class/instance lifetime | 109 |
| WidgetStore.load | record_path | Local binding for record path in WidgetStore.load; use the enclosing contract and type below. | tuple | Enclosing invocation or class/instance lifetime | 109 |
| WidgetStore.load | stream | Managed resource for stream in WidgetStore.load; use the enclosing contract and type below. | Return type of open; see its callable contract | Context-manager block; exit invokes its cleanup protocol | 116, 130 |
| WidgetStore.load | sealed | Local binding for sealed in WidgetStore.load; use the enclosing contract and type below. | Return type of read; see its callable contract | Enclosing invocation or class/instance lifetime | 117 |
| WidgetStore.load | raw | Local binding for raw in WidgetStore.load; use the enclosing contract and type below. | Return type of unseal; see its callable contract | Enclosing invocation or class/instance lifetime | 120 |
| WidgetStore.load | record | Local binding for record in WidgetStore.load; use the enclosing contract and type below. | Return type of loads; see its callable contract | Enclosing invocation or class/instance lifetime | 123 |
| WidgetStore.load | proposal | Local binding for proposal in WidgetStore.load; use the enclosing contract and type below. | Return type of dict; see its callable contract | Enclosing invocation or class/instance lifetime | 128 |
| WidgetStore.load | source | Explicit source document or source-code text; never imported for reference generation. | Return type of read; see its callable contract | Enclosing invocation or class/instance lifetime | 131 |
| WidgetStore.load | validate_widget_css | Imported dependency for validate widget css in WidgetStore.load; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 134 |
| WidgetStore.load | css_path | Local binding for css path in WidgetStore.load; use the enclosing contract and type below. | Return type of _companion; see its callable contract | Enclosing invocation or class/instance lifetime | 136 |
| WidgetStore.load | tests_path | Local binding for tests path in WidgetStore.load; use the enclosing contract and type below. | Return type of _companion; see its callable contract | Enclosing invocation or class/instance lifetime | 137 |
| WidgetStore.load | member | Loop item for member in WidgetStore.load; use the enclosing contract and type below. | Element of the declared iterable | Enclosing invocation or class/instance lifetime | 138 |
| WidgetStore.load | css | Local binding for css in WidgetStore.load; use the enclosing contract and type below. | Return type of validate_widget_css; see its callable contract | Enclosing invocation or class/instance lifetime | 141 |
| WidgetStore.load | approved | Local binding for approved in WidgetStore.load; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 142 |
| WidgetStore._validate | self | Owning instance; its attributes retain state for the instance lifetime. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 155 |
| WidgetStore._validate | tool | Parameter for tool in WidgetStore._validate; use the enclosing contract and type below. | ApprovedTool | Enclosing invocation or class/instance lifetime | 155 |
| WidgetStore._validate | proposal | Parameter for proposal in WidgetStore._validate; use the enclosing contract and type below. | dict | Enclosing invocation or class/instance lifetime | 155 |
| WidgetStore._validate.comprehension_157 | value | Value at the current validation/rendering boundary; apply the enclosing contract. | Element of the declared iterable | This comprehension only; does not leak into its enclosing scope | 159 |
| WidgetStore._validate | module | Local binding for module in WidgetStore._validate; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 162 |
| WidgetStore.publish | self | Owning instance; its attributes retain state for the instance lifetime. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 167 |
| WidgetStore.publish | tool | Parameter for tool in WidgetStore.publish; use the enclosing contract and type below. | ApprovedTool | Enclosing invocation or class/instance lifetime | 167 |
| WidgetStore.publish | proposal | Parameter for proposal in WidgetStore.publish; use the enclosing contract and type below. | dict[str, str] | Enclosing invocation or class/instance lifetime | 167 |
| WidgetStore.publish | css | Parameter for css in WidgetStore.publish; use the enclosing contract and type below. | str &#124; None | Enclosing invocation or class/instance lifetime | 167, 178 |
| WidgetStore.publish | default_widget_css | Imported dependency for default widget css in WidgetStore.publish; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 176 |
| WidgetStore.publish | validate_widget_css | Imported dependency for validate widget css in WidgetStore.publish; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 176 |
| WidgetStore.publish | source | Explicit source document or source-code text; never imported for reference generation. | Return type of encode; see its callable contract | Enclosing invocation or class/instance lifetime | 179 |
| WidgetStore.publish | record | Local binding for record in WidgetStore.publish; use the enclosing contract and type below. | dict | Enclosing invocation or class/instance lifetime | 180 |
| WidgetStore.publish | raw | Local binding for raw in WidgetStore.publish; use the enclosing contract and type below. | Return type of encode; see its callable contract | Enclosing invocation or class/instance lifetime | 187 |
| WidgetStore.publish | sealed | Local binding for sealed in WidgetStore.publish; use the enclosing contract and type below. | Return type of seal; see its callable contract | Enclosing invocation or class/instance lifetime | 190 |
| WidgetStore.publish | target | Local binding for target in WidgetStore.publish; use the enclosing contract and type below. | Return type of _companion; see its callable contract | Enclosing invocation or class/instance lifetime | 193 |
| WidgetStore.publish | css_target | Local binding for css target in WidgetStore.publish; use the enclosing contract and type below. | Return type of _companion; see its callable contract | Enclosing invocation or class/instance lifetime | 194 |
| WidgetStore.publish | tests_target | Local binding for tests target in WidgetStore.publish; use the enclosing contract and type below. | Return type of _companion; see its callable contract | Enclosing invocation or class/instance lifetime | 195 |
| WidgetStore.publish | record_path | Local binding for record path in WidgetStore.publish; use the enclosing contract and type below. | Return type of _path; see its callable contract | Enclosing invocation or class/instance lifetime | 196 |
