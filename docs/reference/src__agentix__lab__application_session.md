# Reference for src/agentix/lab/application_session.py

Composite application snapshots executed inside the existing native ASGI boundary.

Only browser HTTP uses IPC. Tool imports/calls remain inside the application worker;
legacy host RPC requests are explicitly rejected. Headless use imports no Gradio.

Source fingerprint: 888b2cc782c3dbc57690563990f992e53ac014a317dcc78e1400efee7099dd5f

This reference is generated from maintained source without imports or execution. Assigned values are intentionally omitted. Runtime-dependent types are explicit; the enclosing docstring defines the behavioral contract. See [architecture](../ARCHITECTURE_QUALITY.md) for manually reviewed responsibility and dependency decisions.

## Classes and callables

### served_style

Render one scoped stylesheet for the served page, not for the saved file.

The preview's own sheet forces radius and background with ``!important`` at
specificity (0,5,0), so a plain ``:where()`` rule loses there. The served copy
repeats ``[id]`` to reach (0,10,0) and marks every declaration important.
Gradio prefixes its startup copy with three container classes. A restaged
copy adds four more attribute selectors so a saved style beats that snapshot.
The reviewed file on disk keeps its plain form.

Kind: callable. Declared return: bytes. Source line: 20.

### served_style.strengthen

Mark each declaration important and repeat font rules on form controls.

A form control does not inherit font from its container, so the text a user
reads keeps the framework font unless the served sheet targets it directly.

Kind: callable. Declared return: str. Source line: 40.

### WidgetTestsFailed

Carry bounded private diagnostic data without exposing child text in user errors.

Kind: class. Declared return: Not declared / class. Source line: 85.

### WidgetTestsFailed.__init__

Copy bounded JSON diagnostics; the report cannot establish successful execution.

Kind: callable. Declared return: None. Source line: 88.

### ApplicationSession

Reuse maintained transport/job lifecycle with a complete reviewed application payload.

Kind: class. Declared return: Not declared / class. Source line: 97.

### ApplicationSession.__init__

Validate capability and optional strict JSON input before allocating native resources.

Kind: callable. Declared return: None. Source line: 100.

### ApplicationSession._stage_payload

Write immutable reviewed snapshots, never reread sources from their original paths.

Kind: callable. Declared return: None. Source line: 145.

### ApplicationSession.restage_styles

Rewrite the served stylesheet so any page load sees the saved style.

``_stage_payload`` writes ``application.css`` once at startup. A style saved
afterwards must reach that same file, otherwise a reload and the separate
"View as web" tab keep serving the old declarations. The member bytes are
accumulated in a session-owned copy of the immutable approved snapshot.
Scoped styles are rebuilt with the same tool-to-instance rewrite used at
startup, plus four attribute selectors to outrank Gradio's prefixed copy
of the original startup stylesheet. The owner writes each individual CSS
member before calling this method; this method only writes the served sheet.

Kind: callable. Declared return: None. Source line: 179.

### ApplicationSession._worker_arguments

Select only maintained application/headless worker modes.

Kind: callable. Declared return: list[str]. Source line: 213.

### ApplicationSession._check_runtime

Kill the owned job when a reviewed callback exceeds 45 seconds.

Kind: callable. Declared return: None. Source line: 226.

### ApplicationSession._control_message

Validate structured result separately; it is not a proof of semantic correctness.

Kind: callable. Declared return: bool. Source line: 234.

### ApplicationSession._invoke_tool

Deny legacy host tool capabilities; application tools must execute in the child.

Kind: callable. Declared return: None. Source line: 272.

### execute_application

Run the reviewed composite data operation natively without UI/server startup.

Validate host-observed successful process exit as well as result shape. Native
execution establishes isolation, not functional correctness of arbitrary code.

Kind: callable. Declared return: dict[str, object]. Source line: 278.

### run_application_widget_tests

Run only new reviewed widget test modules natively; success remains provisional.

Kind: callable. Declared return: dict. Source line: 298.

## Variables and parameters

