# Reference for src/agentix/ui/sessions.py

Bounded server-owned workflow sessions with owner-bound opaque tokens.

Gradio session hashes provide routing, not account authentication. Tokens remain
in server-side State, and every callback must verify both token and request owner.

Source fingerprint: ebc7097ff065c23590ca4ca9676cf5495e41beb04be595ac54a7a6169fa320b2

This reference is generated from maintained source without imports or execution. Assigned values are intentionally omitted. Runtime-dependent types are explicit; the enclosing docstring defines the behavioral contract. See [architecture](../ARCHITECTURE_QUALITY.md) for manually reviewed responsibility and dependency decisions.

## Classes and callables

### SessionAccessError

A stale, unknown or cross-owner session cannot be accessed.

Kind: class. Declared return: Not declared / class. Source line: 18.

### Session

Registry-owned session identity, controller and last activity timestamp.

Kind: class. Declared return: Not declared / class. Source line: 23.

### SessionRegistry

Create isolated controllers and reject foreign/stale browser tokens.

Kind: class. Declared return: Not declared / class. Source line: 33.

### SessionRegistry.__init__

Configure bounded sessions; construction creates no runtime or model.

Kind: callable. Declared return: None. Source line: 36.

### SessionRegistry._remove

Cancel pending writes before dropping a closed/expired owner's state.

Kind: callable. Declared return: None. Source line: 53.

### SessionRegistry.resolve

Return/create this owner's session, rejecting untrusted token changes.

Initial callbacks can race with no token; the owner index makes creation
idempotent. Active workers are not silently evicted by idle expiry.

Kind: callable. Declared return: Session. Source line: 63.

### SessionRegistry.close

Close only a matching owner; stale/unrelated unloads cannot cancel work.

Kind: callable. Declared return: None. Source line: 98.

### SessionRegistry.close_state

Trusted Gradio State cleanup hook; never register as a public callback.

Kind: callable. Declared return: None. Source line: 105.

### SessionRegistry.close_owner

Handle a trusted framework unload request without requiring UI inputs.

Kind: callable. Declared return: None. Source line: 112.

### SessionCallbacks

Framework-independent browser callbacks; every operation rechecks ownership.

Kind: class. Declared return: Not declared / class. Source line: 120.

### SessionCallbacks.__init__

Retain only the server registry, never a global active controller.

Kind: callable. Declared return: None. Source line: 123.

### SessionCallbacks._session

Resolve trusted framework routing metadata and opaque server State.

Kind: callable. Declared return: Session. Source line: 127.

### SessionCallbacks.submit

Submit to this browser's controller and update its server State token.

Kind: callable. Declared return: tuple[Any, ...]. Source line: 131.

### SessionCallbacks.poll

Return a coherent editor/request-ID snapshot for this browser only.

Kind: callable. Declared return: tuple[Any, ...]. Source line: 136.

### SessionCallbacks.approve

Approve only the displayed request through the verified owner controller.

Kind: callable. Declared return: bool. Source line: 141.

### SessionCallbacks.reject

Reject only the displayed request through the verified owner controller.

Kind: callable. Declared return: bool. Source line: 146.

### SessionCallbacks.toggle

Update this owner's setting and return its server State token.

Kind: callable. Declared return: str. Source line: 151.

### SessionCallbacks.configure_model

Verify browser ownership; clear the key input on both success and failure.

Kind: callable. Declared return: tuple[str, str, str]. Source line: 157.

### SessionCallbacks.model_menu

Dispatch fixed profile actions after owner checks; never return secrets.

Kind: callable. Declared return: tuple[Any, ...]. Source line: 175.

### SessionCallbacks.refresh_models

Read only the local Ollama catalog after checking the browser owner.

Kind: callable. Declared return: tuple[list[str], str, str]. Source line: 196.

### SessionCallbacks.validation_status

Read this owner's trusted validation state, never another session's.

