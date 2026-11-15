"""IAC-001 offline contracts using trusted temporary data and PowerShell providers.

No package manager, network request, installer or application server is started.
"""

import json
import os
import re
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
    # Inject the filesystem location boundary; production ignores virtualized LOCALAPPDATA.
    body = re.sub(
        r"(\$env:LOCALAPPDATA='[^']*';)",
        lambda match: match.group()
        + "& (Get-Module Agentix.Iac) {$script:UserLocalRoot=$env:LOCALAPPDATA};",
        body,
    )
    command = (
        "$ErrorActionPreference='Stop'; Import-Module '"
        + str(MODULE).replace("'", "''")
        + "' -Force; & (Get-Module Agentix.Iac) {$script:UserLocalRoot=$env:LOCALAPPDATA}; function Read-IacConfiguration {$config=& (Get-Module Agentix.Iac) {Read-IacConfiguration};$config.home=Join-Path $env:LOCALAPPDATA 'agentix-data\\v7';$config.toolsRoot=Join-Path $env:LOCALAPPDATA 'checkout\\generated_tools';return $config}; function New-IacFixtureState { param($Config) "
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


def test_schema_two_configuration_selects_separate_home_and_artifact_roots():
    """IAC-010: reviewed schema-2 roots isolate runtime state from tool artifacts."""
    result = powershell(
        "$c=Read-IacConfiguration;$c.schema=2;$c.home=Join-Path $env:LOCALAPPDATA 'agentix-data\\v7';"
        "$c.toolsRoot=Join-Path $env:LOCALAPPDATA 'checkout\\generated_tools';Assert-IacConfiguration $c;"
        "$paths=Get-IacPaths $c;@{home=$paths.root;tools=$paths.tools;environment=$paths.environment}|ConvertTo-Json"
    )
    assert result["home"].endswith("agentix-data\\v7")
    assert result["tools"].endswith("checkout\\generated_tools")
    assert result["environment"].startswith(result["home"])


def test_checked_in_schema_two_configuration_declares_approved_roots():
    """IAC-010: the reviewed profile declares the approved V7 runtime and artifact roots."""
    configuration = json.loads((ROOT / "infra" / "windows.local.json").read_text(encoding="utf-8"))

    assert configuration["schema"] == 2
    assert configuration["home"] == r"D:\AI\Agentix-data\v7"
    assert configuration["toolsRoot"] == r"D:\AI\AgentiX_v7\generated_tools"


@pytest.mark.parametrize(
    "field,value",
    [("home", "relative"), ("toolsRoot", "relative")],
)
def test_schema_two_configuration_rejects_relative_roots(field, value):
    """IAC-010: configurable deployment roots must remain explicit absolute paths."""
    result = powershell(
        "$c=Read-IacConfiguration;$c.schema=2;$c.home=Join-Path $env:LOCALAPPDATA 'agentix-data\\v7';"
        "$c.toolsRoot=Join-Path $env:LOCALAPPDATA 'checkout\\generated_tools';$c."
        + field
        + "='"
        + value
        + "';$r=try{Assert-IacConfiguration $c;$false}catch{$true};$r|ConvertTo-Json"
    )
    assert result is True


def test_schema_two_configuration_rejects_overlapping_runtime_and_artifact_roots():
    """IAC-010: artifact storage cannot be a writable subdirectory of managed runtime state."""
    result = powershell(
        "$c=Read-IacConfiguration;$c.schema=2;$c.home=Join-Path $env:LOCALAPPDATA 'agentix-data\\v7';"
        "$c.toolsRoot=$c.home;$r=try{Assert-IacConfiguration $c;$false}catch{$true};$r|ConvertTo-Json"
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


def test_ollama_state_does_not_change_plan_and_port_conflict_blocks():
    """External Ollama state cannot affect IaC planning or trigger provisioning."""
    result = powershell(
        "$c=Read-IacConfiguration; $s=New-IacFixtureState -Config $c; $s.model.present=$false; $s.model.digest=''; "
        "$p=Get-IacPlan -Config $c -State $s; "
        "$s.portFree=$false; $busy=Get-IacPlan -Config $c -State $s; "
        "@{blocked=@($p.blockers).Count;changes=@($p.changes);busy=@($busy.blockers).Count}|ConvertTo-Json"
    )
    assert result["blocked"] == 0
    assert "model" not in result["changes"]
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
            "AGENTIX_HOME": str(tmp_path / "deployment"),
            "AGENTIX_TOOLS_ROOT": str(path),
            "AGENTIX_SERVER_PORT": "7873",
            "AGENTIX_OPEN_BROWSER": "false",
        },
        base_dir=tmp_path,
    )
    assert settings.tools_root == path
    assert settings.server_port == 7873
    assert settings.open_browser is False
    legacy = Settings.from_environment(
        {
            "AGENTIX_HOME": str(tmp_path / "deployment"),
            "AGENTIX_TOOLS_ROOT": str(tmp_path / "deployment" / "tools"),
        },
        base_dir=tmp_path,
    )
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


