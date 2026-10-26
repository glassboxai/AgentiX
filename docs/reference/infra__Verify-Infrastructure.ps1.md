# infra/Verify-Infrastructure.ps1

Source SHA-256: 573aefb61d6b93f5d28919e24be584a1b9e690a45e65f6e4e559456e4e0b872b

Statically validate maintained PowerShell syntax and security-sensitive command usage.

## Functions

## Scoped variables

Assigned values are excluded. Parameter/temporary meaning follows the owning function contract; process and script scopes are explicit.

| Name | Scope | Static type | Lifecycle |
| --- | --- | --- | --- |
| ast | module | System.Object | Enclosing invocation, unless explicitly process/environment or script scoped. |
| command | module | System.Object | Enclosing invocation, unless explicitly process/environment or script scoped. |
| count | module | System.Object | Enclosing invocation, unless explicitly process/environment or script scoped. |
| ErrorActionPreference | module | System.Object | Enclosing invocation, unless explicitly process/environment or script scoped. |
| file | module | System.Object | Enclosing invocation, unless explicitly process/environment or script scoped. |
| item | module | System.Object | Enclosing invocation, unless explicitly process/environment or script scoped. |
| node | module | System.Object | Enclosing invocation, unless explicitly process/environment or script scoped. |
| null | module | System.Object | Enclosing invocation, unless explicitly process/environment or script scoped. |
| parseErrors | module | System.Object | Enclosing invocation, unless explicitly process/environment or script scoped. |
| PSScriptRoot | module | System.Object | Enclosing invocation, unless explicitly process/environment or script scoped. |
| tokens | module | System.Object | Enclosing invocation, unless explicitly process/environment or script scoped. |
| true | module | System.Object | Enclosing invocation, unless explicitly process/environment or script scoped. |
