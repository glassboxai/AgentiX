"""Pipeline tests substitute only slow model/native/browser boundaries."""

import json

from schema3_package import widget_source

from agentix.application.app_workflow import ApplicationPipeline
from agentix.lab.application_artifacts import application_digest


def test_pipeline_persists_exact_proposals_without_approval(tmp_path):
    """Catch overwriting proposals, auto-approval or importing generated Python."""
    requests = []

    def factory(folder):
        """Build a model-boundary fixture for the independently exercised pipeline."""

        def client(role, content):
            """Return a controlled model-boundary proposal without executing source."""
            requests.append(role)
            if role == "General Widget Designer":
                module = content["requirements"]["approved_tool_contract"]["module"]
                return {
                    "widget_code": widget_source(module),
                    "tests_code": 'raise RuntimeError("must not execute tests on host")',
                    "notes": "fixture",
                }
            catalog = content["requirements"]["approved_catalog"]
            return {
                "inputs": {"text": {"type": "string", "description": "Text to inspect"}},
                "widgets": [{"id": name, "tool": name} for name in sorted(catalog)],
                "connection_code": (
                    '"""Connect approved catalog calls."""\n'
                    "def run(payload: dict, call) -> None:\n"
                    '    """Call every approved tool with the shared text input."""\n'
                    + "".join(
                        f'    call("{name}", text=payload["text"])\n' for name in sorted(catalog)
                    )
                ),
                "notes": "fixture",
            }

        return client

    from test_application_catalog import installed, registry

    fixtures = tmp_path / "installed"
    fixtures.mkdir()
    tools = registry(installed(fixtures)).resolve()
    candidate = ApplicationPipeline(tmp_path / "apps", factory).generate(
        "Count words and vowels", tools=tools
    )
    assert requests == ["General Assembler", "General Widget Designer", "General Widget Designer"]
    manifest = json.loads((candidate.package / "application.json").read_bytes())
    assert manifest["schema_version"] == 3
    assert set(manifest["tools"]) == set(tools)
    assert len(application_digest(candidate.package)) == 64
    assert not candidate.verified
    assert not candidate.approved
    proposals = json.loads((candidate.folder / "proposals.json").read_bytes())
    assert (
        "must not execute tests on host"
        in proposals["widgets"]["count_vowels_in_text"]["tests_code"]
    )


def test_pipeline_canonicalizes_its_owned_data_root(tmp_path):
    """Catch packaging an unresolved operator data alias rejected by source capture."""
    pipeline = ApplicationPipeline(tmp_path / "child" / ".." / "apps")
    assert pipeline.root == tmp_path / "apps"
