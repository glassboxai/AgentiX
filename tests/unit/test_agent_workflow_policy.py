"""Check instructions delivered at agent/task construction, not source-file text."""

import pytest


@pytest.mark.parametrize("role", ["manager", "architect", "coder", "tester"])
def test_agents_receive_application_workflow_obligations(system, role):
    """Verify agents receive application workflow obligations."""
    agent = getattr(system.main, role + "_agent")
    delivered = agent.backstory
    for obligation in (
        "English specifications",
        "normal values",
        "exact tier boundaries",
        "invalid types",
        "human review",
        "EXECUTE",
        "not merely answering",
    ):
        assert obligation in delivered
    assert agent.verbose is True


def test_roles_do_not_receive_conflicting_creation_responsibilities(system):
    """Verify roles do not receive conflicting creation responsibilities."""
    assert "pure standalone top-level functions" in system.main.architect_agent.goal
    assert "iterate until all tests pass" not in system.main.tester_agent.goal
    assert "empty catalog" in system.main.manager_agent.backstory


def test_empty_catalog_manager_has_no_tools_but_execution_manager_keeps_them(system, monkeypatch):
    """Catch prompts that forbid guessed verification but still expose its tool."""
    from types import SimpleNamespace

    assigned = []

    def crew(**kwargs):
        """Provide crew for the enclosing trusted test fixture."""
        assigned.append(kwargs["tasks"][0].agent)
        return SimpleNamespace(kickoff=lambda: "Plain conversation")

    monkeypatch.setattr(system.main, "Crew", crew)
    assert system.main.run_system("hello") == "Plain conversation"
    assert assigned[0].tools == []
    assert system.main.manager_agent.tools
