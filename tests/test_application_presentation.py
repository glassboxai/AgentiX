"""Bounded presentation regressions for the composite data-operation surface."""

from agentix.ui.application_presentation import (
    MAX_RESULT_CELL_LENGTH,
    MAX_RESULT_ROWS,
    describe_data_inputs,
    named_result_rows,
)


def test_input_contract_names_keys_types_and_one_example_payload():
    """V7-073: the owner reads the closed JSON contract before typing a payload."""
    manifest = {
        "inputs": {
            "text": {"type": "string", "description": "Text to analyze"},
            "repeat": {"type": "integer", "description": "How many times"},
            "ratio": {"type": "number"},
            "flag": {"type": "boolean"},
            "tags": {"type": "array", "items": {"type": "string"}},
        }
    }

    text = describe_data_inputs(manifest)

    assert "| `text` | string | Text to analyze |" in text
    assert "| `repeat` | integer | How many times |" in text
    assert "| `ratio` | number |  |" in text
    assert "| `flag` | boolean |  |" in text
    assert "| `tags` | array |  |" in text
    assert (
        'Example payload: `{"text": "Hello World!", "repeat": 1, "ratio": 1.5, '
        '"flag": true, "tags": ["Hello World!"]}`' in text
    )


def test_input_contract_keeps_model_description_inert_and_bounded():
    """A model-authored description cannot inject markup or grow without a limit."""
    manifest = {
        "inputs": {
            "text": {
                "type": "string",
                "description": "<script>alert(1)</script> [link](http://evil) " + "x" * 400,
            }
        }
    }

    text = describe_data_inputs(manifest)

    assert "<script>" not in text and "](http" not in text
    assert "scriptalert(1)/script link(http://evil)" in text
    assert len(text.splitlines()[4]) <= 200


def test_input_contract_reports_an_application_without_declared_inputs():
    """An empty closed input map is stated instead of rendering an empty table."""
    assert describe_data_inputs({"inputs": {}}) == (
        "This application declares no data-operation inputs."
    )


def test_named_results_bound_rows_and_cells_without_losing_types():
    """Observed results become bounded text cells; oversized bodies are truncated."""
    value = {
        "calculator": 5,
        "random_draw": [2, 4],
        "label": "x" * (MAX_RESULT_CELL_LENGTH * 2),
        "flag": True,
    }
    value.update({f"extra_{index}": index for index in range(MAX_RESULT_ROWS)})

    rows = named_result_rows(value)

    assert rows["headers"] == ["Result", "Type", "Value"]
    assert len(rows["data"]) == MAX_RESULT_ROWS
    assert rows["data"][0] == ["calculator", "integer", "5"]
    assert rows["data"][1] == ["random_draw", "array", "[2, 4]"]
    assert rows["data"][2][1] == "string"
    assert len(rows["data"][2][2]) == MAX_RESULT_CELL_LENGTH
    assert rows["data"][3] == ["flag", "boolean", "true"]
