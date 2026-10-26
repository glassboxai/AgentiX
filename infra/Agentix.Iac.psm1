<#
.SYNOPSIS
Per-user desired-state planning and bounded convergence for AgentiX.
.DESCRIPTION
All paths and commands come from reviewed, versioned infrastructure definitions.
Plan/Test are read-only. Apply refuses drift, elevation and linked managed paths.
No generated artifact directory is enumerated, adopted or removed.
#>
Set-StrictMode -Version Latest
$ErrorActionPreference = 'Stop'
# DSC must not depend on ambient module auto-loading or a caller's module path.
if ($PSVersionTable.PSEdition -eq 'Desktop') {
    Import-Module ([IO.Path]::Combine($PSHOME, 'Modules\Microsoft.PowerShell.Management\Microsoft.PowerShell.Management.psd1')) -Global -ErrorAction Stop
    Import-Module (Join-Path $PSHOME 'Modules\Microsoft.PowerShell.Utility\Microsoft.PowerShell.Utility.psd1') -Global -ErrorAction Stop
    Import-Module (Join-Path $PSHOME 'Modules\Microsoft.PowerShell.Archive\Microsoft.PowerShell.Archive.psd1') -Global -ErrorAction Stop
    Import-Module (Join-Path $PSHOME 'Modules\Microsoft.PowerShell.Security\Microsoft.PowerShell.Security.psd1') -Global -ErrorAction Stop
}

$script:InfraRoot = $PSScriptRoot
$script:ProjectRoot = Split-Path $PSScriptRoot -Parent
$script:ResourceOrder = @('python','ollama','dsc','environment','launchers','location','model')

function ConvertTo-IacMap {
    <#
.SYNOPSIS
Recursively normalize JSON into ordered maps for stable fingerprints.
#>
    param($Value)
    if ($null -eq $Value) { return $null }
    # Cmdlet results may wrap primitive values in PSObject with no properties.
    if ($Value -is [string] -or $Value.GetType().IsValueType) { return $Value }
    if ($Value -is [Collections.IDictionary]) {
        $map = [ordered]@{}
        [string[]]$keys=@($Value.Keys)
        [Array]::Sort($keys,[StringComparer]::Ordinal)
        foreach ($key in $keys) { $map[$key] = ConvertTo-IacMap $Value[$key] }
        return $map
    }
    if ($Value -is [pscustomobject]) {
        $map = [ordered]@{}
        [string[]]$keys=@($Value.PSObject.Properties.Name)
        [Array]::Sort($keys,[StringComparer]::Ordinal)
        foreach ($key in $keys) { $map[$key] = ConvertTo-IacMap $Value.$key }
        return $map
    }
    if ($Value -is [Collections.IEnumerable] -and $Value -isnot [string]) {
        return ,@($Value | ForEach-Object { ConvertTo-IacMap $_ })
    }
    return $Value
}

function Get-IacDigest {
    <#
.SYNOPSIS
SHA-256 of canonical JSON; does not publish input values.
#>
    param($Value)
    $text = ConvertTo-Json -InputObject (ConvertTo-IacMap $Value) -Depth 60 -Compress
    $algorithm = [Security.Cryptography.SHA256]::Create()
    try { return ([BitConverter]::ToString($algorithm.ComputeHash([Text.Encoding]::UTF8.GetBytes($text)))).Replace('-','').ToLowerInvariant() }
    finally { $algorithm.Dispose() }
}