def test_ollama_metadata_is_not_an_iac_blocker():
    """Model identity belongs to application-level TOFU, not the installer plan."""
    result = powershell(
        "$c=Read-IacConfiguration;$s=New-IacFixtureState $c;$s.model.present=$false;$s.model.digest='different';$p=Get-IacPlan $c $s;@{blocked=@($p.blockers).Count;actions=@($p.changes)}|ConvertTo-Json"
    )
    assert result == {"blocked": 0, "actions": []}


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
    assert not (tmp_path / "AgentiX/v5/tooling").exists()


def test_environment_refuses_unowned_existing_directory(tmp_path):
    """Provisioning never adopts or clears another environment directory."""
    result = powershell(
        "$env:LOCALAPPDATA='"
        + str(tmp_path)
        + "';$c=Read-IacConfiguration;$p=Get-IacPaths $c;New-Item -ItemType Directory -Path $p.environment -Force|Out-Null;$r=try{Set-IacResource 'environment' $c @{};'unexpected'}catch{$_.Exception.Message};$r|ConvertTo-Json"
    )
    assert "unowned environment" in result


@pytest.mark.parametrize(
    "overrides",
    [
        {"AGENTIX_OPEN_BROWSER": "yes"},
        {"AGENTIX_TOOLS_ROOT": "relative"},
        {"AGENTIX_TOOLS_ROOT": ""},
    ],
)
def test_invalid_runtime_configuration_fails_before_start(overrides, tmp_path):
    """The managed launcher cannot silently reinterpret ambiguous settings."""
    from agentix.settings import Settings

    environment = {
        "AGENTIX_HOME": str(tmp_path / "home"),
        "AGENTIX_TOOLS_ROOT": str(tmp_path / "tools"),
        **overrides,
    }
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
        + "';$env:OLLAMA_MODEL='prior-model';& (Get-Module Agentix.Iac) {function script:Test-IacLaunch {@{inDesiredState=$true;warnings=@()}};function script:Get-IacState {@{portFree=$true}};function script:Get-IacPlaywrightChromiumPath {return $null}};$c=Read-IacConfiguration;$message=try {Start-IacApplication -Config $c -Mode Cli -Run {throw 'trusted fixture failure'};'unexpected'} catch {$_.Exception.Message};@{restored=($env:OLLAMA_MODEL -eq 'prior-model');error=$message}|ConvertTo-Json"
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


def test_iac_process_forwards_stdout_and_stderr_before_exit():
    """IAC-012 forwards each native stream while the child is still running."""
    code = (
        "import sys,time;print('stdout-ready',flush=True);"
        "sys.stderr.write('stderr-ready\\n');sys.stderr.flush();time.sleep(0.35);print('stdout-done',flush=True)"
    )
    payload = json.dumps(code).replace("'", "''")
    executable = str(sys.executable).replace("'", "''")
    result = powershell(
        "$events=[Collections.Concurrent.ConcurrentQueue[string]]::new();$watch=[Diagnostics.Stopwatch]::StartNew();"
        "$code=ConvertFrom-Json '"
        + payload
        + "';$output=Invoke-IacProcess '"
        + executable
        + "' @('-I','-c',$code) -OnStdout {param($line)$events.Enqueue(('stdout:'+ $line + ':' + $watch.ElapsedMilliseconds))} -OnStderr {param($line)$events.Enqueue(('stderr:'+ $line + ':' + $watch.ElapsedMilliseconds))};"
        + "@{events=@($events);elapsed=$watch.ElapsedMilliseconds;output=$output}|ConvertTo-Json -Depth 5"
    )
    assert "stdout-ready" in result["output"]
    assert "stderr-ready" in result["output"]
    assert any(event.startswith("stdout:stdout-ready:") for event in result["events"])
    assert any(event.startswith("stderr:stderr-ready:") for event in result["events"])
    timings = {event.rsplit(":", 2)[1]: int(event.rsplit(":", 1)[1]) for event in result["events"]}
    assert timings["stdout-ready"] < timings["stdout-done"]
    assert timings["stderr-ready"] < timings["stdout-done"]


