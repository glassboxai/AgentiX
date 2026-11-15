"""Regression tests for explicit host-owned dependency recovery."""

import pytest


def test_missing_registered_requirement_has_fixed_review_details(tmp_path):
    """A missing requirement exposes only host-maintained consent details."""
    from agentix.host_requirements import HostRequirements

    service = HostRequirements(browser_path=lambda: tmp_path / "missing.exe")

    requirement = service.missing("playwright-chromium")

    assert requirement is not None
    assert requirement.identifier == "playwright-chromium"
    assert requirement.command[-3:] == ("playwright", "install", "chromium")
    assert "generated" not in requirement.user_message.lower()


def test_install_runs_only_registered_command_and_rechecks(tmp_path):
    """An explicit install uses the active Python and accepts only a verified result."""
    from agentix.host_requirements import HostRequirements

    browser = tmp_path / "chromium.exe"
    seen = []

    def runner(command, environment):
        """Record the exact immutable host command and emulate browser installation."""
        seen.append((command, environment))
        browser.write_bytes(b"browser")

    service = HostRequirements(
        browser_path=lambda: browser,
        runner=runner,
        python="C:/host/python.exe",
        environment_factory=lambda: {},
    )

    assert service.install("playwright-chromium").identifier == "playwright-chromium"
    assert seen == [(("C:\\host\\python.exe", "-I", "-m", "playwright", "install", "chromium"), {})]


def test_unknown_or_unsatisfied_requirement_cannot_be_installed(tmp_path):
    """No caller can turn the recovery boundary into arbitrary package execution."""
    from agentix.host_requirements import HostRequirementInstallError, HostRequirements

    calls = []
    service = HostRequirements(
        browser_path=lambda: tmp_path / "still-missing.exe",
        runner=lambda command, environment: calls.append((command, environment)),
    )

    with pytest.raises(ValueError, match="Unknown host requirement"):
        service.install("pip-anything")
    with pytest.raises(HostRequirementInstallError, match="could not be verified"):
        service.install("playwright-chromium")
    assert len(calls) == 1


def test_installer_environment_excludes_package_manager_and_proxy_configuration():
    """A reviewed browser download cannot inherit arbitrary package sources or targets."""
    from agentix.host_requirements import installer_environment

    environment = installer_environment(
        {
            "SYSTEMROOT": "C:/Windows",
            "LOCALAPPDATA": "C:/Users/example/AppData/Local",
            "PIP_INDEX_URL": "https://untrusted.invalid",
            "PIP_TARGET": "C:/outside",
            "HTTPS_PROXY": "http://proxy.invalid",
        }
    )

    assert environment == {
        "SYSTEMROOT": "C:/Windows",
        "LOCALAPPDATA": "C:/Users/example/AppData/Local",
    }
