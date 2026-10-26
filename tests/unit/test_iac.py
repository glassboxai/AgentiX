"""IAC-001 offline contracts using trusted temporary data and PowerShell providers.

No package manager, network request, installer or application server is started.
"""

import json
import os
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parents[2]
MODULE = ROOT / "infra" / "Agentix.Iac.psm1"
PWSH = shutil.which("pwsh") or shutil.which("powershell.exe")


def powershell(body):
    """Evaluate a trusted test body, failing on PowerShell errors and malformed JSON."""
    command = (
        "$ErrorActionPreference='Stop'; Import-Module '"
        + str(MODULE).replace("'", "''")
        + "' -Force; function New-IacFixtureState { param($Config) "
        + "@{packageManager=@{available=$true;version='fixture';path='fixture'};python=@{version=$Config.pythonVersion;path='fixture';hash='x'};"
        + "ollama=@{version=$Config.ollamaVersion;path='fixture';hash='x'};"
        + "dsc=@{version=$Config.dscVersion;path='fixture';hash='x'};"
        + "environment=@{present=$true};launchers=@{present=$true};location=@{present=$true};"
        + "model=@{present=$true;server=$true;digest=$Config.modelDigest;version=$Config.ollamaVersion};portFree=$true}}; "
        + body
    )
    with tempfile.TemporaryDirectory(prefix="agentix-iac-unit-") as local:
        command = "$env:LOCALAPPDATA='" + local.replace("'", "''") + "';" + command
        result = subprocess.run(
            [PWSH, "-NoProfile", "-NonInteractive", "-Command", command],
            capture_output=True,
            text=True,
            timeout=35,
            check=False,
        )
    assert result.returncode == 0, result.stderr
    return json.loads(result.stdout)


def test_plan_is_read_only_and_idempotent(tmp_path):
    """A converged inventory produces no changes and never invokes an actuator."""
    result = powershell(
        "$c=Read-IacConfiguration; $s=New-IacFixtureState -Config $c; "
        "$p=Get-IacPlan -Config $c -State $s; "
        "@{changes=@($p.changes).Count; valid=(Test-IacPlan $p $c $s)} | ConvertTo-Json"
    )
    assert result == {"changes": 0, "valid": True}


@pytest.mark.parametrize("field", ["model", "pythonVersion", "port", "unknown"])
def test_configuration_rejects_unsafe_or_unknown_values(field):
    """Models, Python, ports and configuration fields cannot silently widen scope."""
    result = powershell(
        "$c=Read-IacConfiguration; $c['"
        + field
        + "']='unsafe'; $r=try {Assert-IacConfiguration $c; $false} catch {$true}; ConvertTo-Json $r"
    )
    assert result is True


def test_plan_rejects_state_drift_and_tampering():
    """Changes to the configuration, planned actions or observed state invalidate review."""
    result = powershell(
        "$c=Read-IacConfiguration; $s=New-IacFixtureState -Config $c; "
        "$p=Get-IacPlan -Config $c -State $s; $s.python.version='wrong'; "
        "$drift=Test-IacPlan $p $c $s; $s=New-IacFixtureState -Config $c; "
        "$p.changes=@('erase_data'); $tamper=Test-IacPlan $p $c $s; "
        "@{drift=$drift;tamper=$tamper}|ConvertTo-Json"
    )
    assert result == {"drift": False, "tamper": False}


def test_missing_model_requires_explicit_download_and_port_conflict_blocks():
    """Ordinary application of a plan cannot download models or replace listeners."""
    result = powershell(
        "$c=Read-IacConfiguration; $s=New-IacFixtureState -Config $c; $s.model.present=$false; $s.model.digest=''; "
        "$p=Get-IacPlan -Config $c -State $s; "
        "$allowed=Get-IacPlan -Config $c -State $s -DownloadModel; "
        "$s.portFree=$false; $busy=Get-IacPlan -Config $c -State $s -DownloadModel; "
        "@{blocked=@($p.blockers).Count;allowed=@($allowed.changes);busy=@($busy.blockers).Count}|ConvertTo-Json"
    )
    assert result["blocked"] > 0
    assert "model" in result["allowed"]
    assert result["busy"] > 0