def test_iac_process_forward_output_preserves_stream_labels():
    """IAC-012 emits concise labeled console records for both native streams."""
    code = "import sys;print('visible-out');sys.stderr.write('visible-err\\n')"
    payload = json.dumps(code).replace("'", "''")
    executable = str(sys.executable).replace("'", "''")
    result = powershell(
        "$code=ConvertFrom-Json '"
        + payload
        + "';$records=@(Invoke-IacProcess '"
        + executable
        + "' @('-I','-c',$code) -ForwardOutput 6>&1);$text=@($records|ForEach-Object {$_.ToString()});$text|ConvertTo-Json"
    )
    assert "[AgentiX][stdout] visible-out" in result
    assert "[AgentiX][stderr] visible-err" in result


def test_iac_process_drains_concurrent_streams_without_failure():
    """IAC-012 drains concurrent stdout/stderr and accepts zero-exit stderr output."""
    code = (
        "import sys,threading;"
        "emit=lambda stream,prefix:[(stream.write(prefix+str(i)+'\\n'),stream.flush()) for i in range(200)];"
        "a=threading.Thread(target=emit,args=(sys.stdout,'out-'));b=threading.Thread(target=emit,args=(sys.stderr,'err-'));"
        "a.start();b.start();a.join();b.join()"
    )
    payload = json.dumps(code).replace("'", "''")
    executable = str(sys.executable).replace("'", "''")
    result = powershell(
        "$stdout=[Collections.Generic.List[string]]::new();$stderr=[Collections.Generic.List[string]]::new();$code=ConvertFrom-Json '"
        + payload
        + "';Invoke-IacProcess '"
        + executable
        + "' @('-I','-c',$code) -OnStdout {param($line)$stdout.Add($line)} -OnStderr {param($line)$stderr.Add($line)}|Out-Null;"
        + "@{stdout=$stdout.Count;stderr=$stderr.Count}|ConvertTo-Json"
    )
    assert result == {"stdout": 200, "stderr": 200}


def test_iac_process_preserves_failure_timeout_and_bounded_diagnostics():
    """IAC-012 retains exit failures, deadlines and bounded native diagnostics."""
    executable = str(sys.executable).replace("'", "''")
    result = powershell(
        "$failure=try {Invoke-IacProcess '"
        + executable
        + "' @('-I','-c','import sys;sys.stderr.write(\"fixture failure\");sys.exit(7)');'unexpected'}catch{$_.Exception.Message};"
        + "$timeout=try {Invoke-IacProcess '"
        + executable
        + "' @('-I','-c','import time;time.sleep(1)') -TimeoutMilliseconds 50;'unexpected'}catch{$_.Exception.Message};"
        + "$bounded=try {Invoke-IacProcess '"
        + executable
        + "' @('-I','-c','import sys;print(\"x\"*300000);sys.exit(1)');'unexpected'}catch{$_.Exception.Message};"
        + "@{failure=$failure;timeout=$timeout;boundedLength=$bounded.Length}|ConvertTo-Json"
    )
    assert "Process failed (7)" in result["failure"]
    assert "fixture failure" in result["failure"]
    assert "20-minute deadline" in result["timeout"]
    assert result["boundedLength"] <= 4200


