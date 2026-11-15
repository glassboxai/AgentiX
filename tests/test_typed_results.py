"""Typed result presentation does not expose raw JSON as the default output."""

from types import SimpleNamespace

import pytest


def test_text_number_boolean_and_table_use_corresponding_readonly_components():
    """Output contracts drive components; no model HTML or JSON renderer is needed."""
    from agentix.ui.result_components import ResultField, build_results

    calls = []

    def component(kind):
        """Record construction only, without requiring a browser."""
        return lambda **kwargs: calls.append((kind, kwargs)) or kwargs

    gr = SimpleNamespace(
        Textbox=component("text"),
        Number=component("number"),
        Checkbox=component("boolean"),
        Dataframe=component("table"),
    )
    fields = [
        ResultField("message", "Message", "text"),
        ResultField("count", "Count", "number"),
        ResultField("ok", "OK", "boolean"),
        ResultField("rows", "Rows", "table"),
    ]
    build_results(gr, fields, "result")
    assert [kind for kind, _ in calls] == ["text", "number", "boolean", "table"]
    assert all(not values["interactive"] for _, values in calls)


def test_result_values_validate_types_and_clear_on_failure():
    """False must not be rendered as a numerical zero; invalid output remains unpublished."""
    from agentix.ui.result_components import ResultField, result_values

    fields = [ResultField("words", "Words", "number"), ResultField("vowels", "Vowels", "number")]
    assert result_values({"words": 2, "vowels": 3}, fields) == [2, 3]
    assert result_values(None, fields) == [None, None]
    with pytest.raises(ValueError):
        result_values({"words": False, "vowels": 3}, fields)


@pytest.mark.parametrize("cell", [float("nan"), float("inf"), "x" * 16385, {"nested": "object"}])
def test_tables_reject_unbounded_or_nonfinite_cells(cell):
    """Dataframe presentation accepts bounded scalar JSON data only."""
    from agentix.ui.result_components import ResultField, result_values

    with pytest.raises(ValueError):
        result_values({"rows": [{"value": cell}]}, [ResultField("rows", "Rows", "table")])
