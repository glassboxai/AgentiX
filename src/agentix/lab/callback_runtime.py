"""Maintained callback lease instrumentation executed only in the native worker.

Leases let the host stop blocked reviewed callbacks. Child-originated messages
are not a proof that arbitrary malicious code reports its execution honestly.
"""

import functools
import inspect
from collections.abc import Callable
from uuid import uuid4


def supervise_callback(function: Callable, emit: Callable) -> Callable:
    """Preserve sync/async/generator behavior while reporting a finite execution lease."""

    def begin() -> str:
        """Allocate an operation identity without including input or output data."""
        identity = uuid4().hex
        emit({"type": "callback_start", "id": identity})
        return identity

    if inspect.isasyncgenfunction(function):

        @functools.wraps(function)
        async def async_generator(*args, **kwargs):
            """Keep the lease through the complete async generator lifecycle."""
            identity = begin()
            try:
                async for value in function(*args, **kwargs):
                    yield value
            finally:
                emit({"type": "callback_end", "id": identity})

        return async_generator
    if inspect.iscoroutinefunction(function):

        @functools.wraps(function)
        async def coroutine(*args, **kwargs):
            """Await the callback under the host-observed lease."""
            identity = begin()
            try:
                return await function(*args, **kwargs)
            finally:
                emit({"type": "callback_end", "id": identity})

        return coroutine
    if inspect.isgeneratorfunction(function):

        @functools.wraps(function)
        def generator(*args, **kwargs):
            """Release the lease even when iteration is cancelled or fails."""
            identity = begin()
            try:
                yield from function(*args, **kwargs)
            finally:
                emit({"type": "callback_end", "id": identity})

        return generator

    @functools.wraps(function)
    def callback(*args, **kwargs):
        """Report bounded normal/error callback completion without artifact content."""
        identity = begin()
        try:
            return function(*args, **kwargs)
        finally:
            emit({"type": "callback_end", "id": identity})

    return callback
