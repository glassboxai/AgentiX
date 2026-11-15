# Reference for tests/unit/test_file_logging.py

Process logging must also persist to a bounded file under the data directory.

Every handler these tests install is flushed, closed and detached again, and no
handler may outlive the test that created it. Handlers owned by pytest or other
libraries are preserved. All destinations are pytest temporary directories.

Source fingerprint: 1da3378027e338d598a71167cc9bf5695c73a0f3af0d1fe09ac7020f2ce90ed0

This reference is generated from maintained source without imports or execution. Assigned values are intentionally omitted. Runtime-dependent types are explicit; the enclosing docstring defines the behavioral contract. See [architecture](../ARCHITECTURE_QUALITY.md) for manually reviewed responsibility and dependency decisions.

## Classes and callables

### test_configure_process_installs_single_rotating_file_handler

A bounded agentix.log appears once under data/logs and receives events.

Kind: callable. Declared return: Not declared / class. Source line: 17.

### test_release_closes_only_the_handlers_it_owns

Cleanup detaches and closes owned handlers without touching foreign ones.

Kind: callable. Declared return: Not declared / class. Source line: 48.

### test_installed_handler_keeps_its_first_destination_when_home_changes

A later AGENTIX_HOME never re-points an already installed handler.

Kind: callable. Declared return: Not declared / class. Source line: 77.

### test_session_storage_stays_inside_the_pytest_temporary_root

The session fixture resolves storage under the pytest temporary root.

Kind: callable. Declared return: Not declared / class. Source line: 104.

## Variables and parameters