| Scope | Name | Role and meaning | Type | Lifetime | Writes |
| --- | --- | --- | --- | --- | --- |
| module | json | Imported dependency for json in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 7 |
| module | re | Imported dependency for re in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 8 |
| module | time | Imported dependency for time in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 9 |
| module | TypeAdapter | Imported dependency for TypeAdapter in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 11 |
| module | ApprovedApplication | Imported dependency for ApprovedApplication in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 13 |
| module | validate_result | Imported dependency for validate result in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 13 |
| module | Text | Imported dependency for Text in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 14 |
| module | WidgetSession | Imported dependency for WidgetSession in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 15 |
| module | STYLE_MARKER | Module binding for STYLE MARKER in module; use the enclosing contract and type below. | bytes | Module/process lifetime | 17 |
| served_style | css | Parameter for css in served_style; use the enclosing contract and type below. | bytes | Enclosing invocation or class/instance lifetime | 20 |
| served_style | tool | Parameter for tool in served_style; use the enclosing contract and type below. | str | Enclosing invocation or class/instance lifetime | 20 |
| served_style | node_id | Parameter for node id in served_style; use the enclosing contract and type below. | str | Enclosing invocation or class/instance lifetime | 20 |
| served_style | restaged | Parameter for restaged in served_style; use the enclosing contract and type below. | bool | Enclosing invocation or class/instance lifetime | 20 |
| served_style | scoped | Local binding for scoped in served_style; use the enclosing contract and type below. | Return type of decode; see its callable contract | Enclosing invocation or class/instance lifetime | 30, 34 |
| served_style | repetitions | Local binding for repetitions in served_style; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 33 |
| served_style.lambda_36 | match | Callback parameter for match in served_style.lambda_36; use the enclosing contract and type below. | Defined by the enclosing callback contract | Enclosing invocation or class/instance lifetime | 36 |
| served_style.strengthen | match | Parameter for match in served_style.strengthen; use the enclosing contract and type below. | re.Match | Enclosing invocation or class/instance lifetime | 40 |
| served_style.strengthen | declarations | Local binding for declarations in served_style.strengthen; use the enclosing contract and type below. | list | Enclosing invocation or class/instance lifetime | 46 |
| served_style.strengthen.comprehension_46 | part | Comprehension item for part in served_style.strengthen.comprehension_46; use the enclosing contract and type below. | Element of the declared iterable | This comprehension only; does not leak into its enclosing scope | 46 |
| served_style.strengthen | body | Local binding for body in served_style.strengthen; use the enclosing contract and type below. | Return type of join; see its callable contract | Enclosing invocation or class/instance lifetime | 47 |
| served_style.strengthen.comprehension_47 | part | Comprehension item for part in served_style.strengthen.comprehension_47; use the enclosing contract and type below. | Element of the declared iterable | This comprehension only; does not leak into its enclosing scope | 48 |
| served_style | rendered | Local binding for rendered in served_style; use the enclosing contract and type below. | Return type of sub; see its callable contract | Enclosing invocation or class/instance lifetime | 52 |
| served_style | font_rules | Local binding for font rules in served_style; use the enclosing contract and type below. | list | Enclosing invocation or class/instance lifetime | 53 |
| served_style | selector | Loop item for selector in served_style; use the enclosing contract and type below. | Element of the declared iterable | Enclosing invocation or class/instance lifetime | 54 |
| served_style | body | Loop item for body in served_style; use the enclosing contract and type below. | Element of the declared iterable | Enclosing invocation or class/instance lifetime | 54 |
| served_style | fonts | Local binding for fonts in served_style; use the enclosing contract and type below. | list | Enclosing invocation or class/instance lifetime | 55 |
| served_style.comprehension_55 | part | Comprehension item for part in served_style.comprehension_55; use the enclosing contract and type below. | Element of the declared iterable | This comprehension only; does not leak into its enclosing scope | 57 |
| served_style | base | Local binding for base in served_style; use the enclosing contract and type below. | Return type of strip; see its callable contract | Enclosing invocation or class/instance lifetime | 62 |
| served_style | subject | Local binding for subject in served_style; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 68 |
| served_style | targets | Local binding for targets in served_style; use the enclosing contract and type below. | tuple | Enclosing invocation or class/instance lifetime | 70, 72 |
| served_style | controls | Local binding for controls in served_style; use the enclosing contract and type below. | Return type of join; see its callable contract | Enclosing invocation or class/instance lifetime | 80 |
| served_style.comprehension_80 | tag | Comprehension item for tag in served_style.comprehension_80; use the enclosing contract and type below. | Element of the declared iterable | This comprehension only; does not leak into its enclosing scope | 80 |
| WidgetTestsFailed.__init__ | self | Owning instance; its attributes retain state for the instance lifetime. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 88 |
| WidgetTestsFailed.__init__ | report | Parameter for report in WidgetTestsFailed.__init__; use the enclosing contract and type below. | dict | Enclosing invocation or class/instance lifetime | 88 |
| WidgetTestsFailed.__init__ | encoded | Local binding for encoded in WidgetTestsFailed.__init__; use the enclosing contract and type below. | Return type of dumps; see its callable contract | Enclosing invocation or class/instance lifetime | 91 |
| WidgetTestsFailed.__init__ | self.report | Attribute for report in WidgetTestsFailed.__init__; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 92 |
| ApplicationSession.__init__ | self | Owning instance; its attributes retain state for the instance lifetime. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 101 |
| ApplicationSession.__init__ | approved | Parameter for approved in ApplicationSession.__init__; use the enclosing contract and type below. | ApprovedApplication | Enclosing invocation or class/instance lifetime | 102 |
| ApplicationSession.__init__ | payload | Parameter for payload in ApplicationSession.__init__; use the enclosing contract and type below. | dict &#124; None | Enclosing invocation or class/instance lifetime | 104, 124, 128 |
| ApplicationSession.__init__ | lifetime | Parameter for lifetime in ApplicationSession.__init__; use the enclosing contract and type below. | int &#124; None | Enclosing invocation or class/instance lifetime | 105 |
| ApplicationSession.__init__ | widget_tests | Parameter for widget tests in ApplicationSession.__init__; use the enclosing contract and type below. | list[str] &#124; None | Enclosing invocation or class/instance lifetime | 106 |
| ApplicationSession.__init__ | display_name | Parameter for display name in ApplicationSession.__init__; use the enclosing contract and type below. | str | Enclosing invocation or class/instance lifetime | 107 |
| ApplicationSession.__init__ | self.display_name | Attribute for display name in ApplicationSession.__init__; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 116 |
| ApplicationSession.__init__ | self.manifest | Versioned inventory or launch record; not an execution-authorization capability. | Return type of loads; see its callable contract | Enclosing invocation or class/instance lifetime | 117 |
| ApplicationSession.__init__ | validate_payload | Imported dependency for validate payload in ApplicationSession.__init__; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 122 |
| ApplicationSession.__init__ | self.widget_tests | Attribute for widget tests in ApplicationSession.__init__; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 137 |
| ApplicationSession.__init__ | self.application | Attribute for application in ApplicationSession.__init__; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 139 |
| ApplicationSession.__init__ | self.payload | Attribute for payload in ApplicationSession.__init__; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 140 |
| ApplicationSession.__init__ | self.headless | Attribute for headless in ApplicationSession.__init__; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 141 |
| ApplicationSession.__init__ | self.clock | Attribute for clock in ApplicationSession.__init__; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 142 |
| ApplicationSession.__init__ | self.callback_leases | Attribute for callback leases in ApplicationSession.__init__; use the enclosing contract and type below. | dict[str, float] | Enclosing invocation or class/instance lifetime | 143 |
| ApplicationSession._stage_payload | self | Owning instance; its attributes retain state for the instance lifetime. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 145 |
| ApplicationSession._stage_payload | name | Current identifier selected by parsing, lookup or dependency registration. | Element of the declared iterable | Enclosing invocation or class/instance lifetime | 147 |
| ApplicationSession._stage_payload | content | Artifact or review text whose encoding, size and approval state must be checked. | Element of the declared iterable | Enclosing invocation or class/instance lifetime | 147 |
| ApplicationSession._stage_payload | styles | Local binding for styles in ApplicationSession._stage_payload; use the enclosing contract and type below. | list | Enclosing invocation or class/instance lifetime | 149, 154 |
| ApplicationSession._stage_payload.comprehension_149 | name | Current identifier selected by parsing, lookup or dependency registration. | Element of the declared iterable | This comprehension only; does not leak into its enclosing scope | 150 |
| ApplicationSession._stage_payload.comprehension_149 | content | Artifact or review text whose encoding, size and approval state must be checked. | Element of the declared iterable | This comprehension only; does not leak into its enclosing scope | 150 |
| ApplicationSession._stage_payload | members | Local binding for members in ApplicationSession._stage_payload; use the enclosing contract and type below. | Return type of dict; see its callable contract | Enclosing invocation or class/instance lifetime | 153 |
| ApplicationSession._stage_payload.comprehension_154 | node | Comprehension item for node in ApplicationSession._stage_payload.comprehension_154; use the enclosing contract and type below. | Element of the declared iterable | This comprehension only; does not leak into its enclosing scope | 156 |
| ApplicationSession._stage_payload | css_path | Local binding for css path in ApplicationSession._stage_payload; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 162 |
| ApplicationSession.restage_styles | self | Owning instance; its attributes retain state for the instance lifetime. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 179 |
| ApplicationSession.restage_styles | member | Parameter for member in ApplicationSession.restage_styles; use the enclosing contract and type below. | str | Enclosing invocation or class/instance lifetime | 179 |
| ApplicationSession.restage_styles | css | Parameter for css in ApplicationSession.restage_styles; use the enclosing contract and type below. | str | Enclosing invocation or class/instance lifetime | 179 |
| ApplicationSession.restage_styles | members | Local binding for members in ApplicationSession.restage_styles; use the enclosing contract and type below. | Return type of dict; see its callable contract | Enclosing invocation or class/instance lifetime | 191 |
| ApplicationSession.restage_styles | styles | Local binding for styles in ApplicationSession.restage_styles; use the enclosing contract and type below. | list | Enclosing invocation or class/instance lifetime | 195 |
| ApplicationSession.restage_styles.comprehension_195 | node | Comprehension item for node in ApplicationSession.restage_styles.comprehension_195; use the enclosing contract and type below. | Element of the declared iterable | This comprehension only; does not leak into its enclosing scope | 199 |
| ApplicationSession.restage_styles | current | Local binding for current in ApplicationSession.restage_styles; use the enclosing contract and type below. | Return type of read_bytes; see its callable contract | Enclosing invocation or class/instance lifetime | 204 |
| ApplicationSession.restage_styles | base | Local binding for base in ApplicationSession.restage_styles; use the enclosing contract and type below. | Return type of rstrip; see its callable contract | Enclosing invocation or class/instance lifetime | 205 |
| ApplicationSession.restage_styles | self._staged_style_members | Attribute for staged style members in ApplicationSession.restage_styles; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 211 |
| ApplicationSession._worker_arguments | self | Owning instance; its attributes retain state for the instance lifetime. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 213 |
| ApplicationSession._check_runtime | self | Owning instance; its attributes retain state for the instance lifetime. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 226 |
| ApplicationSession._check_runtime | expired | Local binding for expired in ApplicationSession._check_runtime; use the enclosing contract and type below. | Return type of any; see its callable contract | Enclosing invocation or class/instance lifetime | 229 |
| ApplicationSession._check_runtime.comprehension_229 | started | Comprehension item for started in ApplicationSession._check_runtime.comprehension_229; use the enclosing contract and type below. | Element of the declared iterable | This comprehension only; does not leak into its enclosing scope | 229 |
| ApplicationSession._control_message | self | Owning instance; its attributes retain state for the instance lifetime. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 234 |
| ApplicationSession._control_message | message | Parameter for message in ApplicationSession._control_message; use the enclosing contract and type below. | dict | Enclosing invocation or class/instance lifetime | 234 |
| ApplicationSession._control_message | kind | Local binding for kind in ApplicationSession._control_message; use the enclosing contract and type below. | Return type of get; see its callable contract | Enclosing invocation or class/instance lifetime | 236 |
| ApplicationSession._control_message | identity | Explicit owner identity used by a session factory or fixture. | Return type of get; see its callable contract | Enclosing invocation or class/instance lifetime | 242 |
| ApplicationSession._control_message.comprehension_247 | c | Comprehension item for c in ApplicationSession._control_message.comprehension_247; use the enclosing contract and type below. | Element of the declared iterable | This comprehension only; does not leak into its enclosing scope | 247 |
| ApplicationSession._invoke_tool | self | Owning instance; its attributes retain state for the instance lifetime. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 272 |
| ApplicationSession._invoke_tool | message | Parameter for message in ApplicationSession._invoke_tool; use the enclosing contract and type below. | dict | Enclosing invocation or class/instance lifetime | 272 |
| execute_application | approved | Parameter for approved in execute_application; use the enclosing contract and type below. | ApprovedApplication | Enclosing invocation or class/instance lifetime | 278 |
| execute_application | payload | Parameter for payload in execute_application; use the enclosing contract and type below. | dict | Enclosing invocation or class/instance lifetime | 278 |
| execute_application | session | Managed resource for session in execute_application; use the enclosing contract and type below. | Return type of ApplicationSession; see its callable contract | Context-manager block; exit invokes its cleanup protocol | 284 |
| execute_application | observation | Local binding for observation in execute_application; use the enclosing contract and type below. | Return type of get; see its callable contract | Enclosing invocation or class/instance lifetime | 287 |
| run_application_widget_tests | approved | Parameter for approved in run_application_widget_tests; use the enclosing contract and type below. | ApprovedApplication | Enclosing invocation or class/instance lifetime | 298 |
| run_application_widget_tests | names | Parameter for names in run_application_widget_tests; use the enclosing contract and type below. | list[str] | Enclosing invocation or class/instance lifetime | 298 |
| run_application_widget_tests | session | Managed resource for session in run_application_widget_tests; use the enclosing contract and type below. | Return type of ApplicationSession; see its callable contract | Context-manager block; exit invokes its cleanup protocol | 300 |
| run_application_widget_tests | observation | Local binding for observation in run_application_widget_tests; use the enclosing contract and type below. | Return type of get; see its callable contract | Enclosing invocation or class/instance lifetime | 302 |
| run_application_widget_tests | report | Local binding for report in run_application_widget_tests; use the enclosing contract and type below. | Return type of get; see its callable contract | Enclosing invocation or class/instance lifetime | 303 |