def test_failed_resource_stops_dependent_changes():
    """A failed prerequisite is not masked and does not start dependent resources."""
    result = powershell(
        "$c=Read-IacConfiguration; $s=New-IacFixtureState -Config $c; "
        "$s.python.version='missing';$s.environment.present=$false;$s.launchers.present=$false; "
        "$p=Get-IacPlan -Config $c -State $s; $calls=[Collections.Generic.List[string]]::new(); "
        "try {Invoke-IacConverge -Config $c -Plan $p -Observe {$s} -Set {param($id,$cfg,$plan) "
        "$calls.Add($id);throw 'fixture installation denied'};throw 'unexpected success'} "
        "catch {@{calls=@($calls);error=$_.Exception.Message}|ConvertTo-Json}"
    )
    assert result["calls"] == ["python"]
    assert "fixture installation denied" in result["error"]


def test_paths_and_reparse_boundaries(tmp_path):
    """Managed paths accept spaces but reject siblings and existing links."""
    result = powershell(
        "$root='" + str(tmp_path / "space root").replace("'", "''") + "'; "
        "Assert-IacContained ($root+'\\child') $root; "
        "$r=try {Assert-IacContained ($root+'-sibling\\child') $root;$false} catch {$true};ConvertTo-Json $r"
    )
    assert result is True


def test_runtime_settings_support_managed_launch(tmp_path):
    """Managed startup selects new storage and a port without changing legacy defaults."""
    from agentix.settings import Settings

    path = tmp_path / "owned tools"
    settings = Settings.from_environment(
        {
            "AGENTIX_TOOLS_ROOT": str(path),
            "AGENTIX_SERVER_PORT": "7873",
            "AGENTIX_OPEN_BROWSER": "false",
        },
        base_dir=tmp_path,
    )
    assert settings.tools_root == path
    assert settings.server_port == 7873
    assert settings.open_browser is False
    legacy = Settings.from_environment({}, base_dir=tmp_path)
    assert legacy.server_port == 7860
    assert legacy.open_browser is True


@pytest.mark.parametrize("value", ["0", "65536", "abc", "7860.5"])
def test_runtime_rejects_invalid_port(value, tmp_path):
    """Invalid deployment configuration fails before network or storage startup."""
    from agentix.settings import Settings

    with pytest.raises(ValueError):
        Settings.from_environment({"AGENTIX_SERVER_PORT": value}, base_dir=tmp_path)


def test_inventory_fingerprint_accepts_adapted_empty_scalars():
    """IAC-ERR-001: observed process/JSON scalar wrappers must hash without property errors."""
    result = powershell(
        "$x=Test-Path -LiteralPath 'does-not-exist-iac-fixture'; Get-IacDigest @{owned=$x;items=@()} | ConvertTo-Json"
    )
    assert len(result) == 64


def test_converged_apply_does_not_call_actuators():
    """An unchanged second application cannot reinstall packages or rewrite launchers."""
    result = powershell(
        "$c=Read-IacConfiguration;$s=New-IacFixtureState $c;$p=Get-IacPlan $c $s; $r=Invoke-IacConverge -Config $c -Plan $p -Observe {$s} -Set {throw 'unexpected mutation'};@{count=@($r.changed).Count}|ConvertTo-Json"
    )
    assert result == {"count": 0}


def test_unknown_model_digest_blocks_even_with_download_consent():
    """A changed installed tag must not be silently replaced after review."""
    result = powershell(
        "$c=Read-IacConfiguration;$s=New-IacFixtureState $c;$s.model.present=$false;$s.model.digest='different';$p=Get-IacPlan $c $s -DownloadModel;@{blocked=@($p.blockers).Count;actions=@($p.changes)}|ConvertTo-Json"
    )
    assert result["blocked"] > 0
    assert "model" not in result["actions"]


def test_configuration_change_invalidates_review():
    """A port change after review requires a new plan even when current observations match."""
    result = powershell(
        "$c=Read-IacConfiguration;$s=New-IacFixtureState $c;$p=Get-IacPlan $c $s;$c.port=7874;Test-IacPlan $p $c $s|ConvertTo-Json"
    )
    assert result is False


def test_incompatible_prerequisite_is_not_upgraded():
    """Installed foreign versions are diagnosed, not scheduled for replacement."""
    result = powershell(
        "$c=Read-IacConfiguration;$s=New-IacFixtureState $c;$s.python.version='3.13.0';$p=Get-IacPlan $c $s;@{blocked=@($p.blockers).Count;actions=@($p.changes)}|ConvertTo-Json"
    )
    assert result["blocked"] > 0
    assert "python" not in result["actions"]