def test_apply_summarizes_dsc_result_without_emitting_its_raw_json():
    """IAC-013 keeps DSC's machine JSON out of the interactive Apply transcript."""
    result = powershell(
        "& (Get-Module Agentix.Iac) {"
        "$script:stages=[Collections.Generic.List[string]]::new();"
        "function script:Get-IacState {@{dsc=@{version='3.3.0'}}};"
        "function script:Test-IacPlan {return $true};"
        "function script:Get-IacPaths {@{dsc='fixture-dsc.exe'}};"
        'function script:Invoke-IacProcess {return \'{"hadErrors":false,"results":[{"name":"fixture"}]}\' };'
        "function script:Test-IacDeployment {@{inDesiredState=$true;changes=@();blockers=@();warnings=@()}};"
        "function script:Write-IacStage {param($Message)$script:stages.Add($Message)}"
        "};$c=Read-IacConfiguration;$plan=@{changes=@();blockers=@()};$output=@(Invoke-IacApply $plan $c);"
        "$stages=& (Get-Module Agentix.Iac) {$script:stages};@{output=@($output);stages=@($stages)}|ConvertTo-Json -Depth 5"
    )
    assert result["output"] == []
    assert "DSC configuration completed successfully." in result["stages"]


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
        + "';$env:PIP_TARGET='outside-fixture';$env:PIP_FIND_LINKS='https://unapproved.invalid';$env:PIP_USER='1';& (Get-Module Agentix.Iac) {function script:Invoke-IacProcess {param($Executable,$Arguments)if ('install' -in $Arguments) {$script:observed=@{target=$env:PIP_TARGET;links=$env:PIP_FIND_LINKS;user=$env:PIP_USER;index=$env:PIP_INDEX_URL;hashes=('--require-hashes' -in $Arguments)}};return ''};function script:Install-IacPlaywrightChromium {return 'fixture'}};$c=Read-IacConfiguration;Set-IacResource 'environment' $c @{};$o=& (Get-Module Agentix.Iac) {$script:observed};@{observed=$o;restored=$env:PIP_TARGET}|ConvertTo-Json -Depth 5"
    )
    result = powershell(body)
    assert result["observed"]["target"] is None
    assert result["observed"]["links"] is None
    assert result["observed"]["user"] is None
    assert result["observed"]["index"] == "https://pypi.org/simple"
    assert result["observed"]["hashes"] is True
    assert result["restored"] == "outside-fixture"


def test_environment_install_downloads_only_missing_playwright_chromium(tmp_path):
    """IAC-011 installs Chromium after dependencies when the venv lacks its expected binary."""
    browser = tmp_path / "playwright" / "chromium" / "chrome.exe"
    body = (
        "$env:LOCALAPPDATA='"
        + str(tmp_path)
        + "';$global:browser='"
        + str(browser)
        + "';& (Get-Module Agentix.Iac) {"
        + "$script:calls=[Collections.Generic.List[string]]::new();function script:Invoke-IacProcess {param($Executable,$Arguments)"
        + "$script:calls.Add(($Arguments -join ' '));if ('playwright' -in $Arguments) {[IO.Directory]::CreateDirectory((Split-Path $global:browser -Parent))|Out-Null;[IO.File]::WriteAllText($global:browser,'fixture')};if ('-c' -in $Arguments) {return $global:browser};return ''}};"
        + "$c=Read-IacConfiguration;Set-IacResource 'environment' $c @{};$calls=& (Get-Module Agentix.Iac) {$script:calls};@{calls=@($calls)}|ConvertTo-Json -Depth 5"
    )
    result = powershell(body)
    assert any("pip install" in call for call in result["calls"])
    assert result["calls"].count("-I -m playwright install chromium") == 1


def test_environment_install_skips_existing_compatible_playwright_chromium(tmp_path):
    """IAC-011 leaves the matching Playwright Chromium binary untouched."""
    browser = tmp_path / "playwright" / "chromium" / "chrome.exe"
    browser.parent.mkdir(parents=True)
    browser.write_text("fixture", encoding="utf-8")
    body = (
        "$env:LOCALAPPDATA='"
        + str(tmp_path)
        + "';$global:browser='"
        + str(browser)
        + "';& (Get-Module Agentix.Iac) {"
        + "$script:calls=[Collections.Generic.List[string]]::new();function script:Invoke-IacProcess {param($Executable,$Arguments)"
        + "$script:calls.Add(($Arguments -join ' '));if ('-c' -in $Arguments) {return $global:browser};return ''}};"
        + "$c=Read-IacConfiguration;Set-IacResource 'environment' $c @{};$calls=& (Get-Module Agentix.Iac) {$script:calls};@{calls=@($calls)}|ConvertTo-Json -Depth 5"
    )
    result = powershell(body)
    assert "-I -m playwright install chromium" not in result["calls"]


