"""Readable instance-scoped control identity regressions."""

from concurrent.futures import ThreadPoolExecutor

import pytest


def allocator():
    """Import the maintained allocator without importing any generated module."""
    from agentix.application.templates.code.element_ids import ElementIds

    return ElementIds()


def test_duplicate_widget_instances_have_stable_unique_semantic_ids():
    """Two copies of one tool must have distinct DOM IDs and event API names."""
    ids = allocator()
    first, second = ids.new_widget("words"), ids.new_widget("words")
    assert ids.control(first, "input") == "application_words_input"
    assert ids.control(first, "input") == ids.control(first, "input")
    assert ids.control(second, "input") == "application_words_2_input"
    assert ids.api_name(first) != ids.api_name(second)
    assert ids.control(first, "group") is None
    assert (
        len(
            {
                ids.control(scope, role)
                for scope in (first, second)
                for role in ("input", "output", "execute")
            }
        )
        == 6
    )


def test_parallel_allocations_do_not_collide():
    """Scope allocation must be atomic even if widget setup becomes concurrent."""
    ids = allocator()
    with ThreadPoolExecutor(max_workers=8) as pool:
        scopes = list(pool.map(lambda _: ids.new_widget("vowels"), range(80)))
    assert len(set(scopes)) == 80


def test_invalid_or_foreign_scopes_and_control_roles_are_rejected():
    """Never silently normalize distinct names into the same selector."""
    ids = allocator()
    with pytest.raises(ValueError):
        ids.new_widget("../words")
    scope = ids.new_widget("words")
    with pytest.raises(ValueError):
        ids.control(scope, "invented")
    with pytest.raises(ValueError):
        ids.control("foreign", "input")