def test_managed_file_links_are_rejected(tmp_path):
    """Existing directory junctions cannot redirect managed writes outside their root."""
    outside = tmp_path / "outside"
    outside.mkdir()
    root = tmp_path / "managed"
    root.mkdir()
    result = powershell(
        "$root='"
        + str(root)
        + "';$outside='"
        + str(outside)
        + "';New-Item -ItemType Junction -Path ($root+'\\link') -Target $outside|Out-Null;$r=try{Assert-IacContained ($root+'\\link\\file') $root;$false}catch{$true};$r|ConvertTo-Json"
    )
    assert result is True


def test_plan_inventory_does_not_create_files_or_contact_network(tmp_path):
    """Real inventory with absent prerequisites is read-only and network is explicitly doubled."""
    result = powershell(
        "$env:LOCALAPPDATA='"
        + str(tmp_path)
        + "';& (Get-Module Agentix.Iac) {function script:Invoke-RestMethod {throw 'offline fixture'};function script:Get-IacPackageManager {@{available=$true;version='fixture';path='fixture'}}};$c=Read-IacConfiguration;$s=Get-IacState $c;@{missing=$s.python.version;present=$s.environment.present}|ConvertTo-Json"
    )
    assert result == {"missing": "missing", "present": False}
    assert list(tmp_path.iterdir()) == []


def test_corrupt_download_is_rejected_before_extraction(tmp_path):
    """Pinned archives cannot be applied when a fake downloader returns changed bytes."""
    result = powershell(
        "$env:LOCALAPPDATA='"
        + str(tmp_path)
        + "';& (Get-Module Agentix.Iac) {function script:Invoke-WebRequest {param($Uri,$OutFile,[switch]$UseBasicParsing,$MaximumRedirection);[IO.File]::WriteAllText($OutFile,'corrupt fixture')}};$c=Read-IacConfiguration;$r=try{Get-IacArchive $c 'dsc';'unexpected'}catch{$_.Exception.Message};$r|ConvertTo-Json"
    )
    assert "integrity check failed" in result
    assert not (tmp_path / "AgentiX/v3/tooling").exists()


def test_environment_refuses_unowned_existing_directory(tmp_path):
    """Provisioning never adopts or clears another environment directory."""
    result = powershell(
        "$env:LOCALAPPDATA='"
        + str(tmp_path)
        + "';$c=Read-IacConfiguration;$p=Get-IacPaths $c;New-Item -ItemType Directory -Path $p.environment -Force|Out-Null;$r=try{Set-IacResource 'environment' $c @{};'unexpected'}catch{$_.Exception.Message};$r|ConvertTo-Json"
    )
    assert "unowned environment" in result


@pytest.mark.parametrize(
    "environment", [{"AGENTIX_OPEN_BROWSER": "yes"}, {"AGENTIX_TOOLS_ROOT": "relative"}]
)
def test_invalid_runtime_configuration_fails_before_start(environment, tmp_path):
    """The managed launcher cannot silently reinterpret ambiguous settings."""
    from agentix.settings import Settings

    with pytest.raises(ValueError):
        Settings.from_environment(environment, base_dir=tmp_path)


def test_windows_powershell_adapter_without_ambient_modules():
    """IAC-ERR-002: DSC resources load OS modules without trusting an inherited module path."""
    executable = Path(os.environ["SystemRoot"]) / "System32/WindowsPowerShell/v1.0/powershell.exe"
    command = (
        "$ErrorActionPreference='Stop';$env:PSModulePath='missing-fixture-modules';$PSModuleAutoLoadingPreference='None';Import-Module '"
        + str(MODULE)
        + "' -Force;$c=Read-IacConfiguration;$p=Get-IacPaths $c;@{lock=$p.lock}|ConvertTo-Json"
    )
    result = subprocess.run(
        [str(executable), "-NoProfile", "-NonInteractive", "-Command", command],
        capture_output=True,
        text=True,
        timeout=35,
    )
    assert result.returncode == 0, result.stderr
    assert len(json.loads(result.stdout)["lock"]) == 64


