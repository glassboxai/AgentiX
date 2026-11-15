"""Desired regressions for requirements lost during the supervised GUI run."""

from types import SimpleNamespace
from unittest.mock import Mock


def test_creation_pipeline_retains_original_user_contract(system, monkeypatch):
    """A shortened manager purpose must not remove the user's input/error contract."""
    query = "Create a tiered bill; reject bool and floats with ValueError; return integer cents."
    decision = '{"action":"CREATE_TOOL","tool_name":"bill","purpose":"Calculate a tiered bill"}'
    monkeypatch.setattr(
        system.main, "Crew", Mock(return_value=SimpleNamespace(kickoff=lambda: decision))
    )
    received = []

    def downstream(tool_name, user_requirement):
        """Observe the actual contract received by the creation-stage boundary."""
        received.append(user_requirement)

    monkeypatch.setattr(system.main, "build_tool_pipeline", downstream)
    system.main.run_system(query)
    assert len(received) == 1
    assert query in received[0]
