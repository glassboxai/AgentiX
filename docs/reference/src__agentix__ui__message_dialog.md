# Reference for src/agentix/ui/message_dialog.py

Reusable modal message window: one persistent message with an Ok close button.

Presentation only: the dialog never changes backend behavior, it replaces
ephemeral native notifications with an explicit user-dismissed window.

Source fingerprint: 066f31ddec2d75f0bb10539b962698e53737398e1ec9f8e87d96421326103285

This reference is generated from maintained source without imports or execution. Assigned values are intentionally omitted. Runtime-dependent types are explicit; the enclosing docstring defines the behavioral contract. See [architecture](../ARCHITECTURE_QUALITY.md) for manually reviewed responsibility and dependency decisions.

## Classes and callables

### MessageDialog

Modal window bound to a message text and an Ok button, hidden by default.

Kind: class. Declared return: Not declared / class. Source line: 13.

### MessageDialog.__init__

Build the hidden window and wire Ok to close it; styling lives in style.css.

Kind: callable. Declared return: None. Source line: 16.

### MessageDialog.outputs

Expose the output pair other handlers append to their output lists.

Kind: callable. Declared return: list. Source line: 31.

### MessageDialog.show

Return updates that open the window displaying the given message.

Kind: callable. Declared return: tuple. Source line: 35.

### MessageDialog.hide

Close the window; the message text is retained but never visible.

Kind: callable. Declared return: Any. Source line: 39.

### MessageDialog.skip

Leave the dialog untouched inside another handler's output row.

Kind: callable. Declared return: tuple. Source line: 43.

### MessageDialog.wrap_stream

Append dialog outputs to a streaming handler; show ValueError in the modal.

Kind: callable. Declared return: Callable. Source line: 47.

### MessageDialog.wrap_stream.stream

Pass ordinary rows through; validation errors become a persistent modal.

Kind: callable. Declared return: Iterator[tuple]. Source line: 51.

### MessageDialog.wrap_stream_final

Stream rows untouched; open the modal with the final row's status text.

Kind: callable. Declared return: Callable. Source line: 61.

### MessageDialog.wrap_stream_final.stream

Hold one row back so only the stream's last status opens the modal.

Kind: callable. Declared return: Iterator[tuple]. Source line: 65.

### MessageDialog.wrap_result

Append dialog outputs to one plain result; its status message opens the modal.

Kind: callable. Declared return: Callable. Source line: 88.

### MessageDialog.wrap_result.call

Mirror the status text into the modal; validation errors open it too.

Kind: callable. Declared return: tuple. Source line: 92.

### MessageDialog.guard_result

Append dialog outputs to one plain result; only validation errors open the modal.

Kind: callable. Declared return: Callable. Source line: 102.

### MessageDialog.guard_result.call

Pass ordinary rows through untouched; ValueError becomes a persistent modal.

Kind: callable. Declared return: tuple. Source line: 106.

### MessageDialog.guard_history

Keep a rejected row renderable by emptying the Chatbot history output.

Gradio postprocesses every output before the error reaches the browser, so a
stale or foreign session token would otherwise surface as a Chatbot format
error instead of the ownership diagnostic. ``size`` counts the handler's own
outputs; the dialog pair is appended here.

Kind: callable. Declared return: Callable. Source line: 127.

### MessageDialog.guard_history.call

Append the dialog pair; on ValueError empty the history and open the modal.

Kind: callable. Declared return: tuple. Source line: 137.

## Variables and parameters

