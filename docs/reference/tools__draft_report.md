# Reference for tools/draft_report.py

Request a prose-only report draft from local Ollama and retain provenance.

This helper never invokes an agent, evaluates model output or writes production
code. Output is an explicitly unverified Markdown draft for human review.

Source fingerprint: a2fc79571c3aec3213b34fb0c686427dee83ad1ad7c5b5a6fed6674c6a0289f6

This reference is generated from maintained source without imports or execution. Assigned values are intentionally omitted. Runtime-dependent types are explicit; the enclosing docstring defines the behavioral contract. See [architecture](../ARCHITECTURE_QUALITY.md) for manually reviewed responsibility and dependency decisions.

## Classes and callables

### NoRedirects

Prevent a local endpoint from redirecting report evidence elsewhere.

Kind: class. Declared return: Not declared / class. Source line: 15.

### NoRedirects.redirect_request

Deny every redirect so local report evidence cannot leave loopback.

Kind: callable. Declared return: Not declared / class. Source line: 18.

### validate_endpoint

Accept HTTP loopback IP literals only, without credentials or URL extras.

Kind: callable. Declared return: Not declared / class. Source line: 23.

### draft

Return unverified model prose and provenance; propagate service errors.

Kind: callable. Declared return: Not declared / class. Source line: 44.

### main

Write report and provenance to explicitly supplied output paths.

Kind: callable. Declared return: Not declared / class. Source line: 81.

## Variables and parameters

| Scope | Name | Role and meaning | Type | Lifetime | Writes |
| --- | --- | --- | --- | --- | --- |
| module | argparse | Imported dependency for argparse in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 7 |
| module | ipaddress | Imported dependency for ipaddress in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 8 |
| module | json | Imported dependency for json in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 9 |
| module | Path | Imported dependency for Path in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 10 |
| module | urlparse | Imported dependency for urlparse in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 11 |
| module | HTTPRedirectHandler | Imported dependency for HTTPRedirectHandler in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 12 |
| module | ProxyHandler | Imported dependency for ProxyHandler in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 12 |
| module | Request | Imported dependency for Request in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 12 |
| module | build_opener | Imported dependency for build opener in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 12 |
| NoRedirects.redirect_request | self | Owning instance; its attributes retain state for the instance lifetime. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 18 |
| NoRedirects.redirect_request | req | Parameter for req in NoRedirects.redirect_request; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 18 |
| NoRedirects.redirect_request | fp | Parameter for fp in NoRedirects.redirect_request; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 18 |
| NoRedirects.redirect_request | code | Source snapshot passed through approval, syntax checks and isolated staging. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 18 |
| NoRedirects.redirect_request | msg | Parameter for msg in NoRedirects.redirect_request; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 18 |
| NoRedirects.redirect_request | headers | Parameter for headers in NoRedirects.redirect_request; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 18 |
| NoRedirects.redirect_request | newurl | Parameter for newurl in NoRedirects.redirect_request; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 18 |
| validate_endpoint | endpoint | Parameter for endpoint in validate_endpoint; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 23 |
| validate_endpoint | parsed | Local binding for parsed in validate_endpoint; use the enclosing contract and type below. | Return type of urlparse; see its callable contract | Enclosing invocation or class/instance lifetime | 25 |
| validate_endpoint | address | Local binding for address in validate_endpoint; use the enclosing contract and type below. | Return type of ip_address; see its callable contract | Enclosing invocation or class/instance lifetime | 27 |
| validate_endpoint | valid | Local binding for valid in validate_endpoint; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 28, 30 |
| draft | evidence | Parameter for evidence in draft; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 44 |
| draft | model | Parameter for model in draft; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 44 |
| draft | endpoint | Parameter for endpoint in draft; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 44, 46 |
| draft | prompt | Local binding for prompt in draft; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 47 |
| draft | payload | Local binding for payload in draft; use the enclosing contract and type below. | dict | Enclosing invocation or class/instance lifetime | 54 |
| draft | request | Local binding for request in draft; use the enclosing contract and type below. | Return type of Request; see its callable contract | Enclosing invocation or class/instance lifetime | 61 |
| draft | opener | Local binding for opener in draft; use the enclosing contract and type below. | Return type of build_opener; see its callable contract | Enclosing invocation or class/instance lifetime | 68 |
| draft | response | Bounded response text to render or validate; it is not executable code. | Return type of open; see its callable contract | Context-manager block; exit invokes its cleanup protocol | 69 |
| draft | data | Local binding for data in draft; use the enclosing contract and type below. | Return type of loads; see its callable contract | Enclosing invocation or class/instance lifetime | 70 |
| main | parser | Local binding for parser in main; use the enclosing contract and type below. | Return type of ArgumentParser; see its callable contract | Enclosing invocation or class/instance lifetime | 83 |
| main | args | Local binding for args in main; use the enclosing contract and type below. | Return type of parse_args; see its callable contract | Enclosing invocation or class/instance lifetime | 88 |
| main | evidence | Local binding for evidence in main; use the enclosing contract and type below. | Return type of loads; see its callable contract | Enclosing invocation or class/instance lifetime | 89 |
| main | text | Local binding for text in main; use the enclosing contract and type below. | Return type of draft; see its callable contract | Enclosing invocation or class/instance lifetime | 90 |
| main | provenance | Local binding for provenance in main; use the enclosing contract and type below. | Return type of draft; see its callable contract | Enclosing invocation or class/instance lifetime | 90 |
