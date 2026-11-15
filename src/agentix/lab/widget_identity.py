"""Canonical external tool identity and co-located widget artifact filenames.

The pilot exposes count_vowels_in_text while retaining count_vowels as the reviewed
implementation callable. The single definition is shared by host and native worker.
"""

TOOL_NAME = "count_vowels_in_text"
FUNCTION_NAME = "count_vowels"
WIDGET_FILENAME = f"{TOOL_NAME}_widget.py"
TOOL_FILENAME = f"{TOOL_NAME}_code.py"
TESTS_FILENAME = f"{TOOL_NAME}_widget_tests.py"
CONTRACT = {
    "schema": 1,
    "tool": TOOL_NAME,
    "function": FUNCTION_NAME,
    "input": "strict text, maximum 16000 characters",
    "output": "nonnegative integer",
    "entry": "create_widget(context)",
    "roles": ["input", "output", "execute"],
}