Kind: callable. Declared return: str. Source line: 215.

### SessionCallbacks.unload

Cancel this framework owner's pending work when its browser unloads.

Kind: callable. Declared return: None. Source line: 219.

## Variables and parameters

| Scope | Name | Role and meaning | Type | Lifetime | Writes |
| --- | --- | --- | --- | --- | --- |
| module | secrets | Imported dependency for secrets in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 7 |
| module | threading | Imported dependency for threading in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 8 |
| module | time | Imported dependency for time in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 9 |
| module | Callable | Imported dependency for Callable in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 10 |
| module | dataclass | Imported dependency for dataclass in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 11 |
| module | Any | Imported dependency for Any in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 12 |
| module | uuid4 | Imported dependency for uuid4 in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 13 |
| module | operation_scope | Imported dependency for operation scope in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 15 |
| Session | token | Typed binding for token in Session; use the enclosing contract and type below. | str | Enclosing invocation or class/instance lifetime | 26 |
| Session | owner | Typed binding for owner in Session; use the enclosing contract and type below. | str | Enclosing invocation or class/instance lifetime | 27 |
| Session | controller | Typed binding for controller in Session; use the enclosing contract and type below. | Any | Enclosing invocation or class/instance lifetime | 28 |
| Session | last_seen | Typed binding for last seen in Session; use the enclosing contract and type below. | float | Enclosing invocation or class/instance lifetime | 29 |
| Session | session_id | Browser or terminal session identifier for state and diagnostic ownership. | str | Enclosing invocation or class/instance lifetime | 30 |
| SessionRegistry.__init__ | self | Owning instance; its attributes retain state for the instance lifetime. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 37 |
| SessionRegistry.__init__ | factory | Parameter for factory in SessionRegistry.__init__; use the enclosing contract and type below. | Callable[[str], Any] | Enclosing invocation or class/instance lifetime | 38 |
| SessionRegistry.__init__ | max_sessions | Parameter for max sessions in SessionRegistry.__init__; use the enclosing contract and type below. | int | Enclosing invocation or class/instance lifetime | 40 |
| SessionRegistry.__init__ | idle_timeout | Parameter for idle timeout in SessionRegistry.__init__; use the enclosing contract and type below. | float | Enclosing invocation or class/instance lifetime | 41 |
| SessionRegistry.__init__ | clock | Parameter for clock in SessionRegistry.__init__; use the enclosing contract and type below. | Callable[[], float] | Enclosing invocation or class/instance lifetime | 42 |
| SessionRegistry.__init__ | self.factory | Attribute for factory in SessionRegistry.__init__; use the enclosing contract and type below. | tuple | Enclosing invocation or class/instance lifetime | 47 |
| SessionRegistry.__init__ | self.max_sessions | Attribute for max sessions in SessionRegistry.__init__; use the enclosing contract and type below. | tuple | Enclosing invocation or class/instance lifetime | 47 |
| SessionRegistry.__init__ | self.idle_timeout | Attribute for idle timeout in SessionRegistry.__init__; use the enclosing contract and type below. | tuple | Enclosing invocation or class/instance lifetime | 48 |
| SessionRegistry.__init__ | self.clock | Attribute for clock in SessionRegistry.__init__; use the enclosing contract and type below. | tuple | Enclosing invocation or class/instance lifetime | 48 |
| SessionRegistry.__init__ | self._sessions | Attribute for sessions in SessionRegistry.__init__; use the enclosing contract and type below. | dict[str, Session] | Enclosing invocation or class/instance lifetime | 49 |
| SessionRegistry.__init__ | self._owners | Attribute for owners in SessionRegistry.__init__; use the enclosing contract and type below. | dict[str, str] | Enclosing invocation or class/instance lifetime | 50 |
| SessionRegistry.__init__ | self._lock | Attribute for lock in SessionRegistry.__init__; use the enclosing contract and type below. | Return type of RLock; see its callable contract | Enclosing invocation or class/instance lifetime | 51 |
| SessionRegistry._remove | self | Owning instance; its attributes retain state for the instance lifetime. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 53 |
| SessionRegistry._remove | session | Parameter for session in SessionRegistry._remove; use the enclosing contract and type below. | Session | Enclosing invocation or class/instance lifetime | 53 |
| SessionRegistry._remove | close | Local binding for close in SessionRegistry._remove; use the enclosing contract and type below. | Return type of getattr; see its callable contract | Enclosing invocation or class/instance lifetime | 55 |
| SessionRegistry.resolve | self | Owning instance; its attributes retain state for the instance lifetime. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 63 |
| SessionRegistry.resolve | token | Parameter for token in SessionRegistry.resolve; use the enclosing contract and type below. | str &#124; None | Enclosing invocation or class/instance lifetime | 63, 88 |
| SessionRegistry.resolve | owner | Parameter for owner in SessionRegistry.resolve; use the enclosing contract and type below. | str | Enclosing invocation or class/instance lifetime | 63 |
| SessionRegistry.resolve | now | Local binding for now in SessionRegistry.resolve; use the enclosing contract and type below. | Return type of clock; see its callable contract | Enclosing invocation or class/instance lifetime | 72 |
| SessionRegistry.resolve | session | Loop item for session in SessionRegistry.resolve; use the enclosing contract and type below. | Element of the declared iterable | Enclosing invocation or class/instance lifetime | 73, 80, 84, 93 |
| SessionRegistry.resolve | session_id | Browser or terminal session identifier for state and diagnostic ownership. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 90 |
| SessionRegistry.resolve | controller | Local binding for controller in SessionRegistry.resolve; use the enclosing contract and type below. | Return type of factory; see its callable contract | Enclosing invocation or class/instance lifetime | 92 |
| SessionRegistry.resolve | session.last_seen | Attribute for session.last seen in SessionRegistry.resolve; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 95 |
| SessionRegistry.close | self | Owning instance; its attributes retain state for the instance lifetime. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 98 |
| SessionRegistry.close | token | Parameter for token in SessionRegistry.close; use the enclosing contract and type below. | str &#124; None | Enclosing invocation or class/instance lifetime | 98 |
| SessionRegistry.close | owner | Parameter for owner in SessionRegistry.close; use the enclosing contract and type below. | str | Enclosing invocation or class/instance lifetime | 98 |
| SessionRegistry.close | session | Local binding for session in SessionRegistry.close; use the enclosing contract and type below. | Return type of get; see its callable contract | Enclosing invocation or class/instance lifetime | 101 |
| SessionRegistry.close_state | self | Owning instance; its attributes retain state for the instance lifetime. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 105 |
| SessionRegistry.close_state | token | Parameter for token in SessionRegistry.close_state; use the enclosing contract and type below. | str &#124; None | Enclosing invocation or class/instance lifetime | 105 |
| SessionRegistry.close_state | session | Local binding for session in SessionRegistry.close_state; use the enclosing contract and type below. | Return type of get; see its callable contract | Enclosing invocation or class/instance lifetime | 108 |
| SessionRegistry.close_owner | self | Owning instance; its attributes retain state for the instance lifetime. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 112 |
| SessionRegistry.close_owner | owner | Parameter for owner in SessionRegistry.close_owner; use the enclosing contract and type below. | str &#124; None | Enclosing invocation or class/instance lifetime | 112 |
| SessionRegistry.close_owner | token | Local binding for token in SessionRegistry.close_owner; use the enclosing contract and type below. | Return type of get; see its callable contract | Enclosing invocation or class/instance lifetime | 115 |
| SessionCallbacks.__init__ | self | Owning instance; its attributes retain state for the instance lifetime. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 123 |
| SessionCallbacks.__init__ | registry | Parameter for registry in SessionCallbacks.__init__; use the enclosing contract and type below. | SessionRegistry | Enclosing invocation or class/instance lifetime | 123 |
| SessionCallbacks.__init__ | self.registry | Attribute for registry in SessionCallbacks.__init__; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 125 |
| SessionCallbacks._session | self | Owning instance; its attributes retain state for the instance lifetime. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 127 |
| SessionCallbacks._session | token | Parameter for token in SessionCallbacks._session; use the enclosing contract and type below. | str &#124; None | Enclosing invocation or class/instance lifetime | 127 |
| SessionCallbacks._session | request | Parameter for request in SessionCallbacks._session; use the enclosing contract and type below. | Any | Enclosing invocation or class/instance lifetime | 127 |
| SessionCallbacks.submit | self | Owning instance; its attributes retain state for the instance lifetime. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 131 |
| SessionCallbacks.submit | message | Parameter for message in SessionCallbacks.submit; use the enclosing contract and type below. | str | Enclosing invocation or class/instance lifetime | 131 |
| SessionCallbacks.submit | token | Parameter for token in SessionCallbacks.submit; use the enclosing contract and type below. | str &#124; None | Enclosing invocation or class/instance lifetime | 131 |
| SessionCallbacks.submit | request | Parameter for request in SessionCallbacks.submit; use the enclosing contract and type below. | Any | Enclosing invocation or class/instance lifetime | 131 |
| SessionCallbacks.submit | session | Local binding for session in SessionCallbacks.submit; use the enclosing contract and type below. | Return type of _session; see its callable contract | Enclosing invocation or class/instance lifetime | 133 |
| SessionCallbacks.poll | self | Owning instance; its attributes retain state for the instance lifetime. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 136 |
| SessionCallbacks.poll | token | Parameter for token in SessionCallbacks.poll; use the enclosing contract and type below. | str &#124; None | Enclosing invocation or class/instance lifetime | 136 |
| SessionCallbacks.poll | request | Parameter for request in SessionCallbacks.poll; use the enclosing contract and type below. | Any | Enclosing invocation or class/instance lifetime | 136 |
| SessionCallbacks.poll | session | Local binding for session in SessionCallbacks.poll; use the enclosing contract and type below. | Return type of _session; see its callable contract | Enclosing invocation or class/instance lifetime | 138 |
| SessionCallbacks.approve | self | Owning instance; its attributes retain state for the instance lifetime. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 141 |
| SessionCallbacks.approve | text | Parameter for text in SessionCallbacks.approve; use the enclosing contract and type below. | str | Enclosing invocation or class/instance lifetime | 141 |
| SessionCallbacks.approve | request_id | Displayed approval identity checked against the owner and expiry; not a secret. | str | Enclosing invocation or class/instance lifetime | 141 |
| SessionCallbacks.approve | token | Parameter for token in SessionCallbacks.approve; use the enclosing contract and type below. | str &#124; None | Enclosing invocation or class/instance lifetime | 141 |
| SessionCallbacks.approve | request | Parameter for request in SessionCallbacks.approve; use the enclosing contract and type below. | Any | Enclosing invocation or class/instance lifetime | 141 |
| SessionCallbacks.approve | session | Local binding for session in SessionCallbacks.approve; use the enclosing contract and type below. | Return type of _session; see its callable contract | Enclosing invocation or class/instance lifetime | 143 |
| SessionCallbacks.reject | self | Owning instance; its attributes retain state for the instance lifetime. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 146 |
| SessionCallbacks.reject | request_id | Displayed approval identity checked against the owner and expiry; not a secret. | str | Enclosing invocation or class/instance lifetime | 146 |
| SessionCallbacks.reject | token | Parameter for token in SessionCallbacks.reject; use the enclosing contract and type below. | str &#124; None | Enclosing invocation or class/instance lifetime | 146 |
| SessionCallbacks.reject | request | Parameter for request in SessionCallbacks.reject; use the enclosing contract and type below. | Any | Enclosing invocation or class/instance lifetime | 146 |
| SessionCallbacks.reject | session | Local binding for session in SessionCallbacks.reject; use the enclosing contract and type below. | Return type of _session; see its callable contract | Enclosing invocation or class/instance lifetime | 148 |
| SessionCallbacks.toggle | self | Owning instance; its attributes retain state for the instance lifetime. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 151 |
| SessionCallbacks.toggle | enabled | Parameter for enabled in SessionCallbacks.toggle; use the enclosing contract and type below. | bool | Enclosing invocation or class/instance lifetime | 151 |
| SessionCallbacks.toggle | token | Parameter for token in SessionCallbacks.toggle; use the enclosing contract and type below. | str &#124; None | Enclosing invocation or class/instance lifetime | 151 |
| SessionCallbacks.toggle | request | Parameter for request in SessionCallbacks.toggle; use the enclosing contract and type below. | Any | Enclosing invocation or class/instance lifetime | 151 |
| SessionCallbacks.toggle | session | Local binding for session in SessionCallbacks.toggle; use the enclosing contract and type below. | Return type of _session; see its callable contract | Enclosing invocation or class/instance lifetime | 153 |
| SessionCallbacks.configure_model | self | Owning instance; its attributes retain state for the instance lifetime. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 158 |
| SessionCallbacks.configure_model | provider | Parameter for provider in SessionCallbacks.configure_model; use the enclosing contract and type below. | str | Enclosing invocation or class/instance lifetime | 159 |
| SessionCallbacks.configure_model | model | Parameter for model in SessionCallbacks.configure_model; use the enclosing contract and type below. | str | Enclosing invocation or class/instance lifetime | 160 |
| SessionCallbacks.configure_model | endpoint | Parameter for endpoint in SessionCallbacks.configure_model; use the enclosing contract and type below. | str | Enclosing invocation or class/instance lifetime | 161 |
| SessionCallbacks.configure_model | key | Parameter for key in SessionCallbacks.configure_model; use the enclosing contract and type below. | str | Enclosing invocation or class/instance lifetime | 162 |
| SessionCallbacks.configure_model | consent | Parameter for consent in SessionCallbacks.configure_model; use the enclosing contract and type below. | bool | Enclosing invocation or class/instance lifetime | 163 |
| SessionCallbacks.configure_model | token | Parameter for token in SessionCallbacks.configure_model; use the enclosing contract and type below. | str &#124; None | Enclosing invocation or class/instance lifetime | 164 |
| SessionCallbacks.configure_model | request | Parameter for request in SessionCallbacks.configure_model; use the enclosing contract and type below. | Any | Enclosing invocation or class/instance lifetime | 165 |
| SessionCallbacks.configure_model | session | Local binding for session in SessionCallbacks.configure_model; use the enclosing contract and type below. | Return type of _session; see its callable contract | Enclosing invocation or class/instance lifetime | 168 |
| SessionCallbacks.configure_model | status | Local binding for status in SessionCallbacks.configure_model; use the enclosing contract and type below. | Return type of configure_model; see its callable contract | Enclosing invocation or class/instance lifetime | 170, 172 |
| SessionCallbacks.model_menu | self | Owning instance; its attributes retain state for the instance lifetime. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 176 |
| SessionCallbacks.model_menu | action | Parameter for action in SessionCallbacks.model_menu; use the enclosing contract and type below. | str | Enclosing invocation or class/instance lifetime | 177 |
| SessionCallbacks.model_menu | identity | Explicit owner identity used by a session factory or fixture. | str | Enclosing invocation or class/instance lifetime | 178 |
| SessionCallbacks.model_menu | name | Current identifier selected by parsing, lookup or dependency registration. | str | Enclosing invocation or class/instance lifetime | 179 |
| SessionCallbacks.model_menu | provider | Parameter for provider in SessionCallbacks.model_menu; use the enclosing contract and type below. | str | Enclosing invocation or class/instance lifetime | 180 |
| SessionCallbacks.model_menu | model | Parameter for model in SessionCallbacks.model_menu; use the enclosing contract and type below. | str | Enclosing invocation or class/instance lifetime | 181 |
| SessionCallbacks.model_menu | endpoint | Parameter for endpoint in SessionCallbacks.model_menu; use the enclosing contract and type below. | str | Enclosing invocation or class/instance lifetime | 182 |
| SessionCallbacks.model_menu | key | Parameter for key in SessionCallbacks.model_menu; use the enclosing contract and type below. | str | Enclosing invocation or class/instance lifetime | 183 |
| SessionCallbacks.model_menu | token | Parameter for token in SessionCallbacks.model_menu; use the enclosing contract and type below. | str &#124; None | Enclosing invocation or class/instance lifetime | 184 |
| SessionCallbacks.model_menu | request | Parameter for request in SessionCallbacks.model_menu; use the enclosing contract and type below. | Any | Enclosing invocation or class/instance lifetime | 185 |
| SessionCallbacks.model_menu | session | Local binding for session in SessionCallbacks.model_menu; use the enclosing contract and type below. | Return type of _session; see its callable contract | Enclosing invocation or class/instance lifetime | 188 |
| SessionCallbacks.refresh_models | self | Owning instance; its attributes retain state for the instance lifetime. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 197 |
| SessionCallbacks.refresh_models | endpoint | Parameter for endpoint in SessionCallbacks.refresh_models; use the enclosing contract and type below. | str | Enclosing invocation or class/instance lifetime | 197 |
| SessionCallbacks.refresh_models | token | Parameter for token in SessionCallbacks.refresh_models; use the enclosing contract and type below. | str &#124; None | Enclosing invocation or class/instance lifetime | 197 |
| SessionCallbacks.refresh_models | request | Parameter for request in SessionCallbacks.refresh_models; use the enclosing contract and type below. | Any | Enclosing invocation or class/instance lifetime | 197 |
| SessionCallbacks.refresh_models | installed_models | Imported dependency for installed models in SessionCallbacks.refresh_models; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 200 |
| SessionCallbacks.refresh_models | session | Local binding for session in SessionCallbacks.refresh_models; use the enclosing contract and type below. | Return type of _session; see its callable contract | Enclosing invocation or class/instance lifetime | 202 |
| SessionCallbacks.refresh_models | configuration | Local binding for configuration in SessionCallbacks.refresh_models; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 204 |
| SessionCallbacks.refresh_models | reader | Local binding for reader in SessionCallbacks.refresh_models; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 205 |
| SessionCallbacks.refresh_models | names | Local binding for names in SessionCallbacks.refresh_models; use the enclosing contract and type below. | Return type of installed_models; see its callable contract | Enclosing invocation or class/instance lifetime | 206, 211 |
| SessionCallbacks.refresh_models | status | Local binding for status in SessionCallbacks.refresh_models; use the enclosing contract and type below. | str | Enclosing invocation or class/instance lifetime | 207, 209, 212 |
| SessionCallbacks.validation_status | self | Owning instance; its attributes retain state for the instance lifetime. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 215 |
| SessionCallbacks.validation_status | token | Parameter for token in SessionCallbacks.validation_status; use the enclosing contract and type below. | str &#124; None | Enclosing invocation or class/instance lifetime | 215 |
| SessionCallbacks.validation_status | request | Parameter for request in SessionCallbacks.validation_status; use the enclosing contract and type below. | Any | Enclosing invocation or class/instance lifetime | 215 |
| SessionCallbacks.unload | self | Owning instance; its attributes retain state for the instance lifetime. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 219 |
| SessionCallbacks.unload | request | Parameter for request in SessionCallbacks.unload; use the enclosing contract and type below. | Any | Enclosing invocation or class/instance lifetime | 219 |