def test_launcher_restores_process_configuration_after_failure(tmp_path):
    """IAC-ERR-003: a closed/failed managed launcher must not change later legacy launches."""
    result = powershell(
        "$env:LOCALAPPDATA='"
        + str(tmp_path)
        + "';$env:OLLAMA_MODEL='prior-model';& (Get-Module Agentix.Iac) {function script:Test-IacDeployment {@{inDesiredState=$true}};function script:Get-IacState {@{portFree=$true}}};$c=Read-IacConfiguration;$message=try {Start-IacApplication -Config $c -Mode Cli -Run {throw 'trusted fixture failure'};'unexpected'} catch {$_.Exception.Message};@{restored=($env:OLLAMA_MODEL -eq 'prior-model');error=$message}|ConvertTo-Json"
    )
    assert result["restored"] is True
    assert "trusted fixture failure" in result["error"]


def test_fingerprints_match_windows_powershell_and_powershell_core():
    """IAC-ERR-004: cross-edition locale sorting cannot invalidate an unchanged DSC plan."""
    expected = powershell("Get-IacSourceDigest|ConvertTo-Json")
    executable = Path(os.environ["SystemRoot"]) / "System32/WindowsPowerShell/v1.0/powershell.exe"
    result = subprocess.run(
        [
            str(executable),
            "-NoProfile",
            "-NonInteractive",
            "-Command",
            "Import-Module '" + str(MODULE) + "' -Force;Get-IacSourceDigest|ConvertTo-Json",
        ],
        capture_output=True,
        text=True,
        timeout=35,
    )
    assert result.returncode == 0, result.stderr
    assert json.loads(result.stdout) == expected


def test_windows_process_adapter_accepts_stderr_with_success():
    """IAC-ERR-005: Windows PowerShell stderr records do not override a native zero exit."""
    executable = Path(os.environ["SystemRoot"]) / "System32/WindowsPowerShell/v1.0/powershell.exe"
    command = (
        "$ErrorActionPreference='Stop';Import-Module '"
        + str(MODULE)
        + "' -Force;$r=Invoke-IacProcess '"
        + sys.executable
        + "' @('-I','-c','import sys;sys.stderr.write(\"fixture warning\");print(\"ready\")');@{output=$r}|ConvertTo-Json"
    )
    result = subprocess.run(
        [str(executable), "-NoProfile", "-NonInteractive", "-Command", command],
        capture_output=True,
        text=True,
        timeout=35,
    )
    assert result.returncode == 0, result.stderr
    assert "ready" in json.loads(result.stdout)["output"]


def test_zero_exit_without_convergence_stops_dependents():
    """IAC-ERR-006: a successful installer exit alone cannot authorize dependent work."""
    result = powershell(
        "$c=Read-IacConfiguration;$s=New-IacFixtureState $c;$s.python.version='missing';$s.environment.present=$false;$p=Get-IacPlan $c $s;$calls=[Collections.Generic.List[string]]::new();$outcome=try{Invoke-IacConverge -Config $c -Plan $p -Observe {$s} -Set {param($id,$cfg,$review)$calls.Add($id)}|Out-Null;'unexpected'}catch{$_.Exception.Message};@{calls=@($calls);error=$outcome}|ConvertTo-Json"
    )
    assert result["calls"] == ["python"]
    assert "converge" in result["error"].lower()


def test_managed_root_resolves_windows_host_redirection(tmp_path):
    """IAC-ERR-007: managed launch paths use the OS-resolved location, not an app-host alias."""
    result = powershell(
        "Resolve-IacRoot -Root '"
        + str(tmp_path)
        + "' -Python '"
        + sys.executable
        + "'|ConvertTo-Json"
    )
    assert Path(result) == tmp_path.resolve()


@pytest.mark.parametrize(
    "status,publisher",
    [
        ("HashMismatch", "Microsoft Corporation"),
        ("NotTrusted", "Microsoft Corporation"),
        ("NotSigned", "Microsoft Corporation"),
        ("Valid", "Unrelated Publisher"),
    ],
)
def test_prerequisite_signatures_reject_invalid_or_foreign_publishers(status, publisher):
    """New native prerequisites require a valid signature from their expected publisher."""
    result = powershell(
        "$r=try {Assert-IacSignature -Path 'trusted-fixture' -Kind dsc -Check {param($path)@{Status='"
        + status
        + "';SignerCertificate=@{Subject='CN="
        + publisher
        + "'}}};'unexpected'}catch{$_.Exception.Message};$r|ConvertTo-Json"
    )
    assert "Binary signature verification failed" in result