function Assert-IacContained {
    <#
.SYNOPSIS
Enforce component containment and reject existing reparse-point ancestors.
#>
    param([string]$Path,[string]$Root)
    $full = [IO.Path]::GetFullPath($Path).TrimEnd('\')
    $boundary = [IO.Path]::GetFullPath($Root).TrimEnd('\')
    if ($full -ne $boundary -and -not $full.StartsWith($boundary+'\',[StringComparison]::OrdinalIgnoreCase)) { throw 'Managed path escapes its root.' }
    $cursor = $full
    while ($cursor) {
        if (Test-Path -LiteralPath $cursor) {
            if ((Get-Item -LiteralPath $cursor -Force).Attributes -band [IO.FileAttributes]::ReparsePoint) { throw 'Managed paths cannot contain reparse points.' }
        }
        $parent = Split-Path $cursor -Parent
        if ($parent -eq $cursor) { break }
        $cursor = $parent
    }
}

function Assert-IacConfiguration {
    <#
.SYNOPSIS
Reject unknown fields, unsupported versions and unsafe deployment inputs.
#>
    param($Config)
    $expected = @('schema','pythonVersion','ollamaVersion','dscVersion','model','modelDigest','port','openBrowser','ollamaUrl')
    if (@(Compare-Object @($Config.Keys | Sort-Object) @($expected | Sort-Object)).Count) { throw 'Unknown or missing infrastructure configuration field.' }
    if ($Config.schema -ne 1 -or $Config.pythonVersion -ne '3.11.9' -or $Config.ollamaVersion -ne '0.40.6' -or $Config.dscVersion -ne '3.3.0') { throw 'Unsupported pinned prerequisite version.' }
    if ($Config.model -ne 'ollama/qwen3-coder:30b' -or $Config.modelDigest -notmatch '^[a-f0-9]{64}$') { throw 'Only the reviewed local model and digest are allowed.' }
    if (($Config.port -isnot [int] -and $Config.port -isnot [long]) -or $Config.port -lt 1024 -or $Config.port -gt 65535) { throw 'Port must be an unprivileged integer TCP port.' }
    if ($Config.openBrowser -isnot [bool] -or $Config.ollamaUrl -ne 'http://127.0.0.1:11434') { throw 'Only the reviewed loopback Ollama endpoint is allowed.' }
}

function Read-IacConfiguration {
    <#
.SYNOPSIS
Load the fixed reviewed profile; never accepts executable configuration.
#>
    $config = ConvertTo-IacMap (Get-Content -LiteralPath (Join-Path $script:InfraRoot 'windows.local.json') -Raw | ConvertFrom-Json)
    Assert-IacConfiguration $config
    return $config
}

function Assert-IacSignature {
    <#
.SYNOPSIS
Require a valid Authenticode signature from the reviewed prerequisite publisher.
.DESCRIPTION
The injected checker is a trusted test boundary. Production uses the Windows
signature verifier; an unsigned, altered or untrusted binary fails closed.
#>
    param([string]$Path,[ValidateSet('python','ollama','dsc')][string]$Kind,[scriptblock]$Check={param($File) Get-AuthenticodeSignature -LiteralPath $File})
    $publishers=@{python='Python Software Foundation';ollama='Ollama Inc.';dsc='Microsoft Corporation'}
    $signature=& $Check $Path
    $pattern=[regex]::Escape('CN='+$publishers[$Kind])+'(?:,|$)'
    if ([string]$signature.Status -ne 'Valid' -or -not $signature.SignerCertificate -or $signature.SignerCertificate.Subject -notmatch $pattern) {
        throw ('Binary signature verification failed for '+$Kind+'.')
    }
}

function Resolve-IacRoot {
    <#
.SYNOPSIS
Resolve Windows packaged-host folder aliases to a persistent physical managed path.
.DESCRIPTION
Uses the explicitly selected trusted Python runtime only for os.path.realpath.
No directories are created. Reparse-point containment is checked separately.
#>
    param([string]$Root,[string]$Python)
    if (-not (Test-Path -LiteralPath $Root)) { return $Root }
    return (Invoke-IacProcess $Python @('-I','-c','import os,sys; print(os.path.realpath(sys.argv[1]))',$Root)).Trim()
}

function Get-IacLocationFile {
    <#
.SYNOPSIS
Return the current user's local, untracked deployment-location receipt path.
#>
    $owner=[Security.Principal.WindowsIdentity]::GetCurrent().User.Value
    $homeIdentity=(Get-IacDigest $env:LOCALAPPDATA.ToLowerInvariant()).Substring(0,16)
    return Join-Path $script:InfraRoot ('.local-paths.'+$owner+'.'+$homeIdentity+'.json')
}

function Read-IacLocation {
    <#
.SYNOPSIS
Validate owner-scoped physical-location metadata without traversing runtime data.
.DESCRIPTION
The receipt is not an approval capability. It records only a user SID and an owned
root inside LOCALAPPDATA, with the fixed AgentiX/v3 suffix and no reparse ancestors.
#>
    $file=Get-IacLocationFile
    if (-not (Test-Path -LiteralPath $file)) { return $null }
    Assert-IacContained $file $script:InfraRoot
    $record=ConvertTo-IacMap ([IO.File]::ReadAllText($file)|ConvertFrom-Json)
    $owner=[Security.Principal.WindowsIdentity]::GetCurrent().User.Value
    if (@(Compare-Object @($record.Keys|Sort-Object) @('owner','root','schema')).Count -or $record.schema -ne 1 -or $record.owner -ne $owner) { throw 'Invalid deployment location receipt.' }
    Assert-IacContained $record.root $env:LOCALAPPDATA
    if (-not $record.root.EndsWith('\AgentiX\v3',[StringComparison]::OrdinalIgnoreCase)) { throw 'Invalid deployment root suffix.' }
    return $record.root
}

function Save-IacLocation {
    <#
.SYNOPSIS
Persist the reviewed physical root for manual launches outside the provisioning host.
.DESCRIPTION
Only owner-scoped metadata is written. The fixed receipt path cannot be redirected
through a reparse point. Identical contents are preserved rather than rewritten.
#>
    param([string]$Root)
    Assert-IacContained $Root $env:LOCALAPPDATA
    if (-not $Root.EndsWith('\AgentiX\v3',[StringComparison]::OrdinalIgnoreCase)) { throw 'Invalid deployment root suffix.' }
    $file=Get-IacLocationFile;Assert-IacContained $file $script:InfraRoot
    $record=[ordered]@{schema=1;owner=[Security.Principal.WindowsIdentity]::GetCurrent().User.Value;root=$Root}
    $content=ConvertTo-Json $record -Compress
    if (-not (Test-Path -LiteralPath $file) -or [IO.File]::ReadAllText($file) -cne $content) { [IO.File]::WriteAllText($file,$content,[Text.UTF8Encoding]::new($false)) }
}

function Get-IacPaths {
    <#
.SYNOPSIS
Derive owned paths without creating them or reading tool storage.
#>
    param($Config)
    $root=Read-IacLocation
    if (-not $root) { $root = Join-Path $env:LOCALAPPDATA 'AgentiX\v3' }
    Assert-IacContained $root $env:LOCALAPPDATA
    $basePython=Join-Path $env:LOCALAPPDATA 'Programs\Python\Python311\python.exe'
    if (Test-Path -LiteralPath $basePython) { Assert-IacSignature $basePython 'python'; $root=Resolve-IacRoot -Root $root -Python $basePython }
    Assert-IacContained $root $env:LOCALAPPDATA
    $lock = (Get-FileHash -LiteralPath (Join-Path $script:InfraRoot 'runtime.lock.txt') -Algorithm SHA256).Hash.ToLowerInvariant()
    $environment = Join-Path $root ('environments\'+$lock.Substring(0,16))
    return @{root=$root; lock=$lock; environment=$environment; python=(Join-Path $env:LOCALAPPDATA 'Programs\Python\Python311\python.exe'); ollama=(Join-Path $env:LOCALAPPDATA 'Programs\Ollama\ollama.exe'); privateOllama=(Join-Path $root ('tooling\ollama\'+$Config.ollamaVersion+'\ollama.exe')); dsc=(Join-Path $root ('tooling\dsc\'+$Config.dscVersion+'\dsc.exe')); tools=(Join-Path $root 'data\tools'); launchers=(Join-Path $root 'launchers')}
}

function Invoke-IacProcess {
    <#
.SYNOPSIS
Run an explicit native argument vector, distinguishing stderr warnings from exit failures.
.DESCRIPTION
Uses CreateProcess without a shell. CRT quoting preserves spaces, quotes and trailing
backslashes on both PowerShell editions. Output returned to callers is bounded;
failures include only its final 4096 characters. Installers are not transactional.
#>
    param([string]$Executable,[string[]]$Arguments)
    $quoted=@()
    foreach ($argument in $Arguments) {
        $escaped=[regex]::Replace($argument,'(\\*)"','$1$1\"')
        $escaped=[regex]::Replace($escaped,'(\\+)$','$1$1')
        $quoted+='"'+$escaped+'"'
    }
    $info=[Diagnostics.ProcessStartInfo]::new()
    $info.FileName=$Executable;$info.Arguments=$quoted -join ' '
    $info.UseShellExecute=$false;$info.CreateNoWindow=$true
    $info.RedirectStandardOutput=$true;$info.RedirectStandardError=$true
    $process=[Diagnostics.Process]::new();$process.StartInfo=$info
    try {
        if (-not $process.Start()) { throw 'Unable to start the prerequisite process.' }
        $stdout=$process.StandardOutput.ReadToEndAsync();$stderr=$process.StandardError.ReadToEndAsync()
        if (-not $process.WaitForExit(1200000)) { $process.Kill();throw 'Prerequisite process exceeded its 20-minute deadline; inspect partial installation before retrying.' }
        $output=$stdout.GetAwaiter().GetResult();$errorText=$stderr.GetAwaiter().GetResult()
        if ($errorText) { $output+="`n"+$errorText }
        if ($output.Length -gt 262144) { $output=$output.Substring($output.Length-262144) }
        if ($process.ExitCode -ne 0) {
            $tail=$output;if ($tail.Length -gt 4096) {$tail=$tail.Substring($tail.Length-4096)}
            throw ('Process failed ('+$process.ExitCode+'): '+$tail)
        }
        return $output.Trim()
    } finally { $process.Dispose() }
}

function Get-IacExecutableState {
    <#
.SYNOPSIS
Read an installed binary identity, retaining hashes for reviewed-plan drift checks.
#>
    param([string]$Path,[string]$Kind)
    if (-not (Test-Path -LiteralPath $Path -PathType Leaf)) { return @{version='missing';path=$Path;hash=''} }
    Assert-IacSignature $Path $Kind
    $version = 'incompatible'
    if ($Kind -eq 'python') { $version = (Invoke-IacProcess $Path @('-I','-c','import platform; print(platform.python_version() if platform.machine().upper()=="AMD64" else "incompatible-architecture")')).Trim() }
    elseif ($Kind -eq 'dsc') { $version = (Invoke-IacProcess $Path @('--version')).Trim().Replace('dsc ','').TrimStart('v') }
    else {
        $version = (Get-Item -LiteralPath $Path).VersionInfo.ProductVersion
        if (-not $version) {
            $text = Invoke-IacProcess $Path @('--version')
            if ($text -match '(\d+\.\d+\.\d+)') { $version=$Matches[1] }
        }
        if ($version -match '(\d+\.\d+\.\d+)') { $version=$Matches[1] }
    }
    return @{version=$version;path=$Path;hash=(Get-FileHash -LiteralPath $Path -Algorithm SHA256).Hash.ToLowerInvariant()}
}

function Get-IacLaunchContent {
    <#
.SYNOPSIS
Generate deterministic launchers with quoted literal paths and manual startup only.
#>
    param($Config,$Paths)
    $entry = (Join-Path $script:InfraRoot 'Invoke-AgentiXIac.ps1').Replace("'","''")
    return @{
        'Start-Gui.ps1'="<#
.SYNOPSIS
Manually launch the managed loopback GUI after prerequisite validation.
#>`n& '$entry' -Action LaunchGui`nexit `$LASTEXITCODE`n";
        'Start-Cli.ps1'="<#
.SYNOPSIS
Manually launch managed interactive terminal review.
#>`n& '$entry' -Action LaunchCli`nexit `$LASTEXITCODE`n"
    }
}

function Get-IacEnvironmentState {
    <#
.SYNOPSIS
Compare actual managed package versions and ownership; receipts alone cannot prove state.
#>
    param($Config,$Paths)
    $exe = Join-Path $Paths.environment 'Scripts\python.exe'
    $owner = Join-Path $Paths.environment '.agentix-owned'
    $present = $false; $packages = ''; $owned = Test-Path -LiteralPath $owner -PathType Leaf
    if ((Test-Path -LiteralPath $exe) -and $owned) {
        try {
            $identity = Invoke-IacProcess $exe @('-I','-c','import sys,platform,json; print(json.dumps([platform.python_version(),sys.prefix,sys.base_prefix]))') | ConvertFrom-Json
            $actual = Invoke-IacProcess $exe @('-I','-m','pip','list','--format=json','--disable-pip-version-check') | ConvertFrom-Json
            $versions = @{}
            foreach ($package in $actual) { $versions[$package.name.ToLowerInvariant().Replace('_','-').Replace('.','-')]=$package.version }
            $required = @{}; $present = ($identity[0] -eq $Config.pythonVersion -and $identity[1] -eq $Paths.environment -and $identity[2] -ne $identity[1])
            foreach ($line in Get-Content -LiteralPath (Join-Path $script:InfraRoot 'runtime.lock.txt')) {
                if ($line -match '^([A-Za-z0-9_.-]+)==([^ ]+) ') {
                    $name=$Matches[1].ToLowerInvariant().Replace('_','-').Replace('.','-');$version=$Matches[2]
                    $required[$name] = $versions[$name]
                    if ($versions[$name] -ne $version) { $present=$false }
                }
            }
            $packages=Get-IacDigest $required
        } catch { $present=$false; $packages='incomplete' }
    }
    return @{present=$present;owned=$owned;packages=$packages;lock=$Paths.lock}
}

function Get-IacPackageManager {
    <#
.SYNOPSIS
Observe WinGet before planning a missing Python installation, freezing its exact identity.
.DESCRIPTION
Does not install packages or refresh sources. Missing or unsupported Windows App
Installer is a platform prerequisite requiring an explicit operator repair.
#>
    $command=Get-Command winget.exe -ErrorAction SilentlyContinue
    if (-not $command) { return @{available=$false;version='missing';path=''} }
    $version=(Invoke-IacProcess $command.Source @('--version')).Trim().TrimStart('v')
    $supported=($version -match '^\d+\.\d+\.\d+$' -and [version]$version -ge [version]'1.6.2631')
    return @{available=$supported;version=$version;path=$command.Source}
}

function Get-IacState {
    <#
.SYNOPSIS
Read prerequisites and owned state without downloads, writes or model execution.
#>
    param($Config)
    $paths=Get-IacPaths $Config
    foreach ($target in @($paths.environment,$paths.dsc,$paths.privateOllama,$paths.launchers)) { Assert-IacContained $target $paths.root }
    $python=Get-IacExecutableState $paths.python 'python'
    $manager=@{available=$true;version='not_required';path=''}
    if ($python.version -eq 'missing') { $manager=Get-IacPackageManager }
    $ollamaPath=$paths.ollama
    if (-not (Test-Path -LiteralPath $ollamaPath)) { $ollamaPath=$paths.privateOllama }
    $ollama=Get-IacExecutableState $ollamaPath 'ollama'
    $dsc=Get-IacExecutableState $paths.dsc 'dsc'
    $launchers=$true
    foreach ($item in (Get-IacLaunchContent $Config $paths).GetEnumerator()) {
        $target=Join-Path $paths.launchers $item.Key
        if (-not (Test-Path -LiteralPath $target) -or [IO.File]::ReadAllText($target) -cne $item.Value) { $launchers=$false }
    }
    $model=@{present=$false;server=$false;digest='';version=''}
    try {
        $version=Invoke-RestMethod ($Config.ollamaUrl+'/api/version') -TimeoutSec 5
        $model.server=$true;$model.version=$version.version
        $tags=Invoke-RestMethod ($Config.ollamaUrl+'/api/tags') -TimeoutSec 5
        foreach ($tag in $tags.models) {
            if ($tag.name -eq 'qwen3-coder:30b') { $model.digest=$tag.digest;$model.present=($tag.digest -eq $Config.modelDigest) }
        }
    } catch { $model.server=$false }
    $busy=@([Net.NetworkInformation.IPGlobalProperties]::GetIPGlobalProperties().GetActiveTcpListeners() | Where-Object { $_.Port -eq $Config.port }).Count -gt 0
    return @{location=@{present=[bool](Read-IacLocation)};packageManager=$manager;python=$python;ollama=$ollama;dsc=$dsc;environment=(Get-IacEnvironmentState $Config $paths);launchers=@{present=$launchers};model=$model;portFree=(-not $busy)}
}

function Get-IacSourceDigest {
    <#
.SYNOPSIS
Fingerprint only named infrastructure and maintained application source, never artifact storage.
#>
    $hashes=@{}
    foreach ($name in @('Agentix.Iac.psm1','Invoke-AgentiXIac.ps1','resource.ps1','AgentiX.dsc.resource.json','configuration.dsc.json','windows.local.json','runtime.lock.txt')) {
        $hashes[$name]=(Get-FileHash -LiteralPath (Join-Path $script:InfraRoot $name) -Algorithm SHA256).Hash
    }
    foreach ($file in Get-ChildItem -LiteralPath (Join-Path $script:ProjectRoot 'src') -Filter '*.py' -File -Recurse) {
        if ($file.Attributes -band [IO.FileAttributes]::ReparsePoint) { throw 'Linked application source is not supported.' }
        $hashes[$file.FullName.Substring($script:ProjectRoot.Length)] = (Get-FileHash -LiteralPath $file.FullName -Algorithm SHA256).Hash
    }
    foreach ($name in @('app.py','main.py','_agentix_path.py')) { $hashes[$name]=(Get-FileHash -LiteralPath (Join-Path $script:ProjectRoot $name) -Algorithm SHA256).Hash }
    return Get-IacDigest $hashes
}

function Get-IacPlan {
    <#
.SYNOPSIS
Produce a deterministic, reviewable plan from explicit observation and desired configuration.
#>
    param($Config,$State,[switch]$DownloadModel)
    Assert-IacConfiguration $Config
    $changes=@();$blockers=@();$warnings=@()
    if ($State.python.version -eq 'missing' -and -not $State.packageManager.available) { $blockers+='Windows App Installer / WinGet 1.6.2631 or newer is required; install or repair this OS component per user before replanning.' }
    foreach ($name in @('python','ollama','dsc')) {
        if ($State[$name].version -ne $Config[$name+'Version']) {
            if ($State[$name].version -ne 'missing') { $blockers+=('Existing '+$name+' has an incompatible version; no automatic upgrade/adoption.') }
            else { $changes+=$name }
        }
    }
    foreach ($name in @('environment','launchers','location')) { if (-not $State[$name].present) { $changes+=$name } }
    if (-not $State.model.present) {
        if ($State.model.digest) { $blockers+='The installed model digest differs from the reviewed pin.' }
        elseif ($DownloadModel) { $changes+='model' }
        elseif ($State.model.server) { $blockers+='Required model missing: create a new plan with -DownloadModel to authorize its download.' }
        else { $warnings+='Ollama is offline. Provisioning may prepare files, but model validation needs a manually started loopback server.' }
    }
    if (-not $State.portFree) { $blockers+='Configured GUI port is occupied; no process will be stopped.' }
    if ($State.model.server -and $State.model.version -ne $Config.ollamaVersion) { $blockers+='Running Ollama server version differs from the pin; it will not be restarted.' }
    $plan=[ordered]@{schema=1;project=$script:ProjectRoot;config=(Get-IacDigest $Config);source=(Get-IacSourceDigest);state=$State;changes=@($changes);blockers=@($blockers);warnings=@($warnings);downloadModel=[bool]$DownloadModel}
    $plan['digest']=Get-IacDigest $plan
    return $plan
}

function Test-IacPlan {
    <#
.SYNOPSIS
Reject stale configuration, observations, source or modified planned actions.
#>
    param($Plan,$Config,$State)
    $fresh=Get-IacPlan -Config $Config -State $State -DownloadModel:([bool]$Plan.downloadModel)
    return ((Get-IacDigest $Plan) -eq (Get-IacDigest $fresh))
}

function Write-IacEvent {
    <#
.SYNOPSIS
Append bounded resource diagnostics without commands, prompts, artifacts or secrets.
#>
    param($Config,[string]$Resource,[string]$Outcome,[double]$Duration)
    $paths=Get-IacPaths $Config;$directory=Join-Path $paths.root 'logs'
    Assert-IacContained $directory $paths.root
    [IO.Directory]::CreateDirectory($directory) | Out-Null
    $log=Join-Path $directory 'infrastructure.jsonl'
    Assert-IacContained $log $paths.root
    foreach ($suffix in 1..4) { Assert-IacContained ($log+'.'+$suffix) $paths.root }
    if ((Test-Path -LiteralPath $log) -and (Get-Item -LiteralPath $log).Length -gt 1048576) {
        for ($i=3;$i -ge 1;$i--) { $old=$log+'.'+$i; if (Test-Path -LiteralPath $old) { Move-Item -LiteralPath $old -Destination ($log+'.'+($i+1)) -Force } }
        Move-Item -LiteralPath $log -Destination ($log+'.1') -Force
    }
    $event=@{utc=[DateTime]::UtcNow.ToString('o');operation=$env:AGENTIX_IAC_OPERATION;resource=$Resource;outcome=$Outcome;durationSeconds=[math]::Round($Duration,3)}
    [IO.File]::AppendAllText($log,((ConvertTo-Json $event -Compress)+"`n"),[Text.UTF8Encoding]::new($false))
}

function Get-IacArchive {
    <#
.SYNOPSIS
Fetch a pinned official archive and verify SHA-256 before extraction.
#>
    param($Config,[string]$Kind)
    $paths=Get-IacPaths $Config
    $archives=@{
        dsc=@{url='https://github.com/PowerShell/DSC/releases/download/v3.3.0/DSC-3.3.0-x86_64-pc-windows-msvc.zip';hash='3f8b27f648661903d066cc19d5a6e7a8c13bd07eb738d4d765ce7239619b8b5f'};
        ollama=@{url='https://github.com/ollama/ollama/releases/download/v0.40.6/ollama-windows-amd64.zip';hash='e359637575302f288d76c0007c408a4be9c7376d59c4f28684d63b232a44b427'}
    }
    $pin=$archives[$Kind];$cache=Join-Path $paths.root 'downloads';Assert-IacContained $cache $paths.root
    [IO.Directory]::CreateDirectory($cache)|Out-Null
    $archive=Join-Path $cache ($Kind+'-'+$pin.hash+'.zip')
    Assert-IacContained $archive $paths.root
    if (-not (Test-Path -LiteralPath $archive)) { Invoke-WebRequest -Uri $pin.url -OutFile $archive -UseBasicParsing -MaximumRedirection 5 }
    if ((Get-FileHash -LiteralPath $archive -Algorithm SHA256).Hash.ToLowerInvariant() -ne $pin.hash) { throw 'Downloaded archive integrity check failed; remove the corrupt owned cache file before retrying.' }
    return $archive
}

function Set-IacResource {
    <#
.SYNOPSIS
Converge one reviewed resource; no elevation, deletion, startup or host fallback.
#>
    param([string]$Resource,$Config,$Plan)
    $paths=Get-IacPaths $Config
    switch ($Resource) {
        'python' {
            Invoke-IacProcess $Plan.state.packageManager.path @('install','--id','Python.Python.3.11','--version','3.11.9','--exact','--source','winget','--architecture','x64','--scope','user','--silent','--disable-interactivity','--accept-source-agreements','--accept-package-agreements','--override','/quiet InstallAllUsers=0 PrependPath=0 Include_launcher=0 Include_test=0 AssociateFiles=0 Shortcuts=0') | Out-Null
        }
        { $_ -in @('dsc','ollama') } {
            $archive=Get-IacArchive $Config $Resource
            $binary=$paths.dsc;if ($Resource -eq 'ollama') {$binary=$paths.privateOllama}
            $directory=Split-Path $binary -Parent;Assert-IacContained $directory $paths.root
            [IO.Directory]::CreateDirectory($directory)|Out-Null
            # Validate every member before Expand-Archive can follow a crafted path.
            Add-Type -AssemblyName System.IO.Compression.FileSystem
            $zip=[IO.Compression.ZipFile]::OpenRead($archive)
            try { foreach ($member in $zip.Entries) { Assert-IacContained (Join-Path $directory $member.FullName) $directory } }
            finally { $zip.Dispose() }
            Expand-Archive -LiteralPath $archive -DestinationPath $directory -Force
            Assert-IacSignature $binary $Resource
        }
        'environment' {
            Assert-IacContained $paths.environment $paths.root
            $owner=Join-Path $paths.environment '.agentix-owned'
            Assert-IacContained $owner $paths.root
            if ((Test-Path -LiteralPath $paths.environment) -and -not (Test-Path -LiteralPath $owner)) { throw 'Refusing to adopt an existing unowned environment directory.' }
            [IO.Directory]::CreateDirectory($paths.environment)|Out-Null
            [IO.File]::WriteAllText($owner,$paths.lock)
            Invoke-IacProcess $paths.python @('-I','-m','venv',$paths.environment) | Out-Null
            $python=Join-Path $paths.environment 'Scripts\python.exe'
            # Ignore user package indexes and Python injection while installing the hash lock.
            $saved=@{}
            foreach ($item in Get-ChildItem Env:PIP_*) { $saved[$item.Name]=$item.Value }
            try {
                # PIP_TARGET/PREFIX/USER could otherwise write outside this owned venv.
                foreach ($item in Get-ChildItem Env:PIP_*) { Remove-Item -LiteralPath ('Env:'+$item.Name) -ErrorAction SilentlyContinue }
                $env:PIP_CONFIG_FILE='NUL';$env:PIP_INDEX_URL='https://pypi.org/simple'
                Invoke-IacProcess $python @('-I','-m','pip','install','--no-input','--disable-pip-version-check','--require-hashes','--only-binary=:all:','-r',(Join-Path $script:InfraRoot 'runtime.lock.txt'))|Out-Null
                Invoke-IacProcess $python @('-I','-m','pip','check')|Out-Null
            } finally {
                foreach ($item in Get-ChildItem Env:PIP_*) { Remove-Item -LiteralPath ('Env:'+$item.Name) -ErrorAction SilentlyContinue }
                foreach ($name in $saved.Keys) { if ($null -eq $saved[$name]) { Remove-Item -LiteralPath ('Env:'+$name) -ErrorAction SilentlyContinue } else { [Environment]::SetEnvironmentVariable($name,$saved[$name],'Process') } }
            }
        }
        'launchers' {
            Assert-IacContained $paths.launchers $paths.root;[IO.Directory]::CreateDirectory($paths.launchers)|Out-Null
            foreach ($item in (Get-IacLaunchContent $Config $paths).GetEnumerator()) { $target=Join-Path $paths.launchers $item.Key;Assert-IacContained $target $paths.root;[IO.File]::WriteAllText($target,$item.Value,[Text.UTF8Encoding]::new($false)) }
        }
        'location' { Save-IacLocation -Root $paths.root }
        'model' {
            if (-not $Plan.downloadModel) { throw 'Model download was not explicitly included in the reviewed plan.' }
            $state=Get-IacState $Config
            if (-not $state.model.server) { throw 'Start the pinned local Ollama server manually before downloading a model.' }
            Invoke-RestMethod -Method Post -Uri ($Config.ollamaUrl+'/api/pull') -ContentType 'application/json' -Body '{"model":"qwen3-coder:30b","stream":false}' -TimeoutSec 3600 | Out-Null
        }
        default { throw 'Unknown infrastructure resource.' }
    }
}

function Invoke-IacConverge {
    <#
.SYNOPSIS
Validate review then converge in dependency order; stop immediately on failure.
#>
    param($Config,$Plan,[scriptblock]$Observe={Get-IacState $Config},[scriptblock]$Set={param($id,$cfg,$review) Set-IacResource $id $cfg $review},[switch]$DscBootstrapped)
    $state=& $Observe
    if ($DscBootstrapped) {
        if ($state.dsc.version -ne $Config.dscVersion) { throw 'DSC bootstrap does not match its pin.' }
        $state.dsc=$Plan.state.dsc
    }
    if (-not (Test-IacPlan $Plan $Config $state)) { throw 'Reviewed plan is stale or modified. Generate and review a fresh plan.' }
    if (@($Plan.blockers).Count) { throw ('Plan is blocked: '+($Plan.blockers -join '; ')) }
    $changed=@()
    foreach ($id in $script:ResourceOrder) {
        if ($id -in $Plan.changes -and -not ($DscBootstrapped -and $id -eq 'dsc')) {
            $watch=[Diagnostics.Stopwatch]::StartNew()
            try {
                & $Set $id $Config $Plan
                $after=& $Observe
                $converged=$false
                if ($id -in @('python','ollama','dsc')) { $converged=($after[$id].version -eq $Config[$id+'Version']) }
                else { $converged=[bool]$after[$id].present }
                if (-not $converged) { throw ('Resource '+$id+' did not converge; dependent changes are stopped.') }
                $changed+=$id
                Write-IacEvent $Config $id 'applied' $watch.Elapsed.TotalSeconds
            }
            catch { Write-IacEvent $Config $id 'failed' $watch.Elapsed.TotalSeconds; throw }
        }
    }
    return @{changed=@($changed)}
}

function Test-IacDeployment {
    <#
.SYNOPSIS
Check desired state without requiring a free port for an already-running managed GUI.
#>
    param($Config)
    $state=Get-IacState $Config;$state.portFree=$true
    $plan=Get-IacPlan -Config $Config -State $state
    return @{inDesiredState=(@($plan.changes).Count -eq 0 -and @($plan.blockers).Count -eq 0 -and $state.model.present);changes=@($plan.changes);blockers=@($plan.blockers);warnings=@($plan.warnings)}
}

function Invoke-IacApply {
    <#
.SYNOPSIS
Bootstrap pinned DSC only after plan validation, then delegate mutation to its resource.
#>
    param($Plan,$Config)
    $principal=[Security.Principal.WindowsPrincipal]::new([Security.Principal.WindowsIdentity]::GetCurrent())
    if ($principal.IsInRole([Security.Principal.WindowsBuiltInRole]::Administrator)) { throw 'Run infrastructure as the normal user, without elevation.' }
    if (-not [Environment]::Is64BitProcess) { throw 'Windows x64 PowerShell is required.' }
    $state=Get-IacState $Config
    if (-not (Test-IacPlan $Plan $Config $state)) { throw 'Reviewed plan is stale or modified.' }
    if (@($Plan.blockers).Count) { throw ($Plan.blockers -join '; ') }
    $env:AGENTIX_IAC_OPERATION=[guid]::NewGuid().ToString('N')
    if ($state.dsc.version -eq 'missing') { Set-IacResource 'dsc' $Config $Plan;Write-IacEvent $Config 'dsc' 'bootstrapped' 0 }
    $paths=Get-IacPaths $Config
    $savedPath=$env:PATH
    Push-Location $script:InfraRoot
    try {
        $env:PATH=$script:InfraRoot+';'+$env:PATH
        $env:AGENTIX_IAC_REVIEW=ConvertTo-Json -InputObject $Plan -Depth 60 -Compress
        Invoke-IacProcess $paths.dsc @('config','set','--file',(Join-Path $script:InfraRoot 'configuration.dsc.json')) | Write-Output
    } finally { Pop-Location; $env:PATH=$savedPath;Remove-Item Env:AGENTIX_IAC_REVIEW -ErrorAction SilentlyContinue }
    $result=Test-IacDeployment $Config
    if (-not $result.inDesiredState) { throw ('Convergence incomplete: '+(ConvertTo-Json $result -Compress)) }
}

function Start-IacApplication {
    <#
.SYNOPSIS
Manually launch GUI/CLI with managed Python after validating prerequisites.
#>
    param($Config,[ValidateSet('Gui','Cli')][string]$Mode,[scriptblock]$Run={
        param($Executable,$Entry)
        & $Executable $Entry
        if ($LASTEXITCODE -ne 0) { throw ('Application exited with code '+$LASTEXITCODE) }
    })
    $test=Test-IacDeployment $Config
    if (-not $test.inDesiredState) { throw 'Managed prerequisites have drifted. Run Test, then review a new Plan before Apply.' }
    $state=Get-IacState $Config
    if ($Mode -eq 'Gui' -and -not $state.portFree) { throw 'Configured GUI port is occupied; no process will be stopped.' }
    $paths=Get-IacPaths $Config
    $variables=@('OLLAMA_MODEL','OLLAMA_BASE_URL','AGENTIX_SERVER_PORT','AGENTIX_OPEN_BROWSER','AGENTIX_TOOLS_ROOT')
    $saved=@{};foreach ($name in $variables) { $saved[$name]=[Environment]::GetEnvironmentVariable($name,'Process') }
    try {
        $env:OLLAMA_MODEL=$Config.model;$env:OLLAMA_BASE_URL=$Config.ollamaUrl
        $env:AGENTIX_SERVER_PORT=[string]$Config.port;$env:AGENTIX_OPEN_BROWSER=([string]$Config.openBrowser).ToLowerInvariant();$env:AGENTIX_TOOLS_ROOT=$paths.tools
        $entry='app.py';if ($Mode -eq 'Cli') {$entry='main.py'}
        & $Run (Join-Path $paths.environment 'Scripts\python.exe') (Join-Path $script:ProjectRoot $entry)
    } finally { foreach ($name in $saved.Keys) { if ($null -eq $saved[$name]) { Remove-Item -LiteralPath ('Env:'+$name) -ErrorAction SilentlyContinue } else { [Environment]::SetEnvironmentVariable($name,$saved[$name],'Process') } } }

}

Export-ModuleMember -Function *-Iac*
