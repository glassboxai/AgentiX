"""Strict generated-tool contracts and presentation regression tests."""

import pytest

from agentix.controllers.tool_controller import format_thoughts_markdown
from agentix.domain.tool_schema import extract_tool_schema

CODE = "\n".join(
    [
        '"""Trusted canonical arithmetic fixture."""',
        "from typing import Annotated",
        'def calculator(a: Annotated[float, "First operand"], b: Annotated[float, "Second operand"]) -> Annotated[float, "Sum of both operands"]:',
        '    """Add two operands."""',
        "    return a + b",
    ]
)


def test_schema_uses_canonical_function_and_annotated_metadata():
    """Extract JSON-safe strict types and descriptions without source execution."""
    schema = extract_tool_schema("calculator", CODE)
    assert schema["function"] == "calculator"
    assert schema["parameters"]["a"] == {"type": "number", "description": "First operand"}
    assert schema["returns"]["type"] == "number"


@pytest.mark.parametrize(
    "source",
    [
        CODE.replace("def calculator", "def add"),
        CODE.replace('Annotated[float, "First operand"]', "float"),
        CODE.replace('"First operand"', '""'),
    ],
)
def test_invalid_public_contract_rejected(source):
    """Naming and meaningful Annotated descriptions are mandatory."""
    with pytest.raises(ValueError):
        extract_tool_schema("calculator", source)


def test_activity_removes_decorative_pipes_only():
    """Keep internal operators and raw diagnostic text intact."""
    raw = "| Active agent |\n| Result: a | b |\n    | Finished |"
    rendered = format_thoughts_markdown(raw)
    assert "Active agent |" not in rendered
    assert "Result: a | b\n" in rendered
    assert raw.startswith("| Active")


def test_pure_private_helpers_and_seeded_random_are_portable():
    """Private local helpers and stdlib randomness do not require host capabilities."""
    from agentix.security.reuse_policy import computation_only

    source = "import random\ndef _checked(value):\n    return int(value)\ndef seeded(seed):\n    return random.Random(_checked(seed)).randint(1, 10)\n"
    assert computation_only(source)


def test_activity_preserves_code_indentation_and_escapes_nested_markup():
    """Removing frames must not destroy Python structure or activate generated HTML."""
    text = 'def f():\n    return "<script>"\n```python'
    rendered = format_thoughts_markdown(text)
    assert "    return" in rendered
    assert "&lt;script&gt;" in rendered


def test_agent_catalog_includes_annotated_parameter_meaning(tmp_path):
    """The manager must actually receive metadata, not only bare argument names."""
    from agentix.storage.catalog import ToolCatalog

    folder = tmp_path / "calculator"
    folder.mkdir()
    (folder / "calculator_code.py").write_text(CODE, encoding="utf-8")
    result = ToolCatalog(tmp_path).render()
    assert "First operand" in result and "Second operand" in result
    assert "Canonical typed contract" in result


def test_activity_strips_trailing_border_on_interleaved_console_fragment():
    """Rich and diagnostic fragments may split a frame, leaving only its right edge."""
    rendered = format_thoughts_markdown("stdout fragment |\n    return a | b")
    assert "stdout fragment |" not in rendered
    assert "    return a | b" in rendered


def test_discard_comprehension_target_is_pure_but_private_loads_stay_blocked():
    """The random tool's conventional underscore loop variable is not introspection."""
    from agentix.security.reuse_policy import computation_only

    assert computation_only(
        "import random\ndef draws(seed):\n    rng=random.Random(seed)\n    return [rng.randint(1,10) for _ in range(3)]\n"
    )
    assert not computation_only("def reads_private():\n    _=3\n    return _\n")
    assert not computation_only("import random\ndef unsafe():\n    return random.__dict__\n")


def test_literal_metadata_keeps_boolean_distinct_from_integer():
    """Strict JSON contracts must not describe a Literal boolean as an integer."""
    source = CODE.replace("import Annotated", "import Annotated, Literal").replace(
        'Annotated[float, "First operand"]', 'Annotated[Literal[True, False], "First operand"]'
    )
    assert extract_tool_schema("calculator", source)["parameters"]["a"]["type"] == "boolean"
    mixed = source.replace("Literal[True, False]", "Literal[True, 1]")
    with pytest.raises(ValueError):
        extract_tool_schema("calculator", mixed)


def test_new_tool_module_documentation_is_mandatory():
    """Generated production APIs cannot silently omit their module documentation."""
    source = CODE.replace('"""Trusted canonical arithmetic fixture."""\n', "")
    with pytest.raises(ValueError, match="module.*first statement"):
        extract_tool_schema("calculator", source)