def test_prerequisite_signature_accepts_reviewed_publisher():
    """A verified vendor signature permits the already hash-pinned prerequisite."""
    result = powershell(
        "Assert-IacSignature -Path 'trusted-fixture' -Kind dsc -Check {param($path)@{Status='Valid';SignerCertificate=@{Subject='CN=Microsoft Corporation'}}};$true|ConvertTo-Json"
    )
    assert result is True


def test_missing_package_manager_blocks_missing_python():
    """A missing Windows package manager is diagnosed before dependent installation."""
    result = powershell(
        "$c=Read-IacConfiguration;$s=New-IacFixtureState $c;$s.python.version='missing';$s.packageManager.available=$false;$p=Get-IacPlan $c $s;@{blocked=@($p.blockers).Count}|ConvertTo-Json"
    )
    assert result["blocked"] > 0


def test_dependency_install_cannot_inherit_pip_target_or_extra_sources(tmp_path):
    """IAC-ERR-008: ambient pip variables cannot redirect writes outside the owned environment."""
    body = (
        "$env:LOCALAPPDATA='"
        + str(tmp_path)
        + "';$env:PIP_TARGET='outside-fixture';$env:PIP_FIND_LINKS='https://unapproved.invalid';$env:PIP_USER='1';& (Get-Module Agentix.Iac) {function script:Invoke-IacProcess {param($Executable,$Arguments)if ('install' -in $Arguments) {$script:observed=@{target=$env:PIP_TARGET;links=$env:PIP_FIND_LINKS;user=$env:PIP_USER;index=$env:PIP_INDEX_URL;hashes=('--require-hashes' -in $Arguments)}};return ''}};$c=Read-IacConfiguration;Set-IacResource 'environment' $c @{};$o=& (Get-Module Agentix.Iac) {$script:observed};@{observed=$o;restored=$env:PIP_TARGET}|ConvertTo-Json -Depth 5"
    )
    result = powershell(body)
    assert result["observed"]["target"] is None
    assert result["observed"]["links"] is None
    assert result["observed"]["user"] is None
    assert result["observed"]["index"] == "https://pypi.org/simple"
    assert result["observed"]["hashes"] is True
    assert result["restored"] == "outside-fixture"


def test_native_argument_quoting_preserves_data():
    """Spaces, quotes, trailing backslashes and shell-like text stay literal arguments."""
    values = [
        "space value",
        'quoted "text"',
        "C:" + chr(92) + "path with spaces" + chr(92),
        "safe;$(not-a-command)",
    ]
    payload = json.dumps(values).replace("'", "''")
    result = powershell(
        "$values=ConvertFrom-Json '"
        + payload
        + "';$arguments=@('-I','-c','import json,sys;print(json.dumps(sys.argv[1:]))')+@($values);Invoke-IacProcess '"
        + sys.executable
        + "' $arguments"
    )
    assert result == values


def test_launcher_preserves_absent_environment_variables(tmp_path):
    """IAC-ERR-009: unset legacy settings must remain absent, not empty strings."""
    result = powershell(
        "$env:LOCALAPPDATA='"
        + str(tmp_path)
        + "';Remove-Item Env:AGENTIX_SERVER_PORT -ErrorAction SilentlyContinue;& (Get-Module Agentix.Iac) {function script:Test-IacDeployment {@{inDesiredState=$true}};function script:Get-IacState {@{portFree=$true}}};Start-IacApplication -Config (Read-IacConfiguration) -Mode Cli -Run {};Test-Path Env:AGENTIX_SERVER_PORT|ConvertTo-Json"
    )
    assert result is False


def test_location_receipt_keeps_deployment_independent_of_host_alias(tmp_path):
    """IAC-ERR-007: a normal terminal must find the physical deployment created by a packaged host."""
    result = powershell(
        "$c=Read-IacConfiguration;$physical=Join-Path $env:LOCALAPPDATA 'host-cache\\AgentiX\\v3';New-Item -ItemType Directory -Path $physical -Force|Out-Null;$fixture=Join-Path $env:LOCALAPPDATA 'infra';New-Item -ItemType Directory -Path $fixture|Out-Null;Copy-Item '"
        + str(ROOT / "infra/runtime.lock.txt")
        + "' (Join-Path $fixture 'runtime.lock.txt');& (Get-Module Agentix.Iac) {param($directory)$script:InfraRoot=$directory} $fixture;Save-IacLocation -Root $physical;$actual=Get-IacPaths $c;@{actual=$actual.root;expected=$physical}|ConvertTo-Json"
    )
    assert result["actual"] == result["expected"]
