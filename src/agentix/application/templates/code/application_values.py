"""Portable strict value validation shared by host contracts and the native code runtime."""

import math


def validate_value(value: object, shape: dict) -> object:
    """Validate bounded finite JSON scalar/array values without coercion or side effects."""
    kind = shape.get("type")
    valid = {
        "string": type(value) is str,
        "integer": type(value) is int,
        "number": type(value) in {int, float},
        "boolean": type(value) is bool,
        "array": type(value) is list,
    }.get(kind, False)
    if not valid or ("enum" in shape and value not in shape["enum"]):
        raise ValueError("Value does not match the reviewed application contract")
    if type(value) is float and not math.isfinite(value):
        raise ValueError("Non-finite application value")
    if type(value) in {str, list} and len(value) > 16000:
        raise ValueError("Application value exceeds its limit")
    if kind == "array":
        for item in value:
            validate_value(item, shape["items"])
    return value
