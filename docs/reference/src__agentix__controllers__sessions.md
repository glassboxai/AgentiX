# Reference for src/agentix/controllers/sessions.py

Bounded server-owned workflow sessions with owner-bound opaque tokens.

Gradio session hashes provide routing, not account authentication. Tokens remain
in server-side State, and every callback must verify both token and request owner.

Source fingerprint: ba1da975d07ed10486e378b85ed6a33fd1ef8e9e0f47752e4a4b03f4c35ddfb9

This reference is generated from maintained source without imports or execution. Assigned values are intentionally omitted. Runtime-dependent types are explicit; the enclosing docstring defines the behavioral contract. See [architecture](../ARCHITECTURE_QUALITY.md) for manually reviewed responsibility and dependency decisions.

## Classes and callables

### SessionAccessError

A stale, unknown or cross-owner session cannot be accessed.

Kind: class. Declared return: Not declared / class. Source line: 25.

### Session

Registry-owned session identity, controller and last activity timestamp.

Kind: class. Declared return: Not declared / class. Source line: 30.

### SessionRegistry

Create isolated controllers and reject foreign/stale browser tokens.

Kind: class. Declared return: Not declared / class. Source line: 40.

### SessionRegistry.__init__

Configure bounded sessions; construction creates no runtime or model.

Kind: callable. Declared return: None. Source line: 43.

### SessionRegistry._remove

Cancel pending writes before dropping a closed/expired owner's state.

Kind: callable. Declared return: None. Source line: 60.

### SessionRegistry.resolve

Return/create this owner's session, rejecting untrusted token changes.

Initial callbacks can race with no token; the owner index makes creation
idempotent. Active workers are not silently evicted by idle expiry.

Kind: callable. Declared return: Session. Source line: 73.

### SessionRegistry.close

Close only a matching owner; stale/unrelated unloads cannot cancel work.

Kind: callable. Declared return: None. Source line: 126.

### SessionRegistry.close_state

Trusted Gradio State cleanup hook; never register as a public callback.

Kind: callable. Declared return: None. Source line: 133.

### SessionRegistry.close_owner

Handle a trusted framework unload request without requiring UI inputs.

Kind: callable. Declared return: None. Source line: 140.

## Variables and parameters

