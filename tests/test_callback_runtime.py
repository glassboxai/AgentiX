"""Callback leases preserve actual callable semantics without native dependencies."""

import asyncio
import inspect

import pytest

from agentix.lab.callback_runtime import supervise_callback


def test_sync_error_releases_the_operation_lease():
    """Catch lingering leases after normal exception propagation."""
    messages = []

    def broken():
        """Raise a controlled callback error to exercise lease release."""
        raise ValueError("fixture")

    with pytest.raises(ValueError):
        supervise_callback(broken, messages.append)()
    assert [message["type"] for message in messages] == ["callback_start", "callback_end"]
    assert messages[0]["id"] == messages[1]["id"]


def test_generator_close_releases_the_operation_lease():
    """Catch either eager iteration or leaked cancelled-generator leases."""
    messages = []

    def source():
        """Produce literal fixture values while preserving callable lifecycle semantics."""
        yield 3
        yield 10

    wrapped = supervise_callback(source, messages.append)
    assert inspect.isgeneratorfunction(wrapped)
    iterator = wrapped()
    assert next(iterator) == 3
    assert len(messages) == 1
    iterator.close()
    assert messages[-1]["type"] == "callback_end"


def test_async_result_preserves_coroutine_contract():
    """Catch converting async callbacks into unsupported synchronous wrappers."""
    messages = []

    async def source():
        """Produce literal fixture values while preserving callable lifecycle semantics."""
        return 0

    wrapped = supervise_callback(source, messages.append)
    assert inspect.iscoroutinefunction(wrapped)
    assert asyncio.run(wrapped()) == 0
    assert messages[-1]["type"] == "callback_end"