| Scope | Name | Role and meaning | Type | Lifetime | Writes |
| --- | --- | --- | --- | --- | --- |
| module | functools | Imported dependency for functools in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 7 |
| module | inspect | Imported dependency for inspect in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 8 |
| module | Callable | Imported dependency for Callable in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 9 |
| module | Iterator | Imported dependency for Iterator in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 9 |
| module | Any | Imported dependency for Any in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 10 |
| MessageDialog.__init__ | self | Owning instance; its attributes retain state for the instance lifetime. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 16 |
| MessageDialog.__init__ | gr | Parameter for gr in MessageDialog.__init__; use the enclosing contract and type below. | Any | Enclosing invocation or class/instance lifetime | 16 |
| MessageDialog.__init__ | self._gr | Attribute for gr in MessageDialog.__init__; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 18 |
| MessageDialog.__init__ | container | Managed resource for container in MessageDialog.__init__; use the enclosing contract and type below. | Return type of Column; see its callable contract | Context-manager block; exit invokes its cleanup protocol | 19 |
| MessageDialog.__init__ | self.container | Attribute for container in MessageDialog.__init__; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 20 |
| MessageDialog.__init__ | self.message | Attribute for message in MessageDialog.__init__; use the enclosing contract and type below. | Return type of Markdown; see its callable contract | Enclosing invocation or class/instance lifetime | 21 |
| MessageDialog.__init__ | self.ok | Attribute for ok in MessageDialog.__init__; use the enclosing contract and type below. | Return type of Button; see its callable contract | Enclosing invocation or class/instance lifetime | 22 |
| MessageDialog.outputs | self | Owning instance; its attributes retain state for the instance lifetime. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 31 |
| MessageDialog.show | self | Owning instance; its attributes retain state for the instance lifetime. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 35 |
| MessageDialog.show | text | Parameter for text in MessageDialog.show; use the enclosing contract and type below. | str | Enclosing invocation or class/instance lifetime | 35 |
| MessageDialog.hide | self | Owning instance; its attributes retain state for the instance lifetime. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 39 |
| MessageDialog.skip | self | Owning instance; its attributes retain state for the instance lifetime. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 43 |
| MessageDialog.wrap_stream | self | Owning instance; its attributes retain state for the instance lifetime. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 47 |
| MessageDialog.wrap_stream | handler | Parameter for handler in MessageDialog.wrap_stream; use the enclosing contract and type below. | Callable | Enclosing invocation or class/instance lifetime | 47 |
| MessageDialog.wrap_stream | size | Parameter for size in MessageDialog.wrap_stream; use the enclosing contract and type below. | int | Enclosing invocation or class/instance lifetime | 47 |
| MessageDialog.wrap_stream.stream | args | Parameter for args in MessageDialog.wrap_stream.stream; use the enclosing contract and type below. | Any | Enclosing invocation or class/instance lifetime | 51 |
| MessageDialog.wrap_stream.stream | row | Loop item for row in MessageDialog.wrap_stream.stream; use the enclosing contract and type below. | Element of the declared iterable | Enclosing invocation or class/instance lifetime | 54 |
| MessageDialog.wrap_stream.stream | error | Caught exception for error in MessageDialog.wrap_stream.stream; use the enclosing contract and type below. | ValueError | Current exception handler; Python clears this binding afterward | 56 |
| MessageDialog.wrap_stream_final | self | Owning instance; its attributes retain state for the instance lifetime. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 61 |
| MessageDialog.wrap_stream_final | handler | Parameter for handler in MessageDialog.wrap_stream_final; use the enclosing contract and type below. | Callable | Enclosing invocation or class/instance lifetime | 61 |
| MessageDialog.wrap_stream_final | size | Parameter for size in MessageDialog.wrap_stream_final; use the enclosing contract and type below. | int | Enclosing invocation or class/instance lifetime | 61 |
| MessageDialog.wrap_stream_final | status_index | Parameter for status index in MessageDialog.wrap_stream_final; use the enclosing contract and type below. | int | Enclosing invocation or class/instance lifetime | 61 |
| MessageDialog.wrap_stream_final.stream | args | Parameter for args in MessageDialog.wrap_stream_final.stream; use the enclosing contract and type below. | Any | Enclosing invocation or class/instance lifetime | 65 |
| MessageDialog.wrap_stream_final.stream | held | Local binding for held in MessageDialog.wrap_stream_final.stream; use the enclosing contract and type below. | NoneType | Enclosing invocation or class/instance lifetime | 67, 72 |
| MessageDialog.wrap_stream_final.stream | row | Loop item for row in MessageDialog.wrap_stream_final.stream; use the enclosing contract and type below. | Element of the declared iterable | Enclosing invocation or class/instance lifetime | 69 |
| MessageDialog.wrap_stream_final.stream | error | Caught exception for error in MessageDialog.wrap_stream_final.stream; use the enclosing contract and type below. | ValueError | Current exception handler; Python clears this binding afterward | 73 |
| MessageDialog.wrap_stream_final.stream | text | Local binding for text in MessageDialog.wrap_stream_final.stream; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 80 |
| MessageDialog.wrap_result | self | Owning instance; its attributes retain state for the instance lifetime. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 88 |
| MessageDialog.wrap_result | handler | Parameter for handler in MessageDialog.wrap_result; use the enclosing contract and type below. | Callable | Enclosing invocation or class/instance lifetime | 88 |
| MessageDialog.wrap_result | size | Parameter for size in MessageDialog.wrap_result; use the enclosing contract and type below. | int | Enclosing invocation or class/instance lifetime | 88 |
| MessageDialog.wrap_result | status_index | Parameter for status index in MessageDialog.wrap_result; use the enclosing contract and type below. | int | Enclosing invocation or class/instance lifetime | 88 |
| MessageDialog.wrap_result.call | args | Parameter for args in MessageDialog.wrap_result.call; use the enclosing contract and type below. | Any | Enclosing invocation or class/instance lifetime | 92 |
| MessageDialog.wrap_result.call | row | Local binding for row in MessageDialog.wrap_result.call; use the enclosing contract and type below. | Return type of handler; see its callable contract | Enclosing invocation or class/instance lifetime | 95 |
| MessageDialog.wrap_result.call | error | Caught exception for error in MessageDialog.wrap_result.call; use the enclosing contract and type below. | ValueError | Current exception handler; Python clears this binding afterward | 96 |
| MessageDialog.guard_result | self | Owning instance; its attributes retain state for the instance lifetime. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 102 |
| MessageDialog.guard_result | handler | Parameter for handler in MessageDialog.guard_result; use the enclosing contract and type below. | Callable | Enclosing invocation or class/instance lifetime | 102 |
| MessageDialog.guard_result | size | Parameter for size in MessageDialog.guard_result; use the enclosing contract and type below. | int | Enclosing invocation or class/instance lifetime | 102 |
| MessageDialog.guard_result.call | args | Parameter for args in MessageDialog.guard_result.call; use the enclosing contract and type below. | Any | Enclosing invocation or class/instance lifetime | 106 |
| MessageDialog.guard_result.call | row | Local binding for row in MessageDialog.guard_result.call; use the enclosing contract and type below. | Return type of handler; see its callable contract | Enclosing invocation or class/instance lifetime | 109 |
| MessageDialog.guard_result.call | error | Caught exception for error in MessageDialog.guard_result.call; use the enclosing contract and type below. | ValueError | Current exception handler; Python clears this binding afterward | 110 |
| MessageDialog.guard_result.call | head | Local binding for head in MessageDialog.guard_result.call; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 111 |
| MessageDialog.guard_result.call | values | Local binding for values in MessageDialog.guard_result.call; use the enclosing contract and type below. | tuple | Enclosing invocation or class/instance lifetime | 118, 120, 122 |
| MessageDialog.guard_history | self | Owning instance; its attributes retain state for the instance lifetime. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 127 |
| MessageDialog.guard_history | handler | Parameter for handler in MessageDialog.guard_history; use the enclosing contract and type below. | Callable | Enclosing invocation or class/instance lifetime | 127 |
| MessageDialog.guard_history | size | Parameter for size in MessageDialog.guard_history; use the enclosing contract and type below. | int | Enclosing invocation or class/instance lifetime | 127 |
| MessageDialog.guard_history | history_index | Parameter for history index in MessageDialog.guard_history; use the enclosing contract and type below. | int | Enclosing invocation or class/instance lifetime | 127 |
| MessageDialog.guard_history.call | args | Parameter for args in MessageDialog.guard_history.call; use the enclosing contract and type below. | Any | Enclosing invocation or class/instance lifetime | 137 |
| MessageDialog.guard_history.call | row | Local binding for row in MessageDialog.guard_history.call; use the enclosing contract and type below. | Return type of handler; see its callable contract | Enclosing invocation or class/instance lifetime | 140 |
| MessageDialog.guard_history.call | error | Caught exception for error in MessageDialog.guard_history.call; use the enclosing contract and type below. | ValueError | Current exception handler; Python clears this binding afterward | 141 |
| MessageDialog.guard_history.call | values | Local binding for values in MessageDialog.guard_history.call; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 142 |
