# Reference for tests/test_application_browser_policy.py

Host browser egress policy for generated native application verification.

Source fingerprint: b0d51569f7ca468d812206da8f80a96c65aec67e6d773a238ca633aa4b25fee6

This reference is generated from maintained source without imports or execution. Assigned values are intentionally omitted. Runtime-dependent types are explicit; the enclosing docstring defines the behavioral contract. See [architecture](../ARCHITECTURE_QUALITY.md) for manually reviewed responsibility and dependency decisions.

## Classes and callables

### test_browser_requests_stay_on_the_owned_origin

Catch navigation/request escape from the supervisor's reviewed application origin.

Kind: callable. Declared return: Not declared / class. Source line: 18.

## Variables and parameters

| Scope | Name | Role and meaning | Type | Lifetime | Writes |
| --- | --- | --- | --- | --- | --- |
| module | pytest | Imported dependency for pytest in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 3 |
| test_browser_requests_stay_on_the_owned_origin | url | Parameter for url in test_browser_requests_stay_on_the_owned_origin; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 18 |
| test_browser_requests_stay_on_the_owned_origin | allowed | Parameter for allowed in test_browser_requests_stay_on_the_owned_origin; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 18 |
| test_browser_requests_stay_on_the_owned_origin | browser_origin_allowed | Imported dependency for browser origin allowed in test_browser_requests_stay_on_the_owned_origin; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 20 |
