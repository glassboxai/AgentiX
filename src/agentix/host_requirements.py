"""Explicit recovery for host-owned, reviewed runtime requirements.

The registry is maintained application code. Generated artifacts and browser input
never supply identifiers, commands, URLs or package-manager arguments. A caller
must separately obtain explicit human consent before calling :meth:`install`.
"""

import logging
import os
import subprocess
import sys
from collections.abc import Callable
from dataclasses import dataclass
from pathlib import Path

logger = logging.getLogger(__name__)


class HostRequirementInstallError(ValueError):
    """Report a bounded, non-sensitive failure while repairing a host requirement."""


@dataclass(frozen=True)
class HostRequirement:
    """Describe one immutable host dependency and its reviewed repair command.

    Attributes:
        identifier: Closed registry key, never supplied by generated artifacts.
        user_message: Consent text explaining the local host change.
        command: Exact process arguments, including the active managed Python.
    """

    identifier: str
    user_message: str
    command: tuple[str, ...]


def playwright_chromium_path() -> Path:
    """Return Playwright's selected Chromium path without starting a browser.

    Raises:
        RuntimeError: If the installed Playwright package cannot expose its
            browser metadata. The caller treats this as an unavailable host
            requirement and never exposes its implementation detail to users.
    """
    from playwright.sync_api import sync_playwright

    with sync_playwright() as driver:
        return Path(driver.chromium.executable_path)


def installer_environment(source: dict[str, str] | None = None) -> dict[str, str]:
    """Return only Windows variables needed by a reviewed local installer.

    Package indexes, targets, proxy settings and arbitrary inherited variables are
    deliberately omitted. The command uses an absolute Python executable and
    Python isolated mode, so no caller-supplied import location is inherited.
    """
    values = os.environ if source is None else source
    return {
        name: values[name]
        for name in ("SYSTEMROOT", "WINDIR", "LOCALAPPDATA", "USERPROFILE", "TEMP", "TMP")
        if values.get(name)
    }


class HostRequirements:
    """Probe and repair only requirements registered by maintained host code.

    Parameters:
        browser_path: Injected browser metadata probe used by tests and the
            application acceptance preflight.
        runner: Injected process boundary. Production uses a bounded subprocess
            call and captures installer output so it cannot leak into logs/UI.
        python: Managed interpreter used for the fixed Playwright command.
        environment_factory: Builds the scrubbed child environment.
    """

    def __init__(
        self,
        *,
        browser_path: Callable[[], Path] = playwright_chromium_path,
        runner: Callable[[tuple[str, ...], dict[str, str]], None] | None = None,
        python: str | None = None,
        environment_factory: Callable[[], dict[str, str]] = installer_environment,
    ) -> None:
        """Build the closed requirement registry without probing or installing."""
        executable = str(Path(python or sys.executable).resolve())
        self._browser_path = browser_path
        self._runner = runner or self._run
        self._environment_factory = environment_factory
        self._requirements = {
            "playwright-chromium": HostRequirement(
                identifier="playwright-chromium",
                user_message=(
                    "Independent GUI verification needs Playwright Chromium. Installing it "
                    "downloads only the Chromium revision selected by this AgentiX environment; "
                    "it does not install Python packages, Ollama, models, Tools or applications."
                ),
                command=(executable, "-I", "-m", "playwright", "install", "chromium"),
            )
        }

    def requirement(self, identifier: str) -> HostRequirement:
        """Return one registered requirement or reject arbitrary installer requests."""
        try:
            return self._requirements[identifier]
        except KeyError:
            raise ValueError("Unknown host requirement") from None

    def missing(self, identifier: str) -> HostRequirement | None:
        """Return a registered requirement only when its postcondition is absent."""
        requirement = self.requirement(identifier)
        try:
            available = self._browser_path().is_file()
        except Exception as error:
            logger.info(
                "event=host_requirement_probe_failed requirement=%s error_type=%s",
                identifier,
                type(error).__name__,
            )
            available = False
        return None if available else requirement

    def install(self, identifier: str) -> HostRequirement:
        """Run one reviewed installer and require its independent postcondition.

        The method does not request consent. Controllers must make the requirement
        visible to the owning user and call this only from the explicit install
        action. Raises a fixed error after failures and retains no child output.
        """
        requirement = self.requirement(identifier)
        if self.missing(identifier) is None:
            return requirement
        logger.info("event=host_requirement_install_started requirement=%s", identifier)
        try:
            self._runner(requirement.command, self._environment_factory())
        except Exception as error:
            logger.warning(
                "event=host_requirement_install_failed requirement=%s error_type=%s",
                identifier,
                type(error).__name__,
            )
            raise HostRequirementInstallError(
                "Host dependency installation failed. The reviewed proposal remains pending."
            ) from None
        if self.missing(identifier) is not None:
            logger.warning("event=host_requirement_install_unverified requirement=%s", identifier)
            raise HostRequirementInstallError(
                "Host dependency installation could not be verified. The reviewed proposal remains pending."
            )
        logger.info("event=host_requirement_install_verified requirement=%s", identifier)
        return requirement

    @staticmethod
    def _run(command: tuple[str, ...], environment: dict[str, str]) -> None:
        """Execute the fixed installer with bounded retained diagnostics only."""
        subprocess.run(
            command,
            check=True,
            capture_output=True,
            text=True,
            timeout=600,
            env=environment,
        )
