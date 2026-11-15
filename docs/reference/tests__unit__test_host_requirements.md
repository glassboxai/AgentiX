# Reference for tests/unit/test_host_requirements.py

Regression tests for explicit host-owned dependency recovery.

Source fingerprint: e845aeef7c9d9aa39086b8585a05eee90a0a84159102189484381a95cc90923e

This reference is generated from maintained source without imports or execution. Assigned values are intentionally omitted. Runtime-dependent types are explicit; the enclosing docstring defines the behavioral contract. See [architecture](../ARCHITECTURE_QUALITY.md) for manually reviewed responsibility and dependency decisions.

## Classes and callables

### test_missing_registered_requirement_has_fixed_review_details

A missing requirement exposes only host-maintained consent details.

Kind: callable. Declared return: Not declared / class. Source line: 6.

### test_install_runs_only_registered_command_and_rechecks

An explicit install uses the active Python and accepts only a verified result.

Kind: callable. Declared return: Not declared / class. Source line: 20.

### test_install_runs_only_registered_command_and_rechecks.runner

Record the exact immutable host command and emulate browser installation.

Kind: callable. Declared return: Not declared / class. Source line: 27.

### test_unknown_or_unsatisfied_requirement_cannot_be_installed

No caller can turn the recovery boundary into arbitrary package execution.

Kind: callable. Declared return: Not declared / class. Source line: 43.

### test_installer_environment_excludes_package_manager_and_proxy_configuration

A reviewed browser download cannot inherit arbitrary package sources or targets.

Kind: callable. Declared return: Not declared / class. Source line: 60.

## Variables and parameters

| Scope | Name | Role and meaning | Type | Lifetime | Writes |
| --- | --- | --- | --- | --- | --- |
| module | pytest | Imported dependency for pytest in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 3 |
| test_missing_registered_requirement_has_fixed_review_details | tmp_path | Parameter for tmp path in test_missing_registered_requirement_has_fixed_review_details; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 6 |
| test_missing_registered_requirement_has_fixed_review_details | HostRequirements | Imported dependency for HostRequirements in test_missing_registered_requirement_has_fixed_review_details; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 8 |
| test_missing_registered_requirement_has_fixed_review_details | service | Local binding for service in test_missing_registered_requirement_has_fixed_review_details; use the enclosing contract and type below. | Return type of HostRequirements; see its callable contract | Enclosing invocation or class/instance lifetime | 10 |
| test_missing_registered_requirement_has_fixed_review_details | requirement | Local binding for requirement in test_missing_registered_requirement_has_fixed_review_details; use the enclosing contract and type below. | Return type of missing; see its callable contract | Enclosing invocation or class/instance lifetime | 12 |
| test_install_runs_only_registered_command_and_rechecks | tmp_path | Parameter for tmp path in test_install_runs_only_registered_command_and_rechecks; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 20 |
| test_install_runs_only_registered_command_and_rechecks | HostRequirements | Imported dependency for HostRequirements in test_install_runs_only_registered_command_and_rechecks; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 22 |
| test_install_runs_only_registered_command_and_rechecks | browser | Local binding for browser in test_install_runs_only_registered_command_and_rechecks; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 24 |
| test_install_runs_only_registered_command_and_rechecks | seen | Local binding for seen in test_install_runs_only_registered_command_and_rechecks; use the enclosing contract and type below. | list | Enclosing invocation or class/instance lifetime | 25 |
| test_install_runs_only_registered_command_and_rechecks.runner | command | Parameter for command in test_install_runs_only_registered_command_and_rechecks.runner; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 27 |
| test_install_runs_only_registered_command_and_rechecks.runner | environment | Parameter for environment in test_install_runs_only_registered_command_and_rechecks.runner; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 27 |
| test_install_runs_only_registered_command_and_rechecks | service | Local binding for service in test_install_runs_only_registered_command_and_rechecks; use the enclosing contract and type below. | Return type of HostRequirements; see its callable contract | Enclosing invocation or class/instance lifetime | 32 |
| test_unknown_or_unsatisfied_requirement_cannot_be_installed | tmp_path | Parameter for tmp path in test_unknown_or_unsatisfied_requirement_cannot_be_installed; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 43 |
| test_unknown_or_unsatisfied_requirement_cannot_be_installed | HostRequirementInstallError | Imported dependency for HostRequirementInstallError in test_unknown_or_unsatisfied_requirement_cannot_be_installed; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 45 |
| test_unknown_or_unsatisfied_requirement_cannot_be_installed | HostRequirements | Imported dependency for HostRequirements in test_unknown_or_unsatisfied_requirement_cannot_be_installed; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 45 |
| test_unknown_or_unsatisfied_requirement_cannot_be_installed | calls | Local binding for calls in test_unknown_or_unsatisfied_requirement_cannot_be_installed; use the enclosing contract and type below. | list | Enclosing invocation or class/instance lifetime | 47 |
| test_unknown_or_unsatisfied_requirement_cannot_be_installed | service | Local binding for service in test_unknown_or_unsatisfied_requirement_cannot_be_installed; use the enclosing contract and type below. | Return type of HostRequirements; see its callable contract | Enclosing invocation or class/instance lifetime | 48 |
| test_unknown_or_unsatisfied_requirement_cannot_be_installed.lambda_50 | command | Callback parameter for command in test_unknown_or_unsatisfied_requirement_cannot_be_installed.lambda_50; use the enclosing contract and type below. | Defined by the enclosing callback contract | Enclosing invocation or class/instance lifetime | 50 |
| test_unknown_or_unsatisfied_requirement_cannot_be_installed.lambda_50 | environment | Callback parameter for environment in test_unknown_or_unsatisfied_requirement_cannot_be_installed.lambda_50; use the enclosing contract and type below. | Defined by the enclosing callback contract | Enclosing invocation or class/instance lifetime | 50 |
| test_installer_environment_excludes_package_manager_and_proxy_configuration | installer_environment | Imported dependency for installer environment in test_installer_environment_excludes_package_manager_and_proxy_configuration; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 62 |
| test_installer_environment_excludes_package_manager_and_proxy_configuration | environment | Local binding for environment in test_installer_environment_excludes_package_manager_and_proxy_configuration; use the enclosing contract and type below. | Return type of installer_environment; see its callable contract | Enclosing invocation or class/instance lifetime | 64 |