def test_environment_install_reports_playwright_chromium_failure(tmp_path):
    """IAC-011 fails with a Chromium-specific diagnostic when Playwright cannot install it."""
    browser = tmp_path / "playwright" / "chromium" / "chrome.exe"
    body = (
        "$env:LOCALAPPDATA='"
        + str(tmp_path)
        + "';$global:browser='"
        + str(browser)
        + "';& (Get-Module Agentix.Iac) {function script:Invoke-IacProcess {param($Executable,$Arguments)"
        + "if ('playwright' -in $Arguments) {throw 'fixture download failure'};if ('-c' -in $Arguments) {return $global:browser};return ''}};"
        + "$c=Read-IacConfiguration;$r=try {Set-IacResource 'environment' $c @{};'unexpected'}catch{$_.Exception.Message};$r|ConvertTo-Json"
    )
    result = powershell(body)
    assert "Playwright Chromium installation failed" in result
    assert "fixture download failure" in result


def test_launcher_uses_venv_playwright_chromium_path(tmp_path):
    """IAC-011 exports the installed venv Playwright Chromium path to the launcher."""
    browser = tmp_path / "playwright" / "chromium" / "chrome.exe"
    browser.parent.mkdir(parents=True)
    browser.write_text("fixture", encoding="utf-8")
    result = powershell(
        "$env:LOCALAPPDATA='"
        + str(tmp_path)
        + "';$global:browser='"
        + str(browser)
        + "';& (Get-Module Agentix.Iac) {function script:Test-IacLaunch {@{inDesiredState=$true;warnings=@()}};function script:Get-IacState {@{portFree=$true}};function script:Invoke-IacProcess {param($Executable,$Arguments)if ('-c' -in $Arguments) {return $global:browser};return ''}};"
        + "$global:seen='';Start-IacApplication -Config (Read-IacConfiguration) -Mode Cli -Run {param($exe,$entry)$global:seen=$env:AGENTIX_PLAYWRIGHT_EXECUTABLE};$global:seen|ConvertTo-Json"
    )
    assert result == str(browser)


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
        + "';Remove-Item Env:AGENTIX_SERVER_PORT -ErrorAction SilentlyContinue;& (Get-Module Agentix.Iac) {function script:Test-IacLaunch {@{inDesiredState=$true;warnings=@()}};function script:Get-IacState {@{portFree=$true}};function script:Get-IacPlaywrightChromiumPath {return $null}};Start-IacApplication -Config (Read-IacConfiguration) -Mode Cli -Run {};Test-Path Env:AGENTIX_SERVER_PORT|ConvertTo-Json"
    )
    assert result is False


def test_location_receipt_binds_the_configured_deployment_root(tmp_path):
    """IAC-010: receipts preserve only the reviewed schema-2 runtime root."""
    result = powershell(
        "$c=Read-IacConfiguration;$physical=Join-Path $env:LOCALAPPDATA 'agentix-data\\v7';$c.home=$physical;$c.toolsRoot=Join-Path $env:LOCALAPPDATA 'checkout\\generated_tools';Assert-IacConfiguration $c;New-Item -ItemType Directory -Path $physical -Force|Out-Null;$fixture=Join-Path $env:LOCALAPPDATA 'infra';New-Item -ItemType Directory -Path $fixture|Out-Null;Copy-Item '"
        + str(ROOT / "infra/runtime.lock.txt")
        + "' (Join-Path $fixture 'runtime.lock.txt');& (Get-Module Agentix.Iac) {param($directory)$script:InfraRoot=$directory} $fixture;Save-IacLocation -Config $c -Root $physical;$actual=Get-IacPaths $c;@{actual=$actual.root;expected=$physical}|ConvertTo-Json"
    )
    assert result["actual"] == result["expected"]


def test_iac_launch_ignores_external_ollama_state():
    """Managed launch is independent of a reachable server and never provisions it."""
    result = powershell(
        "$c=Read-IacConfiguration;$s=New-IacFixtureState $c;$s.model.server=$false;"
        "& (Get-Module Agentix.Iac) {param($state)$script:fixture=$state;function script:Get-IacState {return $script:fixture};function script:Get-IacPlaywrightChromiumPath {return $null}} $s;"
        "$calls=[Collections.Generic.List[string]]::new();Start-IacApplication -Config $c -Mode Cli -Run {param($exe,$entry)$calls.Add($entry)};"
        "@{calls=$calls.Count}|ConvertTo-Json"
    )
    assert result == {"calls": 1}


def test_iac_configuration_rejects_removed_ollama_fields():
    """Ollama versions and model pins cannot return through installer configuration."""
    result = powershell(
        "$c=Read-IacConfiguration;$c.ollamaVersion='0.40.14';$r=try{Assert-IacConfiguration $c;$false}catch{$true};$r|ConvertTo-Json"
    )
    assert result is True
