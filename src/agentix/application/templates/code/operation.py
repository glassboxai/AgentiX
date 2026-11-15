"""Maintained native call recorder for reviewed generated connection code; no graph."""

import importlib
import json
from copy import deepcopy
from pathlib import Path

from application_logic import run
from application_values import validate_value

MANIFEST = json.loads(Path(__file__).with_name("application.json").read_text(encoding="utf-8"))


def execute(payload: dict) -> tuple[dict, dict]:
    """Execute generated Python once; bound approved calls and capture widget arguments.

    This module is imported exclusively in the native worker. No agents, graph
    interpretation or host RPC are used. Errors publish no partial outputs.
    """
    if type(payload) is not dict or set(payload) != set(MANIFEST["inputs"]):
        raise ValueError("Missing or unknown application input")
    for name, shape in MANIFEST["inputs"].items():
        validate_value(payload[name], shape)
    widgets = {widget["id"]: widget["tool"] for widget in MANIFEST["widgets"]}
    results, arguments = {}, {}

    def call(identity: str, **kwargs: object) -> object:
        """Invoke one approved widget's tool once, recording actual arguments and result."""
        if type(identity) is not str or identity not in widgets or identity in results:
            raise ValueError("Unknown or repeated application call")
        contract = MANIFEST["tools"][widgets[identity]]
        if set(kwargs) - set(contract["parameters"]) or not set(contract["parameters"]) - set(
            contract.get("defaults", {})
        ) <= set(kwargs):
            raise ValueError("Missing or unknown tool argument")
        for name, value in kwargs.items():
            validate_value(value, contract["parameters"][name])
        function = getattr(importlib.import_module(contract["module"]), contract["function"])
        arguments[identity] = deepcopy(dict(contract.get("defaults", {})) | kwargs)
        results[identity] = validate_value(function(**deepcopy(kwargs)), contract["returns"])
        return deepcopy(results[identity])

    run(deepcopy(payload), call)
    if set(results) != set(widgets):
        raise ValueError("Connection code skipped a required tool call")
    return results, arguments


def analyze_text(payload: dict) -> dict:
    """Return complete observed results for the maintained native data entrypoint."""
    return execute(payload)[0]