| Scope | Name | Role and meaning | Type | Lifetime | Writes |
| --- | --- | --- | --- | --- | --- |
| module | logging | Imported dependency for logging in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 7 |
| module | secrets | Imported dependency for secrets in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 8 |
| module | threading | Imported dependency for threading in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 9 |
| module | time | Imported dependency for time in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 10 |
| module | Callable | Imported dependency for Callable in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 11 |
| module | dataclass | Imported dependency for dataclass in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 12 |
| module | Any | Imported dependency for Any in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 13 |
| module | uuid4 | Imported dependency for uuid4 in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 14 |
| module | log_event | Imported dependency for log event in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 16 |
| module | operation_scope | Imported dependency for operation scope in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 16 |
| module | logger | Module logger emitting bounded operation diagnostics rather than artifact bodies. | Return type of getLogger; see its callable contract | Module/process lifetime | 18 |
| module | DEFAULT_MAX_SESSIONS | Module binding for DEFAULT MAX SESSIONS in module; use the enclosing contract and type below. | int | Module/process lifetime | 20 |
| module | DEFAULT_IDLE_TIMEOUT_SECONDS | Module binding for DEFAULT IDLE TIMEOUT SECONDS in module; use the enclosing contract and type below. | int | Module/process lifetime | 21 |
| module | MAX_OWNER_IDENTIFIER_LENGTH | Module binding for MAX OWNER IDENTIFIER LENGTH in module; use the enclosing contract and type below. | int | Module/process lifetime | 22 |
| Session | token | Typed binding for token in Session; use the enclosing contract and type below. | str | Enclosing invocation or class/instance lifetime | 33 |
| Session | owner | Typed binding for owner in Session; use the enclosing contract and type below. | str | Enclosing invocation or class/instance lifetime | 34 |
| Session | controller | Typed binding for controller in Session; use the enclosing contract and type below. | Any | Enclosing invocation or class/instance lifetime | 35 |
| Session | last_seen | Typed binding for last seen in Session; use the enclosing contract and type below. | float | Enclosing invocation or class/instance lifetime | 36 |
| Session | session_id | Browser or terminal session identifier for state and diagnostic ownership. | str | Enclosing invocation or class/instance lifetime | 37 |
| SessionRegistry.__init__ | self | Owning instance; its attributes retain state for the instance lifetime. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 44 |
| SessionRegistry.__init__ | factory | Parameter for factory in SessionRegistry.__init__; use the enclosing contract and type below. | Callable[[str], Any] | Enclosing invocation or class/instance lifetime | 45 |
| SessionRegistry.__init__ | max_sessions | Parameter for max sessions in SessionRegistry.__init__; use the enclosing contract and type below. | int | Enclosing invocation or class/instance lifetime | 47 |
| SessionRegistry.__init__ | idle_timeout | Parameter for idle timeout in SessionRegistry.__init__; use the enclosing contract and type below. | float | Enclosing invocation or class/instance lifetime | 48 |
| SessionRegistry.__init__ | clock | Parameter for clock in SessionRegistry.__init__; use the enclosing contract and type below. | Callable[[], float] | Enclosing invocation or class/instance lifetime | 49 |
| SessionRegistry.__init__ | self.factory | Attribute for factory in SessionRegistry.__init__; use the enclosing contract and type below. | tuple | Enclosing invocation or class/instance lifetime | 54 |
| SessionRegistry.__init__ | self.max_sessions | Attribute for max sessions in SessionRegistry.__init__; use the enclosing contract and type below. | tuple | Enclosing invocation or class/instance lifetime | 54 |
| SessionRegistry.__init__ | self.idle_timeout | Attribute for idle timeout in SessionRegistry.__init__; use the enclosing contract and type below. | tuple | Enclosing invocation or class/instance lifetime | 55 |
| SessionRegistry.__init__ | self.clock | Attribute for clock in SessionRegistry.__init__; use the enclosing contract and type below. | tuple | Enclosing invocation or class/instance lifetime | 55 |
| SessionRegistry.__init__ | self._sessions | Attribute for sessions in SessionRegistry.__init__; use the enclosing contract and type below. | dict[str, Session] | Enclosing invocation or class/instance lifetime | 56 |
| SessionRegistry.__init__ | self._owners | Attribute for owners in SessionRegistry.__init__; use the enclosing contract and type below. | dict[str, str] | Enclosing invocation or class/instance lifetime | 57 |
| SessionRegistry.__init__ | self._lock | Attribute for lock in SessionRegistry.__init__; use the enclosing contract and type below. | Return type of RLock; see its callable contract | Enclosing invocation or class/instance lifetime | 58 |
| SessionRegistry._remove | self | Owning instance; its attributes retain state for the instance lifetime. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 60 |
| SessionRegistry._remove | session | Parameter for session in SessionRegistry._remove; use the enclosing contract and type below. | Session | Enclosing invocation or class/instance lifetime | 60 |
| SessionRegistry._remove | close | Local binding for close in SessionRegistry._remove; use the enclosing contract and type below. | Return type of getattr; see its callable contract | Enclosing invocation or class/instance lifetime | 64 |
| SessionRegistry.resolve | self | Owning instance; its attributes retain state for the instance lifetime. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 73 |
| SessionRegistry.resolve | token | Parameter for token in SessionRegistry.resolve; use the enclosing contract and type below. | str &#124; None | Enclosing invocation or class/instance lifetime | 73, 108 |
| SessionRegistry.resolve | owner | Parameter for owner in SessionRegistry.resolve; use the enclosing contract and type below. | str | Enclosing invocation or class/instance lifetime | 73 |
| SessionRegistry.resolve | now | Local binding for now in SessionRegistry.resolve; use the enclosing contract and type below. | Return type of clock; see its callable contract | Enclosing invocation or class/instance lifetime | 88 |
| SessionRegistry.resolve | session | Loop item for session in SessionRegistry.resolve; use the enclosing contract and type below. | Element of the declared iterable | Enclosing invocation or class/instance lifetime | 89, 98, 103, 121 |
| SessionRegistry.resolve | session_id | Browser or terminal session identifier for state and diagnostic ownership. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 110 |
| SessionRegistry.resolve | controller | Local binding for controller in SessionRegistry.resolve; use the enclosing contract and type below. | Return type of factory; see its callable contract | Enclosing invocation or class/instance lifetime | 114 |
| SessionRegistry.resolve | error | Caught exception for error in SessionRegistry.resolve; use the enclosing contract and type below. | Exception | Current exception handler; Python clears this binding afterward | 115 |
| SessionRegistry.resolve | session.last_seen | Attribute for session.last seen in SessionRegistry.resolve; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 123 |
| SessionRegistry.close | self | Owning instance; its attributes retain state for the instance lifetime. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 126 |
| SessionRegistry.close | token | Parameter for token in SessionRegistry.close; use the enclosing contract and type below. | str &#124; None | Enclosing invocation or class/instance lifetime | 126 |
| SessionRegistry.close | owner | Parameter for owner in SessionRegistry.close; use the enclosing contract and type below. | str | Enclosing invocation or class/instance lifetime | 126 |
| SessionRegistry.close | session | Local binding for session in SessionRegistry.close; use the enclosing contract and type below. | Return type of get; see its callable contract | Enclosing invocation or class/instance lifetime | 129 |
| SessionRegistry.close_state | self | Owning instance; its attributes retain state for the instance lifetime. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 133 |
| SessionRegistry.close_state | token | Parameter for token in SessionRegistry.close_state; use the enclosing contract and type below. | str &#124; None | Enclosing invocation or class/instance lifetime | 133 |
| SessionRegistry.close_state | session | Local binding for session in SessionRegistry.close_state; use the enclosing contract and type below. | Return type of get; see its callable contract | Enclosing invocation or class/instance lifetime | 136 |
| SessionRegistry.close_owner | self | Owning instance; its attributes retain state for the instance lifetime. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 140 |
| SessionRegistry.close_owner | owner | Parameter for owner in SessionRegistry.close_owner; use the enclosing contract and type below. | str &#124; None | Enclosing invocation or class/instance lifetime | 140 |
| SessionRegistry.close_owner | token | Local binding for token in SessionRegistry.close_owner; use the enclosing contract and type below. | Return type of get; see its callable contract | Enclosing invocation or class/instance lifetime | 143 |
| module | SessionCallbacks | Imported dependency for SessionCallbacks in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 149 |
