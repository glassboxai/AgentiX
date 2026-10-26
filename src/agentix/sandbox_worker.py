"""Disposable child entrypoint; never imported to execute artifacts in the host.

All output is untrusted. Parent validates framing, schema and OS status. Tests
share this interpreter and can tamper with unittest; reports are not attestations.
"""

import contextlib
import importlib.util
import json
import sys
import unittest
from pathlib import Path


def main() -> None:
    """Read a bounded parent-authored request and emit one JSON report on stdout."""
    folder = Path(__file__).resolve().parent
    sys.path.insert(0, str(folder))
    request = json.loads((folder / "request.json").read_text(encoding="utf-8"))
    # Keep ordinary prints separate from the report; the parent bounds both.
    with contextlib.redirect_stdout(sys.stderr):
        if request["kind"] == "tests":
            suite = unittest.defaultTestLoader.discover(
                str(folder), pattern=f"{request['tool_name']}_tests.py"
            )
            result = unittest.TextTestRunner(stream=sys.stderr, verbosity=1).run(suite)
            report = dict(
                kind="tests",
                run=result.testsRun,
                failures=len(result.failures),
                errors=len(result.errors),
                skipped=len(result.skipped),
                successful=result.wasSuccessful() and not result.expectedFailures,
            )
        else:
            path = folder / f"{request['tool_name']}_code.py"
            spec = importlib.util.spec_from_file_location(request["tool_name"], path)
            module = importlib.util.module_from_spec(spec)
            spec.loader.exec_module(module)
            name = request["function_name"]
            if name.startswith("_") or not callable(getattr(module, name, None)):
                raise ValueError("Requested public function does not exist")
            if request["kind"] == "observation":
                try:
                    value = getattr(module, name)(**request["kwargs"])
                except Exception as exc:
                    report = dict(
                        kind="observation", status="raised", exception_type=type(exc).__name__
                    )
                else:
                    # JSON is the only boundary representation. No parent ever
                    # loads a Python object or exception supplied by this child.
                    json.dumps(value, allow_nan=False)
                    report = dict(kind="observation", status="returned", value=value)
            else:
                report = dict(kind="call", result=str(getattr(module, name)(**request["kwargs"])))
    print("\nAGENTIX_REPORT:" + json.dumps(report), flush=True)
    if report["kind"] == "tests" and not report["successful"]:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