| Scope | Name | Role and meaning | Type | Lifetime | Writes |
| --- | --- | --- | --- | --- | --- |
| module | logging | Imported dependency for logging in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 8 |
| module | Path | Imported dependency for Path in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 9 |
| module | agentix_file_handlers | Imported dependency for agentix file handlers in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 11 |
| module | release_agentix_file_handlers | Imported dependency for release agentix file handlers in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 11 |
| module | configure_process | Imported dependency for configure process in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 13 |
| module | data_directory | Imported dependency for data directory in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 14 |
| test_configure_process_installs_single_rotating_file_handler | tmp_path | Parameter for tmp path in test_configure_process_installs_single_rotating_file_handler; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 17 |
| test_configure_process_installs_single_rotating_file_handler | monkeypatch | Parameter for monkeypatch in test_configure_process_installs_single_rotating_file_handler; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 17 |
| test_configure_process_installs_single_rotating_file_handler | root | Explicit root directory against which named paths are resolved. | Return type of getLogger; see its callable contract | Enclosing invocation or class/instance lifetime | 20 |
| test_configure_process_installs_single_rotating_file_handler | baseline | Local binding for baseline in test_configure_process_installs_single_rotating_file_handler; use the enclosing contract and type below. | Return type of agentix_file_handlers; see its callable contract | Enclosing invocation or class/instance lifetime | 21 |
| test_configure_process_installs_single_rotating_file_handler | handler | Loop item for handler in test_configure_process_installs_single_rotating_file_handler; use the enclosing contract and type below. | Element of the declared iterable | Enclosing invocation or class/instance lifetime | 22, 29, 43 |
| test_configure_process_installs_single_rotating_file_handler | handlers | Local binding for handlers in test_configure_process_installs_single_rotating_file_handler; use the enclosing contract and type below. | Return type of agentix_file_handlers; see its callable contract | Enclosing invocation or class/instance lifetime | 27 |
| test_configure_process_installs_single_rotating_file_handler | item | Loop item for item in test_configure_process_installs_single_rotating_file_handler; use the enclosing contract and type below. | Element of the declared iterable | Enclosing invocation or class/instance lifetime | 34 |
| test_configure_process_installs_single_rotating_file_handler | log_path | Local binding for log path in test_configure_process_installs_single_rotating_file_handler; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 36 |
| test_configure_process_installs_single_rotating_file_handler.comprehension_41 | item | Comprehension item for item in test_configure_process_installs_single_rotating_file_handler.comprehension_41; use the enclosing contract and type below. | Element of the declared iterable | This comprehension only; does not leak into its enclosing scope | 41 |
| test_release_closes_only_the_handlers_it_owns | tmp_path | Parameter for tmp path in test_release_closes_only_the_handlers_it_owns; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 48 |
| test_release_closes_only_the_handlers_it_owns | monkeypatch | Parameter for monkeypatch in test_release_closes_only_the_handlers_it_owns; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 48 |
| test_release_closes_only_the_handlers_it_owns | root | Explicit root directory against which named paths are resolved. | Return type of getLogger; see its callable contract | Enclosing invocation or class/instance lifetime | 51 |
| test_release_closes_only_the_handlers_it_owns | detached | Local binding for detached in test_release_closes_only_the_handlers_it_owns; use the enclosing contract and type below. | Return type of agentix_file_handlers; see its callable contract | Enclosing invocation or class/instance lifetime | 52 |
| test_release_closes_only_the_handlers_it_owns | handler | Loop item for handler in test_release_closes_only_the_handlers_it_owns; use the enclosing contract and type below. | Element of the declared iterable | Enclosing invocation or class/instance lifetime | 53, 72 |
| test_release_closes_only_the_handlers_it_owns | foreign | Local binding for foreign in test_release_closes_only_the_handlers_it_owns; use the enclosing contract and type below. | Return type of StreamHandler; see its callable contract | Enclosing invocation or class/instance lifetime | 55 |
| test_release_closes_only_the_handlers_it_owns | owned | Local binding for owned in test_release_closes_only_the_handlers_it_owns; use the enclosing contract and type below. | Return type of agentix_file_handlers; see its callable contract | Enclosing invocation or class/instance lifetime | 59 |
| test_release_closes_only_the_handlers_it_owns | released | Local binding for released in test_release_closes_only_the_handlers_it_owns; use the enclosing contract and type below. | Return type of release_agentix_file_handlers; see its callable contract | Enclosing invocation or class/instance lifetime | 61 |
| test_installed_handler_keeps_its_first_destination_when_home_changes | tmp_path | Parameter for tmp path in test_installed_handler_keeps_its_first_destination_when_home_changes; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 77 |
| test_installed_handler_keeps_its_first_destination_when_home_changes | monkeypatch | Parameter for monkeypatch in test_installed_handler_keeps_its_first_destination_when_home_changes; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 77 |
| test_installed_handler_keeps_its_first_destination_when_home_changes | first | Local binding for first in test_installed_handler_keeps_its_first_destination_when_home_changes; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 79 |
| test_installed_handler_keeps_its_first_destination_when_home_changes | second | Local binding for second in test_installed_handler_keeps_its_first_destination_when_home_changes; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 80 |
| test_installed_handler_keeps_its_first_destination_when_home_changes | detached | Local binding for detached in test_installed_handler_keeps_its_first_destination_when_home_changes; use the enclosing contract and type below. | Return type of agentix_file_handlers; see its callable contract | Enclosing invocation or class/instance lifetime | 82 |
| test_installed_handler_keeps_its_first_destination_when_home_changes | handler | Loop item for handler in test_installed_handler_keeps_its_first_destination_when_home_changes; use the enclosing contract and type below. | Element of the declared iterable | Enclosing invocation or class/instance lifetime | 83, 99 |
| test_installed_handler_keeps_its_first_destination_when_home_changes | installed | Typed binding for installed in test_installed_handler_keeps_its_first_destination_when_home_changes; use the enclosing contract and type below. | list[logging.Handler] | Enclosing invocation or class/instance lifetime | 85, 88 |
| test_installed_handler_keeps_its_first_destination_when_home_changes | original | Local binding for original in test_installed_handler_keeps_its_first_destination_when_home_changes; use the enclosing contract and type below. | Return type of resolve; see its callable contract | Enclosing invocation or class/instance lifetime | 90 |
| test_session_storage_stays_inside_the_pytest_temporary_root | tmp_path_factory | Parameter for tmp path factory in test_session_storage_stays_inside_the_pytest_temporary_root; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 104 |
| test_session_storage_stays_inside_the_pytest_temporary_root | authorized | Local binding for authorized in test_session_storage_stays_inside_the_pytest_temporary_root; use the enclosing contract and type below. | Return type of resolve; see its callable contract | Enclosing invocation or class/instance lifetime | 106 |
| test_session_storage_stays_inside_the_pytest_temporary_root | resolved | Local binding for resolved in test_session_storage_stays_inside_the_pytest_temporary_root; use the enclosing contract and type below. | Return type of resolve; see its callable contract | Enclosing invocation or class/instance lifetime | 107 |
| test_session_storage_stays_inside_the_pytest_temporary_root.comprehension_109 | left | Comprehension item for left in test_session_storage_stays_inside_the_pytest_temporary_root.comprehension_109; use the enclosing contract and type below. | Element of the declared iterable | This comprehension only; does not leak into its enclosing scope | 111 |
| test_session_storage_stays_inside_the_pytest_temporary_root.comprehension_109 | right | Comprehension item for right in test_session_storage_stays_inside_the_pytest_temporary_root.comprehension_109; use the enclosing contract and type below. | Element of the declared iterable | This comprehension only; does not leak into its enclosing scope | 111 |
